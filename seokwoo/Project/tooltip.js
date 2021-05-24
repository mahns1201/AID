var tooltip = document.querySelector('.land-tooltip');

// HTML의 모든 'path' 태그를 반복합니다.
[].forEach.call(document.querySelectorAll('path.land'), function(item) {
    
    // mousemove와 mouseleave 이벤트에 대한 이벤트 수신기를 추가합니다.
    // 즉, 마우스가 지역별로 이동할 때마다 전달된 함수를 호출합니다.
    item.addEventListener('mousemove', function(e) {
        tooltip.style.display = 'block';
        tooltip.style.top = e.clientY + 'px'
        tooltip.style.left = e.clientX + 'px';

        // 'title' 요소에 지정된 값(지명)을 반환합니다.
        tooltip.textContent = e.target.getAttribute("title");
    });

    item.addEventListener('mouseleave', function() {
        tooltip.style.display = 'none';
    });
})