---
nav_title: カタログを作成
article_title: カタログを作成する
alias: "/catalogs/"
page_order: 1
description: "この参考記事では、Liquidを通してBrazeのキャンペーンでユーザー以外のデータを参照するカタログを作成する方法について説明する。"
---

# カタログを作成

> カタログを作成するには、ユーザー以外のデータのCSVファイルをBrazeにインポートする。これにより、その情報にアクセスしてメッセージを充実させることができます。カタログには、任意のタイプのデータを取り込むことができます。このデータは通常、e コマース・ビジネスの商品情報や、教育プロバイダーのコース情報など、あなたの会社のある種のメタデータです。

## ユースケース

カタログの一般的なユースケースは次のとおりです。

- 製品
- サービス
- 食品
- 今後のイベント
- 音楽
- パッケージ

この情報をインポートすると、Liquid を介したカスタム属性またはカスタムイベントプロパティへのアクセスと同様の方法で、メッセージ内でのアクセスを開始できます。

## サポートされているデータ型 {#supported-data-types}

以下の表は、サポートされているカタログデータ型と、それらの作成または更新方法を一覧表示している。

| データタイプ    | 説明                                   | CSVアップロードで利用可能だ | APIとCDIを通じて利用可能だ |
|--------------|-----------------------------------------------|:------------------------:|:-------------------------:|
| string       | 一連の文字。                     | ✅ そうだ                    | ✅ そうだ                     |
| 数値       | 数値。整数か浮動小数点数のいずれかである。     | ✅ そうだ                    | ✅ そうだ                     |
| ブール値      | A `true`または `false`値。                    | ✅ そうだ                    | ✅ そうだ                     |
| 時刻         | [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)形式でフォーマットされた文字列。                        | ✅ そうだ                    | ✅ そうだ                     |
| JSONオブジェクト  | キーと値のペアを持つ入れ子オブジェクトだ。プラットフォーム上で表示できるが、作成や更新はAPIまたはCDIを通じてのみ行える。         | ⛔ ダメだ                     | ✅ そうだ                     |
| 文字列配列 | 文字列のリストだ。プラットフォーム上で表示できるが、作成や更新はAPIまたはCDIを通じてのみ行える。最大100個まで。 | ⛔ ダメだ                     | ✅ そうだ                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## カタログを作成する

カタログを作成するには、**データ設定**＞**カタログ**に移動し、**新規カタログ作成**を選択する。次に以下のいずれかのオプションを選ぶ：

{% tabs local %}
{% tab Upload CSV %}
### ステップ 1: CSVファイルを確認せよ

CSVファイルをアップロードする前に、そのファイルが以下の要件を満たしていることを確認せよ。

| CSVの要件 | 詳細 |
|-----------------|---------|
| ヘッダー | CSVファイルの最初の列は必ず「ID」と名付けなければならない`id`。また、各行には一意の「`id`ID」値が含まれていなければならない。 |
| 列 | CSVファイルには最大1,000個のフィールド（列）を含めることができる。各列名は最大250文字までである。 |
| ファイルサイズ | 無料プランでは、会社全体で扱うすべてのCSVファイルの合計サイズは100MBに制限される。プロプランの場合、単一のCSVファイルの最大ファイルサイズは2GBである。 |
| フィールド値 | 各セル（フィールド値）は最大5,000文字まで含むことができる。 |
| 有効な文字 | 列`id`とすべてのヘッダー値は、英字、数字、ハイフン、アンダースコアのみを含めることができる。 |
| データ型 | CSVアップロードでサポートされているデータ型は、文字列、数値、ブール値、時刻である。APIおよびCDIを通じてのみ利用可能なデータ型を含む、全データ型のリストについては、[「サポートされているデータ型](#supported-data-types)」を参照せよ。 |
| フォーマット | すべてのテキストを小文字で統一する。 |
| エンコーディング | UTF-8エンコーディングでCSVファイルを保存し、アップロードする。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
CSV ファイルを保存するためにより多くのスペースが必要な場合、カタログのアップグレードの詳細については、Brazeのアカウントマネージャーにお問い合わせください。
{% endalert %}

### ステップ 2:CSVをアップロードする

ファイルをアップロードゾーンにドラッグ＆ドロップするか、[**CSV をアップロードする**] を選択してファイルを選択します。

![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

各列のデータ型を選択せよ。

{% alert note %}
このデータタイプは、カタログをセットアップした後は編集できない。また、`NULL` 値はCSV アップロードではサポートされておらず、文字列として扱われます。
{% endalert %}

![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

カタログの名前と任意の説明を入力せよ。カタログに名前を付ける際には、以下の要件を心に留めておくことだ。

  - 一意でなければなりません。
  - 最大 250 文字。
  - 数字、アルファベット、ハイフン、アンダースコアのみを含むことができる。

{% alert tip %}
[カタログ名にテンプレートを使用](#template-catalog-names)することもできる。これにより、言語やキャンペーンなどの変数に基づいてカタログ名をダイナミックに生成できる。
{% endalert %}

!["my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.pngという名前のカタログ %}{: style="max-width:80%;"}

**プロセスカタログ**を押してカタログを作成します。

{% alert important %}
[階層](#tiers)を超えた場合、CSV ファイルが拒否される可能性があります。
{% endalert %}

### チュートリアル: CSVファイルからカタログを作成する

このチュートリアルでは、2つのゲームとそのコスト、そして画像リンクを掲載したカタログを使用する。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">id</th>
    <th class="tg-0pky">名称</th>
    <th class="tg-0pky">価格</th>
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

CSVファイルをアップロードしてカタログを作成する。`id`、`title`、`price`、および `image_link` のデータ型は、それぞれ文字列、文字列、数値、文字列です。 

{% alert note %}
このデータタイプは、カタログをセットアップした後は編集できない。
{% endalert %}

![四つのカタログ列名：「id」、「title」、「price」、/assets/img_archive/catalog_data_type.pngimage_buster"image_link".]({%    %}){: style="max-width:85%;"}

次に、このカタログに名前を"games_catalog"付け、**カタログ処理**ボタンを選択する。その後、Brazeはカタログを作成する前に、カタログにエラーがないかチェックする。

!["games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.pngという名前のカタログ %}{: style="max-width:85%;"}

カタログが作成された後は、この名前を編集することはできないことに注意してほしい。カタログを削除してから、同じカタログ名を使用して更新後のバージョンを再びアップロードできます。

カタログを作成したら、[キャンペーンでカタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/)の参照を開始できます。
{% endtab %}

{% tab Create in browser %}
### 前提条件

ブラウザでカタログを編集または作成するには、ワークスペースに対して以下の[ユーザー権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)が必要だ：

- カタログを表示
- カタログを編集
- カタログをエクスポート
- カタログを削除

{% multi_lang_include deprecations/user_permissions.md %}

### ステップ 1: カタログの詳細を入力せよ

カタログの名前と任意の説明を入力せよ。カタログに名前を付ける際には、以下の要件を心に留めておくことだ。

- 一意でなければなりません。
- 最大 250 文字。
- 数字、アルファベット、ハイフン、アンダースコアのみを含むことができる。

{% alert tip %}
[カタログ名にテンプレートを使用](#template-catalog-names)することもできる。これにより、言語やキャンペーンなどの変数に基づいてカタログ名をダイナミックに生成できる。
{% endalert %}

!["my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.pngという名前のカタログ %}{: style="max-width:80%;"}

### ステップ 2:カタログを作成する

リストからカタログを選択し、次に**「カタログを更新」**＞**「フィールドを追加」**を選択する。**フィールド名**を入力し、ドロップダウンからデータ型を選択する。必要に応じて繰り返す。

![「rating」と「name」という2つのフィールドの例。]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

[**カタログを更新**] > [**項目を追加**] を選択し、以前に追加したフィールドに基づいて情報を入力して、カタログに項目を追加します。次に、[**項目を保存**] または [**保存して追加**] を選択して、項目の追加を続行します。

![カタログ項目を追加する。]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Brazeは、ダッシュボードのタイムスタンプに基づいて時間値を処理する。例えば、カラムの値が "03/13/2024 "で、タイムゾーンが太平洋タイムゾーンの場合、この時刻は "Mar 12, 2024, 5:00 PM "としてBrazeにインポートされる。
{% endalert %}
{% endtab %}
{% endtabs %}

## カタログデータ型

カタログは様々なデータ型をサポートし、データを効果的に整理し構造化するのに役立つ。以下の表は、サポートされている各データ型と、それらがCSVおよびAPIの型名にどのように対応するかを説明するものである：

| データ型 | フォーマット | 例 | 説明 |
|-----------|--------|---------|-------------|
| string | テキスト | `"Hello World"` | 名前、説明、IDなどのテキストデータに使用される任意の文字列。CSVおよびAPIインポートにおける型`string`に相当する。 |
| 時刻 | ISO 8601 または Unix タイムスタンプ（秒単位） | `"2024-03-15T14:30:00Z"` | 日付と時刻の値は、ISO 8601 または Unix タイムスタンプ（秒単位）でフォーマットされる。APIにおける型と、CSVインポート`time`における型`datetime`に相当する。 |
| ブール値 | `true` または `false` | `true` | 真または偽の状態を表す論理値。CSVおよびAPIインポートにおける型`boolean`に相当する。 |
| 数値 | 整数か小数 | `42` または `19.99` | 価格、数量、評価などの数値。整数や浮動小数点数を含む。CSVインポートにおける  および`float`  型、ならびにAPI`integer`における  型`number`に相当する。 |
| オブジェクト | JSONオブジェクト | `{"key": "value", "price": 10}` | 複雑な入れ子構造のデータ。API`type`の値は`object`。ダッシュボードではJSONオブジェクトとして表示される。APIまたはクラウドデータ取り込み（CDI）経由でのみ利用可能だ。 |
| 配列 | 文字列の配列 | `["red", "blue", "green"]` | 文字列値のリスト。API`type`の値は`array`。ダッシュボードでは文字列配列として表示される。APIまたはCDIを通じてのみ利用可能だ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

## カタログ名でのテンプレートの使用 {#template-catalog-names}

カタログに名前を付ける際、カタログ名にテンプレートを使用することもできる。これにより、言語やキャンペーンなどの変数に基づいてカタログ名をダイナミックに生成できる。例えば、次のものを使用できます。

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## カタログの管理

### ダッシュボードで

CSVをアップロードした後やブラウザでカタログを作成した後、カタログを更新するには、**[カタログを更新] > [CSVをアップロード**] を選択する。その後、カタログ内のアイテムを更新するか、追加するか、削除するかを選択する。

### REST API の使用

作成したカタログが増えた場合、[カタログのリストのエンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)を使用して、ワークスペース内のカタログのリストを返すこともできます。

REST APIは、JSONオブジェクトや文字列配列を含む、すべての[カタログデータ型](#supported-data-types)をサポートしている。JSONオブジェクトと文字列配列は、REST APIを通じてのみ作成または更新できる。

### クラウドデータ取り込みの利用

カタログは[、クラウドデータ取り込み]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data/)を通じて維持できる。具体的には、データウェアハウス（Snowflake、Redshift、BigQuery、Databricks、Microsoft Fabric、S3など）からカタログデータを直接同期し、スケジュールされたスケジュールに基づいて更新する。

## カタログ項目の管理

カタログの管理に加えて、非同期および同期エンドポイントを使用してカタログ項目を管理することもできます。これには、カタログ項目の編集と削除、およびカタログ項目の詳細の一覧表示の機能が含まれます。 

例えば、個々のカタログ項目を編集する場合は、[`/catalogs/catalog_name/items/item_id` エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)を使用できます。

## カタログ保管 {#tiers}

無料版のカタログでは、会社全体で結合されたすべての CSV ファイルに対して最大100MBの CSV ファイルサイズがサポートされていますが、Catalogs Pro バージョンでは、単一の CSV ファイルに対して最大2GBの CSV ファイルサイズがサポートされています。

{% alert important %}
Braze ダッシュボードに表示されるパッケージの権利は、見やすいように最も近い単位に丸められていますが、購入した権利全体が付与されています。カタログストレージのアップグレードを依頼するには、Brazeのアカウントマネージャーに連絡する。
{% endalert %}

#### 無料版

無料版カタログのストレージサイズは最大 100 MBです。100MB 未満であれば、アイテムに制限はありません。 

#### カタログ Pro

会社レベルで、カタログ Pro の最大ストレージはカタログデータのサイズに基づきます。ストレージサイズのオプションは以下の通りである：5GB、10GB、15GBのいずれか。なお、無料版のストレージ (100 MB) はこれらの各プランに含まれています。
