---
nav_title: API エンドポイントドキュメントガイドライン
article_title: API エンドポイントドキュメントガイドライン
description: "Braze API エンドポイントのドキュメント作成に関するガイドラインです。"
page_order: 3
noindex: true
---

# API エンドポイントドキュメントガイドライン

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

> 一般的に、API エンドポイントのドキュメントは[一般ガイドライン]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#general-guidelines)に従う必要があります。ただし、このドキュメントに記載されている特定のトピックについては、異なるコンテンツガイドラインが必要になる場合があります。

Braze は以下の REST API メソッドをサポートしています：

* GET  
* DELETE  
* PATCH  
* POST  
* PUT

## 新しいエンドポイント記事の作成

新しいエンドポイント記事を作成する際は、そのエンドポイントを [Braze API ガイド]({{site.baseurl}}/api/home)にも追加して、検索可能にしてください。**`_docs`** フォルダ **`> _api`** フォルダ **`> home.md`** ファイルに移動し、エンドポイントのパスと1文の説明を追加します。

## エンドポイントの参照方法

一般的に、ドキュメントでエンドポイントを参照する際の明確な規則はありません。Braze のエンドポイントを参照する場合は、ユースケースに応じてエンドポイントの参照方法を判断してください。

エンドポイントはパス（例：`/users/track`）で参照するか、エンドポイント名に「endpoint」という単語を付けて参照できます（例：the track user endpoint）。パスが特に長い場合は、エンドポイント名で参照してください。

エンドポイント名で参照する場合は、文のスタイルを使用します。パスで参照する場合は、コードテキストを使用します。

セクション名を直接参照する場合を除き、「endpoint」という単語を大文字にしないでください。エンドポイントを直接参照する場合は、「API」という単語を含めないでください。

エンドポイントが API として参照される場合もあります。例えば、Braze のエンドポイントについて一般的に述べる場合、「Braze uses a REST API with many endpoints」は正確な表現です。

エンドポイント名を引用符で囲まないでください。パスを参照する際にプレーンテキストを使用しないでください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">正しい例</th><th style="width: 50%;">誤った例</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Use the Generate preference center URL endpoint to complete the next steps.</td><td style="width: 50%;">Use <code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code> to complete the next steps.</td></tr>
<tr><td style="width: 50%;">Use the <code>/users/track</code> endpoint.</td><td style="width: 50%;">Use the "Users Track" API endpoint.</td></tr>
</tbody>
</table>
{:/}

### エンドポイント記事へのリンク

エンドポイント記事を参照する際は、コンテキストから外れても意味が通じる[意味のあるリンクテキスト]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#writing-links)を使用してください。エンドポイントのパスをリンクとして使用する場合は、パスだけではエンドポイントの機能が明確に伝わらない可能性があるため、周囲のテキストで詳細を提供してください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">正しい例</th><th style="width: 50%;">誤った例</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Delete user profiles using the Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user endpoint</a>.</td><td style="width: 50%;">Delete user profiles using the Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user</a> endpoint.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code> endpoint</a></td><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a> endpoint</td></tr>
</tbody>
</table>
{:/}

## 見出し

エンドポイント記事の導入部には、以下の情報を含める必要があります：

* リクエストタイプとエンドポイントパス URL  
* エンドポイントの簡単な説明（「Use this endpoint to…」で始めます）  
* 「See me in Postman」リンク  
* 必要な REST API キーの権限を示す注意アラート

以下のチェックリストを使用して、各エンドポイント記事に適切な見出し（およびコンテンツ）が記載された順序で含まれていることを確認してください。エンドポイント固有のサブ見出し（異なるタイプのリクエスト例など）がある場合もあります。

* レート制限  
* パスパラメーター  
* リクエストボディ  
* リクエストパラメーター  
* リクエスト例  
* レスポンスパラメーター  
* レスポンス例  
* トラブルシューティング（該当する場合）

フォーマットのガイドラインについては、[見出しとタイトル]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#headings-and-titles)を参照してください。

### パスパラメーター

エンドポイントにパスパラメーターがある場合は、パスパラメーターの見出しとテーブル（リクエストパラメーターテーブルと同様）を含めてください。

エンドポイントにパスパラメーターがない場合は、パスパラメーターの見出しと次のコールアウトを含めてください：「There are no path parameters for this endpoint.」

エンドポイントにパスパラメーターもリクエストパラメーターもない場合は、以下のように同じセクションに注意書きをまとめてください。

{% raw %}
{::nomarkdown}
<div style="margin-left: 2em;">
<code>
## Path and request parameters <br>
There are no path or request parameters for this endpoint.
</code>
</div>
{:/}
{% endraw %}

## 命名規則

各エンドポイント名は、メソッドの後に能動的な動詞で始めてください。これにより、ユーザーはエンドポイントの機能をすぐに理解できます。

エンドポイント名の先頭の動詞として API メソッドを使用しないでください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">正しい例</th><th style="width: 50%;">誤った例</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">POST: Create new user alias</td><td style="width: 50%;">POST: New user alias</td></tr>
<tr><td style="width: 50%;">GET: Look up an existing dashboard user account</td><td style="width: 50%;">GET: Existing dashboard user account</td></tr>
</tbody>
</table>
{:/}

この命名規則の例外は、[Export セクション]({{site.baseurl}}/api/endpoints/export)のエンドポイントです。セクション名自体が、リストされた情報をエクスポートできることを示す動詞になっているためです。

## API キーの権限

API キーの権限は、特定の API コールへのアクセスを制限するためにユーザーまたはグループに割り当てることができる権限です。各エンドポイントのドキュメントでは、Postman ドキュメントリンクの後に以下のコールアウトを含めてください：

> To use this endpoint, you must generate an API key with the `permission_name_here` permission.

API キーの権限の完全なリストを確認するには、Braze ダッシュボードの**設定とテスト**にある**設定 > API キー**に移動してください。フルアクセスの API キー（キー名には通常「full access」というフレーズが含まれています）を選択します。各権限名は通常、エンドポイント名と一致します。

SCIM エンドポイントには、開発者コンソール外で行われる SCIM インテグレーションに固有のものであるため、API キーの権限がリストされていないことに注意してください。

## レート制限

一般的に、レート制限にはリクエスト数と割り当てられた時間を指定する必要があります。

合計レート制限を共有するエンドポイントに注意してください。例えば、すべての非同期カタログアイテムエンドポイントは合計レート制限を共有しているため、それぞれの記事でその旨を示すことが重要です。

### レート制限ファイルの更新方法

エンドポイントのドキュメントでレート制限の更新または新しいレート制限のリストが必要な場合は、**_docs > _api > api_limits.md** に移動してレート制限を編集してください。

## パラメーター

リクエストパラメーターとレスポンスパラメーターを2つの別々のテーブルで定義してください。これらのテーブルには以下の列を含める必要があります：

* **Parameter**  
* **Required**  
* **Data Type**  
* **Description**

エンドポイントのパラメーターを直接参照する場合や、**Parameter** 列に値をリストする場合は、コードテキストを使用してください。**Required**、**Data Type**、**Description** 列に値をリストする場合は、先頭を大文字にしてください。

### プレースホルダーテキスト

プレースホルダーテキストには、ユーザーが含めるべき内容の簡単な説明を波かっこで囲んで使用してください。

API キーのプレースホルダーには、`YOUR-REST-API-KEY` ではなく `YOUR_REST_API_KEY` を使用してください。

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">正しい例</th><th style="width: 50%;">誤った例</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code></td><td style="width: 50%;"><code>/preference_center/v1/[preferenceCenterExternalId]</code></td></tr>
<tr><td style="width: 50%;"><code>/scim/v2/Users/{userId}</code></td><td style="width: 50%;"><code>/url/[userId]/scim/v2/Users/userID</code></td></tr>
</tbody>
</table>
{:/}

API キーのプレースホルダーには、`YOUR-REST-API-KEY`（ハイフン付き）ではなく `YOUR_REST_API_KEY`（アンダースコア付き）を使用してください。

## リクエストとレスポンス

API リクエストには、ヘッダーとリクエストパラメーターが含まれます。リクエストパラメーターは以下のようにフォーマットしてください：

```bash
parameter": (required/optional, data type) A brief description
```

以下は、[Create new user alias エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/)のリクエストボディの例です：

```bash
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "user_aliases": (required, array of new user alias object)
}
```

リクエスト例で文字列または配列のパラメーターを識別するには、二重直線引用符（" "）を使用してください。すべての開きかっこが閉じられていることを確認してください。

API レスポンスには、レスポンスボディ、ヘッダー、および HTTP ステータスコードが含まれます。常にレスポンス例を含めてください。この例には、パラメーターを説明するシンプルなテキスト例を含める必要があります。以下は、[Update user alias エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/#example-request)のレスポンス例です。

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

### ステータスコードとエラーコード

ステータスコードは、ユーザーの特定のリクエストが正常に完了したかどうかを示します。何が成功とみなされるかをユーザーに知らせるために、ステータスコードを含めると役立ちます。例えば、400 と 404 はエンドポイントのエラーレスポンスの指標となります。

エンドポイントのドキュメントでエラーコードをリストする必要がある場合は、**_docs** フォルダ **> _api** フォルダ **> errors.md** ファイルにある [API Error and Responses]({{site.baseurl}}/api/errors/) 記事にリンクしてください。

## サンプルコード

サンプルコードは、サンプルリクエストやレスポンスと同様に、最小限の作業でコピーして使用できるようにする必要があります。プレースホルダーテキスト（例：ヘッダー内の API キー）を除き、リクエスト例はそのまま動作する必要があります。Postman を使用して、リクエストが正しくフォーマットされていることを確認してください。

### 整形コードとミニファイコード

エンドポイントのリクエストにボディが含まれている場合は、Postman で例を整形してください。これにより、Braze の規則を学んでいる開発者がリクエストの各部分を理解しやすくなります。

エンドポイントのリクエストボディが非常に短い場合やボディが含まれていない場合は、不要な空白が削除されるようにリクエストをミニファイしてください。[JSON Minifier](https://codebeautify.org/jsonminifier) などのツールを使用してください。

### インラインコメント

コード例の単一行コメントを示すには、2つのスラッシュ（//）を使用してください。

インラインコメントは、コードの特定のセクションにユーザーの注意を引いたり、コードブロックの機能を説明したり、追加のコンテキストを提供したりするための有用なツールです。

インラインコメントを使用して、ユーザーのロジックレイヤーが配置される場所と、SDK コードをどのように参照するかを素早く示してください。シンプルで現実的な例を使用してください。例えば、「example_attribute」よりも「favorite_movie」という属性の例の方が効果的です。ユーザーのビジネスがエンドユーザーのお気に入りの映画を追跡していなくても、この例はこの属性を通じて追跡される可能性のある*種類*のユースケースを示しています。一般的な例では、同じ直感的な理解を引き出すことができません。

人間が読めるコードやメソッド名を単に繰り返すだけのインラインコメントは避けてください。代わりに、Braze 固有のメソッドやパラメーターにさまざまな同義語を使用して、英語を母語としない方への理解の足がかりを提供してください。

一般的に、インラインコメントを提供する際は標準的な英語の規則に従ってください。例えば、文は大文字で始め、単語は完全にスペルアウトしてください。

## その他のリソース

- [Google developer documentation style guide](https://developers.google.com/style)  
  - [API reference code and comments](https://developers.google.com/style/api-reference-comments)