---
nav_title: "POST:メディアライブラリーにアセットをアップロードする"
article_title: "POST:メディアライブラリーにアセットをアップロードする"
search_tag: エンドポイント
page_order: 1

layout: api_page
page_type: reference
description: "この記事は`POST /media_library/create`エンドポイントの詳細を説明する。"
---

{% api %}
# メディアライブラリーにアセットをアップロードする
{% apimethod post %}
/media_library/create
{% endapimethod %}

> このエンドポイントを使用すると、外部でホストされているURL（`asset_url`）またはリクエスト本文で送信されたバイナリファイルデータ（`asset_file`）のいずれかを使用して、[Brazeメディアライブラリー](https://www.braze.com/docs/user_guide/engagement_tools/templates_and_media/media_library)にアセットを追加できる。このエンドポイントは画像と、画像を含むZIPファイルをサポートしている。

## 前提条件

このエンドポイントを使用するには、[API キー]({{site.baseurl}}/api/basics#rest-api-key/)と`media_library.create`の権限が必要です。

## レート制限

{% multi_lang_include rate_limits.md endpoint='default' %}

## Request body

を含めると`asset_url`、エンドポイントはURLからファイルをダウンロードする。を含めると`asset_file`、エンドポイントはリクエスト本文のバイナリデータを使用する。

: `asset_url`のリクエストボディの例

```json
{
  "asset_url": "https://cdn.example.com/assets/cat.jpg",
  "name": "Cat Graphic"
}
```

: `asset_file`のリクエストボディの例

```json
{
  "asset_file": <BINARY FILE DATA>,
  "name": "Cat Graphic"
}
```

リクエスト本文には以下のパラメータが含まれる：

| パラメーター | 必須かどうか | データ型 | 説明 |
| --------- | -------- | --------- | ----------- |
| `asset_url` | オプション | string | Brazeにアップロードするアセットの、一般に公開されているURL。 |
| `asset_file` | オプション | 二進法 | バイナリファイルデータ。 |
| `name` | オプション | string | このアセットのメディアライブラリーに表示される名前。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
`asset_url` と`asset_file`は互いに排他的である。APIリクエストにはどちらか一方のみを含める必要がある。
{% endalert %}

### アップロードされたファイル名

このセクションでは、エンドポイントがアップロードされたファイルに名前を割り当てる方法を説明する。その方法は、パラメータ`name`を含めるかどうかによって異なる。

#### 単一ファイルのアップロード

| シナリオ | 結果: |
| --- | --- |
| `name` 提供された | この`name`値はメディアライブラリーにおけるアセット名として使用される。 |
| `name` 除外された | URLまたはアップロードされたファイルの元のファイル名が使用される。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

#### ZIPファイルのアップロード

| シナリオ | 結果: |
| --- | --- |
| `name` 提供された | この`name`値は接頭辞として使用され、末尾には連番が追加される（例：「My File 1」、「My File 2」、「My File 3」）。 |
| `name` 除外された | 各ファイルは、ZIPファイル内の元のファイル名を保持する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

## リクエスト例

このセクションには2つのリクエスト`curl`例が含まれる。1つはURLを使用してアセットを追加するものであり、もう1つはバイナリファイルデータを使用するものである。

このリクエストは、メディアライブラリーにアセットを追加する例を示している`asset_url`。

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic"}'
```

このリクエストは、メディアライブラリーにアセットを追加する例を示している`asset_file`。

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_file":<BINARY FILE DATA>, "name":"Cat Graphic"}'
```

### エラー応答

このセクションでは、発生する可能性のあるエラーとその対応するメッセージおよび説明を列挙する。 

#### 検証エラー

検証エラーは、次のような構造体を返す：

```json
{
  "message": (String) Human-readable error description
}
```

この表は、発生しうる検証エラーの一覧である。

| HTTPステータス | メッセージ | 説明 |
| --- | --- | --- |
| 400 | どちらかasset_url一方を提供asset_fileしなければならない。 | リクエストに資産パラメータが指定されていない。 |
| 400 | と  の両asset_url方を提供asset_fileすることはできない。一つだけ提供してください。 | 両方の資産パラメータが提供されたが、許可されているのは一つだけだ。 |
| 403 | この会社ではメディアライブラリーの公開APIのイネーブルメントは行われていない。 | このワークスペースではメディアライブラリーのイネーブルメントが有効になっていない。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### 処理エラー

処理エラーはエラーコード付きで異なる応答を返す：

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

この表は、発生する可能性のある処理エラーを一覧表示している。

| エラーコード | HTTPステータス | 説明 |
| --- | --- | --- |
| `UNSUPPORTED_FILE_TYPE` | 400 | アップロードされたファイル形式はサポートされていない。その`meta`オブジェクトには、却下されたものが`file_type`含まれている。 |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | ファイルが最大許容サイズを超えている。画像, 写真は5MBの制限がある。 |
| `MEDIA_LIBRARY_LIMIT_REACHED` | 400 | ワークスペースはアセットの最大数に達した（無料トライアル企業ではデフォルトで200、それ以外は無制限）。オブジェクト`meta`には現在のものが`limit`含まれる。 |
| `ASSET_UPLOAD_FAILED` | 400 | 処理の問題により、アセットのアップロードに失敗した。 |
| `ZIP_UPLOAD_ERROR` | 400 | ZIPファイルが破損しているか、開封できない。オブジェクト`meta`にはメッセージ`original_error`が含まれている。 |
| `ZIP_FILE_TOO_LARGE` | 400 | ZIPファイルの圧縮前の総サイズは5MBの制限を超えている。その`meta`オブジェクトには、`zip_file_name`とが含まれている`zip_file_size`。 |
| `ZIPPED_ENTITY_HAS_NO_NAME` | 400 | ZIPファイル内のファイルエントリには名前がない。ZIPファイルが破損していないことを確認し、名前が付けられていないファイルエントリには名前を付けること。 |
| `ZIPPED_ENTITY_CANNOT_HAVE_NESTED_DIRECTORY` | 400 | ZIPファイルにはネストされたディレクトリが含まれているが、これはサポートされていない。すべてのファイルはZIPのルートレベルに置かなければならない。 |
| `GENERIC_ERROR` | 500 | アップロード中に予期せぬエラーが発生した。その`meta`オブジェクトにはデバッグ用のメッセージ`original_error`が含まれている。もう一度試すか、[サポートに]({{site.baseurl}}/support_contact/)連絡する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## 応答

このエンドポイントには5つのステータスコード応答がある： `200`, `400`,`403` `429`, , および `500`。

以下のJSONは、レスポンスの期待される形状を示している。

```json
{ 
    "new_assets": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "url": (String) the URL to access the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif")
        }
    ],
    "errors": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif"),
            "error": (String) the error that occurred
        }
    ],
    "dashboard_url": (String) the URL to view this asset in the Braze dashboard
}
```

{% endapi %}
