---
nav_title: 高度なフィルター
article_title: 高度な Liquid フィルター
page_order: 4
description: "このリファレンス記事には、高度なフィルター、例、およびキャンペーンでの使用方法が一覧表示されています。"

---

# 高度なフィルター

> このリファレンス記事では、Liquidの高度なフィルターの概要と使用方法について説明します。

## エンコーディングフィルター

{% raw %}
| フィルター名 | フィルター説明 | 入力例 | 出力例 |
\|---|---|---|---|
`md5` | md5エンコードされた文字列を返します | `{{'hey' | md5}}` | 6057f13c496ecf7fd777ceb9e79ae285 |
`sha1` | sha1エンコードされた文字列を返します | `{{'hey' | sha1}}` | 7f550a9f4c44173a37664d938f1355f0f92a47a7 |
`sha2` | sha2（256 ビット、別称 SHA-256) エンコードされた文字列を返します | `{{'hey' | sha2}}` | fa690b82061edfd2852629aeba8a8977b57e40fcb77d1a7a28b26cba62591204 |
`base64` | base64エンコードされた文字列を返します | `{{'blah' | base64_encode}}` | YmxhaA== |
`hmac_sha1_hex`(旧 `hmac_sha1`） | 16 進文字列としてエンコードされた hmac-sha1 署名を返します | `{{'hey' | hmac_sha1_hex: 'secret_key'}}` | 2a3969bed25bfeefb00aca4063eb9590b4df8f0e |
`hmac_sha1_base64` | hmac-sha1署名を返し、base64文字列としてエンコードされます | `{{'hey' | hmac_sha1_base64: 'secret_key'}}` | KjlpvtJb/u+wCspAY+uVkLTfjw4= |
`hmac_sha256_hex` | hmac-sha256署名を返し、16進文字列としてエンコードされます | `{{'hey' | hmac_sha256_hex: 'secret_key'}}` | 8df897f8da3d7992fe57c8dbc6f27578cfbf2dcc4d0fbb4000b8c924841d508e |
`hmac_sha256_base64` | hmac-sha256署名を返し、base64文字列としてエンコードされます | `{{'hey' | hmac_sha256_base64: 'secret_key'}}` | jfiX+No9eZL+V8jbxvJ1eM+/LcxND7tAALjJJIQdUI4= |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## URLフィルター

| フィルター名 | フィルター 説明 | 例の入力 | 例の出力 |
|---|---|---|---|
| `url_escape` | URLで許可されていない文字列内のすべての文字を識別し、エスケープされたバリアントに置き換えます | `{{'hey<>hi' | url_escape}}` | hey%3C%3Ehi |
| `url_param_escape` | URLで許可されていない文字列のすべての文字を、アンパサンドを含むエスケープされたバリアントに置き換える。 (&) | `{{'hey<&>hi' | url_param_escape}` | hey%3C%26%3Ehi |
| `url_encode` | URL フレンドリーな文字列をエンコードします | `{{ 'google search' | url_encode }}` | google+search |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}
{% alert tip %}
`assign`タグは、複数のハイパーリンクを作成する際に時間と労力を節約するためにHTMLと組み合わせることができます。
{% raw %}
```
{% assign url = "https://www.examplelink.com" %}
<a href='{{url}}'>Shop the collection</a>
```
{% endraw %}
{% endalert %}
{% raw %}

## プロパティアクセサーフィルター

| フィルター名 | フィルター 説明 |
|---|---|---|---|
| `property_accessor` | ハッシュとハッシュキーを受け取り、そのキーでそのハッシュの値を返します |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

**ハッシュ例:**`{"a" => 42, "b" => 0}`
**入力例:**`{{hash | property_accessor: 'a'}}`
**出力例:** `42`

さらに、プロパティアクセサフィルターを使用すると、カスタム属性をテンプレート化してハッシュキーに変換し、特定のハッシュ値にアクセスできます。

{% endraw %}

{% alert note %}
Liquid 内の Braze では、ハッシュを変数 （式など） としてインスタンス化する方法はありません。
{% endalert %}

{% raw %}

## 数値フォーマットフィルター

| フィルター名 | フィルター 説明 | 例の入力 | 例の出力 |
|---|---|---|---|
| `number_with_delimiter` | コンマで数字をフォーマットします | `{{ 123456 | number_with_delimiter }}` | 123,456 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## JSONエスケープ / 文字列エスケープフィルター

| フィルター名 | フィルター 説明 |
|---|---|
| `json_escape` | 文字列内の特殊文字（ダブルクォート`""`やバックスラッシュ''など）をエスケープします。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

このフィルターは、JSON辞書で文字列をパーソナライズする際に常に使用する必要があり、特にwebhookに便利です。

## JSON フォーマットフィルター

| フィルター名 | フィルター 説明 |
|---|---|
| `json_parse` | JSON 文字列を、オブジェクトや配列などの対応するデータ構造に変換します。 | 
| `as_json_string` | オブジェクトや配列などのデータ構造を対応する JSON 文字列に変換します。 | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

{% details json_parse example input and output %}

### インプット 

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
```

### 出力

```liquid
{% for item in my_data %}
Item ID: {{ item.id }}
Item Name: {{ item.store_name }}
{% endfor %}
```
{% endraw %}

{% enddetails %}

{% details as_json_string example input and output %}

### インプット

{% raw %}
```liquid
{% assign my_data_string = '[{"id":"1","store_name":"demo-store"}]'  %}
{% assign my_data = my_data_string | json_parse %}
{% assign json_string = my_data | as_json_string %}
```

### 出力

```liquid
{{json_string}}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values
