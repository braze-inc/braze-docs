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
    description: 
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    description:
    tags:
      - Segment or CSV membership
  - name: Updated/imported from CSV
    description:
    tags:
      - Segment or CSV membership
  - name: Custom attributes
    description:
    tags:
      - Custom attributes
  - name: Nested custom attributes
    description: 
    tags:
      - Custom attributes
  - name: Day of recurring event
    description: 
    tags:
      - Custom attributes
  - name: Custom events
    description:
    tags:
      - Custom events
  - name: First did custom event
    description: 
    tags:
      - Custom events
  - name: Last did custom event 
    description:
    tags:
      - Custom events
  - name: X custom event in Y days
    description: 
      - Custom events
  - name: X custom event property in Y days
    description: 
    tags:
      - Custom events
  - name: User Email Address 
    description: 
    tags:
      - Other filters
  - name: External user ID
    description: 
    tags:
      - Other filters
  - name: Random Bucket Number
    description: Randomly generated number assigned to each profile for testing purposes.
    tags:
      - Other filters
  - name: Session count overall
    description: 
    tags:
      - Sessions
  - name: Session count for app
    description:
    tags:
      - Sessions
  - name: X sessions in last Y days
    description: 
    tags:
      - Sessions
  - name: First used app
    description: 
    tags:
      - Sessions
  - name: First used specific app
    description: 
    tags:
      - Sessions
  - name: Last used app
    description: 
    tags:
      - Sessions
  - name: Last used specific app
    description: 
    tags:
      - Sessions
  - name: Median session duration
    description: 
    tags:
      - Sessions
  - name: Received message from campaign
    description: 
    tags:
      - Retargeting
  - name: Received campaign variant
    description: 
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
    description: 
    tags:
      - Retargeting
  - name: Last received push
    description: 
    tags:
      - Retargeting
  - name: Last in-app message impression
    description:
    tags:
      - Retargeting
  - name: Last received SMS/MMS
    description: 
    tags:
      - Retargeting
  - name: Last received webhook
    description: 
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
    description: 
    tags:
      - Retargeting
  - name: Last engaged with message
    description: 
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
    description: 
    tags:
      - Retargeting
  - name: Has marked you as spam
    description: 
    tags:
      - Retargeting
  - name: Invalid phone number 
    description: 
    tags:
      - Retargeting
  - name: Last sent specific SMS Inbound Keyword category
    description: 
    tags:
      - Retargeting
  - name: Converted from Campaign
    description: 
    tags:
      - Retargeting
  - name: Converted from Canvas
    description: 
    tags:
      - Retargeting
  - name: In campaign control group
    description:
    tags:
      - Retargeting
  - name: In Canvas control group
    description: 
    tags:
      - Retargeting
  - name: Last enrolled in control group
    description: 
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    description: 
    tags:
      - Retargeting
  - name: Clicked card 
    description:
    tags:
      - Retargeting
  - name: Feature flags
    description: 
    tags:
      - Retargeting
  - name: Subscription group
    description: 
    tags:
      - Channel subscription behavior
  - name: Last Received Email
    description: Segments your users by the last time that they have received one of your email messages. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Marketing Activity
  - name: Last Received Push
    description: Segments your users by the last time that they received one of your push notifications. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Marketing Activity
  - name: Last Received Webhook
    description: Segments your users by the last time that Braze sent a webhook for that user. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Marketing Activity
  - name: Age
    description: Segments your users by their age, as they indicated from within your app.
    tags:
      - User Attributes
  - name: Amplitude Cohorts
    description: Clients who use Amplitude can supplement their segments by choosing and importing their cohorts in Amplitude.
    tags:
      - User Attributes
  - name: Background Push Enabled
    description: Segments your users on whether they have enabled background push or not.
    tags:
      - User Attributes
  - name: Birthday
    description: Segments your users by their birthday, as they indicated from within your app. <br> Users with a birthday on the 29th of February will be included in segments including March 1.
    tags:
      - User Attributes
  - name: Braze Segment Extension
    description: After creating a Segment Extension in the Braze dashboard, you can choose to include/exclude those extensions in your segment.
    tags:
      - User Attributes
  - name: City
    description: Segments your users by their last indicated city location.
    tags:
      - User Attributes
  - name: Country
    description: Segments your users by their last indicated country location.
    tags:
      - User Attributes
  - name: Device Carrier
    description: Segments your users by their device carrier.
    tags:
      - User Attributes
  - name: Device Count
    description: Segments your users by how many devices they have used your app on.
    tags:
      - User Attributes
  - name: Device Model
    description: Segments your users by their mobile phone's model version.
    tags:
      - User Attributes
  - name: Device OS
    description: Segments your users that have one or more devices with the specified operating system.
    tags:
      - User Attributes
  - name: Clicked Content Card
    description: Segments your users by whether or not they have clicked a specific Content Card. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Clicked Email
    description: Segments your users by whether or not they have clicked a specific email. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Clicked In-App Message
    description: Segments your users by whether or not they have clicked a specific in-app message. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Clicked In-App Message Button
    description: Segments your users by whether or not they have clicked a specific in-app message button. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Directly Opened Push Notification
    description: Segments your users by whether or not they have directly opened a specific push notification. The proportion of opens that are affected by Apple's Mail Privacy Protection (MPP) for iOS 15. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Dismissed Content Card
    description: Segments your users by whether or not they have dismissed a specific Content Card. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Opened Email
    description: Segments your users by whether or not they have opened a specific email. This includes both user and machine opens. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Opened Email (Other Opens)
    description: Segments your users by whether or not they have opened a specific email. This includes email opens that haven't been identified as "Machine opens". For example, when a user opens an email on another platform (such as Gmail app on a phone, Gmail on desktop browser), this will be logged as an "Other opens". This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Opened Email (Machine Opens)
    description: Segments your users by whether or not they have opened a specific email. This includes email opens that are affected by Apple's Mail Privacy Protection (MPP) for iOS 15. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Replied to SMS
    description: Segments your users by whether or not they have replied to a specific SMS message. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Viewed Content Card
    description: Segments your users by whether or not they have viewed a specific Content Card. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Viewed In-App Message
    description: Segments your users by whether or not they have viewed a specific in-app message. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Email Available
    description: Segments your users by whether or not they have a valid email address, and if they are subscribed/opted-in to email. The email available filter checks for three criteria&#58; if the user is unsubscribed from emails, if Braze has received a hard bounce, and if the email was marked as spam. If any of these criteria are met, or if an email doesn't doesn't exist for a user, the user will not be included.
    tags:
      - User Attributes
  - name: Email Opt-In Date
    description: Segments your users by the date on which they opted into email.
    tags:
      - User Attributes
  - name: Email Subscription Status
    description: Segments your users by their subscription status for email.
    tags:
      - User Attributes
  - name: Subscription Groups
    description: Segments your users by their Subscription Group for email or SMS/MMS. Archived Groups will not appear and cannot be used.
    tags:
      - Other
  - name: Email Unsubscribed Date
    description: Segments your users by the date on which they unsubscribed from future emails.
    tags:
      - User Attributes
  - name: First Name
    description: Segments your users by their first name, as they indicated from within your app.
    tags:
      - User Attributes
  - name: Gender
    description: Segments your users by gender, as they indicated from within your app.
    tags:
      - User Attributes
  - name: Has App
    description: Segments by whether or not a user has ever installed your app. This will include users who currently have your app installed and those that have uninstalled in the past. This generally requires users to open the app (start a session) to be included in this filter. However, there are some exceptions, such as if a user was imported into Braze and manually associated with your app.
    tags:
      - User Attributes
  - name: Language
    description: Segments your users by their preferred language.
    tags:
      - User Attributes
  - name: Last Name
    description: Segments your users by their last name, as they indicated from within your app.
    tags:
      - User Attributes
  - name: Location Available
    description: Segments your users by whether or not they have reported their locations. In order to use this filter, your app needs to have <a href="/docs/search/?query=location%20tracking">location tracking integrated.</a>
    tags:
      - User Attributes
  - name: Most Recent Watch Model
    description: Segments your users by their most recent smartwatch model.
    tags:
      - User Attributes
  - name: Phone Number
    description: Segments your users by their phone number. Only use digits [0-9]. Do not include parenthesis, dashes, etc.
    tags:
      - User Attributes
  - name: Push Enabled
    description: Segments your users who have provisional push authorization or are enabled for foreground push. Specifically, this count includes:<br>1. iOS users who are provisionally authorized for push. <br>2. Users who explicitly activated push notifications for any of the apps in your workspace. For these users, this count includes only foreground push.<br><br>Push Enabled does not include users who have unsubscribed. <br><br>After segmenting with this filter, you will be able to see a breakdown of who is in that segment for Android, iOS, and web in the bottom panel, called <em>Reachable Users</em>.
    tags:
      - User Attributes
  - name: Push Enabled For App
    description: Segments by whether or not your user has push enabled for your app on their device. This count includes both foreground and background push.
    tags:
      - User Attributes
  - name: Push Opt-In Date
    description: Segments your users by the date on which they opted into push.
    tags:
      - User Attributes
  - name: Push Subscription Status
    description: Segments your users by their <a href="/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state">subscription status</a> for push.
    tags:
      - User Attributes
  - name: Push Unsubscribed Date
    description: Segments your users by the date on which they unsubscribed from future push notifications.
    tags:
      - User Attributes
  - name: Random Bucket Number
    description: Segments your users by a randomly assigned number (0 to 9999 inclusive). It can enable the creation of uniformly distributed segments of truly random users for A/B and multivariate testing.
    tags:
      - User Attributes
  - name: Update/Imported from CSV
    description: Segments your users based on whether they were a part of a CSV upload or not.
    tags:
      - User Attributes
  - name: Web Browser
    description: Segments your users by the web browser they use to access your website.
    tags:
      - User Attributes
  - name: Install Attribution Ad
    description: Segments your users by the ad that their install was attributed to.
    tags:
      - User Attributes
  - name: Hard Bounce
    description: Segment your users by whether or not their email address has hard bounced (such as the email address is invalid).
    tags:
      - Install Attribution
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
  - name: Device IDFA
    description: Allows you to designate your campaign recipients by IDFA for testing.
    tags:
      - Testing
  - name: Device IDFV
    description: Allows you to designate your campaign recipients by IDFV for testing.
    tags:
      - Testing
  - name: Email Address
    description: Allows you to designate your campaign recipients by individual email addresses for testing. This can also be used to send transactional emails to all your users (including unsubscribed) using the "Email Address is not Blank" specifier within the filter.
    tags:
      - Testing
  - name: External User ID
    description: Allows you to designate your campaign recipients by individual user IDs for testing.
    tags:
      - Testing
  - name: Segment Membership
    description: Allows you to filter based on segment membership anywhere that filters are used (such as segments, campaigns, etc.) and target multiple different segments within one campaign. Note that segments already using the Segment Membership Filter cannot be further included/nested into other segments.
    tags:
      - Other
  - name: Provisionally Authorized on iOS
    description: Allows you to find users who are provisionally authorized on iOS 12 for a given app.
    tags:
      - Other
  - name: "Intelligent Channel"
    description: Filters the portion of your audience whose most active channel (the channel which has the highest likelihood of engagement given the user's past three months or activity) is the one you select in the subsequent dropdown (Email, Mobile push, or Web push). <br> You can also elect to filter by Not Enough Data, which only sends to users who have received messages from at least two of the three available channels in the drop-down but have not had enough distinct channel activity to determine a most engaged channel. <br> <a href="/docs/user_guide/intelligence/intelligent_channel/">Learn more about this filter here.</a> <br> <br> _As of the <a href="/docs/help/release_notes/2019/november/#intelligence-suite">November 2019 product release</a>, 'Most Engaged Channel' has been renamed to 'Intelligent Channel'._
    tags:
      - User Activity
  - name: Ad Tracking Enabled
    description: Allows you to filter based on if your users have opted-in to ad tracking. Ad tracking relates to the IDFA or "identifier for advertisers" assigned to all iOS devices by Apple. This identifier allows advertisers to track users and serve them targeted ads.
    tags:
      - Testing
  - name: Invalid Phone Number
    description: Segments your users by whether or not their phone number is invalid.
    tags:
      - User Attributes
---