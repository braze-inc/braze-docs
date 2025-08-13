---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "Braze と Alpaco の統合では、Alpaco の構文を使用して、データドリブン型のメールテンプレートを作成して Braze にエクスポートします。"
page_type: partner
search_tag: Partner

---

# Alpaco

> [Alpaco](https://alpaco.email/) は、ドラッグ＆ドロップメールエディターを備えたオンラインメールマーケティングツールであり、デザインと出力をこれまでにない方法でコントロールできます。Braze と Alpaco の統合では、データドリブン型でブランドらしさのあるメールテンプレートを作成して Braze にエクスポートできます。 

_この統合は Alpaco によって管理されます。_

{% alert note %}
Alpaco は[完全な Liquid](https://shopify.github.io/liquid/) 変数をサポートしています。このため、Braze 設定で使用されるすべての Liquid 変数を完全にサポートしています。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ------------| ----------- |
| Alpaco アカウント | このパートナーシップを活用するには、Alpaco アカウントが必要です。 |
| Braze REST API キー | 完全な**テンプレート**権限を持つBraze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| クラスタインスタンス | Braze [クラスターインスタンス]({{site.baseurl}}/api/basics/#endpoints)は、Braze ダッシュボードと REST エンドポイントに対応しています。<br><br> 例えば、ダッシュボードのURLが`https://dashboard-03.braze.com` の場合、エンドポイントは`dashboard-03` となる。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合

Braze REST API キーとクラスターインスタンスを Alpaco カスタマーサクセスチームに提供します。その後、このチームが初期統合を設定できます。

{% alert note %}
これは1回限りのセットアップであり、今後のエクスポートは自動的にこのAPIキーを使用する。
{% endalert %}

## Alpaco のメールを Braze にエクスポートする

### ステップ1:Alpaco でメールテンプレートを作成する

Alpaco プラットフォームでは、さまざまな設定やオプションを使用して、ブランドアイデンティティを表現するテンプレートを作成できます。テンプレートに満足したら [**Save**] を選択します。

![Alpaco でのテンプレートの作成]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### ステップ2:電子メールを作成する

テンプレートが作成されたら、ロビーに移動し、テンプレートを使ってメールを作成する。[**Review**] を選択して、すべてが適切に表示されていることを確認します。

![Alpaco でのメールの作成]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### ステップ3:Eメールを見直し、Brazeにエクスポートする

[**Export**] を選択し、Braze 統合を選択して、メールテンプレートを Braze にエクスポートします。 

メールテンプレートに変更を加える場合は、Alpaco でそれらの変更を行ってから、メールテンプレートを再び Braze にエクスポートします。これでBrazeのメールがあなたの変更で更新される。

![Alpaco メールのエクスポート]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## BrazeでAlpacoのEメールテンプレートを使う

Braze ダッシュボードで **[テンプレートとメディア] > [メールテンプレート]** に移動して、アップロードした Alpaco メールを見つけます。このテンプレートを使用して、ブランドらしさのあるデータドリブン型のメールをユーザーに送信できます。


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
