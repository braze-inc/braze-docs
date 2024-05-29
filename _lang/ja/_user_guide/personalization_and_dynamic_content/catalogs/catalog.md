---
nav_title: カタログの作成
article_title: カタログの作成
alias: "/catalogs/"
page_order: 1
description: "この参考記事では、Liquidを通じてBrazeキャンペーンの非ユーザーデータを参照するカタログを作成して使用する方法について説明します。"
---

# カタログの作成

> [カタログを使用すると、Liquidを通じてBrazeキャンペーンの非ユーザーデータを参照できます。]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) 

カタログを作成するには、非ユーザーデータの CSV ファイルを Braze にインポートする必要があります。これにより、その情報にアクセスしてメッセージを充実させることができます。カタログにはあらゆる種類のデータを取り込むことができます。このデータは通常、eコマースビジネスの商品情報や教育機関向けのコース情報など、会社の何らかのメタデータです。

カタログの一般的な使用例には、次のようなものがあります。

- 製品
- サービス
- 食べ物
- 近日開催予定のイベント
- ミュージック
- パッケージ

この情報をインポートすると、Liquidからカスタム属性やカスタムイベントプロパティにアクセスするのと同じ方法で、メッセージからアクセスできるようになります。

## CSV ファイルの準備

カタログを作成する前に、希望するカタログ作成方法がアップロードである場合は、必ずCSVファイルを用意してください。 

CSV ファイルを作成するときは、次のガイドラインに注意してください。CSV ファイルの最初の列はのヘッダーである必要があり`id`、`id`各項目は一意である必要があります。その他の列名はすべて一意でなければなりません。さらに、カタログ CSV ファイルには次の制限が適用されます。

- 最大 500 フィールド (列)
- フィールド (列) 名の最大文字数は 250 文字
- 社内のすべての CSV ファイルを組み合わせて最大 100 MB (無料)
- CSV ファイルの最大サイズは 2 GB (プロ)
- 5,000 文字の最大フィールド値 (セル)
- およびヘッダー値には、文字、数字、ハイフン、`id`アンダースコアのみ

次のステップでCSVファイルを正常にアップロードするには、CSVファイルをUTF-8形式でエンコードしていることを確認してください。また、CSV ファイル内のすべてのテキストを小文字にすることをお勧めします。

{% alert note %}
CSV ファイルを保存するためのスペースがもっと必要ですか?カタログのアップグレードの詳細については、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

## メソッドを選択する

カタログを作成するには、**[データ設定] > [****カタログ**] に移動します。

{% alert note %}
[古いナビゲーションを使用している場合は、[]({{site.baseurl}}/navigation)**データ**] に [**カタログ**] が表示されます。
{% endalert %}

「**新規カタログを作成**」をクリックし、「**CSV をアップロード**」または「**ブラウザで作成**」を選択します。

### メソッド 1:CSV をアップロード

1. ファイルをアップロードゾーンにドラッグアンドドロップするか、[**CSV をアップロード**] をクリックしてファイルを選択します。<br>![][1]{: style="max-width:80%;"}<br><br>
2. 列ごとに、ブーリアン、数値、文字列、または時間のいずれかのデータタイプを選択します。
<br> ![][9]{: style="max-width:80%;"}<br><br>
3. カタログに名前を付けてください。カタログの次の要件に注意してください。 name:
- 一意でなければなりません。
- 最大 250 文字まで
- 数字、文字、ハイフン、およびアンダースコアのみを使用できます<br><br>
4. (オプション) カタログの説明を追加します。
5. [**プロセスカタログ**] をクリックしてカタログを作成します。

{% alert note %}
このデータタイプは、カタログを設定した後は編集できません。
{% endalert %}

カタログ名にはテンプレートを使用できないことに注意してください。たとえば、カタログ名として以下を使用することはできません。そうしないと、呼び出しは失敗します。
{% raw %}
```liquid
{% catalog_items custom_attribute.${catalog} item1, item2 %}
```
{% endraw %}

{% alert important %}
[レベルを超えると](#tiers)、CSV ファイルが拒否されることがあります。
{% endalert %}

ブラウザでカタログを作成することを選択した後に、CSV ファイルを更新することもできます。[**カタログを更新] > [CSV をアップロード**] をクリックし、カタログ内の商品を更新、追加、削除するかどうかを選択します。

### メソッド 2:ブラウザで作成

1. カタログの名前を入力します。カタログの次の要件に留意してください。 name:
- 一意でなければなりません。
- 最大 250 文字まで
- 数字、文字、ハイフン、およびアンダースコアのみを使用できます <br> ![][14]{: style="max-width:80%;"}<br><br>
2. (オプション) カタログの説明を入力します。
3. カタログのリストページから作成したカタログを選択して、**カタログを更新します**。
4. [**カタログを更新] > [フィールドを追加**] をクリックしてフィールドを追加します。次に、**フィールド名を入力し**、ドロップダウンを使用してデータタイプを選択します。必要に応じて繰り返します。<br> ![][12]{: style="max-width:50%;"}<br><br>
5. [**カタログの更新] >** [アイテムの追加] をクリックして、以前に追加したフィールドに基づいて情報を入力してカタログにアイテムを追加します。次に、[**商品を保存] または [**保存して別の商品を追加****] をクリックして、商品の追加を続行します。<br> ![][13]{: style="max-width:50%;"}

ブラウザでカタログの作成を選択した後に CSV ファイルをアップロードすることもできます。

{% alert note %}
Braze はダッシュボードのタイムスタンプに基づいて時間値を処理します。たとえば、列の値が「03」の場合/13/2024" and your time zone is the Pacific Time Zone, this time would be imported to Braze as "Mar 12, 2024, 5:00 PM".
{% endalert %}

#### カタログ例

このチュートリアルでは、2 つのゲームとその価格、イメージリンクを掲載したカタログを使用します。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">ID</th>
    <th class="tg-0pky">タイトル</th>
    <th class="tg-0pky">価格</th>
    <th class="tg-0pky">image_link</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">1234</td>
    <td class="tg-0pky">テイルズ</td>
    <td class="tg-0pky">7.49 米ドル</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
  <tr>
    <td class="tg-0pky">1235</td>
    <td class="tg-0pky">再生</td>
    <td class="tg-0pky">22.49 米ドル</td>
    <td class="tg-0pky">https://picsum.photos/200</td>
  </tr>
</tbody>
</table>

この例では、CSV ファイルをアップロードしてカタログを作成します。、、`image_link`およびのデータ型は`id``title``price`、それぞれ文字列、文字列、数値、および文字列です。 

{% alert note %}
このデータタイプは、カタログを設定した後は編集できません。
{% endalert %}

![][9]{: style="max-width:85%;"}

次に、このカタログに「games\_catalog」という名前を付けて、**プロセスカタログボタンをクリックします**。その後、Braze はカタログの作成前にカタログにエラーがないか確認します。

![][11]{: style="max-width:85%;"}

カタログが作成された後は、この名前を編集することはできませんのでご注意ください。カタログを削除し、同じカタログ名を使用して更新バージョンを再アップロードできます。 

## メッセージでのカタログの使用

カタログは、Liquidがサポートされているドラッグアンドドロップエディターのどこでも含め、すべてのメッセージングチャネルで使用できます。

### ステップ 1:パーソナライゼーションタイプを追加 {#step-one-personalization}

**選択したメッセージコンポーザーで、<i class="fas fa-plus-circle"></i>プラスアイコンをクリックして「**パーソナライゼーションを追加」モーダルを開き、パーソナライゼーションタイプの**「**カタログアイテム**」を選択します。**次に、**カタログ名を選択します**。前の例を使用して、「ゲーム」カタログを選択します。

![][2]

次のLiquidプレビューがすぐに表示されます。

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### ステップ 2:カタログアイテムを選択します

次は、カタログアイテムを追加しましょう！ドロップダウンを使用して、表示するカタログ項目と情報を選択します。この情報は、カタログの生成に使用したアップロードされた CSV ファイルの列に対応します。

たとえば、テイルズゲームのタイトルと価格を参照するには、カタログアイテムとして `id` for Tales (1234) を選択し、`title`表示される情報をリクエストします。`price`

{% raw %}
\`\`\`liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
\`\`\`
{% endraw %}

これは以下のようにレンダリングされます。

> たったの7.49ドルでテイルズを手に入れよう！

## API 経由のカタログ

[Catalogs エンドポイントを活用して]({{site.baseurl}}/api/endpoints/catalogs/)、増え続けるデータや情報を管理できます。

### カタログの管理

[カタログの作成エンドポイントを使用してカタログを作成できます]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/)。

さらにカタログを作成するときに、[List catalogs エンドポイントを使用してワークスペース内のカタログのリストを返すこともできます]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/)。

### カタログアイテムの管理

カタログの管理に加えて、非同期エンドポイントと同期エンドポイントを使用してカタログアイテムを管理することもできます。これには、カタログアイテムを編集および削除したり、カタログアイテムの詳細を一覧表示したりする機能が含まれます。 

たとえば、個々のカタログアイテムを編集する場合は、[`/catalogs/catalog_name/items/item_id`エンドポイントを使用できます]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/)。

## その他のユースケース

### 複数のアイテム

1つのメッセージで1つのアイテムだけに制限されるわけではありません！「**パーソナライゼーションを追加**」モーダルを使用して、追加のカタログ項目と情報を挿入して表示するだけです。追加できるカタログ項目は 3 つまでであることに注意してください。 

**この例では、「テイルズ」、「テスラグラード」、「アカラトゥス」の 3 `id` つのゲームのうち「**カタログアイテム**」を追加し、「表示する情報」を選択します。`title`**

![][6]{: style="max-width:70%" }

Liquidの周りにテキストを追加することで、メッセージをさらにパーソナライズできます。

{% raw %}
```liquid
Get the ultimate trio {% catalog_items games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

これは以下のように戻ります。

> テイルズ、テスラグラード、アカラトゥスの究極のトリオを今すぐ手に入れよう！

{% alert tip %}
[選択項目をチェックしてデータのグループを作成し]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/)、よりパーソナライズされたメッセージを作成しましょう！
{% endalert %}

### `if`リキッドステートメントの使用

カタログ項目を使用して条件文を作成できます。たとえば、キャンペーンで特定のアイテムが選択されたときに、特定のメッセージが表示されるようにすることができます。

そのためには、次のような形式の Liquid `if` ステートメントを使用します。

{% raw %}
```liquid
{% catalog_items Test-list %}
{% if {{items[0].first-item}} == true %}
Do this
{% else %}
Do that
{% endif %}
```
{% endraw %}

`if`ステートメントを使用する前にカタログリストを宣言する必要があることに注意してください。上の例では、`Test-list`がカタログリストです。

#### `if`リキッドスニペットの例

この例では、`venue_name`カスタム属性が 10 文字以上または 10 文字未満の場合、異なるメッセージが表示されます。`venue_name`の場合`blank`、何も表示されません。

{% raw %}
```liquid
{% catalog_selection_items item-list selections %} 
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters. 
{% elsif items[0].venue_name.size < 10 %}
Message if the venue name's size is less than 10 characters. 
{% else %} 
{% abort_message(no venue_name) %} 
{% endif %}
```
{% endraw %}

### 画像を使う {#using-images}

また、カタログ内の画像を参照してメッセージングに使用することもできます。そのためには、画像の Liquid `catalogs` `item` フィールドにあるタグとオブジェクトを使用します。

たとえば、ゲームカタログのをテイルズのプロモーションメッセージに追加するには、「**カタログアイテム**」フィールドと `image_link`「**表示する情報**」フィールドに「」を選択します。`image_link` `id`これにより、次の Liquid タグが画像に追加されます。 field:

{% raw %}
\`\`\`liquid
{% catalog_items Games 1234 %}

{{ items[0].image\_link }}
\`\`\`
{% endraw %}

![画像フィールドでカタログ Liquid タグが使用されているコンテンツカードコンポーザー。] [3]

Liquidをレンダリングすると、次のようになります。

![カタログ Liquid タグがレンダリングされたコンテンツカードの例] [4]{: style="max-width:50%" }

### カタログアイテムのテンプレート作成

テンプレートを使用して、カスタム属性に基づいてカタログアイテムを動的に取得することもできます。たとえば、あるユーザーがカタログのゲーム ID `wishlist` の配列を含むカスタム属性を持っているとします。

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

Liquidテンプレートを使用すると、ウィッシュリストIDを動的に引き出して、メッセージで使用できます。そのためには、カスタム属性に [変数を割り当て] [10]、次に [**パーソナライゼーションの追加**] モーダルを使用して配列から特定の項目を取得します。

{% alert tip %}
配列はで始まるが`0`、では始まらないことを覚えておいてください`1`。
{% endalert %}

たとえば、テイルズ（カタログで希望していた商品）がセール中であることをユーザーに知らせるには、メッセージコンポーザーに以下を追加します。

{% raw %}
\`\`\`liquid
{% assign wishlist = {{custom\_attribute.${wishlist}}}%}
{% catalog\_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now, for just {{ items[0].price }}!
\`\`\`
{% endraw %}

以下のように表示されます。
> たったの7.49ドルで今すぐテイルズを手に入れよう！

テンプレートを使用すると、個々のカスタム属性、イベントプロパティ、またはその他のテンプレート可能なフィールドに基づいて、ユーザーごとに異なるカタログ項目をレンダリングできます。

### CSV をアップロードする

追加する新しいカタログ項目または更新するカタログ項目の CSV をアップロードできます。アイテムのリストを削除するには、アイテムIDのCSVをアップロードして削除できます。

### 液体を使用する

Liquid ロジックのカタログを手動でつなぎ合わせることもできます。ただし、存在しない ID を入力した場合でも、Braze はオブジェクトを含まないアイテム配列を返すことに注意してください。配列のサイズをチェックしたり、`if`空の配列ケースに対応するステートメントを使用したりするなどのエラー処理を含めることをお勧めします。

## カタログの管理

カタログをさらに作成するにつれて、[カタログエンドポイントを活用して]({{site.baseurl}}/api/endpoints/catalogs/)、増え続けるデータや情報を管理できます。これには、カタログアイテムの作成、編集、削除、およびカタログアイテムの詳細を一覧表示する機能が含まれます。

## カタログ層 {#tiers}

次の表は、無料版とプロ版のカタログの違いをまとめたものです。

| エリア | 無料版 | カタログプロ |
|---|---|---|
| CSV ファイルのサイズ | 会社全体ですべての CSV ファイルを組み合わせた場合は最大 100 MB | 単一の CSV ファイルの場合は最大 2 GB |
| 項目値の文字数制限 | 1 つの値には最大 5,000 文字まで入力できます。たとえば、ラベルが付いたフィールドがある場合`description`、フィールド内の最大文字数は5,000文字です。| 1つの値には最大5,000文字です。たとえば、ラベルが付いたフィールドがある場合`description`、フィールド内の最大文字数は 5,000 文字です。|
| アイテム列名の文字数制限 | 最大 250 文字 | 最大 250 文字 |
| セレクション | カタログあたり最大30セレクション | カタログあたり最大30セレクション |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### カタログストレージ

{% alert important %}
Braze ダッシュボードに表示されるパッケージ利用権は、視覚的に見やすいように最も近い単位に四捨五入されています。ただし、購入したすべての利用権は引き続きご利用いただけます。カタログストレージのアップグレードをリクエストするには、Braze アカウントマネージャーにお問い合わせください。
{% endalert %}

#### 無料版

無料版のカタログのストレージサイズは最大100 MBです。100 MB 未満であれば、アイテム数に制限はありません。選択内容はストレージに貢献します。選択内容が複雑になればなるほど、使用するストレージも多くなります。

#### カタログプロ

企業レベルでは、Catalogs Proの最大ストレージはカタログデータのサイズによって異なります。5 ギガバイト、10 ギガバイト、または 15 ギガバイト無料版のストレージ（100 MB）は、これらの各プランに含まれていることに注意してください。

[1]: {% image_buster /assets/img_archive/catalog_CSV_upload.png %}
[2]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[3]: {% image_buster /assets/img_archive/catalog_image_link1.png %}
[4]: {% image_buster /assets/img_archive/catalog_image_link2.png %}
[5]: {% image_buster /assets/img_archive/catalog_CSV_example.png %}
[6]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}
[7]: {% image_buster /assets/img_archive/create_catalog_option.png %}
[9]: {% image_buster /assets/img_archive/catalog_data_type.png %}
[11]: {% image_buster /assets/img_archive/catalog_new_name.png %}
[12]: {% image_buster /assets/img_archive/add_catalog_fields.png %}
[13]: {% image_buster /assets/img_archive/add_catalog_items.png %}
[14]: {% image_buster /assets/img_archive/in_browser_catalog.png %}
[10]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables
