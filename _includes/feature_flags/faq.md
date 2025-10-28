# Frequently asked questions

> This article provides answers to some frequently asked questions about feature flags.

## Functionality and support

### What platforms are Braze feature flags supported on? {#platforms}

Braze supports feature flags on iOS, Android, and Web platforms with the following SDK version requirements:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Do you need support on other platforms? Email our team: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### What is the level of effort involved when implementing a feature flag? {#level-of-effort}

A feature flag can be created and integrated in a few minutes. 

Most of the effort involved will be related to your engineering team building the new feature you plan to roll out. But when it comes to adding a feature flag, it's as simple as an `IF`/`ELSE` statement in your app or website's code:

{% tabs %}
{% tab JavaScript %}

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

{% endtab %}
{% tab Java %}

```java
if (braze.getFeatureFlag("new_shopping_cart").getEnabled()) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (braze.getFeatureFlag("new_shopping_cart")?.enabled == true) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% endtabs %}

### How can feature flags benefit Marketing teams? {#marketing-teams}

Marketing teams can use feature flags to coordinate product announcements (such as product launch emails) when a feature is only enabled for a small percentage of users.

For example, with Braze feature flags, you can roll out a new Customer Loyalty program to 10% of users in your app, and send an email, push, or other messaging to that same 10% of enabled users using the Canvas Feature Flag step. 

### How can feature flags benefit Product teams? {#product-teams}

Product teams can use feature flags to perform gradual rollouts or soft launches of new features in order to monitor key performance indicators and customer feedback before making it available to all users.

Product teams can use [feature flag properties]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#properties) to remotely populate content in an app, such as deep links, text, imagery, or other dynamic content.

Using the Canvas Feature Flag step, Product teams can also run an A/B split test to measure how a new feature impacts conversion rates compared to users with the feature disabled. 

### How can feature flags benefit engineering teams? {#engineering-teams}

Engineering teams can use feature flags to reduce the risk inherent in launching new features and avoid rushing to deploy code fixes in the middle of the night.

By releasing new code hidden behind a feature flag, your team can turn the feature on or off remotely from the Braze dashboard, bypassing the delay of pushing out new code or waiting for an app store update approval.

## Feature rollouts and targeting

### Can a feature flag be rolled out to only a select group of users? {#target-users}

Yes, create a segment in Braze that targets specific users&mdash;by email address, `user_id`, or any other attribute on your user profiles. Then, deploy the feature flag for 100% of that segment.

### How does adjusting the rollout percentage affect users who were previously bucketed into the enabled group? {#random-buckets}

Feature flag rollouts remain consistent for users across devices and sessions.

- When a feature flag is rolled out to 10% of random users, that 10% will remain enabled and persist for the lifetime of that feature flag.
- If you increase the rollout from 10% to 20%, the same 10% will remain enabled, plus a new, additional 10% of users will be added to the enabled group.
- If you lower the rollout from 20% to 10%, only the original 10% of users will remain enabled.

This strategy helps ensure that users are shown a consistent experience in your app and don't flip-flop back and forth across sessions. Of course, disabling a feature down to 0% will remove all users from the feature flag, which is helpful if you discover a bug or need to disable the feature altogether.

## Technical topics

### Can feature flags be used to control when the Braze SDK is initialized? {#initialization}

No, the SDK must be initialized to download and synchronize feature flags for the current user. This means you can't use feature flags to limit which users are created or tracked in Braze.

### How frequently does the SDK refresh feature flags? {#refresh-frequency}

Feature flags are refreshed at session start and when changing active users. Feature flags can also be manually refreshed using the SDK's [refresh method]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#refreshing). Feature flag refreshes are rate limited to once every five minutes (subject to change).

Keep in mind that good data practices recommend not refreshing feature flags too quickly (with potential rate limiting if done so), so it's best only to refresh before a user interacts with new features or periodically in the app if necessary.

### Are feature flags available while a user is offline? {#offline}

Yes, after feature flags are refreshed, they are stored locally on the user's device and can be accessed while offline.

### What happens if feature flags are refreshed mid-session? {#listen-for-updates}

Feature flags may be refreshed mid-session. There are scenarios where you may want to update your app if certain variables or your configuration should change. There are other scenarios where you may not want to update your app, to avoid a shocking change in how your UI is rendered.

To control this, [listen for updates]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#updates) to feature flags and determine whether to re-render your app based on which feature flags have changed. 

### Why aren't users in my Global Control Group receiving feature flags experiments?

You can't enable feature flags for users in your [Global Control Group]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/). This means users in your Global Control Group also can't be part of Feature Flag experiments.

## Additional questions?

Have questions or feedback? Email our team: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

