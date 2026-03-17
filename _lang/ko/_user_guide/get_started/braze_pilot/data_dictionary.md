---
nav_title: 데이터 사전
article_title: Braze 파일럿용 데이터 사전
page_order: 3
page_type: reference
description: "이 참조 문서에서는 엔지니어 또는 개발자에게 필요한 통합 단계에 대해 간략하게 설명합니다."
---

# 데이터 사전

> Braze Pilot의 각 앱 시뮬레이션은 앱 내 사용자 활동에 기반하여 다양한 이벤트와 속성을 수집하도록 계측됩니다. 

## 데이터 접근 방식

해당 앱은 가상의 브랜드가 대표하는 업계에서 흔히 볼 수 있는 커스텀 속성과 이벤트를 기록합니다. 이러한 속성을 활용하여 다양한 일반적인 사용 사례에 대한 데모를 구현할 수 있습니다.
일반적으로 모든 이벤트와 속성에는 해당 데이터를 담당하는 앱 시뮬레이션에 대응하는 짧은 코드가 접두사로 붙습니다. For example:

- Steppington 앱 시뮬레이션에 의해 기록된 모든 데이터에는 접두사가 붙습니다. `st_`
- 팬츠미로 앱 시뮬레이션에 의해 기록된 모든 데이터는 접두사로 `pl_`
- MovieCanon 앱 시뮬레이션에 의해 기록된 모든 데이터는 접두사로 `mc_`

## 기록된 이벤트 및 속성 목록

다음 표는 Braze Pilot이 기록하는 이벤트 및 속성을 나열합니다.

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 32%;
}
th:nth-child(2), td:nth-child(2) {
    width: 15%;
}
th:nth-child(3), td:nth-child(3) {
    width: 10%;
}
th:nth-child(4), td:nth-child(4) {
    width: 20%;
}
th:nth-child(5), td:nth-child(5) {
    width: 28%;
}
</style>

<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>앱</th>
            <th>유형</th>
            <th>등록정보</th>
            <th>로그에 기록될 때</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>mc_entered_app</code></td>
            <td>MovieCanon</td>
            <td>Event</td>
            <td></td>
            <td>사용자가 MovieCanon 앱에 진입할 때</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>MovieCanon</td>
            <td>Event</td>
            <td><code>title: string</code></td>
            <td>사용자가 동영상 시청을 마쳤을 때</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>MovieCanon</td>
            <td>Event</td>
            <td><code>title: string</code></td>
            <td>사용자가 영화 페이지를 볼 때</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>PantsLabyrinth</td>
            <td>Event</td>
            <td><code>item_name: string</code></td>
            <td>사용자가 제품 페이지를 볼 때</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>PantsLabyrinth</td>
            <td>Event</td>
            <td></td>
            <td>사용자가 팬츠라비린스 앱에 진입할 때</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>PantsLabyrinth</td>
            <td>Event</td>
            <td><code>item_name: string</code></td>
            <td>사용자가 원하는 목록에 항목을 추가할 때</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>PantsLabyrinth</td>
            <td>Event</td>
            <td><code>item_name: string</code></td>
            <td>사용자가 장바구니에 상품을 추가할 때</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event&gt;</code></td>
            <td>PantsLabyrinth</td>
            <td>Event</td>
            <td><code>name: string</code><br><code>price: number</code></td>
            <td>사용자가 구매를 완료할 때</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td></td>
            <td>사용자가 Steppington 앱에 접속할 때</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>사용자가 운동을 완료할 때</td>
        </tr>
        <tr>
            <td><code>st_viewed_premium_benefit</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>benefit_type: string</code></td>
            <td>사용자가 Steppington+ 탭을 방문할 때 (기능 플래그로 인에이블먼트된 경우)</td>
        </tr>
        <tr>
            <td><code>st_viewed_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code></td>
            <td>사용자가 운동 페이지를 방문할 때</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>사용자가 운동을 완료할 때</td>
        </tr>
        <tr>
            <td><code>st_most_recent_completed_class</code></td>
            <td>Steppington</td>
            <td>속성</td>
            <td><code>string</code></td>
            <td>사용자가 운동을 완료할 때</td>
        </tr>
        <tr>
            <td><code>st_favorited_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code></td>
            <td>사용자가 수업을 즐겨찾기에 추가할 때</td>
        </tr>
        <tr>
            <td><code>st_unfavorited_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code></td>
            <td>사용자가 클래스의 즐겨찾기를 해제할 때</td>
        </tr>
        <tr>
            <td><code>st_started_free_trial</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td></td>
            <td>사용자가 <strong>무료 체험 시작</strong> 버튼을 선택할 때</td>
        </tr>
        <tr>
            <td><code>st_set_goal</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>goal_name: string</code><br><code>goal: number</code><br><code>units: string</code></td>
            <td>사용자가 <strong>무료 체험 시작</strong> 버튼을 선택할 때.</td>
        </tr>
    </tbody>
</table>
