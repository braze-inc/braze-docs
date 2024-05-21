---
page_order: 1.2
nav_title: セグメンテーションフィルター
article_title: セグメンテーションフィルター
layout: glossary_page
glossary_top_header: "Segmentation Filters"
glossary_top_text: The Braze SDK provides you with a powerful arsenal of filters to segment and target your users based off of specific features and attributes. You can search or narrow these filters by filter category.<br><br>To learn about the different custom attribute data types you can use to segment users, view <a href="/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types">Custom attribute data types</a>.

page_type: glossary
tool: Segments
description: "この用語集には、ユーザーをセグメント化およびターゲット化するための使用可能なフィルターが一覧表示されています。"
search_rank: 2
glossary_tag_name: Filter Category
glossary_filter_text: "Select a category to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Segment or CSV membership
  - name: Custom attributes
  - name: Custom events
  - name: Sessions
  - name: Retargeting
  - name: Channel subscription behavior
  - name: Purchase behavior
  - name: Demographic attributes
  - name: App
  - name: Uninstall
  - name: Devices
  - name: Location
  - name: Cohort membership
  - name: Install attribution
  - name: Intelligence and predictive
  - name: Social activity
  - name: Other Filters

glossaries:
  - name: Segment Membership
    description: Allows you to filter based on segment membership anywhere that filters are used (such as segments, campaigns, and others) and target multiple different segments within one campaign. <br><br>Note that segments already using this filter cannot be further included/nested into other segments. You must recreate the segment you're trying to include by using the same filters.
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    description: After creating a Segment Extension in the Braze dashboard, you can choose to include/exclude those extensions in your segment.
    tags:
      - Segment or CSV membership
  - name: Updated/Imported from CSV
    description: Segments your users based on whether they were a part of a CSV upload or not.
    tags:
      - Segment or CSV membership
  - name: Custom Attributes
    description: Determines whether or not a user matches a custom recorded attribute value. (24-hour period) <br><br>Time zone:<br>Company's Time Zone
    tags:
      - Custom attributes
  - name: Nested Custom Attributes
    description: Attributes that are the properties of custom attributes.<br><br>When filtering a nested time custom attribute, you can choose to filter based on "Day of Year" or "Time". "Day of Year" will check only the month and day for comparison. "Time" will compare the full timestamp, including the year.
    tags:
      - Custom attributes
  - name: Day of Recurring Event
    description: This filter looks at the month and day of custom attribute with the data type of "date", but does not look at the year. This filter is useful for annual events.<br><br>Time zone&#58;<br>This filter adjusts for whatever time zones the user is in.
    tags:
      - Custom attributes
  - name: Custom Event
    description: Determines whether or not a user has performed a specially recorded event.<br><br> Example:<br>Activity completed with property activty_name.<br><br>Time zone:<br>UTC - Calendar Day = 1 calendar day will look at 24-48 hours of user history
    tags:
      - Custom events
  - name: First Did Custom Event
    description: Determines the earliest time that a user has performed a specially recorded event. (24-hour period) <br><br>Example:<br> First Abandoned Cart Less than 1 day ago<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Custom events
  - name: Last Did Custom Event 
    description: Determines the latest time that a user has performed a specially recorded event. (24-hour period) <br><br>Example:<br> Last Abandoned Cart Less than 1 day ago<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Custom events
  - name: X Custom Event In Y Days
    description: Determines whether or not a user has performed a specially recorded event between 0 and 50 times in the last specified number of calendar days between 1 and 30. (Calendar Day = 1 calendar day will look at 24-48 hours of user history)<br> <a href="/docs/x-in-y-behavior/"> Learn more about X-in-Y behavior here.</a> <br><br>Example:<br>Abandoned Cart exactly 0 times in the last 1 calendar day<br><br>Time zone:<br>UTC - To account for all time zones, 1 calendar day will look at 24-48 hours of user history, depending on the time the segment is evaluated; for 2 calendar days, will look at 48-72 hours of user history, and so on.
    tags:
      - Custom events
  - name: X Custom Event Property In Y Days
    description: Determines whether or not a user has performed a specially recorded event in relation to a specific property between 0 and 50 times in the last specified number of calendar days between 1 and 30. (Calendar Day = 1 calendar day will look at 24-48 hours of user history)<br><a href="/docs/x-in-y-behavior/">Learn more about X-in-Y behavior here.</a> <br><br>Example:<br> Added to Favorites w/ property "event_name" exactly 0 times in the last 1 calendar day<br><br>Time zone:<br>UTC - To account for all time zones, 1 calendar day will look at 24-48 hours of user history, depending on the time the segment is evaluated; for 2 calendar days, will look at 48-72 hours of user history, and so on.
    tags:
      - Custom events
  - name: Email Address 
    description: Allows you to designate your campaign recipients by individual email addresses for testing. This can also be used to send transactional emails to all your users (including unsubscribed) using the "Email Address is not Blank" specifier within the filter.
    tags:
      - Other Filters
  - name: External User ID
    description: Allows you to designate your campaign recipients by individual user IDs for testing.
    tags:
      - Other Filters
  - name: "Random Bucket #"
    description: Segments your users by a randomly assigned number (0 to 9999 inclusive). It can enable the creation of uniformly distributed segments of truly random users for A/B and multivariate testing.
    tags:
      - Other Filters
  - name: Session Count
    description: Segments your users by the number of sessions they have had in any of your apps within your workspace.
    tags:
      - Sessions
  - name: Session Count For App
    description: Segments your users by the number of sessions they have had in a specific, designated app.
    tags:
      - Sessions
  - name: X Sessions In Last Y Days
    description: Segments your users by the number of sessions (between 0 and 50) they have had in your app in the last specified number of calendar days between 1 and 30. <br> <a href="/docs/x-in-y-behavior/">Learn more about X-in-Y behavior here.</a>
    tags:
      - Sessions
  - name: First Used App
    description: Segments your users by the earliest recorded time that they opened your app. <em>Note that this will capture the first session they have using a version of your app with the Braze SDK integrated.</em> (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Sessions
  - name: First Used Specific App
    description: Segments your users by the earliest recorded time that they opened any of your apps within your workspace. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Sessions
  - name: Last Used App
    description: Segments your users by the most recent time that they have opened your app. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Sessions
  - name: Last Used Specific App
    description: Segments your users by the most recent time that they have opened a specific, designated app. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Sessions
  - name: Median Session Duration
    description: Segments your users by the median length of their sessions in your app.
    tags:
      - Sessions
  - name: Received Message from Campaign
    description: 
    tags:
      - Retargeting
  - name: Received Campaign Variant
    description: Segments your users by which variant of a multivariate campaign they have received.
    tags:
      - Retargeting
  - name: Received Message from Canvas Step
    description: Segments your users by whether or not they have received a specific Canvas component.
    tags:
      - Retargeting
  - name: Last Received Message from Specific Canvas Step
    description: Segments your users by when they received a specific Canvas component.
    tags:
      - Retargeting
  - name: Last Received Message from Specific Campaign
    description: Segments your users by whether or not they have received a specific campaign.
    tags:
      - Retargeting
  - name: Received Message from Campaign or Canvas with Tag
    description: Segments your users by whether or not they have received a specific campaign or Canvas with a specific tag.
    tags:
      - Retargeting
  - name: Last Received Message from Campaign or Canvas With Tag
    description: Segments your users by when they received a specific campaign or Canvas with a specific tag. (24-hour period)
    tags:
      - Retargeting
  - name: Has Never Received a Message from Campaign or Canvas Step
    description: Segments your users by whether or not they have received any campaign or Canvas component.
    tags:
      - Retargeting
  - name: Last Received Email
    description: Segments your users by the last time that they have received one of your email messages. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last Received Push
    description: Segments your users by the last time that they received one of your push notifications. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last In App Message Impression
    description: Segments your users by the last time they viewed an in-app message.
    tags:
      - Retargeting
  - name: Last Received SMS
    description: Segments your users by the last time that they have received an SMS. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last Received Webhook
    description: Segments your users by the last time that Braze sent a webhook for that user. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last Received WhatsApp
    description: Segments your users by the last time that they have received a WhatsApp message. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last Viewed News Feed
    description: Segments your users by the last time they viewed News Feed.
    tags:
      - Retargeting
  - name: News Feed View Count
    description: Segments your users by how many times they viewed News Feed.
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign
    description: Filter by interaction with a specific campaign.
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    description: Filter by interaction with a specific campaign that has a specific tag.
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    description: Filter by interaction with a specific Canvas component.
    tags:
      - Retargeting
  - name: Clicked Alias in Campaign
    description: Filter your users by whether they clicked a specific alias in a specific campaign.
    tags:
      - Retargeting
  - name: Clicked Alias in Canvas Step
    description: Filter your users by whether they clicked a specific alias in a specific Canvas.
    tags:
      - Retargeting
  - name: Clicked Alias in Any Campaign or Canvas Step
    description: Filter your users by whether they clicked a specific alias in any campaign or Canvas.
    tags:
      - Retargeting
  - name: Hard Bounced
    description: Segment your users by whether or not their email address has hard bounced (such as the email address is invalid).
    tags:
      - Retargeting
  - name: Has Marked You As Spam
    description: Segments your users by whether or not they have marked your messages as spam.
    tags:
      - Retargeting
  - name: Invalid Phone Number 
    description: Segments your users by whether or not their phone number is invalid.
    tags:
      - Retargeting
  - name: Last Sent Specific SMS Inbound Keyword Category
    description: Segments your users by when they last sent an SMS to a specific subscription group within a specific keyword category.
    tags:
      - Retargeting
  - name: Converted From Campaign
    description: Segments your users by whether or not they have converted on a specific campaign. This filter doesn't include users that are in the control group.
    tags:
      - Retargeting
  - name: Converted From Canvas
    description: Segments your users by whether or not they have converted on a specific Canvas. This filter doesn't include users that are in the control group.
    tags:
      - Retargeting
  - name: In Campaign Control Group
    description: Segments your users by whether or not they were in the control group for a specific multivariate campaign.
    tags:
      - Retargeting
  - name: In Canvas Control Group
    description: Segments your users by whether or not they were in the control group for a specific Canvas.
    tags:
      - Retargeting
  - name: Last Enrolled in Any Control Group
    description: Segments your users by the last time that they fell into the control group in a campaign. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    description: Segments your users by whether or not they have entered a variation path of a specific Canvas.
    tags:
      - Retargeting
  - name: Last Received Any Message
    description: Segments your users by determining the last message that was received. (24-hour period)<br><br>Example:<br>Last Received Message Less than 1 Day ago = less than 24 hours ago<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last Engaged With Message
    description: Segments your users by the last time that they have clicked or opened one of your messaging channels (email, in-app, push). Includes option to filter by machine opens or other opens for email messages. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Clicked card 
    description: Segments your users by whether or not they have clicked a specific Content Card. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Feature Flags
    description: The segment of your users that have a particular <a href="/docs/developer_guide/platform_wide/feature_flags/about">feature flag</a> currently enabled.
    tags:
      - Retargeting
  - name: Subscription Group
    description: Segments your users by their subscription group for email or SMS/MMS. Archived Groups will not appear and cannot be used.
    tags:
      - Channel subscription behavior
  - name: Email Available
    description: Segments your users by whether or not they have a valid email address, and if they are subscribed/opted-in to email. The email available filter checks for three criteria&#58; if the user is unsubscribed from emails, if Braze has received a hard bounce, and if the email was marked as spam. If any of these criteria are met, or if an email doesn't doesn't exist for a user, the user will not be included.
    tags:
      - Channel subscription behavior
  - name: Email Opt In Date
    description: Segments your users by the date on which they opted into email.
    tags:
      - Channel subscription behavior
  - name: Email Subscription Status
    description: Segments your users by their subscription status for email.
    tags:
      - Channel subscription behavior
  - name: Email Unsubscribed Date 
    description: Segments your users by the date on which they unsubscribed from future emails.
    tags:
      - Channel subscription behavior
  - name: Push Enabled
    description: Segments your users who have provisional push authorization or are enabled for foreground push. Specifically, this count includes:<br>1. iOS users who are provisionally authorized for push. <br>2. Users who explicitly activated push notifications for any of the apps in your workspace. For these users, this count includes only foreground push.<br><br>Push Enabled does not include users who have unsubscribed. <br><br>After segmenting with this filter, you will be able to see a breakdown of who is in that segment for Android, iOS, and web in the bottom panel, called <em>Reachable Users</em>.
    tags:
      - Channel subscription behavior
  - name: Push Enabled For App
    description: Segments by whether users have push enabled for your app on their device. These users are reachable via push but might not be opted in. This count includes users who have provisionally authorized foreground and background push tokens.
    tags:
      - Channel subscription behavior
  - name: Background Push Enabled
    description: Segments your users on whether they have enabled background push or not.
    tags:
      - Channel subscription behavior
  - name: Push Opt In Date
    description: Segments your users by the date on which they opted into push.
    tags:
      - Channel subscription behavior
  - name: Push Subscription Status
    description: Segments your users by their <a href="/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state">subscription status</a> for push.
    tags:
      - Channel subscription behavior
  - name: Push Unsubscribed Date
    description: Segments your users by the date on which they unsubscribed from future push notifications.
    tags:
      - Channel subscription behavior
  - name: Purchased Product
    description: Segments your users by products purchased in your app.
    tags:
      - Purchase behavior
  - name: Total Number of Purchases
    description: Segments your users by how many purchases they have made in your app.
    tags:
      - Purchase behavior
  - name: X Product Purchased In Y Days
    description: Filter users by times a specific product was purchased.
    tags:
      - Purchase behavior
  - name: X Purchases in Last Y Days
    description: Segments your users by the number of times (between 0 and 50) they have made a purchase in the last specified number of calendar days between 1 and 30. <br> <a href="/docs/x-in-y-behavior/">Learn more about X-in-Y behavior here.</a>
    tags:
      - Purchase behavior
  - name: X Purchase Property In Y Days
    description: Segments your users by the number of times a purchase was made in relation to a certain purchase property in the last specified number of calendar days between 1 and 30. <br> <a href="/docs/x-in-y-behavior/">Learn more about X-in-Y behavior here.</a>
    tags:
      - Purchase behavior
  - name: First Made Purchase
    description: Segments your users by the earliest time that a user made a purchase in your app.
    tags:
      - Purchase behavior
  - name: First Purchase For App
    description: Segments your users by the earliest time that a user made a purchase from your app.
    tags:
      - Purchase behavior
  - name: Last Purchased Product
    description: Filter users by when they first purchased a specific product.
    tags:
      - Purchase behavior
  - name: Money Spent
    description: Segments your users by the amount of money that they have spent in your app.
    tags:
      - Purchase behavior
  - name: X Money Spent in Y Days
    description: Segments your users by the amount of money that they have spent in your app in the last specified number of calendar days between 1 and 30. This amount will only include the sum of the last 50 purchases. <br> <a href="/docs/x-in-y-behavior/">Learn more about X-in-Y behavior here.</a>
    tags:
      - Purchase behavior
  - name: Country
    description: Segments your users by their last indicated country location.
    tags:
      - Demographic attributes
  - name: City
    description: Segments your users by their last indicated city location.
    tags:
      - Demographic attributes
  - name: Language
    description: Segments your users by their preferred language.
    tags:
      - Demographic attributes
  - name: Age
    description: Segments your users by their age, as they indicated from within your app.
    tags:
      - Demographic attributes
  - name: Birthday
    description: Segments your users by their birthday, as they indicated from within your app. <br> Users with a birthday on the 29th of February will be included in segments including March 1.<br><br>To target December or January birthdays, only insert filter logic within the 12-month span of the year you're targeting. In other words, do not insert logic that looks back to the previous calendar year's December or forward to the next year's January. For example, to target December birthdays, you can filter for "on December 31", "before December 31", or "after November 30".
    tags:
      - Demographic attributes
  - name: Gender
    description: Segments your users by gender, as they indicated from within your app.
    tags:
      - Demographic attributes
  - name: Phone Number
    description: Segments your users by their phone number. Only use digits [0-9]. Do not include parenthesis, dashes, and similar.
    tags:
      - Demographic attributes
  - name: First Name
    description: Segments your users by their first name, as they indicated from within your app.
    tags:
      - Demographic attributes
  - name: Last Name
    description: Segments your users by their last name, as they indicated from within your app.
    tags:
      - Demographic attributes
  - name: Has App
    description: Segments by whether or not a user has ever installed your app. This will include users who currently have your app installed and those that have uninstalled in the past. This generally requires users to open the app (start a session) to be included in this filter. However, there are some exceptions, such as if a user was imported into Braze and manually associated with your app.
    tags:
      - App
  - name: Most Recent App Version Name
    description: Segments by the recent name of the user's app.
    tags:
      - App 
  - name: Most Recent App Version Number
    description: Segments by the recent app version number of the user's app.
    tags:
      - App 
  - name: Uninstalled
    description: Segments your users by whether they have uninstalled your app and have not reinstalled it.
    tags:
      - Uninstall 
  - name: Device Carrier
    description: Segments your users by their device carrier.
    tags:
      - Devices
  - name: Device Count
    description: Segments your users by how many devices they have used your app on.
    tags:
      - Devices
  - name: Device Model
    description: Segments your users by their mobile phone's model version.
    tags:
      - Devices
  - name: Device OS
    description: Segments your users that have one or more devices with the specified operating system.
    tags:
      - Devices
  - name: Most Recent Device Locale
    description: Segments your users by the <a href="/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/">locale information</a> from the most recently used device.
    tags:
      - Devices      
  - name: Most Recent Watch Model
    description: Segments your users by their most recent smartwatch model.
    tags:
      - Devices    
  - name: Provisionally Authorized on iOS
    description: Allows you to find users who are provisionally authorized on iOS 12 for a given app.
    tags:
      - Devices   
  - name: Web Browser
    description: Segments your users by the web browser they use to access your website.
    tags:
      - Devices
  - name: Device IDFA
    description: Allows you to designate your campaign recipients by IDFA for testing.
    tags:
      - Advertising use cases
  - name: Device IDFV
    description: Allows you to designate your campaign recipients by IDFV for testing.
    tags:
      - Advertising use cases 
  - name: Device Google Ad ID
    description: Segments your users by the Google ad ID.
    tags:
      - Advertising use cases
  - name: Device Roku Ad ID
    description: Segments your users by the Roku ad ID.
    tags:
      - Advertising use cases
  - name: Device Windows Ad ID
    description: Segments your users by the Windows ad ID.
    tags:
      - Advertising use cases  
  - name: Ad Tracking Enabled
    description: Allows you to filter based on if your users have opted-in to ad tracking. Ad tracking relates to the IDFA or "identifier for advertisers" assigned to all iOS devices by Apple. This identifier allows advertisers to track users and serve them targeted ads.
    tags:
      - Advertising use cases
  - name: Most Recent Location
    description: Segments your users by the last recorded location at which they have used your app.
    tags:
      - Location
  - name: Location Available
    description: Segments your users by whether or not they have reported their locations. In order to use this filter, your app needs to have <a href="/docs/search/?query=location%20tracking">location tracking integrated.</a>
    tags:
      - Location
  - name: Amplitude Cohorts
    description: Clients who use Amplitude can supplement their segments by choosing and importing their cohorts in Amplitude.
    tags:
      - Cohort membership
  - name: Census Cohorts
    description: Clients who use Census can supplement their segments by choosing and importing their cohorts in Census.
    tags:
      - Cohort membership
  - name: Heap Cohorts
    description: Clients who use Heap can supplement their segments by choosing and importing their cohorts in Heap.
    tags:
      - Cohort membership
  - name: Hightouch Cohorts
    description: Clients who use Hightouch can supplement their segments by choosing and importing their cohorts in Hightouch.
    tags:
      - Cohort membership
  - name: Kubit Cohorts
    description: Clients who use Kubit can supplement their segments by choosing and importing their cohorts in Kubit.
    tags:
      - Cohort membership
  - name: Mixpanel Cohorts
    description: Clients who use Mixpanel can supplement their segments by choosing and importing their cohorts in Mixpanel.
    tags:
      - Cohort membership
  - name: Segment Cohorts
    description: Clients who use Segment can supplement their segments by choosing and importing their cohorts in Segment.
    tags:
      - Cohort membership
  - name: Tinyclues Cohorts
    description: Clients who use Tinyclues can supplement their segments by choosing and importing their cohorts in Tinyclues.
    tags:
      - Cohort membership
  - name: Install Attribution Ad
    description: Segments your users by the ad that their install was attributed to.
    tags:
      - User Attributes
  - name: Install Attribution Adgroup
    description: Segments your users by the ad group that their install was attributed to.
    tags:
      - Install Attribution
  - name: Install Attribution Campaign
    description: Segments your users by the ad campaign that their install was attributed to.
    tags:
      - Install Attribution
  - name: Install Attribution Source
    description: Segments your users by the source that their install was attributed to.
    tags:
      - Install Attribution
  - name: Churn Risk Category
    description:  Segments your users by churn risk category according to a specific prediction.
    tags:
      - Intelligence and predictive
  - name: Churn Risk Score
    description: Segments your users by churn risk score according to a specific prediction.
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Category
    description: Segments your users by likelihood of performing an event according to a specific prediction.
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Score
    description: Segments your users by likelihood of performing an event according to a specific prediction.
    tags:
      - Intelligence and predictive
  - name: Intelligent Channel
    description: Segment your users by their most active channel in the last three months.
    tags:
      - Intelligence and predictive
  - name: Number of Facebook Friends Using App
    description: Segments your users by how many Facebook friends they have who use the same app.
    tags:
      - Social activity
  - name: Connected Facebook
    description: Segments your users by whether they connected your app to Facebook.
    tags:
      - Social activity
  - name: Connected Twitter
    description: Segments your users by whether they connected your app to X (formerly Twitter).
    tags:
      - Social activity
  - name: Number of Twitter Followers
    description: Segments your users by how many X (formerly Twitter) followers they have.
    tags:
      - Social activity
---
