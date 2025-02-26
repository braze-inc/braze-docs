---
nav_title: 규칙 기반 추천
article_title: 규칙 기반 추천
page_type: tutorial
page_order: 16
alias: "/rules_based_recommendations/"
description: "이 문서에서는 카탈로그 또는 연결된 콘텐츠를 사용하는 규칙 기반 추천 엔진을 만드는 방법에 대해 간략하게 설명합니다."
tool:
  - Campaigns
  - Canvas

---

# 규칙 기반 권장 사항

> 규칙 기반 추천 엔진은 사용자 데이터와 제품 정보를 사용하여 메시지 내에서 사용자에게 관련 항목을 제안합니다. [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)와 Braze [카탈로그]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) 또는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)를 사용하여 사용자 행동과 속성을 기반으로 콘텐츠를 동적으로 개인화합니다.

Liquid, 카탈로그 및 연결된 콘텐츠에 대해 자세히 알아보려면 다음 Braze 학습 과정을 확인하세요.

- [이메일을 통한 개인화된 추천](https://learning.braze.com/personalized-recommendations-with-email)
- [Liquid를 통한 동적 개인화](https://learning.braze.com/path/dynamic-personalization-with-liquid)
- [연결된 콘텐츠 기본 사항](https://learning.braze.com/path/dynamic-personalization-with-liquid/connected-content-fundamentals)

{% alert important %}
규칙 기반 추천은 수동으로 설정해야 하는 고정된 논리에 기반합니다. 즉, 로직을 업데이트하지 않으면 사용자의 구매 내역과 취향에 맞게 추천이 조정되지 않습니다.<br><br>사용자의 기록에 따라 자동으로 조정되는 개인화된 AI 추천을 만들려면 [AI 항목 추천]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/)을 확인하세요.
{% endalert %}

## 카탈로그 추천 엔진 만들기

1. 제품 [카탈로그를 생성합니다]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/).
2. 각 제품에 대해 추천 제품 목록을 "product_recommendations"라는 열에 구분 기호(예: 파이프 `|`)로 구분된 문자열로 추가합니다.
3. 카탈로그에 권장 사항을 찾으려는 제품 ID를 전달합니다.
4. 해당 카탈로그 항목의 `product_recommendations` 값을 가져와서 Liquid 분할 필터를 사용하여 구분 기호로 분할합니다.
5. 이러한 ID 중 하나 이상을 카탈로그에 다시 전달하여 다른 제품 세부 정보를 수집합니다.

### 카탈로그 사용 사례

건강식품 앱이 있고 사용자가 앱에 가입한 기간에 따라 다른 레시피를 전송하는 콘텐츠 카드 캠페인을 만들고 싶다고 가정해 보겠습니다. 

1. 다음 정보가 포함된 CSV를 통해 카탈로그를 생성하고 업로드합니다.<br>- **id:** 사용자가 앱에 가입한 후 경과한 일수와 관련된 고유 번호입니다. 예를 들어 `3`은 3일과 관련이 있습니다.<br>- **유형:** `comfort`, `fresh` 등과 같은 레시피 카테고리.<br>- **제목:** "이번 주 점심 미리 만들어 놓기" 또는 "타코 먹자"와 같이 각 ID에 대해 전송될 콘텐츠 카드의 제목입니다.<br>- **링크:** 레시피 문서로 연결되는 링크입니다.<br>- **image_url:** 레시피에 해당하는 이미지입니다.

{: start="2"}
2\. 카탈로그가 Braze에 업로드된 후 일부 카탈로그 항목의 미리 보기를 확인하여 가져온 정보가 정확하게 입력되었는지 확인합니다. 미리 보기에서 항목이 무작위로 표시될 수 있지만 추천 엔진의 출력에는 영향을 미치지 않습니다.

![][1]

{: start="3"}
3\. 콘텐츠 카드 캠페인을 만듭니다. 작성기에서 Liquid 로직을 입력하여 캠페인을 수신할 사용자와 표시할 레시피 및 이미지를 결정합니다. 이 사용 사례에서 Braze는 사용자의 `start_date`(또는 가입 날짜)를 가져와 현재 날짜와 비교합니다. 날짜 차이에 따라 전송되는 콘텐츠 카드가 결정됩니다. 

![][2]

**제목:**

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].title }}
```
{% endraw %}

**메시지:**

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{% if items[0].title != blank %}
{{ items[0].body }}
{% else %}
{% abort_message('no card for today') %}
{% endif %}
```
{% endraw %}

**이미지:**

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].image_url }}
```
{% endraw %}

{: start="4"}
4\. **클릭 시 동작** 섹션에서 사용자가 iOS, Android 및 웹 기기에서 콘텐츠 카드를 클릭할 때 리디렉션해야 하는 위치에 대한 Liquid 로직을 입력합니다. 

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].link }}
```
{% endraw %}

![][3]{: style="max-width:60%;"}<br><br>

{: start="5"}
5\. **테스트** 탭으로 이동하여 **사용자로 메시지 미리보기**에서 커스텀 **사용자를** 선택합니다. **커스텀 속성** 필드에 날짜를 입력하면 해당 날짜에 가입한 사용자에게 전송될 콘텐츠 카드를 미리 볼 수 있습니다. <br><br>

![][4]

## 연결된 콘텐츠 추천 엔진 만들기

1. 다음 방법 중 하나로 연결된 콘텐츠 엔드포인트를 만듭니다.
- SheetDP와 같은 서비스를 사용하여 스프레드시트를 JSON API 엔드포인트로 변환하고, 이렇게 생성되는 API URL을 기록해 두세요.
- 커스텀 사내 엔드포인트 구축, 호스팅 및 유지 관리
- [Amazon Personalise]({{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/), [Certona]({{site.baseurl}}/partners/message_personalization/dynamic_content/certona/), [Dynamic Yield]({{site.baseurl}}/partners/message_personalization/dynamic_content/dynamic_yield/) 등 [Alloy 파트너]({{site.baseurl}}/partners/message_personalization/dynamic_content/)와 같은 타사 파트너를 통해 추천 엔진을 구매하세요.

2. 연결된 콘텐츠 Liquid를 메시지 본문 또는 콘텐츠 블록 HTML 편집기에 작성하면 엔드포인트를 호출하여 데이터베이스를 검색할 수 있습니다.
3. 특정 사용자의 프로필에서 찾은 커스텀 속성 값에 맞춰 Liquid를 정렬합니다.
4. 결과적으로 올바른 추천을 가져옵니다.

{% raw %}
```
{% connected_content YOUR-API-URL :save items %}

{% assign recommended_item_ids_from_user_profile = custom_attribute.${RECOMMENDED_ITEM_IDS} | split: ';' %}

{% for item_id in recommended_item_ids_from_user_profile %}
  {% assign recommended_item = items | where: "ITEM_ID", ITEM_ID | first %}
  recommended_item.item_name
{% endfor %}
```
{% endraw %}

| 속성 | 교체 |
| --- | --- |
|`YOUR-API-URL` | API의 실제 URL로 바꿉니다. |
|`RECOMMENDED_ITEM_IDS` | 추천 항목의 ID가 포함된 커스텀 속성의 실제 이름으로 바꿉니다. 이 속성은 세미콜론으로 구분된 ID 문자열이 될 것으로 예상됩니다. |
|`ITEM_ID` | API 응답에서 항목 ID에 해당하는 속성의 실제 이름으로 바꿉니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
이는 기본적인 예시이며, 특정 요구 사항과 데이터 구조에 따라 추가 수정이 필요할 수 있습니다. 자세한 안내는 [Liquid 설명서]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)를 참조하거나 개발자에게 문의하세요.
{% endalert %}

## 연결된 콘텐츠 사용 사례

Zomato 레스토랑 데이터베이스에서 레스토랑 추천을 가져와 그 결과를 `restaurants`이라는 로컬 변수로 저장한다고 가정해 보겠습니다. 다음과 같은 연결된 콘텐츠 호출을 할 수 있습니다.

{% raw %}
```liquid

{% connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

다음으로 사용자의 도시와 음식 유형에 따라 레스토랑 추천을 가져오고 싶다고 가정해 보겠습니다. 사용자의 도시 및 음식 유형에 대한 커스텀 속성을 통화 시작 부분에 동적으로 삽입한 다음 `restaurants` 값을 `city_food.restaurants` 변수에 할당하면 됩니다.

연결된 콘텐츠 호출은 다음과 같이 표시됩니다.

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

레스토랑 이름과 평점만 검색하도록 응답을 맞춤 설정하려면 다음과 같이 통화 끝에 필터를 추가하면 됩니다.

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0].restaurant.name}}
{{city_food.restaurants[0].restaurant.user_rating.rating_text}}
```
{% endraw %}

마지막으로 레스토랑 추천을 등급별로 그룹화한다고 가정해 보겠습니다. 다음을 수행:

1. `assign`을 사용하여 "우수", "매우 우수", "좋음"의 등급 카테고리에 대한 빈 배열을 만듭니다.
2. 목록에 있는 각 레스토랑의 등급을 조사하는 `for` 루프를 추가합니다. 
- 평점이 "우수"인 경우 `excellent_restaurants` 문자열에 레스토랑 이름을 추가한 다음 끝에 * 문자를 추가하여 각 레스토랑 이름을 구분합니다. 
- 평점이 "매우 좋음"인 경우 `very_good_restaurants` 문자열에 레스토랑 이름을 추가한 다음 끝에 * 문자를 추가합니다.
- 평점이 "좋음"인 경우 `good_restaurants` 문자열에 레스토랑 이름을 추가한 다음 끝에 * 문자를 추가합니다.
3. 반환되는 레스토랑 추천 수를 카테고리당 4개로 제한합니다.

최종 통화는 이렇게 이루어집니다.

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}
{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}
{% assign excellent_restaurants = “” %}
{% assign very_good_resturants = “” %}
{% assign good_restaurants = “” %}
{% for list in restaurants %}
{% if {{list.restaurant.user_rating.rating_text}} == `Excellent` %}
{% assign excellent_restaurants = excellent_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user_rating.rating_text}} == `Very Good` %}
{% assign very_good_restaurants = very_good_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user_rating.rating_text}} == `Good` %}
{% assign good_restaurants = good_restaurants | append: list.restaurant.name | append: `*` %}
{% endif %}
{% endfor %}
{% assign excellent_array = excellent_restaurants | split: `*` %}
{% assign very_good_array = very_good_restaurants | split: `*` %}
{% assign good_array = good_restaurants | split: `*` %}

Excellent places
{% for list in excellent_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Very good places
{% for list in very_good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Good places
{% for list in good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}
```
{% endraw %}

아래 스크린샷에서 사용자 기기에 응답이 표시되는 방식에 대한 예를 참조하세요.

![][5]{: style="max-width:30%;"}

## 고려 사항

사용 가능한 리소스와 사용 사례에 적합한 추천 엔진을 결정할 때는 이 고려 사항 표를 참조하세요.

| 고려 사항 | Liquid | 카탈로그 CSV | 카탈로그 API | 연결된 콘텐츠 |
| --- | --- | --- | --- | --- |
| 데이터 포인트를 소비하지 않습니다. | 지원되지 않음 | 지원 | 지원 | 지원 |
| 코드 솔루션 없음 | 지원되지 않음 | 사전 생성된 Liquid의 경우 지원 | 지원되지 않음 | 지원되지 않음 |
| 고급 Liquid가 자주 필요함 | 지원 | 지원되지 않음 | 지원되지 않음 | 지원 |
| 제품 피드 내 데이터 업데이트 | 지원되지 않음 | 권장 사항이 자주 업데이트되지 않는 경우 지원됩니다. | 권장 사항이 최대 매시간 업데이트되는 경우 지원됩니다. | 지원 및 권장 사항은 실시간으로 업데이트됩니다. |
| Braze UI 내에서 추천 생성 | 지원 | 지원 | 지원 | Braze 외부에서 생성된 경우 지원되지 않습니다. |
| 권장 사항 데이터 호스팅, 관리, 문제 해결 없음 | 지원 | 지원 | 지원 | 지원되지 않음 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

[1]: {% image_buster /assets/img/recs/catalog_items.png %}
[2]: {% image_buster /assets/img/recs/content_card_preview.png %}
[3]: {% image_buster /assets/img/recs/on_click_behavior.png %}
[4]: {% image_buster /assets/img/recs/custom_attributes_test.png %}
[5]: {% image_buster /assets/img/recs/sample_response.png %}