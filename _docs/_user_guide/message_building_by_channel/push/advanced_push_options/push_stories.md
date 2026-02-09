---
nav_title: "Push stories"
article_title: Push Stories
page_order: 2
page_type: reference
description: "This reference article covers what Push Stories are, how to create one, as well as some frequently asked questions."
channel:
  - push

---

# Push Stories

> Push Stories are a new type of push notification introduced by Braze. This feature takes the photo carousel functionality popularized in Instagram and Facebook and allows marketers to create a carousel of pages within a push that tells a rich, cohesive story. These pages consist of an image, click action, title, and description. Your users can swipe through these pages and view the story—as told by you.

| Android Example (Expanded) | IOS Example (Expanded) |
| :-----: | :----------: |
| ![]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | ![]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
On iOS SDK versions 3.13.0+, due to a change in how the SDK downloads images, a thumbnail of the first image will not show on the condensed view of the push. Ensure that your message copy prompts users to expand the push to see the images.
{% endalert %}

## Prerequisites

The following SDK versions are required to receive Push Stories:

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## How to use Push Stories

![]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

To use Push Stories, do the following:

1. Create a [push campaign]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/).
2. For your **Notification Type**, select **Push Stories**.
3. Select **iOS** or **Android**. Note that if you select both for a push message, the option to create a Push Story won't appear. 

### Push Story composer

To create a page, perform the following steps:

1. Click **Manage Pages** from the main composer.
    <br><br>![]({% image_buster /assets/img_archive/pushstories_add_pages.png %}){: style="max-width:70%"}<br><br>
2. Insert an image for each page, along with the click behavior for that image.
3. If desired, add a **Title** and **Description** for each page. If you use a title and description for one page, they must be inserted for all pages.

The previews will be reflected and are interactive.

![]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
If you are pulling in images with [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content), ensure that your image URL begins with `https://`. Using `http://` will crash your app.
{% endalert %}

### Image and text specifications

The following image and text specifications apply to the photo carousel portion of Push Stories. For information on the basic push that users interact with to activate the Push Story, refer to the [text guidelines for push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#native-mobile-push-notifications).

{% tabs %}
{% tab Images %}

- **Image ratio:** 2:1 (required)
- **Recommended image size:** 500 KB
- **Maximum image size:** 5 MB
- **File types:** PNG, JPEG

{% endtab %}
{% tab Text %}

- **Title:** 30 characters (recommended)
- **Description:** 30 characters (recommended)

{% alert note %}
While there may be some variance in character length from device to device, the title and description for Push Stories are limited to one line each. The remainder of your message will be truncated. Always test your message on a real device.
{% endalert %}

{% endtab %}
{% endtabs %}

### Push Story segmentation

When you create a campaign or Canvas, you can filter which users you want to target based on whether they have clicked on a Push Story page. Then, select the campaign and the page you want to use to target your users.

### Push Stories analytics

The analytics will look very similar to the current analytics section for push notifications. For Push Stories analytics, you can open the **Direct Opens** metric to view the clicks per page.

![iOS Push Performance table with sample analytics and expanded details for the Direct Opens metric.]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## Troubleshooting

### iOS

#### I sent myself a Push Story but didn't receive the notification

Apple has specific rules in place that will prevent certain types of notifications from being sent to a device based on a number of different factors. This includes evaluating the customers' data plan, notification size, and the customers' storage capacity. As a result, sometimes no notification will be sent to your customers.

These are limitations imposed by Apple that should be considered when designing your Push Story.

#### I sent myself a Push Story but saw the condensed view instead

In certain situations where all the pages do not load, for example, due to a loss of data connection, the Push Story will only show the condensed notification.

### Android

#### Push Story doesn't dismiss after clicking the image 

By default, Push Stories are not dismissed on Android after a user clicks on the image. If you'd like to dismiss the notification, call [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721).  

