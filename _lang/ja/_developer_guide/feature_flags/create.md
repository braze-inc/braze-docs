---
nav_title: フィーチャーフラグを作成する
article_title: フィーチャーフラグを作成する
page_order: 20
description: "このリファレンス記事では、新機能のロールアウトを調整するために機能フラグを作成する方法について説明する。"
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# 機能フラグを作成する

> フィーチャーフラグを使用すると、選択したユーザーに対してリモートで機能を有効または無効にすることができます。Brazeダッシュボードで新しい機能フラグを作成する。名前と `ID`、ターゲットオーディエンス、およびこの機能を有効にするユーザーの割合を指定します。その後、アプリまたは Web サイトのコードで同じ `ID` を使用して、ビジネスロジックの特定の部分を条件付きで実行できます。機能フラグおよび Braze での使用方法の詳細については、[機能フラグについて]({{site.baseurl}}/developer_guide/feature_flags/)を参照してください。

## 前提条件

### SDKバージョン

フィーチャーフラグを使用するには、少なくとも以下の最小バージョン以上の最新の SDK を使用するようにしてください。

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

### Braze 権限

ダッシュボードでフィーチャーフラグを管理するには、管理者であるか、次の [[権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)] を持っている必要があります。

| 許可                                                                    | あなたにできること                           |
|-------------------------------------------------------------------------------|-------------------------------------------|
| **フィーチャーフラグを管理する**                                                      | 機能フラグを表示、作成、編集する。     |
| **アクセスキャンペーン、キャンバス、カード、フィーチャーフラッグ、セグメント、メディアライブラリー** | 利用可能な機能フラグのリストを見る。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## フィーチャー・フラッグを作成する

### ステップ 1:新しいフィーチャー・フラッグを作成する

[**メッセージング**] > [**フィーチャーフラグ**] に進み、[**フィーチャーフラグを作成**] を選択します。

![Braze ダッシュボード で以前に作成された機能フラグのリスト]({% image_buster /assets/img/feature_flags/feature-flags-list.png %}){: style="max-width:75%"}

### ステップ 2:詳細を記入する

**Details（詳細）**」で、機能フラグの名前、ID、説明を入力する。

| フィールド        | 説明                                                                                                                                                                                                         |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 名前         | マーケティング担当者や管理者が読みやすいタイトル。                                                                                                                                                       |
| ID           | この機能が[ユーザーに対して有効か](#enabled)どうかをチェックするために、コード内で使用する一意のID。このIDは後で変更できないので、続ける前に[ID命名のベストプラクティスを](#naming-conventions)確認してほしい。 |
| 説明  | フィーチャーフラグに関するいくつかのコンテキストを提供するオプションの説明。                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### ステップ 3:カスタムプロパティを作成する

**Properties（プロパティ）**」で、機能が有効になっているときにアプリがBraze SDKを通じてアクセスできるカスタムプロパティを作成する。各変数には、文字列、ブール値、画像、タイムスタンプ、JSON、数値を割り当てることができ、デフォルトの値を設定することもできます。

{% tabs local %}
{% tab 例 %}
次の例では、フィーチャーフラグが、リストされたカスタムプロパティを使用して e コマースストアの在庫切れバナーを表示しています。 

|プロパティ名|タイプ|値|
|--|--|--|
|`banner_height`|`number`|`75`|
|`banner_color`|`string`|`blue`|
|`banner_text`|`string`|`Widgets are out of stock until July 1.`|
|`dismissible`|`boolean`|`false`|
|`homepage_icon`|`image`|`http://s3.amazonaws.com/[bucket_name]/`|
|`account_start`|`timestamp`|`2011-01-01T12:00:00Z`|
|`footer_settings`|`JSON`|`{ "colors": [ "red", "blue", "green" ], "placement": 123 }`|

{% alert tip %}
追加できるプロパティ数に制限はありません。ただし、フィーチャーフラグのプロパティは合計10 KB に制限されています。プロパティ値とキーの長さはともに255文字に制限されている。
{% endalert %}
{% endtab %}
{% endtabs %}

### ステップ 4:ターゲットとするセグメントを選ぶ

フィーチャーフラグをロールアウトする前に、ターゲットとするユーザーの[セグメント]({{site.baseurl}}/user_guide/engagement_tools/segments/)を選択する必要があります。**Add Filter**ドロップダウンメニューを使用して、ターゲットオーディエンスからユーザーをフィルタリングする。複数のフィルターを追加して、オーディエンスをさらに絞り込みます。

![2つのドロップダウンメニューがある。1つ目は「セグメント別ターゲットユーザー」です。2つ目は「追加のフィルター」です。]({% image_buster /assets/img/feature_flags/feature-flags-targeting.png %})

### ステップ5: ロールアウト・トラフィックを設定する {#rollout}

デフォルトでは、フィーチャーフラグは常に無効になっているため、機能リリースの日付とユーザーのアクティベーションの合計を切り離すことができます。ロールアウトを開始するには、**Rollout Traffic**スライダを使用するか、テキストボックスにパーセンテージを入力して、選択したセグメント内のランダムユーザーのパーセンテージを選択し、この新機能を受信します。

![Rollout Traffic というラベルが付いたスライダ。0 ～100 の間にまたがります。]({% image_buster /assets/img/feature_flags/feature-flags-rollout.png %}){: style="max-width:75%;"}

{% alert important %}
新機能の本番準備が整うまでは、ロールアウトのトラフィックを0％以上に設定しないこと。ダッシュボードで最初にフィーチャーフラグを定義する際、この設定は0％のままにします。
{% endalert %}

## 機能フラグの"enabled"フィールドの使用 {#enabled}

機能フラグを定義したら、それが特定のユーザーに対して有効かどうかをチェックするようにアプリやサイトを設定する。有効になったら、ユースケースに応じて何らかのアクションを設定するか、機能フラグの変数プロパティを参照する。Braze SDKは、機能フラグのステータスとそのプロパティをアプリに取り込むためのゲッターメソッドを提供する。 

フィーチャーフラグはセッション開始時に自動的に更新されるため、起動時に機能の最新バージョンを表示できます。SDKはこれらの値をキャッシュし、オフラインの状態でも使用できるようにする。 

{% alert note %}
[フィーチャーフラッグのインプレッション](#impressions)を必ず記録してください。
{% endalert %}

たとえば、アプリに新しいタイプのユーザープロファイルをロールアウトするとします。`ID` を `expanded_user_profile` に設定することもできます。次に、この新しいユーザープロファイルを特定のユーザーに表示するかどうかをアプリで確認します。以下に例を示します。

{% tabs %}
{% tab JavaScript %}

```javascript
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")
if featureFlag?.enabled == true {
  print("expanded_user_profile is enabled")
} else {
  print("expanded_user_profile is not enabled")
}
```
{% endtab %}
{% tab Java %}
```java
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.getEnabled()) {
  Log.i(TAG, "expanded_user_profile is enabled");
} else {
  Log.i(TAG, "expanded_user_profile is not enabled");
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag?.enabled == true) {
  Log.i(TAG, "expanded_user_profile is enabled.")
} else {
  Log.i(TAG, "expanded_user_profile is not enabled.")
}
```

{% endtab %}
{% tab React Native %}

```javascript
const featureFlag = await Braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Unity %}
```csharp
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.Enabled) {
  Console.WriteLine("expanded_user_profile is enabled");
} else {
  Console.WriteLine("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Cordova %}
```javascript
const featureFlag = await BrazePlugin.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);  
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```
{% endtab %}
{% tab Flutter %}
```dart
BrazeFeatureFlag? featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");
if (featureFlag?.enabled == true) {
  print("expanded_user_profile is enabled");
} else {
  print("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Roku %}
```brightscript
featureFlag = m.braze.getFeatureFlag("expanded_user_profile")
if featureFlag <> invalid and featureFlag.enabled
  print "expanded_user_profile is enabled"
else
  print "expanded_user_profile is not enabled"
end if
```
{% endtab %}
{% endtabs %}

### フィーチャーフラグのインプレッションをログに記録する {#impressions}

ユーザーが新しい機能を操作する機会があった場合、または機能が無効になっている場合 (AB テストのコントロールグループの場合) にユーザーが操作した__可能性がある__場合は、フィーチャーフラグのインプレッションを追跡します。フィーチャーフラグのインプレッションは、1セッションにつき1回のみ記録されます。 

通常、このコード行は、アプリ内でフィーチャーフラグを参照する場所の直下に置くことができます：

{% tabs %}
{% tab JavaScript %}

```javascript
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.logFeatureFlagImpression(id: "expanded_user_profile")
```

{% endtab %}
{% tab Java %}

```java
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.logFeatureFlagImpression("expanded_user_profile")
```

{% endtab %}
{% tab React Native %}

```javascript
Braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.LogFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Flutter %}
```dart
braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% endtabs %}

### プロパティにアクセスする {#accessing-properties}

フィーチャーフラグのプロパティにアクセスするには、ダッシュボードで定義したタイプに応じて、以下のメソッドのいずれかを使用します。

参照したプロパティが存在しない場合、これらのメソッドは`null` を返す。

{% tabs %}
{% tab JavaScript %}

```javascript
// Returns the Feature Flag instance
const featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
const stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
const booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
const numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
const imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a FeatureFlagJsonPropertyValue
const jsonProperty = featureFlag.getJsonProperty("footer_settings");
```

{% endtab %}
{% tab Swift %}

```swift
// Returns the Feature Flag instance
let featureFlag: FeatureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")

// Returns the String property
let stringProperty: String? = featureFlag.stringProperty(key: "color")

// Returns the boolean property
let booleanProperty: Bool? = featureFlag.boolProperty(key: "expanded")

// Returns the number property as a double
let numberProperty: Double? = featureFlag.numberProperty(key: "height")

// Returns the Unix UTC millisecond timestamp property as an integer
let timestampProperty : Int? = featureFlag.timestampProperty(key: "account_start")

// Returns the image property as a String of the image URL
let imageProperty : String? = featureFlag.imageProperty(key: "homepage_icon")

// Returns the JSON object property as a [String: Any] dictionary
let jsonObjectProperty : [String: Any]? = featureFlag.jsonObjectProperty(key: "footer_settings")
```

{% endtab %}
{% tab Java %}

```java
// Returns the Feature Flag instance
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
String stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
Boolean booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
Number numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
Long timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
String imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
JSONObject jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Returns the Feature Flag instance
val featureFlag = braze.getFeatureFlag("expanded_user_profile")

// Returns the String property
val stringProperty: String? = featureFlag.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = featureFlag.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = featureFlag.getNumberProperty("height")

// Returns the Unix UTC millisecond timestamp property as a long
val timestampProperty: Long? = featureFlag.getTimestampProperty("account_start")

// Returns the image property as a String of the image URL
val imageProperty: String?  = featureFlag.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = featureFlag.getJSONProperty("footer_settings")
```

{% endtab %}
{% tab React Native %}

```javascript
// Returns the String property
const stringProperty = await Braze.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await Braze.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await Braze.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await Braze.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await Braze.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await Braze.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Unity %}

```csharp
// Returns the Feature Flag instance
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.GetStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.GetBooleanProperty("expanded");

// Returns the number property as an integer
var integerProperty = featureFlag.GetIntegerProperty("height");

// Returns the number property as a double
var doubleProperty = featureFlag.GetDoubleProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
var timestampProperty = featureFlag.GetTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.GetImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
var jsonObjectProperty = featureFlag.GetJSONProperty("footer_settings");
```

{% endtab %}
{% tab Cordova %}

```javascript
// Returns the String property
const stringProperty = await BrazePlugin.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await BrazePlugin.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await BrazePlugin.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await BrazePlugin.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await BrazePlugin.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await BrazePlugin.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Flutter %}

```dart
// Returns the Feature Flag instance
BrazeFeatureFlag featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
var numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as an integer
var timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a Map<String, dynamic> collection
var jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endtab %}
{% tab Roku %}

```brightscript
' Returns the String property
color = featureFlag.getStringProperty("color")

' Returns the boolean property
expanded = featureFlag.getBooleanProperty("expanded")

' Returns the number property
height = featureFlag.getNumberProperty("height")

' Returns the Unix UTC millisecond timestamp property
account_start = featureFlag.getTimestampProperty("account_start")

' Returns the image property as a String of the image URL
homepage_icon = featureFlag.getImageProperty("homepage_icon")

' Returns the JSON object property
footer_settings = featureFlag.getJSONProperty("footer_settings")
```

{% endtab %}
{% endtabs %}

### すべてのフィーチャーフラグのリストを取得する {#get-list-of-flags}

{% tabs %}
{% tab JavaScript %}

```javascript
const features = getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Swift %}

```swift
let features = braze.featureFlags.featureFlags
for let feature in features {
  print("Feature: \(feature.id)", feature.enabled)
}
```

{% endtab %}
{% tab Java %}

```java
List<FeatureFlag> features = braze.getAllFeatureFlags();
for (FeatureFlag feature: features) {
  Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlags = braze.getAllFeatureFlags()
featureFlags.forEach { feature ->
  Log.i(TAG, "Feature: ${feature.id} ${feature.enabled}")
}
```

{% endtab %}
{% tab React Native %}

```javascript
const features = await Braze.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Unity %}

```csharp
List<FeatureFlag> features = Appboy.AppboyBinding.GetAllFeatureFlags();
foreach (FeatureFlag feature in features) {
  Console.WriteLine("Feature: {0} - enabled: {1}", feature.ID, feature.Enabled);
}
```

{% endtab %}
{% tab Cordova %}
```javascript
const features = await BrazePlugin.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```
{% endtab %}
{% tab Flutter %}
```dart
List<BrazeFeatureFlag> featureFlags = await braze.getAllFeatureFlags();
featureFlags.forEach((feature) {
  print("Feature: ${feature.id} ${feature.enabled}");
});
```
{% endtab %}
{% tab Roku %}
```brightscript
features = m.braze.getAllFeatureFlags()
for each feature in features
      print "Feature: " + feature.id + " enabled: " + feature.enabled.toStr()
end for
```
{% endtab %}
{% endtabs %}

### フィーチャーフラグを更新する {#refreshing}

セッションの途中で現在のユーザーの機能フラグを更新して、Brazeから最新の値を引き出すことができる。

{% alert tip %}
更新はセッション開始時に自動的に行われます。リフレッシュが必要なのは、チェックアウトページをロードする前や、機能フラグが参照されることがわかっている場合など、重要なユーザーアクションの前だけである。
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
braze.refreshFeatureFlags(() => {
  console.log(`Feature flags have been refreshed.`);
}, () => {
  console.log(`Failed to refresh feature flags.`);
});
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.requestRefresh { result in
  switch result {
  case .success(let features):
    print("Feature flags have been refreshed:", features)
  case .failure(let error):
    print("Failed to refresh feature flags:", error)
  }
}
```

{% endtab %}
{% tab Java %}

```java
braze.refreshFeatureFlags();
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.refreshFeatureFlags()
```

{% endtab %}
{% tab React Native %}

```javascript
Braze.refreshFeatureFlags();
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.RefreshFeatureFlags();
```

{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.refreshFeatureFlags();
```
{% endtab %}
{% tab Flutter %}
```dart
braze.refreshFeatureFlags();
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.refreshFeatureFlags()
```
{% endtab %}
{% endtabs %}

### 変更をリッスンする {#updates}

SDK がフィーチャーフラグを更新するときにアプリをリッスンして更新するように Braze SDK を構成できます。

これは、ユーザーがある機能を利用できなくなった場合に、アプリを更新したい場合に便利です。たとえば、ある機能が有効になっているかどうか、またはそのプロパティ値の1つに基づいて、アプリの状態を設定する場合です。

{% tabs %}
{% tab JavaScript %}

```javascript
// Register an event listener
const subscriptionId = braze.subscribeToFeatureFlagsUpdates((features) => {
  console.log(`Features were updated`, features);
});
// Unregister this event listener
braze.removeSubscription(subscriptionId);
```

{% endtab %}
{% tab Swift %}

```swift
// Create the feature flags subscription
// - You must keep a strong reference to the subscription to keep it active
let subscription = braze.featureFlags.subscribeToUpdates { features in
  print("Feature flags were updated:", features)
}
// Cancel the subscription
subscription.cancel()
```

{% endtab %}
{% tab Java %}

```java
braze.subscribeToFeatureFlagsUpdates(event -> {
  Log.i(TAG, "Feature flags were updated.");
  for (FeatureFlag feature: event.getFeatureFlags()) {
    Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
  }
});
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.subscribeToFeatureFlagsUpdates() { event ->
  Log.i(TAG, "Feature flags were updated.")
  event.featureFlags.forEach { feature ->
    Log.i(TAG, "Feature: ${feature.id}")
  }
}
```

{% endtab %}
{% tab React Native %}

```javascript
// Register an event listener
Braze.addListener(braze.Events.FEATURE_FLAGS_UPDATED, (featureFlags) => {
  console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```

{% endtab %}
{% tab Unity %}

変更をリッスンするには、[**Braze 構成**] > [**フィーチャーフラグ**] の [**Game オブジェクト名**] と [**Callback メソッド名**] の値を、アプリケーションの対応する値に設定します。

{% endtab %}
{% tab Cordova %}
```javascript
// Register an event listener
BrazePlugin.subscribeToFeatureFlagUpdates((featureFlags) => {
    console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```
{% endtab %}
{% tab Flutter %}

アプリのDartコードでは、以下のサンプル・コードを使用する：

```dart
// Create stream subscription
StreamSubscription featureFlagsStreamSubscription;

featureFlagsStreamSubscription = braze.subscribeToFeatureFlags((featureFlags) {
  print("Feature flags were updated");
});

// Cancel stream subscription
featureFlagsStreamSubscription.cancel();
```

次に、iOSのネイティブ・レイヤーにもこれらの変更を加える。Android のレイヤーには、追加のステップは必要ないことに注意してください。

1. [subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/subscribetoupdates(_:)) のドキュメントで説明されているように、`featureFlags.subscribeToUpdates` を実装してフィーチャーフラグの更新をサブスクライブします。

2. `featureFlags.subscribeToUpdates` コールバックの実装では `BrazePlugin.processFeatureFlags(featureFlags)` を呼び出す必要があります。

例としては [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift)を参照のこと。

{% endtab %}
{% tab Roku %}
```brightscript
' Define a function called `onFeatureFlagChanges` to be called when feature flags are refreshed
m.BrazeTask.ObserveField("BrazeFeatureFlags", "onFeatureFlagChanges")
```
{% endtab %}

{% tab React Hook %}
```typescript
import { useEffect, useState } from "react";
import {
  FeatureFlag,
  getFeatureFlag,
  removeSubscription,
  subscribeToFeatureFlagsUpdates,
} from "@braze/web-sdk";

export const useFeatureFlag = (id: string): FeatureFlag => {
  const [featureFlag, setFeatureFlag] = useState<FeatureFlag>(
    getFeatureFlag(id)
  );

  useEffect(() => {
    const listener = subscribeToFeatureFlagsUpdates(() => {
      setFeatureFlag(getFeatureFlag(id));
    });
    return () => {
      removeSubscription(listener);
    };
  }, [id]);

  return featureFlag;
};
```
{% endtab %}
{% endtabs %}

## 変更履歴を見る

フィーチャーフラグの変更ログを見るには、フィーチャーフラグを開き、[**変更ログ**] を選択します。

![機能フラグの「編集」ページ。「変更履歴」ボタンがハイライトされている。]({% image_buster /assets/img/feature_flags/changelog/open_changelog.png %}){: style="max-width:60%;"}

ここでは、いつ変更されたのか、誰が変更したのか、どのカテゴリーに属するのか、などを確認できます。

![]({% image_buster /assets/img/feature_flags/changelog/changelog.png %}) 選択した機能フラグの変更履歴。{: style="max-width:90%;"}

## フィーチャーフラグでセグメント化する {#segmentation}

Braze は、現在フィーチャーフラグが有効になっているユーザーを自動的に追跡します。[[**フィーチャーフラグ**] フィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#feature-flags) を使ってセグメントまたはターゲットメッセージングを作成できます。Segment s でのフィルター ing の詳細については、[Segmentの作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)を参照してください。

![フィルター検索バーに「フィーチャーフラグ」と入力された「フィルター」セクション。]({% image_buster /assets/img/feature_flags/feature-flags-filter-name.png %}){: style="max-width:75%;"}

{% alert note %}
再帰的なセグメントを防ぐため、他のフィーチャーフラグを参照するセグメントを作成することはできない。
{% endalert %}

## ベストプラクティス

### ロールアウトをキャンバスや実験と一緒にしてはいけない

異なるエントリーポイントによってユーザーが有効になったり無効になったりするのを避けるには、ロールアウト・スライダーをゼロより大きな値に設定するか、キャンバスまたは実験で機能フラグを有効にする必要がある。ベストプラクティスとして、キャンバスや実験で機能フラグを使用する予定がある場合は、ロールアウトのパーセンテージをゼロにしておくこと。

### 命名規則

コードを明確で一貫性のあるものにするために、フィーチャー・フラグIDに名前をつけるときは、以下のフォーマットを使うことを検討しよう：

```plaintext
BEHAVIOR_PRODUCT_FEATURE
```

次のように置き換えます。

| placeholder | 説明                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| `BEHAVIOR`  | 機能の動作。コードでは、その動作がデフォルトで無効になっていることを確認し、機能フラグ名に`disabled` のような表現を使わないようにする。 |
| `PRODUCT`   | その機能が属する製品。                                                                                       |
| `FEATURE`    | 機能の名前。                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

`show` が動作、`animation_profile` が製品、`driver` が機能であるフィーチャーフラグの例を次に示します。

```plaintext
show_animation_profile_driver
```

### 計画を立てる

常に安全策を取る。オフスイッチを必要とする可能性のある新機能を検討する場合、新しいアプリのアップデートが必要だと気づくよりも、機能フラグ付きの新しいコードをリリースし、それを必要としない方が良い。

### 記述的にする

機能フラグに説明を追加する。これはBrazeのオプションフィールドであるが、利用可能な機能フラグを参照する際に、他の人が持つかもしれない質問に答えるのに役立つ。

- このフラッグの有効化と動作の責任者の連絡先詳細
- このフラグを無効にする必要がある場合
- このフラグが制御する新機能に関するドキュメントやメモへのリンク
- 依存関係や機能の使用方法に関する注意事項がある場合

### 古い機能フラグを整理する

私たちは皆、必要以上に長い間、100%のロールアウトで機能を放置してしまっています。

コード (および Braze ダッシュボード) をクリーンに保つために、すべてのユーザーがアップグレードを完了し、機能を無効にするオプションが不要になったら、コードベースから永久フィーチャーフラグを削除します。これは、開発環境の複雑さを軽減するだけでなく、機能フラグのリストを整理整頓するのにも役立つ。

