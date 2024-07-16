---
nav_title: Alpaco
article_title:アルパコ
alias: /partners/Alpaco
description:BrazeとAlpacoの統合は、Alpacoの構文を活用してデータ駆動型のメールテンプレートを作成し、Brazeにエクスポートします。
page_type: partner
search_tag:Partner

---

# アルパコ

> [アルパコ](https://alpaco.email/)は、デザインと出力の新しいレベルの制御のためのドラッグアンドドロップのメールエディタを提供するオンラインのメールマーケティングツールです。BrazeとAlpacoの統合により、ブランドに合ったデータ駆動型のメールをBrazeにエクスポートできます。 

{% alert note %}
Alpacoは[完全なLiquid](https://shopify.github.io/liquid/)変数をサポートしており、そのため、Braze構成で使用されるLiquid変数も完全にサポートしています。
{% endalert %}

## 前提条件

| 要件 | 説明 |
| ------------| ----------- |
| アルパコアカウント | このパートナーシップを利用するには、Alpacoアカウントが必要です。 |
| Braze REST API キー | 完全な**テンプレート**権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| クラスタインスタンス | お客様のBraze[クラスターインスタンス]({{site.baseurl}}/api/basics/#endpoints)は、BrazeダッシュボードおよびRESTエンドポイントと一致します。<br><br> 例えば、ダッシュボードのURLが`https://dashboard-03.braze.com`の場合、エンドポイントは`dashboard-03`になります。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

BrazeのREST APIキーとクラスターインスタンスをAlpacoのカスタマーサクセスチームに提供してください。チームはその後、初期統合を設定します。

{% alert note %}
これは一度限りの設定であり、将来のエクスポートは自動的にこのAPIキーを使用します。
{% endalert %}

## BrazeへのAlpacoメールのエクスポート

### ステップ1:アルパコでメールテンプレートを作成する

Alpacoプラットフォームでは、さまざまな設定やオプションを使用して、ブランドアイデンティティを表現するテンプレートを作成します。**保存**を選択して、テンプレートに満足したら。

![Alpaco Create template]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### ステップ2:メールを作成

テンプレートが作成された後、ロビーに移動してテンプレートを使用してメールを作成します。**レビュー**を選択して、すべてが正しいことを確認してください。

![Alpaco Create email]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### ステップ3:レビューとエクスポートメールをBrazeに送信

**エクスポート**を選択し、Braze統合を選択して、メールテンプレートをBrazeにエクスポートします。 

メールテンプレートに変更を加えたい場合は、Alpacoで変更を行い、その後再度メールをBrazeにエクスポートしてください。これにより、Brazeのメールが変更内容で更新されます。

![Alpaco Export email]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## BrazeでAlpacoのメールテンプレートを使用する

Brazeダッシュボードで**テンプレートとメディア > メールテンプレート**に移動して、アップロードしたAlpacoメールを見つけてください。これで、このテンプレートを使用して、ブランドに合ったデータ駆動型のメールをユーザーに送信できます。

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
