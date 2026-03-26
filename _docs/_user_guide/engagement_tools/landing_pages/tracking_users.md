---
nav_title: Tracking users
article_title: Track users through a form
description: "Learn how to identify users who submit a form through your landing page by adding a Liquid tag to your messages."
page_order: 2
---

# Track users through a form

> Learn how to track users who submit a form through your landing page by adding a landing page Liquid tag to your  messages. This Liquid tag is supported across all Braze messaging channels, including email, SMS, in-app messages, and more. To learn more about tracking data, see [About landing page tracking data]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/about_tracking_data).

## How it works

You can add a {% raw %}`{% landing_page_url %}`{% endraw %} Liquid tag to any of your single or multi-channel messages in Braze. When a user visits that landing page and submits the form, Braze will automatically link that data to their existing profile, rather than create a new profile for that user. In the following example, a the landing page Liquid tag is used to link customers to a survey:

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
You can also use landing pages for lead generation by embedding the page URL into your external channels. After you create a landing page, go to **Landing Page Details** to get the unique URL for your landing page.
{% endalert %}

## Using landing page Liquid tags

### Prerequisites

Before you start, you'll need to create a [landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) and a [campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

### Step 1: Verify the page URL {#page-url}

Braze will use your landing page's URL to generate its unique Liquid tag. If you want to change the current page URL, go to **Messaging** > **Landing Pages**, then open your landing page. Under **page URL**, you can enter a new page URL.

{% alert warning %}
If you change the page URL after sending your message, any user that attempts to visit your landing page using the old URL will be sent to a `404` page.
{% endalert %}

![An example page URL for a landing page in Braze.]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### Step 2: Generate the Liquid tag

Go to **Messaging** > **Campaigns**, then choose a campaign. In your message editor, select **Personalization**.

![The 'Add personalization' button in the drag-and-drop editor.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

Braze will automatically generate a Liquid tag using your [landing page URL](#page-url). Refer to the following table to generate your tag:

|**Personalization type**| Choose **Landing Page**.|
|**Landing page**|Choose the landing page [you previously created](#prerequisites).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

To add the Liquid tag to your message, you can either select **Insert**, or copy the snippet to your clipboard and add it manually.

![An auto-generated Liquid tag for the selected landing page.]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

Your snippet will be similar to the following:

{% raw %}
```ruby
{% landing_page_url custom-url-handle %}
```
{% endraw %}

### Step 3: Finalize and send your message

Embed the Liquid snippet into your message, then finalize the rest of your message. For example:

{% raw %}
```html
<a href=" {% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

When you're ready, you can send the message to start tracking users through your landing page.
