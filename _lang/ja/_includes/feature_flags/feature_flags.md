# フィーチャーフラグ

> フィーチャーフラグを使用すると、特定のユーザーまたはランダムに選択したユーザーの機能をリモートで有効または無効にすることができます。重要なことは、追加のコードデプロイやアプリストアの更新なしに、本番環境で機能のオンオフを切り替えることができることです。これにより、新しい機能を安全かつ確信を持ってロールアウトできます。

{% alert tip %}
独自のフィーチャーフラグを作成する準備ができたら、[フィーチャーフラグの作成]({{site.baseurl}}/developer_guide/feature_flags/create/)をご確認ください。
{% endalert %}

## 前提条件

フィーチャーフラグの使用を開始するために必要な SDK の最小バージョンは次のとおりです。

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## ユースケース

### 段階的なロールアウト

フィーチャーフラグを使用して、サンプルの母集団に対して徐々に機能を有効にします。たとえば、最初に VIP ユーザーに新しい機能をソフトローンチできます。この戦略は、新しい機能を一度に全ユーザーに配布することに伴うリスクを軽減し、バグの早期発見に役立ちます。

![ロールアウトのトラフィックスライダーが 0% から 100% に変化する様子を示すアニメーション。]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

たとえば、顧客サービスを迅速に行うために、新しい「ライブチャットサポート」リンクをアプリに追加することにしたとします。この機能をすべての顧客に一度にリリースすることもできます。しかし、幅広くリリースすることには、次のようなリスクがあります。 

* サポートチームはまだトレーニング段階にあり、顧客はリリース後にサポートチケットを作成できるようになります。これでは、サポートチームがより多くの時間を必要とする場合に余裕がなくなります。
* 新しいサポートケースの実際のボリュームがわからないため、適切なスタッフが配置されない可能性があります。
* サポートチームが圧倒された場合、この機能を再度すばやく無効にする戦略がありません。
* チャットウィジェットにバグが発生する可能性があり、顧客にネガティブな体験をさせたくありません。

Braze フィーチャーフラグを使用することで、機能を段階的にロールアウトし、これらのリスクをすべて軽減できます。

* 「ライブチャットサポート」機能は、サポートチームが準備ができたと言ったときにオンにします。
* 人員が適切に配置されているかどうかを判断するために、この新機能を 10% のユーザーに対してのみ有効にします。
* バグがある場合は、新しいリリースを急いで配布するのではなく、ただちに機能を無効にすることができます。

この機能を段階的に展開するには、「ライブチャットウィジェット」という名前の[フィーチャーフラグを作成]({{site.baseurl}}/developer_guide/feature_flags/create/)します。

![Live Chat Widget という名前の例のフィーチャーフラグの詳細。ID は enable_live_chat です。このフィーチャーフラグの説明は、サポートページにライブチャットウィジェットが表示されることを示しています。]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

アプリコードでは、Braze フィーチャーフラグが有効になっている場合にのみ **Start Live Chat** ボタンを表示します。

{% tabs %}
{% tab JavaScript %}

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)
```

{% endtab %}
{% tab Java %}

```java
// Get the initial value from the Braze SDK
FeatureFlag featureFlag = braze.getFeatureFlag("enable_live_chat");
Boolean liveChatEnabled = featureFlag != null && featureFlag.getEnabled();

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(event -> {
  FeatureFlag newFeatureFlag = braze.getFeatureFlag("enable_live_chat");
  Boolean newValue = newFeatureFlag != null && newFeatureFlag.getEnabled();
  liveChatEnabled = newValue;
});

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Get the initial value from the Braze SDK
val featureFlag = braze.getFeatureFlag("enable_live_chat")
var liveChatEnabled = featureFlag?.enabled

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates() { event ->
  val newValue = braze.getFeatureFlag("enable_live_chat")?.enabled
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}

```

{% endtab %}
{% tab Swift %}

```swift
// Get the initial value from the Braze SDK
let featureFlag = braze.featureFlags.featureFlag(id: "enable_live_chat")
var liveChatEnabled = featureFlag?.enabled ?? false

// Listen for updates from the Braze SDK
braze.featureFlags.subscribeToUpdates() { _ in  
  let newValue = braze.featureFlags.featureFlag(id: "enable_live_chat")?.enabled ?? false
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
liveChatView.isHidden = !liveChatEnabled
```

{% endtab %}
{% endtabs %}

### アプリ変数をリモートでコントロールする

フィーチャーフラグを使用して、本番環境でアプリの機能を変更できます。これは特にモバイルアプリにおいて重要です。アプリストアの承認プロセスにより、すべてのユーザーに変更を迅速にロールアウトすることが難しいためです。

たとえば、マーケティングチームが現行のセールやプロモーションをアプリのナビゲーションに掲載したいとします。通常、エンジニアは変更に 1 週間、アプリストアのレビューに 3 日間のリードタイムを必要とします。しかし、感謝祭、ブラックフライデー、サイバーマンデー、ハヌカー、クリスマス、元旦がすべて 2 か月以内にあるため、これらのタイトな締め切りに間に合わせることはできません。

フィーチャーフラグを使用すると、Braze によってアプリのナビゲーションリンクのコンテンツを制御し、マーケティングマネージャーが数日ではなく数分で変更を加えることが可能になります。

この機能をリモートで構成するには、`navigation_promo_link` という新しいフィーチャーフラグを作成し、次の初期プロパティを定義します。

![汎用販売ページに向けたリンクとテキストプロパティを持つフィーチャーフラグ。]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

アプリでは、Braze の getter メソッドを使用して、このフィーチャーフラグのプロパティを取得し、これらの値に基づいてナビゲーションリンクを構築します。

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

{% endtab %}
{% tab Java %}

```java
// liveChatView is the View container for the Live Chat UI
FeatureFlag featureFlag = braze.getFeatureFlag("navigation_promo_link");
if (featureFlag != null && featureFlag.getEnabled()) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
liveChatView.setPromoLink(featureFlag.getStringProperty("link"));
liveChatView.setPromoText(featureFlag.getStringProperty("text"));

```

{% endtab %}
{% tab Kotlin %}

```kotlin
// liveChatView is the View container for the Live Chat UI
val featureFlag = braze.getFeatureFlag("navigation_promo_link")
if (featureFlag?.enabled == true) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}
liveChatView.promoLink = featureFlag?.getStringProperty("link")
liveChatView.promoText = featureFlag?.getStringProperty("text")
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "navigation_promo_link")
if let featureFlag {
  liveChatView.isHidden = !featureFlag.enabled
} else {
  liveChatView.isHidden = true
}
liveChatView.promoLink = featureFlag?.stringProperty("link")
liveChatView.promoText = featureFlag?.stringProperty("text")
```

{% endtab %}
{% endtabs %}

これで、感謝祭の前日には、Braze ダッシュボードでこれらのプロパティ値を変更するだけで済みます。

![感謝祭の販売ページに向けたリンクとテキストプロパティを持つフィーチャーフラグ。]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

その結果、次回誰かがアプリを読み込むと、新しい感謝祭セールが表示されます。

### メッセージの調整

フィーチャーフラグを使用して、機能のロールアウトとメッセージングを同期し、プロダクトチームとマーケティングチームの連携を強化します。フィーチャーフラグを通じて機能リリースとメッセージングを調整することで、両チームが戦略を一致させ、一貫したユーザーエクスペリエンスを作成できます。

たとえば、ユーザー向けに新しいロイヤルティ報酬プログラムを開始するとします。マーケティングチームとプロダクトチームにとって、プロモーションのメッセージングと機能のロールアウトのタイミングを完璧に調整するのは難しいことです。しかし、Canvas のフィーチャーフラグを使用すると、プロダクトチームは特定のオーディエンスに対して機能を有効にする高度なロジックを適用でき、マーケティングチームは同じユーザーに対して関連するメッセージングをコントロールできます。

機能のロールアウトとメッセージングを効率的に調整するために、`show_loyalty_program` という新しいフィーチャーフラグを作成します。最初の段階的リリースでは、フィーチャーフラグを有効にするタイミングと対象を Canvas でコントロールします。この時点では、ロールアウトのパーセンテージは 0% のままにし、ターゲットセグメントは選択しません。

![ロイヤルティ報酬プログラムという名前のフィーチャーフラグ。ID は show_loyalty_program であり、ホーム画面とプロファイルページに新しいロイヤルティ報酬プログラムが表示されることを示す説明です。]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

次に、Canvas で「高価値顧客」セグメント向けの `show_loyalty_program` フィーチャーフラグを有効にする[フィーチャーフラグステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/)を作成します。

![オーディエンス分割ステップを含む Canvas の例で、高価値顧客セグメントが show_loyalty_program フィーチャーフラグを有効にする場合。]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

これで、このセグメントのユーザーに対して新しいロイヤルティプログラムが表示され始め、有効にした後、メールと調査が自動的に送信され、チームがフィードバックを収集できるようになります。

### 機能実験

フィーチャーフラグを使用して、新しい機能に関する仮説を実験で確認できます。トラフィックを 2 つ以上のグループに分割することで、グループ間でフィーチャーフラグの影響を比較し、その結果に基づいて最適なアクションを決定できます。

[A/B テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)は、ユーザーの応答を変数の複数バージョンと比較する強力なツールです。

この例では、チームは e コマースアプリの新しいチェックアウトフローを構築しました。ユーザーエクスペリエンスが改善されていると確信しているにもかかわらず、A/B テストを実行して、アプリの収益に与える影響を測定したいと考えています。

まず、`enable_checkout_v2` という新しいフィーチャーフラグを作成します。オーディエンスやロールアウトのパーセンテージは追加しません。代わりに、フィーチャーフラグ実験を使用して、トラフィックを分割し、機能を有効にして、結果を測定します。

アプリでは、フィーチャーフラグが有効かどうかを確認し、応答に基づいてチェックアウトフローを切り替えます。

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />  
} else {
  return <OldCheckoutFlow />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewCheckoutFlow();
} else {
  return new OldCheckoutFlow();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("enable_checkout_v2")
braze.logFeatureFlagImpression("enable_checkout_v2")
if (featureFlag?.enabled == true) {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "enable_checkout_v2")
braze.featureFlags.logFeatureFlagImpression(id: "enable_checkout_v2")
if let featureFlag, featureFlag.enabled {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% endtabs %}

A/B テストは、[フィーチャーフラグ実験]({{site.baseurl}}/developer_guide/feature_flags/experiments/)で設定します。

これで、50% のユーザーが従来の体験を見て、残りの 50% が新しい体験を見ることになります。その後、2 つのバリアントを分析し、どちらのチェックアウトフローがより高いコンバージョン率をもたらしたかを判断できます。{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

![トラフィックを 50% ずつの 2 つのグループに分割するフィーチャーフラグ実験。]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

勝者が決定したら、このキャンペーンを停止し、すべてのユーザーに対してフィーチャーフラグのロールアウト率を 100% に増やすことができます。一方、エンジニアリングチームはこれを次のアプリリリースにハードコーディングします。

### セグメンテーション

**フィーチャーフラグ**フィルターを使用して、フィーチャーフラグが有効になっているかどうかに基づいて、セグメントを作成したりユーザーにターゲットメッセージを送信したりできます。たとえば、アプリのプレミアムコンテンツをコントロールするフィーチャーフラグがあるとします。フィーチャーフラグが有効になっていないユーザーをフィルター処理するセグメントを作成し、そのセグメントに対して、プレミアムコンテンツを表示するためにアカウントをアップグレードするように促すメッセージを送信できます。

![]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

セグメントでのフィルタリングの詳細については、[セグメントの作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)を参照してください。

{% alert note %}
再帰的なセグメントを防ぐため、他のフィーチャーフラグを参照するセグメントを作成することはできません。
{% endalert %}

## プランの制限

これらは、無料プランと有料プランのフィーチャーフラグの制限事項です。

| 機能                                                                                                   | 無料バージョン     | 有料バージョン      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [アクティブなフィーチャーフラグ](#active-feature-flags)                                                                     | ワークスペースあたり 10 | ワークスペースあたり 110 |
| [アクティブなキャンペーン実験]({{site.baseurl}}/developer_guide/feature_flags/experiments/)          | ワークスペースあたり 1  | ワークスペースあたり 100 |
| [フィーチャーフラグ Canvas ステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) | 無制限        | 無制限         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

次のいずれかに該当する場合、フィーチャーフラグはアクティブと見なされ、制限に対してカウントされます。

- ロールアウトが 0% を超えている
- アクティブな Canvas で使用されている
- アクティブな実験で使用されている

同じフィーチャーフラグが Canvas で使用されていてロールアウトが 50% である場合など、複数の条件に一致する場合でも、制限に対してアクティブなフィーチャーフラグは 1 つとしてのみカウントされます。

{% alert note %}
有料バージョンのフィーチャーフラグを購入するには、Braze アカウントマネージャーにお問い合わせいただくか、Braze ダッシュボードでアップグレードをリクエストしてください。
{% endalert %}