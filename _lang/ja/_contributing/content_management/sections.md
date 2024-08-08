---
nav_title: セクション
article: Sections
description: "Brazeドークスでセクションを作成および順序付けする方法について説明します。"
page_order: 2
noindex: true
---

# セクション

> Brazeドークスでセクションを作成および順序付けする方法について説明します。個々のページを作成、変更、または削除するには、[ページ]({{site.baseurl}}/contributing/content_management/pages/)を参照してください。セクションの一般的な情報については、[コンテンツ管理]({{site.baseurl}}/contributing/content_management/#sections)を参照してください。

{% multi_lang_include contributing/prerequisites.md %}

## セクションの作成

### ステップ 1:ディレクトリとマークダウンファイルを作成する

関連するプライマリセクションまたはサブセクションを開き、新しいセクションのディレクトリとマークダウンファイルを作成します。

```plaintext
braze-docs
└── _docs
    └── PRIMARY_SECTION 
        └── SUBSECTION 
            ├── NEW_DIRECTORY 
            └── NEW_FILE.md
```

以下を交換します。

| プレースホルダ| 説明                                                                                                                                                                                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PRIMARY_SECTION` | 新しいコンテンツが属するプライマリセクションの名前。詳細については、[プライマリセクション]({{site.baseurl}}/contributing/content_management/#primary-sections)を参照してください。|
| `SUBSECTION` | 該当する場合は、新しいコンテンツのサブセクションの名前が属します。詳細については、[サブセクション]({{site.baseurl}}/contributing/content_management/#subsections)を参照してください。|
| `NEW_DIRECTORY` | 新しいセクションの名前。[ろう付けドックススタイルガイド]({{site.baseurl}}/contributing/style_guide/) に従います。すべての小文字を使用し、特殊文字を削除し、スペースをアンダースコアに置き換えます(`_`)。この名前は`NEW_FILE` と一致する必要があります。|
| `NEW_FILE` | 新しいセクションの名前。[Braze Docs Style Guide]({{site.baseurl}}/contributing/style_guide/) に従います。すべての小文字を使用し、特殊文字を削除し、スペースをアンダースコアに置き換えます(`_`)。この名前は`NEW_DIRECTORY` と一致する必要があります。|
{: .reset-td-br-1 .reset-td-br-2}

ディレクトリ構造は、次のようになります。

```plaintext
braze-docs
└── _docs
    └── _developer_guide 
        └── platform_wide 
            ├── getting_started 
            └── getting_started.md
```

### ステップ 2:セクションの設定

新しいセクションを作成するときに、ランディングページの有無にかかわらず、新しいセクションを設定できます。

- **ランディングページあり:**セクションで&quot のランディングページ、Getting started&quot、前提条件のリスト化、ユーザージャーニーの概要など、専用の概要が必要な場合は、この方法を使用します。
- **ランディングページなし:**セクションに専用の概要が必要ない場合は、この方法を使用します。[Braze Docs Style Guide]({{site.baseurl}}/contributing/style_guide/)に記載されているように、コンテンツは常に役立つはずです。便利なコンテンツが少ない場合は、ランディングページを追加しないでください。

{% tabs %}
{% tab with landing page %}
新しいMarkdown ファイルを開き、以下のテンプレートを追加します。テンプレートの詳細については、[テンプレート]({{site.baseurl}}/contributing/templates/)を参照してください。

\`\`\`markdown
---
nav_title: NAV\_TITLE
article_title: LANDING\_PAGE\_TITLE
description: SHORT\_DESCRIPTION
---

# LANDING\_PAGE\_TITLE 

> SHORT\_DESCRIPTION

## HEADING

CONTENT
\`\`\`

以下を交換します。

| プレースホルダ| 説明|
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `NAV_TITLE` | ページのタイトルが左側のナビゲーションバーに表示されます。ほとんどの場合、`nav_title` は`article_title` に一致する必要がありますが、領域を節約するには、より短い_ を使用しますが、_ title は同じです。|
| `LANDING_PAGE_TITLE` | ランディングページのタイトル。メタデータの`LANDING_PAGE_TITLE` の値は検索エンジンの結果に使用され、`LANDING_PAGE_TITLE` の値はページに表示されるタイトルに使用されます。|
| `SHORT_DESCRIPTION` | ページの短い1-2 センテンスの説明。YAML の`SHORT_DESCRIPTION` 値は検索エンジンの結果に使用され、`SHORT_DESCRIPTION` 値はページに表示される説明に使用されます。|
| `HEADING` | 見出し2セクションのタイトル。|
| `CONTENT` | 見出し2 セクションの本文段落。|
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
このテンプレートは、必要に応じてstarted-add [追加のメタデータ]({{site.baseurl}}/contributing/yaml_front_matter/metadata/)とヘッダーを追加するためだけのものです。
{% endalert %}
{% endtab %}

{% tab without landing page %}
サブセクションのMarkdown ファイルを開き、以下のメタデータを追加してページのナビゲーションタイトルを設定し、ランディングページを無効にします。

\`\`\`markdown
---
nav_title: NAV\_TITLE
config_only: true
---
\`\`\`

{% alert tip %}
このテンプレートは、必要に応じてstarted-add [追加のメタデータ]({{site.baseurl}}/contributing/yaml_front_matter/metadata/)とヘッダーを追加するためだけのものです。
{% endalert %}

`NAV_TITLE` は、左側のナビゲーションバーに表示されるページのタイトルに置き換えます。ページは次のようになります。

\`\`\`markdown
---
nav_title: はじめに
page_order: 2
noindex: true
config_only: true
---
\`\`\`
{% endtab %}
{% endtabs %}

### ステップ 3:ページを追加する

新しいディレクトリで、ページごとにマークダウンファイルを作成します。デフォルトのページレイアウトを使用するには、[ステップ2]({{site.baseurl}}/contributing/content_management/sections/?tab=with%20landing%20page#step-2-configure-your-section) でテンプレートを使用します。ディレクトリ構造は、次のようになります。

```plaintext
braze-docs
└── _docs
    └── _developer_guide 
        └── platform_wide 
            ├── getting_started 
            │    ├── integrating_the_sdk.md 
            │    └── setting_up_push_notifications.md
            └── getting_started.md
```

各ページへのコンテンツの追加が完了したら、[セクション](#ordering-a-section)の順序付けに進みます。

{% alert tip %}
ページへのコンテンツの追加に関する詳細なウォークスルーについては、[ページ]({{site.baseurl}}/contributing/content_management/pages/#writing-content)を参照してください。
{% endalert %}

## セクションの注文

セクションを注文するには、そのセクションのいずれかのMarkdown ファイルを開き、YAML の前面にある[`page_order`]({{site.baseurl}}/contributing/yaml_front_matter/metadata/#page-order) キーを検索します。

\`\`\`markdown
---
page_order:
---
\`\`\`

`page_order` キーは、左側のナビゲーションバーのセクションのページの相対的な順序を表し、負でない任意の番号(`0`、`20`、`5.5` など) に設定できます。つまり、カレントディレクトリ内の各Markdown ファイルの`page_order` を知る必要がありますが、他のディレクトリ(サブディレクトリを含む) を知る必要はありません。

カレントディレクトリ内の各Markdown ファイルの`page_order` キーを任意の負でない番号に設定します。次の例では、`page_order` が`2` に設定されています。  

\`\`\`markdown
---
nav_title: B項
page_order: 2 
---

# B項上陸ページ
\`\`\`

出力は次のようになります。

![The left-side navigation on Braze Docs, with the 'Section B' landing page listed third.]({% image_buster /assets/img/contributing/styling_examples/subsection_landing_page.png %})
