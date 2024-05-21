--- 
nav_title: 6月
page_order: 6
noindex: true
page_type: update
description: "この記事には2021年6月のリリースノートが含まれています。"
---

# 2021年6月

## トランザクションメールキャンペーン

トランザクションメールとは、送信者と受信者の間で合意されたトランザクションを容易にするために送信されるメールのことです。Braze の[ トランザクションメールキャンペーン]({{site.baseurl}}/api/api_campaigns/transactional_campaigns) は、注文の確認、パスワードのリセット、請求アラート、またはその他のビジネスクリティカルな通知など、自動化された非プロモーションメールメッセージを送信する目的で構築されています。さらに、対応する[トランザクションメールエンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/) が作成されました。トランザクションメールと新しいエンドポイントは、選択したブレーズパッケージの一部としてのみ使用できます。 

## イベント・プロパティーのネストされたオブジェクト・サポート

Braze では、カスタムイベントおよび購入イベントの[ネストされたオブジェクト]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/nested_object_support/) がサポートされるようになりました。ネストされたオブジェクトを使用すると、カスタムイベントおよび購入のプロパティとしてデータの配列を送信できます。このネストされたデータは、Liquid およびdot 表記を使用してAPI トリガー・メッセージ内のパーソナライズされた情報をテンプレート化するために使用できます。

## 新HMAC Liquidフィルター

新しい[`hmac_sha1`と`hmac_sha256`液体エンコーディングフィルタ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/)がブレーズプラットフォームに追加されました。

## 購入イベントページ

Brazeでの購入イベントの詳細についてお気に入りですか?詳しくは、専用の[購入イベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/)記事をご覧ください。

## 新たなろう付けパートナーシップ

### Nexla - ワークフロー自動化

[Nexla]({{site.baseurl}}/partners/nexla) は、統合されたデータ操作と2021年のGartner Cool Vendor のリーダーです。Currents を使用してデータウェアハウスにデータを送信する顧客は、Nexla を活用して、そのデータを他の場所に抽出、変換、ロードすることができます。これにより、データはエコシステム全体で簡単にアクセスできるようになります。Nexla では、Braze Currents を使用して、簡単なポイントで選択した宛先に配信されるカスタム形式のデータを取得し、クリックすることができます。 

### Amperity - 顧客データプラットフォーム

[Amperity]({{site.baseurl}}/partners/amperity/)は、包括的なエンタープライズ顧客データプラットフォームであり、ブランドが顧客を知り、戦略的な意思決定を行い、一貫して正しい行動方針を取ることで、消費者により良いサービスを提供することを支援します。Amperityは、貴重なAmperityデータをBrazeに送ることができるように、顧客のCDPとBraze全体の統一されたビューを提供することで、Brazeプラットフォームをサポートしています。

### デジオ・サーベイ

[Digioh]({{site.baseurl}}/partners/digioh/) は、リストの拡大、ファーストパーティデータのキャプチャ、ブレーズキャンペーンでのデータの使用を支援します。ドラッグ・アンド・ドロップ・ビルダーは、顧客とつながるブランド・フォーム、ポップアップ、嗜好センター、ランディング・ページ、アンケートを簡単に作成することができる。

### AppsFlyer オーディエンス- 属性/分析

[AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/) は、マーケティング分析モバイル属性およびディープリンクを通じてアプリの分析と最適化を支援するモバイルマーケティング分析および属性プラットフォームです。[AppsFlyer Audiences]({{site.baseurl}}/partners/appsflyer_audiences/) を使用すると、オーディエンスセグメントを構築し、これらのセグメントを直接Braze に渡して強力なカスタマーエンゲージメントキャンペーンを作成できます。

