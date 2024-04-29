---
nav_title: "Shopify 履歴バックフィル"
article_title: "Shopify 履歴バックフィル"
alias: "/shopify_historical_backfill/"
description: "このリファレンス記事では、リスクやサポートされるデータなど、Shopify 履歴バックフィルを設定する方法について説明します。"
page_type: partner
search_tag: Partner
page_order: 1
---

# Shopify 履歴バックフィル 

> Shopify 履歴バックフィル機能を使用すると、ブランドは顧客と購入データを自動的かつシームレスに同期できるため、最も価値のあるセグメントの 1 つである購入者とのエンゲージメントをすぐに開始できます。 

このバックフィルの一環として、Braze は Shopify 統合接続前の過去 90 日間のすべての顧客、注文、購入イベントをインポートします。次のセクションで説明する影響を考慮すると、この機能はアクティブなメッセージが実行されていない新しい顧客に最適であることに注意してください。この機能はデータ ポイントの使用量にもカウントされます。

## リスク

この機能は、影響を受けるキャンペーンやキャンバスに関してユーザーが無関係なメッセージをタイミング悪く受信するなど、予期しない結果をもたらす可能性のある履歴データとイベントをインポートします。次のトリガー イベントを使用するキャンペーンとキャンバスは、この機能が同期する Shopify データを使用している場合に影響を受ける可能性があります。
カスタム属性値を変更
コンバージョンイベントを実行
キャンペーンの例外イベントを実行
サブスクリプションのステータスを更新
サブスクリプショングループのステータスを更新
メールアドレスを追加します
購入 ()
カスタムイベント () を実行

{% alert important %}
Shopify 履歴バックフィルのデータを使用して、現在アクティブなキャンペーンとキャンバスで上記のイベントをトリガーする可能性のあるメッセージを監査することをお勧めします。 

- 「購入する」と「カスタム イベントを実行する」の場合、Braze で Shopify ストアが接続された後、 [開始時間の期間を]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/?redirected=true#step-4-assign-duration) 任意の日付と時刻に更新できます。この新しい開始時刻より前の過去のイベントでは、メッセージはトリガーされません。 
- 上記の他のすべてのイベントについては、バックフィルをアクティブ化する前に [一時的に停止して]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign) 、メッセージが送信されないようにすることができます。
{% endalert %}

## Shopify 履歴バックフィルの設定

### 前提条件

バックフィルをオンにする前に、次のイベントを有効にする必要があります。有効にしないと、データはインポートされません。

- `shopify_created_order`
- Braze 購入イベント 

上記のイベントは、 [イベント選択]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#event-selection)中にShopifyを設定するときに有効にすることができます。

{% alert important %}
バックフィル機能は統合時に 1 回だけ有効にできます。
{% endalert %}

### ステップ1:Shopifyバックフィルプロセスを開始する

Shopify パートナーページで、**「データバックフィルの開始」を**選択します。既存の Shopify 顧客の場合、データのバックフィルを開始する前に、Braze が過去のすべての注文イベントを収集できるようにアクセスを再承認する必要があります。

![][3]{: style="max-width:75%;"}

### ステップ2:Shopifyデータのバックフィルをオンにする

次に、セットアップ コンポーザーがポップアップ表示され、オプションで過去の Shopify データのバックフィルを有効にすることができます。このバックフィルの一環として、Braze はデフォルトで、Shopify 統合前の過去 90 日間の次の Shopify データのみを同期します。
注文作成イベント
Braze 購入イベント
顧客データ

バックフィルされる具体的な顧客データを確認するには、 [サポートされている Shopify 顧客データ](#supported-shopify-customer-data) セクションにアクセスしてください。

{% alert note %}
この機能は、バックフィル中に作成された新しいユーザーの電子メールと SMS サブスクリプションの状態のみを同期します。これにより、ユーザーの現在のステータスが上書きされないように、Braze の既存ユーザーのサブスクリプション状態は同期されません。<br><br>現在の動作に関するフィードバックがある場合は、 **ダッシュボード** の **「リソース** 」の「 **製品ロード** マップ」にリストされている製品ポータルから送信してください ( [更新されたナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、**「コミュニティ** > **製品ロードマップ**」を選択してください)。
{% endalert %}

**「次へ」**をクリックすると、バックフィルが有効になり、過去のデータの同期が開始されます。履歴バックフィルは **1 回しか**実行できないため、データの同期が完了した後は、このインポートを再度実行できないことに注意してください。

![][1]{: style="max-width:75%;"}

### ステップ3:埋め戻し進行中

ダッシュボード通知が届き、ステータスが「進行中」と表示され、バックフィルが開始されたことが示されます。バックフィルが完了するまでの時間は、Braze が Shopify から同期する必要がある顧客と注文の数によって異なることに注意してください。この間、このページを離れて、バックフィルが完了したことを通知するダッシュボード通知または電子メールを待つことができます。

![][2]{: style="max-width:75%;"}

### ステップ4:埋め戻し完了
Shopify バックフィルが完了すると、ダッシュボード通知とメールが届きます。Shopify パートナー ページでも、履歴バックフィルのステータスが「完了」に更新されます。

## サポートされているShopify顧客データ

### Shopifyカスタム属性

| 属性名 | 説明 |
| --- | --- |
| `shopify_order_count`| このカスタム属性は、この顧客が Shopify で完了した注文の合計に対応します。これは、このプロセスの一環としてバックフィルされたユーザーのみが利用できます。 |
| `shopify_total_spent`| このカスタム属性は、この顧客が Shopify で費やした合計金額に対応します。これは、このプロセスの一環としてバックフィルされたユーザーのみが利用できます。 |
| `shopify_tags`| この属性は、Shopify 管理者によって設定された [顧客タグ](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types) に対応します。 |
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
