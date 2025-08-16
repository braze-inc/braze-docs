---
nav_title: 5月
page_order: 8
noindex: true
page_type: update
description: "この記事には2020年5月のリリースノートが含まれている。"
---
# 2020年5月

## Google Tag Manager

[Google Tag Managerを]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)使用したBrazeのAndroid SDKのデプロイと管理方法に関するドキュメントと例を追加。

## 新しいブラックリスト電子メールAPIエンドポイント

Braze API経由でメールアドレスを[ブラックリスト化]({{site.baseurl}}/api/endpoints/email/post_blacklist/)できるようになった。メールアドレスをブラックリストに登録すると、そのユーザーはメールの配信を停止され、ハードバウンスされたことになる。

## Braze APIエンドポイントのAPIキー変更

2020年5月より、BrazeはAPIキーの読み取り方法をより安全なものに変更した。これで API キーがリクエストヘッダーとして渡されるはずです。[**リクエスト例**] の下の個々のエンドポイントページや、[**API キーの説明**] で例を確認できます。

Braze は、リクエストボディとURL パラメータに渡される`api_key` を引き続きサポートしますが、最終的にはサンセット(TBD) になります。**API コールを適宜更新します。**これらの変更は[Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro)内で更新された。
{% details API キーの説明 %}
{% tabs %}
{% tab GET Request %}
この例では、`/email/hard_bounces` エンドポイントを使用している。

**前:リクエスト本文のAPI キー**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key={YOUR_REST_API_KEY}&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
```
**現在: ヘッダーのAPIキー**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endtab %}
{% tab POST Request %}
この例では、`/user/track` エンドポイントを使用している。

**前:リクエスト本文のAPI キー**
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
**現在: ヘッダーのAPIキー**
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


