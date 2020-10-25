function post(endpt, args, takesArgs, callback) {
  const http = new XMLHttpRequest();
  if (takesArgs) {
    const data = new FormData();
    for (let k in args) {
      data.append(k, args[k]);
    }
    http.open("POST", endpt);
    http.send(data)
  } else {
    http.open("POST", endpt);
    http.send();
  }

  http.onreadystatechange = function() {
    if (http.readyState === 4 && http.status === 200) {
      let response = http.responseText;
      console.log(response);
      let json = JSON.parse(http.response);
      callback(json);
    }

  }
}

function get(endpt, callback) {
  const http = new XMLHttpRequest();

  http.open("GET", endpt, true);
  http.send();

  http.onreadystatechange = function() {
    if (http.readyState === 4 && http.status === 200) {
      var response = http.responseText;
      callback(response);
    }

  }
}

function toggleLightMode(){
  document.body.classList.toggle('light-mode')
  for (tag of document.getElementsByClassName('tag')){
    tag.classList.toggle('light-mode')
  }
}

var currProject = {"name" : "Startup Central",
  "desc" : 'The applications custom maps projects and devs to a fit algorithm as to make recommendations for projects that should get in touch with each other to share in their creative process and to utilize like-minded projects for feedback.',
  'img_URL': "../static/assets/oop.jpg",
  'tags': ['#Python', '#HTML' , '#CSS', '#SCSS', '#JS'],
  'collabs': ['Joseph Brown', 'Nick MacCrae', 'Jacob Snyderman', 'Jon Macias']
}

var projectURL = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia1.s-nbcnews.com%2Fi%2Fnewscms%2F2018_46%2F2642661%2F1811111-hal-9000-1155p_a6911350a03c931077af0ec13fbdc8ef.jpg&imgrefurl=https%3A%2F%2Fwww.nbcnews.com%2Fpop-culture%2Fmovies%2Fdouglas-rain-creepy-voice-hal-2001-dies-90-n935036&tbnid=tdadpK0FZXrhDM&vet=12ahUKEwjg_5GG5c_sAhXPTN8KHX_FBQcQMygCegUIARCrAQ..i&docid=Q1r7duaq_q6hKM&w=2400&h=2400&q=hal%20&hl=en&ved=2ahUKEwjg_5GG5c_sAhXPTN8KHX_FBQcQMygCegUIARCrAQ"

var collabURL = "https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.wikia.nocookie.net%2Fannex%2Fimages%2Fb%2Fb5%2FDr.Heinz.jpg%2Frevision%2Flatest%2Fscale-to-width-down%2F340%3Fcb%3D20081106141050&imgrefurl=https%3A%2F%2Fannex.fandom.com%2Fwiki%2FDr._Heinz_Doofenshmirtz&tbnid=5KuUbL2MMYj9wM&vet=12ahUKEwjp5sq148_sAhUNneAKHSPbDvMQMygBegUIARCZAQ..i&docid=5zWpHoGBmBVWvM&w=340&h=411&q=heinz%20doo&hl=en&ved=2ahUKEwjp5sq148_sAhUNneAKHSPbDvMQMygBegUIARCZAQ"

function getCurrProject(){
  return currProject;
}

function getRecommendedProjects(projName){
  get('/getProjRecommendations?projectName=' + name, json => {
    console.log(json)
  })
  return [{'name': 'Synplicity', 'desc': 'An AR Syntax Checking Tool', 'tags': ['#Python', '#C'], 'collabs': ['Bobby DropTables', 'Jacob Snyderman', 'John Tantillo'], 'img_URL': "../static/assets/oop.jpg"}]
}

function getUserData(name){
  get('/getProfile?userID=' + name, json => {
    let result = JSON.parse(json)
    console.log(json)
    return {}
  })
}

function setUp_homePage(){
  let currProjectTitle = document.getElementById('curr-project-name');
  let currDesc = document.getElementById('curr-project-description')
  let tagBox = document.getElementById('tag-box');
  let reccommendBox = document.getElementById('reccomendations');
  let collabBox = document.getElementsByClassName('col-scroll-wrapper')[0]
  let currProj = getCurrProject();
  currProjectTitle.innerText = currProj['name']
  currDesc.innerText = currProj['desc']
  for (project of getRecommendedProjects()){
    reccommendBox.appendChild(newRecommendationTile(project['name'],project['desc'],projectURL))
  }
  for (c_name of currProj['collabs']){
    let collab = getUserData(c_name)
    collabBox.appendChild(newColTile(collab['name'],collab['tags'],collabURL))
  }
  loadPageTags(currProj['tags'], document.getElementById('tag-box'))
}

function search(search_string){
  let results = document.getElementById('search-results')
  if(search_string === ''){
    for (project of getRecommendedProjects()){
      results.appendChild(newSearchResult(project['name'],project['desc'],project['tags'],project['collabs'],projectURL))
    }
  }
  else{
    get('/getProjNames',search => {
      for (project of search){
        results.appendChild(newSearchResult(project['name'],project['desc'],project['tags'],project['collabs'],projectURL))
      }
    })
  }
}