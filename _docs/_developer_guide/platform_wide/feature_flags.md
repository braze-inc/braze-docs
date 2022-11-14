---
nav_title: Feature Flags
article_title: Feature Flags
page_order: 3
description: "Learn how to coordinate new feature rollouts with Braze Feature Flags"
platform:
  - iOS
  - Android
  - Web
---

# Feature flags

Feature flags allow you to remotely enable or disable in-production functionality for a specific section of your user base. 

Create a new feature flag within the Braze dashboard by providing a name and an `ID`, a target audience, and a percentage of traffic to allocate to this feature. Then, using that same `ID` in your app or website's code, you can restrict certain parts of the business logic from running.

For example, if you've built a new profile page for your ride-sharing app, instead of releasing it (and potential bugs) directly to your entire user base, you can roll out the new profile page to only a single segment. 

## Prerequisites

To use feature flags, ensure your SDKs are up to date with at least these minimum versions:
<!-- TODO -->
{% sdk_min_versions android:9999 web:9999 swift:9999 %}

## Implementation
Manage, create, and delete feature flags by navigating to **Feature Flags** in the left sidebar of the Braze dashboard. This page displays a list of existing feature flags for this app group.

[TO DO: ADD SCREENSHOT]

### Create a new feature flag
To create a new feature flag, click the **Create Feature Flag** button. Then, define your feature flag's [details](#details), [properties](#properties), user [targeting](#targeting), and [rollout traffic](#rollout-traffic).

[TO DO: ADD SCREENSHOT]

#### Details
Give your new feature flag a **Name** and **ID**. 
* The **Name** field allows you to provide a human-readable title for this feature flag that will be used by marketers and administrators. 
* The **ID** field will be called in your code to define the functionality that you want controlled by this feature flag.
* The **Description** field is an optional field that allows you to provide additional context around this feature flag.


{% alert important %} 
To prevent breaking production app behavior, feature flag `ID`s should be both unique and immutable. 

A feature flag `ID` is unique. The same `ID` is used across app groups so that different platforms (i.e., iOS/Android/Web) can share references to the same feature. Once set, the feature flag `ID` should not be changed.
{% endalert %}

Choose an `ID` thoughtfully as it will be used as you develop your feature. Practice good naming conventions to ensure that your code is readable by your colleagues (and your future self).

#### Properties
To update your app remotely, define variables as key/value pairs for your feature flag upon creation. These properties will be passed to your app through the Braze SDK. Defining properties is an optional step.

Variables can be **strings**, **boolean** values, or **numbers**. Define both the variable key and default value for each property.

For example:

[To do: Add example]

[Question: Is there any limit to the number of properties that can be added to a feature flag?]

#### Targeting
To target a particular [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) of users for your feature rollout, use the **Add Segment** dropdown menu.

If no segment is selected, the percentage of targeted users (see [Rollout Traffic](#rollout-traffic), below) will come from your entire user base. You can add multiple segments to target.

To filter users out of your target audience, use the **Add Filter** dropdown menu. You can add multiple filters to narrow your audience.

[Question: Is there any limit to the number of segments or filters that can be added to a feature flag?]

#### Rollout Traffic
Feature flags always start as disabled to allow you to separate the timing of the feature's release and activation in your users' experience. When you are ready to rollout your new feature, use the **Rollout Traffic** slider to randomly define a portion of your targeted user base to receive the new feature. Set the **Rollout Traffic** slider to set a percentage between 0% (no users) and 100% (the entire target audience). 

{% alert warning %} 
Do not set your rollout traffic above 0% until you are ready for your new feature to go live. When you initially define your feature flag in the dashboard, leave this setting at 0%.
{% endalert %}

### Check for the feature flag in your application
Once you have defined your feature flag, configure your app to check whether or not it is enabled for a particular user. When it is enabled, you'll set some action or reference the feature flag's variable properties based on your use case. 

Let's say you were to rolling out a new type of user profile for your app. You might set the `ID` as `expanded_user_profile`. Then, you would have your app check to see if it should display this new user profile to a particular user. For example:

[To do: Help with example code, please]
```javascript
const {value, properties} = braze.getFeature("expanded_user_profile");
if (value) {
  return <NewDesign />
} else {
  return <OldDesign />
}
Const height = expanded_user_profile.properties.height;
Const background = expanded_user_profile.properties.background;
}
```

The Braze SDK uses getter methods to pull your feature flag's properties into your app. It refreshes these properties during app start so that it displays the most up-to-date version of your feature. The SDK caches these values so your app can be used while offline. 

#### Refresh flags
You can set a flag to request a refresh if your rate limit/throttling allows.

```javascript
braze.refreshFeatureFlags(() => {
  // refresh is completed
})
```

#### Listen for changes
You can configure the SDK to listen and update your app if a refresh changes a flag's value.

```javascript
braze.subscribeToFeatureUpdates("new_design", ({value}) => {
  // new_design feature's value has changed
})
```

## Use cases
Feature flags let you turn a feature on and off in production without additional code deployment or app store updates. This allows you to safely roll out new features with confidence. 

Feature flags have a few different strategic uses, outlined below.

### Gradual rollouts
Feature flags allow you to gradually enable features to a sample population. For example, you can soft launch a new feature to your VIP users first. This strategy helps mitigate risks associated with shipping new features to everyone at once and helps catch bugs early. This also allows you to roll back feature enablement without requiring an additional code release.

For example, imagine that you have an ecommerce product that now comes in multiple colors and you want to implement a new color selector so users can specify which color to purchase.  

Without Feature Flags: We release this new feature and it goes live to the app stores. If there's a bug, users might not be able to make a purchase and we'll have to release a new version to the app store with a fix.

With Feature Flags: We release this new feature but only enable it for 5% of our users in Braze. If all goes well we gradually increase to 20%, 50%, and eventually 100%. If there's a bug we simply decrease down to 0% and examine what went wrong without losing additional revenue.

### Remotely control app variables 
Modify functionality on-the-fly. This is even more important for mobile apps, where updates can’t be rolled out as quickly to all users.
* Swap out content without waiting for an app store release
* Dynamically personalize content using Braze profile attributes

For example, change homepage links or banners on the fly

### Message coordination 
With Braze-powered Feature Flags, customers could coordinate feature rollout and messaging through Canvas. Braze will be the source of truth for the customer experience and its relevant messaging. * Send messaging to users testing out a new feature
* Understand the impact of a feature rollout on conversions
* Automatically optimize conversions with Experiment Paths


### Feature experimentation
Experimenting with feature flags lets you confirm a hypothesis around a new feature. By splitting traffic into two or more groups, you can compare the impact of a feature flag across groups, and determine the best course of action based on the results.

Example: Our E-commerce team has a new product checkout page design that we believe will improve purchase conversion rates.

Without Feature Flags: We release the new checkout page, and if next month's revenue is lower, we have to release a new app version to revert the changes, which can take 1-2 weeks.

With Feature Flags: We show the new checkout page to 50% of users and make a decision in 1 month to either enable it to 100% or turn it completely off and revisit the designs. In either case we won't risk a poor experience for 50% of our users.