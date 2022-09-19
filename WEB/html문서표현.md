# HTML 문서 구조화
    table의 각 영역을 명시하기 위해 <thead> <tbody> <tfoot> 요소를 활용

    <tr> : 가로줄 구성
    <th>,<td> : 내부 구성
    table 태그 기본 구성
       - thead
            - tr > th
        - tbody
            - tr > td
        - tfoot
             - tr > td
         - caption

# form 
    - form은 정보를 서버에 제출하기 위해 사용하는 태그
    - form 기본 속성
        -  action : form을 처리할 서버의 url
        -  method : form을 제출할 때 사용할 HTTP 메서드
        -  enctype : method가 post인 경우 데이터의 유형
    
## intput 
    - 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
    - 인풋의 속성
        - name
        - value
        - required, readonly, autofocus, autocomplete, disabled 등
       

##  input label
    - label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
        - 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일(터치) 환경에서 편하게 사용할 수 있음
        - label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어쉽게 내용을 확인 할 수 있도록 함
## input유형
    - 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음
        - text : 일반 텍스트 입력
        - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
        - email : 이메일 형식이 아닌 경우 form 제출 불가
        - number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
        - file : accept 속성을 활용하여 파일 타입 지정 가능