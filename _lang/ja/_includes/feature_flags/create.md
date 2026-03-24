# フィーチャーフラグを作成する

> フィーチャーフラグを使用すると、選択したユーザーに対してリモートで機能を有効または無効にすることができます。Braze ダッシュボードで新しいフィーチャーフラグを作成します。名前と `ID`、ターゲットオーディエンス、およびこの機能を有効にするユーザーの割合を指定します。その後、アプリまたは Web サイトのコードで同じ `ID` を使用して、ビジネスロジックの特定の部分を条件付きで実行できます。フィーチャーフラグおよび Braze での使用方法の詳細については、[フィーチャーフラグについて]({{site.baseurl}}/developer_guide/feature_flags/)を参照してください。

## 前提条件

### SDK バージョン

フィーチャーフラグを使用するには、少なくとも以下の最小バージョン以上の最新の SDK を使用するようにしてください。

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

### Braze の権限

ダッシュボードでフィーチャーフラグを管理するには、管理者であるか、次の[権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)を持っている必要があります。

| 権限                                                                    | できること                           |
|-------------------------------------------------------------------------------|-------------------------------------------|
| **フィーチャーフラグを管理する**                                                      | フィーチャーフラグを表示、作成、編集します。     |
| **キャンペーン、キャンバス、カード、フィーチャーフラグ、セグメント、メディアライブラリーにアクセスする** | 利用可能なフィーチャーフラグのリストを表示します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## フィーチャーフラグを作成する

### ステップ 1: 新しいフィーチャーフラグを作成する

[**メッセージング**] > [**フィーチャーフラグ**] に進み、[**フィーチャーフラグを作成**] を選択します。

![既存のフィーチャーフラグと新規作成方法を示すデータテーブル。]({% image_buster /assets/img/feature_flags/create_ff.png %}){: style="max-width:75%"}

### ステップ 2: 詳細を記入する

**フィーチャーフラグの詳細**欄に、フィーチャーフラグの名前、ID、説明を入力します。

![フィーチャーフラグに名前、ID、説明、プロパティを追加できることを示すフォーム。]({% image_buster /assets/img/feature_flags/create_ff_properties.png %}){: style="max-width:75%"}


| フィールド        | 説明                                                                |
|--------------|----------------------------------------------------------------------------|
| 名前         | マーケターや管理者が読みやすいタイトルです。              |
| ID           | この機能が[ユーザーに対して有効か](#enabled)どうかをチェックするために、コード内で使用する一意の ID です。この ID は後で変更できないため、続ける前に [ID 命名のベストプラクティス](#naming-conventions)を確認してください。 |
| 説明  | フィーチャーフラグに関するコンテキストを提供するオプションの説明です。   |
| プロパティ   | フィーチャーフラグをリモートで設定するオプションのプロパティです。キャンバスステップやフィーチャーフラグ実験で上書きできます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### ステップ 2a: カスタムプロパティを作成する

**プロパティ**では、機能が有効な場合にアプリが Braze SDK を通じてアクセスできるカスタムプロパティをオプションで作成できます。各変数には文字列、ブール値、画像、タイムスタンプ、JSON、数値を割り当てることができ、デフォルト値を設定することもできます。

{% tabs local %}
{% tab example %}
次の例では、フィーチャーフラグが指定されたカスタムプロパティを使用して、e コマースストアに在庫切れバナーを表示します。 

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
追加できるプロパティ数に制限はありません。ただし、フィーチャーフラグのプロパティは合計 10 KB に制限されています。プロパティ値とキーの長さはともに 255 文字に制限されています。
{% endalert %}
{% endtab %}
{% endtabs %}

### ステップ 4: ターゲットとするセグメントを選ぶ

フィーチャーフラグをロールアウトする前に、ターゲットとするユーザーの[セグメント]({{site.baseurl}}/user_guide/engagement_tools/segments/)を選択する必要があります。新しく作成したフラグで [**ルールを追加**] を選択し、フィルターグループとセグメントのドロップダウンメニューを使って、ターゲットオーディエンスからユーザーを絞り込みます。複数のフィルターを追加して、オーディエンスをさらに絞り込みます。

![セグメントとフィルターを追加できる「ロールアウトトラフィック」というラベルのテキストボックス。]({% image_buster /assets/img/feature_flags/segmentation_ff.png %}){: style="max-width:75%;"}

### ステップ 5: ロールアウトトラフィックを設定する {#rollout}

デフォルトでは、フィーチャーフラグは常に無効になっています。これにより、機能リリースの日付と全ユーザーへの有効化を分離できます。ロールアウトを開始するには、**ロールアウトトラフィック**セクションのテキストボックスにパーセンテージを入力します。これにより、選択したセグメント内のランダムなユーザーの割合が決定され、この新機能がそのユーザーに提供されます。

{% alert important %}
新機能の本番準備が整うまでは、ロールアウトトラフィックを 0% 以上に設定しないでください。ダッシュボードで最初にフィーチャーフラグを定義する際、この設定は 0% のままにしてください。
{% endalert %}

{% alert important %}
単一のルールまたは単一のオーディエンスにフラグをロールアウトする場合は、セグメンテーション基準とロールアウト割合を選択した最初のルールを追加します。最後に、**その他のユーザー**ルールがオフになっていることを確認し、フラグを保存します。 
{% endalert %}

## 複数ルールによるフィーチャーフラグのロールアウト

複数ルールによるフィーチャーフラグのロールアウトを使用して、ユーザー評価のルールシーケンスを定義します。これにより、精密なセグメンテーションとコントロールされた機能リリースが可能になります。この方法は、同じ機能を多様なオーディエンスに展開するのに最適です。 

### 評価順序

フィーチャーフラグのルールは、リストされている順序で上から下へ評価されます。ユーザーは最初に満たしたルールに該当します。ユーザーがどのルールにも該当しない場合、その適格性はデフォルトの「その他のユーザー」ルールによって決定されます。

### ユーザーの適格性

- ユーザーが最初のルールの条件を満たした場合、そのユーザーは直ちにフィーチャーフラグを受け取る資格を得ます。
- ユーザーが最初のルールに該当しない場合、2 番目のルールで評価され、以下同様に続きます。

順次評価は、ユーザーがルールの条件を満たすか、リストの一番下にある「その他のユーザー」ルールに到達するまで続きます。

### 「その他のユーザー」ルール

「その他のユーザー」ルールはデフォルトとして機能します。ユーザーが先行するいずれのルールにも該当しない場合、そのフィーチャーフラグの適用可否は「その他のユーザー」ルールのトグル設定によって決定されます。例えば、「その他のユーザー」ルールが「オフ」に設定されている場合、デフォルト状態では、他のどのルールの条件にも該当しないユーザーは、セッション開始時にフィーチャーフラグを受け取りません。

### ルールの並べ替え

デフォルトでは、ルールは作成された順序で並べられますが、ダッシュボード上でルールをドラッグ＆ドロップすることで順序を変更できます。

![ユーザーがフィーチャーフラグにルールを追加できることを示す画像。]({% image_buster /assets/img/feature_flags/add_rule.png %}){: style="max-width:80%;"}

![複数のルールが追加され、さらに「その他のユーザー」ルールが設定されたフィーチャーフラグの概要を示す画像。]({% image_buster /assets/img/feature_flags/mr_rules_overview.png %}){: style="max-width:80%;"}

### 複数ルールによるフィーチャーフラグのユースケース

#### チェックアウトページを段階的にリリースする

例えば、e コマースブランドで働いていて、新しいチェックアウトページを安定性を確保しながら異なる地域に展開したい場合を考えてみましょう。複数ルールのフィーチャーフラグを使用すると、以下の設定が可能です。

- **ルール 1:** 米国セグメントを 100% に設定します。
- **ルール 2:** ブラジルユーザーの 50% に設定し、全員が同時にフローを受け取らないようにします。 
- **ルール 3（その他のユーザー）:** その他の全ユーザーに対しては、「その他のユーザー」ルールを有効にし、15% に設定します。これにより、全ユーザーの一部が新しいフローでチェックアウトできるようになります。

#### まず内部テスターに届ける

例えば、プロダクトマネージャーとして、新製品をリリースする際に内部テスターが常にフィーチャーフラグを受け取れるようにしたい場合を考えてみましょう。内部テスターのセグメントを最初のルールに追加し、100% に設定すれば、内部テスターはすべての機能ロールアウト時に対象となります。

## フィーチャーフラグの「enabled」フィールドの使用 {#enabled}

フィーチャーフラグを定義したら、アプリやサイトを設定して、特定のユーザーに対してそのフィーチャーフラグが有効かどうかを確認するようにします。有効になったら、ユースケースに応じて何らかのアクションを設定するか、フィーチャーフラグの変数プロパティを参照します。Braze SDK は、フィーチャーフラグのステータスとそのプロパティをアプリに取り込むためのゲッターメソッドを提供します。 

フィーチャーフラグはセッション開始時に自動的に更新されるため、起動時に機能の最新バージョンを表示できます。SDK はこれらの値をキャッシュし、オフラインの状態でも使用できるようにします。 

{% alert note %}
[フィーチャーフラグのインプレッション](#impressions)を必ず記録してください。 
{% endalert %}

たとえば、アプリに新しいタイプのユーザープロファイルをロールアウトするとします。`ID` を `expanded_user_profile` に設定します。次に、この新しいユーザープロファイルを特定のユーザーに表示するかどうかをアプリで確認します。以下に例を示します。

{% tabs %}
{% tab Web %}

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
{% tab Android %}
{% subtabs local %}
{% subtab Java %}
```java
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.getEnabled()) {
  Log.i(TAG, "expanded_user_profile is enabled");
} else {
  Log.i(TAG, "expanded_user_profile is not enabled");
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag?.enabled == true) {
  Log.i(TAG, "expanded_user_profile is enabled.")
} else {
  Log.i(TAG, "expanded_user_profile is not enabled.")
}
```

{% endsubtab %}
{% endsubtabs %}
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

ユーザーが新しい機能を操作する機会があった場合、または機能が無効になっている場合（A/B テストのコントロールグループの場合）にユーザーが操作した__可能性がある__場合は、フィーチャーフラグのインプレッションを追跡します。フィーチャーフラグのインプレッションは、1 セッションにつき 1 回のみ記録されます。 

通常、このコード行は、アプリ内でフィーチャーフラグを参照する場所の直下に置くことができます。

{% tabs %}
{% tab Web %}

```javascript
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.logFeatureFlagImpression(id: "expanded_user_profile")
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
braze.logFeatureFlagImpression("expanded_user_profile")
```

{% endsubtab %}
{% endsubtabs %}
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

指定したキーに対応する型のプロパティが存在しない場合、これらのメソッドは `null` を返します。

{% tabs %}
{% tab Web %}

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

// Returns the string property
let stringProperty: String? = featureFlag.stringProperty(key: "color")

// Returns the boolean property
let booleanProperty: Bool? = featureFlag.boolProperty(key: "expanded")

// Returns the number property as a double
let numberProperty: Double? = featureFlag.numberProperty(key: "height")

// Returns the Unix UTC millisecond timestamp property as an integer
let timestampProperty: Int? = featureFlag.timestampProperty(key: "account_start")

// Returns the image property as a String of the image URL
let imageProperty: String? = featureFlag.imageProperty(key: "homepage_icon")

// Returns the JSON object property as a [String: Any] dictionary
let jsonObjectProperty: [String: Any]? = featureFlag.jsonObjectProperty(key: "footer_settings")
```

{% endtab %}
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

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

{% endsubtab %}
{% subtab Kotlin %}

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

{% endsubtab %}
{% endsubtabs %}
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
{% tab Web %}

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
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
List<FeatureFlag> features = braze.getAllFeatureFlags();
for (FeatureFlag feature: features) {
  Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
val featureFlags = braze.getAllFeatureFlags()
featureFlags.forEach { feature ->
  Log.i(TAG, "Feature: ${feature.id} ${feature.enabled}")
}
```

{% endsubtab %}
{% endsubtabs %}
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

セッションの途中で現在のユーザーのフィーチャーフラグを更新して、Braze から最新の値を取得できます。

{% alert tip %}
更新はセッション開始時に自動的に行われます。更新が必要なのは、チェックアウトページの読み込み前や、フィーチャーフラグが参照されることがわかっている場合など、重要なユーザーアクションの前だけです。
{% endalert %}

{% tabs %}
{% tab Web %}

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
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
braze.refreshFeatureFlags();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
braze.refreshFeatureFlags()
```

{% endsubtab %}
{% endsubtabs %}
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

これは、ユーザーがある機能を利用できなくなった場合にアプリを更新したい場合に便利です。たとえば、ある機能が有効かどうか、またはそのプロパティ値の 1 つに基づいて、アプリの状態を設定する場合です。

{% tabs %}
{% tab Web %}

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
{% tab Android %}
{% subtabs local %}
{% subtab Java %}

```java
braze.subscribeToFeatureFlagsUpdates(event -> {
  Log.i(TAG, "Feature flags were updated.");
  for (FeatureFlag feature: event.getFeatureFlags()) {
    Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
braze.subscribeToFeatureFlagsUpdates() { event ->
  Log.i(TAG, "Feature flags were updated.")
  event.featureFlags.forEach { feature ->
    Log.i(TAG, "Feature: ${feature.id}")
  }
}
```

{% endsubtab %}
{% endsubtabs %}
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

変更をリッスンするには、[**Braze 構成**] > [**フィーチャーフラグ**] の [**Game Object Name**] と [**Callback Method Name**] の値を、アプリケーションの対応する値に設定します。

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

アプリの Dart コードでは、以下のサンプルコードを使用します。

```dart
// Create stream subscription
StreamSubscription featureFlagsStreamSubscription;

featureFlagsStreamSubscription = braze.subscribeToFeatureFlags((featureFlags) {
  print("Feature flags were updated");
});

// Cancel stream subscription
featureFlagsStreamSubscription.cancel();
```

{% subtabs %}
{% subtab Flutter SDK 18.0.0+ %}

フィーチャーフラグのデータは、Android と iOS の両方のネイティブレイヤーから自動的に転送されます。追加のセットアップは不要です。

{% endsubtab %}
{% subtab Flutter SDK 17.1.0 and earlier %}

Flutter SDK 17.1.0 以前を使用している場合、iOS ネイティブレイヤーからのフィーチャーフラグデータの転送には手動セットアップが必要です。アプリケーションには、`BrazePlugin.processFeatureFlags(featureFlags)` を呼び出す `featureFlags.subscribeToUpdates` コールバックが含まれている可能性があります。Flutter SDK 18.0.0 に移行するには、`BrazePlugin.processFeatureFlags(_:)` の呼び出しを削除してください。データ転送は自動的に処理されるようになりました。

例については、Braze Flutter SDK サンプルアプリケーションの [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) を参照してください。

{% endsubtab %}
{% endsubtabs %}

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

## ユーザーの適格性を確認する

Braze でユーザーがどのフィーチャーフラグを利用できるか確認するには、[**オーディエンス**] > [**ユーザー検索**] に移動し、ユーザーを検索して選択します。

[**フィーチャーフラグの適格性**] タブでは、プラットフォーム、アプリケーション、またはデバイスごとに適格なフィーチャーフラグのリストをフィルターできます。フィーチャーフラグの横にある <i class="fa-solid fa-eye"></i> を選択することで、ユーザーに返されるペイロードをプレビューすることもできます。

![ユーザーが利用可能なフィーチャーフラグの一覧表を示す画像。]({% image_buster /assets/img/feature_flags/eligibility.png %}){: style="max-width:85%;"}

## 変更ログを表示する

フィーチャーフラグの変更ログを表示するには、フィーチャーフラグを開き、[**変更ログ**] を選択します。

![フィーチャーフラグの「編集」ページで、「変更ログ」ボタンが強調表示されている。]({% image_buster /assets/img/feature_flags/changelog/open_changelog.png %}){: style="max-width:60%;"}

ここでは、いつ変更されたのか、誰が変更したのか、どのカテゴリーに属するのかなどを確認できます。

![選択したフィーチャーフラグの変更ログ。]({% image_buster /assets/img/feature_flags/changelog/changelog.png %}){: style="max-width:90%;"}

## フィーチャーフラグでセグメント化する {#segmentation}

Braze は、現在フィーチャーフラグが有効になっているユーザーを自動的に追跡します。[**フィーチャーフラグ**フィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#feature-flags)を使ってセグメントまたはターゲットメッセージングを作成できます。セグメントでのフィルタリングの詳細については、[セグメントの作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)を参照してください。

![「フィルター」セクションで、フィルター検索バーに「フィーチャーフラグ」と入力した状態。]({% image_buster /assets/img/feature_flags/feature-flags-filter-name.png %}){: style="max-width:75%;"}

{% alert note %}
再帰的なセグメントを防ぐため、他のフィーチャーフラグを参照するセグメントを作成することはできません。
{% endalert %}

## ベストプラクティス

### ロールアウトをキャンバスや実験と組み合わせない

異なるエントリーポイントによってユーザーが有効になったり無効になったりするのを避けるには、ロールアウトスライダーをゼロより大きな値に設定するか、キャンバスまたは実験でフィーチャーフラグを有効にするかのいずれかにしてください。ベストプラクティスとして、キャンバスや実験でフィーチャーフラグを使用する予定がある場合は、ロールアウトのパーセンテージをゼロにしておいてください。

### 命名規則

コードを明確で一貫性のあるものにするために、フィーチャーフラグ ID に名前を付けるときは、以下のフォーマットを使用することを検討してください。

```plaintext
BEHAVIOR_PRODUCT_FEATURE
```

次のように置き換えます。

| プレースホルダー | 説明                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| `BEHAVIOR`  | 機能の動作です。コードでは、その動作がデフォルトで無効になっていることを確認し、フィーチャーフラグ名に `disabled` のような表現を使わないようにしてください。 |
| `PRODUCT`   | その機能が属する製品です。                                                                                       |
| `FEATURE`    | 機能の名前です。                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

`show` が動作、`animation_profile` が製品、`driver` が機能であるフィーチャーフラグの例を次に示します。

```plaintext
show_animation_profile_driver
```

### 事前に計画する

常に安全策を取りましょう。オフスイッチが必要になる可能性のある新機能を検討する場合、新しいアプリのアップデートが必要だと後から気づくよりも、フィーチャーフラグ付きの新しいコードをリリースして結果的に不要だった方がはるかに良いです。

### 説明を記述する

フィーチャーフラグに説明を追加しましょう。これは Braze のオプションフィールドですが、利用可能なフィーチャーフラグを参照する際に他の人が持つかもしれない疑問に答えるのに役立ちます。

- このフラグのイネーブルメントと動作の責任者の連絡先
- このフラグを無効にすべきタイミング
- このフラグが制御する新機能に関するドキュメントやメモへのリンク
- 依存関係や機能の使用方法に関する注意事項

### 古いフィーチャーフラグを整理する

必要以上に長い間、100% のロールアウトで機能を放置してしまうことは誰にでもあります。

コード（および Braze ダッシュボード）をクリーンに保つために、すべてのユーザーがアップグレードを完了し、機能を無効にするオプションが不要になったら、コードベースから永久フィーチャーフラグを削除してください。これにより、開発環境の複雑さが軽減されるだけでなく、フィーチャーフラグのリストも整理整頓されます。