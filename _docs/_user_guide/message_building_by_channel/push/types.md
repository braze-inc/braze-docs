---
nav_title: Types of Push Notifications
page_order: 1

page_type: glossary
description: "This glossary lists the different types of Push Notifications you can use Braze to send."
channel: push

layout: glossary_page
glossary_top_header: "Types of Push Notifications"
glossary_top_text: "There are many types of push notifications you can use to interact with your customers. These can be narrowed by channel and used to meet the needs of many different users. You can configure most of these settings in your Push Campaigns, but there are notes in the descriptions below that will indicate whether any backend configurations are needed and what those might be."

glossary_tag_name: Channels
glossary_filter_text: "Select any channel below to narrow Push Type options."

# category to icon/fa or image mapping
glossary_tags:
  - name: iOS
  - name: Android
  - name: Web

glossaries:
  - name: "Regular Push"
    description: "The all-encompassing Push Message. Appear on your user's device with a notification sound and message which slides in or appears in a notification bar or stack."
    tags:
      - iOS
      - Android
      - Web
  - name: "Web Push"
    description: "These push messages appear in Web Apps or Browsers. They still require permissions to reach the customer."
    tags:
      - Web
  - name: "Push Primer Campaigns"
    description: "Though Push Primer Campaigns aren't necessarily a 'type' of message, they are a required method for enabling push on a user's device. For iOS devices, push primer campaigns can actually be your first push message, which are called 'provisional push' messages and show the user immediate value in enabling push."
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
    description: "Push with Action Buttons are messages that allow you to provide options to your users and offer several calls to action."
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
    description: "Silent Push Notifications are important because they don't intrude as much as regular push notifications."
    tags:
      - iOS
      - Android
      - Web
  - name: "Provisional Push Notifications for iOS"
    description: "Segments your users based upon the calendar date of custom attributes. This filter looks for matches of an indicated day/month, but ignores the year. As such, the filter works nicely for anniversary use cases."
    tags:
      - iOS
  - name: "HTML Push Notifications"
    description: "Determines the earliest time that a user has performed a specially recorded event (above)."
    tags:
      - iOS
      - Android
      - Web
  - name: "Notification IDs & Channel IDs"
    description: "Notification IDs and Channel IDs allow you to replace or update push notifications already received, but not opened, by the user."
    tags:
      - iOS
      - Android
  - name: "Background Push Notifications"
    description: "These push notifications don't appear in the view of the user at all, though they must still be enabled to receive them."
    tags:
      - iOS
      - Android
      - Web

---
