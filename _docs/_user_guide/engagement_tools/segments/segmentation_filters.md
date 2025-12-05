---
page_order: 2
nav_title: Segmentation filters
article_title: Segmentation Filters
layout: glossary_page
glossary_top_header: "Segmentation Filters"
glossary_top_text: The Braze SDK provides you with a powerful arsenal of filters to segment and target your users based off of specific features and attributes. You can search or narrow these filters by filter category.<br><br>To learn about the different custom attribute data types you can use to segment users, view <a href="/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types">Custom attribute data types</a>.

page_type: glossary
tool: Segments
description: "This glossary lists available filters to segment and target your users."
search_rank: 2
glossary_tag_name: Filter Category
glossary_filter_text: "Select a category to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Segment or CSV membership
  - name: Custom attribute
  - name: Custom events
  - name: Sessions
  - name: Retargeting
  - name: Channel subscription behavior
  - name: Purchase behavior
  - name: eCommerce
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
    description: Allows you to filter based on segment membership anywhere that filters are used (such as segments, campaigns, and others) and target multiple different segments within one campaign. <br><br>Note that segments already using this filter cannot be further included or nested into other segments because this may create a cycle where Segment A includes Segment B, which then tries to include Segment A again. If that happened, the segment would keep referencing itself, making it impossible to calculate who actually belongs in it. Also, nesting segments like this adds complexity and can slow things down. Instead, recreate the segment you're trying to include using the same filters.
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
    description: Determines whether or not a user matches a custom recorded attribute value. <br><br>Time zone:<br>Company's Time Zone
    tags:
      - Custom attribute
  - name: Created At
    description: Segments users by when their user profile was created. If a user was added by CSV or API, then this filter reflects the date they were added. If the user isn't added by CSV or API and has their first session tracked by the SDK, then this filter reflects the date of that first session.
    tags:
      - Other Filters
  - name: Nested Custom Attributes
    description: Attributes that are the properties of custom attributes.<br><br>When filtering a nested time custom attribute, you can choose to filter based on "Day of Year" or "Time". "Day of Year" checks only the month and day for comparison. "Time" compares the full timestamp, including the year.
    tags:
      - Custom attribute
  - name: Day of Recurring Event
    description: This filter looks at the month and day of custom attribute with the data type of "date", but does not look at the year. This filter is useful for annual events.<br><br>Time zone&#58;<br>This filter adjusts for whatever time zones the user is in, so long as the message sends using the local time scheduling option; otherwise, this filter uses your company time zone.
    tags:
      - Custom attribute
  - name: Custom Event
    description: Determines whether or not a user has performed a specially recorded event.<br><br> Example:<br>Activity completed with property activity_name.<br><br>Time zone:<br>UTC - Calendar Day = 1 calendar day looks at 24-48 hours of user history
    tags:
      - Custom events
  - name: First Did Custom Event
    description: Determines the earliest time that a user has performed a specially recorded event. (24-hour period) <br><br>Example:<br> First Abandoned Cart Less than 1 day ago<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Custom events
  - name: Last Did Custom Event 
    description: Determines the latest time that a user has performed a specially recorded event. This filter supports decimals, such as 0.25 hours. (24-hour period) <br><br>Example:<br> Last Abandoned Cart Less than 1 day ago<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Custom events
  - name: X Custom Event In Y Days
    description: Determines whether or not a user has performed a specially recorded event between 0 and 50 times in the last specified number of calendar days between 1 and 30. (Calendar Day = 1 calendar day looks at 24-48 hours of user history)<br> <a href="/docs/x-in-y-behavior/"> Learn more about X-in-Y behavior here.</a> <br><br>Example:<br>Abandoned Cart exactly 0 times in the last 1 calendar day<br><br>Time zone:<br>UTC - To account for all time zones, 1 calendar day looks at 24-48 hours of user history, depending on the time the segment is evaluated; for 2 calendar days, looks at 48-72 hours of user history, and so on.
    tags:
      - Custom events
  - name: X Custom Event Property In Y Days
    description: Determines whether or not a user has performed a specially recorded event in relation to a specific property between 0 and 50 times in the last specified number of calendar days between 1 and 30. (Calendar Day = 1 calendar day looks at 24-48 hours of user history)<br><a href="/docs/x-in-y-behavior/">Learn more about X-in-Y behavior here.</a> <br><br>Example:<br> Added to Favorites w/ property "event_name" exactly 0 times in the last 1 calendar day<br><br>Time zone:<br>UTC - To account for all time zones, 1 calendar day looks at 24-48 hours of user history, depending on the time the segment is evaluated; for 2 calendar days, looks at 48-72 hours of user history, and so on.
    tags:
      - Custom events
  - name: Email Address 
    description: Allows you to designate your campaign recipients by individual email addresses for testing. This can also be used to send transactional emails to all your users (including unsubscribed) using the "Email Address is not Blank" specifier within the filter, so that you can maximize delivery of emails regardless of opt-in status. <br><br>This filter only checks if user profiles have an email address, whereas the <a href="/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available">Email Available</a> filter checks for additional criteria.
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
    description: Segments your users by the earliest recorded time that they opened your app. <em>This captures the first session they have using a version of your app with the Braze SDK integrated.</em> (24-hour period)<br><br>Time zone:<br>Company's Time Zone
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
    description: Segments your users by whether or not they have received a specific campaign.<br><br> For Content Cards, Banners, and in-app messages, this is when a user logs an impression, not when the card or in-app message is sent.<br><br>For push and webhooks, this is when the message is sent to the user.<br><br> For WhatsApp, this is when the last message API request is sent to WhatsApp, not when the message is delivered to the user's device. <br><br>For emails, this is when an email request is sent to the email service provider (regardless if it actually gets delivered). When multiple users share the same email address:<br>- On the initial send, only the specific targeted user's profile is updated. <br>- When the email is delivered, or if the user then opens the email or a link in the email, all users sharing that email address appear to have received the message.<br><br>For SMS, this is when the last message was delivered to the SMS provider. This doesn't guarantee that the message was delivered to the user's device.
    tags:
      - Retargeting
  - name: Received Campaign Variant
    description: Segments your users by which variant of a multivariate campaign they have received.<br><br> For Content Cards, Banners, and in-app messages, this is when a user logs an impression, not when the card or in-app message is sent.<br><br>For push and webhooks, this is when the message is sent to the user.<br><br> For WhatsApp, this is when the last message API request is sent to WhatsApp, not when the message is delivered to the user's device. <br><br>For emails, this is when an email request is sent to the email service provider (regardless if it actually gets delivered). When multiple users share the same email address:<br>- On the initial send, only the specific targeted user's profile is updated. <br>- When the email is delivered, or if the user then opens the email or a link in the email, all users sharing that email address appear to have received the message.<br><br>For SMS, this is when the last message was delivered to the SMS provider. This doesn't guarantee that the message was delivered to the user's device.
    tags:
      - Retargeting
  - name: Received Message from Canvas Step
    description: Segments your users by whether or not they have received a specific Canvas component.<br><br> For Content Cards and in-app messages, this is when a user logs an impression, not when the card or in-app message is sent.<br><br>For push and webhooks, this is when the message is sent to the user.<br><br> For WhatsApp, this is when the last message API request is sent to WhatsApp, not when the message is delivered to the user's device. <br><br>For emails, this is when an email request is sent to the email service provider (regardless if it actually gets delivered). When multiple users share the same email address:<br>- On the initial send, only the specific targeted user's profile is updated. <br>- When the email is delivered, or if the user then opens the email or a link in the email, all users sharing that email address appear to have received the message.<br><br>For SMS, this is when the last message was delivered to the SMS provider. This doesn't guarantee that the message was delivered to the user's device.
    tags:
      - Retargeting
  - name: Last Received Message from Specific Canvas Step
    description: Segments your users by when they received a specific Canvas component. This filter doesn't consider when users received other Canvas components.
    tags:
      - Retargeting
  - name: Last Received Message from Specific Campaign
    description: Segments your users by whether or not they have received a specific campaign. This filter doesn't consider when users received other campaigns.
    tags:
      - Retargeting
  - name: Received Message from Campaign or Canvas with Tag
    description: Segments your users by whether or not they have received a specific campaign or Canvas with a specific tag.<br><br> For Content Cards, Banners (Campaigns only), and in-app messages, this is when a user logs an impression, not when the card or in-app message is sent.<br><br>For push and webhooks, this is when the message is sent to the user.<br><br> For WhatsApp, this is when the last message API request is sent to WhatsApp, not when the message is delivered to the user's device. <br><br>For emails, this is when an email request is sent to the email service provider (regardless if it actually gets delivered). When multiple users share the same email address:<br>- On the initial send, only the specific targeted user's profile is updated. <br>- When the email is delivered, or if the user then opens the email or a link in the email, all users sharing that email address appear to have received the message.<br><br>For SMS, this is when the last message was delivered to the SMS provider. This doesn't guarantee that the message was delivered to the user's device.
    tags:
      - Retargeting
  - name: Last Received Message from Campaign or Canvas With Tag
    description: Segments your users by when they received a specific campaign or Canvas with a specific tag. This filter doesn't consider when users received other campaigns or Canvases. (24-hour period)
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
    description: Segments your users by the time that the last message was delivered to the SMS provider. This doesn't guarantee that the message was delivered to the user's device. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last Received Webhook
    description: Segments your users by the last time that Braze sent a webhook for that user. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last Received WhatsApp
    description: Segments your users by the last time that they received a WhatsApp message. This is when the last message API request is sent to WhatsApp, not when the message is delivered to the user's device. (24-hour period)<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Live Activities Push to Start Registered for App
    description: Segments your users by whether they are registered to start a Live Activity through iOS push notifications for a specific app.
    tags:
      - Devices
  - name: Clicked/Opened Campaign
    description: Filter by interaction with a specific campaign. For email messaging, the open event includes both machine opens and non-machine opens.<br><br> For email, this also includes the option to filter by "opened any email (machine opens)" and "opened any email (other opens)". If multiple users share the same email address:<br>- When the email is opened or clicked, all other users with that same email address also have their profiles updated. <br>- If the original user changes their email address after the message is sent and before the open or click, the open or click gets applied to all remaining users with that email address instead of the original user.<br><br>For SMS, an interaction is defined as:<br>- The user last sent a reply SMS matching a given keyword category. This is attributed to the most recent campaign received by all users with this phone number. The campaign must have been received in the last four hours.<br>- The user last selected any shortened link in an SMS message that has user click tracking turned on, from a given campaign.
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    description: Filter by interaction with a specific campaign that has a specific tag. For email messaging, the open event includes both machine opens and non-machine opens.<br><br> For email, this includes the option to filter by "opened any email (machine opens)" and "opened any email (other opens)". If multiple users share the same email address:<br>- When the email is opened or clicked, all other users with that same email address also have their profiles updated. <br>- If the original user changes their email address after the message is sent and before the open or click, the open or click gets applied to all remaining users with that email address instead of the original user.<br><br>For SMS, an interaction is defined as:<br>- The user last sent a reply SMS matching a given keyword category. This is attributed to the most recent campaign received by all users with this phone number. The campaign must have been received in the last four hours.<br>- When the user last selected any shortened link in an SMS message that has user click tracking turned on, from a given campaign or Canvas step with tag.
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    description: Filter by interaction with a specific Canvas component. For email messaging, the open event includes both machine opens and non-machine opens.<br><br>For email, this includes the option to filter by "opened any email (machine opens)" and "opened any email (other opens)".<br><br>For SMS, an interaction is defined as:<br>- The user last sent a reply SMS matching a given keyword category. This is attributed to the most recent campaign received by all users with this phone number. The campaign must have been received in the last four hours. <br>- The user last selected any shortened link in an SMS message that has user click tracking turned on, from a given Canvas step.
    tags:
      - Retargeting
  - name: Clicked Alias in Campaign
    description: Filter your users by whether they clicked a specific alias in a specific campaign. This only applies to email messages. <br><br> If multiple users share the same email address:<br>- When the email is opened or clicked, all other users with that same email address also have their profiles updated. <br>- If the original user changes their email address after the message is sent and before the open or click, the open or click gets applied to all remaining users with that email address instead of the original user.
    tags:
      - Retargeting
  - name: Clicked Alias in Canvas Step
    description: Filter your users by whether they clicked a specific alias in a specific Canvas. This only applies to email messages. <br><br> If multiple users share the same email address:<br>- When the email is opened or clicked, all other users with that same email address also have their profiles updated. <br>- If the original user changes their email address after the message is sent and before the open or click, the open or click gets applied to all remaining users with that email address instead of the original user.
    tags:
      - Retargeting
  - name: Clicked Alias in Any Campaign or Canvas Step
    description: Filter your users by whether they clicked a specific alias in any campaign or Canvas. This only applies to email messages. <br><br> If multiple users share the same email address:<br>- When the email is opened or clicked, all other users with that same email address also have their profiles updated. <br>- If the original user changes their email address after the message is sent and before the open or click, the open or click gets applied to all remaining users with that email address instead of the original user.
    tags:
      - Retargeting
  - name: Hard Bounced
    description: Segment your users by whether or not their email address has hard bounced (such as the email address is invalid).
    tags:
      - Retargeting
  - name: Soft Bounced
    description: Segment your users by whether they soft bounced X times in Y days. Segment filters can only look back 30 days, but you can look back further with Segment Extensions.<br><br>This filter operates differently than a soft bounce event in Currents. The Soft Bounced segment filter counts a soft bounce if there was no successful delivery during the 72 hour retry period. In Currents, every unsuccessful retry is sent as a soft bounce event. 
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
    description: Segments your users by whether or not they were in the control group for a specific Canvas. This filter only evaluates users who have entered the Canvas.<br><br>For example, if you filter for users who are not in the control group for a Canvas, you receive all users who entered the Canvas but are not in the control group.
    tags:
      - Retargeting
  - name: Last Enrolled in Any Control Group
    description: Segments your users by the last time that they fell into the control group in a campaign. <br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    description: Segments your users by whether or not they have entered a variation path of a specific Canvas. This filter evaluates all users.<br><br>For example, if you filter for users who have not entered a Canvas variation control group, you receive all users who are not in the control group regardless if they entered the Canvas.
    tags:
      - Retargeting
  - name: Last Received Any Message
    description: Segments your users by determining the last message that was received. (24-hour period)<br><br> For Content Cards, Banners, and in-app messages, this is when a user last logged an impression, not when the card or in-app message was last sent.<br><br>For push and webhooks, this is when any message was sent to the user.<br><br> For WhatsApp, this is when the last message API request was sent to WhatsApp, not when the message was delivered to the user's device. <br><br>For emails, this is when an email request is sent to the email service provider (regardless if it actually gets delivered). When multiple users share the same email address:<br>- On the initial send, only the specific targeted user's profile is updated. <br>- When the email is delivered, or if the user then opens the email or a link in the email, all users sharing that email address appear to have received the message.<br><br>For SMS, this is when the last message was delivered to the SMS provider. This doesn't guarantee that the message was delivered to the user's device.<br><br>Example:<br>Last Received Message Less than 1 Day ago = less than 24 hours ago<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Last Engaged With Message
    description: Segments your users by the last time they have clicked or opened one of your messaging channels (Banners, Content Card, email, in-app, SMS, push, WhatsApp). For email messaging, the open event includes both machine opens and non-machine opens. (24-hour period)<br><br>For emails, this is when an email request is sent to the email service provider (regardless if it actually gets delivered). This also includes the option to filter by "opened any email (machine opens)" and "opened any email (other opens)". When multiple users share the same email address:<br>- On the initial send, only the specific targeted user's profile is updated. <br>- When the email is delivered, or if the user then opens the email or a link in the email, all users sharing that email address appear to have received the message.<br><br>For SMS, this is when the user last selected any shortened link in a message that has user click tracking turned on.<br><br>Time zone:<br>Company's Time Zone
    tags:
      - Retargeting
  - name: Clicked card 
    description: Segments your users by whether or not they have clicked a specific Content Card. This filter is available as a subfilter of "Clicked/opened campaign", "Clicked/opened campaign or Canvas with Tag", and "Clicked/opened step".
    tags:
      - Retargeting
  - name: Feature Flags
    description: The segment of your users that have a particular <a href="/docs/developer_guide/feature_flags/">feature flag</a> currently enabled.
    tags:
      - Retargeting
  - name: Subscription Group
    description: Segments your users by their subscription group for email, SMS/MMS, or WhatsApp. Archived Groups do not appear and cannot be used.
    tags:
      - Channel subscription behavior
  - name: Email Available
    description: Segments your users by whether they have a valid email address, and if they are subscribed or opted-in to email. This filter checks for three criteria&#58; if the user is unsubscribed from emails, if Braze has received a hard bounce, and if the email was marked as spam. If any of these criteria are met, or if an email doesn't doesn't exist for a user, the user is not included.<br><br>Note that if you send a transactional message, users whose "Email Available" is <code>false</code> won't be included in the audience calculation but could still receive a message. However, the audience calculation includes only subscribed or opted-in users. <br><br>For emails where the opt-in status is important, we suggest using the "Email Available" filter instead of the <a href="/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address">Email Address</a> filter; the additional criteria can help you target users who truly want to see your messages.
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
  - name: Foreground Push Enabled
    description: Segments your users who have provisional push authorization or are enabled for foreground push. Specifically, this count includes:<br>1. iOS users who are provisionally authorized for push. <br>2. Users who are foreground push enabled and whose push subscription status is not unsubscribed, for any of your apps. For these users, this count includes only foreground push.<br><br>Foreground Push Enabled does not include users who have unsubscribed. <br><br>After segmenting with this filter, you can see a breakdown of who is in that segment for Android, iOS, and web in the bottom panel, called <em>Reachable Users</em>.
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled for App
    description: Segments by whether users have push enabled for your app on their device. Users who are foreground push enabled for an app. This does not take push subscription status into account. This count includes users who have provisionally authorized foreground and background push tokens.
    tags:
      - Channel subscription behavior
  - name: Background or Foreground Push Enabled
    description: Segments by whether users have a push token and haven't unsubscribed. Users who are background or foreground push enabled for any of your apps.
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
  - name: Last Made Purchase
    description: Filter users by the last time they made a purchase.
    tags: 
      - Purchase behavior
  - name: Last Purchased Product
    description: Filter users by when they last purchased a specific product.
    tags:
      - Purchase behavior
  - name: Money Spent
    description: Segments your users by the amount of money that they have spent in your app.
    tags:
      - Purchase behavior
  - name: X Money Spent in Y Days
    description: Segments your users by the amount of money that they have spent in your app in the last specified number of calendar days between 1 and 30. This amount includes only the sum of the last 50 purchases. <br> <a href="/docs/x-in-y-behavior/">Learn more about X-in-Y behavior here.</a>
    tags:
      - Purchase behavior
  - name: Last order placed (last 730 days)
    description: Segments your users by when they last placed an order, which is based on the <a href="/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events">eCommerce recommended event</a> for order placed (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter once per day, and the maximum lookback window is the last 2 years.<br><br>This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.
    tags:
      - eCommerce
  - name: Total orders count (last 730 days)
    description: Segments your users by the total count of a user's orders within the last 2 years, based on the <a href="/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events">eCommerce recommended event</a> for order placed (workspaces not tracking eCommerce events do not have data for this filter). This count excludes canceled orders, which must be tracked using the <a href="/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events">eCommerce recommended event</a> for order canceled. Users are evaluated for this filter once per day.<br><br>This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.
    tags:
      - eCommerce
  - name: Total orders count
    description: Segments your users by the total count of a user's orders across their lifetime, based on the <a href="/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events">eCommerce recommended event</a> for order placed (workspaces not tracking eCommerce events do not have data for this filter). This count excludes canceled orders, which must be tracked using the <a href="/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events">eCommerce recommended event</a> for order canceled. Users are evaluated for this filter in real time.<br><br>This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.
    tags:
      - eCommerce
  - name: Total canceled orders count (last 730 days)
    description: Segments your users by the total count of orders a user canceled within the last 2 years, based on the <a href="/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events">eCommerce recommended event</a> for order placed (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter once per day.<br><br>This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.
    tags:
      - eCommerce
  - name: Customer lifetime value (last 730 days)
    description: Segments your users by the total revenue a user is expected to generate over their purchasing history with your brand. The calculation considers the last 730 days and takes the Average Order Value (AOV), multiplies it by the total number of orders placed, and then factors in the user's active purchasing duration (the time span between their first and their most recent order). This filter uses data tracked in <a href="/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events">eCommerce recommended event</a>s (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter once per day.<br><br>This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.
    tags:
      - eCommerce
  - name: Total refund value (last 730 days)
    description: Segments your users by the value of refunds granted to a user over the last 2 years, based on the <a href="/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events">eCommerce recommended event</a> for order refunded (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter once per day.<br><br>This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.
    tags:
      - eCommerce
  - name: Total refund value
    description: Segments your users by the total value of refunds granted to a user across their lifetime, based on the <a href="/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events">eCommerce recommended event</a> for order refunded (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter in real time.<br><br>This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.
    tags:
      - eCommerce
  - name: Total revenue (last 730 days)
    description: Segments your users by the total revenue generated from a user's orders over the last 2 years, calculated based on subtracting the revenue associated with the <a href="/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events">eCommerce recommended event</a> for order refunded from the revenue associated with the eCommerce event for order placed (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter once per day.<br><br>This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.
    tags:
      - eCommerce
  - name: Total revenue
    description: Segments your users by the total revenue generated from a user's orders across the user's lifetime, calculated based on subtracting the revenue associated with the <a href="/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events">eCommerce recommended event</a> for order refunded from the revenue associated with the eCommerce event for order placed (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter in real time.<br><br>This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.
    tags:
      - eCommerce
  - name: Average order value (last 730 days)
    description: Segments your users by the average (mean) value of a user's orders over the last 2 years, based on the <a href="/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events">eCommerce recommended event</a> for order placed (workspaces not tracking eCommerce events do not have data for this filter). Users are evaluated for this filter once per day.<br><br>This filter is in beta. Contact your Braze account manager if you’re interested in using this filter.
    tags:
      - eCommerce
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
    description: Segments your users by their birthday, as they indicated from within your app. <br> Users with a birthday on the 29th of February are included in segments including March 1.<br><br>To target December or January birthdays, only insert filter logic within the 12-month span of the year you're targeting. In other words, do not insert logic that looks back to the previous calendar year's December or forward to the next year's January. For example, to target December birthdays, you can filter for "on December 31", "before December 31", or "after November 30".
    tags:
      - Demographic attributes
  - name: Gender
    description: Segments your users by gender, as they indicated from within your app.
    tags:
      - Demographic attributes
  - name: Unformatted Phone Number
    description: Segments your users by their unformatted phone number. Does not include parenthesis, dashes, or other symbols.
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
    description: Segments by whether or not a user has ever installed your app. This includes users who currently have your app installed and those that have uninstalled in the past. This generally requires users to open the app (start a session) to be included in this filter. However, there are some exceptions, such as if a user was imported into Braze and manually associated with your app.
    tags:
      - App
  - name: Most Recent App Version Name
    description: Segments by the recent name of the user's app.<br><br>When using "less than" or "less than or equal to", if the main app version doesn't exist, this filter returns `true` because the user is older than the app version. This means that if the user’s last main app version doesn't exist, they automatically match the filter.
    tags:
      - App 
  - name: Most Recent App Version Number
    description: Segments by the recent app version number of the user's app.<br><br>When using “less than” or “less than or equal to”, if the main app version doesn't exist, this filter returns `true` because the user is older than the app version. This means that if the user’s last main app version doesn't exist, they automatically match the filter.<br><br>It may take time for the current app versions to populate. The app version on the user profile updates when the information is captured by the SDK, which relies on when users open their apps. If the user doesn't open the app, the current version won't be updated. These filters also won't apply retroactively. It's good to use "greater than" or "equal" to current and future versions, but using past version filters may cause unexpected behaviors.
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
    description: Allows you to filter based on whether your users have opted-in to ad tracking. Ad tracking relates to the IDFA or "identifier for advertisers" assigned to all iOS devices by Apple, which can be set by SDKs. This identifier allows advertisers to track users and serve them targeted ads.
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
  - name: Message Open Likelihood
    description: Filters your users based on their likelihood to open a message on a specified channel on a scale of 0-100%. Users without sufficient data to measure a likelihood for a channel can be selected using "is blank."
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
  - name: Phone Number
    description: Segments your users by the E.164 formatted phone number field.<br><br> When a phone number is sent to Braze, Braze tries to coerce it into the <a href="/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers">e.164 format</a> that is used to send across SMS and WhatsApp channels. The coercion process can fail if the number isn't formatted properly, which results in the user profile having an unformatted phone number but not a sending phone number. This segment filter returns users by their e.164 formatted phone number (when available).<br><br>Use cases:<br> - Use this filter to understand the most accurate target audience size when sending SMS or WhatsApp messages.  <br>- Use regular expressions (regex) with this filter to segment by phone numbers with a specific country code. <br>- Use this filter to segment users by phone numbers that failed the e.164 coercion process.
    tags:
      - Other filters
---
