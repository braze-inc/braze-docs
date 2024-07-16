---
nav_title: Phrasee React
article_title:Phraseeリアクト
page_order:2
description:"この参考記事では、Braze Currentsとコネクテッドコンテンツを活用し、Webhook経由でサブスクライバーからクリック追跡情報を収集するBrazeとPhrasee Reactのパートナーシップについて概説している。Phraseeは、これらのイベントをバリアントに結びつけ、リアルタイムで言語を最適化する。"
page_type: partner
search_tag:Partner

---

# Phraseeリアクト

> [Phraseeは][1]、人工知能、計算言語学、顧客中心主義の精神を結集し、ブランド・ボイスに合わせてカスタマイズされたブランド・ランゲージを、大規模に、チャネルに展開することを支援する。

Phrasee Xを搭載したPhrasee Reactは、Braze Currentsとコネクテッドコンテンツを活用し、サブスクライバーからWebhook経由でクリック追跡情報を収集する。Phraseeは、これらのイベントをあなたのバリアントに結びつけ、リアルタイムで言語を最適化する。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Phraseeアカウント | このパートナーシップを利用するには、[Phraseeアカウントが][3]必要である。 |
| Phrasee コネクトサーバートークン | BrazeキャンペーンでPhrasee言語にアクセスするためのパスワードとなる長い文字列。<br><br>まだ提供されていない場合は、カスタマー・サクセス・マネージャーにリクエストすることができる。 |
| Currents | Currentsにデータをエクスポートするには、アカウントに[Braze Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)設定する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:Amazon S3の認証情報をリクエストする

Brazeからクリック追跡イベントを受け取るには、専用のAmazon S3バケットを設定するPhraseeが必要だ。このプロセスを開始するには、カスタマーサクセスマネージャーに連絡する。バケットが作成されると、Currentsを作成するための固有の認証情報が提供される。 

### ステップ2:カレントを作成する

1. Brazeで、**Currents > Create New Currents > Amazon S3 Data Exportを**クリックする。 
2. 次に、Currentsに名前を付け、連絡先メールを入力する。
3. 認証情報ボックスに、AWSアクセスキーIDとシークレットアクセスキーを追加する。次に、AWS S3バケット名として "Phrasee-Braze-currents-exports "を追加する。 
4. 最後に、カスタマーサクセスマネージャーから受け取ったAWS S3バケットフォルダを追加する。それはおそらくあなたの会社名だろう。
5. **一般設定**」の「匿名ユーザーからのイベントを含める」にチェックを入れ、「**エンゲージメントイベントの管理**」の「メールクリック」にチェックを入れる。
6. 終了したら、**Launch Currentsを**クリックする。

### ステップ3:パーソナライズされた情報（PII）の削除を要求する。

次に、Brazeアカウントチームに連絡し、パーソナライズされた情報がPhraseeに送信されないようにする。

デフォルトでは、Currentsはメールや住所などの特定のPII属性を含む。PhraseeはPIIを受け取ることはできないし、受け取ることもないので、Brazeのアカウントチームに、Phraseeに渡されるイベントデータについてこれをオフにするようリクエストすることが重要である。

### ステップ 4:Phrasee Xのコードスニペット 

必要なコードスニペットについては、Phraseeアカウントチームに問い合わせること。

これらのスニペットは[コネクテッドコンテンツを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)活用し、メールに配置された後、ダイナミックな言語とトラッキングピクセルを取り込み、PhraseeはPhrasee Xを使ってリアルタイムで言語を最適化することができる。


[1]: https://phrasee.co/
[3]: mailto:awesome@phrasee.co