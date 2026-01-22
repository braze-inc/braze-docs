---
nav_title: 내비게이션 딥링크
article_title: Braze 파일럿의 내비게이션 딥링크
page_order: 4
page_type: reference
description: "이 참조 문서에서는 엔지니어 또는 개발자에게 필요한 통합 단계를 간략하게 다룹니다."
---

# Braze Pilot의 내비게이션 딥링크

> Braze 파일럿은 Braze 메시징에서 파일럿 앱의 특정 부분으로 딥링킹을 지원합니다. 이를 통해 참여 사용 사례를 만들어 사용자를 파일럿 애플리케이션의 다양한 부분으로 유도할 수 있습니다. 선택적 딥링크 매개변수를 사용하여 앱의 특정 페이지에 있는 콘텐츠를 사용자에 맞게 커스텀할 수도 있습니다. 딥링킹에 대한 자세한 내용은 [인앱 콘텐츠에 딥링킹하기를]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking) 참조하세요.

## 일반

다음은 파일럿 앱의 기본 탐색 페이지에 대한 딥링크입니다. 

| 화면 | 딥링크 |
| --- | --- |
| 프로젝트 | `braze-pilot://navigation/projects` |
| 로그 데이터 | `braze-pilot://navigation/logdata` |
| 설정 | `braze-pilot://navigation/setup` |
| 언어 변경 | `braze-pilot://navigation/selectlanguage` |
| 카메라 | `braze-pilot://navigation/camera` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 스테핑턴턴

다음은 파일럿의 가상의 브랜드 앱인 Steppington에 대한 딥링킹입니다.

### 딥링크 예시

`braze-pilot://navigation/steppington/workout?title=Running&icon=HEART_DETAILS&image=https://picsum.photos/400&info=This%20workout%20is%20awesome%21&workout=5k%20Run&calories=600&length=25&workout_info_left_text=Road%20Run&workout_info_left_icon=RUNNING_HOME&workout_info_center_text=120%20BPM&workout_info_center_icon=HEART_DETAILS&workout_info_right_text=25%3A00&workout_info_right_icon=TIMER_DETAILS`

### 매개변수 없는 딥링크

| 화면 | 딥링크 |
| --- | --- |
| 스플래시 화면 | `braze-pilot://navigation/steppington/splash` |
| 홈 | `braze-pilot://navigation/steppington/home` |
| 스테핑턴턴+ 페이지 | `braze-pilot://navigation/steppington/plus` |
| 목표 화면 | `braze-pilot://navigation/steppington/goals` |
| 목표 변경 화면 | `braze-pilot://navigation/steppington/changegoals` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 매개변수가 있는 딥링크

| 화면 | 딥링크 |
| --- | --- |
| 운동 | `braze-pilot://navigation/steppington/workout` |
| 활동적인 운동 | `braze-pilot://navigation/steppington/activeworkout` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 허용되는 매개 변수

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 22%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table>
    <thead>
        <tr>
            <th>매개변수</th>
            <th>설명</th>
            <th>필수</th>
            <th>기본값(지정하지 않은 경우)</th>
            <th>유형</th>
            <th>예</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>title</code></td>
            <td>화면 상단에 사용할 제목입니다.</td>
            <td>예</td>
            <td></td>
            <td>문자열</td>
            <td>실행 중</td>
        </tr>
        <tr>
            <td><code>아이콘</code></td>
            <td>사용할 아이콘을 나타내는 문자열입니다.</td>
            <td>아니요</td>
            <td><code>RUNNING_HOME</code></td>
            <td>문자열</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>이미지</code></td>
            <td>항목 이미지의 URL입니다.</td>
            <td>예</td>
            <td></td>
            <td>문자열</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>정보</code></td>
            <td>운동 시작 버튼 위에 배치할 운동에 대한 정보입니다.</td>
            <td>예</td>
            <td></td>
            <td>문자열</td>
            <td>This%20workout%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>운동</code></td>
            <td>운동 이름입니다. 이벤트에서 보낸 <code>st_completed_class</code> 이벤트에 보냈습니다.</td>
            <td>예</td>
            <td></td>
            <td>번호</td>
            <td>5k%20달리기</td>
        </tr>
        <tr>
            <td><code>칼로리</code></td>
            <td>활성 운동 화면에 표시할 칼로리 수입니다. 이벤트에서 보낸 <code>st_completed_class</code> 이벤트에 보냈습니다.</td>
            <td>아니요</td>
            <td>500~1,250 사이의 임의의 숫자</td>
            <td>번호</td>
            <td>600</td>
        </tr>
        <tr>
            <td><code>길이</code></td>
            <td>운동 시간입니다. 이벤트에서 보낸 <code>st_completed_class</code> 이벤트에 보냈습니다.</td>
            <td>아니요</td>
            <td></td>
            <td>번호</td>
            <td>25</td>
        </tr>
        <tr>
            <td><code>workout_info_left_text</code></td>
            <td>활성 운동 화면의 왼쪽 카드에 사용할 텍스트입니다.</td>
            <td>아니요</td>
            <td></td>
            <td>문자열</td>
            <td>Road%20Run</td>
        </tr>
        <tr>
            <td><code>workout_info_left_icon</code></td>
            <td>활성 운동 화면의 왼쪽 카드에서 사용할 아이콘입니다.</td>
            <td>아니요</td>
            <td></td>
            <td>문자열</td>
            <td>RUNNING_HOME</td>
        </tr>
        <tr>
            <td><code>workout_info_center_text</code></td>
            <td>활성 운동 화면의 중앙 카드에 사용할 텍스트입니다.</td>
            <td>아니요</td>
            <td></td>
            <td>문자열</td>
            <td>120%20BPM</td>
        </tr>
        <tr>
            <td><code>workout_info_center_icon</code></td>
            <td>활성 운동 화면의 중앙 카드에서 사용할 아이콘입니다.</td>
            <td>아니요</td>
            <td></td>
            <td>문자열</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>workout_info_right_text</code></td>
            <td>활성 운동 화면의 오른쪽 카드에 사용할 텍스트입니다.</td>
            <td>아니요</td>
            <td></td>
            <td>문자열</td>
            <td>25%3A00</td>
        </tr>
        <tr>
            <td><code>workout_info_right_icon</code></td>
            <td>활성 운동 화면의 오른쪽 카드에서 사용할 아이콘입니다.</td>
            <td>아니요</td>
            <td></td>
            <td>문자열</td>
            <td>TIMER_DETAILS</td>
        </tr>
    </tbody>
</table>

##### 아이콘 옵션

| 아이콘 | 이미지 |
| --- | --- |
| `RUNNING_HOME` | \![운동화 아이콘.]({% image_buster /assets/img/braze_pilot/running_home_icon.png %}){:style="max-width:30%"} |
| `HEART_DETAILS` | 하트 아이콘.]({% image_buster /assets/img/braze_pilot/heart_details_icon.png %}){:style="max-width:30%"} |
| `TIMER_DETAILS` | \![스톱워치 아이콘.]({% image_buster /assets/img/braze_pilot/timer_details_icon.png %}){:style="max-width:30%"} |
| `YOGA_HOME` | 요가 자세를 취하고 있는 사람의 아이콘입니다.]({% image_buster /assets/img/braze_pilot/yoga_home_icon.png %}){:style="max-width:30%"} |
| `BICYCLE_HOME` | 자전거 아이콘.]({% image_buster /assets/img/braze_pilot/bicycle_home_icon.png %}){:style="max-width:30%"} |
| `DUMBBELL_HOME` | \![덤벨 아이콘.]({% image_buster /assets/img/braze_pilot/dumbbell_home_icon.png %}){:style="max-width:30%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 바지미로

파일럿의 가상의 브랜드 앱인 PantsLabyrinth의 딥링킹 링크입니다.

### 딥링크 예시

`braze-pilot://navigation/pantslabyrinth/itemdetails?name=Jeans&price=85&image=https://picsum.photos/400&description=This%20item%20is%20awesome%21&quantity=2&size=Large&colors=%230000FF,%23FF0000&color_strings=White,Blue&selected_color=1`

### 매개변수 없는 딥링크

| 화면 | 딥링크 |
| --- | --- |
| 스플래시 화면 | `braze-pilot://navigation/pantslabyrinth/splash` |
| 시작 화면 | `braze-pilot://navigation/pantslabyrinth/welcome` |
| 목록 화면 | `braze-pilot://navigation/pantslabyrinth/listing` |
| 장바구니 페이지 | `braze-pilot://navigation/pantslabyrinth/cart` |
| 위시리스트 페이지 | `braze-pilot://navigation/pantslabyrinth/wishlist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 매개변수가 있는 딥링크

| 화면 | 딥링크 |
| --- | --- |
| 항목 세부 정보 페이지 | `braze-pilot://navigation/pantslabyrinth/itemdetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 허용되는 매개 변수

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 20%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table>
    <thead>
        <tr>
            <th>매개변수</th>
            <th>설명</th>
            <th>필수</th>
            <th>기본값(지정하지 않은 경우)</th>
            <th>유형</th>
            <th>예</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>이름</code></td>
            <td>항목의 이름입니다.</td>
            <td>예</td>
            <td></td>
            <td>문자열</td>
            <td>청바지</td>
        </tr>
        <tr>
            <td><code>가격</code></td>
            <td>아이템의 가격입니다.</td>
            <td>예</td>
            <td></td>
            <td>문자열</td>
            <td>85</td>
        </tr>
        <tr>
            <td><code>이미지</code></td>
            <td>항목 이미지의 URL입니다.</td>
            <td>예</td>
            <td></td>
            <td>문자열</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>설명</code></td>
            <td>항목에 대한 설명입니다.</td>
            <td>예</td>
            <td></td>
            <td>문자열</td>
            <td>This%20item%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>수량</code></td>
            <td>아이템의 수량입니다.</td>
            <td>아니요</td>
            <td>1</td>
            <td>번호</td>
            <td>2</td>
        </tr>
        <tr>
            <td><code>크기</code></td>
            <td>항목의 크기를 나타내는 문자열입니다.</td>
            <td>아니요</td>
            <td>M</td>
            <td>문자열</td>
            <td>대형</td>
        </tr>
        <tr>
            <td><code>색상</code></td>
            <td>쉼표로 구분된 16진수 색상 목록입니다. 항목에 사용할 수 있는 색상은 다음과 같습니다.</td>
            <td>아니요</td>
            <td>%23000000</td>
            <td>문자열</td>
            <td>230000FF,%23FF0000</td>
        </tr>
        <tr>
            <td><code>color_strings</code></td>
            <td>쉼표로 구분된 색상 문자열 목록입니다. 텍스트의 색상을 담당합니다.</td>
            <td>아니요</td>
            <td>블랙</td>
            <td>문자열</td>
            <td>파란색, 빨간색</td>
        </tr>
        <tr>
            <td><code>selected_color</code></td>
            <td>사용자가 화면에 도착했을 때 색상 선택기에서 선택할 색상의 선택 색인입니다. 값을 사용하지 않으면 첫 번째 색상이 선택됩니다.</td>
            <td>아니요</td>
            <td>0</td>
            <td>번호</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

## MovieCanon

다음은 파일럿의 가상의 브랜드 앱인 Steppington에 대한 딥링킹입니다.

### 딥링크 예시

`braze-pilot://navigation/moviecannon/moviedetails?id=1&title=Jaws&thumbnail=https://picsum.photos/400&video=0&description=This%20video%20is%20awesome%21`

### 매개변수 없는 딥링크

| 화면 | 딥링크 |
| --- | --- |
| 스플래시 화면 | `braze-pilot://navigation/moviecannon/splash` |
| 시작 화면 | `braze-pilot://navigation/moviecannon/welcome` |
| 영화 목록 페이지 | `braze-pilot://navigation/moviecannon/moviecannon` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 매개변수가 있는 딥링크

| 화면 | 딥링크 |
| --- | --- |
| 동영상 세부 정보 페이지 | `braze-pilot://navigation/moviecannon/moviedetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 허용되는 매개 변수

| 매개변수 | 설명 | 필수 | 유형 | 예 |
| --- | --- | --- | --- | --- |
| `id` | 동영상의 ID입니다. | 예 | 번호 | 1 |
| `title` | 영화 제목입니다. | 예 | 문자열 | Jaws |
| `thumbnail` | 동영상 앞에 표시할 미리보기 이미지의 웹 URL입니다. | 예 | 문자열 | `https://picsum.photos/400` |
| `video` | 표시할 동영상 목록의 색인입니다. | 아니요 | 번호 | 0 |
| `description` | 동영상에 대한 설명입니다. | 예 | 문자열 | `This%20video%20is%20awesome%21` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
