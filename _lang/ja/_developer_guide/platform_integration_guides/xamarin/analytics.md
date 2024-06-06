---
nav_title: 分析
article_title: Analytics for Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 4
description: "この記事では、Xamarin プラットフォームの iOS、Android、FireOS 分析について説明します。"

---
 
# Xaraminアナリティクス

> この記事では、Xamarin の分析を処理する方法について説明します。

## ユーザー ID の設定

{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(context).ChangeUser("YOUR_USER_ID");
```

ユーザー ID をいつ、どのように設定および変更するかについての詳細な説明については、 [Android 統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) を参照してください。

{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance().ChangeUser("YOUR_USER_ID");
```

ユーザーIDをいつ、どのように設定および変更するかについての詳細な説明については、 [iOS統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/) を参照してください。
{% endtab %}
{% endtabs %}

## カスタムイベントのトラッキング
{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(context).LogCustomEvent("YOUR_EVENT_NAME");
```

イベント トラッキングのおすすめの方法とインターフェースの詳細については、 [Android の統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) をご覧ください。
{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance ().LogCustomEvent ("YOUR_EVENT_NAME");
```

**実装例** - `logCustomEvent` [TestApp.XamariniOS](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-unified/TestApp.XamariniOS) サンプル アプリケーション内で`AppboySampleViewController.cs`使用されます。

イベントトラッキングのベストプラクティスとインターフェースの詳細については、 [iOS統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/) を参照してください。
{% endtab %}
{% endtabs %}

## 購入のロギング
{% tabs %}
{% tab Android %}
```csharp
Braze.getInstance(context).LogPurchase("product_id", 100);
```

収益トラッキングのおすすめの方法とインターフェースの詳細については、 [Android の統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases=) をご覧ください。
{% endtab %}
{% tab iOS %}
```csharp
// C#
Appboy.SharedInstance ().LogPurchase ("product_id", "USD", new NSDecimalNumber("10"));
```

**実装例** \- サンプル・アプリケーションの `EventsAndPurchasesButtonHandler` メソッド `AppboySampleViewController.cs`でユーザー・プロパティが設定されているのを、 .

収益トラッキングのベストプラクティスとインターフェースの詳細については、 [iOS統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/logging_purchases/) を参照してください。
{% endtab %}
{% endtabs %}

### 注文レベルで購入を記録する
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。 

## カスタム属性の設定
{% tabs %}
{% tab %}
```csharp
Braze.getInstance(context).CurrentUser.SetFirstName("FirstName");
```

属性トラッキングのおすすめの方法とインターフェースの詳細については、 [Android の統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) をご覧ください。
{% endtab %}
{% tab iOS %}

```csharp
// C#
Appboy.SharedInstance ().User.FirstName = "YOUR_NAME";
```

**実装例** \- サンプル・アプリケーションの `UserPropertyButtonHandler` メソッド `AppboySampleViewController.cs`でユーザー・プロパティが設定されているのを、 .

属性トラッキングのベストプラクティスとインターフェースの詳細な説明については、 [iOS統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/) を参照してください。
{% endtab %}
{% endtabs %}

## 位置情報の追跡

- Android :位置追跡をサポートする方法については、 [Android 統合手順][2] を参照してください。
- iOS:位置追跡をサポートする方法については、 [バックグラウンドでの位置情報を使用した][11] Xamarin のチュートリアルと [iOS 統合の手順][12] を参照してください。

[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/#location-tracking
[11]: http://developer.xamarin.com/guides/cross-platform/application_fundamentals/backgrounding/part_4_ios_backgrounding_walkthroughs/location_walkthrough/
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/locations_and_geofences/
