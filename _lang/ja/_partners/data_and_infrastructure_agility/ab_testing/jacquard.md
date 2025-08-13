---
nav_title: Jacquard
article_title: Jacquard
page_order: 1
description: "この参考記事では、Braze CurrentsとConnected Contentを活用し、Webhookを通じて購読者からクリックトラッキング情報を収集する、BrazeとJacquard Dynamic Optimisationのパートナーシップについて概説している。Jacquard は、これらのイベントを言語バリアントに関連付けて、リアルタイムで言語を最適化します。"
page_type: partner
search_tag: Partner
---

# Jacquard のダイナミック最適化

> [Jacquard][1] は、人工知能、計算言語学、そして顧客中心の精神を融合し、ブランドボイスに合わせてカスタマイズされたチャネルにわたり、ブランドのメッセージを大規模に展開できるようにします。

Jacquard Xを利用したDynamic Optimisationは、Braze CurrentsとConnected Contentを活用し、ウェブフックを通じて購読者からクリックトラッキング情報を収集する。Jacquard は、これらのイベントを言語バリアントに関連付けて、リアルタイムで言語を最適化します。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Jacquard アカウント | このパートナーシップを活用するには、[Jacquard アカウント][1]が必要です。 |
| Jacquard 接続サーバートークン | Jacquard 言語にアクセスするための、Braze キャンペーンのパスワードとして機能する長い文字列。<br><br>このトークンがまだ提供されていない場合は、Jacquard カスタマーサクセスマネージャーにリクエストできます。 |
| Currents | Currents にデータを再度エクスポートするには、アカウントに [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:Jacquard Amazon S3の認証情報をリクエストする

クリック・トラッキング・イベントをBrazeから受け取るには、Jacquardが専用のAmazon S3バケットをセットアップする必要がある。このプロセスを開始するには、Jacquard カスタマーサクセスマネージャーに連絡してください。バケットが作成されると、Current を作成するための一意の認証情報が提供されます。 

### ステップ2:Current を作成する

1. Braze で、**[Currents] > [新しい Currents を作成] > [Amazon S3 データのエクスポート]** を選択します。 
2. 次に Current に名前を付け、連絡先メールを入力します。
3. 認証情報ボックスに、Jacquard AWS アクセスキー ID とシークレットアクセスキーを追加します。次に、AWS S3バケット名として "frasee-braze-currents-exports "を追加する。 
4. 最後に、Jacquard カスタマーサクセスマネージャーから受け取った AWS S3バケットフォルダーを追加します。これはお客様の社名である可能性があります。
5. [**一般設定**] の [匿名ユーザーのイベントを含める] ボックスをオンにし、[**エンゲージイベントの管理**] で [メールクリック] をオンにします。
6. 終了したら、[**Currents を起動**] を選択します。

### ステップ3:個人を特定できる情報（PII）の削除を要請すること。

次に、Braze アカウントチームに連絡し、個人を特定できる情報が Jacquard に送信されないようにします。

デフォルトでは、Current にはメールや住所などの特定の PII 属性が含まれます。JacquardはPIIを受け取ることはできないし、受け取ることもないので、Jacquardに渡されるすべてのイベントデータについてこれをオフにするよう、Brazeのアカウントチームにリクエストすることが重要である。

### ステップ4:Jacquard X コードスニペット 

必要なコードスニペットについては、Jacquard アカウントチームにお問い合わせください。

これらのスニペットは[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)を利用しており、メールに配置されると、言語とトラッキングピクセルをダイナミックに取得します。これにより、Jacquard は Jacquard X を使用してリアルタイムで言語を最適化できます。


[1]: https://www.jacquard.com/
[3]: mailto:awesome@phrasee.co