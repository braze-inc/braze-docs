---
nav_title: "Shopify 履歴バックフィル"
article_title: "Shopify 履歴バックフィル"
alias: "/shopify_historical_backfill_legacy/"
description: "この参考記事では、Shopifyのヒストリカル・バックフィルを設定する方法について、リスクやサポートされるデータを含めて概説している。"
page_type: partner
search_tag: Partner
page_order: 1
---

# Shopify 履歴バックフィル 

> Shopify の履歴バックフィル機能により、ブランドは自動化されたシームレスな方法で顧客と購入データを同期できます。このため、最も価値が高いセグメントの1つである購入者にすぐに働きかけることができます。 

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

この埋め戻しの一環として、Brazeは、Shopify統合接続前の過去90日間のすべての顧客、注文、購入イベントをインポートする。この機能は、次のセクションで説明する内容を踏まえたると、アクティブなメッセージが実行されていない新しい顧客にとって理想的です。この機能もデータポイントの使用量にカウントされる。

## リスク

この機能は、意図しない結果を引き起こした可能性があるイベントと履歴データをインポートします。このような意図しない結果には、影響を受けたキャンペーンやキャンバスに関して無関係でタイミングが適切ではないメッセージをユーザーが受信したことなどがあります。以下のトリガーイベントを使用しているキャンペーンとキャンバスは、この機能が同期しているShopifyのデータを使用している場合、影響を受ける可能性がある：
- カスタム属性の値を変更する
- 変換イベントを実行する
- キャンペーンの例外イベントを実行する
- サブスクリプションのステータスを更新
- 更新サブスクリプショングループステータス
- メールアドレスを追加する
- 購入*
- カスタムイベント\*を実行する

{% alert important %}
Shopifyのヒストリカル・バックフィルのデータを使って、現在アクティブなキャンペーンとキャンバスに、上記のイベントを引き起こす可能性のあるメッセージがないか監査することをお勧めする。 

- 「購入」と「カスタムイベントを実行」の場合、[期間の開始時刻]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-4-assign-duration)を、Braze で Shopify ストアが接続された後の任意の日時に更新できます。この新しい開始時刻より前に発生した過去のイベントは、メッセージをトリガーしません。 
- 上記以外のイベントについては、バックフィルを有効にする前に[一時的に停止させる]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign)ことで、メッセージが送信されないことを保証することができる。
{% endalert %}

## Shopify 履歴バックフィルの設定

### 前提条件

次のイベントは、バックフィルをオンにする前に有効にしておく必要があります。有効にしないと、データはインポートされません。

- `shopify_created_order`
- Braze 購入イベント 

上記のイベントは、Shopifyのセットアップ中に、[イベント選択]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#event-selection)時に有効にすることができる。

{% alert important %}
バックフィル機能は、統合で一度だけアクティブにできます。
{% endalert %}

### ステップ1:Shopify バックフィルプロセスを開始する

Shopifyパートナーページで [**データバックフィルの開始**] を選択します。既存の Shopify 顧客の場合、データのバックフィルを開始する前に、Braze が過去のすべての注文イベントを収集できるようにアクセスを再認証する必要があります。

![]({% image_buster /assets/img/Shopify/backfill3.png %}){: style="max-width:75%;"}

### ステップ2: Shopifyデータの埋め戻しをトグルする

次に、設定コンポーザーがポップアップ表示され、Shopify 履歴データのバックフィルを有効にすることができます。この埋め戻しの一環として、BrazeはデフォルトでShopify統合前の過去90日間の以下のShopifyデータのみを同期する：
- 注文作成イベント
- Braze 購入イベント
- 顧客データ

具体的にどのような顧客データが埋め戻されているかを見るには、[サポートされているShopifyの顧客データ](#supported-shopify-customer-data)セクションを見ることができる。

{% alert note %}
この機能は、バックフィル中に作成された新規ユーザーのメールおよび SMS サブスクリプションの状態のみを同期します。ユーザーの現在のステータスをオーバーライドしないようにするため、Braze の既存のユーザーのサブスクリプション状態は同期されません。<br><br>現行の動作に関するフィードバックがある場合は、製品ポータルから送信してください。これは [**ダッシュボード**] の [**リソース**] に [**製品ロードマップ**] とリストされています ([新しくなったナビゲーション]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)を使用している場合は、[**コミュニティ**] > [**製品ロードマップ**] を選択してください)。
{% endalert %}

[**次へ**] をクリックすると、バックフィルがアクティブになり、過去のデータの同期が開始されます。履歴バックフィルは**一度**だけ実行できます。このため、データの同期終了後にこのインポートをもう一度実行することはできません。

![]({% image_buster /assets/img/Shopify/backfill1.jpg %}){: style="max-width:75%;"}

### ステップ 3: 埋め戻し作業中

ダッシュボード通知を受け取り、ステータスが [進行中] と表示されたら、バックフィルが開始しています。バックフィルが完了するまでにかかる時間は、BrazeがShopifyから同期する必要がある顧客や注文の数によって異なることに注意してほしい。この間、このページから離れて、バックフィル完了を通知するダッシュボード通知またはメールが届くまで待つことができます。

![]({% image_buster /assets/img/Shopify/backfill2.png %}){: style="max-width:75%;"}

### ステップ 4: 埋め戻しが完了した
Shopify のバックフィルが完了すると、ダッシュボード通知とメールを受け取ります。Shopify パートナーページで [履歴バックフィル] の下のステータスが [完了] に更新されます。

## サポートされている Shopify 顧客データ

### Shopifyカスタム属性

| 属性名 | 説明 |
| --- | --- |
| `shopify_order_count` | このカスタム属性は、この顧客がShopifyで完了した注文の合計に対応する。これは、このプロセスの一部としてバックフィルされたユーザーの場合にのみ使用できます。 |
| `shopify_total_spent` | このカスタム属性は、この顧客が Shopify で支払った総額に対応します。これは、このプロセスの一部としてバックフィルされたユーザーの場合にのみ使用できます。 |
| `shopify_tags` | この属性は、Shopifyの管理者が設定した[顧客タグに](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types)対応する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

### Shopifyの標準属性
- メール
- 名
- 姓
- 電話
- 市区町村
- 国

