---
nav_title: 詳細フィルタ
article_title: 高度な液体フィルター
page_order: 4
description: "このリファレンス記事には、高度なフィルタ、例、およびキャンペーンでの使用方法が記載されています。"

---

# 詳細フィルタ

## フィルタのエンコード

{% raw %}
| filter name | filter description | example input | example 出力 |
|---|---|---|---|
`md5` | md5 エンコードされた文字列を返します| `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
`sha1` | sha1 エンコードされた文字列| `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
`sha2` | sha2 (256 ビット、SHA-256 とも呼ばれます) エンコードされた文字列| `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba897b57e40fcb7d1a7a28b26cba62591204 |
`base64` | base64 エンコードされた文字列を返します| `{{'blah' | base64_encode}}` | YmxhaA== |
`hmac_sha1_hex` (以前の`hmac_sha1`) | hmac-sha1 シグネチャを返します。16 進文字列としてエンコードされます| `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |
`hmac_sha1_base64` | base64 文字列としてエンコードされたhmac-sha1 シグネチャを返します| `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= |
`hmac_sha256_hex` | 16 進文字列としてエンコードされたhmac-sha256 シグネチャを返します| `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fb4000b8c924841d508e |
`hmac_sha256_base64` | base64 文字列としてエンコードされたhmac-sha256 シグネチャを返します| `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxNDAALjJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## URLフィルタ

| filter name | filter description | example input | example 出力 |
|---|---|---|---|
| `url_escape` | URLS で許可されていない文字列内のすべての文字を識別し、その文字をエスケープされたバリアント| `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | URL で許可されていない文字列のすべての文字を、アンパサンド(&) | `{{'hey<&>hi' | url_param_escape}` | hey%3C%26%3Ehi |
| `url_encode` | URLフレンドリな文字列をエンコードする| `{{ 'google search' | url_encode }}` | google+search |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endraw %}
{% alert tip %}
`assign` タグをHTML と組み合わせると、複数のハイパーリンクを作成する際の時間と労力を節約できます。
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## プロパティアクセサフィルタ

| フィルタ名| フィルタの説明|
|---|---|---|---|
| `property_accessor` | ハッシュキーとハッシュキーを取り、そのキーのハッシュの値を返します|
{: .reset-td-br-1 .reset-td-br-2}

**ハッシュの例:**`{"a" => 42, "b" => 0}`
**入力例:**`{{hash | property_accessor: 'a'}}`
**出力例:** `42`

さらに、プロパティアクセサフィルタを使用すると、カスタム属性をハッシュキーにテンプレート化して特定のハッシュ値にアクセスできます。

{% endraw %}

{% alert note %}
Braze 内のLiquid では、ハッシュを変数(式など) としてインスタンス化する方法はありません。
{% endalert %}

{% raw %}

## 数値書式フィルタ

| filter name | filter description | example input | example 出力 |
|---|---|---|---|
| `number_with_delimiter` | カンマで数値をフォーマット| `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## JSON エスケープ/文字列エスケープフィルタ

| フィルタ名| フィルタの説明|
|---|---|---|---|
| `json_escape` | 文字列の特殊文字をエスケープします(二重引用符`""` やバックスラッシュ'\\' など)。|
{: .reset-td-br-1 .reset-td-br-2}

このフィルタは、JSON ディクショナリの文字列をパーソナライズする場合に常に使用する必要があり、特にWebhook に役立ちます。
{% endraw %}


[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:#accounting-for-null-attribute-values
