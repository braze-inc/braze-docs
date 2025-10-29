---
nav_title: Liquid
article_title: Liquid
page_order: 0
layout: dev_guide
alias: /liquid/
search_rank: 3
guide_top_header: "液体タグを使用したカスタマイズ"
guide_top_text: "Braze は、指定されたユーザーの値を自動的にメッセージに置き換えます。中括弧の2組の内側に式を置き、補間値を使用していることをBrazeに通知します。これらの括弧内では、置換するユーザー値は、先頭にドル記号を付けた追加の括弧で囲む必要があります。<br><br>Liquid の詳細については、Braze Learning のガイド付きの「<b><a href='https://learning.braze.com/path/dynamic-personalization-with-liquid'>Liquid のダイナミックパーソナライゼーション</a></b>」の Braze 学習パスをご覧ください。"
description: "このランディングページでは、サポートされているパーソナライゼーションタグ、フィルター、デフォルト値の設定など、Liquid のすべてを網羅しています。"

guide_featured_title: "セクションの記事"
guide_featured_list:
- name: Liquid の使用
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
- name: Liquid のユースケース
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/
  image: /assets/img/braze_icons/list.svg
- name: チュートリアル
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/tutorials/
  image: /assets/img/braze_icons/book-open-01.svg
- name: よくある質問
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/faq/
  image: /assets/img/braze_icons/annotation-question.svg
  
---

## Liquid について

> Liquid は、Shopify が開発した Ruby で書かれているオープンソースのテンプレート言語です。Braze では、Liquid を使用してユーザーのプロファイルからデータをメッセージにテンプレート化します。 

例えば、整数データ型のユーザープロファイルからカスタム属性を取得し、その値を最も近い整数に丸めることができます。Liquid の構文と使用方法については、[**サポートされているパーソナライゼーションタグ**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を参照してください。

リキッドテンプレーティング言語は、オブジェクト、タグs、およびフィルターs の使用をサポートします。

- [**オブジェクト**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)を使用すると、メッセージにパーソナライズされた 属性sを挿入できます。
- [**タグ**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)を使用すると、メッセージングにデータを挿入し、条件付きロジックを使用して、特定の条件が満たされた場合にメッセージを送信できます。例えば、タグを使用して、「if」文などのインテリジェントロジックをキャンペーンに含めることができます。
- [**フィルター**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/)では、パーソナライズされた属性とダイナミックコンテンツを再フォーマットできます。たとえば、[`date` filter]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/#date-filter) を使用して、*2016-09-07 08:43:50 UTC* などのタイムスタンプを、*September 7, 2016* などの日付に変換できます。

{% alert warning %}
Brazeは現在、ShopifyのLiquidの100%をサポートしておらず、私たちのドキュメントで概要を説明しようとした特定の部分のみをサポートしています。すべてのメッセージを送信する前にLiquidを使用してテストすることを強くお勧めします。これにより、エラーのリスクやサポートされていないLiquidの使用を減らすことができます。
{% endalert %}

### Liquid 5のサポート

Braze は、**Shopify** からのLiquid 5 までのLiquid をサポートします。Liquid の実装では、構文パーソナライゼーションタグのタイプと空白コントロールがサポートされます。タグの詳細については、[構文タグs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#syntax-tags)を参照してください。

次の新しい配列と演算フィルターは、メッセージングの構築時に Liquid で使用することができます。
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

定義については、[フィルタ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/)を参照してください。

### Liquid の更新

#### カラーラベル

各 Liquid 要素は色分けされているので、Liquid エディターではこれらを一目で区別することができます。

\![]({% image_buster /assets/img/liquid_color_code.png %})

#### 入力予測 Liquid

また、パーソナライズされたメッセージを作成する際に、カスタム属性や属性名などに入力予測 Liquid を利用することもできます。

\![]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## 知っておくべき用語

これらの用語は、サポートレベルに基づいて、[**Shopifyのドキュメント**](https://shopify.github.io/liquid/basics/introduction/)から再解釈されます。

{% raw %}

| 用語 | 定義 | 例 |  
|---|---|---|
| Liquid | Shopifyによって作成され、動的コンテンツのロードとプルに使用されるRubyで記述された、一般的に使用される顧客向けテンプレート言語。 | `{{${first_name}}}`は、ユーザーの名をメッセージに挿入します。 |
| オブジェクト | 変数のデノテーションと、メッセージ内のコンテンツを表示する場所をLiquid に伝える目的の変数名の場所。 | `{{${city}}}` は、ユーザーの都市をメッセージに挿入します。 |
| 条件付きロジックタグ | ロジックを作成し、メッセージコンテンツのフローを制御するために使用します。Braze では、条件付きロジックタグを使用して、事前定義された特定の条件に基づいて、メッセージに例外やバリエーションを作成します。 | ```{% if ${language} == 'en' %}``` は、ユーザーが自分の言語として英語を指定した場合、指定の方法でメッセージをトリガーします。 |
| フィルター | Liquid オブジェクトの出力を変更、狭め、または再フォーマットするために使用します。これは、数学演算を作成するためによく使用されます。 | ```{{"Big Sale" | upcase}}``` は、メッセージの中で「Big Sale」という言葉を「BIG SALE」として表示します。 |
| 演算子 | メッセージで使用され、ユーザーが受信するメッセージに影響を与える可能性のある依存関係または基準を作成します。 | ユーザーが、`{% custom_attribute.${Total_Revenue} > 0%}` のメッセージタグで定義された条件を満たしている場合、メッセージを受信します。そうでない場合は、設定した内容に応じて、別の指定されたメッセージが受信されます (または受信されません)。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endraw %}

<br>

