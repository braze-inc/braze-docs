---
nav_title: 機能フラグについて
article_title: 機能フラグについて
page_order: 1
description: "このリファレンス記事では、前提条件とユースケースを含むフィーチャーフラグの概要について説明します。"
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
  - Unity
  - Cordova
  - React Native
  - Flutter
  - Roku

---

# フィーチャーフラグについて

> 機能フラグを使用すると、特定のユーザーまたは任意の選択に対して、機能をリモートで有効または無効にできます。重要なことは、追加のコード展開やアプリストア更新を使用せずに、機能のオンオフを本番環境で切り替えることができることです。これにより、自信を持って新しい機能を安全に展開することができます。 

Brazeでフィーチャーフラグを作成する方法に関するステップを探していますか?\[フィーチャーフラグs][3]の作成]を参照してください。

## 前提条件

フィーチャーフラグ s を使用するには、SDKs が以下の最低限のバージョンで最新であることを確認します。

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## フィーチャーフラグ sの使用

フィーチャーフラグ s を使用して:

- [段階的に展開する](#gradual-rollouts)
- [遠隔コントロール アプリ](#remotely-control-app-variables)
- [機能のロールアウトとメッセージングの同期](#message-coordination)
- [新機能を試す](#feature-experimentation)
- [ユーザーsをフィーチャーフラグsで分割](#segmentation)

### 段階的な展開

フィーチャーフラグs を使用すると、サンプリングポピュレーションの機能が徐々に有効になります。たとえば、最初にVIP ユーザーに新しい機能をソフト起動できます。この戦略は、新しい機能を一度に全員に配送することに伴う危険性を軽減するのに役立ち、バグの早期発見に役立ちます。

![ロールアウトトラフィックスライダの移動"画像は0% から100% になります。][1]

たとえば、新しい"Live Chat Support"をアプリに追加して顧客を高速化することを決めました。この機能は、すべての顧客s に一度に公開することができます。しかし、広範なリリースには、次のようなリスクがあります。 

* 弊社のサポートチームはまだトレーニング ingにあり、顧客 sはリリース後にサポートチケットを始めることができます。これは、サポートチームがより多くの時間を必要とする場合、私たちに余裕をもたらしません。
* 新しいサポートケースの実際の数量がわからないため、アプリ適切な人員が確保されていない可能性があります。
* サポートチームが圧倒された場合、この機能を再度すばやく無効にする戦略はありません。
* チャットウィジェットにバグが導入されている可能性があり、顧客 s にネガティブな体験をさせたくない場合があります。

Braze フィーチャーフラグ s を使用すると、機能を徐々に展開し、これらのすべての危険を軽減できます。

* "Live Chat Support"機能は、サポートチームが準備ができたと言ったときにオンにします。
* この新機能は、ユーザーのわずか10%で有効にし、アプリに適切な人員がいるかどうかを判断します。
* バグがある場合は、新しいリリースを急いで出荷する代わりに、この機能をすばやく無効にすることができます。

この機能を徐々にロールアウトするには、[create]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/) a フィーチャーフラグ named "Live Chat Widget."

![Live Chat Widget という名前の例の機能フラグの詳細。ID はenable_live_chat です。このフィーチャーフラグの説明は、ライブチャットウィジェットがサポートページに表示されることを示しています。][7]

このアプリ コードでは、Braze フィーチャーフラグが有効になっている場合、**Live Chat**ボタンのみを表示します。

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

### 遠隔コントロール アプリ

フィーチャーフラグを使用して、本番環境でアプリの機能を変更します。これは、アプリストアのアプリがすべてのユーザーs への変更の迅速な展開を妨げる携帯アプリで特に大切です。

例えば、弊社のマーケティングチームが、弊社の現行の販売・プロモーションを弊社アプリのナビゲーションに掲載したいとします。通常、当社の技術者は、変更には1週間のリードタイムを要し、アプリ店舗の見直しには3日間を要する。しかし、感謝祭、ブラック・フライデー、サイバー・マンデー、ハヌッカ、クリスマス、お正月の2ヶ月以内には、これらの厳しい締め切り日には間に合わないでしょう。

フィーチャーフラグ s を使用すると、Braze にアプリナビゲーションリンクの内容の消費電力を与えることができ、マーケティング マネージャーが日数ではなく分数で変更できるようになります。

この機能をリモートで設定するには、`navigation_promo_link` という新しいフィーチャーフラグを作成し、次の最初のプロパティーを定義します。

![汎用販売ページに向けたリンクとテキストプロパティを持つ機能フラグ。][9]

このアプリでは、Brazeでgetter メソッドを使用して、このフィーチャーフラグのプロパティを取得し、これらの値に基づいてナビゲーションリンクを構築します。

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

さて、感謝祭の前日、私たちはBraze ダッシュボードの中でプロパティの価値観を変えなければならないだけです。

![Thanksgivingの販売ページに向けたリンクとテキストプロパティを持つ機能フラグ。][10]

そのため、次回誰かがアプリを読み込むすると、新しい感謝祭の取引を見ることになる。

### メッセージ連携

フィーチャーフラグを使用して、機能のロールアウトとメッセージングを同期します。これにより、Brazeをユーザーエクスペリエンスとその関連メッセージングの両方の真理の源泉として使用できます。これを実現するには、新しい機能をオーディエンスの特定のSegmentまたはフィルターの対象部分に向けます。次に、そのSegmentのみを対象とするキャンペーンまたはキャンバスを作成します。 

ここでは、私たちのユーザーsのために新しいロイヤルティ 報酬番組を立ち上げているとしよう。マーケティングチームとプロダクトチームが、プロモーションメッセージングの時期をフィーチャーの展開と完全に調整することは難しいかもしれない。キャンバスの機能フラグを使用すると、選択したオーディエンスの機能を有効にし、関連するメッセージングを同じユーザーs にコントロールする場合に、高度なロジックをアプリできます。

機能のロールアウトとメッセージングを効率的に調整するために、`show_loyalty_program` という新しいフィーチャーフラグを作成します。最初のフェーズリリースでは、フィーチャーフラグが有効になっているときとそのユーザをコントロールします。ここでは、ロールアウトパーセンテージe を0% のままにして、対象Segments を選択しません。

![ロイヤルティ・リワード・プログラムという名前のフィーチャーフラグ。ID はshow_ロイヤルティ_program で、これがホーム画面とプロファイル画面に新しいロイヤルティ 報酬 s プログラムを表示していることを示します。][11]

次に、キャンバスフローで、&quot の`show_loyalty_program` フィーチャーフラグを有効にする[ フィーチャーフラグ ステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) を作成します。" 高値のCustomers" Segment:

![たとえば、オーディエンス分割ステップのキャンバスでは、高値の顧客がSegmentshow_ロイヤルティ_program フィーチャーフラグを有効にします。][4]

これで、このSegmentのユーザー s が新しいロイヤルティプログラムを表示し始め、有効になった後、メールと調査が自動的に送信され、チームがフィードバックを収集できるようになります。

### 機能実験

フィーチャーフラグ s を使用して、新しい機能を試し、仮説を確認します。トラフィックを2 つ以上のグループに分割することで、グループ間でフィーチャーフラグの影響を比較し、その結果に基づいてアクションの最適なコースを決定できます。

[A/B test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) は、ユーザーのレスポンスを変数の複数バージョンと比較する強力なツールです。

この事例では、私たちのe コマース アプリのために新しいチェックアウトフローを構築しました。ユーザー体験は改善されていると確信しているにもかかわらず、A/Bテストを実行して、アプリの収益に与える影響を測定したいと考えています。

まず、`enable_checkout_v2` という新しいフィーチャーフラグを作成します。オーディエンスやロールアウトのパーセンテージeは追加しません。代わりに、フィーチャーフラグ試験を使用して、トラフィックを分割し、機能を有効にして、結果を測定します。

このアプリでは、フィーチャーフラグが有効かどうかを確認し、レスポンスに基づいてチェックアウトフローをスワップアウトします。

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

\[Feature Flag Experiment][12]] でA/B テストを設定します。

さて、50%のユーザー sが旧来の体験を見て、残りの50%が新しい体験を見てくれるでしょう。次に、2つのバリアントsを解析して、どのチェックアウトフローがより高いコンバージョン率をもたらすかを決定することができる。

![交通を50%の2群に分けるフィーチャーフラグ実験。][6]

勝者が決まったら、このキャンペーンをやめて、フィーチャーフラグのロールアウトパーセンテージeをすべてのユーザーsで100%に増やすことができます。一方、開発チームのハードコードは、これを次回のアプリリリースに移します。

### セグメンテーション

フィーチャーフラグを使用しているかどうかに基づいて、**フィーチャーフラグ**フィルターを使用してSegmentまたは対象メッセージングをユーザーで作成します。たとえば、アプリでプレミアムコンテンツをコントロールするフィーチャーフラグがあるとします。Segmentを作成して、フィーチャーフラグが有効になっていないユーザーのためにsをフィルターし、そのSegmentにアカウントをアップグレードしてプレミアムコンテンツを表示するように促すメッセージを送信することができます。

![][14]

Segment s でのフィルター ing の詳細については、[Segmentの作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)を参照してください。

{% alert note %}
再帰的Segmentsを防ぐために、他のフィーチャーフラグを参照するSegmentを作成することはできません。
{% endalert %}

## 制限事項

次のテーブルは、フィーチャーフラグにアプリする制限について説明しています。有料版のフィーチャーフラグ s をお買い求めになるには、Braze アカウントマネージャーに問い合わせるか、Braze ダッシュボードのアップグレードをリクエストしてください。

| 制限エリア                                                                                                   | 無料版     | 有料版      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [活性フィーチャーフラグs](#active-feature-flags)                                                                     | 10/ワークスペース | ワークスペースあたり110 |
| [活性キャンペーン試験]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/)          | ワークスペースごとに1つ  | ワークスペースあたり100 |
| [機能フラグキャンバスステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) | 無制限        | 無制限         |
{: .reset-td-br-1 .reset-td-br-2}

### 活性フィーチャーフラグs

フィーチャーフラグは有効と見なされ、次のいずれかがアプリした場合に制限に加算されます。

- ロールアウトが0%を超えている
- アクティブなキャンバスで使用
- アクティブな実験で使用

同じフィーチャーフラグがキャンバスで使用されていて、ロールアウトが50% である場合など、複数の条件に一致する場合でも、制限に向かって有効なフィーチャーフラグは1 つだけカウントされます。

[1]: {% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %}
[2]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/use_cases/
[3]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/
[4]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step
[6]: {% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %}
[7]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %}
[8]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/
[9]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %}
[10]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %}
[11]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %}
[12]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/
[14]: {% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %}
