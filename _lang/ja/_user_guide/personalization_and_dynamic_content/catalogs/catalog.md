---
nav_title: カタログを作成する
article_title: カタログを作成する
alias: "/catalogs/"
page_order: 1
description: "この参考記事では、Liquidを通してBrazeのキャンペーンでユーザー以外のデータを参照するカタログを作成する方法について説明する。"
---

# カタログを作成する

> カタログを作成するには、ユーザー以外のデータのCSVファイルをBrazeにインポートする。これにより、その情報にアクセスしてメッセージを充実させることができます。カタログには、任意のタイプのデータを取り込むことができます。このデータは通常、e コマース・ビジネスの商品情報や、教育プロバイダーのコース情報など、あなたの会社のある種のメタデータです。<br><br>このページでは、カタログを作成するための CSV ファイルの準備およびアップロード方法、カタログの管理方法などについて説明します。

カタログの一般的なユースケースは次のとおりです。

- 製品
- サービス
- 食品
- 今後のイベント
- 音楽
- パッケージ

この情報をインポートすると、Liquid を介したカスタム属性またはカスタムイベントプロパティへのアクセスと同様の方法で、メッセージ内でのアクセスを開始できます。

## CSVファイルを準備する

カタログを作成する前に、アップロードによるカタログ作成を希望する場合は、CSVファイルを用意しておくこと。

{% alert note %}
CSV ファイルを保存するためにより多くのスペースが必要な場合、カタログのアップグレードの詳細については、Brazeのアカウントマネージャーにお問い合わせください。
{% endalert %}

### CSVファイルのガイドライン

CSVファイルを作成する際には、以下のガイドラインに注意すること。CSVファイルの最初の列は、`id` のヘッダーでなければならず、各項目の`id` は一意でなければならない。その他のカラム名はすべて一意でなければならない。さらに、カタログCSVファイルには以下の制限が適用される：

- 最大1,000フィールド（列）。
- 最大250文字のフィールド（カラム）名
- 全社CSVファイル合計で最大100MB（無料）
- CSV ファイルの最大サイズ 2 GB (Pro)
- 最大5,000文字のフィールド値（セル）。
- `id` とヘッダーの値には、英字、数字、ハイフン、アンダースコアのみを使用できます。

また、CSVファイルのテキストはすべて小文字でフォーマットすることを推奨する。次のステップでCSVファイルをうまくアップロードするために、CSVファイルをUTF-8形式でエンコードしていることを確認しよう。

## 方法を選択する

カタログを作成するには、「**データ設定**」＞「**カタログ**」と進む。

**新しいカタログを作成**」を選択し、「**CSVをアップロード**」または「**ブラウザで作成**」のいずれかを選択する。

### 方法1:CSVをアップロードする

1. ファイルをアップロードゾーンにドラッグ＆ドロップするか、[**CSV をアップロードする**] を選択してファイルを選択します。<br>![]({% image_buster /assets/img_archive/catalog_CSV_upload.png %}){: style="max-width:80%;"}<br><br>
2. 各列のデータ型として、boolean、number、string、timeのいずれかを選択する。
<br> ![]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:80%;"}<br><br>
3. カタログに名前をつける。カタログ名に関する以下の要件に留意すること：
- 一意でなければなりません。
- 最大 250 文字。
- 数字、アルファベット、ハイフン、アンダースコアのみを含むことができる。<br><br>
4. (オプション) カタログの説明を追加します。
5. **プロセスカタログ**を押してカタログを作成します。

{% alert note %}
このデータタイプは、カタログをセットアップした後は編集できない。また、`NULL` 値はCSV アップロードではサポートされておらず、文字列として扱われます。
{% endalert %}

カタログ名にテンプレートを使うこともできる。例えば、次のものを使用できます。
{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items {{language}} fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

{% alert important %}
[階層](#tiers)を超えた場合、CSV ファイルが拒否される可能性があります。
{% endalert %}

ブラウザでカタログ作成を選択した後、CSVファイルを更新することもできる。**[カタログを更新] > [CSV をアップロード]** を選択し、カタログのアイテムの更新、追加、または削除のいずれを実行するかを選択します。

### 方法2：ブラウザで作成する

ブラウザーでカタログを編集または作成するには、「カタログダッシュボードの管理」権限が必要です。

1. カタログの名前を入力する。カタログ名については、以下の要件に留意すること：
- 一意でなければなりません。
- 最大 250 文字
- 数字、アルファベット、ハイフン、アンダースコアのみを含むことができる。 <br> !["my_catalog".]({% image_buster /assets/img_archive/in_browser_catalog.png %}) という名前のカタログ{: style="max-width:80%;"}<br><br>
2. (オプション) カタログの説明を入力します。
3. カタログを更新するには、[**カタログ**] ページのリストから、先ほど作成したカタログを選択します。
4. [**カタログを更新**] > [**フィールドを追加**] をクリックして、フィールドを追加します。次に、**フィールド名を**入力し、ドロップダウンを使ってデータタイプを選択する。必要に応じて繰り返す。<br> ![「rating」と「name」という2つのフィールドの例。]({% image_buster /assets/img_archive/add_catalog_fields.png %}){: style="max-width:50%;"}<br><br>
5. [**カタログを更新**] > [**項目を追加**] を選択し、以前に追加したフィールドに基づいて情報を入力して、カタログに項目を追加します。次に、[**項目を保存**] または [**保存して追加**] を選択して、項目の追加を続行します。<br> ![カタログアイテムを追加します。]({% image_buster /assets/img_archive/add_catalog_items.png %}){: style="max-width:50%;"}

ブラウザでカタログ作成を選択した後、CSVファイルをアップロードすることもできる。

{% alert note %}
Brazeは、ダッシュボードのタイムスタンプに基づいて時間値を処理する。例えば、カラムの値が "03/13/2024 "で、タイムゾーンが太平洋タイムゾーンの場合、この時刻は "Mar 12, 2024, 5:00 PM "としてBrazeにインポートされる。
{% endalert %}

#### チュートリアル: CSVファイルからカタログを作成する

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

![4 つのカタログ列名:"id"、"title"、"price"、"image_link".]({% image_buster /assets/img_archive/catalog_data_type.png %}){: style="max-width:85%;"}

次に、このカタログに「games_catalog」という名前を付け、「**Process Catalog」**ボタンを選択します。その後、Brazeはカタログを作成する前に、カタログにエラーがないかチェックする。

![「games_catalog」という名前のカタログ。]({% image_buster /assets/img_archive/catalog_new_name.png %}){: style="max-width:85%;"}

カタログが作成された後は、この名前を編集することはできないことに注意してほしい。カタログを削除してから、同じカタログ名を使用して更新後のバージョンを再びアップロードできます。

カタログを作成したら、[キャンペーンでカタログ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/)の参照を開始できます。

## APIでカタログを管理する

作成したカタログが増えた場合、[カタログのリストのエンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)を使用して、ワークスペース内のカタログのリストを返すこともできます。

### カタログ項目の管理

カタログの管理に加えて、非同期および同期エンドポイントを使用してカタログ項目を管理することもできます。これには、カタログ項目の編集と削除、およびカタログ項目の詳細の一覧表示の機能が含まれます。 

例えば、個々のカタログ項目を編集する場合は、[`/catalogs/catalog_name/items/item_id` エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)を使用できます。

## カタログ階層{#tiers}

無料版のカタログでは、会社全体で結合されたすべての CSV ファイルに対して最大100MBの CSV ファイルサイズがサポートされていますが、Catalogs Pro バージョンでは、単一の CSV ファイルに対して最大2GBの CSV ファイルサイズがサポートされています。

### カタログストレージ

{% alert important %}
Braze ダッシュボードに表示されるパッケージの権利は、見やすいように最も近い単位に丸められていますが、購入した権利全体が付与されています。カタログストレージのアップグレードを依頼するには、Brazeのアカウントマネージャーに連絡する。
{% endalert %}

#### 無料版

無料版カタログのストレージサイズは最大 100 MBです。100MB 未満であれば、アイテムに制限はありません。 

#### カタログ Pro

会社レベルで、カタログ Pro の最大ストレージはカタログデータのサイズに基づきます。ストレージサイズのオプションは以下の通りである：5GB、10GB、15GBのいずれか。なお、無料版のストレージ (100 MB) はこれらの各プランに含まれています。

