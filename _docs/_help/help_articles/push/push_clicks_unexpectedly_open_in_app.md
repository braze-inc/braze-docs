---
nav_title: Push clicks unexpectedly opening in app
article_title: Push Clicks Unexpectedly Opening in App
page_type: solution
description: "This help article covers how to troubleshoot when a push link is expected to open in a web browser, not the app."
channel: push
---

# Push clicks unexpectedly opening in app

If you're experiencing issues with links in push notifications unexpectedly opening in your app instead of your web browser, there may be an issue with your campaign configuration or SDK implementation. Refer to these steps for help.

## Verify on-click behavior

In your campaign or Canvas step, double-check that **Open web URL inside mobile app** is not selected. If it is, clear the selection and relaunch. 

!["On-click behavior" field of configuring a push set to "Open web URL" with "Open web URL inside mobile app" unchecked.]({% image_buster /assets/img/push_on_click.png %})

The default interaction for the on-click behavior "Open web URL" differs by SDK version. For SDK versions iOS 2.29.0 and Android 2.0.0 and higher, this option is selected by default and web URLs will open in a web view within the app. Prior to these versions, this option is cleared by default and web URLs open in the device's default web browser.

If this is not the issue, there may be a problem with your push implementation. 

## Double-check push integration

If links in your push notifications are opening in the app unexpectedly, it might be due to issues with your push notification integration or customization settings. Follow these steps to troubleshoot:

1. **Review the push delegate implementation:** Ensure that the Braze push delegate is implemented correctly. For detailed instructions, refer to the integration guide for push notifications for your [platform]({{site.baseurl}}/developer_guide/home/).
2. **Inspect custom link handling:** Check if the app includes custom handling for all `https://` links. Custom configurations might override default behaviors. Collaborate with your development team to review and adjust these settings if necessary.
3. **Verify iOS push registration:** For iOS, revisit step 1 of the push integration guide on [registering push notifications with APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). Ensure your delegate object is assigned synchronously before the app finishes launching. This step should be completed in the `application:didFinishLaunchingWithOptions:` method.
4. **Test your integration:** After making adjustments, test the push notification behavior on both iOS and Android devices to confirm the issue is resolved.

If the problem persists, reach out to [Braze Support]({{site.baseurl}}/support_contact) for further assistance.


*Last updated on December 6, 2024*