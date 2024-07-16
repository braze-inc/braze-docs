---
nav_title: 「Shopify ヒストリカルバックフィル」
article_title:「Shopify ヒストリカルバックフィル」
alias: 「/shopify_historical_backfill/"
description:「この参考記事では、リスクやサポート対象データを含め、Shopifyの履歴バックフィルの設定方法を概説しています。「
page_type: partner
search_tag:Partner
page_order:1
---

# Shopify ヒストリカルバックフィル 

> Shopify Historical Backfill機能を使用すると、ブランドは顧客と購入データを自動的かつシームレスに同期できるため、最も価値のあるセグメントの1つである購入者とのエンゲージメントをすぐに開始できます。 

このバックフィルの一環として、BrazeはShopify統合接続前の過去90日間のすべての顧客、注文、購入イベントをインポートします。この機能は、次のセクションで説明する内容を考慮すると、アクティブなメッセージがまったく実行されていない新規のお客様に最適であることに注意してください。この機能は、データポイント使用量にもカウントされます。

## リスク

この機能は、影響を受けたキャンペーンやキャンバスについて、ユーザーが無関係でタイミングの悪いメッセージを受け取るなど、意図しない結果をもたらす可能性のある履歴データやイベントをインポートします。以下のトリガーイベントを使用するキャンペーンとキャンバスは、この機能が同期しているShopifyデータのいずれかを使用している場合に影響を受ける可能性があります。
- カスタム属性値の変更
- コンバージョンイベントを実行
- キャンペーンの例外イベントを実行
- 購読状況の更新
- サブスクリプショングループステータスの更新
- Eメールアドレスを追加
- 購入する*
- カスタムイベントを実行*

{% alert important %}
Shopify Historical Backfillのデータを使用して、現在アクティブなキャンペーンとキャンバスを監査して、上記のイベントトリガー可能性のあるメッセージがないか確認することをおすすめします。 

- 「購入」と「カスタムイベントを実行」では、[開始時間を]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/?redirected=true#step-4-assign-duration)、ShopifyストアがBrazeに接続された後の任意の日時に更新できます。この新しい開始時刻より前の過去のイベントでは、メッセージはトリガーされません。 
- 上記の他のすべてのイベントについては、[バックフィルを有効にする前に一時的に停止して]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign)、メッセージが送信されないようにすることができます。
{% endalert %}

## Shopify ヒストリカルバックフィルのセットアップ

### 前提条件

バックフィルを有効にする前に次のイベントを有効にする必要があります。有効にしないと、そのデータはインポートされません。

- `shopify_created_order`
- Braze 購入イベント 

[上記のイベントは、イベント選択時にShopify設定する際に有効にできます。]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#event-selection)

{% alert important %}
バックフィル機能は、インテグレーションで一度だけ有効にできます。
{% endalert %}

### ステップ1:Shopifyのバックフィルプロセスを開始する

Shopify パートナーページで、\[**データバックフィルを開始**] を選択します。Shopifyの既存のお客様の場合、データのバックフィルを開始する前に、Brazeが過去の注文イベントをすべて収集できるようにアクセスを再認証する必要があります。

![][3]{: style="max-width:75%;"}

### ステップ2:Shopifyデータのバックフィルをオンに切り替える

次に、セットアップコンポーザーがポップアップし、オプションで過去のShopifyデータのバックフィルを有効にできます。このバックフィルの一環として、Brazeはデフォルト Shopify統合前の過去90日間の以下のShopifyデータのみを同期します。
- 注文作成イベント
- Braze 購入イベント
- 顧客データ

どの特定の顧客データがバックフィルされているかを確認するには、[サポート対象のShopifyの顧客データセクションをご覧ください](#supported-shopify-customer-data)。

{% alert note %}
この機能は、バックフィル中に作成された新規ユーザーのメールとSMSのサブスクリプション状態のみを同期します。これにより、ユーザーの現在のステータスが上書きされないように、Braze の既存のユーザーのサブスクリプションステータスは同期されません。<br><br>現在の行動に関するフィードバックがある場合は、**ダッシュボードの** \[**Resources** as **Product Roadmap**] に一覧表示されている製品ポータルから送信してください ([更新されたナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、\[**コミュニティ**] > \[**製品ロードマップ**] を選択します)。
{% endalert %}

\[**次へ] をクリックすると**、バックフィルが有効になり、過去のデータの同期が開始されます。**ヒストリカル・バックフィルは一度しか完了できないため**、データの同期が完了した後にこのインポートを再度実行することはできないことに注意してください。

![][1]{: style="max-width:75%;"}

### ステップ3:バックフィル中

ダッシュボードに通知が届き、バックフィルが開始されたことを示すステータスが「進行中」と表示されます。バックフィルが完了するまでにかかる時間は、BrazeがShopifyから同期する必要があるお客様と注文の数によって異なりますのでご注意ください。この間は、このページを離れ、バックフィルの完了を知らせるダッシュボード通知またはメールくのを待つことができます。

![][2]{: style="max-width:75%;"}

### ステップ 4:バックフィルが完了しました
Shopifyのバックフィルが完了すると、ダッシュボード通知とメールが届きます。Shopify パートナーページでも、履歴バックフィルのステータスが「完了」更新されます。

## サポートされているShopifyの顧客データ

### Shopify カスタム属性

| 属性名 | 説明 |
| --- | --- |
| `shopify_order_count` | このカスタム属性は、この顧客 Shopifyで完了した注文の合計に対応します。これは、このプロセスの一環としてバックフィルされたユーザーのみが使用できます。 |
| `shopify_total_spent` | このカスタム属性は、この顧客 Shopifyで費やした合計金額に対応します。これは、このプロセスの一環としてバックフィルされたユーザーのみが使用できます。 |
| `shopify_tags` | この属性は、[Shopify管理者が設定した顧客ータグに対応しています](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types)。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

### Shopifyの標準属性
- メール
- 名
- 姓
- 電話
- 市区町村
- 国

[1]: {% image_buster /assets/img/Shopify/backfill1.jpg %}
[2]: {% image_buster /assets/img/Shopify/backfill2.png %}
[3]: {% image_buster /assets/img/Shopify/backfill3.png %} 
