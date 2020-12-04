    function myFunction1() {
  var x1 = document.getElementById("client");
  if (x1.style.display === "none") {
    x1.style.display = "block";
  } else {
    x1.style.display = "none";
  }
}

function myFunction2() {
  var x2 = document.getElementById("voiture");
  if (x2.style.display === "none") {
    x2.style.display = "block";
  } else {
    x2.style.display = "none";
  }
}

function myFunction3() {
  var x3 = document.getElementById("intervention");
  if (x3.style.display === "none") {
    x3.style.display = "block";
  } else {
    x3.style.display = "none";
  }
}

function myFunction4() {
  var x4 = document.getElementById("technicien");
  if (x4.style.display === "none") {
    x4.style.display = "block";
  } else {
    x4.style.display = "none";
  }
}

function myFunction5() {
    var x1 = document.getElementById("client");
    var x2 = document.getElementById("voiture");
    var x3 = document.getElementById("intervention");
    var x4 = document.getElementById("technicien");

    x1.style.display = none;
    x2.style.display = none;
    x3.style.display = none;
    x4.style.display = none;
}

window.onload = myFunction5();