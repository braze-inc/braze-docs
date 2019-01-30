---
nav_title: Push Stories
platform: Message_Building_and_Personalization
subplatform: Push
page_order: 2
---

# Push Stories

Push Stories is a new type of Push Notification introduced by Braze (formerly known as Appboy). It allows customers to send down multiple ‘pages’, which consists of an image, click action, title, and description to a device. The users can iterate through these pages and go though the 'story' as told by each marketer.


| Android Example (Expanded) | IOS Example (Expanded) |
| :-----: | :----------: |
| ![AndroidPreview][1] | ![IOSPreview][2] |


## How it works
_Pre-req: Clients must update to the latest version of Android(version:2.2.0+) and IOS (version: 3.2.0+)_

## Dashboard Changes
![Composerdropdown][6]


### New Composer
![composerworkflow][3]

The Push Story composer is controlled by a drop down at the top. You can choose to send a Standard Push Notification as you would today or send a Push Story Notification instead.

To create a page:

* Click “Manage Pages” from the main composer.
* Insert an image for each page, along with the click behavior for that image.
* Title/Description for each page can also be inserted (if inserted for one page, they must be inserted for all pages).
* The previews will be reflected and are interactive.

### Push Stories Analytics

![pushstoriesanalytics][5]

The analytics will look very similar to the current analytics section for Push Notification. The only difference is when you open the “Direct Opens” section, you can now see clicks per page.


## FAQs

### Can I target users who clicked a particular page in the Push Story?
Push Story Segmentation is now available! When you create a Campaign or Canvas, you can filter which users you want to target based on whether they have clicked on a Push Story Page. Then, select the Campaign and the page you want to use to target your users.


###  I sent myself a Push Story on iOS but did not receive the notification - what happened?
Apple has specific rules in place that will prevent certain types of notifications from being sent to a device based on a number of different factors - this includes evaluating the customers data plan, whether the app was forced-closed, notification size and/or the customers storage capacity.  As a result, sometimes no notification will be sent to your customers. These are limitations imposed by Apple that should be considered when designing your Push Story.


### I sent myself a Push Story on iOS but saw the condensed view instead - what happened?
In certain situations where all the pages do not load, for example due to a loss of data connection, the Push Story will only show the condensed notification.


[1]: {% image_buster /assets/img_archive/pushstories_android_preview.png %}
[2]: {% image_buster /assets/img_archive/pushstories_ios_preview.png %}
[3]: {% image_buster /assets/img_archive/pushstories_composer_setup.gif %}
[4]: {% image_buster /assets/img_archive/pushstories_composer_dropdown.png %}
[5]: {% image_buster /assets/img_archive/pushstories_analytics.png %}
[6]: {% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}
