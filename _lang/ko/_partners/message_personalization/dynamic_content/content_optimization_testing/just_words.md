---
nav_title: Just Words
article_title: Just Words
description: "This reference article outlines the partnership between Braze and Just Words, an AI-based SaaS business platform that creates personalized versions of existing campaigns and optimizes subject lines, creative content, and HTML email layouts over time."
alias: /partners/just_words/
page_type: partner
---

# Just Words Integration Guide

> [Just Words](https://www.justwords.ai/) hyper-personalizes messaging at scale on lifecycle marketing channels, empowering you to dynamically test hundreds of variations and auto-refresh underperforming content.

When you use Just Words with Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) to personalize your existing Braze campaigns and Canvases, Just Words will use Braze Currents to optimize the content dynamically—so you don’t have to.

## What are the benefits?

After your integration is complete, you can leverage the Just Works platform to:

- See real-time experiment results
- Dynamically edit copy
- View performance insights

{% alert note %}
Questions? Contact Just Words on their [booking page](https://www.justwords.ai/book-demo) or through the shared Slack channel.
{% endalert %}

## Prerequisites

| Requirement | Description |
|---|---|
| Just Words Account | A [Just Words](https://www.justwords.ai/) account is required to take advantage of this partnership. If you don’t have a Just Words account, [schedule a 30-minute onboarding call](https://www.justwords.ai/book-demo). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integrating Just Words with Braze

### Step 1: Create a Just Words template

1. Go to your Just Words console and [create a new template](https://console.justwords.ai/new).
2. Choose an easy-to-remember ID that uses letters, numbers, and underscores only.
3. Fill out basic campaign details.
4. Use AI to generate personalized variations.

![Just Words 템플릿 제작 플랫폼입니다.]({% image_buster /assets/img/just_words/creation_interface.png %}){: style="max-width:80%;"}

### 2단계: Create a Just Words API key

1. Go to **Org Settings** > **API Keys** > **Generate API Key**.
2. Copy and save the API key in a secure location.

![Just Words API 키 양식입니다.]({% image_buster /assets/img/just_words/api_key_form.png %}){: style="max-width:80%;"}

### 3단계: Use Just Words in your Braze content

Just Words works with Canvases and campaigns by using Connected Content. If you're creating a Canvas, each email step should correspond to a unique Just Words template.

#### Step 3.1: Set up your A/B test

{% tabs %}
{% tab Canvas %}

1. In a Canvas, select **Add Variant** > **Add Variant** until you have your desired number of variants, and add steps to each variant (like an email Message step).
2. Split the audience traffic as desired. For example, if you have two variants, you might give each one 50%. Or, you could have two variants with 40% each and a control group with 20%. For more information about A/B tests for Canvases, refer to [Creating a Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
3. In the composers for the Message steps that you want to use with Connected Content, paste in the Connected Content snippet from Just Words Console, such as the following snippet.

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

![Braze A/B 테스트 캔버스 설정.]({% image_buster /assets/img/just_words/braze_canvas.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Campaign %}

1. In the **Compose Messages** step of your campaign, create two variants.
2. In the **Target Audience** step, go to the **A/B Testing** section and modify the percentages of users who will receive each of your variants (and your optional control group). You can further customize your test by selecting an optimization option. For more information about A/B tests for campaigns, refer to [Creating multivariate and A/B tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/).
3. In the message composer, paste in the Connected Content snippet from Just Words Console, such as the following snippet.

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### Step 3.2:  Add personalization with custom attributes (optional)

To personalize your messages with custom attributes (such as `industry`), use the following Liquid format:

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}&attrs.industry={{ custom_attribute.industry }}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

Note that the custom attribute of `industry` is indicated by {% raw %}```&attrs.industry={{ custom_attribute.industry }}```{% endraw %}. 

![HTML 메시지 작성기에서 Braze Liquid 로직.]({% image_buster /assets/img/just_words/just_words_personalization.png %}){: style="max-width:80%;"}

### 4단계: Preview the email

Make sure to preview the email in Braze to confirm that the personalized content correctly renders.

![Just Words 이메일에 대한 Braze 메시지 미리보기.]({% image_buster /assets/img/just_words/just_words_preview.png %}){: style="max-width:80%;"}

### 5단계: Set up Braze Currents

Braze Currents enables performance tracking and optimization over time.

1. In Braze, go to **Partner Integrations** > **Data Export**.
2. Select **Create New Test Current** and then select **Test Amazon S3 Data Export**.

!["새 테스트 전류 만들기" 드롭다운에서 "Amazon S3 데이터 내보내기 테스트" 옵션을 선택합니다.]({% image_buster /assets/img/just_words/test_amazon_s3.png %}){: style="max-width:80%;"}

{: start="3" }
3\. Enter the S3 Access ID, AWS Secret Access Key, Bucket name, and folder that were provided by Just Words during onboarding.

![AWS 비밀 액세스 키에 대한 "자격 증명" 섹션.]({% image_buster /assets/img/just_words/aws_secret_access_key.png %}){: style="max-width:80%;"}

{: start="4" }
4\. Select the events to track, such as sends, opens, clicks, unsubscribes, conversions, and others.

!["메시지 참여 이벤트" 섹션에서 이벤트를 선택할 수 있습니다.]({% image_buster /assets/img/just_words/message_engagement_events.png %}){: style="max-width:80%;"}

{: start="5" }
5\. Launch the Braze Current.

You're all set! Now you can use Just Words with Braze Connected Content.