---
nav_title: "Types of push notifications"
article_title: Types of Push Notifications
page_order: 1
page_type: glossary
description: "This glossary lists the different types of Push Notifications you can use Braze to send."
channel: push

layout: glossary_page
glossary_top_header: "Types of push notifications"
glossary_top_text: "There are many types of push notifications you can use to interact with your customers. These can be narrowed by channel and used to meet the needs of many different users. You can configure most of these settings in your Push campaigns, but there are notes in the following descriptions that will indicate whether any backend configurations are needed and what those might be."

glossary_tag_name: Channels
glossary_filter_text: "Select any of the following channels to narrow Push Type options."

# category to icon/fa or image mapping
glossary_tags:
  - name: iOS
  - name: Android
  - name: Web

glossaries:
  - name: "Regular Push"
    description: "The all-encompassing Push message. These appear on your user's device with a notification sound and message which slides in or appears in a notification bar or stack."
    tags:
      - iOS
      - Android
      - Web
  - name: "Web Push"
    description: "These push messages appear in Web Apps or Browsers. They still require permission to reach the customer. Note that Web Push does not work if the user is using a hidden browser."
    tags:
      - Web
  - name: "Push Primer Campaigns"
    description: "In-app message campaigns used to gain explicit push opt-in or opt-out signal from users. Through the primer, you can avoid sending notifications to users that are likely to turn off push through the device settings. For iOS, push campaigns are relevant as foreground push notifications (such as notifications that wake up the device) are not enabled until a user explicitly opts into iOS' native push prompt."
    tags:
      - iOS
      - Android
      - Web
  - name: "Push Stories"
    description: "Push Stories are immersive messages that take your user through a visual journey in the form of a carousel. These are available for mobile devices only."
    tags:
      - iOS
      - Android
  - name: "Push with Action Buttons"
    description: "Push with action buttons are messages that allow you to provide options to your users and offer several calls to action."
    tags:
      - iOS
      - Android
      - Web
  - name: "Rich Push Notifications"
    description: "Rich Push Notifications are notifications with immersive images and creative content that can expand beyond a simple icon and call to action text."
    tags:
      - iOS
      - Android
  - name: "Silent Push Notification"
    description: "A push notification that does not wake up the device when rendering on the device. Instead, the notification will be stored in the device's notification tray."
    tags:
      - iOS
      - Android
  - name: "Provisional Push Notifications for iOS"
    description: "Introduced by Apple in iOS 12, provisional authorization automatically occurs on install for iOS apps, allowing brands to send silent notifications without displaying a push prompt to users. When the silent push is sent and viewed in the device's notification tray, users will be given the option to allow or discontinue push notifications."
    tags:
      - iOS
  - name: "HTML Push Notifications"
    description: "HTML Push Notifications are push messages that are hard coded in HTML and do not use the pre-set push templates that Braze provides. Having the option to create HTML push notifications allows your company to have full creative freedom and consistent branding when it comes to how you want these push messages to look."
    tags:
      - Android
  - name: "Notification IDs & Channel IDs"
    description: "Notification IDs and Channel IDs allow you to replace or update push notifications already received, but not opened, by the user."
    tags:
      - iOS
      - Android
  - name: "Background Push Notifications"
    description: "Push notifications that are not rendered for the device. Usually used to send packets of information down to the app for background processes and uninstall tracking. A Background-enabled push token is required for background push to be sent."
    tags:
      - iOS
      - Android
      - Web
  - name: "Wearable Push Notifications"
    description: "These push notifications allow brands to send messages directly to wearable devices like the Apple Watch."
    tags:
      - iOS

---
