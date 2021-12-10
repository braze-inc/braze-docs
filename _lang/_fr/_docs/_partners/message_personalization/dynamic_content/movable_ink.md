---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
page_order: 1
description: "This article outlines the partnership between Braze and Movable Ink, a cloud-based software platform that offers digital marketers a way to create compelling and unique visual experiences that move customers."
page_type: partner
search_tag: Partner
---

# Movable Ink

> [Movable Ink][1] is a cloud-based software platform that offers digital marketers a way to create compelling and unique visual experiences that move customers. The Movable Ink platform provides valuable customization options that can easily be inserted into your campaigns.

Expand Braze's creative capabilities by leveraging Movable Ink's Intelligent Creative features like polling, countdown timer, and scratch-off. The Movable Ink and Braze integration powers a more well-rounded approach to dynamic data-driven messages, providing users with real-time elements about the things that matter.

## Prerequisites

| Requirement         | Description                                                                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Movable Ink account | You'll need a Movable Ink account to take advantage of this partnership.                                                                                                                                                  |
| Data source         | You will need to connect a data source to Movable Ink. This can be done through CSV, website import, or API. Make sure that you pass data with a unifying identifier between Braze and Movable Ink (e.g., `external_id`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Use cases
- Personalized monthly or end-of-year recaps.
- Dynamically personalize images for email, push, or rich notifications based on last known behavior.<br> For Example:
    - Using a rich push message to dynamically create a schedule of events by pulling data from API.
    - Using the Countdown Timer feature to notify users when a big sale is approaching (e.g., Black Friday, Valentine's Day, Holiday Deals, etc.)
    - Use the Scratch Off feature as a fun and interactive way to disburse Promo Codes.

## Supported Movable Ink capabilities

Intelligent Creative has many offerings that Braze users can take advantage of. Below is a list of what is supported.

| Movable Ink Capability      | Feature              | Rich Push Notification | In-App Messaging / Content Cards | Details                                                                                                 |
| --------------------------- | -------------------- | ---------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Creative Optimizer          | Display A/B Contents | ✗                      | ✔                                |                                                                                                         |
|                             | Optimize             | ✗                      | ✔*                               | * Must Use Branch's Deeplinking solution                                                                |
| Targeting Rules             | Date                 | ✔*                     | ✔                                | * Supported but not recommended because push notifications are cached upon receipt and do not refresh   |
|                             | Day of Week          | ✔*                     | ✔                                | * Supported but not recommended because push notifications are cached upon receipt and do not refresh   |
|                             | Time of Day          | ✔*                     | ✔                                | * Supported but not recommended because push notifications are cached upon receipt and do not refresh   |
| Stories/Behavior Activity   |                      | ✔*                     | ✔*                               | * The unique user identifier used for Braze must be linked to your ESP’s identifier                     |
| Deep Linking within the app |                      | ✔*                     | ✔*                               | * Must use Branch’s deep linking solution                                                               |
| Apps                        | Countdown Timer      | ✔*                     | ✔                                | * Supported but not recommended because push notifications are cached upon receipt and do not refresh   |
|                             | Polling              | ✗                      | ✔*                               | * After voting, will leave the app to be a mobile landing page                                          |
|                             | Scratch Off          | ✔*                     | ✔*                               | * On click, will leave the app for the Scratch Off experience                                           |
|                             | Video                | ✔*                     | ✔*                               | * Animated GIFs only, <br>For Android, Braze requires [GIF support][GIFsupport] in implementation |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Integration

### Step 1: Create a data source for Movable Ink

Customers will need to create a data source that can either be a CSV, website import, or API integration.

![datasource]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs %}
{% tab CSV Data Source %}
- __CSV Data Source__: Each row must have at least one segment column and one content column. After your CSV has been uploaded, select which columns should be used to target the content. [Example CSV File]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![datasource]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Website Data Source %}
- __Website Data Source__: Each row must have at least one segment column and one content column. After your CSV has been uploaded, select which columns should be used to target the content.
  - Within this process, you'll need to map:
    - Which fields will be used as Segments
    - Which fields you want as data fields that can be dynamically personalized in the creative (ex: user attributes or custom attributes like first name, last name, city, etc.)

![datasource]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API Integrations %}
- __API Integrations__: Use your company's API to power content directly from an API response.

![datasource]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### Step 2: Create a campaign on the Movable Ink platform

From the Movable Ink home screen, create a campaign. You can select from email from HTML, email from image, or a block that can be used in any channel, including push, in-app message, and Content Cards (suggested). We also suggest taking a look at the various content options available through blocks.

![create_campaign]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Ink has an easy editor for you to drag and drop elements like text, image, etc. If you have populated your data source, you can dynamically generate an image using the data properties. In addition, you can also create fallbacks within this flow for users if the campaign is sent and a user doesn't fit within the personalization criteria.

![create_campaign2]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

Before finishing your campaign, make sure to preview the dynamic images and test out the query parameters to see what the images will look upon view. Once complete, a dynamic URL will generate that can then be inserted into Braze!

For more information on how to use the Movable Ink Platform, visit the [Movable Ink support center][support]

### Step 3: Obtain Movable Ink content URL

To include Movable Ink content into Braze messages, you must locate the source URL Movable Ink has provided you.

To obtain the source URL, you must have set up the content in the Movable Ink dashboard, and then from there, finish and export your content. On the **Finish** page, copy the source URL(`img src`) from the creative tag.

![Obtain URL]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

Next, in the Braze Platform, paste the URL in the appropriate field. Appropriate fields for your messaging channel can be found in step 4. Lastly, replace any merge tags (i.e. {% raw %}`&mi_u=%%email%%`{% endraw %}) with the corresponding Liquid variable (i.e. {% raw %}`&mi_u={{${email_address}}}`{% endraw %}).

### Step 4: Braze experience

#### Push notifications

1. In the Braze Platform:
    - Android Push: Paste the URL in the __Push Icon Image__ and __Expanded Notification Image__ fields.
    - iOS Push: Paste URL in __Rich Notification Media__ link field, and directly below, denote the file format you are using.
    - Web Push: Paste the URL in the __Push Icon Image__ and __Large Notification Image__ fields.<br><br>
2. To make sure images are not cached, prepend the URL in the message with empty Liquid tags: <br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-goes-here`{% endraw %}

#### In-app messages and Content Cards

1. In the Braze platform, paste the URL in the __Rich Notification Media__ field.<br><br>
2. Provide a unique URL to help prevent caching. To ensure that Movable Ink’s real-time images work and will not be affected by caching, use Liquid to append a timestamp to the end of the Movable Ink image URL. <br> To do this, use the following syntax, replacing the image URL as needed:<br>{% raw %} `{% assign timestamp = "now" | date: "%s" %}` <br> `{% assign img = "https://movable-ink-image-url-goes-here" |  append:timestamp %} {{img}}` {% endraw %} <br>This template will take the current time (in seconds), append it to the end of the Movable Ink image tab (as a query param), and then output the final result. You can preview it with the **Test** tab  - this will evaluate the code and show a preview.<br><br>
3. Lastly, re-evaluate segment membership. To do this, enable the `Re-evaluate Segment membership` option located on the "Target Users" step of a campaign. If this is option is not available, reach out to your Customer Success Manager or Braze support. This option will instruct Braze SDKs to re-request the campaign providing a unique URL each time an in-app message is triggered.

## Troubleshooting

#### Dynamic images not showing correctly? What channel are you experiencing difficulties with?
- __Push__: Make sure that you have empty logic before your Movable Ink image URL: <br>{% raw %}`{% if true %}{% endif %}https://movable-ink-image-url-goes-here`{% endraw %}
- __In-app messages and Content Cards__: Make sure that the image URL is unique for each impression. This can be done by appending the appropriate Liquid so that each URL is different. See [In-App and Content Card Messages Instructions][Instructions].
- __Image not loading__: Be sure to replace any "merge tags" with the corresponding Liquid fields in the Braze dashboard. For example: {% raw %}`https://mi-msg.com/p/rp/image.png?mi_u=%%email%%`{% endraw %} with {% raw %}`https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}`{% endraw %}.

#### Having trouble showing GIFs on Android?
- Android requires GIF support in implementation. Follow the Android [in-app message customization][GIFsupport] article if you do not have this setup.
[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})

[1]: https://movableink.com/
[support]: https://support.movableink.com/
[GIFsupport]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#gifs-IAMs
[GIFsupport]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#gifs-IAMs
[Instructions]: {{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink/#step-4-braze-experience