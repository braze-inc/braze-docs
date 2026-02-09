---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "이 참고 문서는 Braze와 Stripo 간의 파트너십을 설명합니다. Stripo는 인터랙티브 요소가 포함된 정교한 이메일을 만들기 위한 드래그 앤 드롭 이메일 템플릿 빌더입니다."
page_type: partner
search_tag: Partner

---

# Stripo

> [Stripo](https://stripo.email/)는 인터랙티브 요소가 포함된 반응형 이메일을 디자인하기 위한 드래그 앤 드롭 이메일 템플릿 빌더입니다. Stripo users can also edit in HTML and decide which elements to display or hide on various devices through the Stripo editor.

_This integration is maintained by Stripo._

## About the integration

The Braze and Stripo integration allows you to export your customized Stripo emails and upload them as templates within Braze.

## Prerequisites

| Requirement | Description |
| ------------| ----------- |
| Stripo account | A Stripo account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with full **Templates** permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Cluster instance | Your Braze [cluster instance]({{site.baseurl}}/api/basics/#endpoints) aligns with your Braze dashboard and REST endpoint.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

### Step 1: Create Stripo email

Create a Stripo email in the Stripo platform and click **Export**. 

![Stripo 내보내기]({% image_buster /assets/img_archive/stripo_export.png %})

### 2단계: Export template to Braze

In the dialogue that appears, select **Braze** as your method of export 

Next, enter your **account name** (such as workspace name), **API key**, and your **cluster instance**.

![Stripo 양식]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
This is a one-time setup, and any exports in the future will automatically utilize this API key.
{% endalert %}

## Usage

Braze 계정의 **템플릿 & 미디어 > 이메일 템플릿** 섹션에서 업로드한 Stripo 템플릿을 찾으세요. You can now use this email template to start sending engaging email messages to your customers!


