---
nav_title: カタログ sの使用
article_title: カタログを使う
page_order: 1.5
description: "この参考記事では、Liquidを通してBrazeのキャンペーンで非ユーザーデータを参照するためにカタログを使用する方法について説明する。"
---

# カタログ sの使用

> カタログを作成した後、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) を使用して、Braze キャンペーンの非ユーザーデータを参照できます。Liquidがサポートされているドラッグ・アンド・ドロップ・エディター内の任意の場所を含む、すべてのメッセージング・チャンネルでカタログを使用できる。

## メッセージでカタログを使う

### ステップ 1: パーソナライゼーションタイプを追加する {#step-one-personalization}

選択したメッセージコンポーザーで、<i class="fas fa-plus-circle"></i> プラスアイコンを選択して**パーソナライズの追加**モーダルを開き、**パーソナライズのタイプに** **カタログアイテムを**選択する。次に、**カタログ名**を選択します。先ほどの例を使って、「ゲーム」カタログを選択する。

![]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

以下の Liquid プレビューがすぐに表示されます。

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### ステップ 2: カタログ項目を選択する

ここではカタログアイテムを追加します。ドロップダウンを使って、カタログ項目と表示する情報を選択する。この情報は、カタログを生成するために使用される、アップロードされたCSVファイルの列に対応している。

例えば、Tales ゲームのタイトルと価格を参照するには、カタログアイテムとして Tales (1234) の `id` を選択し、表示される情報に対して `title` と `price` をリクエストします。

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

これは次のように表示される：

> 「Tales」をわずか 7.49 ドルでゲットしよう!

## カタログのエクスポート

ダッシュボードからカタログをエクスポートするには、次の2つの方法があります。 

- **Catalogs** セクションのカタログ行にカーソルを合わせます。次に、**Export catalog**ボタンを選択します。
- カタログを選択します。次に、カタログの**Preview**タブで**Export catalog**ボタンを選択します。

エクスポートを開始すると、CSV ファイルをダウンロードするための電子メールが送信されます。このファイルを取得するには最大 4 時間かかります。

## その他の使用例

### 複数の項目

1つのメッセージ内の1つの項目だけに限定されるわけではありません。**Add Personalization**モーダルを使用して、一度に最大3つのカタログアイテムを追加できます。メッセージにアイテムを追加するには、メッセージコンポーザーで**カスタマイズを追加**を選択し、表示する追加のカタログアイテムと情報を選択します。

この例では、Tales、Teslagrad、Acaratus の 3 つのゲームの `id` を**カタログアイテム**に追加し、[**表示する情報**] のために `title` を選択します。

![]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Liquid の周りにテキストを追加することで、メッセージをさらにパーソナライズできます。

{% raw %}
```liquid
Get the ultimate trio {% catalog_items games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

これは以下のように返される：

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
さらにパーソナライズされたメッセージングのために、データグループを作成するには、[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/)を参照してください。
{% endalert %}

### リキッド`if` ステートメントを使用する

カタログ項目を使って条件文を作ることができる。例えば、キャンペーンで特定の項目が選択されたときに、特定メッセージの表示をトリガーできます。

これを行うには、次の例のように、Liquid `if` ステートメントを使用します。

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

この例では、カスタム属性`venue_name` の文字数が10 文字を超えているか、10 文字未満である場合、異なるメッセージが表示されます。`venue_name` が `blank` の場合、何も表示されません。 

`if` ステートメントを使用する前に、カタログリストと、該当する場合はセレクションを宣言する必要があることに注意してください。この例では、`item-list` がカタログリストで、`selections` が選択名です。

### 画像の使用 {#using-images}

また、カタログ内の画像を参照してメッセージングで使用することもできます。そのためには、画像のリキッドフィールドで`catalogs` タグと`item` オブジェクトを使う。

例えば、Games カタログの `image_link` を「Tales」のプロモーションメッセージに追加するには、[**カタログ項目**] フィールドで `id` を選択し、[**表示する情報**] フィールドで `image_link` を選択します。これにより、以下のリキッドタグが画像フィールドに追加される：

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

!["画像 フィールドで使用するカタログリキッドタグ付きコンテンツカードコンポーザー。]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Liquid がレンダリングされると、次のように表示されます。

![カタログリキッドタグ付きコンテンツカードをレンダリングしました。]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

### カタログ項目をテンプレート化する

また、テンプレート化を使って、カスタム属性に基づいてカタログ項目を動的に引き出すこともできる。例えば、あるユーザーがカスタム属性`wishlist` （カタログのゲームIDの配列）を持っているとする。

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

{% alert note %}
カタログ内のJSONオブジェクトは、APIを介してのみ取り込まれます。CSV ファイルを使用してJSON オブジェクトをアップロードすることはできません。
{% endalert %}

Liquid テンプレートを使用することで、ウィッシュリストから ID をダイナミックに取り出し、メッセージで使用できます。そのためには、カスタム属性に[変数を割り当て]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables)、**パーソナライゼーションの追加**モーダルを使用して、配列から特定のアイテムを取り出す。カタログアイテム ID として参照する変数が適切に参照されるようにするため、`{{result}}` のように、変数を中かっこで囲む必要があります。

{% alert tip %}
配列は`1` ではなく`0` から始まることを忘れないでほしい。
{% endalert %}

例えば、「Tales」(ウィッシュリストに含まれている、御社カタログの項目) が販売中であることをユーザーに通知するために、メッセージ作成画面で以下を追加できます。

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now, for just {{ items[0].price }}!
```
{% endraw %}

以下のように表示される：
> 「Tales」をわずか 7.49 ドルで今すぐゲットしよう!

テンプレート化により、各ユーザーのカスタム属性、イベントプロパティ、その他のテンプレート化可能なフィールドに基づいて、各ユーザーに異なるカタログ項目をレンダリングすることができる。

### CSVをアップロードする

追加する新しいカタログ項目や、更新するカタログ項目の CSV をアップロードできます。アイテムのリストを削除するには、アイテムIDのCSVをアップロードして削除する。

### Liquid の使用

Liquid ロジック使用してカタログを手動で作成することもできます。ただし、存在しないIDを入力しても、Brazeはオブジェクトのないitems配列を返すことに注意。配列のサイズをチェックしたり、`if` ステートメントを使用して配列が空の場合を考慮するなど、エラー処理を含めることを推奨する。

{% alert note %}
現在、カタログ内で Liquid を使用することはできません。リキッドパーソナライゼーションがカタログのセル内にリストされている場合、ダイナミック値はレンダリングされず、実際のリキッドのみが表示される。
{% endalert %}

#### リキッドを含むカタログアイテムのテンプレート化

[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)と同様に、Liquid タグで `:rerender` フラグを使用してカタログアイテムの Liquid コンテンツをレンダリングする必要があります。`:rerender` フラグはレベル1の深さしかないことに注意してください。つまり、階層化 Liquid タグ 呼び出しには適用されません。

カタログアイテムにユーザープロファイルフィールド (Liquid パーソナライゼーションタグ内) が含まれている場合は、Liquid を適切にレンダリングするために、テンプレート作成の前にメッセージでこれらの値を Liquid で事前に定義する必要があります。`:rerender` フラグが指定されていない場合、生の Liquid コンテンツがレンダリングされます。

たとえば、「Messages」という名前のカタログに、この Liquid を含むアイテムがあるとします。

![]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

以下のリキッドコンテンツをレンダリングするには:

{% raw %}
```liquid
Hi ${first_name}

{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

次のように表示されます。

{% raw %}
```
Hi Peter,

Welcome to our store, Peter!
```
{% endraw %}

{% alert note %}
カタログリキッドタグは、カタログs 内で再帰的に使用することはできません。
{% endalert %}


[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}
