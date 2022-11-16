---
nav_title: In-App Rating Prompt for iOS
article_title: In-App Rating Prompt for iOS
page_order: 6
description: "This article describes approaches and implications for using Braze to ask users to review your app."
channel:
  - in-app messages

---

# In-app rating prompt for iOS

> This article describes approaches and implications for using Braze to ask users to review your app. For tips on how to make an effective app rating campaign, check out [The Do's and Don'ts of Customer App Ratings](https://www.braze.com/resources/articles/the-dos-and-donts-of-customer-app-ratings).

Apple offers a native prompt, introduced with iOS 10.3, that lets users rate apps from within the app itself. If you want to request app ratings from users using an in-app message on iOS, you must use the native prompt, as Apple disallows custom review prompts (see [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/#code-of-conduct), section 5.6.1).

Per Apple guidelines, app review prompts can be displayed to a user 3 times a year, so any app review campaigns should take advantage of [rate limiting]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/). Users can also opt-out of seeing app review prompts entirely in their app settings.

## Using Braze to ask users for app reviews

You can still take advantage of Braze campaigns to ask users to rate and review your app at the right moment. There are two main approaches you can take.

### Approach 1: Deep linking to the App Store

With this approach, you want to encourage users to visit the App Store to add a review. To do so, create an in-app message campaign that [deep links]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) to the App Store.

![Two mobile screens side-by-side. The first is an in-app message that asks the user to rate the app on the App Store. The second is the iOS App Store page for that app.][1]

### Approach 2: Soft priming

This approach involves priming with a separate in-app message. Priming is a way of asking users for permission before you send them a native App Store review prompt. To do so, create an in-app message campaign and add a custom deep link that calls the `requestReview(in:)` method when clicked. For detailed steps, refer to [Custom App Store review prompt]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/custom_app_store_review_prompt).

![Two in-app messages side-by-side. The first primes the user to rate the app by asking if they have a moment to rate the app. The second is the native iOS App Store review message, displaying a scale of five stars the user can select to rate the app.][2]

### Considerations

As an alternative to soft priming, you could also display the iOS app rating prompt directly without any Braze soft primer message displayed before. The advantage of this is if the user is opted-out of app review prompts, there wouldn't be the suboptimal user experience of trying to rate the application but no prompt appearing to do so.


[1]: {% image_buster /assets/img_archive/app_store_app_review.png %}
[2]: {% image_buster /assets/img_archive/prime_app_review.png %}