---
nav_title: "取得:カスタム属性をエクスポートする"
article_title: "取得:カスタム属性をエクスポートする"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、BrazeのExport custom attributesエンドポイントの詳細について概説する。"

---
{% api %}
# カスタム属性をエクスポートする
{% apimethod get %}
/custom_attributes
{% endapimethod %}

> アプリに記録されたカスタム属性のリストをエクスポートするには、このエンドポイントを使用する。属性は50のグループに分けられ、アルファベット順にソートされて返される。

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`custom_attributes.get`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='custom_attributes' %}

## クエリーパラメーター

このエンドポイントへの各コールにより、50の属性が返されます。50を超える属性については、次のレスポンス例に示すように、`Link` ヘッダーを使用して次のページのデータを取得します。

| パラメータ | required | データ型 | 説明 |
|---|---|---|---|
| `cursor` | オプション | 文字列 | カスタム属性のページネーションを決定する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 例のリクエスト

### カーソルなし

```
curl --location --request GET 'https://rest.iad-01.braze.com/custom_attributes' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

### カーソル付き

```
curl --location --request GET 'https://rest.iad-03.braze.com/custom_attributes?cursor=c2tpcDow' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 応答

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "attributes" : [
        {
            "array_length": 100, (number) the maximum array length, or null if not applicable,
            "data_type": "Number", (string) the data type,
            "description": "The attribute description", (string) the attribute description,
            "name": "The attribute name", (string) the attribute name,
            "status": "Active", (string) the attribute status,
            "tag_names": ["Tag One", "Tag Two"] (array) the tag names associated with the attribute formatted as strings,
        },
        ...
    ]
}
```

### 致命的なエラーの応答コード {#fatal-export}

リクエストが致命的なエラーに遭遇した場合に返されるステータスコードと関連するエラーメッセージについては、[致命的なエラー]({{site.baseurl}}/api/errors/#fatal-errors)を参照してください。

{% alert tip %}
CSV および API のエクスポートに関するヘルプについては、「[エクスポートのトラブルシューティング]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/)」を参照してください。
{% endalert %}

{% endapi %}
