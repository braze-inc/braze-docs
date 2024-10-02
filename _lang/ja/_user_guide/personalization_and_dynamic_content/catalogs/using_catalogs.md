---
nav_title: カタログを使う
article_title: カタログを使う
page_order: 1.5
description: "この参考記事では、Liquidを通してBrazeのキャンペーンで非ユーザーデータを参照するためにカタログを使用する方法について説明する。"
---

# メッセージでカタログを使う

> カタログを作成した後、[Liquidを通して]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid)Brazeキャンペーンで非ユーザーデータを参照できる。Liquidがサポートされているドラッグ・アンド・ドロップ・エディター内の任意の場所を含む、すべてのメッセージング・チャンネルでカタログを使用できる。

## ステップ 1:パーソナライゼーション・タイプを追加する {#step-one-personalization}

選択したメッセージコンポーザーで、<i class="fas fa-plus-circle"></i> プラスアイコンを選択して**パーソナライズの追加**モーダルを開き、**パーソナライズのタイプに** **カタログアイテムを**選択する。次に、**カタログ名を**選択する。先ほどの例を使って、「ゲーム」カタログを選択する。

![][1]

リキッドのプレビューはすぐに見ることができる：

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

## ステップ 2:カタログ項目を選択する

次に、カタログ項目を追加する番だ！ドロップダウンを使って、カタログ項目と表示する情報を選択する。この情報は、カタログを生成するために使用される、アップロードされたCSVファイルの列に対応している。

例えば、『テイルズ』ゲームのタイトルと価格を参照するには、カタログ項目として『テイルズ』の`id` （1234）を選択し、表示される情報に対して`title` 、`price` 。

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

これは次のように表示される：

> テイルズ』をわずか7.49ドルで手に入れよう！

## その他の使用例

### 複数の項目

1つのメッセージに含まれる項目は1つに限定されない！**パーソナライズの追加]**モーダルを使用して、表示する追加カタログ項目と情報を挿入するだけである。なお、追加できるカタログ項目は3つまでである。 

この例をチェックしてください。3つのゲーム、Tales、Teslagrad、Acaratusの`id`を**カタログ**アイテムに追加し、**表示する情報**のために`title`を選択します。

![][2]{: style="max-width:70%" }

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
{% catalog_items Test-list %}
{% if {{items[0].first-item}} == true %}
Do this
{% else %}
Do that
{% endif %}
```
{% endraw %}

カタログ・リストを宣言してから、`if` 。上の例では、`Test-list` がカタログ・リストである。

#### ユースケース:リキッド`if` スニペット

このシナリオでは、カスタム属性`venue_name` の文字数が10文字以上か10文字未満かで、異なるメッセージが表示される。`venue_name` が`blank` の場合、何も表示されない。

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


[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}
