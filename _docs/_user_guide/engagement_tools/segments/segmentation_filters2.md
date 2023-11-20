---
page_order: 0
nav_title: Segmentation filters API
article_title: Segmentation filters API
layout: glossary_page
glossary_top_header: "Segmentation filters API"
glossary_top_text: "The Braze SDK provides you with a powerful arsenal of filters to segment and target your users based off of specific features and attributes. As you can see, you can search or narrow these filters by filter category."

page_type: glossary
tool: Segments
description: "This landing page lists available Braze API endpoints and their uses."
glossary_tag_name: Filter Category
glossary_filter_text: "Select filter category to narrow the glossary:"
glossary_mid_text: "Filter search"

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
  - name: Other filters

glossaries:
  - name: Segment membership
    description: Allows you to filter based on segment membership anywhere that filters are used (such as segments, campaigns, etc.) and target multiple different segments within one campaign. Note that segments already using the Segment Membership Filter cannot be further included/nested into other segments.
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    description: After creating a Segment Extension in the Braze dashboard, you can choose to include/exclude those extensions in your segment.
    tags:
      - Segment or CSV membership
  - name: Updated/imported from CSV
    description: Segments your users based on whether they were a part of a CSV upload or not.
    tags:
      - Segment or CSV membership
  - name: Custom attributes
    description: Determines whether or not a user matches a custom recorded attribute value. (24-hour period) <br><br>Time zone:<br>Company's Time Zone
    tags:
      - Custom attributes
  - name: Nested custom attributes
    description: 
    tags:
      - Custom attributes
  - name: Day of recurring event
    description: This filter looks at the month and day of custom attribute with the data type of "date", but does not look at the year. This filter is useful for annual events.<br><br>Time zone&#58;<br>This filter adjusts for whatever time zones the user is in.
    tags:
      - Custom attributes
  - name: Custom events
    description: Determines whether or not a user has performed a specially recorded event.<br><br> Example:<br>Activity completed with property activty_name.<br><br>Time zone:<br>UTC - Calendar Day = 1 calendar day will look at 24-48 hours of user history
    tags:
      - Custom events
  - name: First did custom event
    description: Determines the earliest time that a user has performed a specially recorded event. (24-hour period) <br><br>Example:<br> First Abandoned Cart Less than 1 day ago<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Custom events
  - name: Last did custom event 
    description: Determines the latest time that a user has performed a specially recorded event. (24-hour period) <br><br>Example:<br> Last Abandoned Cart Less than 1 day ago<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Custom events
  - name: X custom event in Y days
    description: Determines whether or not a user has performed a specially recorded event between 0 and 50 times in the last specified number of calendar days between 1 and 30. (Calendar Day = 1 calendar day will look at 24-48 hours of user history)<br> <a href="/docs/x-in-y-behavior/"> Learn more about X-in-Y behavior here.</a> <br><br>Example:<br>Abandoned Cart exactly 0 times in the last 1 calendar day<br><br>Time zone:<br>UTC - To account for all time zones, 1 calendar day will look at 24-48 hours of user history, depending on the time the segment is evaluated; for 2 calendar days, will look at 48-72 hours of user history, etc.
      - Custom events
  - name: X custom event property in Y days
    description: Determines whether or not a user has performed a specially recorded event in relation to a specific property between 0 and 50 times in the last specified number of calendar days between 1 and 30. (Calendar Day = 1 calendar day will look at 24-48 hours of user history)<br><a href="/docs/x-in-y-behavior/">Learn more about X-in-Y behavior here.</a> <br><br>Example:<br> Added to Favorites w/ property "event_name" exactly 0 times in the last 1 calendar day<br><br>Time zone:<br>UTC - To account for all time zones, 1 calendar day will look at 24-48 hours of user history, depending on the time the segment is evaluated; for 2 calendar days, will look at 48-72 hours of user history, etc.
    tags:
      - Custom events
  - name: User Email Address 
    description: Allows you to designate your campaign recipients by individual email addresses for testing. This can also be used to send transactional emails to all your users (including unsubscribed) using the "Email Address is not Blank" specifier within the filter.
    tags:
      - Other filters
  - name: External user ID
    description: Allows you to designate your campaign recipients by individual user IDs for testing.
    tags:
      - Other filters
  - name: Random Bucket Number
    description: Segments your users by a randomly assigned number (0 to 9999 inclusive). It can enable the creation of uniformly distributed segments of truly random users for A/B and multivariate testing.
    tags:
      - Other filters
  - name: Session count overall
    description: Segments your users by the number of sessions they have had in any of your apps within your workspace.
    tags:
      - Sessions
  - name: Session count for app
    description: Segments your users by the number of sessions they have had in a specific, designated app.
    tags:
      - Sessions
  - name: X sessions in last Y days
    description: Segments your users by the number of sessions (between 0 and 50) they have had in your app in the last specified number of calendar days between 1 and 30. <br> <a href="/docs/x-in-y-behavior/">Learn more about X-in-Y behavior here.</a>
    tags:
      - Sessions
  - name: First used app
    description: Segments your users by the earliest recorded time that they opened your app. <em>Note that this will capture the first session they have using a version of your app with the Braze SDK integrated.</em> (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Sessions
  - name: First used specific app
    description: Segments your users by the earliest recorded time that they opened any of your apps within your workspace. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Sessions
  - name: Last used app
    description: Segments your users by the most recent time that they have opened your app. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Sessions
  - name: Last used specific app
    description: Segments your users by the most recent time that they have opened a specific, designated app. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Sessions
  - name: Median session duration
    description: Segments your users by the median length of their sessions in your app.
    tags:
      - Sessions
  - name: Received message from campaign
    description: 
    tags:
      - Retargeting
  - name: Received campaign variant
    description: Segments your users by which variant of a multivariate campaign they have received.
    tags:
      - Retargeting
  - name: Received message from Canvas step
    description: 
    tags:
      - Retargeting
  - name: Last received message from specific campaign
    description: 
    tags:
      - Retargeting
  - name: Last received message from specific Canvas step
    description: 
    tags:
      - Retargeting
  - name: Received message from campaign or Canvas with tag
    description: 
    tags:
      - Retargeting
  - name: Last received message from campaign or Canvas with tag
    description: 
    tags:
      - Retargeting
  - name: Has never received a message from campaign or Canvas step
    description: 
    tags:
      - Retargeting
  - name: Last received email
    description: Segments your users by the last time that they have received one of your email messages. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last received push
    description: Segments your users by the last time that they received one of your push notifications. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last in-app message impression
    description:
    tags:
      - Retargeting
  - name: Last received SMS/MMS
    description: Segments your users by the last time that they have received an SMS. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last received webhook
    description: Segments your users by the last time that Braze sent a webhook for that user. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last received Whatsapp
    description: 
    tags:
      - Retargeting
  - name: Last viewed News Feed
    description: 
    tags:
      - Retargeting
  - name: Last received any message
    description: egments your users by determining the last message that was received. (24-hour period)<br><br>Example:<br>Last Received Message Less than 1 Day ago = less than 24 hours ago<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last engaged with message
    description: Segments your users by the last time that they have clicked or opened one of your messaging channels (email, in-app, push). Includes option to filter by machine opens or other opens for email messages. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign
    description: 
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    description:
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    description: 
    tags:
      - Retargeting
  - name: Clicked Alias in campaign
    description: 
    tags:
      - Retargeting
  - name: Clicked Alias in Canvas step
    description: 
    tags:
      - Retargeting
  - name: Clicked Alias in any campaign or Canvas Step
    description: 
    tags:
      - Retargeting
  - name: Hard bounced
    description: Segment your users by whether or not their email address has hard bounced (such as the email address is invalid).
    tags:
      - Retargeting
  - name: Has marked you as spam
    description: Segments your users by whether or not they have marked your messages as spam.
    tags:
      - Retargeting
  - name: Invalid phone number 
    description: Segments your users by whether or not their phone number is invalid.
    tags:
      - Retargeting
  - name: Last sent specific SMS Inbound Keyword category
    description: 
    tags:
      - Retargeting
  - name: Converted from Campaign
    description: Segments your users by whether or not they have converted on a specific campaign. This filter doesn't include users that are in the control group.
    tags:
      - Retargeting
  - name: Converted from Canvas
    description: Segments your users by whether or not they have converted on a specific Canvas. This filter doesn't include users that are in the control group.
    tags:
      - Retargeting
  - name: In campaign control group
    description: Segments your users by whether or not they were in the control group for a specific multivariate campaign.
    tags:
      - Retargeting
  - name: In Canvas control group
    description: Segments your users by whether or not they were in the control group for a specific Canvas.
    tags:
      - Retargeting
  - name: Last enrolled in control group
    description: Segments your users by the last time that they fell into the control group in a campaign. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    description: Segments your users by whether or not they have entered a variation path of a specific Canvas.
    tags:
      - Retargeting
  - name: Clicked card 
    description: Segments your users by whether or not they have clicked a specific Content Card. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Feature flags
    description: The segment of your users that have a particular <a href="/docs/developer_guide/platform_wide/feature_flags/about">feature flag</a> currently enabled.
    tags:
      - Retargeting
  - name: Subscription group
    description: Segments your users by their Subscription Group for email or SMS/MMS. Archived Groups will not appear and cannot be used.
    tags:
      - Channel subscription behavior
  - name: Email available
    description: Segments your users by whether or not they have a valid email address, and if they are subscribed/opted-in to email. The email available filter checks for three criteria&#58; if the user is unsubscribed from emails, if Braze has received a hard bounce, and if the email was marked as spam. If any of these criteria are met, or if an email doesn't doesn't exist for a user, the user will not be included.
    tags:
      - Channel subscription behavior
  - name: Email opt in date
    description: Segments your users by the date on which they opted into email.
    tags:
      - Channel subscription behavior
  - name: Email subscription status
    description: Segments your users by their subscription status for email.
    tags:
      - Channel subscription behavior
  - name: Email unsubscribed date 
    description:  Segments your users by the date on which they unsubscribed from future emails.
    tags:
      - Channel subscription behavior
  - name: Push enabled
    description: Segments your users who have provisional push authorization or are enabled for foreground push. Specifically, this count includes:<br>1. iOS users who are provisionally authorized for push. <br>2. Users who explicitly activated push notifications for any of the apps in your workspace. For these users, this count includes only foreground push.<br><br>Push Enabled does not include users who have unsubscribed. <br><br>After segmenting with this filter, you will be able to see a breakdown of who is in that segment for Android, iOS, and web in the bottom panel, called <em>Reachable Users</em>.
    tags:
      - Channel subscription behavior
  - name: Push enabled for app
    description: Segments by whether or not your user has push enabled for your app on their device. This count includes both foreground and background push.
    tags:
      - Channel subscription behavior
  - name: Background push enabled
    description: 
    tags:
      - Channel subscription behavior
  - name: Push opt in date
    description: Segments your users by the date on which they opted into push.
    tags:
      - Channel subscription behavior
  - name: Push subscription status
    description: Segments your users by their <a href="/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state">subscription status</a> for push.
    tags:
      - Channel subscription behavior
  - name: Push unsubscribed date
    description: Segments your users by the date on which they unsubscribed from future push notifications.
    tags:
      - Channel subscription behavior
  - name: Purchased product
    description: Segments your users by products purchased in your app.
    tags:
      - Purchase behavior
  - name: Total number of purchases
    description: Segments your users by how many purchases they have made in your app.
    tags:
      - Purchase behavior
  - name: X product purchased in Y days
    description: 
    tags:
      - Purchase behavior
  - name: X purchase property in Y days
    description: Segments your users by the number of times a purchase was made in relation to a certain purchase property in the last specified number of calendar days between 1 and 30. <br> <a href="/docs/x-in-y-behavior/">Learn more about X-in-Y behavior here.</a>
    tags:
      - Purchase behavior
  - name: X purchases in Y days
    description: Segments your users by the number of times (between 0 and 50) they have made a purchase in the last specified number of calendar days between 1 and 30. <br> <a href="/docs/x-in-y-behavior/">Learn more about X-in-Y behavior here.</a>
    tags:
      - Purchase behavior
  - name: First made purchase
    description: 
    tags:
      - Purchase behavior
  - name: First purchase for app
    description: 
    tags:
      - Purchase behavior
  - name: Last purchased product
    description: 
    tags:
      - Purchase behavior
  - name: Money spent
    description: Segments your users by the amount of money that they have spent in your app.
    tags:
      - Purchase behavior
  - name: X money spent in Y days
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
    description: Segments your users by their birthday, as they indicated from within your app. <br> Users with a birthday on the 29th of February will be included in segments including March 1.
    tags:
      - Demographic attributes
  - name: Gender
    description: Segments your users by gender, as they indicated from within your app.
    tags:
      - Demographic attributes
  - name: Phone number
    description: Segments your users by their phone number. Only use digits [0-9]. Do not include parenthesis, dashes, etc.
    tags:
      - Demographic attributes
  - name: First name
    description:  Segments your users by their first name, as they indicated from within your app.
    tags:
      - Demographic attributes
  - name: Last name
    description:  Segments your users by their last name, as they indicated from within your app.
    tags:
      - Demographic attributes
  - name: Has app
    description: Segments by whether or not a user has ever installed your app. This will include users who currently have your app installed and those that have uninstalled in the past. This generally requires users to open the app (start a session) to be included in this filter. However, there are some exceptions, such as if a user was imported into Braze and manually associated with your app.
    tags:
      - App
  - name: Most recent app version name
    description: 
    tags:
      - App 
  - name: Most recent app version number
    description: 
    tags:
      - App 
  - name: Uninstalled
    description: 
    tags:
      - Uninstall 
  - name: Uninstalled
    description: Segments your users by whether they have uninstalled your app and have not reinstalled it.
    tags:
      - Uninstall 
  - name: Device carrier
    description: Segments your users by their device carrier.
    tags:
      - Devices
  - name: Device count
    description: Segments your users by how many devices they have used your app on.
    tags:
      - Devices
  - name: Device model
    description: Segments your users by their mobile phone's model version.
    tags:
      - Devices
  - name: Device OS
    description: Segments your users that have one or more devices with the specified operating system.
    tags:
      - Devices
  - name: Most recent device locale
    description: Segments your users by the <a href="/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/">locale information</a> from the most recently used device.
    tags:
      - Devices      
  - name: Most recent watch model
    description: Segments your users by their most recent smartwatch model.
    tags:
      - Devices    
  - name: Provisionally authorized on iOS
    description: Allows you to find users who are provisionally authorized on iOS 12 for a given app.
    tags:
      - Devices   
  - name: Web browser (not sure about this one)
    description: Segments your users by the web browser they use to access your website.
    tags:
      - Devices   
  - name: Ad tracking
    description: Allows you to filter based on if your users have opted-in to ad tracking. Ad tracking relates to the IDFA or "identifier for advertisers" assigned to all iOS devices by Apple. This identifier allows advertisers to track users and serve them targeted ads.
    tags:
      - Advertising use cases
  - name: Device IDFA
    description: Allows you to designate your campaign recipients by IDFA for testing.
    tags:
      - Advertising use cases
  - name: Device IDFV
    description: Allows you to designate your campaign recipients by IDFV for testing.
    tags:
      - Advertising use cases
  - name: Device Google Ad ID
    description: 
    tags:
      - Advertising use cases
  - name: Device Roku Ad ID
    description: 
    tags:
      - Advertising use cases
  - name: Device Roku Ad ID
    description: 
    tags:
      - Advertising use cases
  - name: Device Windows Ad ID
    description: 
    tags:
      - Advertising use cases
  - name: Most recent location
    description: Segments your users by the last recorded location at which they have used your app.
    tags:
      - Location
  - name: Location available
    description: Segments your users by whether or not they have reported their locations. In order to use this filter, your app needs to have <a href="/docs/search/?query=location%20tracking">location tracking integrated.</a>
    tags:
      - Location
  - name: Amplitude cohorts
    description: Clients who use Amplitude can supplement their segments by choosing and importing their cohorts in Amplitude.
    tags:
      - Cohort membership
  - name: Census cohorts
    description: 
    tags:
      - Cohort membership
  - name: Heap cohorts
    description: 
    tags:
      - Cohort membership
  - name: Hightouch cohorts
    description: 
    tags:
      - Cohort membership
  - name: Kubit cohorts
    description: 
    tags:
      - Cohort membership
  - name: Mixpanel cohorts
    description: 
    tags:
      - Cohort membership
  - name: Segment cohorts
    description: 
    tags:
      - Cohort membership
  - name: Tinyclues cohorts
    description: 
    tags:
      - Cohort membership
- name: Install attribution ad
    description: Segments your users by the ad that their install was attributed to.
    tags:
      - User Attributes
  - name: Hard bounce
    description: Segment your users by whether or not their email address has hard bounced (such as the email address is invalid).
    tags:
      - Install Attribution
  - name: Install attribution adgroup
    description: Segments your users by the ad group that their install was attributed to.
    tags:
      - Install Attribution
  - name: Install attribution campaign
    description: Segments your users by the ad campaign that their install was attributed to.
    tags:
      - Install Attribution
  - name: Install attribution source
    description: Segments your users by the source that their install was attributed to.
    tags:
      - Install Attribution
  - name: Churn risk category
    description: 
    tags:
      - Intelligence and predictive
  - name: Churn risk score
    description: 
    tags:
      - Intelligence and predictive
  - name: Purchase likelihood category
    description: 
    tags:
      - Intelligence and predictive
  - name: Purchase likelihood score
    description: 
    tags:
      - Intelligence and predictive
  - name: Intelligent channel
    description: 
    tags:
      - Intelligence and predictive
  - name: Number of Facebook Friends using app
    description: 
    tags:
      - Social activity
  - name: Connected Facebook
    description: 
    tags:
      - Social activity
  - name: Connected Twitter
    description: 
    tags:
      - Social activity
  - name: Number of Twitter followers
    description: 
    tags:
      - Social activity


---