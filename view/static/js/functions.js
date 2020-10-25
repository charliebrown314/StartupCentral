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

function getCurrProject(){
  return {"name" : "Startup Central", "desc" : "According to all known laws of aviation, there is no way a bee\n" +
        "                        should be able to fly. Its wings are too small to get its fat little body off the ground.\n" +
        "                        The bee, of course, flies anyway because bees don't care what humans think is impossible.\n" +
        "                        Yellow, black. Yellow, black.\n" +
        "                        Yellow, black. Yellow, black.\n" +
        "                        Ooh, black and yellow!\n" +
        "                        Let's shake it up a little.", 'img_URL': "../static/assets/oop.jpg", 'tags': ['#Python', '#HTML' , '#CSS', '#SCSS', '#JS']}
}

function getRecommendedProjects(){
  return [{'name': 'Synplicity', 'desc': 'An AR Syntax Checking Tool', 'img_URL': "../static/assets/oop.jpg"}]
}

function getCollaborators(projectName){
  return [{'name': 'Bobby DropTables', 'tags': ['#SQL','#Python', '#JS'], 'img_URL' : '../static/assets/linked_in_pfp.jpeg'}]
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
    reccommendBox.appendChild(newRecommendationTile(project['name'],project['desc'],project['img_URL']))
  }
  for (collab of getCollaborators(project['name'])){
    collabBox.appendChild(newColTile(collab['name'],collab['tags'],collab['img_URL']))
  }
  loadPageTags(currProj['tags'], document.getElementById('tag-box'))
}

function search(search_string){
  if(search_string == ''){

  }
  else{

  }
}