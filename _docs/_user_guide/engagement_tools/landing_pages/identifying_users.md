---
nav_title: Identifying Users
article_title: Identifying users through a landing page
description: "Learn how to identify users who submit a form through your landing page by adding a Liquid tag to your messages."
page_order: 3
---

# Identifying users through a landing page

> Learn how to identify users who submit a form through your landing page by adding a {% raw %}`{% landing_page_url %}`{% endraw %} Liquid tag to your  messages. This Liquid tag is supported across all Braze messaging channels, including email, SMS, in-app messages, and more.

## How it works

You can add a landing page liquid tag to any of your single or multi-channel messages in Braze. When a user visits that landing page and submits the form, Braze will automatically link that data to their existing profile, rather than create a new profile for that user.

{% alert tip %}
You can also use landing pages for lead generation by embedding the page URL into your external channels. After you create a landing page, go to **Landing Page Details** to get the unique URL for your landing page.
{% endalert %}

## Using landing page liquid tags

### Prerequisites

Before you start, you'll need to create a [landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating/) and a [campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

### Step 1: Verify the URL handle

Braze will use your landing page's URL handle to generate its unique liquid tag. If you want to change the current URL handle, go to **Messaging** > **Landing Pages**, then open your landing page. Under **URL handle**, you can enter a new URL handle.

{% alert warning %}
If you change the URL handle after sending your message, any user that attempts to visit your landing page using the old URL will be sent to a `404` page.
{% endalert %}

![An example URL handle for a landing page in Braze.]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### Step 2: Generate the liquid tag

Go to **Messaging** > **Campaigns**, then choose a campaign. Under **Message content**, select **Drag-and-drop editor**.

![The 'Compose Messages' step in Braze with the 'Drag-and-drop editor' option shown.]({% image_buster /assets/img/landing_pages/message-content-options.png %})

In the editor, select **Personalization**.

![The 'Add personalization' button in the drag-and-drop editor.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:35%;"}

Braze will automatically generate a liquid tag using your [landing page's URL handle](#step-1-verify-your-url-handle). Refer to the following table to generate your tag:

|**Personalization type**| Choose **Landing Page**.|
|**Landing page**|Choose the landing page [you previously created](#prerequisites).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Select **Copy Liquid** to copy the snippet to your clipboard. Your snippet will be similar to the following:

{% raw %}
```ruby
{% landing_page_url CUSTOM_URL_HANDLE %}
```
{% endraw %}

### Step 3: Finalize and send your message

Embed the liquid snippet into your message, then finalize the rest of your message. When you're ready, you can send the message to start tracking users through your landing page.
