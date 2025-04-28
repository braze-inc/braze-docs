---
nav_title: Just Words
article_title: Just Words
description: "This reference article outlines the partnership between Braze and Just Words, an AI-based SaaS business platform that creates personalized versions of existing campaigns and optimizes subject lines, creative content, and HTML email layouts over time."
alias: /partners/just_words/
page_type: partner
---

# Just Words Integration Guide

> [Just Words](https://www.justwords.ai/) hyper-personalizes messaging at scale on lifecycle marketing channels, empowering you to dynamically test hundreds of variations and auto-refresh underperforming content.

When you use Just Words with Braze Connected Content to personalize your existing Braze campaigns and Canvases, Just Words will use Braze Currents to optimize the content dynamically—so you don’t have to.

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

![The Just Words template creation platform.]({% image_buster /assets/img/just_words/creation_interface.png %}){: style="max-width:80%;"}

### Step 2: Create a Just Words API key

1. Go to **Org Settings** > **API Keys** > **Generate API Key**.
2. Copy and save the API key in a secure location.

![The Just Words API key form.]({% image_buster /assets/img/just_words/api_key_form.png %}){: style="max-width:80%;"}

### Step 3: Use Just Words in your Braze content

Just Words works with Canvases and campaigns by using Connected Content.

#### Canvas

Each email step in the Canvas should correspond to a unique Just Words template.

#### Step 3.1: Set up your A/B test

1. In a Canvas, select **Add Variant** > **Add Variant**, and add steps to each variant (like an email Message step).
2. Split the audience traffic in half (make each variant 50%).
3. In the composers for the Message steps that you want to use with Connected Content, paste in the Connected Content snippet from Just Words Console.

![Braze A/B test Canvas setup.]({% image_buster /assets/img/just_words/braze_canvas.png %}){: style="max-width:70%;"}

##### Example Connected Content snippet

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

![Braze Liquid logic in an HTML message composer.]({% image_buster /assets/img/just_words/just_words_personalization.png %}){: style="max-width:80%;"}

### Step 4: Preview the email

Make sure to preview the email in Braze to confirm that the personalized content correctly renders.

![Braze message preview for a Just Words email.]({% image_buster /assets/img/just_words/just_words_preview.png %}){: style="max-width:80%;"}

### Step 5: Set up Braze Currents

Braze Currents enables performance tracking and optimization over time.

1. In Braze, go to **Partner Integrations** > **Data Export**.
2. Select **Create New Test Current** and then select **Test Amazon S3 Data Export**.

!["Create New Test Current" dropdown with the option of "Test Amazon S3 Data Export".]({% image_buster /assets/img/just_words/test_amazon_s3.png %}){: style="max-width:80%;"}

{: start="3" }
3. Enter the S3 Access ID, AWS Secret Access Key, Bucket name, and folder that were provided by Just Words during onboarding.

!["Credentials" section for the AWS secret access key.]({% image_buster /assets/img/just_words/aws_secret_access_key.png %}){: style="max-width:80%;"}

{: start="4" }
4. Select the events to track, such as sends, opens, clicks, unsubscribes, conversions, and others.

!["Message Engagement Events" section with events to select.]({% image_buster /assets/img/just_words/message_engagement_events.png %}){: style="max-width:80%;"}

{: start="5" }
5. Launch the Braze Current.

You're all set! Now you can access the Just Words platform to:

- See real-time experiment results
- Dynamically edit copy
- View performance insights

{% alert note %}
Questions? Contact Just Words on their [booking page](https://www.justwords.ai/book-demo) or through the shared Slack channel.
{% endalert %}
