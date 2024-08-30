---
nav_title: "Shopifyヒストリカル・バックフィル"
article_title: "Shopifyヒストリカル・バックフィル"
alias: "/shopify_historical_backfill/"
description: "この参考記事では、Shopifyのヒストリカル・バックフィルを設定する方法について、リスクやサポートされるデータを含めて概説している。"
page_type: partner
search_tag: Partner
page_order: 1
---

# Shopifyヒストリカル・バックフィル 

> Shopifyのヒストリカル・バックフィル機能により、ブランドは自動化されたシームレスな方法で顧客と購買データを同期することができる。 

この埋め戻しの一環として、Brazeは、Shopify統合接続前の過去90日間のすべての顧客、注文、購入イベントをインポートする。この機能は、次のセクションで説明する意味を考えると、アクティブなメッセージを走らせていない新しい顧客にとって理想的であることに注意してほしい。この機能もデータポイントの使用量にカウントされる。

## リスク

この機能は、過去のデータとイベントをインポートし、影響を受けたキャンペーンやキャンバスに対して、ユーザーが無関係なメッセージを受け取ったり、不適切なメッセージを受け取ったりするような、意図しない結果を招く可能性がある。以下のトリガーイベントを使用しているキャンペーンとキャンバスは、この機能が同期しているShopifyのデータを使用している場合、影響を受ける可能性がある：
- カスタム属性の値を変更する
- 変換イベントを実行する
- キャンペーンの例外イベントを実行する
- 購読ステータスを更新する
- サブスクリプション・グループのステータスを更新する
- メールアドレスを追加する
- 購入する
- カスタムイベント\*を実行する

{% alert important %}
Shopifyのヒストリカル・バックフィルのデータを使って、現在アクティブなキャンペーンとキャンバスに、上記のイベントを引き起こす可能性のあるメッセージがないか監査することをお勧めする。 

- Make Purchase "と "Perform Custom Event "については、ShopifyストアがBrazeに接続された後、[開始時間の期間を]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/?redirected=true#step-4-assign-duration)任意の日時に更新することができる。この新しい開始時刻以前の過去のイベントは、いかなるメッセージもトリガーされない。 
- 上記以外のイベントについては、バックフィルを有効にする前に[一時的に停止させる]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign)ことで、メッセージが送信されないことを保証することができる。
{% endalert %}

## Shopifyヒストリカル・バックフィルを設定する

### 前提条件

バックフィルをオンにする前に、以下のイベントを有効にしておく必要がある：

- `shopify_created_order`
- ブレイズ購入イベント 

上記のイベントは、Shopifyのセットアップ中に、[イベント選択]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#event-selection)時に有効にすることができる。

{% alert important %}
バックフィル機能を有効にできるのは、統合の中で一度だけである。
{% endalert %}

### ステップ1:Shopifyのバックフィル・プロセスを開始する

Shopifyのパートナーページで、**Start Data Backfillを**選択する。Shopifyの既存顧客については、データの埋め戻しを開始する前に、Brazeが過去の注文イベントをすべて収集できるよう、アクセスを再承認する必要がある。

![][3]{: style="max-width:75%;"}

### ステップ2:Shopifyデータの埋め戻しをトグルする

次に、セットアップ・コンポーザーがポップアップし、オプションで過去のShopifyデータのバックフィルを有効にすることができる。この埋め戻しの一環として、BrazeはデフォルトでShopify統合前の過去90日間の以下のShopifyデータのみを同期する：
- オーダー作成イベント
- ブレイズ購入イベント
- 顧客データ

具体的にどのような顧客データが埋め戻されているかを見るには、[サポートされているShopifyの顧客データ](#supported-shopify-customer-data)セクションを見ることができる。

{% alert note %}
この機能は、バックフィル中に作成された新規ユーザーのEメールとSMSの購読状態のみを同期する。これは、ユーザーの現在のステータスを上書きしないように、Brazeの既存ユーザーの購読ステータスを同期しない。<br><br>現在の動作に関するフィードバックがある場合は、**ダッシュボードの**「**リソース**」にある「**製品ロードマップ」**（[更新されたナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**「コミュニティ**」>「**製品ロードマップ**」を選択）に記載されている製品ポータルから提出する。
{% endalert %}

**次へ」を**クリックすると、バックフィルが有効になり、過去のデータの同期が開始される。ヒストリカル・バックフィルは**一度しか**完了できないので、データの同期が完了した後、このインポートを再度実行することはできない。

![][1]{: style="max-width:75%;"}

### ステップ3:埋め戻し作業中

ダッシュボードに通知が届き、ステータスが「進行中」と表示され、埋め戻しが開始されたことがわかる。バックフィルが完了するまでにかかる時間は、BrazeがShopifyから同期する必要がある顧客や注文の数によって異なることに注意してほしい。この間は、このページから離れ、埋め戻しが完了したことを知らせるダッシュボードの通知やEメールを待つことができる。

![][2]{: style="max-width:75%;"}

### ステップ4:埋め戻しが完了した
Shopifyのバックフィルが完了すると、ダッシュボード通知とメールが届く。また、Shopifyのパートナーページでは、ヒストリカル・バックフィルのステータスが "Complete "に更新される。

## Shopifyの顧客データをサポート

### Shopifyカスタム属性

| 属性名 | 説明 |
| --- | --- |
| `shopify_order_count` | このカスタム属性は、この顧客がShopifyで完了した注文の合計に対応する。これは、このプロセスの一環としてバックフィルされたユーザーに対してのみ有効である。 |
| `shopify_total_spent` | このカスタム属性は、この顧客がShopifyで使用した合計金額に対応する。これは、このプロセスの一環としてバックフィルされたユーザーに対してのみ有効である。 |
| `shopify_tags` | この属性は、Shopifyの管理者が設定した[顧客タグに](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types)対応する。 |
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
