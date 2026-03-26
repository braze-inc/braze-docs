---
nav_title: Transifex
article_title: Transifex
alias: /partners/transifex/
description: "この参考記事では、BrazeとTransifexのパートナーシップについて概説している。Transifexは、ローカリゼーション・プラットフォームであり、翻訳を自動化することで、チームを優れた顧客体験の提供に集中させることを可能にする。"
page_type: partner
search_tag: Partner

---

# Transifex

> [Transifex](https://www.transifex.com/) は、言語に関係なく、ユーザー群全体で堅牢なローカライゼーションを可能にします。

_この統合は Transifex によって管理されます。_

## 統合について

BrazeとTransifexインテグレーションでは、Connected Contentを使用して、リソース文字列コレクションをプルし、言語ベースの条件付き書式の行ではなく、関連する翻訳をメッセージに含めることができます。これにより、翻訳が自動化され、チームは優れたカスタマー・エクスペリエンスの提供に集中することができる。

{% alert important %}
2022年4月7日をもって、Transifex は API バージョン2と2.5を廃止し、バージョン3に移行しました。バージョン2と2.5は動作せず、関連するリクエストは失敗します。<br><br>以下の統合手順は、バージョン3のアップデートを反映したものである。コネクテッドコンテンツ呼び出しを適宜更新します。
{% endalert %}

## 前提条件

| 必要条件| 説明|
| ---| ---|
|トランシフェックス アカウント | このパートナーシップを活用するには、[Transifexアカウント](https://www.transifex.com/signin/)が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Transifex 統合では、Transifex の[リソース翻訳 API](https://developers.transifex.com/reference/get_resource-translations) を使用します。次の cURL を使用すると、翻訳に関連付けられたコンテンツ値がアカウントにあるかどうかを確認できます。 

まず、Transifexアカウントにある `<ORGANIZATION_NAME>`、`<PROJECT_NAME>`、`<RESOURCE_NAME>` を入力します。次に、`<LANGUAGE>` を翻訳をフィルタリングしたい言語コードに、`<TRANSIFEX_BEARER_TOKEN>` をTransifexの[ベアラートークンに](https://developers.transifex.com/reference/api-authentication)置き換える。

```
curl --request GET \
     --url 'https://rest.api.transifex.com/resource_translations?filter\[resource\]=o:<ORGANIZATION_NAME>:p:<PROJECT_NAME>:r:<RESOURCE_NAME>&filter\[language\]=l:<LANGUAGE>' \
     --header 'Accept: application/vnd.api+json' \
     --header 'Authorization: Bearer 1/<TRANSFIX_BEARER_TOKEN>'
```

たとえば、Transifex プロジェクトが`https://www.transifex.com/appboy-3/french2/french_translationspo/` にある場合、`project_name` は"french2&quot になり、`resource_name` は次のようになります "french_translationspo".

## コネクテッドコンテンツメッセージの例

このコード例は、Transifexリソース翻訳APIとユーザーの`language` 属性を利用している。必要に応じて文字列オブジェクトをループし、Liquid `{{strings.data[X].attributes.strings.other}}` を使用して関連するコンテンツを取得できます。

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
