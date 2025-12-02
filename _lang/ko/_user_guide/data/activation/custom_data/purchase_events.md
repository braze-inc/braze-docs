---
nav_title: 구매 이벤트
article_title: 구매 이벤트
page_order: 8
page_type: reference
description: "이 참조 문서에서는 구매 이벤트 및 속성정보, 사용 방법, 세분화, 관련 분석을 볼 수 있는 위치 등에 대해 설명합니다."
search_rank: 3
---

# 구매 이벤트

> 이 페이지에서는 구매 이벤트 및 속성정보, 사용 방법, 세분화, 관련 분석을 볼 수 있는 위치 등에 대해 설명합니다.

구매 이벤트는 사용자가 취한 구매 행동으로, 인앱 구매를 기록하고 각 고객 프로필의 생애주기 가치(LTV)를 설정하는 데 사용됩니다. 이러한 이벤트는 팀에서 설정해야 합니다. 구매 이벤트를 기록하면 수량, 유형과 같은 속성을 추가할 수 있으므로 이러한 속성을 기반으로 사용자를 타겟팅할 수 있습니다.

## 구매 이벤트 기록

[`/users/track` 엔드포인트를]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 통해 [구매 개체를]({{site.baseurl}}/api/objects_filters/purchase_object/) 전달하거나 아래 나열된 SDK 라이브러리 중 하나를 사용하여 구매를 기록할 수 있습니다.

다음은 구매를 기록하는 데 사용되는 다양한 플랫폼의 방법을 나열한 것입니다. 이 페이지에서는 구매 이벤트에 속성정보와 수량을 추가하는 방법에 대한 설명서도 확인할 수 있습니다. 이러한 속성을 기반으로 사용자를 추가로 타겟팅할 수 있습니다.

- [Android 및 FireOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=swift)
- [웹]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=unity)
- [.NET MAUI]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=roku)

## 구매 데이터 보기

구매 이벤트를 설정하고 로깅을 시작한 후에는 [개요 탭의]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab) 사용자 프로필에서 이 구매 데이터를 볼 수 있습니다.

## 구매 데이터 사용

Braze에서 구매 데이터를 사용할 수 있는 방법은 여러 가지가 있습니다:

- **[세그먼트 세분화](#purchase-event-segmentation):** 구매 데이터를 사용하여 구매 행동에 기반한 사용자 세그먼트를 생성하세요.
- **[개인화](#personalization):** 구매 데이터를 사용하여 사용자에게 개인화된 메시지를 전달하세요.
- **[트리거된 메시지](#trigger-messages):** 구매 이벤트에 따라 트리거될 메시지를 설정하세요.
- **[분석](#analytics):** 구매 데이터를 분석하여 사용자 행동과 마케팅 캠페인의 효과에 대한 인사이트를 얻으세요.

### 세그먼트 세분화 {#purchase-event-segmentation}

기록된 구매 이벤트를 기반으로 원하는 수 또는 유형의 후속 캠페인을 트리거할 수 있습니다. 예를 들어, 지난 30일 동안 구매한 사용자 세그먼트 또는 특정 금액 이상을 지출한 사용자 세그먼트를 만들 수 있습니다.

사용자를 타겟팅할 때 다음과 같은 세분화 필터를 사용할 수 있습니다:

- 첫 구매
- 앱 첫 구매
- 마지막으로 구매한 제품
- 지출한 돈
- 구매한 제품
- 총 구매 횟수
- Y일 동안 지출한 X 금액
- Y일 동안 구매한 X 제품 수
- Y일 내 X 구매 속성정보
- 지난 Y일 동안의 X 구매

각 필터에 대한 자세한 내용은 [세분화 필터]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) 용어집을 참조하고 '구매 행동'을 기준으로 필터링하세요.

\![정확히 세 번 구매한 사용자에 대한 필터링]({% image_buster /assets/img/purchase_filter_example.gif %}){: style="max-width:80%;"}

{% alert tip %}
특정 구매가 발생한 횟수를 기준으로 세그먼트화하려면 해당 구매를 [증가하는 커스텀 속성으로]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage) 개별적으로 기록합니다.
{% endalert %}

### 개인화

사용자로부터 수집하는 다른 유형의 데이터와 마찬가지로, 구매 데이터를 사용하여 Liquid를 통해 메시징을 개인화할 수 있습니다. 예를 들어, 방금 구매한 제품과 유사한 제품을 추천하는 개인화된 이메일을 사용자에게 보낼 수 있습니다.

사용자가 마지막으로 구매한 제품의 이름을 저장하는 `last_purchased_product` 이라는 구매 이벤트 속성정보가 있다고 가정해 보겠습니다. 이 속성을 사용하여 다음과 같이 이메일 메시지를 개인화할 수 있습니다:

{% raw %}

```liquid
{% if ${last_purchased_product} == "Running Shoes" %}
  We hope you're enjoying your new running shoes! Based on your recent purchase, you might also like these running shorts and water bottles.
{% elsif ${last_purchased_product} == "Yoga Mat" %}
  We hope you're enjoying your new yoga mat! Based on your recent purchase, you might also like these yoga blocks and straps.
{% else %}
  Thank you for your recent purchase! We hope you're enjoying your new item.
{% endif %}
```

{% endraw %}

이 예제에서는 `last_purchased_product` 속성을 기반으로 메시징이 개인화됩니다. 사용자가 마지막으로 구매한 제품이 '러닝화'였다면 러닝 반바지와 물병을 추천하는 메시징을 받게 됩니다. 마지막 제품이 '요가 매트'였다면 요가 블록과 스트랩을 추천하는 메시징을 받게 됩니다. `last_purchased_product` 이면 일반적인 감사 메시지를 받게 됩니다.

### 트리거된 메시지

일반적인 사용 사례는 사용자가 구매할 때 이메일과 같은 메시지를 자동으로 전송하는 것입니다. 예를 들어 감사 메시지나 향후 구매에 대한 할인 코드를 보낼 수 있습니다.

이렇게 하려면 액션 기반 캠페인 또는 캔버스를 만든 다음 트리거 동작을 **구매로** 설정합니다. 구매한 제품이나 구매 금액 등 트리거에 대한 추가 조건을 지정할 수도 있습니다.

또한 Liquid로 트리거된 메시지를 개인화할 수도 있습니다. 다음 예제에서 `${purchase_product_name}` 는 구매 제품의 이름을 저장하는 실제 속성 이름으로 대체할 커스텀 속성으로, Braze 설정에 저장됩니다.

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

### 분석

세분화를 위한 구매 측정기준을 추적하는 것 외에도 Braze는 각 제품의 구매 횟수 및 시간 경과에 따른 매출도 기록합니다. 이는 가장 인기 있는 제품을 식별하거나 프로모션 캠페인이 매출에 미치는 영향을 측정하는 데 유용할 수 있습니다.

이 데이터는 [매출 보고서]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) 페이지에서 확인할 수 있습니다.

### 매출 계산 이해하기

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>측정기준</th>
            <th>정의</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">평생 매출</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">사용자당 생애주기 가치</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">일 평균 매출</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics#daily-purchases">일일 구매</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">사용자당 일일 매출</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

#### 평생 매출 계산

Braze는 구매 이벤트를 사용하여 사용자의 생애주기 매출(생애주기 가치 또는 LTV라고도 함)을 계산하는데, 이는 향후 고객과의 전체 관계에 귀속되는 순이익을 예측한 것입니다. 이를 통해 고객 확보 및 유지 전략에 대한 정보에 입각한 의사 결정을 내릴 수 있습니다.

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$  

사용자의 LTV를 이해하기 위해 참고할 수 있는 두 가지 주요 위치가 Braze에 있습니다:

- 각 앱과 사이트의 생애주기별 *매출* 및 *사용자당 생애주기 가치와* 같은 전반적인 측정기준은 [매출 보고서를]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data) 참조하세요.
- 특정 사용자의 평생 매출을 파악하려면 해당 사용자의 [고객 프로필을]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab) 참조하세요.

##### 환불이 평생 매출에 미치는 영향

구매 이벤트를 사용하여 구매 데이터를 추적하는 경우, 구매 이벤트 속성이 음수인 Braze 구매 이벤트를 `price` 로깅하여 환불을 추적해야 합니다. 이 접근 방식은 평생 매출에 대한 정확한 총계를 유지합니다.

단, 환불은 추가 구매 이벤트에 포함된다는 점에 유의하세요. 다음 예시를 살펴보겠습니다. Sam은 $12에 첫 구매를 했지만 구매 금액의 일부를 반품하여 $5를 환불받습니다. Sam의 프로필이 기록됩니다:

- 12달러의 가격으로 1건 구매
- 5달러의 가격으로 1건 구매
- 평생 매출 $7

샘의 프로필에는 두 번의 구매 이벤트가 있지만 실제로는 한 번만 구매했습니다. 사용자의 구매 횟수를 중심으로 구축된 세그먼트나 사용 사례가 있는 경우 이를 고려하는 것이 중요합니다. 지속적인 환불은 고객 프로필의 구매 횟수를 부풀릴 수 있습니다.

## 구매 이벤트 속성정보 {#purchase-properties}

구매 이벤트 속성을 사용하면 구매에 대한 속성을 설정하여 트리거 조건을 더욱 세분화하고, 메시징의 개인화를 강화하며, 로데이터 내보내기를 통해 보다 정교한 분석을 생성할 수 있습니다. 속성 값 유형(문자열, 숫자, 부울 값, 날짜)은 플랫폼마다 다르며 키-값 쌍으로 할당되는 경우가 많습니다.

예를 들어, 전자상거래 애플리케이션이 있고 구매 후 사용자에게 메시지를 보내려는 경우, `brand_name` 이라는 구매 이벤트 속성정보를 추가하여 타겟 오디언스를 추가로 개선하고 캠페인 개인화를 강화할 수 있습니다.

**구매 이벤트 속성정보를 기반으로 트리거하는 예시입니다:**

!!! 헤드폰마트와 같은 브랜드명을 가진 헤드폰을 구매하는 사용자에게 캠페인을 전송하는 실행 기반 전달 설정]({% image_buster /assets/img/purchase2.png %}){: style="max-width:80%;margin-left:15px;"}

자세한 내용은 [구매 속성정보 개체를]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object) 참조하세요.

### 이벤트 속성정보 세분화

이벤트 속성정보 세분화를 사용하면 발생한 커스텀 이벤트뿐만 아니라 해당 이벤트와 관련된 속성을 기반으로 사용자를 타겟팅할 수 있습니다. 이 기능은 구매 및 커스텀 이벤트를 세분화할 때 추가 필터링 옵션을 추가합니다.

\![]({% image_buster /assets/img/nested_object3.png %}){: style="max-width:80%;margin-left:15px;"}

이러한 세분화 필터에는 다음이 포함됩니다:
- 지난 Y일 동안 값이 V인 속성 Y의 커스텀 이벤트를 X회 수행했습니다.
- 지난 Y일 동안 가치가 V인 속성 Y를 X번 구매했습니다.
- 모든 구매, 이벤트, 구매 및 이벤트 내 속성에 1~30일 세그먼트 추가

세그먼트 [확장과]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) 달리 사용되는 세그먼트는 실시간으로 업데이트되고, 세그먼트 수에 제한이 없으며, 최대 30일의 조회 기록을 제공하고, 데이터 포인트가 발생합니다. 추가 데이터 포인트 요금이 부과되므로 Braze 고객 성공 매니저에게 문의하여 커스텀 이벤트에 대한 이벤트 속성정보를 사용 설정해야 합니다.

승인되면 대시보드의 **데이터 설정** > **커스텀 이벤트** 아래에서 **속성 관리를** 선택하여 추가 속성을 추가할 수 있습니다. 그런 다음 캠페인의 타겟팅 단계 또는 캔버스 빌더에서 이러한 이벤트 속성정보를 사용할 수 있습니다.

### 캔버스 항목 속성 및 이벤트 속성정보

{% multi_lang_include canvas_entry_event_properties.md %}

### 주문 수준에서 구매 기록

제품 수준 대신 주문 수준에서 구매를 기록하려면 주문 이름 또는 주문 카테고리를 `product_id` 으로 사용합니다. 자세한 내용은 [구매 개체 사양을]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) 참조하세요. 

### 제품 ID 명명 규칙

Braze에서는 구매 객체에 대한 몇 가지 일반적인 명명 규칙을 제공합니다 `product_id`. `product_id` 을 선택할 때 Braze는 모든 로깅된 항목을 이 `product_id` 으로 그룹화하려는 의도로 제품 이름 또는 제품 카테고리와 같은 간단한 이름을 사용할 것을 제안합니다.

이를 통해 제품을 쉽게 식별하여 세그먼트를 세분화하고 트리거할 수 있습니다. 

## 구매 이벤트 차단 목록

때때로 너무 많은 데이터 포인트를 기록하거나 마케팅 전략에 더 이상 유용하지 않거나 오류로 기록된 구매 이벤트를 식별할 수 있습니다. 엔지니어링 팀이 앱이나 웹사이트의 백엔드에서 해당 데이터를 제거하는 작업을 하는 동안 이 데이터가 Braze로 전송되지 않도록 하려면 커스텀 데이터 오브젝트를 차단 목록에 추가하면 됩니다.

Braze 대시보드의 **데이터 설정** > 제품에서 차단 목록을 관리할 수 있습니다. 자세한 내용은 [고객 데이터 관리하기를]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/) 참조하세요.

