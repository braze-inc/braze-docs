---
nav_title: Click tracking
article_title: Click Tracking
page_order: 3
description: "This reference article covers how to turn on click tracking in your WhatsApp messages, test shortened links, use your custom domain in tracked links, and more."
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Click tracking

> This page covers how to turn on click tracking in your WhatsApp messages, test shortened links, use your custom domain in tracked links, and more.

Click tracking lets you measure when someone taps a link in your WhatsApp message, giving you a clear view into what content is driving engagement. Braze shortens your URLs, adds tracking behind the scenes, and logs click events as they happen.

You can turn on click tracking in both response and template messages. It works with links in buttons and body text, and supports personalized URLs and custom domains. After it's turned on, you'll see click data in your WhatsApp performance reports and be able to segment users based on who clicked what.

{% alert note %}
Click tracking doesn’t work with deep links. You can shorten universal links from providers such as Branch or Appsflyer, but Braze is unable to troubleshoot issues that may arise in doing so (such as breaking the attribution or causing a redirect).
{% endalert %}

## How it works

### Response messages 

To set up click tracking for response messages:
1. Create a response message that includes a call-to-action (CTA) button with a website URL.
2. Enable click tracking by clicking the designated button in the interface.

The link will be shortened to the Braze domain, or the custom domain specified for the subscription group, and personalized for the user.

Any static URLs that start with `http://` or `https://` will be shortened. Shortened URLs that contain Liquid personalization (such as user-level tracking targeting) will be valid for two months.

![WhatsApp message composer with content body and a button.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### Template messages 

For template messages, the base URL must be submitted correctly when creating the template to turn on click tracking.

#### Step 1: Build a click-tracking supported template in WhatsApp

1. In your WhatsApp Manager, create a base URL that is either your custom domain or `brz.ai`.
2. Make sure that the links included in the template are compatible with click tracking.
3. Don’t change the template variables after it’s set up as a campaign in Braze; downstream changes can’t be incorporated.
4. For CTA button links, select **Dynamic**, and then provide the base URL (`brz.ai` or your custom domain).<br><br>![Section to create a call to action.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %})<br><br>
5. For links in the body text, when writing the template in your WhatsApp Manager, remove any inserted spaces for links contained in the body that you want to track.<br><br>![Textbox to enter the content body for the call to action.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %})

#### Step 2: Complete your template in Braze

When composing, Braze will automatically detect which templates have supportable URL domains, both in the body text and for CTA buttons. The status will be shown at the bottom of the template. 

!["Link Status" section showing an active status for click tracking.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **Supported links:** Links that are submitted with the matching base URL will have click tracking enabled.
- **Partially-supported links:** If some links in a template are submitted as full URLs, click tracking **won't** be applied to those links.
- **Unsupported links:** Links without an approved base URL **won't** have click tracking capabilities.

The destination URL will need to be provided for any link with a base URL that matches either `brz.ai` or your custom domain. 

!["Buttons" section with fields for a button name, website URL, and click tracking URL.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## Liquid personalization in URLs

You can dynamically construct your URL directly within the Braze composer, allowing you to add dynamic UTM parameters to your URLs or send users unique links (such as directing users to their abandoned cart or to a specific product that is back in stock).
URLs can be dynamically generated through the use of any supported Liquid personalization tags.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

We also support the shortening of custom-defined Liquid variables, such as in these examples:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Shorten URLs rendered by Liquid variables

Braze shortens URLs that are rendered by Liquid, even those included in API-trigger properties. For example, if {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} represents a valid URL, we will shorten and track that URL before sending the WhatsApp message.

## Testing

Before launching your campaign or Canvas, it’s best practice to preview and test your message first. To do so, go to the **Test** tab to preview and send a WhatsApp to content test groups or an individual user.

This preview will update with relevant personalization and the shortened URL. 

{% alert important %}
If a draft is created within an active Canvas, a shortened URL won’t be generated. The actual shortened URL is generated when the Canvas draft is made active.
{% endalert %}

## Reporting

When click tracking is turned on or used with supported templates, the WhatsApp performance table includes the column **Total Clicks** that shows a count of click events per variant and an associated click rate. For more details on WhatsApp metrics, refer to [WhatsApp message performance]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics).

![WhatsApp Message Canvas step.]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

Click data will be automatically reported in the analytics dashboard.

![WhatsApp message performance table.]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## Retargeting users 

You can use the `Clicked/Opened Step` filter and `clicked tracked WhatsApp link` interaction to segment users based on their interactions with the links.

![Filter group with a filter for "clicked tracked WhatsApp link".]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Do I know which individual users are clicking on a URL?

Yes. When click tracking is turned on (or enabled based on template configuration), you can retarget users who have clicked URLs by leveraging the WhatsApp retargeting filters or the WhatsApp click events (`users.messages.whatsapp.Click`) sent by Currents.

### Do previews on the WhatsApp device count as clicks? 

No, they do not contribute to the click rate for WhatsApp messages. 

