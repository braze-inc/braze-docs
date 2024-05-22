---
nav_title: アルパコ
article_title: アルパコ
alias: /partners/Alpaco
description: "Braze とAlpaco の統合は、Alpaco の構文を利用して、データ駆動型のメールテンプレートを作成し、Braze にエクスポートします。"
page_type: partner
search_tag: Partner

---

# アルパコ

> [Alpaco](https://alpaco.email/) は、デザインと出力の新しいレベルの制御のためのドラッグアンドドロップ電子メールエディタを提供するオンライン電子メールマーケティングツールです。Braze とAlpaco の統合により、ブランドおよびデータ駆動型のメールをBraze にエクスポートできます。 

{% alert note %}
Alpaco では、[完全なLiquid](https://shopify.github.io/liquid/) 変数がサポートされています。このような変数は、Braze 構成で使用されるすべてのLiquid 変数も完全にサポートされています。
{% endalert %}

## 前提条件

| 要件 | 説明 |
| ------------| ----------- |
| Alpacoアカウント| このパートナーシップを活用するには、Alpacoアカウントが必要です。|
| Braze REST API キー| 完全な**テンプレート** 権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys**.| からBraze ダッシュボードで作成できます。
| クラスタインスタンス| Braze [cluster instance]({{site.baseurl}}/api/basics/#endpoints) は、Braze ダッシュボードとREST エンドポイントに合わせます。<br><br> たとえば、ダッシュボードのURL が`https://dashboard-03.braze.com` の場合、エンドポイントは`dashboard-03` になります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

AlpacoカスタマーサクセスチームにBraze REST APIキーとクラスターインスタンスを提供します。チームは、最初の統合を設定します。

{% alert note %}
これは1 回限りのセットアップであり、今後のエクスポートではこのAPI キーが自動的に使用されます。
{% endalert %}

## AlpacoメールのBrazeへのエクスポート

### ステップ 1: Alpaco でのメールテンプレートの作成

Alpacoプラットフォームでは、さまざまな設定とオプションを使用して、ブランドアイデンティティを表すテンプレートを作成します。テンプレートに満足したら、**Save**を選択します。

![Alpaco Create template]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### ステップ 2: メールを作成する

テンプレートが作成されたら、ロビーに移動し、テンプレートを含むメールを作成します。**Review**を選択して、すべてが正しく見えることを確認します。

![Alpaco Create email]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### ステップ 3: メールをレビューし、Brazeにエクスポートする

**Export**を選択し、Braze 統合を選択してメールテンプレートをBraze にエクスポートします。 

メールテンプレートに変更を加える場合は、Alpaco でそれらの変更を行い、メールを再びBraze にエクスポートします。これにより、Braze 内の電子メールが変更されます。

![Alpaco Export email]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Brazeでのアルパコメールテンプレートの使用

アップロードしたAlpaco メールを見つけるには、Braze ダッシュボードの**Templates & Media > Email Templates** に移動します。このテンプレートを使用して、オンブランドおよびデータ駆動型のメールをユーザーに送信できるようになりました。

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
