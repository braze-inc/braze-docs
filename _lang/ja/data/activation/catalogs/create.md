---
nav_title: カタログを作成する
article_title: カタログを作成する
alias: "/catalogs/"
page_order: 1
description: "この参考記事では、Liquidを通してBrazeのキャンペーンでユーザー以外のデータを参照するカタログを作成する方法について説明する。"
---

# カタログを作成する

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

## カタログを作成する

カタログを作成するには、**データ設定** > **カタログs**に移動し、**新しいカタログを作成**を選択して、次のいずれかのオプションを選択します。

{% tabs local %}
{% tab Upload CSV %}
### ステップ 1: CSVファイルの確認

CSVファイルをアップロードするには、お使いのCSVファイルが次の条件を満たしていることを確認してください。

| CSV 要件 | 詳細 |
|-----------------|---------|
| ヘッダー | CSVファイルの最初の列は`id` という名前にする必要があり、各行には一意の`id` 値が必要です。 |
| 列 | CSVファイルには、最大1000 個のフィールド(列) を指定でき、各列の名前は最大250 文字にすることができます。 |
| ファイルサイズ | フリープランの場合、企業全体のすべてのCSVファイルの総容量は100MB に制限されます。プロプランの場合、1 つのCSVファイルの最大ファイルサイズは2GB です。 |
| フィールド値 | セル(フィールド)には、最大5000 文字を含めることができます。 |
| 有効な文字 | `id`列とすべてのヘッダーは、文字、数字、ハイフン、アンダースコアのみを含むことができます。 |
| データ型 | CSVファイルをアップロードするためにサポートされているデータタイプには、ストリング、整数、浮動小数点数、ブール値、日時などがあります。 |
| フォーマット | 整合性を維持するために、すべてのテキストを小文字でフォーマットします。 |
| エンコーディング | UTF-8 エンコードを使用してCSVファイルを保存してアップロードします。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert note %}
CSV ファイルを保存するためにより多くのスペースが必要な場合、カタログのアップグレードの詳細については、Brazeのアカウントマネージャーにお問い合わせください。
{% endalert %}

### ステップ 2: CSVをアップロードする

ファイルをアップロードゾーンにドラッグ＆ドロップするか、[**CSV をアップロードする**] を選択してファイルを選択します。

![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}

各列のデータ型を選択します。

{% alert note %}
このデータタイプは、カタログをセットアップした後は編集できない。また、`NULL` 値はCSV アップロードではサポートされておらず、文字列として扱われます。
{% endalert %}

![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}

カタログの名前と説明(オプション)を入力します。カタログに名前を付けるときは、次の点に注意してください。

  - 一意でなければなりません。
  - 最大 250 文字。
  - 数字、アルファベット、ハイフン、アンダースコアのみを含むことができる。

{% alert tip %}
また、[カタログネーム](#template-catalog-names)でテンプレートsを使用して、言語やキャンペーンなどの変数に基づいてカタログネームをダイナミックな生成することもできます。
{% endalert %}

!["my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}という名前のカタログ{: style="max-width:80%;"}

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

![4 つのカタログ列名:"id"、"title"、"price"、"image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}{: style="max-width:85%;"}

次に、このカタログに"games_catalog" と名前を付け、**Process カタログ** ボタンを選択します。その後、Brazeはカタログを作成する前に、カタログにエラーがないかチェックする。

!["games_catalog".]({% image_buster /assets/img_archive/catalog_new_name.png %}という名前のカタログ{: style="max-width:85%;"}

カタログが作成された後は、この名前を編集することはできないことに注意してほしい。カタログを削除してから、同じカタログ名を使用して更新後のバージョンを再びアップロードできます。

カタログを作成したら、[キャンペーンでカタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/)の参照を開始できます。
{% endtab %}

{% tab Create in browser %}
### 前提条件

ブラウザーでカタログを編集または作成するには、**カタログの管理ダッシュボード** 権限が必要です。

### ステップ 1: カタログ内容を入力

カタログの名前と説明(オプション)を入力します。カタログに名前を付けるときは、次の点に注意してください。

- 一意でなければなりません。
- 最大 250 文字。
- 数字、アルファベット、ハイフン、アンダースコアのみを含むことができる。

{% alert tip %}
また、[カタログネーム](#template-catalog-names)でテンプレートsを使用して、言語やキャンペーンなどの変数に基づいてカタログネームをダイナミックな生成することもできます。
{% endalert %}

!["my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}という名前のカタログ{: style="max-width:80%;"}

### ステップ 2: カタログを作成する

一覧からカタログを選択し、**アップデートカタログ**> **フィールドを追加** を選択します。**フィールド名**を入力し、ドロップダウンを使用してデータ型を選択します。必要に応じて繰り返す。

![「rating」と「name」という2つのフィールドの例。]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}

[**カタログを更新**] > [**項目を追加**] を選択し、以前に追加したフィールドに基づいて情報を入力して、カタログに項目を追加します。次に、[**項目を保存**] または [**保存して追加**] を選択して、項目の追加を続行します。

![カタログ項目を追加する。]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

{% alert note %}
Brazeは、ダッシュボードのタイムスタンプに基づいて時間値を処理する。例えば、カラムの値が "03/13/2024 "で、タイムゾーンが太平洋タイムゾーンの場合、この時刻は "Mar 12, 2024, 5:00 PM "としてBrazeにインポートされる。
{% endalert %}
{% endtab %}
{% endtabs %}

## カタログの名前でのテンプレートsの使用 {#template-catalog-names}

カタログに名前を付けるときは、カタログの名前にテンプレート s を使用することもできます。これにより、言語やキャンペーンなどの変数に基づいてカタログの名前をダイナミックな的に生成できます。例えば、次のものを使用できます。

{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

## カタログの管理

### ダッシュボードで

CSV を更新した後、またはブラウザーでカタログを作成した後にカタログをアップロードするには、** 更新 カタログ > アップロード CSV** を選択し、カタログ内の項目を更新、追加、または削除するかどうかを選択します。

### REST API の使用

作成したカタログが増えた場合、[カタログのリストのエンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)を使用して、ワークスペース内のカタログのリストを返すこともできます。

API を使用するためにサポートされているデータ型は、string、integer、float、boolean、datetime です。また、API を使用してカタログを管理するときに、配列やオブジェクトをアップロードすることもできます。

## カタログ項目の管理

カタログの管理に加えて、非同期および同期エンドポイントを使用してカタログ項目を管理することもできます。これには、カタログ項目の編集と削除、およびカタログ項目の詳細の一覧表示の機能が含まれます。 

例えば、個々のカタログ項目を編集する場合は、[`/catalogs/catalog_name/items/item_id` エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)を使用できます。

## カタログストレージ

無料版のカタログでは、会社全体で結合されたすべての CSV ファイルに対して最大100MBの CSV ファイルサイズがサポートされていますが、Catalogs Pro バージョンでは、単一の CSV ファイルに対して最大2GBの CSV ファイルサイズがサポートされています。

{% alert important %}
Braze ダッシュボードに表示されるパッケージの権利は、見やすいように最も近い単位に丸められていますが、購入した権利全体が付与されています。カタログストレージのアップグレードを依頼するには、Brazeのアカウントマネージャーに連絡する。
{% endalert %}

#### 無料版

無料版カタログのストレージサイズは最大 100 MBです。100MB 未満であれば、アイテムに制限はありません。 

#### カタログ Pro

会社レベルで、カタログ Pro の最大ストレージはカタログデータのサイズに基づきます。ストレージサイズのオプションは以下の通りである：5GB、10GB、15GBのいずれか。なお、無料版のストレージ (100 MB) はこれらの各プランに含まれています。
