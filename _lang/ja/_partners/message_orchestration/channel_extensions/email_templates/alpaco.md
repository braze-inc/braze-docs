---
nav_title: アルパコ
article_title: アルパコ
alias: /partners/Alpaco
description: "BrazeとAlpacoの統合は、Alpacoの構文を活用してデータ駆動型Eメールテンプレートを作成し、Brazeにエクスポートします。"
page_type: partner
search_tag: Partner

---

# アルパコ

> [Alpaco](https://alpaco.email/)は、ドラッグ＆ドロップでデザインと出力をワンランク上のレベルでコントロールできるEメールエディターを提供するオンラインEメールマーケティングツールです。BrazeとAlpacoの統合により、オンブランドとデータドリブンのメールをBrazeにエクスポートできます。 

{% alert note %}
Alpacoは[完全なLiquid](https://shopify.github.io/liquid/)変数をサポートしているため、Braze構成で使用されるあらゆるLiquid変数も完全にサポートしています。
{% endalert %}

## 前提条件

| 要件 | 説明 |

|アルパコアカウント|この提携を利用するにはアルパコアカウントが必要です。|
| Braze REST APIキー | **Templates**のフル権限を持つBraze REST APIキー。<br><br> これは**、設定**>**APIキー**からBrazeダッシュボードで作成できます。|
| Cluster instance | Brazeの[クラスタインスタンスは]({{site.baseurl}}/api/basics/#endpoints)、BrazeのダッシュボードとRESTエンドポイントに合わせます。<br><br> たとえば、ダッシュボードのURLが`https://dashboard-03.braze.com`の場合、エンドポイントは`dashboard-03`になります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

Braze REST APIキーとクラスタインスタンスをAlpacoカスタマーサクセスチームに提供します。その後、チームが初期インテグレーションをセットアップします。

{% alert note %}
これは1回限りの設定で、今後エクスポートする場合は自動的にこのAPIキーが使用されます。
{% endalert %}

## BrazeへのAlpacoメールのエクスポート

### ステップ1: Alpacoでメールテンプレートを作成する

Alpacoプラットフォームでは、さまざまな設定とオプションを使用して、ブランドアイデンティティを表現するテンプレートを作成します。テンプレートに問題がなければ**[保存]**を選択します。

![Alpaco Create template]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### ステップ2: メールを作成する

テンプレートを作成したら、ロビーに移動してテンプレート付きのメールを作成します。[**確認]を**選択し、すべてが正しく表示されていることを確認します。

![Alpaco Create email]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### ステップ 3 Brazeへのメールの確認とエクスポート

[**エクスポート]**を選択し、Braze統合を選択してメールテンプレートをBrazeにエクスポートします。 

メールテンプレートを変更する場合は、Alpacoで変更を行った後、再度Brazeにメールをエクスポートします。これにより、Braze内のメールが変更内容で更新されます。

![Alpaco Export email]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## BrazeでAlpacoのメールテンプレートを使用する

Brazeダッシュボードの[**テンプレートとメディア**]>[電子メールテンプレート]に移動して、アップロードしたAlpacoの電子メールを見つけます。このテンプレートを使用して、オンブランドおよびデータ駆動型のEメールをユーザーに送信できるようになりました。

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
