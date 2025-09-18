---
nav_title: 미래 국가
article_title: 미래 국가
description: "퓨처 앤섬과 Braze를 통합하는 방법을 알아보세요."
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# 미래 국가

> 리얼 머니 게임 업계를 위한 퓨처 앤썸의 올인원 제품인 Amplifier AI는 콘텐츠 개인화, 실시간 경험, 역동적인 오디언스를 제공합니다. Amplifier AI works seamlessly across sports, casino, and lottery, allowing customers to enhance Braze player profiles with industry-specific player attributes, such as favorite game, favorite team, engagement score, next bet recommendation, expected next bet, and more.

{% alert important %}
이 기능은 현재 얼리 액세스 중입니다. 시작하려면 Future Anthem 고객 성공 팀에 문의하세요.
{% endalert %}

## 전제 조건

| 요구 사항              | 설명                                            |
|--------------------------|--------------------------------------------------------|
| 향후 앤섬 계정    | 미래 애국가 계정. |
| Braze REST API 키       | Braze REST API 키는 [`users.track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트      | 인스턴스와 일치하는 Braze [REST 엔드포인트]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) (예: `rest.iad-01.com`). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 활용 사례

이 통합을 통해 다음을 수행할 수 있습니다.

- 참여도가 높은 사용자를 식별하여 독점 프로모션이나 VIP 보상과 같은 개인화된 제안으로 타겟팅하세요.
- 사용자가 이미 좋아하는 게임을 기반으로 비슷한 게임을 추천합니다.

## 통합

향후 Anthem 고객 성공 팀에서 통합 설정을 도와드립니다. 고객 성공 담당자에게 연락하면 Braze에 보낼 가장 관련성 높은 속성을 식별하는 데 도움을 드릴 것입니다.

|미래 애국가 속성의 예|Braze의 속성 예시|
|-----------------------------------|---------------------------|
|![사용자 프로필의 속성]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %})|![개체 속성.]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %})|

## 브레이즈 사용자 지정 속성

다음은 사용 가능한 Braze 사용자 지정 속성입니다. 자세한 내용은 [미래 국가를 참조하세요: 시작하기](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab 베팅 추천 %}

| 하위 카테고리 | 예제(JSON) | 데이터 유형 |
| ------- | ----------- |----------- |
| 사용자 기본 설정 | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| 객체 |
| 싱글 베팅 추천 | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| 객체 |
| 어큐뮬레이터 베팅 추천 | `{"Bet_1": "Halland Goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}`| 객체 |
| 어큐뮬레이터 베팅 추천 | `{"Bet_1": 1.5, "Bet_2": 2}` | 객체 |
| 베팅 빌더 베팅 추천 | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahwaks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}`| 객체 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 보너스 추천 %}

| 하위 카테고리 | 예시 | 데이터 유형 |
| ------- | ----------- |----------- |
|NGR - 사용자 생애 동안의 순 게임 수익 | 2232| 숫자|
| NGR14 - 지난 14일 동안의 순 게임 수익 | 42 | 숫자
| 플레이어 수익성 점수| 130 | 숫자 |
| 참여 점수 | 0.78 | 숫자 |
| 고객이탈 위험 점수 | 0.02 | 숫자 |
| 다음 예상 베팅 날짜 | 2024-08-29 | 시간 |
| 베팅 및 획득 - 보너스 가치 추천 | 20 | 숫자 |
| 향후 기타 보너스 가치 추천 | 0 | 숫자 |
| 향후 CLTV  | 3126 | 숫자 |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab 게임 추천 %}

| 하위 카테고리 | 예시 | 데이터 유형 |
| ------- | ----------- |----------- |
| 추천 대상 | 플러피 페이버릿, 피싱 프렌지, 빅베이스 보난자, 레인보우 골드, 와일드 웨스트| 배열 |
| 즐겨 찾는 게임 | 피싱 열풍 | 배열 |
| 추천 신규 게임 | 끈적끈적한 꿀벌, 딥 메가웨이를 조심하라, 골드 파티, 플린트스톤즈| 배열 |
| 플레이 중인 플레이어와 같은 플레이어(협업 필터링) |골드 블리츠, 빅 베이스 스플래시, 릭 앤 모티, 사자의 서, 올림푸스의 문, 럭 오 더 아이리시 | 배열 |
| 플레이했기 때문에(게임 유사성)|플러피 페이버릿 2, 행운의 리쉬 익스프레스, 골드 캐시, 아즈텍 보물 찾기, 스타 보난자 | 배열 |
| 다음 단계(게임 시퀀싱) | 피싱 프렌지 더 빅 캐치, 빅 뱅커, 9 마스크 오브 파이어, 슈퍼 라이온, 피싱 더 빅팟 오브 골드, 피싱 더 빅팟 오브 골드 | 배열 |
| 인기 게임 | 아이리스 신전, 피싱 열풍, 낚시 보상, 미친 시간, 푹신한 즐겨 찾기 | 배열 |
| 인기 게임 | 돼지 은행가, 하이퍼 골드, 피라미드 왕, 골드 캐시 | 배열 |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab 플레이어 클러스터 %}

| 하위 카테고리 | 예시 | 데이터 유형 |
| ------- | ----------- |----------- |
| 플레이어가 어떤 클러스터에 있는지 표시 | 고부가가치 게임 다양성| 문자열 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab 플레이어 유지 - 플레이어 잠재적 위험 %}

| 하위 카테고리 | 예시 | 데이터 유형 |
| ------- | ----------- |----------- |
| 위험 점수 | 0.5| 숫자 |
| 위험한 플레이어 | 참 | 부울 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}
