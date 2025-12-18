---
nav_title: 推奨事項の使用
article_title: メッセージングでの項目の推奨事項の使用
description: "この記事では、メッセージで項目の推奨事項を使用する方法について説明します。"
page_order: 1.2
---

# メッセージングでの項目の推奨事項の使用

> おすすめがトレーニングされたら、Liquid を使用して、`product_recommendation` Liquid オブジェクトを直接操作することで、メッセージ内のおすすめ項目をフェッチして表示できます。

{% alert tip %}
ステップバイステップのウォークスルーについては、以下のBraze Learning コースをご覧ください。[Crafting Personalized Experiences with AI](https://learning.braze.com/ai-item-recommendations-use-case/1996254)。
{% endalert %}

## 前提条件

メッセージングで推奨事項を使用する前に、[推奨エンジンを作成し、トレーニングする必要があります]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/)。トレーニングにかかる時間は10分～36時間です。トレーニングが終了したとき、またはエラーが発生したときにメールが届きます。

## メッセージングでのレコメンデーションの使用

### ステップ1:Liquid コードの追加

おすすめのトレーニングが終了したら、Liquidでメッセージをカスタマイズして、そのカタログに最も人気のある製品を挿入できます。

{% tabs local %}
{% tab pre-formatted code %}
![パーソナライゼーションタイプとしてアイテムの推奨を使用した [パーソナライゼーションを追加] モーダル。]({% image_buster /assets/img/add_personalization.png %}){: style="max-width:30%;float:right;margin-left:15px;"}

メッセージコンポーザーの**パーソナライゼーションを追加** セクションからLiquid を生成できます。

1. パーソナライゼーションをサポートするメッセージ作成画面では、[<i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="パーソナライゼーションを追加"></i>] を選択してパーソナライゼーションウィンドウを開きます。
2. [**パーソナライゼーションタイプ**] で、[**項目のレコメンデーション**] を選択します。
3. [**項目のレコメンデーション名**] で、先に作成したおすすめを選択します。
4. [**予測アイテム数**] で、挿入する上位商品の数を入力します。たとえば、購入数の多い上位 3 つのアイテムを表示できます。
5. [**表示する情報**] で、カタログのどのフィールドを各アイテムに含めるかを選択します。各アイテムのこれらのフィールドの値は、このおすすめに関連付けられたカタログから取得されます。
6. [**コピー**] アイコンを選択し、メッセージ内の必要な場所に Liquid を貼り付けます。
{% endtab %}

{% tab custom code %}
カタログの`product_recommendation` オブジェクトを参照することで、カスタムのLiquid コードを記述できます。これには、そのカタログの動的に生成されたすべての製品レコメンドデータが含まれ、オブジェクトの配列として構造化されます。各オブジェクトは、推奨アイテムを表します。

|仕様|詳細|
|-------------|-------|
|**構造**|各アイテムは`items[index]` としてアクセスされます。ここで、インデックスは0 (最初のアイテムの場合) から始まり、後続のアイテムのインクリメントです。|
|**カタログフィールド**|配列内の各項目には、カタログ内のフィールド(列) に対応するキーと値のペアが含まれます。たとえば、製品レコメンドの一般的なカタログ項目には、次のようなものがあります。<br>- `name`または `title`<br>- `price`<br>- `image_url`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

`assign` タグを使用して`product_recommendation` データをフェッチし、変数に割り当てます。

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
```
{% endraw %}

次のように置き換えます。

|placeholder|説明|
|-----------|-----------|
|`recommendation_name`|Braze で作成した AI レコメンデーションの名前。|
|`items`|推奨アイテム配列を格納する変数。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

次に、配列インデックスとドット表記を使用して、特定の項目とそのフィールドを参照します。

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
```
{% endraw %}

複数の項目を含めるには、各項目をインデックスで個別に参照します。`.name` および`.price` は、対応する項目をカタログからプルします。 

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].name }} for {{ items[0].price }}
{{ items[1].name }} for {{ items[1].price }}
{{ items[2].name }} for {{ items[2].price }}
```
{% endraw %}

AI 推奨では、複数の製品が配列として返されます。`items[0]` は最初の項目、`items[1]` は2 番目の項目、というようになります。レコメンドが1 つの項目のみを返す場合、`items[1]` を参照しようとすると、空のフィールドが返されます。
{% endtab %}
{% endtabs %}

### ステップ2:画像を参照する(オプション)

おすすめのカタログにイメージリンクが含まれている場合は、メッセージで参照できます。 

{% tabs %}
{% tab Drag-and-drop%}
メールのドラッグ＆ドロップエディターで、メールに画像ブロックを追加し、この画像ブロックを選択して [**画像のプロパティ**] を開きます。

![ドラッグアンドドロップエディタのイメージプロパティパネル]({% image_buster /assets/img/image_with_liquid.png %}){: style="max-width:45%"}

[**Liquid を含む画像**] を切り替え、[**ダイナミック URL**] フィールドに以下を追加します。

{% raw %}
```liquid
{% assign items = {{product_recommendation.${recommendation_name}}} %}
{{ items[0].image_url_field }}
```
{% endraw %}

次のように置き換えます。

|placeholder|説明|
|-----------|-----------|
|`recommendation_name`|お勧めの名前。|
|`image_url_field`|イメージURL を含むカタログ内のフィールドの名前。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

プレビューおよびテストメールにプレースホルダ画像を含めるには、**画像を選択**を選択し、メディアライブラリから画像を選択するか、ホスティングサイトから画像のURLを入力します。
{% endtab %}

{% tab HTML %}
HTML イメージ参照の場合、イメージ`src` 属性をカタログのイメージURL フィールドに設定します。製品名や説明など、別のフィールドをalt テキストとして使用することもできます。

{% raw %}
```html
{% assign items = {{product_recommendation.${recommendation_name}}} %}
<img src="{{ items[0].image_url_field }}" alt="{{ items[0].name }}">
```
{% endraw %}

次のように置き換えます。

|placeholder|説明|
|-----------|-----------|
|`recommendation_name`|お勧めの名前。|
|`image_url_field`|イメージURL を含むカタログ内のフィールドの名前。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}
