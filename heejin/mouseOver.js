var lands = document.getElementsByClassName('land');

for(var i = 0; i < lands.length; i++) {
    lands[i].addEventListener('mouseover', mouseOverEffect);
    lands[i].addEventListener('mouseout', mouseOutEffect);
}

function mouseOverEffect() {
    this.classList.add("land-hightlight");
}

function mouseOutEffect() {
    this.classList.remove("land-hightlight");
}