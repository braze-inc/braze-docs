---
nav_title: Transifex
article_title:Transifex
alias: /partners/transifex/
description:"この参考記事では、BrazeとローカライゼーションプラットフォームであるTransifexのパートナーシップについて概説している。" 翻訳をオートメーション化することで、チームは優れたカスタマーエクスペリエンスの提供に専念することができる。
page_type: partner
search_tag:Partner

---

# Transifex

> Transifexは、言語に関係なく、ユーザー群全体の強固なローカライゼーションを可能にする。

BrazeとTransifexの統合は、コネクテッドコンテンツを活用し、言語ベースの条件付き書式の行の代わりに、リソース文字列コレクションを引き出し、関連する翻訳をメッセージに含めることを可能にする。これにより、翻訳がオートメーション化され、チームは優れたカスタマーエクスペリエンスの提供に集中することができる。

{% alert important %}
2022年4月7日現在、Transifexはバージョン3への移行に伴い、APIのバージョン2および2.5を非推奨とした。<br><br>以下の統合手順は、バージョン3の更新を反映したものである。コネクテッド・コンテンツのコールを適宜更新する。
{% endalert %}

## 前提条件

| 必要条件| 説明|
| ---| ---|
|Transifexアカウント | このパートナーシップを利用するには[Transifexアカウントが](https://www.transifex.com/signin/)必要である。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Transifexの統合は、Transifexの[リソース翻訳APIを](https://developers.transifex.com/reference/get_resource-translations)使用する。以下のcURLで、自分のアカウントに翻訳に関連するコンテンツ値があるかどうかを確認できる。 

まず、Transifexアカウントにある`<ORGANIZATION_NAME>` 、`<PROJECT_NAME>` 、`<RESOURCE_NAME>` を入力する。次に、`<LANGUAGE>` を翻訳をフィルターしたい言語コードに、`<TRANSIFEX_BEARER_TOKEN>` をあなたのTransifex[ベアラートークンに](https://developers.transifex.com/reference/api-authentication)置き換える。

```
curl --request GET \
     --url 'https://rest.api.transifex.com/resource_translations?filter\[resource\]=o:<ORGANIZATION_NAME>:p:<PROJECT_NAME>:r:<RESOURCE_NAME>&filter\[language\]=l:<LANGUAGE>' \
     --header 'Accept: application/vnd.api+json' \
     --header 'Authorization: Bearer 1/c500429f7b89ff62b8015475ed68d90a2295302'
```

例えば、Transifexプロジェクトが`https://www.transifex.com/appboy-3/french2/french_translationspo/` にある場合、`project_name` は "french2"、`resource_name` は "french_translationspo "となる。

## コネクテッドコンテンツのメッセージ例

このコード例は、Transifexリソース翻訳APIとユーザーの`language` 属性を利用している。ニーズに応じて、文字列オブジェクトをループし、以下のLiquidを使用して関連するコンテンツを引き出すことができる：`{{strings.data[X].attributes.strings.other}}`.

{% raw %}
```
{% assign organization = "<ORGANIZATION_NAME>" %}
{% assign project = "<PROJECT_NAME>" %}
{% assign resource = "<RESOURCE_NAME>" %}

{% if {{${language}}} == "en" or {{${language}}} == "it" or {{${language}}} == "de" or {{${language}}} == "another_language_you_support"  %}
{% connected_content
     https://rest.api.transifex.com/resource_translations?filter[resource]=o:{{organization}}:p:{{project}}:r:{{resource}}&filter[language]=l:{{${language}}}
     :method GET
     :headers {
       "Authorization": "Bearer <TRANSIFEX_BEARER_TOKEN>"
  }
     :accept application/vnd.api+json
     :save strings
%}
{% endif %}

{% if {{strings}} != null and {{strings.data[0].attributes.strings.other}} != "" and {{${language}}} != null %}
  {{strings.data[0].attributes.strings.other}}
{% else %}
  {% abort_message('null or blank') %}
{% endif %}
```
{% endraw %}

[16]: [success@braze.com](mailto:success@braze.com)
[31]: https://docs.transifex.com/api/translation-strings