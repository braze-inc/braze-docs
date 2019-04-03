---
page_order: 1
nav_title: Segmentation Filters
layout: glossary_page
glossary_top_header: "Segmentation Filters"
glossary_top_text: Braze’s SDK provides you with a powerful arsenal of filters to segment and target your users based off of specific features and attributes. As you can see, you can search or narrow these filters by <a href="/docs/user_guide/engagement_tools/segments/filter_categories/">Filter Category.</a>

glossary_tag_name: Filter Category
glossary_filter_text: "Select Categories below to narrow the glossary:"

# category to icon/fa or image mapping
glossary_tags:
  - name: Custom Data
  - name: User Activity
  - name: Retargeting
  - name: Marketing Activity
  - name: User Attributes
  - name: Install Attribution
  - name: Social Activity
  - name: Testing
  - name: Other

glossaries:
  - name: Custom Attributes
    description: Determines whether or not a user matches a custom recorded attribute value.
    tags:
      - Custom Data
  - name: Custom Event
    description: Determines whether or not a user has performed a specially recorded event.
    tags:
      - Custom Data
  - name: Date of Custom Attribute
    description: Segments your users based upon the calendar date of custom attributes. This filter looks for matches of an indicated day/month, but ignores the year. As such, the filter works nicely for anniversary use cases.
    tags:
      - Custom Data
  - name: First Did Custom Event
    description: Determines the earliest time that a user has performed a specially recorded event (above).
    tags:
      - Custom Data
  - name: X Custom Event in Y Days
    description: Determines whether or not a user has performed a specially recorded event between 0 and 50 times in the last 1, 3, 7, 14, 21, and 30 days.
    tags:
      - Custom Data
  - name: X Custom Event Property in Y Days
    description: Determines whether or not a user has performed a specially recorded event in relation to a specific property between 0 and 50 times in the last 1, 3, 7, 14, 21, and 30 days. <br> <em>Please note that Custom Event Properties must be turned on by Braze for specific custom events. Contact your Account Manager or <a href="/docs/support_contact/">open a support ticket</a> if you don’t see the filters you need.</em>
    tags:
      - Custom Data
  - name: First Made Purchase
    description: Segments your users by the earliest recorded time that they have made a purchase in your app.
    tags:
      - User Activity
  - name: First Purchase for App
    description: Segments your users by the earliest recorded time that they have bought any item from your app.
    tags:
      - User Activity
  - name: First Purchased Product
    description: Segments your users by the earliest recorded time that they have bought a specific item from your app (special membership, gift certificate, etc…).
    tags:
      - User Activity
  - name: First Used App
    description: Segments your users by the earliest recorded time that they opened your app. <em>Note that this will capture the first session they have using a version of your app with the Braze SDK integrated.</em>
    tags:
      - User Activity
  - name: First Used Specific App
    description: Segments your users by the earliest recorded time that they opened any of your apps within your app group.
    tags:
      - User Activity
  - name: Last Made Purchase
    description: Segments your users by the most recent time that they have made a purchase in your app.
    tags:
      - User Activity
  - name: Last Purchase for App
    description: Segments your users by the most recent time that they have bought bought an item from your app.
    tags:
      - User Activity
  - name: Last Purchased Product
    description: Segments your users by the most recent time that they have bought a specific item from your app (special membership, gift certificate, etc…).
    tags:
      - User Activity
  - name: Last Used App
    description: Segments your users by the most recent time that they have opened your app.
    tags:
      - User Activity
  - name: Last Used Specific App
    description: Segments your users by the most recent time that they have opened a specific, designated app.
    tags:
      - User Activity
  - name: Median Session Duration
    description: Segments your users by the median length of their sessions in your app.
    tags:
      - User Activity
  - name: Money Spent In-App
    description: Segments your users by the amount of money that they have spent in your app.
    tags:
      - User Activity
  - name: Most Recent App Version
    description: Segments your users by the latest version of your app that they have used.
    tags:
      - User Activity
  - name: Most Recent Location
    description: Segments your users by the last recorded location at which they have used your app.
    tags:
      - User Activity
  - name: Purchased Product
    description: Segments your users by products purchased in your app.
    tags:
      - User Activity
  - name: Session Count
    description: Segments your users by the number of sessions they have had in any of your apps within your app group.
    tags:
      - User Activity
  - name: Session Count For App
    description: Segments your users by the number of sessions they have had in a specific, designated app.
    tags:
      - User Activity
  - name: Total Number of Purchases
    description: Segments your users by how many purchases they have made in your app.
    tags:
      - User Activity
  - name: Uninstall Date
    description: Segments your users by the date they uninstalled your app.
    tags:
      - User Activity
  - name: Uninstalled
    description: Segments your users by whether they have uninstalled your app.
    tags:
      - User Activity
  - name: X Money Spent in Last Y Days
    description: Segments your users by the amount of money that they have spent in your app in the last 1, 3, 7, 14, 21, and 30 days. This amount will only include the sum of the last 50 purchases.
    tags:
      - User Activity
  - name: X Product Purchased in Last Y Days
    description: Segments your users by the number of times (between 0 and 50) they have bought a specific item from your app in the last 1, 3, 7, 14, 21, and 30 days (special membership, gift certificate, etc…).
    tags:
      - User Activity
  - name: X Purchase Property in Y Days
    description: Segments your users by the number of times a purchase was made in relation to a certain purchase property in the last 1, 3, 7, 14, 21, and 30 days.
    tags:
      - User Activity
  - name: X Purchases in Last Y Days
    description: Segments your users by the number of times (between 0 and 50) they have made a purchase in the last 1, 3, 7, 14, 21, and 30 days.
    tags:
      - User Activity
  - name: X Sessions in Last Y Days
    description: Segments your users by the number of sessions (between 0 and 50) they have had in your app in the last 1, 3, 7, 14, 21, and 30 days.
    tags:
      - User Activity
  - name: Clicked Card
    description: Segments your users by whether or not they have clicked a specific card or promotion.
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign
    description: Segments your users by whether or not they have interacted with a specific campaign.
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    description: Segments your users by whether or not they have interacted with a specific campaign or Canvas with a specific tag.
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    description: Segments your users by whether or not they have interacted with a specific Canvas step.
    tags:
      - Retargeting
  - name: Converted From Campaign
    description: Segments your users by whether or not they have converted on a specific campaign.
    tags:
      - Retargeting
  - name: Converted From Canvas
    description: Segments your users by whether or not they have converted on a specific Canvas.
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    description: Segments your users by whether or not they have entered a variation path of a specific Canvas.
    tags:
      - Retargeting
  - name: Has Never Received A Campaign or Canvas Step
    description: Segments your users by whether or not they have received a designated campaign or canvas step.
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
  - name: Is Not In Segment
    description: Segments your users by whether or not they are included in an already existing segment.
    tags:
      - Retargeting
  - name: Last Received Campaign or Canvas With Tag
    description: Segments your users by when they received a specific campaign or Canvas with a specific tag.
    tags:
      - Retargeting
  - name: Last Received Specific Campaign
    description: Segments your users by when they last received a specific campaign.
    tags:
      - Retargeting
  - name: Last Received Specific Canvas Step
    description: Segments your users by selecting those who received a specific, designated Canvas Step.
    tags:
      - Retargeting
  - name: Received Campaign
    description: Segments your users by whether or not they have received a specific campaign.
    tags:
      - Retargeting
  - name: Received Campaign Variant
    description: Segments your users by which variant of a multivariate campaign they have received.
    tags:
      - Retargeting
  - name: Received Campaign or Canvas with Tag
    description: Segments your users by whether or not they have received a specific campaign or Canvas with a specific tag.
    tags:
      - Retargeting
  - name: Received Canvas Step
    description: Segments your users by whether or not they have received a specific Canvas step.
    tags:
      - Retargeting
  - name: Has Marked You As Spam
    description: Segments your users by whether or not they have marked your messages as spam.
    tags:
      - Marketing Activity
  - name: Last Engaged With Message
    description: Segments your users by the last time that they have clicked or opened one of your messaging channels (email, in-app, push).
    tags:
      - Marketing Activity
  - name: Last Enrolled in Any Control Group
    description: Segments your users by the last time that they fell into the control group in a campaign.
    tags:
      - Marketing Activity
  - name: Last In App Message Impression
    description: Segments your users by determining the last in app message impression was received.
    tags:
      - Marketing Activity
  - name: Last Received Any Message
    description: Segments your users by determining the last message that was received.
    tags:
      - Marketing Activity
  - name: Last Received Any Campaign
    description: Segments your users by the last time that they have received a campaign on any messaging channel.
    tags:
      - Marketing Activity
  - name: Last Received Email
    description: Segments your users by the last time that they have received one of your email messages.
    tags:
      - Marketing Activity
  - name: Last Received Push
    description: Segments your users by the last time that they received one of your push notifications.
    tags:
      - Marketing Activity
  - name: Last Received Webhook
    description: Segments your users by the last time that Braze sent a webhook for that user.
    tags:
      - Marketing Activity
  - name: Last Viewed News Feed
    description: Segments your users by the last time that they have visited your app’s news feed interface.
    tags:
      - Marketing Activity
  - name: News Feed View Count
    description: Segments your users by the number of times that they have viewed your app’s news feed interface.
    tags:
      - Marketing Activity
  - name: Age
    description: Segments your users by their age, as they indicated from within your app.
    tags:
      - User Attributes
  - name: Amplitude Cohorts
    description: Clients who use Amplitude to supplement their segments may import and choose from those cohorts.
    tags:
      - User Attributes
  - name: Background Push Enabled
    description: Segments your users on whether they have enabled background push or not.
    tags:
      - User Attributes
  - name: Birthday
    description: Segments your users by their birthday, as they indicated from within your app. <br> Users with a birthday on February 29th will be included in segments including March 1.
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
    description: Segments your users by their mobile phone’s model version.
    tags:
      - User Attributes
  - name: Device OS
    description: Segments your users by their mobile phone’s operating system.
    tags:
      - User Attributes
  - name: Email Available
    description: Segments your users by whether or not they have reported their respective email addresses, and if they are subscribed/opted-in to email.
    tags:
      - User Attributes
  - name: Email Opt In Date
    description: Segments your users by the date on which they opted into email.
    tags:
      - User Attributes
  - name: Email Subscription Status
    description: Segments your users by their subscription status for email.
    tags:
      - User Attributes
  - name: Subscription Groups
      description: Segments your users by their Subscription Group for email.
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
    description: Segments your users by gender, as they indicated from within your app..
    tags:
      - User Attributes
  - name: Has App
    description: Segments by whether or not a user has your app.
    tags:
      - User Attributes
  - name: Language
    description: Segments your users by their preferred language.
    tags:
      - User Attributes
  - name: Last Name
    description: Segments your users by their last name, as they indicated from within your app..
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
    description: Segments your users who have explicitly activated push notifications for any of the apps in your app group. After segmenting with this filter, you will be able to see a breakdown of who is in that segment for Android, iOS, and web in the bottom panel, called <em>Reachable Users</em>.
    tags:
      - User Attributes
  - name: Push Enabled For App
    description: Segments by whether or not your user has push enabled for your app on their device.
    tags:
      - User Attributes
  - name: Push Opt In Date
    description: Segments your users by the date on which they opted into push.
    tags:
      - User Attributes
  - name: Push Subscription Status
    description: Segments your users by their <a href="/docs/help/best_practices/push/push_subscription_status/#push-subscription-status">subscription status</a> for push.
    tags:
      - User Attributes
  - name: Push Unsubscribed Date
    description: Segments your users by the date on which they unsubscribed from future push notifications.
    tags:
      - User Attributes
  - name: Random Bucket Number
    description: Segments your users by a randomly assigned number (0 to 9999 inclusive). Can enable the creation of uniformly distributed segments of truly random users for A/B and multivariate testing.
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
      - Install Attribution
  - name: Install Attribution Adgroup
    description: Segments your users by the adgroup that their install was attributed to.
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
  - name: Connected to Facebook
    description: Segments your users who have granted Facebook account access within your app.
    tags:
      - Social Activity
  - name: Connected to Twitter
    description: Segments your users who have granted Twitter account access within your app.
    tags:
      - Social Activity
  - name: Number of Facebook Friends Using App
    description: Segments your users by the number of friends that they have on Facebook that are using your app.
    tags:
      - Social Activity
  - name: Number of Twitter Followers
    description: Segments your users by the number of followers that they have on Twitter.
    tags:
      - Social Activity
  - name: Device IDFA
    description: Allows you to designate your campaign recipients by IDFA for testing.
    tags:
      - Testing
  - name: Device IDFV
    description: Allows you to designate your campaign recipients by IDFV for testing.
    tags:
      - Testing
  - name: Email Address
    description: Allows you to designate your campaign recipients by individual email addresses for testing.
    tags:
      - Testing
  - name: External User ID
    description: Allows you to designate your campaign recipients by individual user IDs for testing.
    tags:
      - Testing
  - name: Segment Membership
    description: Allows you to filter based on segment membership anywhere that filters are used (i.e. segments, campaigns, etc) and target multiple different segments within one campaign.
    tags:
      - Other
  - name: Provisionally Authorized on iOS
    description: Allows you to find users who are provisionally authorized on iOS 12 for a given app.
    tags:
      - Other



---
