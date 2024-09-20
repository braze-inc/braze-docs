---
nav_title: ジャカード
article_title: ジャカード
page_order: 1
description: "この参考記事では、Braze CurrentsとConnected Contentを活用し、Webhookを通じて購読者からクリックトラッキング情報を収集する、BrazeとJacquard Dynamic Optimisationのパートナーシップについて概説している。Jacquardは、これらのイベントをあなたの言語バリアントに結びつけ、リアルタイムで言語を最適化する。"
page_type: partner
search_tag: Partner
---

# ジャカード・ダイナミック最適化

> [ジャカードは][1]、人工知能、計算言語学、顧客中心主義の精神を結集し、ブランド・ボイスに合わせてカスタマイズされたブランド・ランゲージを、大規模に、チャネルに展開することを支援する。

Jacquard Xを利用したDynamic Optimisationは、Braze CurrentsとConnected Contentを活用し、ウェブフックを通じて購読者からクリックトラッキング情報を収集する。Jacquardは、これらのイベントをあなたの言語バリアントに結びつけ、リアルタイムで言語を最適化する。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| ジャカード・アカウント | このパートナーシップを利用するには、[ジャカードのアカウントが][1]必要である。 |
| ジャカード・コネクト・サーバー・トークン | Jacquard言語にアクセスするためのBrazeキャンペーンのパスワードとなる長い文字列。<br><br>まだ提供されていない場合は、ジャカードのカスタマー・サクセス・マネージャーにリクエストすることができる。 |
| Currents | Currentsにデータをエクスポートするには、アカウントに[Braze Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)設定する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ 1:Jacquard Amazon S3の認証情報をリクエストする

クリック・トラッキング・イベントをBrazeから受け取るには、Jacquardが専用のAmazon S3バケットをセットアップする必要がある。このプロセスを開始するには、ジャカードのカスタマー・サクセス・マネージャーに連絡すること。バケットが作成されると、Currentを作成するための固有の認証情報が提供される。 

### ステップ2:電流を作る

1. Brazeで、**Currents > Create New Current > Amazon S3 Data Exportを**選択する。 
2. 次に、カレントの名前を付け、連絡先のEメールを入力する。
3. 認証情報ボックスに、Jacquard AWSのアクセスキーIDとシークレットアクセスキーを追加する。次に、AWS S3バケット名として "frasee-braze-currents-exports "を追加する。 
4. 最後に、Jacquardカスタマー・サクセス・マネージャーから受け取ったAWS S3バケット・フォルダを追加する。それはおそらくあなたの会社名だろう。
5. **General Settings "**の "Include events from anonymous users "にチェックを入れ、**"Manage Engagement Events "**の "Email Click "にチェックを入れる。
6. 終了したら、**Launch Currentを**選択する。

### ステップ 3:個人を特定できる情報（PII）の削除を要請すること。

次に、Brazeのアカウントチームに連絡し、個人を特定できる情報がJacquardに送信されないようにする。

デフォルトでは、カレントは電子メールや住所などの特定のPII属性を含む。JacquardはPIIを受け取ることはできないし、受け取ることもないので、Jacquardに渡されるすべてのイベントデータについてこれをオフにするよう、Brazeのアカウントチームにリクエストすることが重要である。

### ステップ 4:ジャカードXのコード・スニペット 

必要なコード・スニペットについては、Jacquardアカウント・チームに問い合わせること。

これらのスニペットは[コネクテッドコンテンツを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)活用し、メールに配置された後、言語とトラッキングピクセルを動的に取り込み、Jacquard Xを使ってリアルタイムで言語を最適化できる。


[1]: https://www.jacquard.com/
[3]: mailto:awesome@phrasee.co