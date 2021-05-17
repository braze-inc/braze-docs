---
nav_title: Creating a News Feed Item
page_order: 3
description: "News-Feed items allow you to insert permanent content directly into your app from our web dashboard. This reference article covers how to create a News Feed item. "
---
# Creating a News Feed Item

News-Feed items allow you to insert permanent content directly into your app from our web dashboard. Better yet, the news feed also is targetable to individual segments just like all of our other message types. This means what you see in the feed might be completely different from another individual. The possibilities for the news-feed are nearly limitless.

To see examples of News Feeds and helpful tips, check out our [Client Integration Gallery][13], [use case][15], and [best practice][16] docs. 

## Step 1: Click Create Card

First, you must choose the type of News Feed item you want to send down to your users. From the dropdown menu, you can select any of our four News Feed card types.

![Newsfeed1][1]

### News Feed Card Specifications

#### News Feed Cards

![Classic Card][2]

Standard news feed cards consist of:

- 110x110 image
- Title
- Body Text
- Link (In-App/Web)

#### Captioned Image Cards

![Captioned Image][3]

Captioned Image cards consist of:

- 600x450 image
- Title
- Body Text
- Link (In-App/Web)

#### Banner Cards

![NewsFeedBanner][4]

Banner cards consist of:

- 600x100 image
- Link (In-App/Web)

#### Image guidelines

|          Card type         |          Aspect Ratio         | Recommended Image Size | Maximum Image Size |   File Types  |
|:-----------------------------:|:----------------------:|:------------------:|:-------------:|
|          Classic         | 1:1 (110 pixels wide minimum) |          500KB         |         1MB        | PNG, JPG, GIF |
|          Captioned image         | 4:3 (600 pixels wide minimum) |          500KB         |         1MB        | PNG, JPG, GIF |
|          Banner         | 6:1 (600 pixels wide minimum) |          500KB         |         1MB        | PNG, JPG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

- PNG files are recommended.
- A custom image loading library is required to display Gifs on Android. We recommend Glide.
- Smaller, high-quality images will load faster, so it’s recommended to use the smallest asset possible to achieve your desired output.


## Step 2: Add a Title, Summary, Image, and Links

![News Feed Title Summary][6]

Time to compose your News Feed card! Create a title and summary for your card and upload an image to go alongside it. You can also set link behavior on this page. This link can be a standard link or a ["Deep Link"][7] to in-app content.

## Step 3: Select A Schedule

![News Feed Schedule][8]

Below the News Feed Card editor, you will find options for when to publish this item. You can choose to publish it immediately after creation or set a time in the future to publish it. You can also choose to deliver the News Feed card at a particular time in your users' local time by selecting the "Publish to Users in their Local Time Zone" checkbox.

## Step 4: Select a Segment

You can configure your News Feed Card to target any [segment][10] you've defined within the dashboard at any schedule you desire. Select your target segment by clicking on the dropdown menu. Here you can see high-level statistics, including email availability and lifetime value per user.

![Target Segment][11]

## Step 5: Review Details and Publish

Next, you will be taken to a page that displays all of the details about your card (and companion In-App message, if applicable). You can review any of the details about these items and edit them if you need to by clicking the pencil icon in any of the headers.

![News Feed Preview][12]

That's it! You're done! You've published your first news-feed card!

## Optional: Link a News Feed Card to an In-App Message

![Linked In App][14]

Multi-Channel campaigns often lead to better overall conversion and engagement rates, so Braze has made it easy to link an in-app message to a specific news feed card. After launching a news feed card, a button will appear in the new feed statistics page allowing you to "create an associated in-app message." Clicking on this will take you to the campaign composer for a new in-app message campaign. While you would input the copy, look, and feel of the in-app message, Braze automatically copies the delivery and targeting rules of the associated news feed card to make sure the campaigns launch together.

## Organizing your News Feed

You can re-order your cards within Braze's News Feed page.
- Cards in the feed are ordered first by whether or not they have been seen by the user, unseen items are at the top of the feed.
  - A card is considered read if it has received an impression in the feed.
  - Impressions are only counted if the card is viewable in the feed (ie, if a user does not scroll down to read a card, an impression is not counted).
- Cards are then ordered by the date and time of creation, where more recent items are first.

[1]: {% image_buster /assets/img_archive/newsfeed1_new.png %}
[2]: {% image_buster /assets/img_archive/classiccard.png %}
[3]: {% image_buster /assets/img_archive/captionedimage.png %}
[4]: {% image_buster /assets/img_archive/newsfeedbanner.png %}
[6]: {% image_buster /assets/img_archive/news-feed-title-summary_new.png %}
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-linking-to-app-settings
[8]: {% image_buster /assets/img_archive/newsfeed2_new.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[11]: {% image_buster /assets/img_archive/targetsegment_new.png %}
[12]: {% image_buster /assets/img_archive/newsfeedpreview_new.png %}
[13]: {{site.baseurl}}/help/best_practices/client_integration_gallery/#client-integration-newsfeed
[14]: {% image_buster /assets/img_archive/linked-in-app_new.png %}
[15]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/news_feed_use_cases/
[16]: {{site.baseurl}}/help/best_practices/news_feed/#news-feed-best-practices
