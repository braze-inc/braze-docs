---
nav_title: ダイナミック・コード生成
article_title: パンチ・ダイナミック・コード生成
page_order: 2
description: "このリファレンス記事では、BrazeにおけるPunchh動的コード生成の使い方を概説している。"
page_type: partner
search_tag: Partner
---

# Punchhによる動的コード生成

> クーポンコードとは、一人のユーザーが使用できるユニークなコードである（一回使用でも複数回使用でも）。Punchhフレームワークはクーポンコードを生成し、モバイルアプリ内やPOSシステムで処理することができる。

Punchhクーポン・フレームワークとBrazeを使えば、以下のようなシナリオが実現できる：

- ゲストがメール内のクーポン生成リンクをクリックすると、クーポンコードを生成する：クーポンコードは動的に生成され、ウェブページに表示される。
- ゲストがメールを開いたときにクーポンコードを生成する：クーポンコードは動的に生成され、メール内に画像として表示される。

## 動的なクーポンコード生成を統合する

### ステップ 1:クーポン・キャンペーンを作成する

1. Punchh クーポン・キャンペーンを使って、以下の画像のようにダイナミック・ジェネレーション・クーポン・キャンペーンを作成する。
2. Punchhクーポン・フレームワークは、ダイナミックなクーポン生成を可能にするために、以下のパラメーターを生成する：
    - 動的クーポン生成トークン：これは、暗号化のためにシステムが生成したセキュリティ・トークンである。
    - 動的クーポン生成URL：このURLは、ビジネスの要求に応じて、リンクまたは画像としてメールに埋め込まれる。

![]({% image_buster /assets/img/punchh/punchh8.png %}){: style="max-width:60%;"}

### ステップ2:署名を生成し、URLを構築する

JWT.IO ライブラリは、JSONウェブトークンをデコード、検証、生成する。これは、2つの当事者間でクレームを安全に表現するための、オープンで業界標準のRFC 7519方式である。 

ゲストとクーポンの一意性を確保するために、以下の`ClaimType` ：

- `campaign_id`これはシステムが生成したパンチキャンペーンIDを表す。
- `email`ユーザーのメールアドレスを表す。 
- `first_name`ユーザーのファーストネームをキャプチャする。 
- `last_name`ユーザーの姓をキャプチャする。

Punchhのダイナミック・クーポン・コードAPIを使用するには、JWTトークンを構築する必要がある。Brazeダッシュボードの使用したいチャンネルのメッセージ本文に、以下のLiquidテンプレートを追加する：

{% raw %}
```liquid
{% assign header = '{"alg":"HS256","typ":"JWT"}' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% capture payload_raw %}

{
  "campaign_id": "CAMPAIGN_ID",
  "email": "{{${email_address}}}",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}"
}

{% endcapture %}

{% assign payload = payload_raw | replace: ' ', '' | replace: '\n', '' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign unsigned_token = header | append: "." | append: payload %}

{% assign secret = "DYNAMIC_COUPON_GENERATION_TOKEN" %}

{% assign signature_raw = unsigned_token | hmac_sha256_base64: secret %}

{% assign signature = signature_raw | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign jwt = unsigned_token | append: "." | append: signature %}

```
{% endraw %}


次のように置き換えます。

| placeholder        | 説明                                          |
|--------------------|------------------------------------------------------|
| `DYNAMIC_COUPON_GENERATION_TOKEN` | 動的クーポン生成トークン。 |
| `CAMPAIGN_ID`                     | キャンペーンID                     |

### ステップ3:クーポンコードをメッセージ本文に追加する

#### パンチ・ウェブページへのリンク

Puncchがホストするウェブページにリンクするには、[先ほど作成した](#step-1-create-a-coupon-campaign-in-punchh)動的生成URLに`{% raw %}{{jwt}}{% endraw %}` 。リンクは以下のようなものであるべきだ： 

{% raw %}
```
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX?sign={{jwt}}
```
{% endraw %}

ユーザーがクーポンのURLをクリックすると、Punchがホストするウェブページにリダイレクトされ、そこで生成されたクーポンが表示される。

![]({% image_buster /assets/img/punchh/punchh7.png %}) ユーザーがクーポンコードの生成に成功した後の確認メッセージの例。

#### JSON経由でコードをプレーンテキストとして抽出する

JSONレスポンスを返すには、[先ほど作成した](#step-1-create-a-coupon-campaign-in-punchh)動的生成URLに`{% raw %}{{jwt}}{% endraw %}` 、URL文字列のトークンの後に`.json` 。リンクは以下のようなものであるべきだ：

{% raw %}
```liquid
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}}
```
{% endraw %}

その後、[Connected Contentを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)活用して、コードをプレーンテキストとしてメッセージ本文に挿入することができる。以下に例を示します。

{% raw %}
```liquid
{% connected_content https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
````
{% endraw %}

#### メールコンテンツ内に画像をリンクする

クーポンコードを画像内にリンクする：

1. [先ほど作成した](#step-1-create-a-coupon-campaign-in-punchh)動的生成URLに`{% raw %}{{jwt}}{% endraw %}` を追加する。
2. URL文字列のトークンの後に`.png` 。
3. リンクをHTML{% raw %}`<img>`{% endraw %} タグに埋め込む。

{% tabs ローカル %}
{% tab 入力例 %}
{% raw %}
```liquid
<img src="https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.png?sign={{jwt}}">
````
{% endraw %}
{% endtab %}

{% tab 出力例 %}
![クーポンコード画像タグのレンダリング出力]({% image_buster /assets/img/punchh/punchh9.png %})
{% endtab %}
{% endtabs %}

## エラーメッセージ

| エラーコード | エラーメッセージ | 説明 |
| --- | --- | --- |
| `coupon_code_expired` | このプロモーションコードの有効期限は切れている | コードは設定された有効期限後に使用される。 |
| `coupon_code_success` | おめでとう、プロモコードは正常に適用された。 | コードは正常に使用されている。 |
| `coupon_code_error` | 有効なプロモーションコードを入力する | 使用されたコードは無効である。 |
| `coupon_code_type_error` | クーポンの種類が正しくない。このクーポンは`%{coupon_type}` でのみ利用できる。 | POSで使用するはずのコードをモバイルアプリで使用すると、このエラーが発生する。 |
| `usage_exceeded` | 本クーポンコードのキャンペーンは終了した。次回はぜひ挑戦してほしい。 | コードの使用量が、使用を許可されたユーザー数を超えている。例えば、ダッシュボードのコンフィギュレーションが3,000人のユーザーによるコードの使用を許可しており、ユーザー数が3,000人を超えた場合、このエラーが発生する。 |
| `usage_exceeded_by_guest` | このプロモコードはすでに処理されている。 | ユーザーによるコードの使用は、ユーザーが使用できる回数を超えている。例えば、ダッシュボードの設定では、1つのコードをユーザーが3回使用することができる。それ以上使用すると、このエラーが発生する。 |
| `already_used_by_other_guest` | このプロモコードはすでに他のゲストが使用している。 | 別のユーザーがすでにこのコードを使用している。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
