---
nav_title: Liquid の使用
article_title: Liquid のユースケースと概要
page_order: 0
description: "このリファレンス記事では、一般的な Liquid のユースケースの概要と、メッセージングに Liquid タグを含める方法について説明します。"
search_rank: 2
---

# [![Braze ラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}Liquid の使用

> この記事では、さまざまなユーザー属性を使用して、メッセージングにダイナミックな個人情報を挿入する方法を紹介する。

Liquid は、Shopify が開発した Ruby で書かれているオープンソースのテンプレート言語です。Brazeでこれを使えば、ユーザープロファイルのデータをメッセージングに取り込んだり、そのデータをカスタマイズしたりすることができる。例えば、ユーザーのサブスクリプションアニバーサリーの日付に基づいて異なるオファーを送信するなど、条件付きメッセージを作成するためにLiquidタグを使用することができる。さらに、フィルターを使用してデータを操作できます。例えばユーザーの登録日をタイムスタンプから「January 15, 2022」のような読みやすい形式にフォーマットできます。Liquid の構文とその機能の詳細については、「[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)」を参照してください。

## 仕組み

リキッドタグはメッセージのプレースホルダーとして機能し、ユーザーのアカウントから同意した情報を取り込み、パーソナライゼーションと適切なメッセージングを可能にする。

次のブロックでは、ユーザーの名を表示する Liquid タグと、ユーザーが名を登録していない場合のデフォルトタグの両方が使用されていることがわかります。

{% raw %}
```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```
{% endraw %}

Janet Doe という名前のユーザーには、次のいずれかの方法でメッセージが表示されます。

```
Hi Janet, thanks for using the App!
```

または。。。

```
Hi Valued User, thanks for using the App!
```

## 代用可能な値

次の項目の値が利用できる場合、メッセージ内で値に置き換えることができます。

- [基本的なユーザー情報]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) (`first_name`、`last_name`、`email_address` など)。
- [カスタム属性]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)
    - [階層化カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#liquid-templating)
- [カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- [最近使用したデバイスの情報]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information)
- [ターゲットデバイス情報]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information)

また、Braze の[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)を使用して、Web サーバーから直接コンテンツを取得することもできます。

{% alert important %}
Brazeは現在、ShopifyのLiquid 5までのLiquidをサポートしている。
{% endalert %}

## Liquid の使用

[Liquid のタグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を使用して、メッセージに親しみやすいタッチを加えて、メッセージの品質を高めることができます。 

### Liquid 構文

Liquid は特定の構造 (構文) に従います。ダイナミックなパーソナライゼーションを作成する際には、これを念頭に置く必要があります。ここで、いくつかの基本的なルールを覚えておこう：

1. **Braze では直線引用符を使用する:**曲線引用符 (**' '**) と直線引用符 (**' '**) には違いがあります。Braze の Liquid では直線引用符 (**' '**) を使用してください。特定のテキストエディターからコピーして貼り付けると、曲線引用符が表示されることがあります。これが、Liquid で問題を引き起こす可能性があります。Brazeのダッシュボードに直接見積もりを入力するのであれば、問題ないだろう！
2. **中括弧はペアで使用する:**中括弧には開き括弧と閉じ括弧の両方 **{ }** が必ず必要です。必ず中括弧を使うこと！
3. **ステートメントが対になっている場合：**それぞれの `if` について、`if` ステートメントが終了したことを示す `endif` が必要です。

#### デフォルト属性とカスタム属性

{% raw %}

メッセージに `{{${first_name}}}` を含めると、メッセージの送信時にユーザーの名 (ユーザープロファイルから取得) に置き換えられます。他のデフォルトユーザー属性でも同じフォーマットを使うことができる。

カスタム属性の値を使いたい場合は、変数に名前空間 "custom_attribute "を追加しなければならない。例えば、「zip code」というカスタム属性を使用するには、メッセージに `{{custom_attribute.${zip code}}}` を含めます。

### タグの挿入

どのメッセージでも、`{{` を2つ入力することでタグを挿入することができる。このタグを入力すると、自動補完機能が作動し、入力した内容が更新され続ける。入力中に表示されるオプションから変数を選択することもできる。

カスタムタグを使用している場合は、そのタグをコピーして好きなメッセージに貼り付けることができる。

{% endraw %}

{% alert note %}

メールメッセージにLiquidを使う場合は、必ずそうすること：

1. クラシック・エディターではなく、HTMLエディターを使って挿入する。クラシックエディターでは、Liquid がプレーンテキストとして解析される可能性があります。例えば、Liquid はユーザーの名でテンプレート化する代わりに、{% raw %}`Hi {{ ${first_name} }}, thanks for using our service!`{% endraw %} として解析します。
2. リキッドコードは、`<body>` タグ内にのみ配置する。このタグの外側に置くと、納品時にレンダリングに一貫性がなくなる可能性がある。

{% endalert %}

### あらかじめフォーマットされた変数を挿入する

テンプレート化されたテキストフィールドの付近にある**パーソナライゼーション追加**モーダルから、事前にデフォルト値でフォーマットされた変数を挿入できます。

![パーソナライゼーションの挿入を選択すると表示されるパーソナライゼーションの追加モーダル。このモーダルには、[パーソナライゼーションタイプ]、[属性]、[デフォルト値 (オプション)] のフィールドがあり、Liquid 構文のプレビューが表示される]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

モーダルにより、カーソルがあった位置に、指定したデフォルト値をもつ Liquid が挿入されます。挿入位置は [プレビュー] ボックスでも指定でき、挿入位置の前後のテキストが表示されます。テキストブロックがハイライトされている場合、ハイライトされたテキストは置き換えられる。

![パーソナライゼーション追加モーダルの GIF。この GIF は、ユーザーがデフォルト値として「fellow traveler」を挿入すると、モーダルが作成画面で強調表示されているテキスト「name」が Liquid スニペットに置き換えられ様子を示す。]({% image_buster /assets/img_archive/insert_var_shot.gif %})

### 変数への代入

{% raw %}
Liquidのいくつかの操作では、操作したい値を変数として格納する必要がある。これは、Liquid ステートメントに複数の属性、イベントプロパティ、またはフィルターが含まれている場合に多く見られます。

例えば、2つのカスタムデータの整数を足し合わせたいとしよう。 

#### 不正確なLiquidの例

以下を使用することはできません。

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

このLiquidが機能しないのは、1行で複数の属性を参照することができないからだ。数学関数が実行される前に、これらの値の少なくとも1つに変数を代入する必要がある。カスタム属性を2つ追加するには、2行のリキッドが必要になる。1つはカスタム属性を変数に代入すること、もう1つは追加を実行することだ。

#### 正しいLiquidの例

以下を使用できます。

```liquid
{% assign value_one = {{custom_attribute.${one}}} %}
{% assign result = value_one | plus: {{custom_attribute.${two}}} %}
```

#### チュートリアル: 変数を使用してバランスを計算する

ユーザーのギフトカード残高と報酬残高を足して、ユーザーの現在の残高を計算しましょう。

まず、`assign` タグを使って、`current_rewards_balance` のカスタム属性を "balance "という言葉に置き換える。つまり、操作できる `balance` という名前の新しい変数が得られました。

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

次に、`plus` フィルターを使用して、各ユーザーのギフトカード残高と、`{{balance}}` で示される報酬残高を加算します。

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
すべてのメッセージに同じ変数を割り当てていることに気づいているか？`assign` タグを何度も書き出す代わりに、そのタグをコンテンツブロックとして保存し、メッセージの先頭に置くことができます。

1. [コンテンツブロックの作成]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block)を行います。
2. コンテンツブロックに名前をつける（スペースや特殊文字は使わない）。
3. ページ下部の [**編集**] を選択します。
4. `assign` タグを入力します。

コンテンツ・ブロックがメッセージの先頭にある限り、変数がオブジェクトとしてメッセージに挿入されるたびに、選択したカスタム属性を参照することになる！
{% endalert %}

