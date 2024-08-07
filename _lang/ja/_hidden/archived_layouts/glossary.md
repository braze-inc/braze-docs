---
nav_title: 用語集
article_title: 用語集のレイアウト
page_order: 0
noindex: true
---

# レイアウト例:用語集

> 用語集のレイアウトはYAMLにあります。これには、いくつかのコンポーネントとパラメータが必要です。用語集レイアウトは、辞書や特定のカテゴリのコンテンツなど、ローカライズされた検索可能なコンテンツに適しています。

## 必要なコンポーネント

1. YAML Open and Closing 表記。つまり、コンテンツの前に`---`、その後に`---` となります。 
2. 特定のパラメータの内容を引用符で囲みます。(ヘッダパラメータ、テキストパラメータ、ハイフンを含むコンテンツ、またはその他の特殊文字)。
3. 用語集タグ s 表記(フィルター タグ s)

## 必要なパラメータ

|パラメータ | コンテンツタイプ | 詳細 |
|---|---|---|
|`page_order`| 数値 | セクション内のページを並べ替えます。この順序は左側のナビゲーションに反映されます。 |
| `nav-title`| 英数字 | 左側のナビゲーションで耳元をアプリするタイトル。 |
|`layout`| 英数字- スペースなし | ドキュメントの[レイアウトセクション](https://github.com/Appboy/braze-docs/tree/develop/_layouts)からレイアウトを選択します。 | 
|`glossary_top_header` | 英数字 | 二重引用符が必要です。タイトルアプリは、ページの上部に表示されます。 |
|`glossary_top_text`| 文字列、英数字 | 用語集のページを説明します。検索バーの上に耳がアプリされ、s がフィルターされます(必要な場合)。これは本質的にHTMLで書かれているので、\`\`\`を使うことができる<br> 改行の作成 | 
|`glossary_tag_name` | 単語、英数字 | フィルターに名前を付けます。これにより、検索バーの下にあるチェックボックスと、以下のデーターに耳がアプリされます。 | 
|`glossary_filter_text`| 文字列、英数字 | フィルターを説明します。通常、指示に使用します。 | 
|`glossary_tags`| YAMLプラスコンテンツ増。 | 次のような形式にします。<br> glossary_tags:<br>  \- name:コンテンツカードによって促進された <br>  \- name:メール | 
| `glossaries`| YAMLプラスコンテンツ増。 | 以下の[用語集パラメータ](#glossaries-parameters)を参照してください。 |

### 用語集パラメータ

|パラメータ | コンテンツタイプ | 詳細 |
|---|---|---|
|`name`| 英数字 | 用語集の項目に名前を付けます。| 
|`description`| 文字列、英数字 | 用語集の項目を説明します。 | 
|`calculation`| 文字列 | (オプション)用語集項目の計算方法を説明します(通常、データまたはメトリックを記述するときに使用されます)。 | 
|`tags`| 英数字 | `glossary_tags` の下に`name` としてリストされているものと一致する必要があります。アプリな限り多くのライセンスを記載する。`All` と記述すると、すべてのフィルターs にアイテムが含まれます。|

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
