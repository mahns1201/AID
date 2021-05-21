// <script> 요소 내에서 "land" 클래스가 있는 모든 요소를 가져옵니다.
var lands = document.getElementsByClassName('land');

// 그 위로 루프하여 마우스 오버 및 마우스 아웃 이벤트에 대한 이벤트 수신기를 추가합니다.
// 즉, 마우스가 지역에서 또는 지역에서 이동할 때마다 전달된 함수를 호출합니다.
// 이 경우, mouseOverEffect와 mouseOutEffect
for(var i = 0; i < lands.length; i++) {
    lands[i].addEventListener('mouseover', mouseOverEffect);
    lands[i].addEventListener('mouseout', mouseOutEffect);
}

// 그런 다음 기능을 정의해야 합니다. 여기서는 mouseOverEffect 함수에서
// "land-hightlight" 클래스를 추가하고 mouseOutEffect 함수에서 제거했습니다.
function mouseOverEffect() {
    this.classList.add("land-hightlight");
}

function mouseOutEffect() {
    this.classList.remove("land-hightlight");
}