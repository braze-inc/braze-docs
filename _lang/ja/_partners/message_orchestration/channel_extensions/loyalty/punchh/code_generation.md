---
nav_title: Dynamic Code Generation
article_title:Punchh ダイナミックなコード生成
page_order:2
description:"この参考記事では、BrazeにおけるPunchhのダイナミックなコード生成の使い方を概説している。"
page_type: partner
search_tag:Partner
---

# ダイナミックなコード生成

> クーポンコードは、一人のユーザーが使用できるユニークなコードである（一回使用でも複数回使用でも）。Punchhフレームワークはクーポンコードを生成し、モバイルアプリ内やPOSシステムで処理することができる。

Punchhクーポン・フレームワークとBrazeを使えば、以下のようなシナリオが実現できる：

- ゲストがメール内のクーポン生成リンクをクリックすると、クーポンコードを生成する：クーポンコードはダイナミックな形で生成され、Webページに表示される。
- ゲストがメールを開封したときにクーポンコードを生成する：クーポンコードはダイナミックな方法で生成され、メール内に画像, 写真として表示される。

## Punchhのダイナミックなクーポンコード生成を統合する方法

### ステップ1:Punchhでクーポンキャンペーンを作成する

1. Punchhクーポンキャンペーンを使い、以下の画像, 写真のようにダイナミックなクーポンキャンペーンを作成する。
2. Punchhクーポン・フレームワークは、ダイナミックなクーポン生成を可能にするために、以下のパラメーターを生成する：
    - ダイナミックなクーポン生成トークン：これは、暗号化のためにシステムが生成したセキュリティ・トークンである。
    - ダイナミックなクーポン生成URL：このURLは、ビジネスの要求に応じて、リンクまたは画像写真としてメールに埋め込まれる。

![Punchhでクーポン・キャンペーンを作成するためのフォームである。][2]{: style="max-width:60%;"}

### ステップ2:署名を生成し、URLを構築する

JWT.IOライブラリーは、JSON Webトークンをデコード、検証、生成する。これは、2者間で主張を安全に表現するための、開封された業界標準のRFC 7519方式である。 

ゲストとクーポンの一意性を確保するために、以下の`ClaimType` ：

- `email`ユーザーのメールアドレスを表す。 
- `campaign_id`これはシステムが生成したパンチキャンペーンIDを表す。 
- `first_name`ユーザーの名。 
- `last_name`ユーザーの姓をキャプチャする。

PunchhのダイナミックなクーポンコードAPIを使用するには、JWTトークンを構築する必要がある。ダッシュボードの使用したいチャネルのメッセージ本文に、以下のLiquidテンプレートを追加する：

{% raw %}
```liquid
{% capture header %}{"alg":"HS256","typ":"JWT"}{% endcapture %}

{% capture payload %}{"campaign_id":"CAMPAIGN_ID","email":"{{${email_address}}}","first_name":"{{${first_name}}}","last_name":"{{${last_name}}}"}{% endcapture %}

{% capture signature_structure %}{{header | base64_encode}}.{{payload | base64_encode | remove: '='}}{% endcapture %}

{% assign secret = "DYNAMIC_COUPON_GENERATION_TOKEN" %}

{% assign final_signature = {{signature_structure | hmac_sha256_base64: secret}} %}

{% capture jwt %}{{signature_structure}}.{{final_signature | remove: '='}}{% endcapture %}

```
{% endraw %}

次のように置き換えます。

| placeholder        | 説明                                          |
|--------------------|------------------------------------------------------|
| `SERVER_NAME`                     | サーバー名。              |
| `DYNAMIC_COUPON_GENERATION_TOKEN` | ダイナミックなクーポン生成トークン。 |
| `CAMPAIGN_ID`                     | キャンペーンID。                     |

### ステップ3:メッセージ本文にクーポンコードを追加する

#### PunchhのWebページへのリンク

PuncchがホストするWebページにリンクするには、メッセージ本文に以下のスニペットを追加する。

{% raw %}
```liquid
https://SERVER_NAME.punchh.com/request_coupons/DYNAMIC_COUPON_GENERATION_TOKEN?sign={{jwt}}
```
{% endraw %}

次のように置き換えます。

| placeholder        | 説明                                          |
|--------------------|------------------------------------------------------|
| `SERVER_NAME`                     | サーバー名。              |
| `DYNAMIC_COUPON_GENERATION_TOKEN` | ダイナミックなクーポン生成トークン。 |

ユーザーがクーポンのURLをクリックすると、PunchがホストするWebページにリダイレクトされ、そこで生成されたクーポンが表示される。

![ユーザーがクーポンコードの生成に成功した後の確認メッセージの例。][1]

#### JSON経由でコードをプレーンテキストとして取り出す

JSONレスポンスを返すには、以下のスニペットのように、Punchh URLのsignクエリーパラメーターの前に`.json` を追加する：

{% raw %}
```liquid
https://SERVER_NAME.punchh.com/request_coupons/DYNAMIC_COUPON_GENERATION_TOKEN.json?sign={{jwt}}
```
{% endraw %}

次のように置き換えます。

| placeholder        | 説明                                          |
|--------------------|------------------------------------------------------|
| `SERVER_NAME`                     | サーバー名。              |
| `DYNAMIC_COUPON_GENERATION_TOKEN` | ダイナミックなクーポン生成トークン。 |

[コネクテッド・コンテンツを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)活用すれば、コードをプレーンテキストとしてメッセージ本文に挿入することができる。以下に例を示します。

{% raw %}
```liquid
{% connected_content https://SERVER_NAME.punchh.com/request_coupons/DYNAMIC_COUPON_GENERATION_TOKEN.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
```
{% endraw %}

#### メールコンテンツ内に画像、写真をリンクする

画像, 写真の中にクーポンコードをリンクするには、メッセージ本文に以下のスニペットを追加する：

{% raw %}
```liquid
<img src="https://SERVER_NAME.punchh.com/request_coupons/DYNAMIC_COUPON_GENERATION_TOKEN.png?sign={{jwt}}">`
```
{% endraw %}

次のように置き換えます。

| placeholder        | 説明                                          |
|--------------------|------------------------------------------------------|
| `SERVER_NAME`                     | サーバー名。              |
| `DYNAMIC_COUPON_GENERATION_TOKEN` | ダイナミックなクーポン生成トークン。 |

出力は以下のようになる：

![クーポンコード画像タグのレンダリング出力。][3]

## 関連するエラーメッセージ

| エラーコード | エラーメッセージ | 説明 |
| --- | --- | --- |
| `coupon_code_expired` | このプロモーションコードの有効期限は切れている。 | コードは設定された有効期限後に使用される。 |
| `coupon_code_success` | おめでとう、プロモコードは正常に適用された。 | コードは正常に使用されている。 |
| `coupon_code_error` | 有効なプロモコードを入力する | 使用されたコードは無効である。 |
| `coupon_code_type_error` | クーポンの種類が正しくない。このクーポンは`%{coupon_type}` でのみ利用できる。 | POSで使用するはずのコードをモバイルアプリで使用すると、このエラーが発生する。 |
| `usage_exceeded` | 本クーポンコードのキャンペーンは終了した。次回はぜひ挑戦してほしい。 | コードの使用量が、使用を許可されたユーザー数を超えている。例えば、ダッシュボードのコンフィギュレーションが3,000人のユーザーによるコードの使用を許可しており、ユーザー数が3,000人を超えた場合、このエラーが発生する。 |
| `usage_exceeded_by_guest` | このプロモコードはすでに処理されている。 | ユーザーによるコードの使用は、ユーザーが使用できる回数を超えている。例えば、ダッシュボードの設定では、1つのコードをユーザーが3回使用することができる。それ以上使用すると、このエラーが発生する。 |
| `already_used_by_other_guest` | このプロモコードはすでに他のゲストによって使用されている。 | 別のユーザーがすでにコードを使用している。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[1]: {% image_buster /assets/img/punchh/punchh7.png %}
[2]: {% image_buster /assets/img/punchh/punchh8.png %}
[3]: {% image_buster /assets/img/punchh/punchh9.png %}
