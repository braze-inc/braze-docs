---
nav_title: "Push Stories"
article_title: Push Stories
page_order: 2
page_type: reference
description: "This reference article covers what Push Stories are, how to create one, as well as some frequently asked questions."
channel:
  - push

---

# Push Stories

> This reference article covers what Push Stories are, how to create one, as well as some frequently asked questions.

Push Stories are a new type of push notification introduced by Braze. This feature takes the photo carousel functionality popularized in Instagram and Facebook and allows marketers to create a carousel of pages within a push that tells a rich, cohesive story. These pages consist of an image, click action, title, and description. Your users can swipe through these pages and view the story—as told by you.

| Android Example (Expanded) | IOS Example (Expanded) |
| :-----: | :----------: |
| ![Android Preview][1] | ![IOS Preview][2] |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
On iOS SDK versions 3.13.0+, due to a change in how the SDK downloads images, a thumbnail of the first image will not show on the condensed view of the push. Ensure that your message copy prompts users to expand the push to see the images.
{% endalert %}

## Prerequisites

Users must update to the latest version of Android (version 2.2.0+) and iOS (version 3.2.0+) to receive Push Stories.

## How to use Push Stories

![Composer dropdown][6]{: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

To use Push Stories, create a [push campaign]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) and select **Push Stories** as your **Notification Type**.

### Push Story composer

To create a page, perform the following steps:

1. Click **Manage Pages** from the main composer.
    <br><br>![Manage pages][4]{: style="max-width:70%"}<br><br>
2. Insert an image for each page, along with the click behavior for that image.
3. If desired, add a **Title** and **Description** for each page. If you use a title and decription for one page, they must be inserted for all pages.

The previews will be reflected and are interactive.

![Composer Workflow][3]{: style="max-width:60%"}

{% alert important %}
If you are pulling in images with [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content), please ensure that your image URL begins with `https://`. Using `http://` will crash your app.
{% endalert %}

### Push Story segmentation

When you create a campaign or Canvas, you can filter which users you want to target based on whether they have clicked on a Push Story page. Then, select the campaign and the page you want to use to target your users.

### Push Stories analytics

![Push Story Analytics][5]

The analytics will look very similar to the current analytics section for Push Notification. The only difference is when you open the “Direct Opens” section, you can now see clicks per page.

## Troubleshooting

### I sent myself a Push Story on iOS but didn't receive the notification

Apple has specific rules in place that will prevent certain types of notifications from being sent to a device based on a number of different factors—this includes evaluating the customers' data plan, notification size, and the customers' storage capacity. As a result, sometimes no notification will be sent to your customers.

These are limitations imposed by Apple that should be considered when designing your Push Story.

### I sent myself a push story on iOS but saw the condensed view instead

In certain situations where all the pages do not load, for example, due to a loss of data connection, the Push Story will only show the condensed notification.


[1]: {% image_buster /assets/img_archive/pushstories_android_preview.png %}
[2]: {% image_buster /assets/img_archive/pushstories_ios_preview.png %}
[3]: {% image_buster /assets/img_archive/pushstories_composer.png %}
[4]: {% image_buster /assets/img_archive/pushstories_add_pages.png %}
[5]: {% image_buster /assets/img_archive/pushstories_analytics.png %}
[6]: {% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}
