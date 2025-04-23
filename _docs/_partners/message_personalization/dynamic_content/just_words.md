---
nav_title: Just_Words
article_title: Just_Words
description: "This reference article outlines the partnership between Braze and Just Words, an AI-based SaaS business platform that creates personalized versions of existing campaigns and optimizes subject lines, creative content, and HTML email layouts over time."
alias: /justwords/
page_type: partner
---
# Just Words Integration Guide

Just Words hyper-personalizes messaging at scale on Lifecycle Marketing channels. You can dynamically test 100s of variations and auto-refresh underperforming content on the fly.

By using **Braze Connected Content**, you can personalize your existing Braze campaigns and canvases with Just Words. Just Words will then use **Braze Currents** to optimize the content dynamically—so you don’t have to.

---

## 1. Create a Just Words Template

If you don’t have a Just Words account, [schedule a 30-minute onboarding call](https://www.justwords.ai/book-demo).

- Go to: [https://console.justwords.ai/new](https://console.justwords.ai/new)
- Choose an easy-to-remember ID (use alphanumerics and underscores).
- Fill out basic campaign details.
- Use AI to generate personalized variations.

![Just Words Template Creation Interface](https://imagedelivery.net/lLhosygWiKIAdQXdGdijjg/7d52f16f-89ea-46ae-43f7-5066a5c3d400/public)

---

## 2. Create a Just Words API Key

- Navigate to **Org Settings → API Keys → Generate API Key**.
- Copy and save the API key in a secure location.

![Just Words API Key Form](https://imagedelivery.net/lLhosygWiKIAdQXdGdijjg/f7dd0269-86c0-420f-369a-970133da2f00/public)

---

## 3. Use Just Words in Your Braze Content

Just Words works with **Canvases** and **Campaigns** using **Connected Content**.

### In a Canvas:

Each email step in the Canvas should correspond to a unique Just Words Template.

#### Setup A/B Test:

1. Click **Edit Canvas**.
2. Select the step to use as the control.
3. Click **Add Variant → Add Variant**, and create new content (e.g., Email) for the treatment.
4. Split the audience traffic 50/50.
5. In the content editor, paste the Connected Content snippet from Just Words Console.

![Braze A/B Test Setup](https://imagedelivery.net/lLhosygWiKIAdQXdGdijjg/6645cc58-acd0-4a8a-9079-a2516c94fa00/public)

### Example Connected Content Snippet:

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

---

### Optional: Add Personalization via Custom Attributes

To personalize by custom attributes (e.g., `industry`):

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

![Braze Liquid Logic](https://imagedelivery.net/lLhosygWiKIAdQXdGdijjg/f94640cc-82f6-4099-a9b2-fcd1d47a3900/public)

---

## 4. Preview the Email

Make sure to preview the email in Braze to confirm that the personalized content is rendering correctly.

![Braze Preview](https://imagedelivery.net/lLhosygWiKIAdQXdGdijjg/deaf4216-ca1f-4775-6964-0e14d8e6d900/public)

---

## 5. Set Up Braze Currents (One-Time Setup)

This enables performance tracking and optimization over time.

1. In Braze Currents, create a new Current of type **Test Amazon S3 Data Export**.

![Step 1](https://imagedelivery.net/lLhosygWiKIAdQXdGdijjg/c81efaff-a5ee-43bb-dd6c-d04a0152cc00/public)

2. Enter the S3 Access ID, AWS Secret Access Key, Bucket name, and folder—Just Words will provide these during onboarding.

![Step 2](https://imagedelivery.net/lLhosygWiKIAdQXdGdijjg/51d64b0d-9ba9-4d74-8a4c-eec636c21700/public)

3. Select the events to track: sends, opens, clicks, unsubscribes, conversions, etc.

![Step 3](https://imagedelivery.net/lLhosygWiKIAdQXdGdijjg/4105908f-2e83-400f-5604-cfefc98d9f00/public)

4. Launch the Current.

---

## You're All Set

Once launched, you can access the Just Words platform to:

- See real-time experiment results
- Edit copy dynamically
- View performance insights

---

> Questions? Contact us through [our booking page](https://www.justwords.ai/booking) or via our shared Slack channel.
