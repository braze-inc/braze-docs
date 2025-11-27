---
nav_title: 用語集
article_title: 用語集のレイアウト
page_order: 0
noindex: true
---

# レイアウト例：用語集

> 用語集のレイアウトはYAMLである。それにはいくつかのコンポーネントとパラメーターが必要です。用語集レイアウトは、辞書や特定のカテゴリーのコンテンツなど、ローカライズされた検索可能なコンテンツに適している。

## 必要なコンポーネント

1. YAMLのオープン表記とクローズ表記。つまり、内容の前に`---` 、後に`---` 。 
2. 特定のパラメータの内容を引用符で囲む。(ヘッダー・パラメーター、テキスト・パラメーター、ハイフンやその他の特殊文字を含むコンテンツ)。
3. 用語集タグの表記（これらはフィルタータグである）

## 必須パラメータ

|パラメーター | コンテンツタイプ | 詳細 |
|---|---|---|
|`page_order`| 数値 | セクション内でページを順番に並べる。この順序は左側のナビゲーションに反映されます。 |
| `nav-title`| 英数字 | 左側のナビゲーションに表示されるタイトル。 |
|`layout`| 英数字 - スペースなし | ドキュメントの[レイアウトセクションから](https://github.com/Appboy/braze-docs/tree/develop/_layouts)レイアウトを選択する。 | 
|`glossary_top_header` | 英数字 | 二重引用符が必要です。タイトルはページ上部に表示される。 |
|`glossary_top_text`| 文字列、英数字 | 用語集ページについて説明する。これは、検索バーとフィルター（選択した場合）の上に表示される。これは基本的にHTMLで書かれているので、\`\`\`を使うことができる。<br> 改行を作成します。 | 
|`glossary_tag_name` | 単一単語、英数字 | フィルターに名前をつける。これらは、検索バーの下のチェックボックスや、下のデータに表示されます。 | 
|`glossary_filter_text`| 文字列、英数字 | フィルターについて説明してほしい。通常、指示に使用します。 | 
|`glossary_tags`| YAMLプラス・コンテンツが増えた。 | 書式は以下の通りです。<br> glossary_tags:<br>  \- name:コンテンツカードによって促進された <br>  \- name:メール | 
| `glossaries`| YAMLプラス・コンテンツが増えた。 | 以下の[用語集パラメーター](#glossaries-parameters)を参照してください。 |

### 用語集 パラメータ

|パラメーター | コンテンツタイプ | 詳細 |
|---|---|---|
|`name`| 英数字 | 用語集に名前をつける。| 
|`description`| 文字列、英数字 | 用語集の項目を説明する。 | 
|`calculation`| string | (任意) あなたの用語集項目がどのように計算されるかを記述する（通常、データや測定基準を記述するときに使用される）。 | 
|`tags`| 英数字 | `glossary_tags` の下に`name` として記載されているものと一致するはずである。該当するものをすべて挙げてください。`All` と書くと、すべてのフィルターにその項目が含まれる。|

## 例

```
---
page_order: 0
nav_title: Report Metrics Glossary
layout: glossary_page
glossary_top_header: "Report Metrics Glossary"
glossary_top_text: "These are terms you'll find in your reports in your Braze account. Search for the metrics you need, or filter by channel. <br>  <br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

glossary_tag_name: Channels
glossary_filter_text: "Select Channels below to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Content Cards
  - name: Email
  - name: In-App Message
  - name: News Feed
  - name: Web Push
  - name: iOS Push
  - name: Android Push
  - name: Webhook

glossaries:
  - name: Variation
    description: Variation of a campaign, differing as defined by the creator.
    calculation: Count
    tags:
      - All
  - name: Audience
    description: Percentage of users who received a particular message. This number is received from Braze.
    calculation: (Number of Recipients in Variant) / (Unique Recipients)
    tags:
      - All
  - name: Unique Recipients
    description: Exact number of users who received a particular message. This number is received from Braze.
    calculation: Count
    tags:
      - Email
      - Web Push
      - iOS Push
      - Android Push
      - In-App Message
      - News Feed
  - name: Total Impressions
    description: The number of users whose devices reported that the in-app message has been delivered (if a user receives a message twice, they will be counted twice). This number is a sum of number of impression events that Braze receives from the SDKs.
    calculation: Count
    tags:
      - In-App Message
      - News Feed
      - Content Cards
---
```
