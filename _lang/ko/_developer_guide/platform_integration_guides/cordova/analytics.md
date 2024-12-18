---
nav_title: 분석
article_title: 애널리틱스 통합
page_order: 3
---

# 애널리틱스 통합

> Cordova Braze SDK용 분석을 통합하는 방법을 알아보세요.

{% multi_lang_include cordova/prerequisites.md %}

## 사용자 지정 이벤트 로깅

사용자 지정 이벤트를 기록하려면 `logCustomEvent()` 메서드를 사용합니다. 보다 자세한 지침은 사용자 지정 이벤트 로깅을 위한 [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events) 및 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) 가이드를 참조하세요.

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logCustomEvent("CUSTOM_EVENT_WITH_PROPERTIES", properties);
```

## 구매 기록

구매를 기록하려면 `logPurchase()` 방법을 사용합니다. 자세한 지침은 구매 기록에 대한 [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases) 및 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/) 가이드를 참조하세요.

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% alert tip %}
제품 수준 대신 주문 수준에서 구매를 기록하려면 주문 이름 또는 주문 카테고리를 `product_id` 으로 사용하면 됩니다. 자세한 내용은 [구매 개체 사양을]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) 참조하세요.
{% endalert %}

## 사용자 지정 속성 설정

사용자 지정 속성을 설정하려면 `setCustomUserAttribute()` 방법을 사용합니다. 자세한 지침은 [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) 및 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/) 가이드의 커스텀 속성 설정을 참조하세요.

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```

## 사용자 ID 설정

사용자 ID를 설정하려면 `changeUser()` 방법을 사용합니다. 보다 자세한 지침은 사용자 아이디 설정에 대한 [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) 및 [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) 가이드를 참조하세요.

```javascript
BrazePlugin.changeUser("USER_ID");
```
