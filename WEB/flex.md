# css position
- 문서 상에서 요소의 위치를 지정
- static: 모든 태그의 기본 값(기준 위치)
    - 일반적인 요소의 배치 순서에 따름
    - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치
  - 아래는 자표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
      1. relative
          - 자기 자신의 static위치를 기준으로 이동
          - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음
      2. absolute
          - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
          - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동
      3. fixed
          - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
          - 부모 요소와 관계없이 viewport를 기준으로 이동
              - 스크롤 시에도 항상 같은 곳에 위치함
      4. sticky
          - 스크롤에 따라 static에서 fixed로 변경
          - 속성을 적용한 박스는 평소에 문서 안에서 position: static상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성

# float
- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함한 인라인요소들이 주변을 wrapping 하도록 함
- 요소가 normal flow를 벗어나도록 함

# felxbox
- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축
    - 메인축(main axis)
    - 교차 축(cross axis)
- 구성요소
    - 부모요소(flex container)
    - 자식요소(flex item)

