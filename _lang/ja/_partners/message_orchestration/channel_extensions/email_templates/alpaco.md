---
nav_title: アルパコ
article_title: アルパコ
alias: /partners/Alpaco
description: "BrazeとAlpacoの統合は、Alpacoの構文を活用して、データ駆動型のEメールテンプレートを作成し、Brazeにエクスポートする。"
page_type: partner
search_tag: Partner

---

# アルパコ

> [アルパコは](https://alpaco.email/)オンラインEメールマーケティングツールで、ドラッグ＆ドロップのEメールエディターにより、デザインとアウトプットを新しいレベルでコントロールできる。BrazeとAlpacoの統合により、オンブランドでデータドリブンなEメールをBrazeにエクスポートできる。 

{% alert note %}
アルパコは[リキッド](https://shopify.github.io/liquid/)変数を[フル](https://shopify.github.io/liquid/)サポートしており、Brazeコンフィギュレーションで使用されているリキッド変数もフルサポートしている。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ------------| ----------- |
| アルパコアカウント | このパートナーシップを利用するには、アルパコのアカウントが必要だ。 |
| Braze REST API キー | 完全な**テンプレート**権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| クラスターインスタンス | Braze[クラスタインスタンスは]({{site.baseurl}}/api/basics/#endpoints)、BrazeダッシュボードとRESTエンドポイントに合わせる。<br><br> 例えば、ダッシュボードのURLが`https://dashboard-03.braze.com` の場合、エンドポイントは`dashboard-03` となる。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

Braze REST APIキーとクラスタインスタンスをアルパコのカスタマーサクセスチームに提供する。その後、チームが初期統合をセットアップする。

{% alert note %}
これは1回限りのセットアップであり、今後のエクスポートは自動的にこのAPIキーを使用する。
{% endalert %}

## アルパコのEメールをBrazeにエクスポートする

### ステップ1:アルパコでメールテンプレートを作成する

アルパコ・プラットフォームでは、さまざまな設定やオプションを使って、ブランド・アイデンティティを表現するテンプレートを作成することができる。テンプレートに満足したら**Saveを**選択する。

![アルパコクリエイト テンプレート]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### ステップ2:電子メールを作成する

テンプレートが作成されたら、ロビーに移動し、テンプレートを使ってメールを作成する。**Reviewを**選択し、すべてが正しく見えることを確認する。

![アルパコクリエイト]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### ステップ 3:Eメールを見直し、Brazeにエクスポートする

**エクスポートを**選択し、Brazeインテグレーションを選択してEメールテンプレートをBrazeにエクスポートする。 

メールテンプレートを変更したい場合は、Alpacoで変更し、再度Brazeにエクスポートする。これでBrazeのメールがあなたの変更で更新される。

![アルパコ・エクスポート Eメール]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## BrazeでAlpacoのEメールテンプレートを使う

Brazeダッシュボードの**Templates & Media > Email Templatesから**、アップロードしたアルパコメールを探す。このテンプレートを使って、ブランドやデータに基づいたメールをユーザーに送ることができる。

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
