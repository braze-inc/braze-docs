---
nav_title: 分析
article_title: Xamarin 向けの分析
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 4
description: "この記事では、Xamarin プラットフォームの iOS、Android、および FireOS の分析について説明します。"

---
 
# Xamarin 分析

> Xamarin プラットフォーム用の分析を生成および確認する方法について説明します。

## セッショントラッキング

Braze SDK では、ユーザーエンゲージメントやユーザーの理解に不可欠なその他の分析を計算するため、Braze ダッシュボードで使用されるセッションデータがレポートされます。次のセッションセマンティクスに基づいて、このSDKは「スタートセッション」と「クローズセッション」データポイントを生成します。これは、Braze ダッシュボード内で表示可能なセッションの長さと数を考慮します。

ユーザー ID を設定したり、セッションを開始したりするには、ユーザー ID パラメーターを受け取る `ChangeUser` メソッドを使用します。

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).ChangeUser("user_id");
```

いつ、どのようにユーザー IDを設定、変更するかについて詳しくは、[Android積分命令]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/)を参照してください。

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.ChangeUser("user_id");
```

ユーザー IDの設定および変更方法の詳細については、[iOS 統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/)を参照してください。

{% endtab %}
{% endtabs %}

## カスタムイベントのログ記録

`LogCustomEvent` を使用してBrazeでカスタムイベントs を録音し、アプリの使用パターンの詳細を確認したり、ダッシュボードのアクションs でユーザーs をSegmentしたりできます。

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogCustomEvent("event_name");
```

イベントトラッキングのベストプラクティスとインターフェイスの詳細については、[Android の統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)を参照してください。

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogCustomEvent("event_name");
```

イベントトラッキングのベストプラクティスとインターフェイスの詳細については、[iOS 統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)を参照してください。

{% endtab %}
{% endtabs %}

## 購入のロギング

`LogPurchase` を使用してアプリ内での購入を記録して、売上を経時的にトラッキングしたり、売上源を横断してトラッキングしたりできます。また、ユーザーを生涯価値でセグメント化することもできます。

Braze は複数の通貨での購入に対応しています。米ドル以外の通貨でレポートする購入は、レポートされた日付の為替レートに基づいて米ドル単位でダッシュボードに表示されます。

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogPurchase("product_id", "USD", new Java.Math.BigDecimal(3.50));
```

売上のトラッキングのベストプラクティスとインターフェイスの詳細については、[Android の統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/)を参照してください。

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogPurchase("product_id", "USD", 3.50);
```

売上のトラッキングのベストプラクティスとインターフェイスの詳細については、[iOS の統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/)を参照してください。

{% endtab %}
{% endtabs %}

### 注文レベルで購入を記録する

商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。 

### 予約済みのキー

以下のキーは予約されているため、購入プロパティとして使用**できません**。

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## カスタム属性を記録する

Braze には、ユーザーに属性を割り当てるメソッドが用意されています。ダッシュボード上のこれらの属性に従って、ユーザーのフィルター処理とセグメント化を行うことができます。

### デフォルトのユーザー属性

Braze が自動収集したユーザー属性を割り当てるには、SDK に付属のセッターメソッドを使用します。たとえば、ユーザーの名を設定できます。

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetFirstName("first_name");
```

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetFirstName("first_name");
```

{% endtab %}
{% endtabs %}

以下の属性がサポートされています。

- 名
- 姓
- 性別
- 生年月日
- 市区町村
- 国
- 電話番号
- メール

### カスタムユーザー属性

Braze は、定義済みのユーザー属性メソッドに加えて、`SetCustomUserAttribute` を使用してアプリケーションのデータを追跡するカスタム属性も提供しています。

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetCustomUserAttribute("custom_attribute_key", true);
```

属性のトラッキングのベストプラクティスとインターフェイスの詳細については、[Android の統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/)を参照してください。

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

属性のトラッキングのベストプラクティスとインターフェイスの詳細については、[iOS の統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/)を参照してください。

{% endtab %}
{% endtabs %}

## 位置情報の追跡

ログと"トラッキング 分析の例については、[ Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/MainActivity.cs) および[iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/MainPage.xaml.cs) のサンプルアプリを参照してください。

{% tabs %}
{% tab Android %}
詳細については、[Android の統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/)を参照してください。
{% endtab %}

{% tab ios %}
ローカルトラッキングをサポートするには、[ iOS を参照してください。バックグラウンドの場所](http://developer.xamarin.com/guides/cross-platform/application_fundamentals/backgrounding/part_4_ios_backgrounding_walkthroughs/location_walkthrough/)と[iOS統合命令]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/locations_and_geofences/)を使用します。
{% endtab %}
{% endtabs %}

