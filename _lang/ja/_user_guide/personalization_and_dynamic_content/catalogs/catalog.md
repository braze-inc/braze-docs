---
nav_title: カタログを作成する
article_title: カタログを作成する
alias: "/catalogs/"
page_order: 1
description: "この参考記事では、Liquidを通してBrazeのキャンペーンでユーザー以外のデータを参照するカタログを作成する方法について説明する。"
---

# カタログを作成する

> カタログを作成するには、ユーザー以外のデータのCSVファイルをBrazeにインポートする。これにより、あなたはその情報にアクセスしてメッセージを充実させることができる。カタログにはどんな種類のデータでも持ち込むことができる。このデータは通常、eコマース・ビジネスの商品情報や、教育プロバイダーのコース情報など、あなたの会社のある種のメタデータである。

カタログの一般的な使用例には次のようなものがある：

- products
- サービス
- 食品
- 今後のイベント
- 音楽
- パッケージ

この情報がインポートされると、Liquidを通してカスタム属性やカスタムイベントプロパティにアクセスするのと同じように、メッセージでアクセスできるようになる。

## CSVファイルを準備する

カタログを作成する前に、アップロードによるカタログ作成を希望する場合は、CSVファイルを用意しておくこと。

{% alert note %}
CSVファイルを保存するためにより多くのスペースが必要か？カタログのアップグレードの詳細については、Brazeのアカウントマネージャーにお問い合わせください。
{% endalert %}

### CSVファイルのガイドライン

CSVファイルを作成する際には、以下のガイドラインに注意すること。CSVファイルの最初の列は、`id` のヘッダーでなければならず、各項目の`id` は一意でなければならない。その他のカラム名はすべて一意でなければならない。さらに、カタログCSVファイルには以下の制限が適用される：

- 最大1,000フィールド（列）。
- 最大250文字のフィールド（カラム）名
- 全社CSVファイル合計で最大100MB（無料）
- 最大CSVファイルサイズ2GB（Pro）
- 最大5,000文字のフィールド値（セル）。
- `id` 、ヘッダー値には文字、数字、ハイフン、アンダースコアのみを使用する。

また、CSVファイルのテキストはすべて小文字でフォーマットすることを推奨する。次のステップでCSVファイルをうまくアップロードするために、CSVファイルをUTF-8形式でエンコードしていることを確認しよう。

## 方法を選択する

カタログを作成するには、「**データ設定**」＞「**カタログ**」と進む。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**「** **データ**」の下に**「カタログ」が**ある。
{% endalert %}

**新規カタログを作成**」をクリックし、「**CSVをアップロード**」または「**ブラウザで作成**」のいずれかを選択する。

### 方法1：CSVをアップロードする

1. ファイルをアップロードゾーンにドラッグ＆ドロップするか、「**CSVをアップロード**」をクリックしてファイルを選択する。<br>![][1]{: style="max-width:80%;"}<br><br>
2. 各列のデータ型として、boolean、number、string、timeのいずれかを選択する。
<br> ![][9]{: style="max-width:80%;"}<br><br>
3. カタログに名前をつける。カタログ名に関する以下の要件に留意すること：
- ユニークでなければならない
- 最大250文字
- 数字、アルファベット、ハイフン、アンダースコアのみを含むことができる。<br><br>
4. (オプション）カタログの説明を追加する。
5. **プロセスカタログ**を押してカタログを作成します。

{% alert note %}
このデータタイプは、カタログをセットアップした後は編集できない。
{% endalert %}

カタログ名にテンプレートを使うこともできる。例えば、次のように使うことができる：
{% raw %}
```liquid
{% assign language = "content_spanish" %}

{% catalog_items language fall_campaign %}
{{ items[0].body }}
```
{% endraw %}

{% alert important %}
CSVファイルは、[階層を](#tiers)超えると拒否される可能性がある。
{% endalert %}

ブラウザでカタログ作成を選択した後、CSVファイルを更新することもできる。**カタログの更新＞CSVのアップロードを**クリックし、カタログのアイテムを更新、追加、削除するかを選択する。

### 方法2：ブラウザで作成する

1. カタログの名前を入力する。カタログ名については、以下の要件に留意すること：
- ユニークでなければならない
- 最大250文字
- 数字、アルファベット、ハイフン、アンダースコアのみを含むことができる。 <br> ![][14]{: style="max-width:80%;"}<br><br>
2. (オプション）カタログの説明を入力する。
3. **カタログ**一覧ページから作成したカタログを選択し、カタログを更新する。
4. **カタログの更新＞フィールドの追加を**クリックして、フィールドを追加する。次に、**フィールド名を**入力し、ドロップダウンを使ってデータタイプを選択する。必要に応じて繰り返す。<br> ![][12]{: style="max-width:50%;"}<br><br>
5. **カタログの更新＞項目の追加を**クリックし、以前に追加したフィールドに基づいて情報を入力し、カタログに項目を追加する。その後、**Save Item**または**Save and Add Anotherを**クリックし、アイテムの追加を続ける。<br> ![][13]{: style="max-width:50%;"}

ブラウザでカタログ作成を選択した後、CSVファイルをアップロードすることもできる。

{% alert note %}
Brazeは、ダッシュボードのタイムスタンプに基づいて時間値を処理する。例えば、カラムの値が "03/13/2024 "で、タイムゾーンが太平洋タイムゾーンの場合、この時刻は "Mar 12, 2024, 5:00 PM "としてBrazeにインポートされる。
{% endalert %}

#### チュートリアルだ：CSVファイルからカタログを作成する

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
    <th class="tg-0pky">タイトル</th>
    <th class="tg-0pky">価格</th>
    <th class="tg-0pky">イメージリンク</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">テイルズ</td>
    <td class="tg-0pky">7.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">再生</td>
    <td class="tg-0pky">22.49</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

CSVファイルをアップロードしてカタログを作成する。`id` 、`title` 、`price` 、`image_link` のデータ型は、それぞれ文字列、文字列、数値、文字列である。 

{% alert note %}
このデータタイプは、カタログをセットアップした後は編集できない。
{% endalert %}

![][9]{: style="max-width:85%;"}

次に、このカタログに「games_catalog」という名前を付け、「**Process Catalog」**ボタンをクリックする。その後、Brazeはカタログを作成する前に、カタログにエラーがないかチェックする。

![][11]{: style="max-width:85%;"}

カタログが作成された後は、この名前を編集することはできないことに注意してほしい。カタログを削除し、同じカタログ名を使用して更新版を再アップロードすることができる。

カタログを作成したら、[キャンペーンでカタログを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/)参照し始めることができる。

## APIでカタログを管理する

より多くのカタログを構築すると、[List catalogsエンドポイントを]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)使用して、ワークスペース内のカタログのリストを返すこともできる。

### カタログ項目を管理する

カタログを管理するだけでなく、非同期エンドポイントや同期エンドポイントを使ってカタログ項目を管理することもできる。これには、カタログ項目の編集と削除、およびカタログ項目の詳細の一覧表示機能が含まれる。 

例えば、個々のカタログ項目を編集したい場合、[`/catalogs/catalog_name/items/item_id` エンドポイントを]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)使うことができる。

## その他の使用例

### 複数の項目

1つのメッセージに含まれる項目は1つに限定されない！**パーソナライズの追加]**モーダルを使用して、表示する追加カタログ項目と情報を挿入するだけである。なお、追加できるカタログ項目は3つまでである。 

この例では、**「**テイルズ」、「テスラグラッド」、「アカラタス」の3つのゲームの`id` を「**カタログ項目**」に追加し、「**表示する情報**」に`title` を選択している。

![][6]{: style="max-width:70%" }

リキッドの周りにテキストを追加することで、メッセージをさらにパーソナライズすることができる：

{% raw %}
```liquid
Get the ultimate trio {% catalog_items games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

これは以下のように返される：

> 究極のトリオ「テイルズ」、「テスラグラッド」、「アカラタス」を今すぐ手に入れよう！

{% alert tip %}
よりパーソナライズされたメッセージングのために、データのグループを作成するための[選択を]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/)チェックする！
{% endalert %}

### リキッド`if` ステートメントを使用する

カタログ項目を使って条件文を作ることができる。例えば、キャンペーンで特定のアイテムが選択されたときに、特定のメッセージを表示させることができる。

そのためには、リキッド`if` ：

{% raw %}
```liquid
{% catalog_items Test-list 1234 %}
{% if {{items[0].first-item}} == true %}
Do this
{% else %}
Do that
{% endif %}
```
{% endraw %}

`if` ステートメントを使用する前に、カタログ名を宣言しなければならない。上の例では、`Test-list` がカタログ名である。

#### ユースケース:リキッド`if` スニペット

このシナリオでは、カスタム属性`venue_name` の文字数が10文字以上か10文字未満かで、異なるメッセージが表示される。`venue_name` が`blank` の場合、何も表示されない。

{% raw %}
```liquid
{% catalog_selection_items venue-list venue_selection %} 
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters. 
{% elsif items[0].venue_name.size < 10 %}
Message if the venue name's size is less than 10 characters. 
{% else %} 
{% abort_message(no venue_name) %} 
{% endif %}
```
{% endraw %}

なお、このシナリオでは`catalog_items` の代わりに`catalog_selection_items` を使用している。これは、`venue-list` がカタログ名、`venue_selection` が[選択項目であり、選択項目から]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/)項目を引っ張っているからである。 

### 画像を使用する {#using-images}

また、カタログの画像を参照してメッセージに使用することもできる。そのためには、画像のリキッドフィールドで`catalogs` タグと`item` オブジェクトを使う。

例えば、「テイルズ」のプロモーション・メッセージに「ゲーム」カタログの`image_link` を追加するには、「**カタログ項目**」フィールドに`id` を、「**表示する情報」**フィールドに`image_link` を選択する。これにより、以下のリキッドタグが画像フィールドに追加される：

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![コンテンツカードコンポーザーで、画像フィールドにカタログのリキッドタグが使用されている。][3]

リキッドがレンダリングされるとこうなる：

![カタログのリキッドタグをレンダリングしたコンテンツカードの例。][4]{: style="max-width:50%" }

### カタログ項目をテンプレート化する

また、テンプレート化を使って、カスタム属性に基づいてカタログ項目を動的に引き出すこともできる。たとえば、あるユーザーがカスタム属性`wishlist` （カタログのゲームIDの配列）を持っているとする。

```json
{
    "attributes": [
        {
            "external_id": "user_id",
            "wishlist": ["1234", "1235"]
        }
    ]
}
```

リキッドテンプレートを使えば、ウィッシュリストのIDを動的に引き出し、メッセージの中で使うことができる。そのためには、\[変数][10] をカスタム属性に割り当て、**パーソナライゼーションの追加**モーダルを使用して、配列から特定のアイテムを取り出す。

{% alert tip %}
配列は`1` ではなく`0` から始まることを忘れないでほしい。
{% endalert %}

例えば、「テイルズ」（カタログに掲載されている、ユーザーが欲しいと思っている商品）がセール中であることをユーザーに知らせるには、メッセージ・コンポーザーに次のように追加すればいい：

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now, for just {{ items[0].price }}!
```
{% endraw %}

以下のように表示される：
> たった7.49ドルで、今すぐ『テイルズ』を手に入れよう！

テンプレート化により、各ユーザーのカスタム属性、イベントプロパティ、その他のテンプレート化可能なフィールドに基づいて、各ユーザーに異なるカタログ項目をレンダリングすることができる。

### CSVをアップロードする

追加する新しいカタログ項目や更新するカタログ項目のCSVをアップロードできる。アイテムのリストを削除するには、アイテムIDのCSVをアップロードして削除する。

### 液体の使用

また、リキッドロジックのカタログを手作業で組み合わせることもできる。ただし、存在しないIDを入力しても、Brazeはオブジェクトのないitems配列を返すことに注意。配列のサイズをチェックしたり、`if` ステートメントを使用して配列が空の場合を考慮するなど、エラー処理を含めることを推奨する。

{% alert note %}
リキッドは現在、カタログ内で使用することはできない。リキッドパーソナライゼーションがカタログのセル内にリストされている場合、ダイナミック値はレンダリングされず、実際のリキッドのみが表示される。
{% endalert %}

増大するデータと情報を管理するために、[カタログ・エンドポイントを]({{site.baseurl}}/api/endpoints/catalogs/)活用することができる。これには、カタログ項目を作成、編集、削除する機能と、カタログ項目の詳細を一覧表示する機能が含まれる。

例えば、[Create catalogsエンドポイントを]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)使用してカタログを作成することができる。より多くのカタログを構築すると、[List catalogsエンドポイントを]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)使用して、ワークスペース内のカタログのリストを返すこともできる。

カタログを管理するだけでなく、非同期エンドポイントや同期エンドポイントを使ってカタログ項目を管理することもできる。これには、カタログ項目の編集と削除、およびカタログ項目の詳細の一覧表示機能が含まれる。例えば、個々のカタログ項目を編集したい場合、[`/catalogs/catalog_name/items/item_id` エンドポイントを]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)使うことができる。

## カタログの階層 {#tiers}

以下の表は、カタログの無料版とプロ版の違いを説明したものである：

| エリア                                  | 無料版                                                                                                                                            | カタログ・プロ                                                                                                                                            |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CSVファイル・サイズ                         | 企業全体ですべてのCSVファイルを合わせて100MBまで                                                                                        | 1つのCSVファイルで最大2GBまで                                                                                                                   |
| アイテム値の文字数制限       | 1つの値は5,000文字まで。例えば、`description` というフィールドがあった場合、フィールド内の最大文字数は5,000文字である。 | 1つの値は5,000文字まで。例えば、`description` というフィールドがあった場合、フィールド内の最大文字数は5,000文字である。 |
| 項目カラム名の文字数制限 | 250文字まで                                                                                                                                    | 250文字まで                                                                                                                                    |
| セレクション                            | カタログ1冊につき最大30セレクション                                                                                                                         | カタログ1冊につき最大30セレクション                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### カタログ保管

{% alert important %}
Brazeのダッシュボードに表示されるパッケージの権利は、視覚的な目的のために最も近い単位に丸められている。カタログストレージのアップグレードを依頼するには、Brazeのアカウントマネージャーに連絡する。
{% endalert %}

#### 無料版

無料版カタログの保存サイズは100MBまで。100MB以下であればアイテムは無制限だ。セレクションは収納に貢献する。セレクションが複雑であればあるほど、より多くのストレージを占有することになる。

#### カタログ・プロ

企業レベルでは、カタログProの最大ストレージはカタログ・データのサイズに基づいている。ストレージサイズのオプションは以下の通りである：5GB、10GB、15GBのいずれか。なお、無料版のストレージ（100MB）は各プランに含まれている。

[1]: {% image_buster /assets/img_archive/catalog_CSV_upload.png %}
[3]: {% image_buster /assets/img_archive/catalog_image_link1.png %}
[4]: {% image_buster /assets/img_archive/catalog_image_link2.png %}
[5]: {% image_buster /assets/img_archive/catalog_CSV_example.png %}
[7]: {% image_buster /assets/img_archive/create_catalog_option.png %}
[9]: {% image_buster /assets/img_archive/catalog_data_type.png %}
[11]: {% image_buster /assets/img_archive/catalog_new_name.png %}
[12]: {% image_buster /assets/img_archive/add_catalog_fields.png %}
[13]: {% image_buster /assets/img_archive/add_catalog_items.png %}
[14]: {% image_buster /assets/img_archive/in_browser_catalog.png %}
[10]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables
