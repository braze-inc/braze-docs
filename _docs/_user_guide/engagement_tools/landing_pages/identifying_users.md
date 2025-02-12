---
nav_title: Identifying Users
article_title: Identifying users through a landing page
description: "Learn how to identify users who submit a form through your landing page by adding a Liquid tag to your messages."
page_order: 3
---

# Identifying users through a landing page

> Learn how to identify users who submit a form through your landing page by adding a {% raw %}`{% landing_page_url %}`{% endraw %} Liquid tag to your  messages. This Liquid tag is supported across all Braze messaging channels, including email, SMS, in-app messages, and more.

## How it works

You can add a landing page liquid tag to any of your single or multi-channel messages in Braze. When a user visits that landing page and submits the form, Braze will automatically link the form's data to their user profile, as well as the messaging channel used to submit the form.

{% alert tip %}
You can also use landing pages for lead generation by embedding its page URL into your external channels. After you create a landing page, go to **Landing Page Details** to get the unique URL of a landing page.
{% endalert %}

## Using landing page liquid tags

### Prerequisites

Before you start, you'll need to [create a landing page]().

### Step 1: Verify the URL handle

Braze will use your landing page's URL handle to generate its unique liquid tag. If you want to change the current URL handle, go to **Messaging** > **Landing Pages**, then open your landing page. Under **URL handle**, you can enter a new URL handle.

{% alert warning %}
If you change the URL handle after sending your message, any user that attempts to visit your landing page using the old URL will be sent to a `404` page.
{% endalert %}

![ALT_TEXT]()

### Step 2: Generate the liquid tag

Go to **Messaging** > **Campaigns**, then choose a campaign. In the **Compose Messages** step, select **Drag-and-drop editor**.

![ALT_TEXT]()

In the editor, select **Add personalization**.

![ALT_TEXT]()

Braze will automatically generate a liquid tag using your [landing page's URL handle](#step-1-verify-your-url-handle). Refer to the following table to generate your tag:

|Dropdown|Choice|
|--------|------|
|**Personalization type**| Choose **Landing Page**.|
|**Landing page**|Choose the landing page [you previously created](#prerequisites).|

Select **Copy Liquid** to copy the snippet to your clipboard. Your snippet will be similar to the following:

{% raw %}
```ruby
{% landing_page_url CUSTOM_URL_HANDLE %}
```
{% endraw %}

### Step 4: Finalize and send your message

Embed the liquid snippet in your message, then finalize the rest of your message. When you're ready, you can send the message to start tracking users through your landing page.
