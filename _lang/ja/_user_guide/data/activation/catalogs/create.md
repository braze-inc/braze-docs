---
nav_title: カタログを作成
article_title: カタログを作成する
alias: "/catalogs/"
page_order: 1
description: "この参考記事では、Liquidを通してBrazeのキャンペーンでユーザー以外のデータを参照するカタログを作成する方法について説明します。"
---

# カタログを作成

> カタログを作成するには、ユーザー以外のデータのCSVファイルをBrazeにインポートします。これにより、その情報にアクセスしてメッセージを充実させることができます。カタログには、任意のタイプのデータを取り込むことができます。このデータは通常、eコマースビジネスの商品情報や、教育プロバイダーのコース情報など、会社のある種のメタデータです。

## ユースケース

カタログの一般的なユースケースは次のとおりです。

- 製品
- サービス
- 食品
- 今後のイベント
- 音楽
- パッケージ

この情報をインポートすると、Liquid を介したカスタム属性またはカスタムイベントプロパティへのアクセスと同様の方法で、メッセージ内でのアクセスを開始できます。

## サポートされているデータタイプ {#supported-data-types}

以下の表は、サポートされているカタログのデータタイプと、それらの作成または更新方法を一覧にしています。

| データタイプ    | 説明                                   | CSVアップロードで利用可能 | APIとCDIを通じて利用可能 |
|--------------|-----------------------------------------------|:------------------------:|:-------------------------:|
| 文字列       | 一連の文字。                     | ✅ はい                    | ✅ はい                     |
| 数値       | 数値。整数か浮動小数点数のいずれか。     | ✅ はい                    | ✅ はい                     |
| ブール値      | `true` または `false` の値。                    | ✅ はい                    | ✅ はい                     |
| 時刻         | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 形式でフォーマットされた文字列。                        | ✅ はい                    | ✅ はい                     |
| JSONオブジェクト  | キーと値のペアを持つネストされたオブジェクト。プラットフォーム上で表示できますが、作成や更新はAPIまたはCDIを通じてのみ行えます。         | ⛔ いいえ                     | ✅ はい                     |
| 文字列配列 | 文字列のリスト。プラットフォーム上で表示できますが、作成や更新はAPIまたはCDIを通じてのみ行えます。最大100要素。 | ⛔ いいえ                     | ✅ はい                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## カタログを作成する

カタログを作成するには、**データ設定** > **カタログ**に移動し、**新規カタログ作成**を選択して、以下のいずれかのオプションを選びます。

{% tabs local %}
{% tab Upload CSV %}
### ステップ 1: CSVファイルを確認する

CSVファイルをアップロードする前に、そのファイルが以下の要件を満たしていることを確認してください。

| CSVの要件 | 詳細 |
|-----------------|---------|
| ヘッダー | CSVファイルの最初の列は `id` と名付ける必要があり、各行には一意の `id` 値が含まれている必要があります。 |
| 列 | CSVファイルには最大1,000個のフィールド（列）を含めることができます。各列名は最大250文字までです。 |
| ファイルサイズ | 無料プランでは、会社全体で扱うすべてのCSVファイルの合計サイズは100 MBに制限されます。プロプランの場合、単一のCSVファイルの最大ファイルサイズは2 GBです。 |
| フィールド値 | 各セル（フィールド値）は最大5,000文字まで含めることができます。 |
| 有効な文字 | `id` 列とすべてのヘッダー値は、英字、数字、ハイフン、アンダースコアのみを含めることができます。 |
| データタイプ | CSVアップロードでサポートされているデータタイプは、文字列、数値、ブール値、時刻です。APIおよびCDIを通じてのみ利用可能なデータタイプを含む全リストについては、[サポートされているデータタイプ](#supported-data-types)を参照してください。 |
| フォーマット | 一貫性を保つため、すべてのテキストを小文字でフォーマットしてください。 |
| エンコーディング | UTF-8エンコーディングでCSVファイルを保存し、アップロードしてください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
CSVファイルを保存するためにより多くのスペースが必要な場合は、カタログのアップグレードの詳細についてBrazeのアカウントマネージャーにお問い合わせください。
{% endalert %}

### ステップ 2: CSVをアップロードする

ファイルをアップロードゾーンにドラッグ＆ドロップするか、[**CSVをアップロード**] を選択してファイルを選択します。

![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

各列のデータタイプを選択します。

{% alert note %}
このデータタイプは、カタログをセットアップした後は編集できません。また、`NULL` 値はCSVアップロードではサポートされておらず、文字列として扱われます。
{% endalert %}

![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

カタログの名前と任意の説明を入力します。カタログに名前を付ける際には、以下の要件に留意してください。

  - 一意でなければなりません
  - 最大250文字
  - 数字、アルファベット、ハイフン、アンダースコアのみを含めることができます

{% alert tip %}
[カタログ名にテンプレートを使用](#template-catalog-names)することもできます。これにより、言語やキャンペーンなどの変数に基づいてカタログ名をダイナミックに生成できます。
{% endalert %}

!["my_catalog" という名前のカタログ。]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

**カタログを処理**を選択してカタログを作成します。

{% alert important %}
[ティア](#tiers)を超えた場合、CSVファイルが拒否される可能性があります。
{% endalert %}

### チュートリアル: CSVファイルからカタログを作成する

このチュートリアルでは、2つのゲームとその価格、そして画像リンクを掲載したカタログを使用します。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">title</th>
    <th class="tg-0pky">price</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">Tales</td>
    <td class="tg-0pky">7.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">Regeneration</td>
    <td class="tg-0pky">22.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

CSVファイルをアップロードしてカタログを作成します。`id`、`title`、`price`、および `image_link` のデータタイプは、それぞれ文字列、文字列、数値、文字列です。

{% alert note %}
このデータタイプは、カタログをセットアップした後は編集できません。
{% endalert %}

![4つのカタログ列名：「id」、「title」、「price」、「image_link」。]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

次に、このカタログに「games_catalog」と名前を付け、**カタログを処理**ボタンを選択します。その後、Brazeはカタログを作成する前に、カタログにエラーがないかチェックします。

!["games_catalog" という名前のカタログ。]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

カタログが作成された後は、この名前を編集することはできません。カタログを削除してから、同じカタログ名を使用して更新後のバージョンを再びアップロードできます。

カタログを作成したら、[キャンペーンでのカタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/)の参照を開始できます。
{% endtab %}

{% tab Create in browser %}
### 前提条件

ブラウザでカタログを編集または作成するには、ワークスペースに対して以下の[ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)が必要です。

- カタログを表示
- カタログを編集
- カタログをエクスポート
- カタログを削除

{% multi_lang_include deprecations/user_permissions.md %}

### ステップ 1: カタログの詳細を入力する

カタログの名前と任意の説明を入力します。カタログに名前を付ける際には、以下の要件に留意してください。

- 一意でなければなりません
- 最大250文字
- 数字、アルファベット、ハイフン、アンダースコアのみを含めることができます

{% alert tip %}
[カタログ名にテンプレートを使用](#template-catalog-names)することもできます。これにより、言語やキャンペーンなどの変数に基づいてカタログ名をダイナミックに生成できます。
{% endalert %}

!["my_catalog" という名前のカタログ。]({% image_buster /assets/img_archive/in_browser_catalog.png %}){: style="max-width:80%;"}

### ステップ 2: カタログを作成する

リストからカタログを選択し、次に**カタログを更新** > **フィールドを追加**を選択します。**フィールド名**を入力し、ドロップダウンからデータタイプを選択します。必要に応じて繰り返します。

![「rating」と「name」という2つのフィールドの例。]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

**カタログを更新** > **項目を追加**を選択し、以前に追加したフィールドに基づいて情報を入力して、カタログに項目を追加します。次に、**項目を保存**または**保存して追加**を選択して、項目の追加を続行します。

![カタログ項目を追加する。]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Brazeは、ダッシュボードのタイムスタンプに基づいて時間値を処理します。例えば、列の値が「03/13/2024」で、タイムゾーンが太平洋タイムゾーンの場合、この時刻は「Mar 12, 2024, 5:00 PM」としてBrazeにインポートされます。
{% endalert %}
{% endtab %}
{% endtabs %}

## カタログのデータタイプ

カタログはさまざまなデータタイプをサポートしており、データを効果的に整理し構造化するのに役立ちます。以下の表は、サポートされている各データタイプと、それらがCSVおよびAPIの型名にどのように対応するかを説明しています。

| データタイプ | フォーマット | 例 | 説明 |
|-----------|--------|---------|-------------|
| 文字列 | テキスト | `"Hello World"` | 名前、説明、IDなどのテキストデータに使用される任意の文字列。CSVおよびAPIインポートにおける `string` 型に相当します。 |
| 時刻 | ISO 8601 または Unix タイムスタンプ（秒単位） | `"2024-03-15T14:30:00Z"` | 日付と時刻の値は、ISO 8601 または Unix タイムスタンプ（秒単位）でフォーマットされます。APIにおける `time` 型と、CSVインポートにおける `datetime` 型に相当します。 |
| ブール値 | `true` または `false` | `true` | 真または偽の状態を表す論理値。CSVおよびAPIインポートにおける `boolean` 型に相当します。 |
| 数値 | 整数または小数 | `42` または `19.99` | 価格、数量、評価などの数値。整数や浮動小数点数を含みます。CSVインポートにおける `integer` および `float` 型、ならびにAPIにおける `number` 型に相当します。 |
| オブジェクト | JSONオブジェクト | `{"key": "value", "price": 10}` | 複雑なネストされたデータ構造。APIの `type` 値は `object` です。ダッシュボードではJSONオブジェクトとして表示されます。APIまたはクラウドデータ取り込み（CDI）経由でのみ利用可能です。 |
| 配列 | 文字列の配列 | `["red", "blue", "green"]` | 文字列値のリスト。APIの `type` 値は `array` です。ダッシュボードでは文字列配列として表示されます。APIまたはCDIを通じてのみ利用可能です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## カタログ名でのテンプレートの使用 {#template-catalog-names}

カタログに名前を付ける際、カタログ名にテンプレートを使用することもできます。これにより、言語やキャンペーンなどの変数に基づいてカタログ名をダイナミックに生成できます。例えば、次のように使用できます。

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## カタログの管理

### ダッシュボードで

CSVをアップロードした後やブラウザでカタログを作成した後にカタログを更新するには、**カタログを更新** > **CSVをアップロード**を選択し、カタログ内のアイテムを更新するか、追加するか、削除するかを選択します。

### REST APIの使用

作成したカタログが増えた場合、[カタログ一覧エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)を使用して、ワークスペース内のカタログのリストを返すこともできます。

REST APIは、JSONオブジェクトや文字列配列を含む、すべての[カタログデータタイプ](#supported-data-types)をサポートしています。JSONオブジェクトと文字列配列は、REST APIを通じてのみ作成または更新できます。

### クラウドデータ取り込みの使用

カタログは[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/)を通じて維持できます。具体的には、データウェアハウス（Snowflake、Redshift、BigQuery、Databricks、Microsoft Fabric、S3など）からカタログデータを直接同期し、スケジュールに基づいて更新します。

## カタログ項目の管理

カタログの管理に加えて、非同期および同期エンドポイントを使用してカタログ項目を管理することもできます。これには、カタログ項目の編集と削除、およびカタログ項目の詳細の一覧表示が含まれます。

例えば、個々のカタログ項目を編集する場合は、[`/catalogs/catalog_name/items/item_id` エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)を使用できます。

## カタログストレージ {#tiers}

無料版のカタログでは、会社全体のすべてのCSVファイルの合計で最大100 MBのファイルサイズがサポートされています。一方、Catalogs Proバージョンでは、単一のCSVファイルに対して最大2 GBのファイルサイズがサポートされています。

{% alert important %}
Brazeダッシュボードに表示されるパッケージのエンタイトルメントは、表示上の理由から最も近い単位に丸められていますが、購入したエンタイトルメントの全量が付与されています。カタログストレージのアップグレードをリクエストするには、Brazeのアカウントマネージャーにお問い合わせください。
{% endalert %}

#### 無料版

無料版カタログのストレージサイズは最大100&nbsp;MBです。100&nbsp;MB未満であれば、アイテム数に制限はありません。

#### Catalogs Pro

会社レベルで、Catalogs Proの最大ストレージはカタログデータのサイズに基づきます。ストレージサイズのオプションは、5&nbsp;GB、10&nbsp;GB、15&nbsp;GBのいずれかです。なお、無料版のストレージ（100&nbsp;MB）はこれらの各プランに含まれています。

## 仕様

以下の表は、カタログに含めることができる内容の仕様をまとめたものです。

| 項目 | 仕様 |
|------|-----------|
| 項目値の文字数 | 単一の値に最大5,000文字。例えば、`description` というラベルのフィールドがある場合、そのフィールド内の最大文字数は5,000文字です。 |
| 項目列名の文字数 | 最大250文字 |
| カタログあたりのセレクション数 | カタログあたり最大30セレクション |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
カタログの Liquid タグは再帰的に使用できません。つまり、同じ Liquid 評価内で、あるカタログ項目を参照し、そこからさらに別のカタログ項目を呼び出すことはできません。
{% endalert %}