---
nav_title: フィーチャーフラグについて
article_title: フィーチャーフラグについて
page_order: 1
description: "このリファレンス記事では、前提条件とユースケースを含む機能フラグの概要について説明します。"
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

# 機能フラグについて

> 機能フラグを使用すると、特定のユーザまたはランダムなユーザ選択に対して、機能をリモートで有効または無効にできます。重要なことは、追加のコードデプロイやアプリストアの更新なしに、本番環境で機能のオン/オフを切り替えることができることです。これにより、自信を持って新しい機能を安全に展開することができます。 

 Braze でフィーチャーフラグを作成する方法についてのステップを探していますか?[機能フラグの作成][3]を参照してください。

## 前提条件

機能フラグを使用するには、SDK が少なくとも次の最小バージョンで最新であることを確認します。

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## 機能フラグの使用

機能フラグを使用して以下を実行します。

- [段階的に展開する](#gradual-rollouts)
- [アプリ変数のリモートコントロール](#remotely-control-app-variables)
- [機能のロールアウトとメッセージングの同期](#message-coordination)
- [新機能を試す](#feature-experimentation)

### 段階的な展開

機能フラグを使用すると、サンプリング母体の機能を徐々に有効にできます。たとえば、最初にVIP ユーザに新しい機能をソフト起動できます。この戦略は、新しい機能を一度に全員に配送することに伴うリスクを軽減するのに役立ち、バグの早期発見に役立ちます。

![ロールアウトトラフィックスライダの移動イメージが0% から100% へ][1]

たとえば、新しい"Live Chat Support"アプリへのリンクを追加して、より迅速なカスタマーサービスを行うことを決定したとします。この機能は、すべてのお客様に一度にリリースできます。しかし、広範なリリースには、次のようなリスクがあります。 

* 私たちのサポートチームはまだトレーニング中で、お客様はリリース後にサポートチケットを開始できます。これは、サポートチームがより多くの時間を必要とする場合、私たちに余裕をもたらしません。
* 新しいサポートケースの実際の数量がわからないため、適切なスタッフが配置されていない可能性があります。
* サポートチームが圧倒された場合、この機能を再びすばやくオフにする戦略はありません。
* チャットウィジェットにバグが導入されている可能性があり、顧客に否定的な経験をさせたくない。

 Braze 機能フラグを使用すると、機能を徐々に展開し、これらのすべてのリスクを軽減できます。

* "Live Chat Support"機能は、サポートチームが準備ができたと言ったときにオンにします。
* この新機能を有効にするユーザーはわずか10%で、適切なスタッフがいるかどうかを判断します。
* バグがある場合は、新しいリリースを急いで出荷する代わりに、この機能をすばやく無効にすることができます。

この機能を徐々に展開するには、[create]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/) a feature flag named "Live Chat Widget."

![Live Chat Widget という名前の例の機能フラグの詳細。ID はenable\_live\_chat です。この機能フラグの説明は、ライブチャットウィジェットがサポートページに表示されることを読み取ります。[7]

アプリコードでは、 Braze 機能フラグが有効になっている場合、**Start Live Chat** ボタンのみが表示されます。

\`\`\`javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Braze SDK から初期値を取得する
const featureFlag = braze.getFeatureFlag("enable\_live\_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Braze SDK からアップデートを聴く
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable\_live\_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Braze SDK が有効になっていると判断した場合のみ、Live Chat を表示します
return (<>
  お困りの場合<button>私たちのチームにメールを送る</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)

\`\`\`

### アプリ変数のリモートコントロール

機能フラグを使用して、本番環境でアプリの機能を変更します。これは、アプリストアの承認により、すべてのユーザーに変更をすばやくロールアウトできないモバイルアプリでは特に重要です。

たとえば、私たちのマーケティングチームが、現在の販売とプロモーションをアプリのナビゲーションにリストアップしたいとします。通常、弊社のエンジニアは、変更には1週間のリードタイム、アプリストアのレビューには3日間を必要とします。しかし、感謝祭、ブラック・フライデー、サイバー・マンデー、ハヌッカ、クリスマス、お正月の2ヶ月以内には、これらの厳しい締め切り日には間に合わないでしょう。

機能フラグを使用すると、アプリのナビゲーションリンクのコンテンツをBraze でパワーアップでき、マーケティングマネージャが日数ではなく分数で変更できるようになります。

この機能をリモートで設定するには、`navigation_promo_link` という新しい機能フラグを作成し、次の初期プロパティを定義します。

![汎用販売ページに向けたリンクとテキストプロパティを持つ機能フラグ][9]

アプリでは、Braze によるgetter メソッドを使用して、この機能フラグのプロパティを取得し、これらの値に基づいてナビゲーションリンクを構築します。

\`\`\`javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation\_promo\_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// "text"プロパティを読む
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">ホーム</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">products</a>
    <a href="/categories">分類
  </div>
&lt;/>)
```

さて、感謝祭の前日、私たちはBrazeダッシュボードでこれらのプロパティ値を変更しなければなりません。

![感謝祭の販売ページに向けたリンクとテキストプロパティを持つ機能フラグ][10]

その結果、次回誰かがアプリをロードすると、新しい感謝祭の取引が表示されます。

### メッセージ連携

機能フラグを使用して、機能のロールアウトとメッセージングを同期します。これにより、ユーザエクスペリエンスとその関連メッセージングの両方の真理のソースとしてBraze を使用できます。これを実現するには、新しい機能を特定のセグメントまたは視聴者のフィルタされた部分にターゲットします。次に、そのセグメントのみをターゲットとするキャンペーンまたはキャンバスを作成します。 

ユーザーのために、新しいロイヤリティ・リワード・プログラムを開始しているとしよう。マーケティングチームとプロダクトチームが、プロモーション・メッセージングのタイミングを、機能の展開と完全に調整することは難しいかもしれない。キャンバスの機能フラグを使用すると、選択したオーディエンスの機能を有効にし、関連するメッセージングを同じユーザに制御するときに、洗練されたロジックを適用できます。

機能のロールアウトとメッセージングを効率的に調整するために、`show_loyalty_program` という新しい機能フラグを作成します。最初の段階的リリースでは、機能フラグが有効になっている時期と対象をキャンバスで制御します。ここでは、ロールアウトの割合を0% のままにして、ターゲットセグメントを選択しません。

![Loyalty Rewards Programという名前のフィーチャーフラグ。ID はshow\_loyalty\_program で、これがホーム画面とプロファイルページに新しいロイヤルティ報酬プログラムを示しているという説明です。][11]

次に、Canvas Flow で、&quot の`show_loyalty_program` 機能フラグを有効にする[Feature Flag step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) を作成します。これにより、&quot の`show_loyalty_program` 機能フラグが有効になります。

![高価値の顧客セグメントがshow\_loyalty\_program 機能フラグをオンにする、Audience Split ステップを持つキャンバスの例][4]

今、このセグメントのユーザーは新しいロイヤルティプログラムを見始め、それが有効になった後、我々のチームがフィードバックを集めるのを助けるために、電子メールとアンケートが自動的に送られます。

### 機能実験

機能フラグを使用して、新しい機能に関する仮説を試し、確認します。トラフィックを2 つ以上のグループに分割することで、グループ間で機能フラグの影響を比較し、その結果に基づいて最良のアクションを決定できます。

[A/B test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) は、ユーザーの応答を変数の複数バージョンと比較する強力なツールです。

この例では、私たちのチームがeコマースアプリの新しいチェックアウトフローを構築しました。ユーザーエクスペリエンスが向上していると確信していますが、A/Bテストを実行して、アプリの収益に与える影響を測定したいと考えています。

まず、`enable_checkout_v2` という新しい機能フラグを作成します。オーディエンスやロールアウトの割合は追加されません。代わりに、機能フラグ実験を使用してトラフィックを分割し、機能を有効にして、結果を測定します。

アプリでは、機能フラグが有効かどうかを確認し、レスポンスに基づいてチェックアウトフローをスワップアウトします。

\`\`\`javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable\_checkout\_v2");
braze.logFeatureFlagImpression("enable\_checkout\_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />  
} else {
  return <OldCheckoutFlow />
()
\`\`\`

[Feature Flag Experiment][12]でA/B テストを設定します。

今では、ユーザーの50%が古い体験を見て、残りの50%が新しい体験を見てくれるでしょう。次に、2つの変形を解析して、どのチェックアウトフローがより高い変換率をもたらしたかを決定することができる。

![トラフィックを2つの50%グループに分割する機能フラグ実験][6]

勝者を決定したら、このキャンペーンを停止し、エンジニアリングチームが次回のアプリリリースにこのことをハードコードする間、機能フラグのロールアウトパーセンテージをすべてのユーザーに対して100%に増やすことができます。

## 制限事項

次の表では、機能フラグレベルで適用される制限について説明します。有料版の機能フラグを購入するには、Braze アカウントマネージャに連絡するか、Braze ダッシュボードでアップグレードをリクエストします。

| 制限エリア| 無料版| 有料版|
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [アクティブな機能フラグ](#active-feature-flags) | 作業領域ごとに10 | 作業領域ごとに110 |
| [アクティブなキャンペーン実験]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/) | 作業領域ごとに1 | 作業領域ごとに100 |
| [機能フラグキャンバスのステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) | 無制限| 無制限|
{: .reset-td-br-1 .reset-td-br-2}

### アクティブなフィーチャーフラグ

機能フラグはアクティブと見なされ、以下のいずれかが適用されると、制限にカウントされます。

- ロールアウトが0%を超えている
- アクティブなキャンバスで使用
- アクティブな実験で使用

同じ機能フラグがキャンバスで使用され、ロールアウトが50% である場合など、複数の条件に一致する場合でも、制限に向かってアクティブな機能フラグは1 としてカウントされます。

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