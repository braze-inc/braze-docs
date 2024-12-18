---
nav_title: 구매 기록
article_title: Roku용 구매 기록
platform: Roku
page_order: 3
page_type: reference
description: "이 페이지에서는 Braze SDK를 통해 Roku의 구매 이벤트를 기록하는 방법을 설명합니다."

---
 
# 구매 기록

> 인앱 구매를 기록하면 여러 매출원에서 시간 경과에 따른 매출을 추적하고 생애주기 가치에 따라 사용자를 세분화할 수 있습니다.

Braze는 여러 통화로 구매를 지원합니다. USD가 아닌 다른 통화로 신고한 구매는 신고한 날짜의 환율을 기준으로 대시보드에 USD로 표시됩니다.

구현하기 전에 [모범 사례]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection) 문서에서 커스텀 이벤트, 커스텀 속성 및 구매 이벤트에서 제공하는 세분화 옵션 예제를 검토하세요. 또한 [이벤트 이름 지정 규칙을]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/event_naming_conventions/) 숙지하는 것이 좋습니다.

## 구매 및 수익 추적

이 기능을 사용하려면 앱에서 구매에 성공한 후 이 메서드 호출을 추가합니다.

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity)
```

### 속성정보 추가

구매 정보와 함께 속성정보 사전을 전달하여 구매에 대한 메타데이터를 추가할 수 있습니다.

속성은 키-값 쌍으로 정의됩니다.  키는 `String` 오브젝트이고 값은 `String` 또는 `Integer`일 수 있습니다.

```brightscript
m.Braze.logPurchase("product_id", "currency_code", Double price, Integer quantity, {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```

### 주문 수준에서 구매 기록
제품 수준 대신 주문 수준에서 구매를 기록하려면 주문 이름 또는 주문 카테고리를 `product_id` 으로 사용하면 됩니다. 자세한 내용은 [구매 개체 사양을]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) 참조하세요. 

### REST API

REST API를 사용하여 구매 내역을 기록할 수도 있습니다. 자세한 내용은 [사용자 API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) 설명서를 참조하세요.

