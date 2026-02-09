---
nav_title: 항목 추천
article_title: Braze의 아이템 추천
page_order: 15
search_rank: 1
description: "Braze의 아이템 추천 엔진에 대해 자세히 알아보세요."
---

# 항목 추천

> 사용자가 실제로 원하는 아이템과 콘텐츠를 제안할 수 있는 추천 엔진을 만들어 Braze로 추천 게임의 수준을 한 단계 높여보세요. AI를 사용하여 경험을 커스텀하거나 Liquid 또는 연결된 콘텐츠로 자체 엔진을 구축하는 것까지, 모든 추천을 중요하게 만드는 데 필요한 모든 것을 찾을 수 있습니다.

## 필수 조건

Braze에서 아이템 추천을 만들거나 사용하려면 먼저 해당 카탈로그에서 사용자에게 추천할 [카탈로그 전용 아이템을 하나 이상 만들어야]({{site.baseurl}}/user_guide/data/activation/catalogs/create/)합니다.

## 유형 및 사용 사례

### 개인화된 AI {#ai}

[AI 항목 추천]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/) 기능의 일부인 AI 개인화된 추천은 딥러닝을 활용하여 사용자가 과거에 관심을 보인 것을 바탕으로 다음에 관심을 가질 가능성이 높은 것을 예측합니다. 이 방법은 사용자 행동에 적응하는 동적 맞춤형 추천 시스템을 제공합니다.

AI 개인화된 추천은 구매나 커스텀 이벤트와 같은 항목 상호작용 데이터의 지난 6개월을 사용하여 추천 모델을 구축합니다. 개인화된 목록을 위한 데이터가 충분하지 않은 사용자의 경우, 가장 인기 있는 항목이 대체 항목으로 사용되므로 사용자는 여전히 관련성 높은 추천을 받을 수 있습니다.

AI 항목 추천을 사용하면
[선택]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/)과 같이 사용 가능한 항목을 추가로 필터링할 수도 있습니다. 그러나 Liquid을 사용한 선택은 AI 추천에 사용할 수 없으므로 카탈로그 선택을 구성할 때 이를 염두에 두세요.

{% alert tip %}
AI 개인화 추천은 수백 또는 수천 개의 항목과 일반적으로 구매 또는 상호 작용 데이터가 있는 최소 30,000명의 사용자를 대상으로 가장 잘 작동합니다. 이는 대략적인 가이드이며 변동될 수 있습니다. 다른 추천 유형은 더 적은 데이터로 작동할 수 있습니다.
{% endalert %}

#### 사용 사례

추적 중인 상호작용 데이터에 따라 이 모델의 사용 사례에는 다음이 포함될 수 있습니다:

{% tabs local %}
{% tab Most likely to purchase next %}
구매 이벤트 또는 구매와 관련된 커스텀 이벤트를 기반으로 사용자가 다음에 구매할 가능성이 가장 높은 항목을 예측하고 추천합니다. 예를 들어, 다음과 같습니다.

- 여행 사이트는 사용자의 검색 기록과 이전 예약을 기반으로 휴가 패키지, 항공편 또는 호텔 숙박을 제안하여 다음 여행 대상을 예상하고 여행 계획을 더 쉽게 할 수 있습니다.
- 스트리밍 플랫폼은 시청 습관을 분석하여 사용자가 다음에 시청할 가능성이 가장 높은 프로그램이나 영화를 추천함으로써 사용자의 참여를 유지하고 고객이탈률을 줄일 수 있습니다.

{% details Requirements %}
- AI 항목 추천
- 관련 항목 카탈로그
- 구매 오브젝트 또는 커스텀 이벤트 등 구매 추적 방법
{% enddetails %}

{% details Setting it up %}
1. [AI 항목 추천]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/)을 생성하세요.
2. **유형**을 **AI 개인화**로 설정합니다.
3. 카탈로그를 선택하세요.
4. (선택 사항)선택 항목을 추가하여 관련 항목으로만 추천을 필터링할 수 있습니다.
5. 현재 구매 이벤트와 해당 이벤트 속성정보를 추적하는 방법을 선택합니다.
6. 추천을 훈련시킵니다.
7. [메시징에서 추천을 사용합니다]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### 가장 인기 있는 항목 {#most-popular}

'가장 인기 있는' 추천 모델에는 사용자가 가장 많이 참여하는 항목이 있습니다.

#### 사용 사례

추적 중인 상호 작용 데이터를 기반으로 이 모델의 사용 사례에는 추천이 포함될 수 있습니다.

{% tabs local %}
{% tab most popular %}
구매를 기반으로 카탈로그의 인기 항목을 탐색하도록 사용자에게 권장합니다. 관련 콘텐츠만 표시되도록 하려면 선택 항목으로 필터링할 것을 권장합니다. 예를 들어, 음식 배달 서비스는 플랫폼 전반의 주문 인기도를 기반으로 사용자의 지역 내에서 최고 평점을 받은 요리나 레스토랑을 강조하여 시도와 발견을 장려할 수 있습니다.

{% details Requirements %}
- AI 항목 추천
- 관련 항목 카탈로그
- 구매 객체 또는 커스텀 이벤트
{% enddetails %}

{% details Setting it up %}
1. [AI 항목 추천]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/)을 생성하세요.
2. **유형**을 **가장 인기 있음**으로 설정합니다.
3. 카탈로그를 선택하세요.
4. (선택 사항)선택 항목을 추가하여 관련 항목으로만 추천을 필터링할 수 있습니다. 예를 들어, 음식 배달 서비스에는 레스토랑 위치나 요리 종류를 필터링할 수 있는 선택 항목이 있을 수 있습니다.
5. 이벤트 및 해당 이벤트 속성을 현재 추적하는 방법을 선택하세요.
6. 추천을 훈련시킵니다.
7. [메시징에서 추천을 사용합니다]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab most liked %}
사용자가 최근에 좋아한 항목이나 좋아요용 커스텀 이벤트를 기반으로 인기 있는 항목을 탐색하도록 유도합니다. 예를 들어, 음악 스트리밍 앱은 사용자가 과거에 좋아했던 장르나 아티스트를 기반으로 개인화된 재생 목록을 만들거나 새 앨범 발매를 제안하여 사용자 인게이지먼트와 앱 사용 시간을 향상시킬 수 있습니다.

{% details Requirements %}
- AI 항목 추천
- 관련 항목 카탈로그
- 좋아요 커스텀 이벤트
{% enddetails %}

{% details Setting it up %}
1. [AI 항목 추천]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/)을 생성하세요.
2. **유형**을 **가장 최근**으로 설정합니다.
3. 카탈로그를 선택하세요.
4. (선택 사항)선택 항목을 추가하여 관련 항목으로만 추천을 필터링할 수 있습니다.
5. **커스텀 이벤트**를 선택하고 목록에서 좋아요에 대한 커스텀 이벤트를 선택합니다.
6. 추천을 훈련시킵니다.
7. [메시징에서 추천을 사용합니다]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab most viewed %}
조회수를 통해 사용자 기반에서 주목받은 항목을 강조하여 인게이지먼트 또는 구매를 유도합니다. 예를 들어, 부동산 웹사이트에서는 사용자의 검색 영역에서 가장 많이 조회된 목록을 표시하여 많은 관심을 받고 있는 매물을 강조 표시하여 좋은 거래나 적절한 위치를 나타낼 수 있습니다.

{% details Requirements %}
- AI 항목 추천
- 관련 항목 카탈로그
- 조회용 커스텀 이벤트
{% enddetails %}

{% details Setting it up %}
1. [AI 항목 추천]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/)을 생성하세요.
2. **유형**을 **가장 인기 있음**으로 설정합니다.
3. 카탈로그를 선택하세요.
4. (선택 사항)선택 항목을 추가하여 관련 항목으로만 추천을 필터링할 수 있습니다.
5. **커스텀 이벤트**를 선택하고 목록에서 조회용 커스텀 이벤트를 선택합니다.
6. 추천을 훈련시킵니다.
7. [메시징에서 추천을 사용합니다]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab popular in cart %}
다른 많은 쇼핑객들이 장바구니에 추가한 상품을 보여주어 사용자에게 현재 제공하는 상품 트렌드를 엿볼 수 있게 합니다.

예를 들어, 패션 소매업체는 다른 고객들이 장바구니에 추가한 인기 상품을 기반으로 유행하는 옷과 액세서리를 홍보할 수 있습니다. 그런 다음 홈페이지와 모바일 앱에 "지금 인기" 섹션을 만들고 실시간으로 업데이트하여 쇼핑객들이 품절되기 전에 구매하도록 유도할 수 있습니다.

{% details Requirements %}
- AI 항목 추천
- 관련 항목 카탈로그
- 장바구니에 담기 커스텀 이벤트
{% enddetails %}

{% details Setting it up %}
1. [AI 항목 추천]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/)을 생성하세요.
2. **유형**을 **가장 인기 있음**으로 설정합니다.
3. 카탈로그를 선택하세요.
4. (선택 사항)선택 항목을 추가하여 관련 항목으로만 추천을 필터링할 수 있습니다.
5. **커스텀 이벤트**를 선택하고 목록에서 장바구니에 추가할 커스텀 이벤트를 선택하세요.
6. 추천을 훈련시킵니다.
7. [메시징에서 추천을 사용합니다]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### 가장 최근 항목 {#most-recent}

'가장 최근' 추천 모델에는 사용자가 가장 많이 참여하는 항목이 있습니다. 이 모델을 사용하여 고객 이탈을 줄이고, 휴면 사용자가 관련 콘텐츠에 다시 참여하도록 유도하세요.

#### 사용 사례

추적 중인 상호 작용 데이터를 기반으로 이 모델의 사용 사례에는 추천이 포함될 수 있습니다.

{% tabs local %}
{% tab Recently clicked %}
클릭에 대한 커스텀 이벤트를 기반으로 사용자가 최근에 클릭한 항목을 다시 방문하도록 유도합니다. 예를 들어, 온라인 패션 소매업체는 사용자가 관심을 보인 옷을 클릭하면 후속 이메일이나 푸시 알림을 보내도록 추천을 생성하여 해당 상품을 다시 방문하고 이를 구매하도록 유도할 수 있습니다.

{% details Requirements %}
- AI 항목 추천
- 관련 항목 카탈로그
- 클릭용 커스텀 이벤트
{% enddetails %}

{% details Setting it up %}
1. [AI 항목 추천]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/)을 생성하세요.
2. **유형**을 **가장 최근**으로 설정합니다.
3. 카탈로그를 선택하세요.
4. (선택 사항)선택 항목을 추가하여 관련 항목으로만 추천을 필터링할 수 있습니다.
5. **커스텀 이벤트**를 선택하고 목록에서 클릭용 커스텀 이벤트를 선택하세요.
6. 추천을 훈련시킵니다.
7. [메시징에서 추천을 사용합니다]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}

{% endtab %}
{% tab Recently liked %}
사용자가 최근에 좋아한 항목이나 좋아요용 커스텀 이벤트를 기반으로 인기 있는 항목을 탐색하도록 유도합니다. 예를 들어, 음악 스트리밍 앱은 사용자가 과거에 좋아했던 장르나 아티스트를 기반으로 개인화된 재생 목록을 만들거나 새 앨범 발매를 제안하여 사용자 인게이지먼트와 앱 사용 시간을 향상시킬 수 있습니다.

{% details Requirements %}
- AI 항목 추천
- 관련 항목 카탈로그
- 좋아요 커스텀 이벤트
{% enddetails %}

{% details Setting it up %}
1. [AI 항목 추천]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/)을 생성하세요.
2. **유형**을 **가장 최근**으로 설정합니다.
3. 카탈로그를 선택하세요.
4. (선택 사항)선택 항목을 추가하여 관련 항목으로만 추천을 필터링할 수 있습니다.
5. **커스텀 이벤트**를 선택하고 목록에서 좋아요에 대한 커스텀 이벤트를 선택합니다.
6. 추천을 훈련시킵니다.
7. [메시징에서 추천을 사용합니다]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Recently engaged %}
조회수, 클릭 수, 구매 등 사용자가 최근에 상호작용한 항목을 홍보합니다. 이 접근 방식은 사용자의 최신 관심사에 맞춰 추천을 최신 상태로 유지합니다. 예를 들어, 다음과 같습니다.

- **교육:** 온라인 교육 플랫폼은 최근 교육 비디오를 시청했지만 아직 강좌에 등록하지 않은 사용자에게 유사한 과정이나 관심 있는 주제를 확인하도록 권장하여 사용자가 학습을 시작하도록 참여하고 동기를 부여할 수 있습니다.
- **피트니스:** 피트니스 앱은 사용자가 최근에 완료하거나 상호작용한 것과 유사한 운동이나 도전을 제안하여 운동 루틴을 다양하고 흥미롭게 유지할 수 있습니다.
- **홈 인테리어 소매업체:** 고객이 전동 공구를 구매한 후, 홈 인테리어 소매업체는 최근 구매를 기반으로 관련 액세서리나 안전 장비를 추천하여 사용자의 경험과 안전을 향상시킬 수 있습니다.

{% details Requirements %}
- AI 항목 추천
- 관련 항목 카탈로그
- 구매 객체 또는 인게이지먼트 상호작용을 위한 커스텀 이벤트
{% enddetails %}

{% details Setting it up %}
1. [AI 항목 추천]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/)을 생성하세요.
2. **유형**을 **가장 최근**으로 설정합니다.
3. 카탈로그를 선택하세요.
4. (선택 사항)선택 항목을 추가하여 관련 항목으로만 추천을 필터링할 수 있습니다.
5. **커스텀 이벤트**를 선택하고 목록에서 클릭용 커스텀 이벤트를 선택하세요.
6. 추천을 훈련시킵니다.
7. [메시징에서 추천을 사용합니다]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Recently added %}
사용자에게 최근 장바구니에 추가했지만 아직 구매하지 않은 항목에 대한 관심을 상기시킵니다. 예를 들어, 온라인 소매업체는 알림을 보내거나 장바구니에 있는 품목에 대해 기간 한정 할인을 제공하여 혜택이 만료되기 전에 구매를 마치도록 유도할 수 있습니다.
{% details Requirements %}

- AI 항목 추천
- 관련 항목 카탈로그
- 장바구니에 담기 커스텀 이벤트
{% enddetails %}

{% details Setting it up %}
1. [AI 항목 추천]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/)을 생성하세요.
2. **유형**을 **가장 최근**으로 설정합니다.
3. 카탈로그를 선택하세요.
4. (선택 사항)선택 항목을 추가하여 관련 항목으로만 추천을 필터링할 수 있습니다.
5. **커스텀 이벤트**를 선택하고 목록에서 장바구니에 추가할 커스텀 이벤트를 선택하세요.
6. 추천을 훈련시킵니다.
7. [메시징에서 추천을 사용합니다]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### 인기 있는 항목 {#trending}

'인기' 추천 모델은 최근 사용자 상호작용에서 가장 긍정적인 모멘텀을 보인 아이템을 추천하는 기능을 합니다. 약 10주간의 이벤트 기록에 대한 가중치 분석을 통해 이를 계산하며, 가장 최근 약 2주에 가장 무거운 가중치를 적용합니다. 작은 변동이 추천 품질에 영향을 미치지 않도록 활동 임계값과 통계적 평활화 기법을 적용합니다.

"가장 인기 있는" 모델과 달리, 지속적으로 높은 상호작용을 특징으로 하는 이 모델은 상호작용이 증가한 항목을 특징으로 합니다. 이를 사용하여 최근 주목받고 있는 인기 상품을 추천할 수 있습니다.

#### 사용 사례

추적 중인 상호 작용 데이터를 기반으로 이 모델의 사용 사례에는 추천이 포함될 수 있습니다.

{% tabs local %}
{% tab Trending purchased %}
사용자가 최근에 더 자주 구매한 항목을 강조 표시합니다. 예를 들어, 이커머스 비즈니스는 사용자가 다음 시즌을 준비하는 동안 재고를 비축하기 시작하는 시즌 상품을 추천할 수 있습니다. 

{% details Requirements %}
- AI 항목 추천
- 관련 항목 카탈로그
- 구매 추적 방법(구매 오브젝트 또는 커스텀 이벤트)
{% enddetails %}

{% details Setting it up %}
1. [AI 항목 추천]({{site.baseurl}}/ai_item_recommendations/)을 생성하세요.
2. **타입**을 **트렌딩**으로 설정합니다.
3. 카탈로그를 선택하세요.
4. (선택 사항)선택 항목을 추가하여 관련 항목으로만 추천을 필터링할 수 있습니다.
5. 구매 이벤트 또는 해당 속성정보와 함께 구매를 추적하는 커스텀 이벤트 중 하나를 선택합니다.
6. 추천을 훈련시킵니다.
7. [메시징에서 권장 사항을 사용합니다.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)
{% enddetails %}
{% endtab %}

{% tab Trending liked %}
사용자가 최근에 좋아요를 누른 빈도가 증가한 항목을 강조 표시합니다. 예를 들어, 음악 앱은 최근 사용자 좋아요가 급증한 신진 아티스트를 기능으로 할 수 있습니다.

{% details Requirements %}
- AI 항목 추천
- 관련 항목 카탈로그
- 좋아요 추적용 커스텀 이벤트
{% enddetails %}

{% details Setting it up %}
1. [AI 항목 추천]({{site.baseurl}}/ai_item_recommendations/)을 생성하세요.
2. **타입**을 **트렌딩**으로 설정합니다.
3. 카탈로그를 선택하세요.
4. (선택 사항)선택 항목을 추가하여 관련 항목으로만 추천을 필터링할 수 있습니다.
5. 커스텀 이벤트를 선택하여 좋아요 추적과 해당 속성정보를 함께 설정합니다.
6. 추천을 훈련시킵니다.
7. [메시징에서 권장 사항을 사용합니다.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging/)
{% enddetails %}
{% endtab %}
{% endtabs %}

### 선택 기반 {#selections-based}

[선택]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/)은 카탈로그 데이터의 특정 그룹입니다. 선택을 사용할 때, 본질적으로 카탈로그의 특정 열을 기반으로 커스텀 필터를 설정하는 것입니다. 여기에는 브랜드, 크기, 위치, 추가된 날짜 등을 위한 필터가 포함될 수 있습니다. 사용자에게 표시할 항목이 충족해야 하는 기준을 정의할 수 있도록 하여 추천하는 항목을ㄹ 제어할 수 있습니다.

이전 세 가지 유형 모두 Braze에서 추천 모델을 설정하고 훈련하는 것을 포함합니다. 이 모델에서도 선택 항목을 사용할 수 있지만, 카탈로그 선택 항목과 Liquid 개인화만으로도 일부 추천 사용 사례를 달성할 수 있습니다.

{% alert note %}
선택 항목을 사용하는 경우 정렬 필드 및 제한 사항은 AI 항목 추천에 사용되지 않습니다. 즉, 특정 정렬 필드가 있는 선택 항목을 만들고 반환되는 항목 수를 제한하면 AI 항목 추천이 처리될 때 이러한 제약 조건이 사용되지 않습니다.
{% endalert %}

#### 사용 사례

추적 중인 상호 작용 데이터를 기반으로 이 모델의 사용 사례에는 추천이 포함될 수 있습니다.

{% tabs local %}
{% tab New items %}
이 시나리오는 사용자 행동에 직접 의존하지 않고 카탈로그 데이터에 의존합니다. 카탈로그에 추가된 날짜를 기준으로 새 항목을 필터링하고 추천 모델을 학습하지 않고도 타겟팅 캠페인이나 캔버스를 통해 홍보할 수 있습니다.

예를 들어, 기술 이커머스 플랫폼은 필터를 사용하여 최근 카탈로그에 추가된 품목을 타겟팅하여 기술 애호가에게 최신 가젯이나 예정된 선주문에 대한 알림을 보낼 수 있습니다.

{% details Requirements %}
- 관련 항목의 카탈로그와 추가된 날짜를 위한 필드
{% enddetails %}

{% details Setting it up %}
1. 카탈로그를 기반으로 선택 항목을 만드세요. 카탈로그에 항목이 추가된 날짜에 해당하는 시간 필드(**데이터 유형**이 **시간**으로 설정된 필드)가 있는지 확인합니다.
2. (선택 사항)원하는 필터를 추가합니다.
3. **정렬 순서 무작위화**가 꺼져 있는지 확인합니다.
4. **정렬 필드**에 추가된 날짜 필드를 선택합니다.
5. **정렬 순서**를 내림차순으로 설정합니다.
6. [메시징에서 선택 항목을 사용합니다]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging).
{% enddetails %}
{% endtab %}

{% tab Random items %}
다양한 사용자 경험을 위해 무작위 항목을 추천하는 것은 다양성을 도입하고 방문 빈도가 낮은 카탈로그 영역에 대한 관심을 유발할 수 있습니다. 이 방법은 특정 모델이나 이벤트를 필요로 하지 않으며, 대신 카탈로그 선택을 사용하여 항목이 무작위로 표시되도록 합니다.

예를 들어, 온라인 서점은 사용자의 과거 구매나 검색 습관을 기반으로 무작위로 책을 추천하는 "Surprise Me" 기능을 제공하여 일반적인 독서 장르 외의 탐색을 장려할 수 있습니다.

{% details Requirements %}
- 관련 항목 카탈로그
- **무작위 정렬 순서**를 킨 선택 항목
{% enddetails %}

{% details Setting it up %}
1. 카탈로그를 기반으로 [선택 항목을 만듭니다.]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#creating-a-selection)
2. (선택 사항)원하는 필터를 추가합니다.
3. **정렬 순서 무작위화**를 켭니다.
4. [메시징에서 선택 항목을 사용합니다]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/#using-selections-in-messaging).
{% enddetails %}
{% endtab %}
{% endtabs %}

### 규칙 기반 {#rules-based}

[규칙 기반 추천]({{site.baseurl}}/rules_based_recommendations/) 엔진은 메시지 내에서 사용자에게 관련 항목을 제안하기 위해 사용자 데이터 및 제품 정보를 사용합니다. 사용자 행동 및 속성에 따라 콘텐츠를 동적으로 개인화하기 위해 Liquid 및 Braze 카탈로그 또는 연결된 콘텐츠를 사용합니다.

규칙 기반 추천은 수동으로 설정해야 하는 고정된 논리에 기반합니다. 즉, 로직을 업데이트하지 않으면 사용자의 개별 구매 내역과 취향에 맞게 추천이 조정되지 않으므로 이 방법은 자주 업데이트할 필요가 없는 추천에 가장 적합합니다.

#### 사용 사례

추적 중인 상호작용 데이터에 따라 이 모델의 사용 사례에는 다음이 포함될 수 있습니다:

- **재고 보충 알림:** 마지막 구매 날짜를 기준으로 월간 비타민이나 주간 식료품과 같이 사용 주기가 예측 가능한 품목에 대한 재고 보충 알림을 보냅니다.
- **첫 구매자:** 첫 구매자에게 스타터 키트나 입문용 상품을 추천하여 두 번째 구매를 유도하세요.
로열티 프로그램: 고객의 현재 포인트 잔액을 기준으로 로열티 포인트 또는 보상을 최대화할 수 있는 제품을 강조 표시합니다.
- **교육 콘텐츠:** 이전에 소비하거나 구매한 자료의 주제를 기반으로 새로운 과정이나 콘텐츠를 제안합니다.

{% multi_lang_include brazeai/recommendations/ai.md section="Plan-specific features" %}

## Frequently asked questions {#faq}

### "가장 인기 있음" 항목이 다른 모델의 추천에 섞이는 원인은 무엇입니까?

Braze의 추천 엔진이 목록을 큐레이트할 때, 먼저 선택한 특정 모델에 따라 개인화된 선택을 우선시합니다. 예를 들어 "가장 최근" 또는 "AI 개인화"과 같은 모델입니다. 이 모델이 어떤 이유로든 30개의 추천 목록을 완성할 수 없는 경우, 모든 사용자들 사이에서 가장 인기 있는 항목 중 일부가 추가되어 각 사용자가 항상 완전한 추천 세트를 갖도록 합니다.

이것은 몇 가지 특정 조건에서 발생합니다:

- 모델은 사용자의 기준에 맞는 항목을 30개 미만으로 찾습니다.
- 관련 항목은 더 이상 사용 가능하거나 재고가 없습니다.
- 항목이 현재 선택 기준을 충족하지 않으며, 이는 재고 변경 또는 사용자 선호도 변경 때문일 수 있습니다.

추천은 독립적으로 작동하며 다른 모델이 무엇을 추천하는지 전혀 알지 못합니다. 즉, 각 섹션에는 동일한 이메일의 다른 AI 추천 섹션에 이미 표시된 항목이 중복되어 있을 수 있습니다.

### Do existing recommendations train weekly after upgrading to Item Recommendations Pro?

예, 하지만 다음 예정된 업데이트 이후에만 가능합니다. 기존 추천은 Item Recommendations Pro로 업그레이드할 때 즉시 주간 훈련 및 일일 예측으로 전환되지 않습니다. 그러나 다음 재훈련 주기에서 새로운 일정이 자동으로 적용됩니다. 예를 들어 2월 1일에 마지막으로 훈련된 추천이 30일마다 재훈련되도록 설정된 경우, 3월 2일 다음 업데이트 이후 새로운 주간 일정을 적용합니다.
