---
nav_title: Stensul
article_title: Stensul
alias: /partners/stensul
description: "이 참고 문서에서는 여러 채널에서 모바일 반응형 이메일 템플릿을 생성하는 기업용 이메일 플랫폼인 Braze와 Stensul의 파트너십에 대해 간략하게 설명합니다."
page_type: partner
search_tag: Partner

---

# Stensul

> [Stensul은](https://stensul.com/) 이메일 마케팅 담당자가 모바일 반응형 온브랜드 이메일을 Stensul에서 구축한 후 캠페인 생성을 위해 실시간으로 Braze로 전송할 수 있는 도구를 제공합니다.

_This integration is maintained by Stensul._

## About the integration

The Braze and Stensul integration allows you to export your HTML-formatted Stensul emails and upload them as templates within Braze.

## Prerequisites

| Requirement | Description |
| ------------| ----------- |
| Stensul account | A Stensul account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with full **Templates** permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Cluster instance | Your Braze [cluster instance]({{site.baseurl}}/api/basics/#endpoints) aligns with your Braze dashboard and REST endpoint.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

Provide your Braze REST API key and cluster instance to your Stensul customer success team. The team will then set up the initial integration for you.

{% alert important %}
This is a one-time setup and any exports in the future will automatically utilize this API key.
{% endalert %}

### Step 1: Create Stensul email

Create a Stensul email in the Stensul platform and click **Complete**.

![Stensul 저장 옵션]({% image_buster /assets/img_archive/stensul_save_options.png %})

### 2단계: Export template to Braze
In the new dialogue that appears on the completion page, select **Upload to ESP**.

![Stensul 업로드 옵션]({% image_buster /assets/img_archive/stensul_upload_options.png %})

Next, enter the **template name**, **subject**, and **preheader** for your email and select **Upload**. You will then receive a confirmation that the upload was successful and a history of past uploads of the file, if applicable.

![Stensul 업로드 성공]({% image_buster /assets/img_archive/stensul_upload_success.png %})

## Usage

Braze 계정의 **템플릿 & 미디어 > 이메일 템플릿** 섹션에서 업로드한 Stensul 템플릿을 찾으세요. You can now use this email template to start sending engaging email messages to your customers!


