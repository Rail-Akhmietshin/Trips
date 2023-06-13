let modal = document.getElementById("myModal");
let btn = document.getElementById("myBtn");
let shut = document.getElementsByClassName("shut")[0];

btn.onclick = function () {
    modal.style.display = "block";
}

shut.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}


