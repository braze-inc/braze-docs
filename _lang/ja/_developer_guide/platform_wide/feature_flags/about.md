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

> フィーチャーフラグを使用すると、特定のユーザーまたは選択したユーザーの機能をリモートで有効または無効にすることができます。重要なことは、追加のコード展開やアプリストア更新を使用せずに、機能のオンオフを本番環境で切り替えることができることです。これにより、新しい機能を安全かつ確信を持ってロールアウトできます。 

Brazeでフィーチャーフラグを作成する方法に関するステップを探していますか?\[フィーチャーフラグの作成][3] を参照してください。

## 前提条件

フィーチャーフラグを使用するには、少なくとも以下の最小バージョン以上の最新の SDK を使用するようにしてください。

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## フィーチャーフラグ sの使用

フィーチャーフラグ s を使用して:

- [段階的なロールアウトを導入する](#gradual-rollouts)
- [アプリ変数をリモートでコントロールする](#remotely-control-app-variables)
- [機能のロールアウトとメッセージングを同期する](#message-coordination)
- [新機能を試す](#feature-experimentation)
- [ユーザーをフィーチャーフラグでセグメント化する](#segmentation)

### 段階的なロールアウト

フィーチャーフラグを使用して、サンプルの母集団に対して徐々に機能を有効にします。たとえば、最初に VIP ユーザーに新しい機能をソフトローンチできます。この戦略は、新しい機能を一度に全ユーザーに配布することに伴う危険性を軽減するのに役立ち、バグの早期発見に役立ちます。

![ロールアウトのトラフィックスライダーが0% から100% に変化する様子を示すアニメーション。][1]

たとえば、顧客サービスを迅速に行うために、新しい「ライブチャットサポート」リンクをアプリに追加することにしたとします。この機能をすべての顧客に一度にリリースすることもできます。しかし、幅広くリリースすることには、次のようなリスクがあります。 

* 当社のサポートチームはまだトレーニング段階にあり、顧客はリリース後にサポートチケットを開始できます。これでは、サポートチームがより多くの時間を必要とする場合に、余裕がなくなります。
* 新しいサポートケースの実際のボリュームがわからないので、適切なスタッフが配置されない可能性があります。
* サポートチームが圧倒された場合、この機能を再度すばやく無効にする戦略はありません。
* チャットウィジェットにバグが発生する可能性があり、顧客にネガティブな体験をさせたくありません。

Braze フィーチャーフラグを使用することで、機能を段階的にロールアウトし、これらのリスクをすべて軽減できます。

* "Live Chat Support"機能は、サポートチームが準備ができたと言ったときにオンにします。
* 人員が適切に配置されているかどうかを判断するために、この新機能を10%のユーザーに対してのみ有効にします。
* バグがある場合は、新しいリリースを急いで配布するのではなく、ただちに機能を無効にすることができます。

この機能を段階的にロールアウトするには、「ライブチャットウィジェット」という名前のフィーチャーフラグを[作成します]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/)。

![Live Chat Widget という名前の例の機能フラグの詳細。ID はenable_live_chat です。このフィーチャーフラグの説明には、ライブチャットウィジェットがサポートページに表示されることが記載されています。][7]

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

### アプリ変数をリモートでコントロールする

フィーチャーフラグを使用して、本番環境でアプリの機能を変更します。これは特にモバイルアプリにおいて重要となる可能性があります。アプリストアの承認プロセスにより、すべてのユーザーに変更を迅速にロールアウトすることが難しいためです。

例えば、弊社のマーケティングチームが、弊社の現行の販売・プロモーションを弊社アプリのナビゲーションに掲載したいとします。通常、当社のエンジニアは変更に1週間、アプリストアのレビューに3日間のリードタイムを必要とします。しかし、感謝祭、ブラックフライデー、サイバーマンデー、ハヌカー、クリスマス、元旦がすべて2ヶ月以内にあるので、これらのタイトな締め切りに間に合わせることはできないでしょう。

フィーチャーフラグを使用すると、Braze によってアプリのナビゲーションリンクのコンテンツを強化し、マーケティングマネージャーが数日ではなく数分で変更を加えることが可能になります。

この機能をリモートで構成するには、`navigation_promo_link` という新しいフィーチャーフラグを作成し、次の初期プロパティを定義します。

![汎用販売ページに向けたリンクとテキストプロパティを持つ機能フラグ。][9]

このアプリでは、Braze で getter メソッドを使用して、このフィーチャーフラグのプロパティを取得し、これらの値に基づいてナビゲーションリンクを構築します。

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

これで、感謝祭の前日には、Braze ダッシュボードでこれらのプロパティ値を変更するだけで済みます。

![Thanksgivingの販売ページに向けたリンクとテキストプロパティを持つ機能フラグ。][10]

その結果、次回誰かがアプリを読み込むと、新しい感謝祭セールが表示されます。

### メッセージの調整

フィーチャーフラグを使用して、機能のロールアウトとメッセージングを同期します。これにより、ユーザーエクスペリエンスと関連メッセージングの両方の信頼できる情報源として Braze を使用できるようになります。これを実現するには、新しい機能の対象をオーディエンスの特定のセグメントまたはフィルター処理された部分にします。次に、そのSegmentのみを対象とするキャンペーンまたはキャンバスを作成します。 

たとえば、ユーザー向けに新しいロイヤルティ報酬プログラムを開始するとします。マーケティングチームと製品チームが、プロモーションメッセージングのタイミングと機能のロールアウトのタイミングを完璧に調整するのは難しいかもしれません。キャンバスのフィーチャーフラグを使用すると、選択したオーディエンスに対して機能を有効にし、その同じユーザーに対して関連するメッセージングをコントロールする際に、高度なロジックを適用できます。

機能のロールアウトとメッセージングを効率的に調整するために、`show_loyalty_program` という新しいフィーチャーフラグを作成します。最初の段階的リリースでは、フィーチャーフラグを有効にするタイミングと対象をキャンバスでコントロールします。この時点では、ロールアウトのパーセンテージは0% のままにし、ターゲットセグメントは選択しません。

![ロイヤルティ報酬プログラムという名前のフィーチャーフラグ。ID は show_loyalty_program で、これはホーム画面とプロファイルページに新しいロイヤルティ報酬プログラムが表示されるということを説明しています。][11]

次に、キャンバスフローで、「高価値顧客」セグメントの `show_loyalty_program` フィーチャーフラグを有効にする[フィーチャーフラグステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/)を作成します。

![高価値顧客セグメントが show_loyalty_program フィーチャーフラグをオンにする、オーディエンス分割ステップを含むキャンバスの例。][4]

これで、このセグメントのユーザーに対して新しいロイヤルティプログラムが表示され始め、有効にした後、メールと調査が自動的に送信され、チームがフィードバックを収集できるようになります。

### 機能実験

フィーチャーフラグを使用して、新しいフィーチャーに関する仮説を実験で確認することができます。トラフィックを2 つ以上のグループに分割することで、グループ間でフィーチャーフラグの影響を比較し、その結果に基づいてアクションの最適なコースを決定できます。

[A/B test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) は、ユーザーのレスポンスを変数の複数バージョンと比較する強力なツールです。

この例では、チームは e コマースアプリの新しいチェックアウトフローを構築しました。ユーザーエクスペリエンスは改善されていると確信しているにもかかわらず、AB テストを実行して、アプリの収益に与える影響を測定したいと考えています。

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

\[フィーチャーフラグ実験][12] でAB テストを設定します。

さて、50%のユーザー sが旧来の体験を見て、残りの50%が新しい体験を見てくれるでしょう。次に、2つのバリアントを分析して、どちらのチェックアウトフローがより高いコンバージョン率をもたらすかを決定できます。

![交通を50%の2群に分けるフィーチャーフラグ実験。][6]

勝者が決定したら、このキャンペーンを停止し、すべてのユーザーに対してフィーチャーフラグのロールアウト率を100%に増やすことができます。一方、開発チームはこれを次のアプリリリースにハードコーディングします。

### セグメンテーション

フィーチャーフラグを使用しているかどうかに基づいて、**フィーチャーフラグ**フィルターを使用してSegmentまたは対象メッセージングをユーザーで作成します。たとえば、アプリのプレミアムコンテンツをコントロールするフィーチャーフラグがあるとします。フィーチャーフラグが有効になっていないユーザーをフィルター処理するセグメントを作成し、そのセグメントに対して、プレミアムコンテンツを表示するためにアカウントをアップグレードするように促すメッセージを送信できます。

![][14]

Segment s でのフィルター ing の詳細については、[Segmentの作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)を参照してください。

{% alert note %}
再帰的Segmentsを防ぐために、他のフィーチャーフラグを参照するSegmentを作成することはできません。
{% endalert %}

## 制限事項

次の表では、フィーチャーフラグレベルで適用される制限について説明します。有料版のフィーチャーフラグを購入するには、Braze アカウントマネージャーに問い合わせるか、Braze ダッシュボードでアップグレードをリクエストしてください。

| 制限エリア                                                                                                   | 無料版     | 有料版      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [アクティブなフィーチャーフラグ](#active-feature-flags)                                                                     | ワークスペースあたり10 | ワークスペースあたり110 |
| [アクティブなキャンペーンの実験]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/)          | ワークスペースごとに1つ  | ワークスペースあたり100 |
| [フィーチャーフラグキャンバスステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) | 無制限        | 無制限         |
{: .reset-td-br-1 .reset-td-br-2}

### アクティブなフィーチャーフラグ

次のいずれかに該当する場合、フィーチャーフラグはアクティブと見なされ、制限に対してカウントされます。

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
