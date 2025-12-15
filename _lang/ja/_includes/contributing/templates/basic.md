このテンプレートを使って、Braze Docsのあらゆるページやセクションを作成できる。例については、[プレビューを生成する]({{site.baseurl}}/contributing/generating_a_preview/)を参照してください。記事内で使用されるドキュメントタイプのガイドラインについては、[ページタイプ]({{site.baseurl}}/contributing/page_types/)を参照してください。

{% details Show template %}
{% raw %}
`````markdown
---
nav_title: NAV_TITLE
article_title: ARTICLE_TITLE
description: "SHORT_DESCRIPTION."
alias: /OPTIONAL_SHORT_ARTICLE_TITLE/
page_type: reference
layout: OPTIONAL_LAYOUT_FILE
---

<!-- The title of your page, used to render the in-page title. -->
# ARTICLE_TITLE

<!-- The overview starts with a '>' character and discusses what will be covered. In an optional following paragraph, contextualize the topic at a high-level in an introduction. -->
> DESCRIPTION.

INTRODUCTION.

<!-- The prerequisites for this task. If no prerequisites are required, you can remove this section. -->
## Prerequisites

Before you start, you'll need to complete the following:

- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE
- ACTION_TO_COMPLETE

<!-- An optional, brief explanation of how the feature workflow looks. -->
## How it works

CONTENT.

<!-- Walk a user through integrating and turning on the feature. -->
 ## Integration
CONTENT.

<!-- A how-to guide with nested steps. -->
## TASK_TO_COMPLETE

<!-- Optional overview of the task. -->
CONTENT.

<!-- Action-oriented header that describes the step’s goal. -->
### Step 1: ACTION_TO_COMPLETE

<!-- Use number bullets or paragraphs to describe how to complete this action -->
CONTENT.

### Step 2: ACTION_TO_COMPLETE

CONTENT.
<!-- Optional references, such as supported data types, fields, definitions, and similar. -->
### REFERENCE_TO_ASSIST_WITH_ACTION

CONTENT.

<!-- For optional steps, add “(optional)” to the end of the header. -->
### Step 3: OPTIONAL_ACTION_TO_COMPLETE (optional)

CONTENT.
<!-- An optional section for what is supported. Add nested headers to be more specific. -->
## Supported data types / Supported attributes / Supported events / Supported ETC.
CONTENT.
<!-- An optional section with important considerations for users to review before using the feature. -->
## Considerations

CONTENT.

<!-- An optional section guiding users through troubleshooting common issues. -->
## Troubleshooting

### ISSUE_TO_TROUBLESHOOT
CONTENT.

`````
{% endraw %}
{% enddetails %}