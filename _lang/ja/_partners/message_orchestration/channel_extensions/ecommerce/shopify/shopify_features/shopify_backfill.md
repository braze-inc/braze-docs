---
nav_title: "Shopify 履歴バックフィル"
article_title: "Shopify 履歴バックフィル"
alias: "/shopify_historical_backfill/"
description: "このリファレンス記事では、リスクやサポートされているデータを含め、Shopifyの履歴バックフィルを設定する方法について説明します。"
page_type: partner
search_tag: Partner
page_order: 1
---

# Shopify 履歴バックフィル 

> 「Shopify Historical Backfill」機能を使用すると、ブランドは顧客と同期し、自動化されたシームレスな方法でデータを購入できるため、最も価値のあるセグメントの1つ(購入者)とすぐに関わり始めることができます。 

このバックフィルの一部として、Braze は、Shopify 統合接続の直前90 日間のすべての顧客、注文、および購入イベントをインポートします。この機能は、次のセクションで説明する内容を考慮すると、アクティブなメッセージが実行されていない新しい顧客に適しています。この機能は、データポイントの使用状況にもカウントされます。

## リスク

この機能は、影響を受けたキャンペーンやキャンバスに対して、ユーザが無関係で時間外のメッセージを受信するなど、予期しない結果を招く可能性のある履歴データやイベントをインポートします。次のトリガーイベントを使用するキャンペーンとキャンバスは、この機能が同期しているShopifyデータのいずれかを使用している場合、影響を受ける可能性があります。
カスタム属性値を変更
コンバージョンイベントを実行
キャンペーンの例外イベントを実行
サブスクリプションのステータスを更新
サブスクリプショングループのステータスを更新
メールアドレスを追加します
購入:
カスタムイベントを実行:

{% alert important %}
Shopify Historical Backfillのデータを使用して、上記のイベントをトリガーする可能性のあるメッセージについて、現在アクティブなキャンペーンとキャンバスを監査することをお勧めします。 

- "Make Purchase"および"Perform Custom Event"では、[開始時間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/?redirected=true#step-4-assign-duration)を、ShopifyストアがBrazeに接続された後の任意の日時に更新できます。この新しい開始時間より前の過去のイベントは、メッセージをトリガーしません。 
- 上記の他のすべてのイベントについては、メッセージが送信されないことを保証するために、バックフィルを有効にする前に[一時的に停止]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign)することができます。
{% endalert %}

## Shopifyヒストリカル・バックフィルのセットアップ

### 前提条件

次のイベントは、バックフィルをオンにする前に有効にする必要があります。有効にしないと、データはインポートされません。

- `shopify_created_order`
- Braze 購入イベント 

上記のイベントは、[イベント選択]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#event-selection)時にShopifyを設定する際に有効にすることができます。

{% alert important %}
バックフィル機能は、統合で一度だけ有効にできます。
{% endalert %}

### ステップ1:Shopify バックフィルプロセスの開始

Shopifyパートナーページで、**Start Data Backfill**を選択します。既存のShopify 顧客の場合、データのバックフィルを開始する前に、Braze が過去のすべての注文イベントを収集するためのアクセスを再認証する必要があります。

![][3]{: style="max-width:75%;"}

### ステップ2:Shopifyデータのバックフィルを切り替える

次に、セットアップ・コンポーザーがポップアップ表示され、オプションで、履歴Shopifyデータのバックフィルを有効にすることができます。このバックフィルの一部として、Braze は、デフォルトでShopify 統合の直前90 日間、以下のShopify データのみを同期します。
注文作成イベント
Braze 購入イベント
顧客データ

どの特定の顧客データがバックフィルされているかを確認するには、[Supported Shopify customer data](#supported-shopify-customer-data) セクションを参照してください。

{% alert note %}
この機能は、バックフィル中に作成された新規ユーザの電子メールとSMS サブスクリプションの状態のみを同期します。これは、ユーザの現在のステータスをオーバーライドしないように、Braze で既存のユーザのサブスクリプションステートを同期しません。<br><br>現在の動作に関するフィードバックがある場合は、製品ポータルから送信してください。**Dashboard**の**Resources**に**Product Roadmap**と記載されています(弊社の[updated navigation]({{site.baseurl}}/navigation)を使用している場合は、**Community**> **Product
{% endalert %}

**Next** を押すと、バックフィルがアクティブになり、過去のデータに対して同期が開始されます。Historical Backfill は**once** のみ完了することができるため、データの同期が完了した後にこのインポートを再度実行することはできません。

![][1]{: style="max-width:75%;"}

### ステップ3:バックフィル中

ダッシュボード通知を受け取り、ステータスが"In Progress"として表示され、バックフィルが開始されたことを示します。バックフィルが完了するまでにかかる時間は、顧客の数によって異なり、Braze がShopify から同期する必要がある注文の数によって異なります。この間、このページを離れ、ダッシュボードの通知または電子メールがバックフィルが完了したことを通知するまで待機できます。

![][2]{: style="max-width:75%;"}

### ステップ4:バックフィル完了
Shopify のバックフィルが完了すると、ダッシュボード通知とメールが送信されます。Shopifyパートナーページは、Historical Backfillのステータスを"Complete"に更新します。

## サポートされているShopifyの顧客データ

### Shopifyのカスタム属性

| 属性名| 説明|
| --- | --- |
| `shopify_order_count` | このカスタム属性は、この顧客がShopifyで完了した注文の合計に対応します。これは、このプロセスの一部としてバックフィルされたユーザーに対してのみ使用できます。|
| `shopify_total_spent` | このカスタム属性は、この顧客がShopifyで費やした合計金額に対応します。これは、このプロセスの一部としてバックフィルされたユーザーに対してのみ使用できます。|
| `shopify_tags` | この属性は、Shopify admins によって設定された[カスタマータグ](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) に対応します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

### Shopify標準属性
- メールアドレス
- 名
- 姓
- 電話
- 市区町村
- 国

[1]: {% image_buster /assets/img/Shopify/backfill1.jpg %}
[2]: {% image_buster /assets/img/Shopify/backfill2.png %}
[3]: {% image_buster /assets/img/Shopify/backfill3.png %} 
