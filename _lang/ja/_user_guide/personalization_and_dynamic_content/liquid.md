---
nav_title: Liquid
article_title: Liquid
page_order: 0
layout: dev_guide
search_rank: 3
guide_top_header: "Liquid タグを使用したパーソナライゼーション"
guide_top_text: "Braze は、特定のユーザーの値を自動的にメッセージに置き換えることができます。補間された値を使用することを Braze に通知するには、式を 2 組の中括弧内に入れます。これらの括弧内では、置換するユーザー値は、前にドル記号が付いた追加の括弧セットで囲む必要があります。<br><br>Liquid の詳細については、ガイド付きの <b><a href='https://learning.braze.com/path/dynamic-personalization-with-liquid'>Dynamic Personalization with Liquid</a></b> Braze 学習パスをご覧ください。"
description: "このランディング ページでは、サポートされているパーソナライズ タグ、フィルター、デフォルト値の設定など、Liquid に関するあらゆる情報を取り上げます。"

guide_featured_title: "セクション記事"
guide_featured_list:
- name: Using Liquid
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/using_liquid/
  fa_icon: fas fa-flask
- name: Supported Personalization Tags
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
  fa_icon: fas fa-tag
- name: Operators
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/operators/
  fa_icon: fas fa-code
- name: Filters
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/filters/
  fa_icon: fas fa-filter
- name: Advanced Filters
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/
  fa_icon: fas fa-cog
- name: Setting Default Values
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/
  fa_icon: fas fa-table
- name: Conditional Messaging Logic
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/
  fa_icon: fas fa-columns
- name: Aborting Messages
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/
  fa_icon: fas fa-undo
- name: Liquid Use Cases
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases/
  fa_icon: fas fa-list-ul
- name: Frequently Asked Questions
  link: /docs/user_guide/personalization_and_dynamic_content/liquid/faq/
  fa_icon: fas fa-question
  
---

## Liquidについて

> Liquid は、Shopify によって開発され、Ruby で記述されたオープンソースのテンプレート言語です。Braze では、Liquid を使用して、ユーザーのプロファイルのデータをメッセージにテンプレート化します。 

たとえば、整数データ型のカスタム属性をユーザー プロファイルから取得し、その値を最も近い整数に丸めることができます。Liquid の構文と使用方法の詳細については、[**「サポートされているパーソナライズ タグ」**][1]を参照してください。

Liquid テンプレート言語は、オブジェクト、タグ、フィルターの使用をサポートしています。

- [**オブジェクトを使用する**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) と、メッセージにパーソナライズされた属性を挿入できます。
- [**タグを使用すると**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) 、メッセージにデータを挿入し、条件付きロジックを使用してアウトラインの条件が満たされた場合にメッセージを送信できます。たとえば、タグを使用して、「if」ステートメントなどのインテリジェントなロジックをキャンペーンに含めることができます。
- [**フィルターを使用すると**]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) 、パーソナライズされた属性と動的コンテンツを再フォーマットできます。たとえば、*2016-09-07 08:43:50 UTC*などのタイムスタンプを、*September 7, 2016*などの日付に変換できます。

{% alert warning %}
Braze は現在、Shopify の Liquid を 100% サポートしているわけではなく、ドキュメントで概要を説明している特定の部分のみをサポートしています。エラーやサポートされていない Liquid の使用のリスクを軽減するために、メッセージを送信する前に Liquid を使用してすべてのメッセージをテストすることを強くお勧めします。
{% endalert %}

### Liquid 5の新機能

Braze は **、Shopify の Liquid 5**までの Liquid のサポートを更新しました。 

Liquid 実装では、構文のパーソナライズ タグ タイプと空白の制御がサポートされています。特定のタグの詳細については、 [構文タグ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#syntax-tags)を参照してください。

次の新しい配列フィルターと数式フィルターは、メッセージングを作成するときに Liquid で使用できます。
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

定義については、 [フィルターの]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/filters/) 記事を参照してください。

## 知っておくべき用語

これらの用語は、[**Shopify のドキュメント**](https://shopify.github.io/liquid/basics/introduction/) から当社のサポート レベルに基づいて再解釈されます。

{% raw %}

| 用語 | 定義 | 例 |  
|---|---|---|
| Liquid | Shopify によって作成され、Ruby で記述された、一般的に使用される顧客向けテンプレート言語。動的コンテンツの読み込み/取得に使用されます。 | `{{${first_name}}}` メッセージにユーザーのファーストネームを挿入します。 |
| オブジェクト | 変数の表記と、メッセージ内のコンテンツを表示する場所を Liquid に指示する目的の変数名の場所。 | `{{${city}}}` ユーザーの都市名をメッセージに挿入します。 |
| 条件付きロジック タグ | タグはロジックを作成し、メッセージ コンテンツのフローを制御します。Braze では、条件付きロジック タグを使用して、特定の定義済み基準に基づいてメッセージの例外とバリエーションを作成します。 | ```{% if ${language} == 'en' %}``` ユーザーが言語として「英語」を指定した場合、指定された方法でメッセージが送信されます。 |
| フィルター | Liquid オブジェクトの出力を変更、絞り込み、または再フォーマットするために使用されます。数学演算を作成するためによく使用されます。 | ```{{"Big Sale" | upcase}}``` メッセージ内で「Big Sale」という単語が「BIG SALE」と表示されます。 |
| 演算子 | メッセージ内で、ユーザーが受信するメッセージに影響を与える依存関係や条件を作成するために使用されます。 | ユーザーがタグ付きメッセージで定義された条件を満たしている場合 `{% custom_attribute.${Total_Revenue} > 0%}`、メッセージを受け取ります。そうでない場合は、設定内容に応じて、別の指定されたメッセージが送信されます (または送信されません)。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endraw %}

<br>

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
