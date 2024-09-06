---
nav_title: Liquid
article_title: Liquid
page_order: 0
layout: dev_guide
search_rank: 3
guide_top_header: "液体タグを使用したカスタマイズ"
guide_top_text: "Braze は、指定されたユーザーの値を自動的にメッセージに置き換えます。中括弧の2組の内側に式を置き、補間値を使用していることをBrazeに通知します。これらの括弧内では、置換するユーザーの数値は、先頭にドル記号を付けた括弧で囲む必要があります。<br><br>Liquidの詳細については、ガイド付きの<b><a href='https://learning.braze.com/path/dynamic-personalization-with-liquid'>Liquid</a></b>Braze 学習 パスでダイナミックパーソナライゼーションをご覧ください!"
description: "このランディングページでは、サポートされているパーソナライゼーション タグs、フィルターs、設定 デフォルトバリューなど、リキッドのすべてを網羅しています。"

guide_featured_title: "セクションの記事"
guide_featured_list:
- name: 液体の使用
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/using_liquid/
  image: /assets/img/braze_icons/beaker-02.svg
- name: サポートされているカスタマイズタグ
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
  image: /assets/img/braze_icons/tag-01.svg
- name: 演算子
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/operators/
  image: /assets/img/braze_icons/code-02.svg
- name: フィルター
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/filters/
  image: /assets/img/braze_icons/flag-02.svg
- name: 詳細フィルタ
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/
  image: /assets/img/braze_icons/settings-01.svg
- name: デフォルト値の設定
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
  image: /assets/img/braze_icons/table.svg
- name: 条件付きメッセージロジック
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
  image: /assets/img/braze_icons/columns-01.svg
- name: メッセージの中止
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: 液体使用例
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/
  image: /assets/img/braze_icons/list.svg
- name: よくある質問
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/faq/
  image: /assets/img/braze_icons/annotation-question.svg
  
---

## 液体について

> Liquidは、Shopifyが開発し、ルビーで書かれた開封ソースのテンプレート語です。Brazeでは、リキッドを使用してユーザーのプロファイルからデータをメッセージにテンプレートします。 

たとえば、整数データタイプのユーザープロファイルからカスタム属性を取得し、その値を最も近い整数に丸めることができます。リキッドのシンタックスと使用方法については、[**対応パーソナライゼーション タグs**][1]を参照してください。

リキッドテンプレーティング言語は、オブジェクト、タグs、およびフィルターs の使用をサポートします。

- [**オブジェクト**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)を使用すると、メッセージにパーソナライズされた 属性sを挿入できます。
- [**タグ**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を使用すると、メッセージングにデータを挿入し、アウトライン条件が満たされている場合に条件ロジックを使用してメッセージを送信できます。たとえば、タグsを使用して、"if"文などのインテリジェントロジックをキャンペーンsに含めることができます。
- [**フィルタ**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) では、パーソナライズされた 属性s とダイナミックなの内容を再フォーマットできます。たとえば、*2016-09-07 08:43:50 UTC* などのタイムスタンプを、*September 7, 2016* などの日付に変換できます。

{% alert warning %}
Brazeは現在、Shopify社のリキッドの100%を支持しておらず、当社のドキュメントで概説しようとした特定の部分のみを支持しています。エラーの危険を減らすため、またはサポートされていない液体を使用するために、すべてのメッセージを液体でテストしてから送信することを強くお勧めします。
{% endalert %}

### Liquid 5

Braze は、**Shopify** からのLiquid 5 までのLiquid をサポートします。リキッドインプリメンテーションでは、シンタックスパーソナライゼーション タグタイプと空白コントロールがサポートされます。タグの詳細については、[構文タグs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#syntax-tags)を参照してください。

次の新しい配列と演算フィルターは、メッセージングの構築時にリキッドで使用できます。
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

定義については、[Filters]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/)の記事を参照してください。

### 流動更新s

各Liquid エレメントはカラーに対応しており、Liquid エディターでLiquid を一目で区別できます。

![]({% image_buster /assets/img/liquid_color_code.png %})

また、パーソナライズされたを作成する際に、カスタム属性s、属性の名前などにプレディケーティブリキッドを活用することもできます。

![]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}


## 知っておくべき用語

これらの用語は、サポートレベルに基づいて、[**Shopifyのドキュメント**](https://shopify.github.io/liquid/basics/introduction/)から再解釈されます。

{% raw %}

| 用語 | 定義 | 例 |  
|---|---|---|
| Liquid | Shopify によって作成され、ルビーで書かれた、一般的に使用される、顧客に面したテンプレート。ダイナミックなの内容を読み込む/プルするために使用されます。 | `{{${first_name}}}` ユーザーの名をメッセージに挿入します。 |
| オブジェクト | 変数のデノテーションと、メッセージ内のコンテンツを表示する場所をLiquid に伝える目的の変数名の場所。 | `{{${city}}}` ユーザーの都市を伝言メモに挿入します。 |
| 条件付きロジックタグ | タグはロジックを作成し、メッセージ内容の流れをコントロールします。Braze では、条件付きロジックタグを使用して、事前定義された特定の条件に基づいて、メッセージに例外やバリエーションを作成します。 | ```{% if ${language} == 'en' %}``` ユーザーが"English"を指定した場合、指定された方法でメッセージをトリガーします。 |
| フィルター | 液体オブジェクトの出力を変更、狭め、または再フォーマットするために使用します。多くの場合、数学演算を作成するために使用されます。 | ```{{"Big Sale" | upcase}}``` "Big Sale"という単語が、メッセージの中でear as "BIG SALE"をアプリします。 |
| 演算子 | メッセージで使用され、ユーザーが受信するメッセージに影響を与える可能性のある依存関係または基準を作成します。 | ユーザーが、`{% custom_attribute.${Total_Revenue} > 0%}` のメッセージタグで定義された条件を満たしている場合、メッセージを受信します。設定されていない場合は、設定した内容に応じて、別の指定されたメッセージが受信されます(または受信されません)。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endraw %}

<br>

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
