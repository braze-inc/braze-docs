---
nav_title: 데이터 사전
article_title: Braze 파일럿용 데이터 사전
page_order: 3
page_type: reference
description: "이 참조 문서에서는 엔지니어 또는 개발자에게 필요한 통합 단계를 간략하게 다룹니다."
---

# 데이터 사전

> Braze Pilot의 각 앱 시뮬레이션은 앱에서의 사용자 활동을 기반으로 다양한 이벤트와 속성을 수집하기 위해 계측됩니다. 

## 데이터에 대한 접근 방식

이 앱은 가상의 브랜드가 담당하는 업계의 일반적인 커스텀 속성 및 이벤트를 기록합니다. 이러한 속성을 사용하여 다양한 일반적인 사용 사례에 대한 데모를 강화할 수 있습니다.
일반적으로 모든 이벤트와 속성에는 데이터를 담당하는 앱 시뮬레이션에 해당하는 짧은 코드가 앞에 붙습니다. 예를 들어

- 스테핑턴턴 앱 시뮬레이션에 의해 기록된 모든 데이터에는 접두사가 붙습니다. `st_`
- 팬츠라비린스 앱 시뮬레이션에 의해 기록된 모든 데이터는 앞에 `pl_`
- MovieCanon 앱 시뮬레이션에 의해 기록된 모든 데이터 앞에는 `mc_`

## 기록된 이벤트 및 속성 목록

다음 표에는 Braze 파일럿이 기록한 이벤트와 속성이 나열되어 있습니다.

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
            <th>이름</th>
            <th>앱</th>
            <th>유형</th>
            <th>속성</th>
            <th>기록되는 시점</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>mc_entered_app</code></td>
            <td>MovieCanon</td>
            <td>이벤트</td>
            <td></td>
            <td>사용자가 MovieCanon 앱에 들어가면</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>MovieCanon</td>
            <td>이벤트</td>
            <td><code>제목: 문자열</code></td>
            <td>사용자가 동영상 시청을 마치면</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>MovieCanon</td>
            <td>이벤트</td>
            <td><code>제목: 문자열</code></td>
            <td>사용자가 동영상 페이지를 볼 때</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>바지미로</td>
            <td>이벤트</td>
            <td><code>item_name: 문자열</code></td>
            <td>사용자가 제품 페이지를 볼 때</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>바지미로</td>
            <td>이벤트</td>
            <td></td>
            <td>사용자가 팬츠라비린스 앱에 들어가면</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>바지미로</td>
            <td>이벤트</td>
            <td><code>item_name: 문자열</code></td>
            <td>사용자가 위시리스트에 아이템을 추가하는 경우</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>바지미로</td>
            <td>이벤트</td>
            <td><code>item_name: 문자열</code></td>
            <td>사용자가 카트에 품목을 추가하는 경우</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event></code></td>
            <td>바지미로</td>
            <td>이벤트</td>
            <td><code>이름: 문자열</code><br><code>가격: 숫자</code></td>
            <td>사용자가 구매를 완료한 경우</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>스테핑턴턴</td>
            <td>이벤트</td>
            <td></td>
            <td>사용자가 스테핑턴턴 앱에 들어가면</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>스테핑턴턴</td>
            <td>이벤트</td>
            <td><code>class_type: 문자열</code><br><code>calories_burned: 숫자</code><br><code>workout_length: 숫자</code></td>
            <td>사용자가 운동을 완료한 경우</td>
        </tr>
        <tr>
            <td><code>st_viewed_premium_benefit</code></td>
            <td>스테핑턴턴</td>
            <td>이벤트</td>
            <td><code>benefit_type: 문자열</code></td>
            <td>사용자가 스테핑톤+ 탭을 방문하는 경우(기능 플래그가 인에이블된 경우)</td>
        </tr>
        <tr>
            <td><code>st_viewed_class</code></td>
            <td>스테핑턴턴</td>
            <td>이벤트</td>
            <td><code>class_type: 문자열</code></td>
            <td>사용자가 운동 페이지를 방문하는 경우</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>스테핑턴턴</td>
            <td>이벤트</td>
            <td><code>class_type: 문자열</code><br><code>calories_burned: 숫자</code><br><code>workout_length: 숫자</code></td>
            <td>사용자가 운동을 완료한 경우</td>
        </tr>
        <tr>
            <td><code>st_most_recent_completed_class</code></td>
            <td>스테핑턴턴</td>
            <td>속성</td>
            <td><code>문자열</code></td>
            <td>사용자가 운동을 완료한 경우</td>
        </tr>
        <tr>
            <td><code>st_favorited_class</code></td>
            <td>스테핑턴턴</td>
            <td>이벤트</td>
            <td><code>class_type: 문자열</code></td>
            <td>사용자가 클래스를 즐겨찾는 경우</td>
        </tr>
        <tr>
            <td><code>st_unfavorited_class</code></td>
            <td>스테핑턴턴</td>
            <td>이벤트</td>
            <td><code>class_type: 문자열</code></td>
            <td>사용자가 클래스를 즐겨찾기에 추가하지 않은 경우</td>
        </tr>
        <tr>
            <td><code>st_started_free_trial</code></td>
            <td>스테핑턴턴</td>
            <td>이벤트</td>
            <td></td>
            <td>사용자가 <strong>무료 평가판 시작</strong> 버튼을 선택하면</td>
        </tr>
        <tr>
            <td><code>st_set_goal</code></td>
            <td>스테핑턴턴</td>
            <td>이벤트</td>
            <td><code>goal_name: 문자열</code><br><code>목표: 숫자</code><br><code>단위: 문자열</code></td>
            <td>사용자가 <strong>무료 평가판 시작</strong> 버튼을 선택합니다.</td>
        </tr>
    </tbody>
</table>
