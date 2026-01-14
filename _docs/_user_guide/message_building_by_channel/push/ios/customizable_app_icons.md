---
nav_title: "Custom app icon feature (iOS)"
article_title: Custom App Icon Feature
page_order: 7
page_type: reference
description: "This reference article covers the iOS 10.3 update on Customizable App Icon."
platform: iOS
channel:
  - push

---

# Custom app icon feature (iOS 10.3) 

> With iOS 10.3 Apple introduced the ability to change an app's home screen icon without having to update the application from the Apple App Store. The developer can now allow the user to change the home screen icon inside of their app. Apple requires all of the app icon images that the developer wants to make available to the user to be included in the binary that is submitted to Apple for review during the publishing of the app on the Apple App Store.

To notify your users of this feature it is possible to send an in-app message or push notification through Braze to the user explaining this functionality or asking the user if they would like to change their icon. The developer would only need to create a deep link into the application where the native iOS prompt can be shown to make the icon change. This is similar to the same guidance we provide around setting up a push notification primer for APNs today.

In addition, this messaging can take full advantage of segmentation to make the message copy highly contextual to a user. You can also leverage A/B testing of messages to see which messaging makes the most impact on your desired result.
