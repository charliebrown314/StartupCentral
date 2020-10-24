"""
116commandcenter.server
This code is partially written and produced by Jacob Snyderman
part of this code is repurposed code by github user Vuka951
for the use of CSE116 at the University at Buffalo
Copyright 2020 Jacob Snyderman (jacobsny@buffalo.edu)
 This work is licensed under the Creative Commons
 Attribution-NonCommercial-ShareAlike 4.0 International License.
 To view a copy of this license, visit
 http://creativecommons.org/licenses/by-nc-sa/4.0/.
"""
import set_var
from auth_decorator import login_required, requires_access_level
from backend_functionality.Course import Course
from datetime import timedelta
from flask import Flask, redirect, url_for, session, request
from authlib.integrations.flask_client import OAuth
import json
import os


class User:
    def __init__(self):
        self.name = None
        self.is_authenticated = False


class Server:
    def __init__(self):
        set_var.main()
        self.app = Flask(__name__)
        self.app.secret_key = os.getenv("APP_SECRET_KEY")
        self.app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
        self.app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)
        self.oauth = OAuth(self.app)
        self.google = self.oauth.register(
            name='google',
            client_id=os.getenv("GOOGLE_CLIENT_ID"),
            client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
            access_token_url='https://accounts.google.com/o/oauth2/token',
            access_token_params=None,
            authorize_url='https://accounts.google.com/o/oauth2/auth',
            authorize_params=None,
            api_base_url='https://www.googleapis.com/oauth2/v1/',
            userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
            # This is only needed if using openId to fetch user info
            client_kwargs={'scope': 'openid email profile'},
        )
 
        self.secretKey = "ThisIsTheMostSecretPasswordEver"

        @self.app.route('/')
        def hello_world():
            # This is where the normal homepage is
            # It should have a login button that turns to a logout button when logged in
            # It should display what email they are logged in as when they are logged in
            try:
                email = dict(session)['profile']['email']
            except:
                email = "no one yet"
            return f'Hello, you are logged in as {email}!'

        @self.app.route('/login')
        def login():
            # This is the login page, it isn't actually a page it is a redirect for
            # google login, please use /login as the redirect when someone presses
            # the login button
            google = self.oauth.create_client('google')  # create the google oauth client
            redirect_uri = url_for('authorize', _external=True)
            return google.authorize_redirect(redirect_uri)

        @self.app.route('/authorize')
        def authorize():
            # Login redirects here to validate their google token and gets them logged
            # into our server, it then redirects back to the page with their designated access_level
            google = self.oauth.create_client('google')  # create the google oauth client
            token = google.authorize_access_token()  # Access token from google (needed to get user info)
            resp = google.get('userinfo')  # userinfo contains email the profile info
            user_info = resp.json()
            print(user_info["email"] + " logged in on the server")
            session['profile'] = user_info
            email = user_info["email"]
            if email.endswith('@buffalo.edu') and ubit not in self.COURSE.DB.get_instructors() and ubit not in {k[2]: k for k in self.COURSE.get_roster()}:
                print([user_info["first_name"], user_info["family_name"], ubit])
                print(ubit + " is being added to the student roster")
                self.COURSE.add_student([user_info["first_name"], user_info["family_name"], ubit])
            al = self.COURSE.get_level(email)
            session['profile']['access_level'] = al
            session.permanent = True  # make the session permanent so it keeps existing after browser gets closed
            if al == 3:
                return redirect('/admin')
            elif al == 2:
                return redirect('/instructor')
            elif al == 1:
                return redirect('/student')
            else:
                return redirect('/')

        @self.app.route('/logout')
        def logout():
            # self explanatory call this to log someone out of their session
            for key in list(session.keys()):
                session.pop(key)
            return redirect('/')

        @self.app.route('/add_instructor')
        @login_required
        @requires_access_level(2)
        def add_inst():
            # add an instructor individually to the database
            ubit = request.args.get('instructor_ubit')
            name = request.args.get('instructor_name')
            ubit_approving = dict(session)['profile']['email']
            ubit_approving = ubit_approving[:ubit_approving.index("@")]
            self.COURSE.add_instructor(ubit_approving, [ubit, name])
            self.COURSE.log('add_instructor', json.dumps({'ubit': ubit_approving, 'data': {'instructor_ubit': ubit, 'instructor_name': name}}))
            return f'{name} with ubit={ubit} has been added'

        @self.app.route('/add_instructors', methods=['POST'])
        @login_required
        @requires_access_level(3)
        def add_instructors():
            # data should be a json dictionary mapping ubit of instructor to full name
            json_data = request.get_json()
            req_data = json.loads(json_data)
            ubit_approving = dict(session)['profile']['email']
            ubit_approving = ubit_approving[:ubit_approving.index("@")]
            for ubit in req_data:
                self.COURSE.add_instructor(ubit_approving, [ubit, req_data[ubit]])
            self.COURSE.log('add_instructors', json.dumps({'ubit': ubit_approving, 'data': json_data}))
            return 'Hopefully every instructor is added now as long as you did not screw up the POST\n' + json_data

        @self.app.route('/get_roster')
        @login_required
        @requires_access_level(2)
        def get_roster():
            # get raw roster for the class of all students
            return json.dumps(self.COURSE.get_roster())

        @self.app.route('/get_gradebook')
        @login_required
        @requires_access_level(2)
        def get_grades():
            # get the list of all student with their current up to date grade for everything
            ubit_approving = dict(session)['profile']['email']
            ubit_approving = ubit_approving[:ubit_approving.index("@")]
            return json.dumps(self.COURSE.get_gradebook())

        @self.app.route('/get_student')
        @login_required
        @requires_access_level(2)
        def get_student():
            # instructor requesting to view a student
            ubit_requested = request.args.get('ubit')
            ubit_approving = dict(session)['profile']['email']
            ubit_approving = ubit_approving[:ubit_approving.index("@")]
            return json.dumps(self.COURSE.get_student(ubit_approving,ubit_requested))

        @self.app.route('/remove_student')
        @login_required
        @requires_access_level(3)
        def remove_student():
            # admin requesting to remove a student
            ubit_requested = request.args.get('ubit')
            ubit_approving = dict(session)['profile']['email']
            ubit_approving = ubit_approving[:ubit_approving.index("@")]
            self.COURSE.log('remove_student', json.dumps({'ubit': ubit_approving, 'data': {'student_ubit': ubit_requested}}))
            return json.dumps(self.COURSE.DB.remove_student(ubit_approving, ubit_requested))

        @self.app.route('/get_self')
        @login_required
        @requires_access_level(1)
        def get_self():
            # meant for a student to request their own grades
            ubit_approving = dict(session)['profile']['email']
            ubit_approving = ubit_approving[:ubit_approving.index("@")]
            return json.dumps(self.COURSE.get_student(ubit_approving, ubit_approving))

        @self.app.route('/grade_assignment')
        @login_required
        @requires_access_level(2)
        def grade_assignment():
            # grade an assignment
            ubit_approving = dict(session)['profile']['email']
            ubit_approving = ubit_approving[:ubit_approving.index("@")]
            ubit_student = request.args.get('student_ubit')
            assignment = request.args.get('assignment')
            grade = request.args.get('grade')
            feedback = request.args.get('feedback')
            self.COURSE.grade_assignment([ubit_student,assignment,grade,ubit_approving,feedback])
            data = {'ubit_student': ubit_student, 'assignment': assignment, 'grade': grade, 'feedback':feedback}
            self.COURSE.log('grade_assignment', json.dumps({'ubit': ubit_approving, 'data': data}))
            return json.dumps([ubit_student,assignment,grade,ubit_approving,feedback])

        @self.app.route('/grade_checkbox')
        @login_required
        @requires_access_level(2)
        def grade_checkbox():
            # grade a checkbox
            ubit_approving = dict(session)['profile']['email']
            ubit_approving = ubit_approving[:ubit_approving.index("@")]
            ubit_student = request.args.get('student_ubit')
            assignment = request.args.get('assignment')
            grade = request.args.get('grade')
            feedback = request.args.get('feedback')
            self.COURSE.grade_checkbox([ubit_student,assignment,grade,ubit_approving,feedback])
            data = {'ubit_student': ubit_student, 'assignment': assignment, 'grade': grade, 'feedback': feedback}
            self.COURSE.log('grade_checkbox', json.dumps({'ubit': ubit_approving, 'data': data}))
            return json.dumps([ubit_student, assignment, grade, ubit_approving, feedback])

        @self.app.route('/review_request')
        @login_required
        @requires_access_level(1)
        def review_request():
            # student requesting a checkbox or assignment to be reviewed
            ubit_approving = dict(session)['profile']['email']
            ubit_approving = ubit_approving[:ubit_approving.index("@")]
            material = request.args.get('material')
            self.COURSE.review_request(ubit_approving, material)
            self.COURSE.log('review_request', json.dumps({'ubit': ubit_approving, 'data': {'material':material}}))
            return redirect('/get_self')

        @self.app.route('/review_in_progress')
        @login_required
        @requires_access_level(2)
        def review_in_progress():
            # a ta requesting the system for something to grade
            ubit_approving = dict(session)['profile']['email']
            ubit_approving = ubit_approving[:ubit_approving.index("@")]
            material = request.args.get('material')
            ubit_student = request.args.get('ubit')
            self.COURSE.log('review_in_progress', json.dumps({'ubit': ubit_approving, 'data': {'student_ubit':ubit_student,'material': material}}))
            self.COURSE.review_in_progress(ubit_approving, ubit_student, material)
            return 'review in progress now'

        @self.app.route('/review_stop_progress')
        @login_required
        @requires_access_level(2)
        def review_stop_progress():
            # a ta requesting the system for something to grade
            ubit_approving = dict(session)['profile']['email']
            ubit_approving = ubit_approving[:ubit_approving.index("@")]
            material = request.args.get('material')
            ubit_student = request.args.get('ubit')
            self.COURSE.log('review_stop_progress', json.dumps({'ubit': ubit_approving, 'data': {'student_ubit':ubit_student,'material': material}}))
            self.COURSE.review_stop_progress(ubit_approving, ubit_student, material)
            return 'review stopped progress now'

        @self.app.route('/get_review_queue')
        @login_required
        @requires_access_level(2)
        def get_review_queue():
            # request the entire review queue to look at
            return json.dumps(self.COURSE.get_review_queue(), default=str)

        @self.app.route('/export_data')
        @login_required
        @requires_access_level(3)
        def export_data():
            # request the entirety of databases data
            data = self.COURSE.DB.export_data()
            return json.dumps(data, default=str)

    def start(self):
        print("Server Running On Port: 8080")
        self.app.run(host="localhost", port=8080)

    def stop(self):
        print("Server Stopping on Port: 8080")
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()


if __name__ == '__main__':
    server = Server()
    server.start()
