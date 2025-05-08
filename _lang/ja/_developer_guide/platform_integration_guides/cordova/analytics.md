---
nav_title: 分析
article_title: 分析の統合
page_order: 3
---

# 分析の統合

> Cordova Braze SDK の分析を統合する方法を学びます。

{% multi_lang_include cordova/prerequisites.md %}

## カスタムイベントのログ記録

カスタムイベントをログに記録するには、`logCustomEvent()` メソッドを使用します。詳細な手順については、カスタムイベントのログ記録に関する [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events) および [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) ガイドを参照してください。

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logCustomEvent("CUSTOM_EVENT_WITH_PROPERTIES", properties);
```

## 購入のロギング

購入をログに記録するには、`logPurchase()` メソッドを使用します。詳細な手順については、購入のログ記録に関する [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases) および [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/) ガイドを参照してください。

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% alert tip %}
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。
{% endalert %}

## カスタム属性の設定

カスタム属性を設定するには、`setCustomUserAttribute()` メソッドを使用します。詳細な手順については、カスタム属性の設定に関する [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) および [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/) ガイドを参照してください。

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```

## ユーザー ID の設定

ユーザー ID を設定するには、`changeUser()` メソッドを使用します。詳細な手順については、ユーザー ID の設定に関する [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) および [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) ガイドを参照してください。

```javascript
BrazePlugin.changeUser("USER_ID");
```
