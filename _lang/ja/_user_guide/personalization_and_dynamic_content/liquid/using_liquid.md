---
nav_title: 液体の使用
article_title: 液体の使用例と概要
page_order: 0
description: "このリファレンス記事では、一般的な Liquid のユースケースの概要と、メッセージングに Liquid タグを含める方法を提供する。"
search_rank: 2
---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}液体を使用

{% raw %}

> メッセージングに個人情報を動的に挿入するために使用できる、さまざまなユーザー属性がある。

メッセージに以下のテキストを含める：`{{${first_name}}}`を含めると、メッセージ送信時にユーザーのファーストネーム（ユーザーのプロフィールから取得）が代入される。カスタム属性の値を使いたい場合は、変数に名前空間 "custom_attribute "を追加しなければならない。例えば、"zip code "というカスタム属性を使うには、メッセージに`{{custom_attribute.${zip code}}}` 。

以下の値は、メッセージに代入することができる：

- [基本ユーザー情報][1]（例えば、`first_name` 、`last_name` 、`email_address` ）。
- [カスタム属性][2]
- [カスタムイベントプロパティ][11]
- [最近使用されたデバイス情報][39]
- [ターゲット・デバイス情報][40]

また、Braze[Connected Contentを使って][9]ウェブサーバーから直接コンテンツを引き出すこともできる。
{% endraw %}

{% alert important %}
Brazeは現在、**ShopifyのLiquid 5までの**Liquidをサポートしている。
{% endalert %}

## 液体の使用

{% raw %}

[Liquidのタグが利用できる][1]ことを知れば、Liquidを使うことでメッセージのパーソナライゼーションを印象的な高みに引き上げることができる。リキッドタグはメッセージのプレースホルダーとして機能し、ユーザーのアカウントから同意した情報を取り込み、パーソナライゼーションと適切なメッセージングを可能にする。

次のブロックでは、ユーザーのファーストネームを呼び出すリキッドタグと、ユーザーがファーストネームを登録しない場合のデフォルトタグの二重の使い方を見ることができる。

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

ジャネット・ドウというユーザーには、メッセージは次のように表示される：

```
Hi Janet, thanks for using the App!
```

あるいは...

```
Hi Valued User, thanks for using the App!
```

### 液体構文

リキッドは特定の構造（シンタックス）に従っており、動的パーソナライゼーションを作成する際には、これを念頭に置く必要がある。ここで、いくつかの基本的なルールを覚えておこう：

1. **ブレイズではストレートクォートを使う：**カーリークオート（'**'）と**ストレートクオート（'**'）には**違いがある。BrazeのLiquidにはストレートクォート('**')を**使う。特定のテキストエディタからコピー＆ペーストするとき、カール引用符が表示されることがある。Brazeのダッシュボードに直接見積もりを入力するのであれば、問題ないだろう！
2. **ブラケットは2個1組である：**すべてのブラケットは、**{ }の**開閉両方が必要である。必ず中括弧を使うこと！
3. **ステートメントが対になっている場合：**`if` に対し、`if` ステートメントが終了したことを示す`endif` が必要である。

### タグを挿入する

どのメッセージでも、`{{` を2つ入力することでタグを挿入することができる。このタグを入力すると、自動補完機能が作動し、入力した内容が更新され続ける。入力中に表示されるオプションから変数を選択することもできる。

カスタムタグを使用している場合は、そのタグをコピーして好きなメッセージに貼り付けることができる。

{% endraw %}

{% alert note %}

メールメッセージにLiquidを使う場合は、必ずそうすること：

1. クラシック・エディターではなく、HTMLエディターを使って挿入する。クラシックエディターは、リキッドをプレーンテキストとして解析することができる。
2. リキッドコードは、`<body>` タグ内にのみ配置する。このタグの外側に置くと、納品時にレンダリングに一貫性がなくなる可能性がある。

{% endalert %}

{% raw %}


### フォーマット済み変数

テンプレート化されたテキスト・フィールドの右上にある "パーソナライゼーション属性の挿入 "モーダルによって、デフォルトであらかじめフォーマットされた変数を挿入することができる。

![BrazeでLiquidをサポートするテキストフィールドにパーソナライズ属性を挿入するための追加ボタン][44]{: style="max-width:70%;"}

モーダルは、カーソルがあった位置に、指定したデフォルト値でリキッドを挿入する。挿入位置はプレビュー・ボックスでも指定でき、プレビュー・ボックスには前後のテキストが表示される。テキストブロックがハイライトされている場合、ハイライトされたテキストは置き換えられる。

![パーソナライズの挿入をクリックした後に表示されるパーソナライズの追加モーダル。モーダルには、パーソナライズタイプ、属性、オプションのデフォルト値のフィールドがあり、リキッド構文のプレビューが表示される。][45]

{% endraw %}

### 変数を割り当てる

{% raw %}
Liquidのいくつかの操作では、操作したい値を変数として格納する必要がある。リキッドステートメントに複数のアトリビュート、イベントプロパティ、フィルターが含まれる場合、このようなケースになることが多い。

例えば、2つのカスタムデータの整数を足し合わせたいとしよう。単純に使うことはできない：

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

なぜなら、1行で複数の属性を参照することができないからだ。数学関数が実行される前に、これらの値の少なくとも1つに変数を代入する必要がある。カスタム属性を2つ追加するには、2行のリキッドが必要になる。1つはカスタム属性を変数に代入すること、もう1つは追加を実行することだ。

#### チュートリアルだ：変数を使用してバランスを計算する

ギフトカードの残高とリワードの残高を足して、ユーザーの現在の残高を計算してみよう：

まず、`assign` タグを使って、`current_rewards_balance` のカスタム属性を "balance "という言葉に置き換える。つまり、`balance` という変数ができたことになる。

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

次に、`plus` フィルタを使って、各ユーザーのギフトカード残高と、`{{balance}}` で示されるリワード残高を結合する。

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
すべてのメッセージに同じ変数を割り当てていることに気づいているか？`assign` タグを何度も書き出す代わりに、そのタグをコンテンツ・ブロックとして保存し、メッセージの先頭に置くことができる。

1. [コンテンツブロックを作成する]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block)。
2. コンテンツブロックに名前をつける（スペースや特殊文字は使わない）。
3. ページ下部の**Editを**クリックする。
4. `assign` タグを入力する。

コンテンツ・ブロックがメッセージの先頭にある限り、変数がオブジェクトとしてメッセージに挿入されるたびに、選択したカスタム属性を参照することになる！
{% endalert %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[9]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[39]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information
[40]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information
[44]: {% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}
[45]: {% image_buster /assets/img_archive/insert_var_shot.png %}
