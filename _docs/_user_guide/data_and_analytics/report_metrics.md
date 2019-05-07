---
page_order: 0
nav_title: Report Metrics Glossary
layout: glossary_page
glossary_top_header: "Report Metrics Glossary"
glossary_top_text: "These are terms you'll find in your reports in your Braze account. Search for the metrics you need, or filter by channel. <br>  <br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

glossary_tag_name: Channels
glossary_filter_text: "Select Channels below to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Email
  - name: In-App Message
  - name: Web Push
  - name: iOS Push
  - name: Android Push
  - name: Webhook
  - name: News Feed

glossaries:
  - name: Variation
    description: Variation of a campaign, differing as defined by the creator.
    calculation: Count
    tags:
      - All
  - name: Audience
    description: Percentage of users who received a particular message. This number is received from Braze.
    calculation: (Number of Recipients in Variant) / (Unique Recipients)
    tags:
      - All
  - name: Unique Recipients
    description: Exact number of users who received a particular message. This number is received from Braze.
    calculation: Count
    tags:
      - Email
      - Web Push
      - iOS Push
      - Android Push
      - All Push
      - News Feed
  - name: Total Impressions
    description: The number of users whose devices reported that the in-app message has been delivered (if a user receives a message twice, they will be counted twice). This number is a sum of number of impression events that Braze receives from the SDKs.
    calculation: Count
    tags:
      - In-App Message
      - News Feed
  - name: Unique Impressions
    description: The total number of people who actually received and viewed the in-app message (if a user receives a message twice, they will be only counted once). This number is a sum of number of impression events that Braze receives from the SDKs.
    calculation: Count
    tags:
      - In-App Message
      - News Feed
  - name: Sends
    description: The total number of messages sent in a campaign. This number is received from Braze.
    calculation: Count
    tags:
      - All
  - name: Deliveries
    description: The total number of messages successfully sent to and received by eligible users.
    calculation: (Sends - Bounces) / (Sends)
    tags:
      - All Push
      - Email
      - Web Push
      - iOS Push
      - Android Push
  - name: Bounces
    description: The total number of messages that were unsuccessful. This could occur because there is not a valid push token, the email addresses were incorrect or deactivated, or the user unsubscribed after the campaign was launched.
    calculation: (Bounces) / (Sends)
    tags:
      - All Push
      - Email
      - Web Push
      - iOS Push
  - name: Spam
    description: The total number of emails delivered that were marked as "spam".
    calculation: (Marked as Spam) / (Sends)
    tags:
      - Email
  - name: Errors
    description: The number of errors returned by webhook events (incremented during the sending process).
    tags:
      - Webhook
  - name: Total Opens
    description: The total number of messages that were opened.
    calculation: (Opens) / (Deliveries) (for Email) or (Unique Opens) / (Deliveries) (for all Push)
    tags:
      - Email
      - iOS Push
      - Android Push
      - Web Push
      - All Push
  - name: Unique Opens
    description: The total number of delivered emails that have been opened by a single user at least once. This is tracked over a 7 day period for Email.
    calculation: (Unique Opens) / (Deliveries)
    tags:
      - Email
  - name: Direct Opens
    description: The total number (and percentage) of push notifications that were directly opened from that push.
    calculation: (Direct Opens) / (Deliveries)
    tags:
      - iOS Push
      - Android Push
  - name: Influenced Opens
    description: The total number (and percentage) of users who opened the app after the push notification was sent, without directly opening the push.
    calculation: (Influenced Opens) / (Deliveries)
    tags:
      - iOS Push
      - Android Push
  - name: Total Clicks
    description: The total number (and percentage) of users who clicked within the delivered email.
    calculation: (Total Clicks) / (Deliveries)
    tags:
      - Email
      - News Feed
  - name: Unique Clicks
    description: Distinct number of recipients who have clicked within a message at least once. This is tracked over a 7 day period for Email.
    calculation: (Unique Clicks) / (Deliveries)
    tags:
      - Email
      - News Feed
  - name: Body Clicks
    description: Occurs when someone clicks on a slideup, modal, or full-screen in-app message that has no buttons.
    calculation: (Body Clicks) / (Impressions)
    tags:
      - In-App Message
  - name: Button 1 Clicks
    description: Total number of clicks on Button 1 of the message.
    calculation: (Button 1 Clicks) / (Impressions)
    tags:
      - In-App Message
  - name: Button 2 Clicks
    description: Total number of clicks on Button 2 of the message.
    calculation: (Button 2 Clicks) / (Impressions)
    tags:
      - In-App Message
  - name: Unsubscribes
    description: The number of recipients whose subscription state changed to unsubscribed as a result of clicking the Braze provided unsubscribe URL.
    calculation: (Unsubscribes) / (Deliveries)
    tags:
      - Email
  - name: Revenue
    description: The total revenue in dollars from campaign recipients within the set primary conversion window.
    tags:
      - All
  - name: Primary Conversions (A)
    description: The number of times a defined event occurred. This defined event is determined by the marketer when building the campaign.
    tags:
      - All
  - name: Conversion Rate
    description: The percentage of times a defined event occurred compared to all recipients of a sent message. This defined event is determined when you build the campaign.
    calculation: (Primary Conversions) / (Unique Recipients)
    tags:
      - All
  - name: Conversions (B, C, D)
    description: The percentage of times a defined event occurred compared to all recipients of a sent message. This defined event is determined when you build the campaign.
    tags:
      - All
  - name: Confidence
    description: The percentage of confidence that a certain variant of a message is outperforming the control group.
    tags:
      - All
  - name: Pending Retry
    description: The number of requests that were temporarily rejected, by the receiving server, but still attempted for re-delivery by the ESP. The ESP will retry delivery until a timeout period is reached (typically after 72 hours).
    tags:
      - Email

---
