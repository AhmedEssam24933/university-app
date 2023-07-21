// function get(url, html_id) {
//   var xhttp = new XMLHttpRequest();
//   xhttp.open('GET', url, true);
//   xhttp.onreadystatechange = function() {
//     if (this.readyState == 4 && this.status == 200) {
//       var data = JSON.parse(this.responseText);
//       var info = "";
//       for (i = 0; i < data.length; i++) {
//           info += "<div>ID: " + data[i].id + ", Name: " + data[i].name + "</div><hr>"
//       }
//       document.getElementById(html_id).innerHTML = info;
//     }
//   };
//   xhttp.send();
// }

// function getFaculty(url, html_id) {
//     get(url, html_id)
// }

function getFaculty() {
  var container = document.getElementById("show");
  if (container.style.display === "none") {
    // If the container is currently hidden, show all the faculty data
    container.style.display = "block";
    var xhttp = new XMLHttpRequest();
    xhttp.open('GET', "http://127.0.0.1:8000/faculty_list", true);
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var data = JSON.parse(this.responseText);
        var info = "";
        for (var i = 0; i < data.length; i++) {
          info += "<div>ID: " + data[i].id + ", Name: " + data[i].name + "</div><hr>"
        }
        container.innerHTML = info;
        // Store the faculty data in a data attribute
        container.setAttribute("data-faculty", info);
      }
    };
    xhttp.send();
  } else {
    // If the container is currently visible, hide all the faculty data
    container.style.display = "none";
  }
}
// function getFaculty() {
//   var container = document.getElementById("show");
//   if (container.style.display === "none") {
//     // If the container is currently hidden, show it and fetch the faculty data
//     container.style.display = "block";
//     var xhttp = new XMLHttpRequest();
//     xhttp.open('GET', "http://127.0.0.1:8000/faculty_list", true);
//     xhttp.onreadystatechange = function() {
//       if (this.readyState == 4 && this.status == 200) {
//         var data = JSON.parse(this.responseText);
//         var info = "";
//         for (var i = 0; i < data.length; i++) {
//             info += "<div>ID: " + data[i].id + ", Name: " + data[i].name + "</div><hr>"
//         }
//         container.innerHTML = info;
//       }
//     };
//     xhttp.send();
//   } else {
//     // If the container is currently visible, hide it
//     container.style.display = "none";
//   }
// }


  function getSpecificFaculty() {
    var xhttp = new XMLHttpRequest();
    var input = document.getElementById("myInput");
    url = "http://127.0.0.1:8000/faculty_pk/" + input.value
    xhttp.open('GET', url , true);
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        var data = JSON.parse(this.responseText);
        document.getElementById("show-specific-faculty").innerHTML = "<div>ID: " + data["id"]+ ", Name: " + data["name"] + "</div><hr>";
      }
    };
    xhttp.send();
  }

function getStudents() {
  var xhttp = new XMLHttpRequest();
  xhttp.open('GET', "http://127.0.0.1:8000/students_list", true);
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var data = JSON.parse(this.responseText);
      var info = "";
      for (var i = 0; i < data.length; i++) {
          info += "<div>ID: " + data[i].id + ", Name: " + data[i].first_name  + " " + data[i].last_name +"</div><hr>"
      }
      document.getElementById("get-students").innerHTML = info;
    }
  };
  xhttp.send();
}


  