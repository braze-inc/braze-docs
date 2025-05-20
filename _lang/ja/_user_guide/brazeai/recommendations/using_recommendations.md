---
nav_title: アイテムの推奨事項の使用
article_title: メッセージングでの項目の推奨事項の使用
description: "この記事では、メッセージで項目の推奨事項を使用する方法について説明します。"
page_order: 20
---

# メッセージングでの項目の推奨事項の使用

> おすすめがトレーニングされたら、Liquid を使用して、おすすめ項目を取り出してメッセージに表示できます。ここでのキーは、`product_recommendation` Liquid オブジェクトで直接作業しています。この記事では、`product_recommendation` Liquid オブジェクトについて説明し、その知識を実践するためのチュートリアルを提供します。

{% alert tip %}
この記事では、Liquidオブジェクトの構文について詳しく説明します。ただし、[ 事前にフォーマットされた変数]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables) を挿入し、テンプレート化されたテキストフィールドの右上にある**Add Personalization** モーダルをデフォルトで使用できます。
{% endalert %}

Braze でAI アイテムの推奨事項を使用するための追加のガイダンスについては、Braze Learning [AI でパーソナライズされたエクスペリエンスを作成するためのコース][1] をご覧ください。このコースでは、業界のユースケース、段階的な手順、AI 駆動型の推奨事項を含むアプリ内メッセージを作成するための追加のユースケースについて説明します。

## 推奨オブジェクトの構造

`product_recommendation` オブジェクトは、モデルによって推奨される一連のアイテムを表します。これは、オブジェクトの配列として構造化された、関連付けられたカタログから直接データを提供します。ここで、各オブジェクトは推奨項目を表します。

- **構造:**各アイテムは`items[index]` としてアクセスされます。ここで、インデックスは0 (最初のアイテムの場合) から始まり、後続のアイテムのインクリメントです。
- **カタログフィールド:**配列内の各項目には、カタログ内のフィールド(列) に対応するキーと値のペアが含まれます。たとえば、製品レコメンドの一般的なカタログ項目には、次のようなものがあります。
   - `name` または `title`
   - `price`
   - `image_url`

## Liquid タグ

`product_recommendation` オブジェクトには、動的に生成された製品レコメンドが含まれます。Liquid でこれらにアクセスするには、まずデータを変数に割り当ててから、メッセージで使用する必要があります。

### 推奨データの割り当て

常にassign タグで開始し、`product_recommendation` データをフェッチして変数に格納します。

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
```

{% endraw %}

- `RECOMMENDATION_NAME`:これを、Braze で作成したAI レコメンドの名前に置き換えます。
- `items`:推奨アイテム配列を格納する変数。

### 個々の項目へのアクセス

推奨データが割り当てられた後、配列インデックスとドット表記を使用して、特定の項目とそのフィールドを参照できます。

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
```

{% endraw %}

複数の項目を含めるには、各項目をインデックスで個別に参照します。`.name` および`.price` は、対応する項目をカタログからプルします。 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```

{% endraw %}

AI 推奨では、複数の製品が配列として返されます。`items[0]` は最初の項目、`items[1]` は2 番目の項目、というようになります。レコメンドが1 つの項目のみを返す場合、`items[1]` を参照しようとすると、空のフィールドが返されます。

## 画像を追加する

おすすめが使用するカタログにイメージリンクが含まれている場合は、メッセージ内のそれらのイメージを参照できます。 

{% tabs %}

{% tab ドラッグアンドドロップ%}
イメージフィールドを持つコンポーザーで、コンポーザーの各フィールドに以下のリキッドを追加します。

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

メールのドラッグアンドドロップエディタの場合:

1. メールにイメージブロックを追加します。
2. 画像ブロックを選択し(**Browse**ボタンではなく)、**画像プロパティ**パネルを開きます。
3. **Image with Liquid**をオンにします。 
4. Liquid スニペットを**Dynamic URL** フィールドに貼り付けます。

{% raw %}

```liquid
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
{{ items[0].IMAGE_URL_FIELD }}
```

{% endraw %}

![ドラッグアンドドロップエディタのイメージプロパティパネル]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:60%"}

{:start="5"}

5. プレビューおよびテストメールにプレースホルダイメージを含めるには、**イメージを選択** を押してメディアライブラリからプレースホルダイメージを追加するか、イメージがホストされているURL を入力します。

{% endtab %}

{% tab HTML %}

HTML イメージ参照の場合、イメージ`src` 属性をカタログのイメージURL フィールドに設定します。製品名や説明など、別のフィールドをalt テキストとして使用することもできます。

{% raw %}

```html
{% assign items = {{product_recommendation.${RECOMMENDATION_NAME}}} %}
<img src="{{ items[0].IMAGE_URL_FIELD }}" alt="{{ items[0].name }}">
```

{% endraw %}

{% endtab %}

{% endtabs %}

-  `MY_RECOMMENDATION_NAME` をお勧めの名前に置き換えます
- `IMAGE_URL_FIELD` を、イメージURL を含むカタログ内のフィールドの名前に置き換えます。


## チュートリアル: 放棄されたカートメールを作成する

このチュートリアルでは、Braze AI アイテムの推奨を使用して、ユーザーの好みや動作に基づいて製品を推奨するダイナミックメールを作成する方法について説明します。 

たとえば、あなたが衣料品のオンライン小売業者「Flash&Thread」のマーケターだとしましょう。商品をカートに入れたままにしていた顧客を再び引き込み、追加の商品をアップセルしたいとします。目的は、放棄されたアイテムとパーソナライズされたおすすめを表示するメールを作成することです。

### ステップ1:カタログの準備

推奨事項はカタログから項目を取得します。カタログの作成の手順に従います。カタログに次のフィールドが含まれていることを確認します。

| フィールド | データタイプ | 説明 |
| --- | --- | --- |
| id | string | カタログ内の各アイテムの一意の識別子 |
| 名前 | string | 「ストライプド・ニット・スウェーター」のような製品名。 |
| 価格 | 数値 | 製品価格(" 49.99" など)。 |
| image_url | string | 製品イメージを指すURL。HTTPS で保護されている必要があります。イメージがメディアライブラリにホストされている場合は、アセットの上にマウスポインタを置いてURL をコピーします。 |
| カテゴリ | string | 製品カテゴリは、"Sweaters"または"Accessories."などです。 |
| 色 | string | "Navy/Grey.&quot など、製品を説明する色です。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


#### カタログ例

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table class="tg">
  <tr>
    <th>id</th>
    <th>名前</th>
    <th>価格</th>
    <th>image_url</th>
    <th>カテゴリ</th>
    <th>色</th>
  </tr>
  <tr>
    <td>1001</td>
    <td>ストライプのニットセーター</td>
    <td>49.99</td>
    <td>https://{{media_library}}/images/67a41294f5eac400685ce908/original.png?1738805908</td>
    <td>セーター</td>
    <td>ネイビー/グレイ</td>
  </tr>
  <tr>
    <td>1002</td>
    <td>カスタムヨットクラブシューズ</td>
    <td>79.99</td>
    <td>https://{{media_library}}/images/67a4136fe5a7660068bbe046/original.png?1738806127</td>
    <td>履物</td>
    <td>ネイビー</td>
  </tr>
  <tr>
    <td>1003</td>
    <td>ワークシューズに戻る</td>
    <td>89.99</td>
    <td>https://{{media_library}}/images/67a41370f542c1006798c26e/original.png?1738806128</td>
    <td>履物</td>
    <td>ピンク/ゴールド</td>
  </tr>
  <tr>
    <td>1004</td>
    <td>夏の終わりの帽子</td>
    <td>29.99</td>
    <td>https://{{media_library}}/images/67a4136fbf6f620068511b67/original.png?1738806127</td>
    <td>付属品</td>
    <td>白い花</td>
  </tr>
</table>


### ステップ2: おすすめを設定する

1. カタログから、**推奨事項の作成**を選択します。
2. [AI アイテムの作成推奨事項][3]の手順に従います。 
3. 推奨タイプについては、**AI Personalized** を選択します。
4. 作成したカタログを使用して、推奨事項をトレーニングします。これにはしばらく時間がかかる場合があります。トレーニングが完了すると、電子メールが送信されます。

### ステップ 3:電子メールを作成する

レコメンデーションのトレーニングが完了したら、それをメッセージングに使用できます。

1. ドラッグアンドドロップエディタでメールを作成します。
2. メッセージ本文で、カタログから推奨をプルインする場所にイメージブロックを追加します。 
3. 画像ブロックを選択し、**Image properties**パネルの**Image with Liquid**をオンにします。 
4. このリキッドスニペットを「動的URL」フィールドに貼り付けます。


{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].image_url }}
```

{% endraw %}

{: start="5"}

5. 画像の下に段落ブロックを追加します。ここでは、製品名とサポートする詳細を追加します。 
6. 次のリキッドスニペットをブロックに貼り付けます。これにより、カタログから最初のおすすめの名前、カテゴリ、色、および価格が取得され、別の行として追加されます。 

{% raw %}

```liquid
{% assign items = {{product_recommendation.${abandoned_cart}}} %}
{{ items[0].name }}
{{ items[0].category }}
{{ items[0].color }}
${{ items[0].price }}
```

{% endraw %}

{: start="7"}

7. 両方のスニペットの場合、`abandoned_cart` をBraze の推奨名に置き換えます。
8. 項目フィールド名(`{{ items[0].field_name }}`) がカタログ内の列名と一致することをダブルチェックします。
9. ブロックを繰り返すたびに配列を1つずつ増やして、カタログから次の推奨項目を引き込みます。たとえば、配列は`{{ items[0].name }}` で始まるため、次の項目は`{{ items[1].name }}` になります。

### ステップ4:メッセージをプレビューする

メッセージが実際のユーザに対してどのように表示されるかを確認するには:

1. エディタの**Preview & Test** タブに移動します。
2. ドロップダウンから [**ランダムユーザー**] を選択します。
3. **Get Random User**を選択すると、ユーザーをオーディエンスからフェッチし、メールがデータとともにどのように表示されるかをプレビューします。

プレビューは、選択したユーザーが推奨に関連付けられた必要な属性またはイベントデータを持っている限り、AI 推奨を含むLiquid を完全にレンダリングします。

推奨事項がプレビューに表示されない場合は、次を確認します。

- ユーザが、推奨モデルをトレーニングした関連する製品またはイベントとやり取りした
- レコメンド自体は正常にトレーニングされました
- 液体コードは正しい推奨事項とフィールドを正しく参照しています



[1]: https://learning.braze.com/ai-item-recommendations-use-case/1996254
[2]: {% image_buster /assets/img/image_with_liquid.png %}
[3]: {{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations#creating-an-ai-item-recommendation