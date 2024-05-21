---
nav_title: ベストプラクティス
article_title: キャンペーンのベストプラクティス
page_order: 0
description: "この記事では、キャンペーンを作成してカスタマイズするためのベストプラクティスについて説明します。"
tool: Campaign

---

# キャンペーンのベストプラクティス

## Braze の 4 つの T

Braze では、当社のプラットフォーム上で利用する予定の顧客データのみを送信することを推奨しています。「Braze の 4 つの T」の哲学に基づき、次の目的に使用するデータのみを送信するようにしてください。

- [オーディエンスセグメント]({{site.baseurl}}/user_guide/engagement_tools/segments/)を構築してオーディエンスを**ターゲティング**するため
- [アクションベース]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery#action-based-delivery)または [API トリガーの]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)配信でメッセージを**トリガー**するため
- [Liquid の条件付きロジック]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)でメッセージを**テンプレート化**し、パーソナライズするため
- [コンバージョントラッキング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events?redirected=true#conversion-events)でキャンペーンの効果を**トラッキング**するため

これにより、Braze に送信されるデータを最適化して、チームにとって長期的に有用であると思われないトラッキングデータポイントを避けながら、ユーザーにメッセージを送る機能を合理化することができます。

## ユーザーのターゲット設定

キャンペーンを徐々に積み上げていくうちに、オーディエンスの減少に気づくことがあります。これは、セグメンテーションを利用して[離脱ユーザー]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/)を特別なキャンペーンでターゲティングできる重要な機会となります。

### オーディエンスを特定する

オーディエンスを定義することで、セグメントとフィルターをうまく活用できます。キャンペーンやメッセージが誰をターゲットとしているのかを考えます。この重要な情報を使って、さまざまなチャネルでメッセージを柔軟に構築できる[マルチチャネルキャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-you-create-a-multichannel-campaign)を作成し、オーディエンスの通知設定に合わせることができます。

一貫性のあるユーザーに感謝の気持ちを示すには、[アクティブユーザー]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/active_user_campaigns/)を理解することも重要です。

## マルチチャネルのキャンペーン

### 機能の認知度

アプリの新しい機能やバージョンにユーザーを引き付けることが目的の場合は、アプリ内チャネルに焦点を当てたマルチチャネル戦略を使用します。[アプリ内メッセージ][5] と [コンテンツカード][7] は、ユーザーがすぐに更新を希望しない場合でも、一般に反感を買うことはありません。適切なアプリストアへの[ディープリンク]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/)を必ず含めます。

アプリを更新したり、アプリの使い方を変えてもらうようにユーザーを説得するのは難しいので、新しいバージョンや新機能のすべての利点と、それによってアプリの使用感がどのように向上するかを伝えましょう。

### 送信のタイミング

タイミングはとても重要です。ユーザーを説得してアプリを更新してもらうのが目的なら、アプリ内でポジティブな体験が得られるまで待ってからユーザーに尋ねましょう。オーディエンスを引きつけるには、邪魔に感じられるメッセージングの繰り返しは避けます。

時間が経つにつれ、ユーザーは特定の機能を忘れたり、新しい機能に気づかなくなったりすることがあります。新しい機能が追加されたら、[アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)でユーザーに知らせましょう。ユーザーがアプリ内で主要な機能を使っていない場合は、ユーザーがアプリを使い、この新機能がいつ役に立つのかを知らせるのが最善かもしれません。[データのオプトイン][7] の記事には、ユーザーのワークフローの期待にあなたのリクエストを確実に一致させるための詳細が掲載されています。

## 高評価

アプリストアで 5 つ星の評価を得ることは、すべてのモバイルマーケターのウィッシュリスト項目です。しかし、ポジティブなレビューを獲得するにはユーザーに作業してもらう必要があるため、簡単なことではありません。弊社の機能をうまく応用すれば、カスタマーエンゲージメントを高めることが可能になります。

### パワーユーザーをターゲットにする

パワーユーザーはアプリの支持者になることができます。多くの場合、彼らは継続的にアプリを使用しており、アプリを改善するためのフィードバックを提供することができます。アプリによって異なりますが、一般にパワーユーザーには次のような傾向があります。

- 多くのセッションを記録している
- アプリを最近使った
- お金を費やし、買い物をした

評価を上げるためには、パワーユーザーにアプリストアでアプリのレビューを依頼しましょう。ポジティブな評価をしてもらえる可能性が高くなります。例えば、以下のフィルターで「パワーユーザー」という名前のセグメントを作成します。
\- これらのアプリを過去 14 日間で 10 回以上使用している
\- 50 ドル以上使っている

![][6]

アプリストアへの訪問は、ユーザーの時間を消費します。余分な労力をかけてもらえる可能性を最大限にするには、ユーザーがアプリでポジティブな体験をした後に評価やレビューを依頼します。例えば、ゲームレベルを超えたり、割引コードを使って買い物をした後などに尋ねてみます。[データのオプトイン]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)に関する記事に、ユーザーのワークフローの期待にあなたのリクエストを確実に一致させるための詳細が掲載されています。


[6]: {% image_buster /assets/img_archive/ratings_power_users.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/