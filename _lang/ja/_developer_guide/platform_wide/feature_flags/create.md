---
nav_title: 機能フラグの作成
article_title: 機能フラグの作成
page_order: 20
description: "この参考記事では、新機能のロールアウトを調整するための機能フラグの作成方法について説明します。"
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# 機能フラグの作成

> 機能フラグを使用すると、選択したユーザーの機能をリモートで有効または無効にできます。Braze ダッシュボード内に新しい機能フラグを作成します。名前、ターゲットユーザー、およびこの機能を有効にするユーザーの割合を指定します。`ID`そして、`ID`それをアプリやウェブサイトのコードで使用することで、ビジネスロジックの特定の部分を条件付きで実行できます。

フィーチャーフラグとは何か、Braze でどのように使用できるかについて詳しく知りたいですか？先に進む前に [機能フラグについて] [5] を確認してください。

## 前提条件

機能フラグを使用するには、SDK が少なくとも次の最低バージョンで最新であることを確認してください。

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## ダッシュボードに機能フラグを実装する

**[**メッセージング**] > [機能フラグ] から機能フラグを作成、編集、アーカイブします。**このページには、このワークスペースの既存の機能フラグのリストが表示されます。

{% alert note %}
[古いナビゲーションを使用している場合は、[]({{site.baseurl}}/navigation)**エンゲージメント**] **の下に機能フラグが表示されます**。
{% endalert %}

![Braze ダッシュボードで以前に作成された機能フラグのリスト] [1]{: style="max-width:75%"}

### アクセス許可 {#permissions}

機能フラグを表示、作成、編集するには、「機能フラグの管理」[権限] [9] が必要です。使用可能な機能フラグのリストを表示するには、「キャンペーン、キャンバス、カード、フィーチャーフラッグ、セグメント、メディアライブラリへのアクセス」権限が必要です。

{% alert note %}
管理者ユーザーは自動的に機能フラグを管理するためのアクセス権を持ちます。制限付きユーザーの場合、**ワークスペースレベルでManage Feature Flagsへのアクセスを明示的に許可または制限できます**。これは、特定のユーザーが特定の環境またはビジネスユニットの機能フラグのみを変更できるようにしたい場合に便利です。
{% endalert %}

![機能フラグの管理権限] [8]{: style="max-width:60%"}

### 新しい機能フラグの作成

新しい機能フラグを作成するには、[**機能フラグの作成**] ボタンをクリックします。次に、[機能フラグの詳細](#details)、[プロパティ](#properties)、[ユーザーターゲティング](#targeting)、[およびロールアウトトラフィックを定義します](#rollout-traffic)。

![空白の機能フラグフォーム] [2]{: style="float:right;max-width:55%;margin-left:15px;"}

#### 詳細

新しい機能フラグに [**名前] と [****ID**] を指定します。

* **名前フィールドでは**、マーケティング担当者や管理者が使用するこの機能フラグのタイトルを人間が読めるように指定できます。
* **ID** フィールドはコード内で参照され、特定のユーザーに対してこの機能が有効になっているかどうかが判断されます。これは一意でなければならず、作成後は変更できません。
* **説明フィールドは**、この機能フラグに関する追加のコンテキストを提供できるオプションフィールドです。

`ID`は機能を開発する際に使用されるため、慎重に選択してください。コードが同僚 (および将来の自分) に読めるように、適切な命名規則を実践してください。

たとえば、`enable_rider_new_profile_page`機能フラグを有効にするとどうなるかを明確にするために`{verb}_{product}_{feature}`、という命名規則を使用するのが一般的です。

{% alert important %}
プロダクションアプリの動作を損なわないようにするには、`ID`機能フラグは一意でなければならず、作成後は変更できません。 

機能フラグはワークスペース内のアプリ間で共有されるため、さまざまなプラットフォーム (iOS)/Android/Web) can share references to the same feature.
{% endalert %}

#### [プロパティ] {#properties}

カスタムプロパティはフィーチャーフラグの一部として定義できます。これらのプロパティは、機能が有効になると、Braze SDK を介してアプリからアクセスできるようになります。プロパティの定義はオプションの手順です。

**変数には、**文字列**、**ブーリアン値**、または数値を使用できます。**各プロパティの変数キーとデフォルト値の両方を定義します。

##### プロパティの例

たとえば、eコマースストアの在庫切れバナーを表示する機能フラグを定義する場合、バナーを表示するときにアプリが使用する次のプロパティを設定できます。

|プロパティ名|タイプ|値|
|--|--|--|
|`banner_height`|`number`|`75`|
|`banner_color`|`string`|`blue`|
|`banner_text`|`string`|`Widgets are out of stock until July 1.`|
|`dismissible`|`boolean`|`false`|

{% alert tip %}
追加できるプロパティの数に制限はありませんが、機能フラグのプロパティは合計で 10 kB に制限されています。プロパティ値とキーはいずれも 255 文字に制限されています。
{% endalert %}

#### ターゲット設定

機能フラグのロールアウトを開始するには、[特定のユーザーセグメントを選択する必要があります]({{site.baseurl}}/user_guide/engagement_tools/segments/)。

「**フィルターを追加**」ドロップダウンメニューを使用して、ユーザーをターゲットオーディエンスから除外します。複数のフィルターを追加して対象者を絞り込みます。

![2 つのドロップダウンメニュー。最初は「セグメント別のターゲットユーザー」です。二つ目は「その他のフィルター」です。] [3]

#### ロールアウトトラフィック {#rollout}

機能フラグは常にオフの状態で開始されるため、ユーザーエクスペリエンスにおける機能のリリースとアクティベーションのタイミングを分けることができます。 

新機能をロールアウトする準備ができたら、オーディエンスを指定し、**ロールアウトトラフィックスライダーを使用して**、ターゲットとするユーザーベースのうち、新機能を受け取るユーザーの割合をランダムに定義します。**ロールアウトトラフィックスライダーを設定して**、0% (ユーザーなし) から 100% (ターゲットオーディエンス全体) までの割合を設定します。 

![0 から 100 までの範囲の [ロールアウトトラフィック] というラベルの付いたスライダ。] [4]

{% alert tip %}
新機能を公開する準備ができるまで、ロールアウトトラフィックを 0% 以上に設定しないでください。ダッシュボードで最初に機能フラグを定義するときは、この設定を 0% のままにしてください。
{% endalert %}

## アプリケーション内で機能フラグが有効になっているかどうかを確認してください {#enabled}

機能フラグを定義したら、特定のユーザーに対して有効になっているかどうかを確認するようにアプリまたはサイトを構成します。有効になったら、アクションを設定するか、ユースケースに基づいて機能フラグの変数プロパティを参照します。Braze SDK には、機能フラグのステータスとそのプロパティをアプリに取り込むためのゲッターメソッドが用意されています。 

機能フラグはセッションの開始時に自動的に更新されるため、起動時に機能の最新バージョンを表示できます。SDK はこれらの値をキャッシュして、オフラインでも使用できるようにします。 

{% alert note %}
[フィーチャーフラグのインプレッションは必ず記録してください](#impressions)。
{% endalert %}

たとえば、アプリに新しいタイプのユーザープロファイルを導入するとします。`ID`をとして設定することもできます`expanded_user_profile`。次に、この新しいユーザープロファイルを特定のユーザーに表示する必要があるかどうかをアプリに確認させます。以下に例を示します。

{% tabs %}
{% tab JavaScript %}

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
{% tab Java %}
```java
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag.getEnabled()) {
  Log.i(TAG, "expanded_user_profile is enabled");
} else {
  Log.i(TAG, "expanded_user_profile is not enabled");
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag.enabled) {
  Log.i(TAG, "expanded_user_profile is enabled.")
} else {
  Log.i(TAG, "expanded_user_profile is not enabled.")
}
```

{% endtab %}
{% tab React Native %}

```javascript
const featureFlag = await Braze.getFeatureFlag("expanded_user_profile");
if (featureFlag.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Unity %}
```csharp
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");
if (featureFlag.Enabled) {
  Console.WriteLine("expanded_user_profile is enabled");
} else {
  Console.WriteLine("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Cordova %}
```javascript
const featureFlag = await BrazePlugin.getFeatureFlag("expanded_user_profile");
if (featureFlag.enabled) {
  console.log(`expanded_user_profile is enabled`);  
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```
{% endtab %}
{% tab Flutter %}
```dart
BrazeFeatureFlag featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");
if (featureFlag.enabled) {
  print("expanded_user_profile is enabled");
} else {
  print("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Roku %}
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

### 機能フラグのインプレッションを記録する {#impressions}

ユーザーが新機能を操作する機会があったとき、__または機能が無効になっていれば操作できたはずのときに__、機能フラグのインプレッションを追跡します（A/B テストのコントロールグループの場合）。

通常、アプリの機能フラグを参照する場所のすぐ下に次のコード行を置くことができます。

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

### プロパティへのアクセス {#accessing-properties}

機能フラグのプロパティにアクセスするには、ダッシュボードで定義したタイプに応じて、次のいずれかの方法を使用します。

機能フラグが有効になっていない場合、または参照するプロパティが存在しない場合、これらのメソッドが返されます`null`。

{% tabs %}
{% tab JavaScript %}

```javascript
// Feature flag instance
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
// String properties
const stringProperty = featureFlag.getStringProperty("color");
// Boolean properties
const booleanProperty = featureFlag.getBooleanProperty("expanded");
// Number properties
const numberProperty = featureFlag.getNumberProperty("height");
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
```

{% endtab %}
{% tab Java %}

```java
// Feature flag instance
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
// String properties
String stringProperty = featureFlag.getStringProperty("color");
// Boolean properties
Boolean booleanProperty = featureFlag.getBooleanProperty("expanded");
// Number properties
Number numberProperty = featureFlag.getNumberProperty("height");
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// feature flag instance
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
// string properties
val stringProperty = featureFlag.getStringProperty("color")
// boolean properties
val booleanProperty = featureFlag.getBooleanProperty("expanded")
// number properties
val numberProperty = featureFlag.getNumberProperty("height")
```

{% endtab %}
{% tab React Native %}

```javascript
// String properties
const stringProperty = await Braze.getFeatureFlagStringProperty("expanded_user_profile", "color");
// Boolean properties
const booleanProperty = await Braze.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");
// Number properties
const numberProperty = await Braze.getFeatureFlagNumberProperty("expanded_user_profile", "height");
```

{% endtab %}
{% tab Unity %}

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
{% tab Cordova %}

```javascript
// String properties
const stringProperty = await BrazePlugin.getFeatureFlagStringProperty("expanded_user_profile", "color");
// Boolean properties
const booleanProperty = await BrazePlugin.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");
// Number properties
const numberProperty = await BrazePlugin.getFeatureFlagNumberProperty("expanded_user_profile", "height");
```
{% endtab %}
{% tab Flutter %}
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
{% tab Roku %}
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

有効になっているすべての機能フラグのリストを取得することもできます。

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

### 機能フラグを更新 {#refreshing}

セッション中に現在のユーザーの機能フラグを更新して、Braze から最新の値を取得できます。

{% alert tip %}
更新は、セッションの開始時に自動的に行われます。更新が必要なのは、チェックアウトページを読み込む前など、重要なユーザーアクションの前、または機能フラグが参照されることがわかっている場合のみです。
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


### 変化に耳を傾ける {#updates}

SDK がいずれかの機能フラグを更新したときにアプリをリッスンして更新するように Braze SDK を設定できます。

これは、ユーザーが機能を利用できなくなった場合にアプリを更新する場合に便利です。たとえば、機能が有効になっているかどうかや、そのプロパティ値のいずれかに基づいてアプリの状態を設定します。

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

変更を確認するには、**Braze 設定** > **機能フラグの** [**ゲームオブジェクト名****] と [コールバックメソッド名**] の値を、アプリケーションの対応する値に設定します。

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

アプリの Dart コードでは、次のサンプルコードを使用してください。

\`\`\`dart
// ストリームサブスクリプションを作成
ストリームサブスクリプション機能はストリームサブスクリプションにフラグを付けます。

featureFlagsStreamSubscription = braze.subscribeToFeatureFlags((featureFlags) {
  print("Feature flags were updated");
});

// ストリームのサブスクリプションをキャンセル
featureFlagsStreamSubscription.cancel();
\`\`\`

次に、iOS ネイティブレイヤーでもこれらの変更を行います。Android レイヤーでは追加の手順は必要ないことに注意してください。

1. [SubscribeTouUpdates ドキュメンテーションで説明されているように、`featureFlags.subscribeToUpdates`機能フラグの更新を購読するように実装してください](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/subscribetoupdates(_:))。

2. `featureFlags.subscribeToUpdates` コールバックの実装では `BrazePlugin.processFeatureFlags(featureFlags)` を呼び出す必要があります。

例については、サンプルアプリの [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) を参照してください。

{% endtab %}
{% tab Roku %}
```brightscript
' Define a function called `onFeatureFlagChanges` to be called when feature flags are refreshed
m.BrazeTask.ObserveField("BrazeFeatureFlags", "onFeatureFlagChanges")
```
{% endtab %}

{% tab React Hook %}
\`\`\`typescript
import { useEffect, useState } from "react";
import {
  フィーチャーフラグ、
  機能フラグを取得、
  購読を削除、
  機能フラグの更新を購読し、
}」@braze /web-sdk「から;

export const useFeatureFlag = (id: string):FeatureFlag => {
  const [featureFlag, setFeatureFlag] = useState<FeatureFlag>(
    getFeatureFlag(id)
  );

  useEffect(() => {
    const listener = subscribeToFeatureFlagsUpdates(() => {
      setFeatureFlag(getFeatureFlag(id));
    });
    return () => {
      removeSubscription(listener);
    ()
  }, [id]);

  リターン機能フラグ;
()
\`\`\`
{% endtab %}
{% endtabs %}

## 機能フラグによるセグメンテーション {#segmentation}

{% alert note %}
Feature Flagのメンバーシップフィルターは徐々に展開されており、まだダッシュボードに表示されていない可能性があります。
{% endalert %}

Braze は、現在どのユーザーが機能フラグの対象になっているか、どのユーザーが機能フラグに参加しているかを自動的に追跡します。[\*\*機能フラグ**フィルター] [6] を使用してセグメントまたはターゲットメッセージを作成できます。セグメントでのフィルタリングの詳細については、[セグメントの作成] [7] を参照してください。

{% alert note %}
再帰的なセグメントを防ぐため、他の機能フラグを参照するセグメントを作成することはできません。
{% endalert %}

## ベストプラクティス

### ロールアウトとキャンバスや実験を組み合わせないでください

さまざまなエントリポイントによってユーザーが有効または無効になるのを防ぐには、ロールアウトスライダーをゼロより大きい値に設定するか、キャンバスまたは実験で機能フラグを有効にする必要があります。ベストプラクティスとして、キャンバスや実験で機能フラグを使用する予定の場合は、ロールアウト率をゼロに保つことをお勧めします。

### 命名規則

- 次のようなパターンに従うことを検討してください`{product}.{feature}.{action}`。 
  - たとえば、配車アプリでは、機能 ID は次のようになります。 `driver.profile.show_animation_v3`
- これは、特定の製品分野やチームの機能フラグを検索する場合にも役立ちます。
- アプリ内で機能フラグのデフォルト状態が無効になっていることを確認してください。
  - たとえば、`disable_feature_xyz`という名前のフラグがある場合はアンチパターンになります。例外もあるかもしれませんが、機能の「有効」状態と実際に有効になっている動作 (機能 XYZ を無効にする) を混同しないようにしてください。

### 前もって計画する

常に安全にプレイしてください。オフスイッチが必要な新機能を検討するときは、新しいアプリの更新が必要だと気付くよりも、機能フラグを付けて新しいコードをリリースし、必要ない方がよいでしょう。

### 説明文を書く

機能フラグに説明を追加します。これはBrazeのオプションフィールドですが、利用可能な機能フラグを閲覧するときに他の人が抱くかもしれない質問に答えるのに役立ちます。

- このフラグの有効化と動作の責任者の連絡先
- このフラグを無効にするべき場合
- このフラグが制御する新機能に関するドキュメントまたはメモへのリンク
- 機能の使用方法に関する依存関係や注意事項

### 古い機能フラグをクリーンアップ

100% ロールアウト時に必要以上に長く機能をオンのままにしておくのは、私たち全員の罪悪感です。

コード (および Braze ダッシュボード) をきれいに保つため、すべてのユーザーがアップグレードして機能を無効にするオプションが不要になったら、コードベースから恒久的な機能フラグを削除してください。これにより、開発環境の複雑さが軽減されるだけでなく、機能フラグのリストが整理されます。

[1]: {% image_buster /assets/img/feature_flags/feature-flags-list.png %}
[2]: {% image_buster /assets/img/feature_flags/feature-flags-create.png %}
[3]: {% image_buster /assets/img/feature_flags/feature-flags-targeting.png %}
[4]: {% image_buster /assets/img/feature_flags/feature-flags-rollout.png %}
[5]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/about/
[6]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#feature-flag
[7]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[8]: {% image_buster /assets/img/feature_flags/feature-flags-manage-permission.png %}
[9]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/
