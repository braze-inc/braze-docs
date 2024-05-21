---
nav_title: 5月
page_order: 8
noindex: true
page_type: update
description: "この記事には、2020 年 5 月のリリース ノートが含まれています。"
---
# 2020年5月

## Google タグ マネージャー

[Google タグ マネージャー]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/android_google_tag_manager/)を使用して Braze の Android SDK をデプロイおよび管理する方法についてのドキュメントと例を追加しました。

## 新しいブラックリストメールAPIエンドポイント

Braze API 経由で電子メール アドレスを [ブラックリストに登録]({{site.baseurl}}/api/endpoints/email/post_blacklist/) できるようになりました。電子メール アドレスをブラックリストに登録すると、そのユーザーは電子メールの購読を解除され、ハード バウンスとしてマークされます。

## Braze API エンドポイントの API キーの変更

2020 年 5 月現在、Braze はセキュリティを強化するために API キーの読み取り方法を変更しました。ここで、API キーをリクエスト ヘッダーとして渡す必要があります。例は、個々のエンドポイント ページの **「サンプル リクエスト**」および **「API キーの説明**」に記載されています。

Brazeは今後もサポートを続けていきます `api_key` リクエスト本文と URL パラメータを通じて渡されますが、最終的には廃止される予定です (TBD)。**それに応じて API 呼び出しを更新します。**これらの変更は [Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro)内で更新されました。
{% details API Key Explanation %}
{% tabs %}
{% tab GET Request %}
この例では、 `/email/hard_bounces` 終点。

**前に：リクエスト本文の API キー**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key={YOUR_REST_API_KEY}&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
```
**今：ヘッダーの API キー**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endtab %}
{% tab POST Request %}
この例では、 `/user/track` 終点。

**前に：リクエスト本文の API キー**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key": YOUR-API-KEY-HERE ,
	"attributes": [ 
 	{
 	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
**今：ヘッダーの API キー**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
	"attributes": [ 
 	{
	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
{% endtab %}
{% endtabs %}
{% enddetails %}


