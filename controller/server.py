"""
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

from datetime import datetime, timedelta
from flask import Flask, redirect, url_for, session, request
from authlib.integrations.flask_client import OAuth
import json
import os

from model.Projects import Projects


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

        self.projects : Projects = Projects("e12cf059-45c3-4649-937a-3a6c345029dd", "us-east1", "StartupCentral", "JacobIsTheBest", "SocialMedaDB")
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
            print(user_info)
            email = user_info["email"]
            fname = user_info["given_name"]
            lname = user_info["family_name"]
            #TODO add to DB but first check for existence

            result = self.projects.DB.getUser(email)

            if not result:
                self.projects.addDev(fname, datetime.now(),lname,email)

            session.permanent = True  # make the session permanent so it keeps existing after browser gets closed
            return redirect('/')

        @self.app.route('/logout')
        def logout():
            # self explanatory call this to log someone out of their session
            for key in list(session.keys()):
                session.pop(key)
            return redirect('/')

        @login_required
        @self.app.route("/getProfile", methods=["POST"])
        def getProfile():

            request_data = request.get_json()

            userID = request_data["userID"]

            return json.dumps(self.Projects.DB.getUser(userID))

        @login_required
        @self.app.route("/getProject", methods=["POST"])
        def getProject():

            request_data = request.get_json()
            projectName = request_data["projectName"]

            return json.dumps(self.Projects.DB.getProject(projectName))

        @login_required
        @self.app.route("/getDevRecommendations", methods=["POST"])
        def getDevRecommendations():
            request_data = request.get_json()
            tags = request_data["tags"]

            return json.dumps(self.Projects.DB.getDevRecommendations(tags))

        @login_required
        @self.app.route("/getProjRecommendations", methods=["POST"])
        def getProjRecommendations():

            request_data = request.get_json()

            projName = request_data["projName"]

            return json.dumps(self.Projects.proj_recommendations(projName))

        @login_required
        @self.app.rout("/searchProject", methods=["POST"])
        def searchProjects():

            request_data = request.get_json()

        @login_required
        @self.app.route("/getProjNames", methods=["GET", "POST"])
        def getProjNames():
            return json.dumps(self.Projects.DB.getProjectNames())

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
