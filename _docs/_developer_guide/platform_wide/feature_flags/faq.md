---
nav_title: Frequently Asked Questions
article_title: Frequently Asked Questions
page_order: 40
description: "This page provides answers to frequently asked questions about campaigns."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
---

# Frequently Asked Questions

## Features and Support

### How can I join the Feature Flags Beta program {#join-beta}

Braze Feature Flags is currently in an open Beta. Please ask your Braze account team to learn more about joining the Beta program.

### What platforms are Braze Feature Flags supported on? {#platforms}

Braze supports Feature Flags on iOS, Android, and Web platforms with the following SDK version requirements:

{% sdk_min_versions android:24.2.0 web:4.6.0 swift:5.9.0 %}

Do you need support on other platforms? Email our team: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### What is the level of effort involved when implementing a feature flag? {#level-of-effort}

A feature flag can be created and integrated in just **minutes**!

Most of the effort involved will be related to your engineering team building the new feature you plan to roll out. But when it comes to adding a feature flag, it's as simple as an `IF`/`ELSE` statement in your app or website's code:

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // show the new homepage your team has built
}
else {
    // show the old homepage
}
```

### How can Feature Flags benefit marketing teams? {#marketing-teams}

Marketing teams can use feature flags to coordinate product announcements (i.e. launch emails) when a feature is only enabled for a small percentage of users.

For example, with Braze Feature Flags you can rollout a new Customer Loyalty program to 10% of users in your app, and send an email, push, or other messaging to that same 10% of enabled users using our upcoming Canvas Feature Flag step.

### How can Feature Flags benefit product teams? {#product-teams}

Product teams can use feature flags to perform gradual rollouts or soft launches of new features in order to monitor KPIs and customer feedback before opening it up to all users.

Product teams can also run an A/B split test to measure how a new feature impacts conversion rates compared to users with the feature disabled. This can be done using our upcoming Canvas Feature Flag step.

Also, Product teams can remotely populate variable and content in an app, such as deeplinks, text, imagery or other dynamic content powered by [Feature Flag Properties][properties].

### How can Feature Flags benefit engineering teams? {#engineering-teams}

Engineering teams can use feature flags to reduce risk of launching new features, and having to rush to deploy code fixes in the middle of the night.

By releasing new code hidden behind a feature flag, your team can turn the feature on or off remotely from the Braze dashboard, and bypass the delay of pushing out new code or waiting for an app store update's approval.

### Can feature flags be used to control when the Braze SDK is initialized? {#initialization}

No, the SDK must be initialized in order to download and synchronize feature flags for the current user. This means you can't use feature flags to limit which users are created or tracked in Braze.

## Feature Rollouts and Targeting

### Can a feature flag be rolled out to only a select group of users? {#target-users}

Yes, simply create a Segment in Braze that targets the individual users - by email address, user_id, or any other attribute on your user profiles. Then, deploy the feature flag to 100%.

### How does adjusting the rollout % affect users who were already bucketed into the enabled group? {#random-buckets}

Feature flag rollouts remain consistent for users, across devices and sessions.

- When a feature flag is rolled out to 10% of random users, that 10% will remain enabled and persist for the lifetimem of that feature flag.
- If you increase the rollout from 10% to 20%, the same 10% will remain enabled, plus a new, additional 10% of users will be added to the enabled group.
- If you lower thet rollout from 20% back down to 10%, only the original 10% of users will remain enabled.

This strategy helps ensure that users are shown a consistant experience in your app, and don't flip-flop back and forth across sessions. Of course, disable a feature down to 0% will remove all users from the feature flag, which is helpful in case you discover a bug or need to disable the feature altogether.

### Can I create a segment of users who are currently in a feature flag? {#feature-flag-filter}

This is on our product roadmap. To help prioritize this, please raise this feedback with your Braze account team, or email our team: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

## Technical Topics

### How frequently are feature flags refreshed by the SDK? {#refresh-frequency}

Feature flags are refreshed at session start, and when changing active users. Feature flags can also be manually refreshed using the SDK's [refresh method][refreshing].

Keep in mind that refreshing feature flags may be throttled if performed too quickly (rate limiting subject to change), so it's best to only refresh before a user interacts with new features or periodically in the app if necessary.

### Are feature flags available while a user is offline? {#offline}

Yes, once feature flags are refreshed they are stored locally on the user's device and can be accessed while offline.

### What happens if feature flags are refreshed mid-session? {#listen-for-updates}

Feature flags may be refreshed mid-session. There are scenarios where you may want to update your app (if certain variables or configuration should change), while other scenarios you may not want to update your app (to avoid a shocking change in how your UI is rendered).

To control this, you can [listen for updates][listen-for-updates] to feature flags and based on which feature flags have changed, make that determination to re-render your app or not.

# Best Practices

### Naming conventions

- Consider following a pattern such as `{product}.{feature}.{action}`. 
  - For example, in a ride sharing app your feature ID may be `driver.profile.show_animation_v3`
- This also helps when searching for a specific product area or team's feature flags
- Make sure that the default state for a feature flag is disabled in your app
  - For example, it is an anti-pattern if you have a flag named `disable_feature_xyz`. There may be exceptions, but try to avoid confusing a feature's "enabled" status with the actual enabled behavior (disabling feature xyz).

### Planning ahead

Always play it safe. When considering new features that may require a kill-switch, it's better to release new code with a feature flag and not need it, than it is to realize a new app update is required.

### Be descriptive

Add a description to your feature flag. While this is an optional field in Braze, it can help answer questions others may have when browsing available feature flags.

- Contact details for who is responsible for the enablement and behavior of this flag
- When this flag should be disable
- Links to documentation or notes about the new feature this flag controls
- Any depdencies or notes on how to use the feature

### Clean up old feature flags

We're all guilty of leaving features on at 100% rollout for longer than necessary.

To help keep your code (and Braze dashboard) clean, remove permanent feature flags from your code base once all users have upgraded and you no longer need the option to disable the feature.

This helps reduce the complexity of your development environment, but also keeps your list of feature flags tidy.

# Questions?

Have questions or feedback? Email our team: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

[properties]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#properties
[refreshing]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#refreshing
[updates]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#updates
