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

function setUp(){

}