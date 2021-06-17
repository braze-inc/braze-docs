---
nav_title: "Push Stories"
page_order: 2
page_type: reference
description: "This reference article covers what Push stories are, how to create one as well as some frequently asked questions."

channel:
  - Push
tool:
  - Docs
  - Dashboard
  - Campaigns
---

# Push Stories

> Push Stories is a new type of Push Notification introduced by Braze. It allows customers to send down multiple ‘pages’, which consists of an image, click action, title, and description to a device. The users can iterate through these pages and go through the 'story' as told by each marketer.


| Android Example (Expanded) | IOS Example (Expanded) |
| :-----: | :----------: |
| ![AndroidPreview][1] | ![IOSPreview][2] |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
On iOS SDK versions 3.13.0+, due to a change in how the SDK downloads images, a thumbnail of the first image will not show on the condensed view of the push. You should ensure that your message copy prompts users to expand the push to see the images.
{% endalert %}

__Prerequisites__: Users must update to the latest version of Android(version:2.2.0+) and iOS (version: 3.2.0+)

## Dashboard Changes

![Composerdropdown][6]{: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}
Within the campaign set up dashboard, once you have selected what Push Message Variants you want, you must select __Push Stories__ as the notification type for the Push Story Composer to appear. 

### New Composer
![composerworkflow][3]

The Push Story composer is controlled by a drop-down at the top. You can choose to send a Standard Push Notification as you would today or send a Push Story Notification instead.

To create a page:

* Click “Manage Pages” from the main composer.
* Insert an image for each page, along with the click behavior for that image.
* Title/Description for each page can also be inserted (if inserted for one page, they must be inserted for all pages).
* The previews will be reflected and are interactive.

{% alert important %}
If you are pulling in images with [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content), please ensure that your image URL begins with `https://`. Using `http://` will crash your app.
{% endalert %}

### Push Stories Analytics

![pushstoriesanalytics][5]

The analytics will look very similar to the current analytics section for Push Notification. The only difference is when you open the “Direct Opens” section, you can now see clicks per page.


## FAQs

### Can I target users who clicked a particular page in the Push Story?
Push Story Segmentation is now available! When you create a Campaign or Canvas, you can filter which users you want to target based on whether they have clicked on a Push Story Page. Then, select the Campaign and the page you want to use to target your users.


###  I sent myself a Push Story on iOS but did not receive the notification - what happened?
Apple has specific rules in place that will prevent certain types of notifications from being sent to a device based on a number of different factors - this includes evaluating the customers' data plan, notification size and/or the customers' storage capacity.  As a result, sometimes no notification will be sent to your customers. These are limitations imposed by Apple that should be considered when designing your Push Story.


### I sent myself a Push Story on iOS but saw the condensed view instead - what happened?
In certain situations where all the pages do not load, for example, due to a loss of data connection, the Push Story will only show the condensed notification.


[1]: {% image_buster /assets/img_archive/pushstories_android_preview.png %}
[2]: {% image_buster /assets/img_archive/pushstories_ios_preview.png %}
[3]: {% image_buster /assets/img_archive/pushstories_composer_setup.gif %}
[5]: {% image_buster /assets/img_archive/pushstories_analytics.png %}
[6]: {% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}
