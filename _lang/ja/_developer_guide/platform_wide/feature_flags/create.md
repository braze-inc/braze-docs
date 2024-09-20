---
nav_title: フィーチャー・フラグを作成する
article_title: フィーチャー・フラグを作成する
page_order: 20
description: "このリファレンス記事では、新機能のロールアウトを調整するために機能フラグを作成する方法について説明する。"
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# 機能フラグを作成する

> 機能フラグにより、選択したユーザーに対してリモートで機能を有効または無効にすることができる。Brazeダッシュボードで新しい機能フラグを作成する。名前と`ID` 、対象読者、この機能を有効にするユーザーの割合を指定する。そして、アプリやウェブサイトのコードで同じ`ID` 、ビジネスロジックの特定の部分を条件付きで実行することができる。機能フラグについての詳細と、Brazeでの使用方法については、\[機能フラグについて][5] を参照のこと。

## 前提条件

### SDKバージョン

機能フラグを使用するには、SDKが少なくとも以下の最小バージョンで最新であることを確認すること：

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

### ブレイズ・パーミッション

ダッシュボードで機能フラグを管理するには、管理者であるか、以下の\[パーミッション][9] ：

| 許可                                                                    | あなたにできること                           |
|-------------------------------------------------------------------------------|-------------------------------------------|
| **機能フラグを管理する**                                                      | 機能フラグを表示、作成、編集する。     |
| **アクセスキャンペーン、キャンバス、カード、フィーチャーフラッグ、セグメント、メディアライブラリー** | 利用可能な機能フラグのリストを見る。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## フィーチャー・フラッグを作成する

### ステップ 1:新しいフィーチャー・フラッグを作成する

**Messaging**>**Feature Flagsに**進み、**Create Feature Flagを**選択する。

![Brazeダッシュボードで過去に作成した機能フラグのリスト][1]{: style="max-width:75%"}

### ステップ2:詳細を記入する

**Details（詳細）**」で、機能フラグの名前、ID、説明を入力する。

| フィールド        | 説明                                                                                                                                                                                                         |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 名前         | マーケティング担当者や管理者が読みやすいタイトル。                                                                                                                                                       |
| ID           | この機能が[ユーザーに対して有効か](#enabled)どうかをチェックするために、コード内で使用する一意のID。このIDは後で変更できないので、続ける前に[ID命名のベストプラクティスを](#naming-conventions)確認してほしい。 |
| 説明  | オプションの説明で、あなたの機能フラグについて説明する。                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### ステップ 3:カスタムプロパティを作成する

**Properties（プロパティ）**」で、機能が有効になっているときにアプリがBraze SDKを通じてアクセスできるカスタムプロパティを作成する。各変数には、文字列、ブーリアン、画像、タイムスタンプ、JSON、数値の値を割り当てることができ、デフォルト値を設定することもできる。

{% tabs local %}
{% tab 例 %}
次の例では、機能フラグが、リストされたカスタムプロパティを使って、eコマースストアの在庫切れバナーを表示している： 

|物件名|タイプ|価値|
|--|--|--|
|`banner_height`|`number`|`75`|
|`banner_color`|`string`|`blue`|
|`banner_text`|`string`|`Widgets are out of stock until July 1.`|
|`dismissible`|`boolean`|`false`|
|`homepage_icon`|`image`|`http://s3.amazonaws.com/[bucket_name]/`|
|`account_start`|`timestamp`|`2011-01-01T12:00:00Z`|
|`footer_settings`|`JSON`|`{ "colors": [ "red", "blue", "green" ], "placement": 123 }`|

{% alert tip %}
追加できる物件数に制限はない。ただし、フィーチャー・フラグのプロパティは合計10kBに制限されている。プロパティ値とキーの長さはともに255文字に制限されている。
{% endalert %}
{% endtab %}
{% endtabs %}

### ステップ 4:ターゲットとするセグメントを選ぶ

機能フラグを展開する前に、ターゲットとするユーザー[セグメントを]({{site.baseurl}}/user_guide/engagement_tools/segments/)選ぶ必要がある。**Add Filter**ドロップダウンメニューを使用して、ターゲットオーディエンスからユーザーをフィルタリングする。複数のフィルターを追加して、視聴者をさらに絞り込む。

![2つのドロップダウンメニューがある。1つ目は「セグメント別ターゲットユーザー」である。2つ目は「Additional Filters」である。][3]

### ステップ 5: ロールアウト・トラフィックを設定する {#rollout}

機能フラグはデフォルトで常に無効になっているため、機能リリースの日付とユーザーのアクティベーションの合計を切り離すことができる。ロールアウトを開始するには、「**ロールアウトトラフィック」**スライダーを使用して、選択したセグメントでこの新機能を受け取るランダムユーザーの割合を選択する。

![Rollout Traffic（ロールアウト・トラフィック）と書かれたスライダーで、0から100の間で設定する。][4]

{% alert important %}
新機能の本番準備が整うまでは、ロールアウトのトラフィックを0％以上に設定しないこと。ダッシュボードで最初にフィーチャー・フラッグを定義する際、この設定は0％のままにしておく。
{% endalert %}

## フィーチャー・フラグを検証する {#enabled}

機能フラグを定義したら、それが特定のユーザーに対して有効かどうかをチェックするようにアプリやサイトを設定する。有効になったら、ユースケースに応じて何らかのアクションを設定するか、機能フラグの変数プロパティを参照する。Braze SDKは、機能フラグのステータスとそのプロパティをアプリに取り込むためのゲッターメソッドを提供する。 

機能フラグはセッション開始時に自動的に更新されるため、起動時に機能の最新バージョンを表示することができる。SDKはこれらの値をキャッシュし、オフラインの状態でも使用できるようにする。 

{% alert note %}
[フィーチャーフラッグのインプレッションを](#impressions)必ず記録すること。
{% endalert %}

例えば、あなたのアプリで新しいタイプのユーザープロファイルを展開するとしよう。`ID` を`expanded_user_profile` と設定することもできる。そして、アプリにこの新しいユーザー・プロファイルを特定のユーザーに表示すべきかどうかをチェックさせる。以下に例を示します。

{% tabs %}
{% tab ジャバスクリプト %}

```javascript
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")
if featureFlag.enabled {
  print("expanded_user_profile is enabled")
} else {
  print("expanded_user_profile is not enabled")
}
```
{% endtab %}
{% tab ジャワ %}
```java
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag.getEnabled()) {
  Log.i(TAG, "expanded_user_profile is enabled");
} else {
  Log.i(TAG, "expanded_user_profile is not enabled");
}
```

{% endtab %}
{% tab コトリン %}

```kotlin
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag.enabled) {
  Log.i(TAG, "expanded_user_profile is enabled.")
} else {
  Log.i(TAG, "expanded_user_profile is not enabled.")
}
```

{% endtab %}
{% tab リアクト・ネイティブ %}

```javascript
const featureFlag = await Braze.getFeatureFlag("expanded_user_profile");
if (featureFlag.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab 団結 %}
```csharp
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");
if (featureFlag.Enabled) {
  Console.WriteLine("expanded_user_profile is enabled");
} else {
  Console.WriteLine("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab コルドバ %}
```javascript
const featureFlag = await BrazePlugin.getFeatureFlag("expanded_user_profile");
if (featureFlag.enabled) {
  console.log(`expanded_user_profile is enabled`);  
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```
{% endtab %}
{% tab フラッター %}
```dart
BrazeFeatureFlag featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");
if (featureFlag.enabled) {
  print("expanded_user_profile is enabled");
} else {
  print("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab ロク %}
```brightscript
featureFlag = m.braze.getFeatureFlag("expanded_user_profile")
if featureFlag.enabled
  print "expanded_user_profile is enabled"
else
  print "expanded_user_profile is not enabled"
end if
```
{% endtab %}
{% endtabs %}

### 機能フラグの印象をログに記録する {#impressions}

ユーザーが新機能とインタラクションする機会があったとき、または機能が無効になっている場合（A/Bテストのコントロールグループの場合）にインタラクションする__可能性が__あったときはいつでも、機能フラグのインプレッションをトラッキングする。フィーチャー・フラグのインプレッションは、1セッションにつき1回のみ記録される。 

通常、このコード行は、アプリ内で機能フラグを参照する場所の直下に置くことができる：

{% tabs %}
{% tab ジャバスクリプト %}

```javascript
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.logFeatureFlagImpression(id: "expanded_user_profile")
```

{% endtab %}
{% tab ジャワ %}

```java
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab コトリン %}

```kotlin
braze.logFeatureFlagImpression("expanded_user_profile")
```

{% endtab %}
{% tab リアクト・ネイティブ %}

```javascript
Braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab 団結 %}

```csharp
Appboy.AppboyBinding.LogFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab コルドバ %}
```javascript
BrazePlugin.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab フラッター %}
```dart
braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab ロク %}
```brightscript
m.Braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% endtabs %}

### プロパティにアクセスする {#accessing-properties}

フィーチャー・フラグのプロパティにアクセスするには、ダッシュボードで定義したタイプに応じて、以下のメソッドのいずれかを使用する。

機能フラグが有効でない場合、または参照するプロパティが存在しない場合、これらのメソッドは`null` を返す。

{% tabs %}
{% tab ジャバスクリプト %}

```javascript
// Feature flag instance
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
// String properties
const stringProperty = featureFlag.getStringProperty("color");
// Boolean properties
const booleanProperty = featureFlag.getBooleanProperty("expanded");
// Number properties
const numberProperty = featureFlag.getNumberProperty("height");
// returns the property as a number in milliseconds
const timestampProperty = featureFlag.getTimestampProperty("account_start");
// returns the property as a string of the image URL
const imageProperty = featureFlag.getImageProperty("homepage_icon");
// returns the JSON property as as JSON object 
const jsonProperty = featureFlag.getJsonProperty("footer_settings");
```

{% endtab %}
{% tab Swift %}

```swift
// Feature flag instance
let featureFlag: FeatureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")
// String properties
let stringProperty: String? = featureFlag.stringProperty(key: "color")
// Boolean properties
let booleanProperty: Bool? = featureFlag.boolProperty(key: "expanded")
// Number properties
let numberProperty: Double? = featureFlag.numberProperty(key: "height")
// returns the property as a TimeInterval in milliseconds
let timestampProperty : Int? = featureFlag.timestampProperty(key: "account_start")
// returns the property as a string of the image URL 
let imageProperty : String? = featureFlag.imageProperty(key: "homepage_icon")
// returns the property as a [String: Any] dictionary
let jsonObjectProperty : [String: Any]? = featureFlag.jsonObjectProperty(key: "footer_settings")
```

{% endtab %}
{% tab ジャワ %}

```java
// Feature flag instance
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
// String properties
String stringProperty = featureFlag.getStringProperty("color");
// Boolean properties
Boolean booleanProperty = featureFlag.getBooleanProperty("expanded");
// Number properties
Number numberProperty = featureFlag.getNumberProperty("height");
// returns the property as a nullable long in milliseconds
Long timestampProperty = featureFlag.getTimestampProperty("account_start");
// returns the property as a string of the image URL 
String imageProperty = featureFlag.getImageProperty("homepage_icon");
// returns the property as a JSON Object
JSONObject jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endtab %}
{% tab コトリン %}

```kotlin
// feature flag instance
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
// string properties
val stringProperty: String? = featureFlag.getStringProperty("color")
// boolean properties
val booleanProperty: Boolean? = featureFlag.getBooleanProperty("expanded")
// number properties
val numberProperty: Number? = featureFlag.getNumberProperty("height")
// returns the property as a nullable long in milliseconds
val timestampProperty: Long? = featureFlag.getTimestampProperty("account_start")
// returns the property as a string of the image URL 
val String imageProperty: String?  = featureFlag.getImageProperty("homepage_icon")
// returns the property as a JSON Object
val jsonObjectProperty: JSONObject? = featureFlag.getJSONProperty("footer_settings")
```

{% endtab %}
{% tab リアクト・ネイティブ %}

```javascript
// String properties
const stringProperty = await Braze.getFeatureFlagStringProperty("expanded_user_profile", "color");
// Boolean properties
const booleanProperty = await Braze.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");
// Number properties
const numberProperty = await Braze.getFeatureFlagNumberProperty("expanded_user_profile", "height");
```

{% endtab %}
{% tab 団結 %}

```csharp
// Feature flag instance
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");
// String properties
var stringProperty = featureFlag.getStringProperty("color");
// Boolean properties
var booleanProperty = featureFlag.getBooleanProperty("expanded");
// Number property as integer
var integerProperty = featureFlag.getIntegerProperty("height");
// Number property as double
var doubleProperty = featureFlag.getDoubleProperty("height");
```
{% endtab %}
{% tab コルドバ %}

```javascript
// String properties
const stringProperty = await BrazePlugin.getFeatureFlagStringProperty("expanded_user_profile", "color");
// Boolean properties
const booleanProperty = await BrazePlugin.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");
// Number properties
const numberProperty = await BrazePlugin.getFeatureFlagNumberProperty("expanded_user_profile", "height");
```
{% endtab %}
{% tab フラッター %}
```dart
BrazeFeatureFlag featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");
// String properties
var stringProperty = featureFlag.getStringProperty("color");
// Boolean properties
var booleanProperty = featureFlag.getBooleanProperty("expanded");
// Number properties
var numberProperty = featureFlag.getNumberProperty("height");
```
{% endtab %}
{% tab ロク %}
```brightscript
' String properties
color = featureFlag.getStringProperty("color")
' Boolean properties
expanded = featureFlag.getBooleanProperty("expanded")
' Number properties
height = featureFlag.getNumberProperty("height")
```
{% endtab %}
{% endtabs %}

### すべての機能フラグのリストを取得する {#get-list-of-flags}

{% tabs %}
{% tab ジャバスクリプト %}

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
{% tab ジャワ %}

```java
List<FeatureFlag> features = braze.getAllFeatureFlags();
for (FeatureFlag feature: features) {
  Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
}
```

{% endtab %}
{% tab コトリン %}

```kotlin
val featureFlags = braze.getAllFeatureFlags()
featureFlags.forEach { feature ->
  Log.i(TAG, "Feature: ${feature.id} ${feature.enabled}")
}
```

{% endtab %}
{% tab リアクト・ネイティブ %}

```javascript
const features = await Braze.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab 団結 %}

```csharp
List<FeatureFlag> features = Appboy.AppboyBinding.GetAllFeatureFlags();
foreach (FeatureFlag feature in features) {
  Console.WriteLine("Feature: {0} - enabled: {1}", feature.ID, feature.Enabled);
}
```

{% endtab %}
{% tab コルドバ %}
```javascript
const features = await BrazePlugin.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```
{% endtab %}
{% tab フラッター %}
```dart
List<BrazeFeatureFlag> featureFlags = await braze.getAllFeatureFlags();
featureFlags.forEach((feature) {
  print("Feature: ${feature.id} ${feature.enabled}");
});
```
{% endtab %}
{% tab ロク %}
```brightscript
features = m.braze.getAllFeatureFlags()
for each feature in features
      print "Feature: " + feature.id + " enabled: " + feature.enabled.toStr()
end for
```
{% endtab %}
{% endtabs %}

### 機能フラグをリフレッシュする {#refreshing}

セッションの途中で現在のユーザーの機能フラグを更新して、Brazeから最新の値を引き出すことができる。

{% alert tip %}
リフレッシュはセッション開始時に自動的に行われる。リフレッシュが必要なのは、チェックアウトページをロードする前や、機能フラグが参照されることがわかっている場合など、重要なユーザーアクションの前だけである。
{% endalert %}

{% tabs %}
{% tab ジャバスクリプト %}

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
{% tab ジャワ %}

```java
braze.refreshFeatureFlags();
```

{% endtab %}
{% tab コトリン %}

```kotlin
braze.refreshFeatureFlags()
```

{% endtab %}
{% tab リアクト・ネイティブ %}

```javascript
Braze.refreshFeatureFlags();
```

{% endtab %}
{% tab 団結 %}

```csharp
Appboy.AppboyBinding.RefreshFeatureFlags();
```

{% endtab %}
{% tab コルドバ %}
```javascript
BrazePlugin.refreshFeatureFlags();
```
{% endtab %}
{% tab フラッター %}
```dart
braze.refreshFeatureFlags();
```
{% endtab %}
{% tab ロク %}
```brightscript
m.Braze.refreshFeatureFlags()
```
{% endtab %}
{% endtabs %}

### 変化に耳を傾ける {#updates}

Braze SDKをリッスンし、SDKが機能フラグを更新したときにアプリを更新するように設定できる。

これは、ユーザーがある機能を利用できなくなった場合に、アプリをアップデートしたい場合に便利だ。例えば、ある機能が有効になっているかどうかや、そのプロパティ値の1つに基づいて、アプリの状態を設定する。

{% tabs %}
{% tab ジャバスクリプト %}

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
{% tab ジャワ %}

```java
braze.subscribeToFeatureFlagsUpdates(event -> {
  Log.i(TAG, "Feature flags were updated.");
  for (FeatureFlag feature: event.getFeatureFlags()) {
    Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
  }
});
```

{% endtab %}
{% tab コトリン %}

```kotlin
braze.subscribeToFeatureFlagsUpdates() { event ->
  Log.i(TAG, "Feature flags were updated.")
  event.featureFlags.forEach { feature ->
    Log.i(TAG, "Feature: ${feature.id}")
  }
}
```

{% endtab %}
{% tab リアクト・ネイティブ %}

```javascript
// Register an event listener
Braze.addListener(braze.Events.FEATURE_FLAGS_UPDATED, (featureFlags) => {
  console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```

{% endtab %}
{% tab 団結 %}

変更をリッスンするには、**「Braze Configuration**>**Feature Flags**」の「**Game Object Name**」と「**Callback Method Name**」の値を、アプリケーションの対応する値に設定する。

{% endtab %}
{% tab コルドバ %}
```javascript
// Register an event listener
BrazePlugin.subscribeToFeatureFlagUpdates((featureFlags) => {
    console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```
{% endtab %}
{% tab フラッター %}

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

次に、iOSのネイティブ・レイヤーにもこれらの変更を加える。アンドロイドのレイヤーでは、追加のステップは必要ない。

1. `featureFlags.subscribeToUpdates` を実装し、[subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/subscribetoupdates(_:))ドキュメントで説明されているように、機能フラグの更新を購読する。

2. `featureFlags.subscribeToUpdates` コールバックの実装では `BrazePlugin.processFeatureFlags(featureFlags)` を呼び出す必要があります。

例としては [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift)を参照のこと。

{% endtab %}
{% tab ロク %}
```brightscript
' Define a function called `onFeatureFlagChanges` to be called when feature flags are refreshed
m.BrazeTask.ObserveField("BrazeFeatureFlags", "onFeatureFlagChanges")
```
{% endtab %}

{% tab リアクトフック %}
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

機能フラグの変更履歴を見るには、機能フラグを開き、**Changelogを**選択する。

![機能フラグの「編集」ページ。「変更履歴」ボタンがハイライトされている。]({% image_buster /assets/img/feature_flags/changelog/open_changelog.png %}){: style="max-width:60%;"}

ここでは、いつ変更されたのか、誰が変更したのか、どのカテゴリーに属するのか、などを確認することができる。

![]({% image_buster /assets/img/feature_flags/changelog/changelog.png %}) 選択した機能フラグの変更履歴。{: style="max-width:90%;"}

## フィーチャー・フラグでセグメンテーションする {#segmentation}

Brazeは、現在どのユーザーが機能フラグの対象になっているか、または参加しているかを自動的に追跡する。[**Feature Flag**フィルターを使って]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#feature-flags)セグメントやターゲットメッセージングを作成できる。セグメントのフィルタリングの詳細については、\[セグメントの作成][7] を参照のこと。

![フィルター」セクションで、フィルター検索バーに「フィーチャー・フラッグ」と入力する。][10]

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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

`show` が動作、`animation_profile` が製品、`driver` が機能である：

```plaintext
show_animation_profile_driver
```

### 計画を立てる

常に安全策を取る。オフスイッチを必要とする可能性のある新機能を検討する場合、新しいアプリのアップデートが必要だと気づくよりも、機能フラグ付きの新しいコードをリリースし、それを必要としない方が良い。

### 説明的であること

機能フラグに説明を追加する。これはBrazeのオプションフィールドであるが、利用可能な機能フラグを参照する際に、他の人が持つかもしれない質問に答えるのに役立つ。

- このフラッグの有効化と動作の責任者の連絡先詳細
- このフラグを無効にする場合
- このフラグが制御する新機能に関するドキュメントやメモへのリンク
- 依存関係や機能の使用方法に関する注意事項がある場合

### 古い機能フラグを整理する

私たちは皆、100％ロールアウトした機能を必要以上に長く放置してしまう罪を犯している。

コード（およびBrazeダッシュボード）をクリーンに保つために、すべてのユーザーがアップグレードし、機能を無効にするオプションが不要になった後、コードベースから永久機能フラグを削除する。これは、開発環境の複雑さを軽減するだけでなく、機能フラグのリストを整理整頓するのにも役立つ。

[1]: {% image_buster /assets/img/feature_flags/feature-flags-list.png %}
[2]: {% image_buster /assets/img/feature_flags/feature-flags-create.png %}
[3]: {% image_buster /assets/img/feature_flags/feature-flags-targeting.png %}
[4]: {% image_buster /assets/img/feature_flags/feature-flags-rollout.png %}
[5]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/about/
[7]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[8]: {% image_buster /assets/img/feature_flags/feature-flags-manage-permission.png %}
[9]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/
[10]: {% image_buster /assets/img/feature_flags/feature-flags-filter-name.png %}
