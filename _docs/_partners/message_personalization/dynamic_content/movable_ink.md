---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
page_order: 1
description: "This article outlines the partnership between Braze and Movable Ink, a cloud-based software platform that offers digital marketers a way to create compelling and unique visual experiences that move customers."
page_type: partner
search_tag: Partner

---

# Movable ink

> [Movable Ink][1] is a cloud-based software platform that offers digital marketers a way to create compelling and unique visual experiences that move customers. The Movable Ink Platform provides valuable customization options that can easily be inserted into your campaigns. 

Expand Braze's creative capabilities by leveraging Intelligent Creative features like polling, countdown timer, and scratch off with Movable Ink. Movable Ink and Braze power a more well-rounded approach to dynamic data-driven messages, providing users with real-time elements about the things that matter.

## Integration

### integration requirements

- An active Movable Ink account.
- Data Source connected to Movable Ink.
    - Either CSV, Website Import, or API.
    - Note: Ensure that you are passing data with a unifying identifier between Movable Ink and Braze (e.g external_id)

Intelligent Creative has many offerings that Braze users can take advantage of. Below is a list of what is supported. 

| Movable Ink Capability | Feature | Rich Push Notification | In-App Messaging / Content Cards | Details |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| Creative Optimizer | Display A/B Contents | ✗ | ✔ | |
|| Optimize | ✗ | ✔* | * Must Use Branch's Deeplinking solution |
| Targeting Rules | Date | ✔* | ✔ | * Supported but not recommended because push notifications are cached upon receipt and do not refresh |
|| Day of Week | ✔* | ✔ | * Supported but not recommended because push notifications are cached upon receipt and do not refresh |
|| Time of Day | ✔* | ✔ | * Supported but not recommended because push notifications are cached upon receipt and do not refresh |
| Stories/Behavior Activity | | ✔* | ✔* | * The unique user identifier used for Braze must be linked to your ESP’s identifier |
| Deep Linking within the app | | ✔* | ✔* | * Must use Branch’s deep linking solution |
| Apps | Countdown Timer | ✔* | ✔ | * Supported but not recommended because push notifications are cached upon receipt and do not refresh |
|| Polling | ✗ | ✔* | * After voting, will leave the app to be a mobile landing page |
|| Scratch Off | ✔* | ✔* | * On click, will leave the app for the Scratch Off experience |
|| Video | ✔* | ✔* | * Animated GIFs only, <br>For Android, Braze requires [GIF support][GIFsupport] in implementation |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### Use cases
- Personalized monthly or end of year recaps.
- Dynamically personalize images for email, push, or rich notifications based on last known behavior.<br>
	For Example: 
	- Using a Rich Push Message to dynamically create a schedule of events by pulling data from API. 
	- Using the Countdown Timer feature to notify users when a big sale is approaching (e.g Black Friday, Valentine's Day, Holiday Deals, etc.)
	- Use the Scratch Off feature as a fun and interactive way to disburse Promo Codes.

## Implementation process

### Step 1: create a data source for movable ink

Customers will need to create a data source that can either be a CSV, Website Import, or API Integration.

![datasource]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs %}
{% tab CSV Data Source %}
- __CSV Data Source__: Each row must have at least one segment column and one content column. After your CSV has uploaded, select which columns should be used to target the content. [Example CSV File]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![datasource]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Website Data Source %}
- __Website Data Source__: Each row must have at least one segment column and one content column. After your CSV has uploaded, select which columns should be used to target the content.
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

### Step 2: create a campaign on the movable ink platform

1. ![create_campaign]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}
From the Movable Ink home screen, you can choose to create a campaign. You can select from either Email from HTML, Email from Image, or a Block that can be used in any channel including Push, In-App Message, and Content Cards (suggested).
We also suggest taking a look at the various content options available through creating a campaign using blocks.<br><br>
2. Movable Ink has an easy editor for customers to drag and drop elements like text, image, etc. <br><br>Given that the customer has populated their data source, they can also dynamically generate an image using the data properties. In addition, they can also create fallbacks within this flow for users in the event that the campaign is sent and a user doesn't fit within the personalization criteria.<br>![create_campaign2]({% image_buster /assets/img/movable_ink/create_campaign2.png %})Customers can also preview the dynamic images and test out the query parameters to see what the images will look upon view. <br><br>For more information on how to use the Movable Ink Platform, check out [Movable Ink Support Center][support]

Once complete, you should be able to generate a dynamic URL that you can then insert into Braze!

### Step 3: obtain movable ink content url

To include Movable Ink content into Braze messages, you must locate the source URL movable ink has provided you. 

1. ![obtain_url]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="float:right;max-width:40%;margin-left:15px;"}
To obtain the source URL, you must have set up the content in the Movable Ink Dashboard, and then from there, Finish & Export your content.
2. On the Finish page, copy the source URL(`img src`) from the creative tag.
3. In the Braze Platform, paste the URL in the appropriate field. Check out the next step to see appropriate fields. 
4. Be sure to replace any merge tags (i.e. {% raw %}```&mi_u=%%email%%```{% endraw %}) with the corresponding Liquid variable (i.e. {% raw %}```&mi_u={{${email_address}}}```{% endraw %}).

### Step 4: braze experience

#### Push notifications

1. In the Braze Platform:
	- __Android Push__: Paste the URL in the __Push Icon Image__ and __Expanded Notification Image__ fields.
	- __iOS Push__: Paste URL in __Rich Notification Media__ link field, and directly below, denote the file format you are using.
	- __Web Push__: Paste the URL in the __Push Icon Image__ and __Large Notification Image__ fields.
2. In order to make sure images are not cached, prepend the URL in the message with empty Liquid tags: <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}

#### In-App Messages and Content Cards

1. In Braze’s platform, paste the URL in the __Rich Notification Media__ field.
2. __Provide a Unique URL to help Prevent Caching.__ To ensure that Movable Ink’s real-time images work and will not be affected by caching, use Liquid to append a timestamp to the end of the Movable Ink image URL. <br> To do this, use the following syntax, replacing the image URL as needed:<br>{% raw %} ```{% assign timestamp = "now" | date: "%s" %}``` <br> ```{% assign img = "https://movable-ink-image-url-goes-here" |  append:timestamp %} {{img}}``` {% endraw %} <br>This template will take the current time (in seconds), append it to the end of the Movable Ink image tab (as a query param), and then output the final result. You can preview it's working with the "Test" tab on the right of the Compose tab - this will evaluate the code and show a preview.
3. __Re-Evaluate Segment Membership__. Enable the `Re-evaluate Segment membership` option located on the "Target Users" step of a campaign. If this is option is not available, reach out to your Customer Success Manager. This option will instruct Braze SDKs to re-request the campaign each time an In-App Message is triggered. It's needed because ordinarily the Liquid code is evaluated just once at send-time, and we need a unique URL every time the message is shown.

## Troubleshooting
__dynamic images not showing correctly? what channel are you experiencing difficulties with?__<br>
- __Push__: Make sure that you have empty logic before your Movable Ink image URL: <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}
- __In-App Messages and Content Cards__: Make sure that the image URL will be unique for each impression. This can be done by appending the appropriate Liquid so that each URL is different. See [In-App and Content Card Messages Instructions][Instructions]. 
- __Image Not Loading__: Be sure to replace any "merge tags" from with the corresponding Liquid fields in the Braze dashboard. For example: {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u=%%email%%```{% endraw %} with {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}```{% endraw %}.
<br><br>

__Having trouble showing GIFs on Android?__<br>
- Android requires [GIF support][GIFsupport] in implementation. If you do not have this setup, follow the instructions to do so [here][GIFsupport].

[1]: https://movableink.com/
[datasource]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[support]: https://support.movableink.com/
[GIFsupport]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#gifs-IAMs
[Instructions]: {{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink/#step-4-braze-experience


