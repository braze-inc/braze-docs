---
nav_title: Content Cards Beta
permalink: /content_cards/
---

# Content Cards Overview

With Content Cards, you can send a highly targeted, dynamic stream of rich content to your customers right within the apps they love, without interrupting their experience. In addition, Content Cards support more personalized features, including card pinning, card dismissal, API-based delivery, custom card expiration times, card analytics, and easy coordination with push notifications. Braze's Content Cards beta is currently scheduled to begin in August of 2018. Note that any of the features described below could be subject to change throughout the course of the beta.


Braze provides a default UI (pictured below) for Content Cards:

![Default Feed][5]


However, Content Cards are also highly customizable - here's an example of what a custom implementation of Content Cards could look like:

![Content Card Feed][1]

## Content Cards Improvements

Content Cards is an improved version of Braze's News Feed product. Here's what we improved:

- Content Cards is no longer a separate tab in the dashboard, making it easy to treat it as any other channel within your cross-channel campaigns.
- Multi-variate testing is now available for Content Cards. Run the same tests across all channels.
- Analytics are more detailed. We now display conversions and unique recipients and support engagement reports.
- Take your campaign orchestration to the next level with improved scheduling capabilities. For example, send an API triggered card after a customer’s first purchase.
- Preview your Content Cards before launch by sending yourself a test from the message composer.

## Content Cards Use Cases and Best Practices

1. Use Content Cards to help make your app feel dynamic and regularly updated by showcasing new content.
2. Coordinate a Content Card with each push message such that customers have a persistent record of promotions and customers without pushes enabled have access to promotions.
3. Trigger a content card when a customer performs a custom event.
4. Trigger content cards via API and use api trigger properties for personalization - for example, add an order confirmation to a user’s Content Cards.
5. Take advantage of the visual space by incorporating images and graphics that stand out.
6. Customize Content Cards to reflect your brand’s identity and create a seamless app experience.
7. Develop a schedule for campaigns like onboarding etc., and determine the proper cadence and frequency of messaging.


## Sending Content Cards

Content Cards can be sent in multivariate and multichannel campaigns. Content Cards can be scheduled, API triggered or triggered by an event. When a Content Card is sent to a user, it will be added to that user's queue of available Content Cards. When users navigate to their Content Cards feed, they can browse through their available Content Cards.


Content Card sending is similar to email and push sending:

- Segmentation is evaluated at the time that the Content Card is sent
- Personalization is templated at the time that the content card is sent
- Once sent, Content Cards cannot be edited (however, you can remove them from users' feeds when archiving or stopping a campaign on the Dashboard)



### Expiration Dates

Once a Content Card is sent, it can be available for a user for up to 30 days. Content Cards have configurable expiration dates - you can either choose that the card expires a certain number of days after it's sent or that it expires on a particular date and time. Note that we'll store up to 100 cards in each user's Content Cards feed.  


### Pinning a Content Card

By default, Content Cards will be displayed in chronological order, with the most recently sent cards at the top of the Content Cards feed.

At times, you might have important content that should be shown first, even if it's not the most recent card that a user has recieved. Important messages can be pinned - pinned cards will display at the top of a user's feed and cannot be dismissed by the user. Note that if more than one card in a user's feed is pinned, the pinned cards will display in chronological order. Note that Content Cards cannot be retroactively pinned or unpinned - you must select the pin option you'd like to use before they are sent to users.

Also note that with a custom integration, it's possible to customize the order in which cards display.

![Content_Cards_Expiry][3]

### Previewing and Testing

Before sending out a Content Card to your users, you may want to test it to make sure it looks right and operates in the intended manner. Creating and sending test messages to select devices or members of your team is very simple using the tools in the dashboard. Simply send yourself or your team a test message the same way you would for any other channel. Note that test Content Cards expire after 5 minutes.

![test sending][4]

### Other Items to Note

The following capabilities are not supported for phase one of the Content Cards Beta:

- Connected Content
- Vouchers
- Frequency Capping
- Re-ordering Content Cards from the Dashboard
- Post-launch Edits  

## Content Cards Analytics

Analytics for Content Cards include sends, impressions, clicks, and dismissals. Additionally, like other campaigns, you can also view unique recipients, revenue, and conversions. You can view these stats on the campaign analytics Dashboard page, by using Engagement Reports, or through our analytics APIs.

|Metric|Definition|Details|
|---|---|---|
|Messages Sent|The number of Content Cards added to users' feeds.|Like email, a Content Card that is sent is not seen by a user until they open their Content Cards feed.|
|Total Impressions|The number of times Content Cards from a campaign have been viewed.|A user viewing a Content Card(s) from a campaign multiple times represents multiple total impressions.|
|Unique Impressions|The number of users who have viewed Content Cards from a campaign.|A user viewing a Content Card(s) from a campaign multiple times represents one unique impression.|
|Total Clicks|The number of times Content Cards from a campaign have been clicked.|A user clicking a Content Card(s) from a campaign multiple times represents multiple total clicks.|
|Unique Clicks|The number of users who have clicked Content Cards from a campaign.|A user clicking a Content Card(s) from a campaign multiple times represents one unique click.|
|Total Dismissals|The number of times Content Cards from a campaign have been dismissed.|A user dismissing a Content Card(s) from a campaign multiple times represents multiple total dismissals.|
|Unique Dismissals|The number of users who have dismissed Content Cards from a campaign.|A user dismissing a Content Card(s) from a campaign multiple times represents one unique dismissal.|
|Unique Recipients|The number of users who have viewed Content Cards from a campaign. This is based on daily sends.|A user viewing a Content Card(s) from a campaign multiple times represents one unique recipient. However, due to campaign re-eligibility, a user receiving and viewing multiple Content Cards from a campaign on different days represents multiple unique recipients (this is the difference between unique recipients and unique impressions).|
|Conversions|The number of users who, after viewing Content Cards from a campaign, perform the campaign's conversion event within the conversion window. This is based on daily sends.|The conversion window for a user begins when they view a given Content Card for the first time.|

## Migrating From News Feed to Content Cards

### Features and Functionality

Content Cards offers many capabilities that are not supported by Braze's current News Feed such as additional delivery options like action-based, API delivery, and enhanced analytics like conversion tracking.

As you plan your migration from the News Feed to Content Cards, it will be important to note the main differences between Content Cards and the News Feed:

- Content Cards segmentation is evaluated at the time messages are sent, News Feed segmentation is evaluated at the time that News Feed Cards are viewed
- Content Cards personalization is templated at the time messages are sent, News Feed card personalization is templated at the time that News Feed Cards are viewed

### Implementation

- Content Cards and the News Feed are separate products so a simple integration in your apps or website is necessary in order to use Content Cards
- If desired, existing News Feed Cards will need to be manually migrated to Content Card Campaigns when you switch from News Feed to Content Cards
- Content Cards is not intended to be used at the same time as the News Feed as it's a replacement for the News Feed
- Content Cards does not currently support categories, use cases for categories can be achieved via customization and key value pairs


[1]:{% image_buster /assets/img_archive/content_cards.png %}
[3]:{% image_buster /assets/img_archive/content_cards_expiry.png %}
[4]:{% image_buster /assets/img_archive/test_send.png %}
[5]:{% image_buster /assets/img_archive/contentcard.png %}
