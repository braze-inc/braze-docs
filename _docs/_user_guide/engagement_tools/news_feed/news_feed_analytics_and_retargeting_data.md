---
nav_title: News Feed Analytics
article_title: News Feed Analytics and Retargeting Data
page_order: 10
page_type: reference
description: "This reference article covers News Feed analytics, and various related filters."
tool: 
- Reports
channel: news feed

---

# Analytics

Similar to scheduled campaigns, the News Feed tool comes with an analytics dashboard to monitor impressions, clicks, and clickthrough rates. Clicking on a specific News Feed message in your dashboard brings up a host of visual analytics to sort through. At the top of the page, you can select your data date range and see a quick visualization of your most important metrics. Additionally, you can see specifics about this News Feed message, such as when it was sent and who it was sent to.

![newsfeed_analytics_top][19]

By scrolling down the page, you can see a larger breakdown of your clicks and impressions day-by-day. Total clicks/impressions are easily compared with unique clicks/impressions through line charts, while a clickthrough rate is presented as an interactive bar chart.

![newsfeed_analytics_bottom][20]

# Retargeting Data

You can leverage Braze's data on which users are interacting with your News Feed via segment filters that let you retarget specific behaviors.

## Feed Impression Filter

Braze automatically tracks when users view the feed and how many times they have viewed it. There are two filters available:

- Last Viewed News Feed
- News Feed View Count

'Last Viewed News Feed' is an effective way to use other channels to draw users back into the feed. This can be easily done with push and in-app notifications. Braze has seen over 100% increases in News Feed impressions with effective targeting. As awareness of the feed increases, these benefits are sustained.

'News Feed View Count' can be used to target users who have never viewed the feed or seldom viewed the feed to encourage more impressions of your cards.

Consider, using these filters in tandem or with other filters to create an even more targeted call to action.

## Clicked Card Filter

You can create segments based on how users have interacted with specific cards in the feed. The filter is in the Retargeting section of the filter list and called Clicked Card.

## Has Clicked Card Filter

- Works well to retarget users who have clicked on a card, but not followed through on your call to action.
- It is also useful to retarget users with related content that may of interest to them.
- You can also use this filter to target users that did not click a card. This filter can be applied to specific cards so that they disappear from a user's feed after they click on them.
  - To set this up, after you create a card go back and edit the target segment to include 'Has not clicked YOUR NEW CARD'.
  - After a user clicks the card, the card will automatically leave the feed when the user's next session starts.
  - Avoid over-using this targeting because user's may end up with empty feeds. Best practice is to use a combination of static and automatically removed content.
- It also works well to retarget users who do not click on a card to follow up with another call to action.

![has not clicked card][14]


[19]: {% image_buster /assets/img_archive/braze_newsfeedanalytics.png %}
[20]: {% image_buster /assets/img_archive/braze_newsfeedanalytics2.png %}
[14]: {% image_buster /assets/img_archive/braze_newsfeedsegment.png %}
