---
nav_title: 구매 기록
article_title: 웹용 구매 기록
platform: Web
page_order: 4
page_type: reference
description: "이 문서에서는 웹용 구매를 기록하고 해당 구매에 속성을 추가하는 방법에 대해 설명합니다."

---
 
# 구매 기록

> 인앱 구매를 기록하면 여러 매출원에서 시간 경과에 따른 매출을 추적하고 생애주기 가치에 따라 사용자를 세분화할 수 있습니다. 

Braze는 여러 통화로 구매를 지원합니다. USD가 아닌 다른 통화로 신고한 구매는 신고한 날짜의 환율을 기준으로 대시보드에 USD로 표시됩니다.

구현하기 전에 [모범 사례]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#user-data-collection)에서 커스텀 이벤트, 커스텀 속성 및 구매 이벤트가 제공하는 세분화 옵션의 예제를 검토하세요.

이 기능을 사용하려면 앱에서 구매 성공 후 [`logPurchase()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) 호출을 앱에 추가하세요. `quantity` 은 100보다 작거나 같아야 합니다.

```javascript
braze.logPurchase(product_id, price, "USD", quantity);
```

## 속성정보 추가

[이벤트 속성 배열을]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#nested-objects) 전달하거나 구매 정보와 함께 키-값 쌍의 객체를 전달하여 구매에 대한 [메타데이터를](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) 추가할 수 있습니다. 

#### 개체 서식 지정

키는 `string` 오브젝트이고 값은 `string`, `numeric`, `boolean` 또는 `Date`일 수 있습니다.

```javascript
braze.logPurchase(product_id, price, "USD", quantity, {key: "value"});
```

#### 주문 수준에서 구매 기록
제품 수준 대신 주문 수준에서 구매를 기록하려면 주문 이름 또는 주문 카테고리를 `product_id` 으로 사용하면 됩니다. 자세한 내용은 [구매 개체 사양을]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) 참조하세요. 

## REST API

REST API를 사용하여 구매 내역을 기록할 수도 있습니다. 자세한 내용은 [사용자 API]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data) 설명서를 참조하세요.

