---
nav_title: Tracking Users
article_title: Tracking users through a form
description: "Learn how to identify users who submit a form through your landing page by adding a Liquid tag to your messages."
page_order: 2
---

# Tracking users through a form

> Learn how to track users who submit a form through your landing page by adding a {% raw %}`{% landing_page_url %}`{% endraw %} Liquid tag to your  messages. This Liquid tag is supported across all Braze messaging channels, including email, SMS, in-app messages, and more. To learn more about tracking data, see [About landing page tracking data]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_data).

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

Go to **Messaging** > **Campaigns**, then choose a campaign. In your message editor, select **Personalization**.

![The 'Add personalization' button in the drag-and-drop editor.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

Braze will automatically generate a liquid tag using your [landing page's URL handle](#step-1-verify-your-url-handle). Refer to the following table to generate your tag:

|**Personalization type**| Choose **Landing Page**.|
|**Landing page**|Choose the landing page [you previously created](#prerequisites).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

To add the liquid tag to your message, you can either select **Insert**, or copy the snippet to your clipboard and add it manually.

![An auto-generated liquid tag for the selected landing page.]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

Your snippet will be similar to the following:

{% raw %}
```ruby
{% landing_page_url my-custom-url-handle %}
```
{% endraw %}

### Step 3: Finalize and send your message

Embed the liquid snippet into your message, then finalize the rest of your message. When you're ready, you can send the message to start tracking users through your landing page.
