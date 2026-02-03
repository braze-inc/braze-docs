--- 
nav_title: 6月
page_order: 6
noindex: true
page_type: update
description: "この記事には、2021年6月のリリースノートが含まれている。"
---

# 2021年6月

## トランザクションメールキャンペーン

トランザクションメールは、送信者と受信者間で合意されたトランザクションを円滑に進めるために送信されます。Brazeの[トランザクションメールキャンペーンは]({{site.baseurl}}/api/api_campaigns/transactional_campaigns)、注文確認、パスワードリセット、請求アラート、その他のビジネスクリティカルな通知など、自動化された非宣伝的なメールメッセージの送信を目的として構築されている。また、対応する[trans アクション al メール エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/)が作成されました。トランザクションメールと新しいエンドポイントは、一部の Braze パッケージのみで使用できます。 

## イベント・プロパティのネストされたオブジェクトのサポート

Braze で、カスタムイベントおよび購入イベントの[ネストされたオブジェクト]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/nested_object_support/)がサポートされるようになりました。ネストされたオブジェクトによって、カスタム・イベントや購入のプロパティとしてデータの配列を送ることができる。このネストされたデータは、Liquidとドット記法を使用することで、APIトリガーメッセージにパーソナライズされた情報をテンプレート化するために使用することができる。

## 新しい HMAC Liquid フィルター

新しい[`hmac_sha1`と`hmac_sha256`リキッドエンコードフィルターs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/)がBraze プラットフォームに追加されました。

## 購入イベントページ

Brazeでの買い物の内容は気になりますか？詳しくは[購入イベントの]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/)記事をご覧いただきたい。

## 新しいBrazeのパートナーシップ

### Nexla - ワークフローの自動化

[Nexla]({{site.baseurl}}/partners/nexla) は統合データ運用分野のリーダーであり、2021年の Gartner Cool Vender に選出されています。Currents を使用してデータウェアハウスにデータを送信するお客様は、Nexla を活用してそのデータを抽出、変換し、他の場所に読み込むことで、エコシステム全体でデータに簡単にアクセスできるようになります。Nexla により、Braze Currents を使用して、ポイントアンドクリックするだけで、カスタム形式のデータを任意の宛先に配信できます。 

### Amperity - 顧客データプラットフォーム

[Amperity]({{site.baseurl}}/partners/amperity/)は、包括的なエンタープライズ顧客データプラットフォームであり、ブランドが自社の顧客を知り、戦略的な意思決定を行い、自社の消費者により良く奉仕するために適切なアクションを一貫して取ることを支援する。Amperity は、顧客データプラットフォームと Braze 全体で顧客の統合ビューを提供し、貴重な Amperity データを Braze に送信できるようにすることで、Braze プラットフォームをサポートします。

### Digioh - アンケート

[Digioh]({{site.baseurl}}/partners/digioh/) は、リストの拡大、ファーストパーティデータの取り込み、Braze キャンペーンでのデータの利用を支援します。ドラッグ＆ドロップビルダーを使用すると、ブランドに合わせたフォーム、ポップアップ、ユーザー設定センター、ランディングページ、顧客とのつながりを築くアンケートなどを簡単に作成できます。

### AppsFlyer オーディエンス- 属性/分析

[AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/) は、モバイルマーケティングにおける分析やアトリビューションを計測するプラットフォームです。マーケティング分析、モバイルアトリビューション、ディープリンクにより、アプリの分析と最適化を支援します。[AppsFlyer Audiences]({{site.baseurl}}/partners/appsflyer_audiences/) を使用すると、オーディエンスセグメントを構築し、これらのセグメントを直接 Braze に渡して、強力なカスタマーエンゲージメントキャンペーンを作成できます。

