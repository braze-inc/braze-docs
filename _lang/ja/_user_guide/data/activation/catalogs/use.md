---
nav_title: カタログの使用
article_title: カタログを使う
page_order: 1.5
description: "この参照記事では、Liquid を通して Braze のキャンペーンで非ユーザーデータを参照するためにカタログを使用する方法について説明します。"
---

# カタログの使用

> カタログを作成した後、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) を使用して、Braze キャンペーンの非ユーザーデータを参照できます。Liquid がサポートされているドラッグ＆ドロップエディター内の任意の場所を含む、すべてのメッセージングチャネルでカタログを使用できます。

## メッセージでカタログを使う

### ステップ 1: パーソナライゼーションタイプを追加する {#step-one-personalization}

任意のメッセージ作成画面で、プラスアイコン<i class="fas fa-plus-circle"></i>を選択して**「パーソナライゼーションを追加」**モーダルを開き、**パーソナライゼーションの種類**として**「カタログアイテム」**を選択します。次に、カタログ名を選択します。先ほどの例を使って、「Games」カタログを選択します。

![]({% image_buster /assets/img_archive/use_catalog_personalization.png %})

以下の Liquid プレビューがすぐに表示されます。

{% raw %}
```liquid
{% catalog_items Games %}
```
{% endraw %}

### ステップ 2: カタログアイテムを選択する

次に、カタログアイテムを追加します。ドロップダウンを使って、カタログアイテムと表示する情報を選択します。この情報は、カタログを生成するために使用された、アップロード済みの CSV ファイルの列に対応しています。

例えば、Tales ゲームのタイトルと価格を参照するには、カタログアイテムとして Tales (1234) の `id` を選択し、表示する情報として `title` と `price` をリクエストします。

{% raw %}
```liquid
{% catalog_items Games 1234 %}
 
Get {{ items[0].title }} for just {{ items[0].price }}!
```
{% endraw %}

これは次のように表示されます。

> 「Tales」をわずか 7.49 ドルでゲットしよう!

## カタログのエクスポート

ダッシュボードからカタログをエクスポートするには、次の 2 つの方法があります。 

- **カタログ**セクションのカタログ行にカーソルを合わせます。次に、**Export catalog** ボタンを選択します。
- カタログを選択します。次に、カタログの**プレビュー**タブで **Export catalog** ボタンを選択します。

エクスポートを開始すると、CSV ファイルをダウンロードするためのメールが届きます。このファイルの取得期限は最大 4 時間です。

## その他のユースケース

### 複数のアイテム

メッセージで使用できるアイテムは 1 つだけではありません。**「パーソナライゼーションを追加」**モーダルを使って、一度に最大 3 つのカタログアイテムを追加できます。さらに追加するには、作成画面で再度**「パーソナライゼーションを追加」**を選択し、追加のカタログアイテムや表示する情報を選びます。

この例では、Tales、Teslagrad、Acaratus の 3 つのゲームの `id` を**カタログアイテム**に追加し、**表示する情報**として `title` を選択します。

![]({% image_buster /assets/img_archive/catalog_multiple_items.png %}){: style="max-width:70%" }

Liquid の周りにテキストを追加することで、メッセージをさらにパーソナライズできます。

{% raw %}
```liquid
Get the ultimate trio {% catalog_items Games 1234 1235 1236 %}
{{ items[0].title }}, {{ items[1].title }}, and {{ items[2].title }} today!
```
{% endraw %}

これは以下のように返されます。

```Get the ultimate trio Tales, Teslagrad, and Acaratus today!```

{% alert tip %}
Check out [selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) to create groups of data for more personalized messaging!
{% endalert %}

### Using Liquid `if` statements

You can use catalog items to create conditional statements. For example, you can trigger a certain message to display when a specific item is selected in your campaign. You must declare the catalog (and, if applicable, the selection) before referencing `items` in an `if` statement.

#### With catalog items

{% raw %}
```liquid
{% catalog_items Games 1234 %}
{% if items[0].on_sale == true %}
  {{ items[0].title }} is on sale! Get it for {{ items[0].price }}.
{% else %}
  Check out {{ items[0].title }} at full price.
{% endif %}
```
{% endraw %}

この例では、`catalog_items` タグが `Games` カタログからアイテム `1234` を取得し、`if` ステートメントが `on_sale` フィールドをチェックして異なるメッセージを表示します。

#### カタログセレクションの場合

{% raw %}
```liquid
{% catalog_selection_items item-list selections %} 
{% if items[0].venue_name.size > 10 %}
Message if the venue name's size is more than 10 characters. 
{% elsif items[0].venue_name.size <= 10 %}
Message if the venue name's size is 10 characters or fewer. 
{% else %} 
{% abort_message('no venue_name') %} 
{% endif %}
```
{% endraw %}

この例では、`venue_name` フィールドの文字数が 10 文字より多いか少ないかによって、異なるメッセージが表示されます。`venue_name` が空白の場合、メッセージは中止されます。

{% alert tip %}
Liquid の構文エラーを避けるには、メッセージ作成画面の **+** プラスボタンを選択して、カタログの Liquid タグを自動的に挿入してください。
{% endalert %}

### 画像の使用 {#using-images}

カタログ内の画像を参照してメッセージングで使用することもできます。そのためには、画像の Liquid フィールドで `catalogs` タグと `item` オブジェクトを使用します。

例えば、Games カタログの `image_link` を「Tales」のプロモーションメッセージに追加するには、**カタログアイテム**フィールドで `id` を選択し、**表示する情報**フィールドで `image_link` を選択します。これにより、以下の Liquid タグが画像フィールドに追加されます。

{% raw %}
```liquid
{% catalog_items Games 1234 %}

{{ items[0].image_link }}
```
{% endraw %}

![画像フィールドで使用されるカタログの Liquid タグを含むコンテンツカード作成画面。]({% image_buster /assets/img_archive/catalog_image_link1.png %})

Liquid がレンダリングされると、次のように表示されます。

![カタログの Liquid タグをレンダリングしたコンテンツカードの例。]({% image_buster /assets/img_archive/catalog_image_link2.png %}){: style="max-width:50%" }

### カタログアイテムのテンプレート化

テンプレート化を使って、カスタム属性に基づいてカタログアイテムをダイナミックに取得することもできます。例えば、あるユーザーがカスタム属性 `wishlist`（カタログのゲーム ID の配列）を持っているとします。

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
カタログ内の JSON オブジェクトは、API を介してのみ取り込まれます。CSV ファイルを使用して JSON オブジェクトをアップロードすることはできません。
{% endalert %}

Liquid テンプレートを使用することで、ウィッシュリストの ID をダイナミックに取り出し、メッセージで使用できます。そのためには、カスタム属性に[変数を割り当て]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables)、**パーソナライゼーションの追加**モーダルを使用して、配列から特定のアイテムを取り出します。カタログアイテム ID として参照する変数は、`{{result}}` のように中かっこで囲む必要があります。

{% alert tip %}
配列は `1` ではなく `0` から始まることを忘れないでください。
{% endalert %}

例えば、「Tales」（ウィッシュリストに含まれているカタログのアイテム）がセール中であることをユーザーに通知するために、メッセージ作成画面で以下を追加できます。

{% raw %}
```liquid
{% assign wishlist = {{custom_attribute.${wishlist}}}%}
{% catalog_items Games {{ wishlist[0] }} %}

Get {{ items[0].title }} now for {{ items[0].price }}!
```
{% endraw %}

以下のように表示されます。
> 今すぐ Tales を 7.49 ドルでゲットしよう!

テンプレート化により、各ユーザーのカスタム属性、イベントプロパティ、その他のテンプレート化可能なフィールドに基づいて、ユーザーごとに異なるカタログアイテムをレンダリングできます。

### CSV のアップロード

追加する新しいカタログアイテムや、更新するカタログアイテムの CSV をアップロードできます。アイテムのリストを削除するには、アイテム ID の CSV をアップロードして削除できます。

### Liquid の使用

Liquid ロジックを使用してカタログを手動で組み立てることもできます。ただし、存在しない ID を入力しても、Braze はオブジェクトのない items 配列を返すことに注意してください。配列のサイズをチェックしたり、`if` ステートメントを使用して配列が空の場合を考慮するなど、エラー処理を含めることをお勧めします。

#### Liquid を含むカタログアイテムのテンプレート化

[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content)と同様に、Liquid タグで `:rerender` フラグを使用してカタログアイテムの Liquid コンテンツをレンダリングする必要があります。`:rerender` フラグは 1 レベルの深さまでしか適用されないことに注意してください。つまり、ネストされた Liquid タグ呼び出しには適用されません。

カタログアイテムにユーザープロファイルフィールド（Liquid パーソナライゼーションタグ内）が含まれている場合は、Liquid を適切にレンダリングするために、テンプレート化の前にメッセージ内でこれらの値を Liquid で事前に定義する必要があります。`:rerender` フラグが指定されていない場合、生の Liquid コンテンツがそのままレンダリングされます。

例えば、「Messages」という名前のカタログに、この Liquid を含むアイテムがあるとします。

![]({% image_buster /assets/img_archive/catalog_liquid_templating.png %}){: style="max-width:80%;"}

以下の Liquid コンテンツをレンダリングするには:

{% raw %}
```liquid
Hi ${first_name},

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
カタログの Liquid タグは、カタログ内で再帰的に使用することはできません。
{% endalert %}


[1]: {% image_buster /assets/img_archive/use_catalog_personalization.png %}
[2]: {% image_buster /assets/img_archive/catalog_multiple_items.png %}