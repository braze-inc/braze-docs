---
nav_title: Feature Flags
article_title: Feature Flags
hidden: true
permalink: "/feature_flags/"
page_order: 3
description: "Learn how to coordinate new feature rollouts with Braze feature flags."
platform:
  - iOS
  - Android
  - Web
---

# Feature flags

Feature flags allow you to remotely enable or disable functionality for a specific or random selection of users. Importantly, they let you turn a feature on and off in production without additional code deployment or app store updates. This allows you to safely roll out new features with confidence. 

Create a new feature flag within the Braze dashboard by providing a name and an `ID`, a target audience, and a percentage of users for whom to enable to this feature. Then, using that same `ID` in your app or website's code, you can conditionally run certain parts of your business logic.

For example, if you've built a new profile page for your ride-sharing app, instead of releasing it (and potential bugs) to your entire user base, you can roll out the new profile page to just 5% of all users as a way to mitigate risk. 

{% alert important %} 
Feature flags are currently in beta. Contact your Braze account manager if you’re interested in participating in the early access. 
{% endalert %}

## Prerequisites

To use feature flags, ensure your SDKs are up to date with at least these minimum versions:
<!-- TODO -->
{% sdk_min_versions android:9999 web:4.4.0 swift:9999 %}

## Implementation
Create, edit, and archive feature flags from the **Feature Flags** page, located under **Engagement**. This page displays a list of existing feature flags for this app group.

![A list of previously created feature flags on the Braze dashboard][1]

### Create a new feature flag
To create a new feature flag, click **Create Feature Flag**. Then, define your feature flag's [details](#details), [properties](#properties), user [targeting](#targeting), and [rollout traffic](#rollout-traffic).

![A blank feature flag form][2]

#### Details
Give your new feature flag a **Name** and **ID**. 
* The **Name** field allows you to provide a human-readable title for this feature flag that will be used by marketers and administrators. 
* The **ID** field will be referenced in your code to determine whether the feature is enabled for a particular user. This must be unique and cannot be modified once created.
* The **Description** field is an optional field that allows you to provide additional context around this feature flag.


{% alert important %} 
To prevent breaking production app behavior, feature flag `ID`s must be unique and cannot be modified once created. 

Feature flags are shared across apps within an app group so that different platforms (i.e., iOS/Android/Web) can share references to the same feature.
{% endalert %}

Choose an `ID` thoughtfully as it will be used as you develop your feature. Practice good naming conventions to ensure that your code is readable by your colleagues (and your future self).

For example, it's common to use a naming convention of `{verb}_{product}_{feature}`, such as `enable_rider_new_profile_page` to make it clear what enabling the feature flag does.

#### Properties
Custom properties can be defined as part of your feature flag. These properties will be accessible by your app through the Braze SDK when the feature is enabled. Defining properties is an optional step.

Variables can be **strings**, **boolean** values, or **numbers**. Define both the variable key and default value for each property.

##### Example properties
For example, if we are defining a feature flag that shows an out-of-stock banner for our e-commerce store, we might set the following properties, which our app will use when displaying the banner:

|:Property Name|Type|Value|
|--|--|--|
|`banner_height`|`number`|`75`|
|`banner_color`|`string`|`blue`|
|`banner_text`|`string`|`Widgets are out of stock until July 1.`|
|`dismissible`|`boolean`|`false`|

{% alert tip %}
There is no limit to the number of properties you can add, though a feature flag's properties are limited to 10kB in total.
{% endalert %}

#### Targeting
To being the rollout of a feature flag, you must choose a particular [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) of users.


To filter users out of your target audience, use the **Add Filter** dropdown menu. You can add multiple filters to narrow your audience.

#### Rollout Traffic
Feature flags always start as disabled to allow you to separate the timing of the feature's release and activation in your users' experience. 

When you are ready to rollout your new feature, specify an audience and then use the **Rollout Traffic** slider to define the random percentage of your targeted user base to receive the new feature. Set the **Rollout Traffic** slider to set a percentage between 0% (no users) and 100% (the entire target audience). 

{% alert warning %} 
Do not set your rollout traffic above 0% until you are ready for your new feature to go live. When you initially define your feature flag in the dashboard, leave this setting at 0%.
{% endalert %}

### Check for the feature flag in your application
Once you have defined your feature flag, configure your app to check whether or not it is enabled for a particular user. When it is enabled, you'll set some action or reference the feature flag's variable properties based on your use case. 

Let's say you were to rolling out a new type of user profile for your app. You might set the `ID` as `expanded_user_profile`. Then, you would have your app check to see if it should display this new user profile to a particular user. For example:

{% tabs %}
{% tab Javascript %}
```javascript
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (feature.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```
{% endtab %}
{% tab Swift %}
```swift
todo copy example from web
```
{% endtab %}
{% tab Java %}
```java
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag.getEnabled()) {
  Log.i(TAG, "expanded_user_profile is enabled", featureFlag.getProperties());
} else {
  Log.i(TAG, "expanded_user_profile is not enabled");
}
```
{% endtab %}
{% tab Kotlin %}
```kotlin
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag.enabled) {
  Log.i(TAG, "expanded_user_profile is enabled. ${featureFlag.properties}")
} else {
  Log.i(TAG, "expanded_user_profile is not enabled.")
}
```
{% endtab %}
{% endtabs %}

The Braze SDK provides getter methods to pull your feature flag's enabled/disabled status and its properties into your app. Feature flags are refreshed automatically at session start so that you can display the most up-to-date version of your feature upon launch. The SDK caches these values so they can be used while offline. 

You can also get a list of all enabled feature flags:

{% tabs %}
{% tab Javascript %}
```javascript
const features = getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```
{% endtab %}
{% tab Swift %}
```swift
todo copy example from web
```
{% endtab %}
{% tab Java %}
```java
List<FeatureFlag> features = braze.getAllFeatureFlags();
for (FeatureFlag feature: features) {
  Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
}
```
{% endtab %}
{% tab Kotlin %}
```kotlin
val featureFlags = braze.getAllFeatureFlags()
featureFlags.forEach { feature ->
  Log.i(TAG, "Feature: ${feature.id} ${feature.enabled}")
}
```
{% endtab %}
{% endtabs %}

#### Refresh feature flags
You can refresh the current user's feature flags mid-session to pull the latest values from Braze.

{% alert tip %}
Refreshing happens automatically upon session start. Manually refreshing may be throttled by Braze. Please ensure you refresh only prior to important user actions or pages, such as before loading a checkout page, or if you know a feature flag will be consumed.
{% endalert %}

{% tabs %}
{% tab Javascript %}
```javascript
braze.refreshFeatureFlags(() => {
  console.log(`Feature flags have been refreshed.`);
}, () => {
  console.log(`Failed to refresh feature flags.);
});
```
{% endtab %}
{% tab Swift %}
```swift
todo copy example from web
```
{% endtab %}
{% tab Java %}
```java
braze.refreshFeatureFlags();
```
{% endtab %}
{% tab Kotlin %}
```kotlin
braze.refreshFeatureFlags()
```
{% endtab %}
{% endtabs %}


#### Listen for changes
You can configure the Braze SDK to listen and update your app when feature flags have been refreshed.

This is useful if you want to update your app if a user is no longer eligible for a feature. For example, setting some state in your app based on whether or not a feature is enabled, or one of its property values.

{% tabs %}
{% tab Javascript %}
```javascript
// register an event listener
const subscriptionId = braze.subscribeToFeatureFlagsUpdates((features) => {
  console.log(`Features were updated`, features);
});
// unregister this event listener
braze.removeSubscription(subscriptionId);
```
{% endtab %}
{% tab Swift %}
```swift
todo copy example from web
```
{% endtab %}
{% tab Java %}
```java
braze.subscribeToFeatureFlagsUpdates(event -> {
  Log.i(TAG, "Feature flags were updated.");
  for (FeatureFlag feature: event.getFeatureFlags()) {
    Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled(), feature.getProperties());
  }
});
```
{% endtab %}
{% tab Kotlin %}
```kotlin
braze.subscribeToFeatureFlagsUpdates() { event ->
  Log.i(TAG, "Feature flags were updated.")
  event.featureFlags.forEach { feature ->
    Log.i(TAG, "Feature: ${feature.id}")
  }
}
```
{% endtab %}
{% endtabs %}

## Use cases
Feature flags have a few different strategic uses, outlined below.

### Gradual rollouts
Use feature flags to gradually enable features to a sample population. For example, you can soft launch a new feature to your VIP users first. This strategy helps mitigate risks associated with shipping new features to everyone at once and helps catch bugs early. 

For example, imagine that you have an ecommerce product that now comes in multiple colors and you want to implement a new color selector so users can specify which color to purchase. You can release this new feature but only enable it for 5% of your users in Braze. If all goes well, you can gradually increase to 20%, 50%, and eventually 100%. If a critical bug is discovered, you can roll back feature enablement to 0% without requiring an additional code release. 

### Remotely control app variables 
Use feature flags to modify your app's functionality on-the-fly. This can be particularly important for mobile apps, where updates can’t be rolled out as quickly to all users.

For example, you can change homepage links or banners on the fly using a feature flag's property values. You can even dynamically personalize this content using Braze profile attributes.

<!-- TODO -->
<!-- [David: Can you provide some examples of how they would do this?] -->

### Message coordination
{% alert important %} 
This functionality is not supported in beta.
{% endalert %}

Use feature flags to coordinate feature rollout and messaging simultaneously. This will allow you to use Braze as the source of truth for both your user experience and its relevant messaging. To achieve this, target the new feature to a particular segment or filtered portion of your audience. Then, create a Campaign or Canvas that only targets that segment. 

### Feature experimentation
{% alert important %} 
This functionality is not supported in beta.
{% endalert %}

Use feature flags to experiment and confirm your hypotheses around your new feature. By splitting traffic into two or more groups, you can compare the impact of a feature flag across groups, and determine the best course of action based on the results.

With Canvas, you can track the impact of feature rollout on conversations. And, using [Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths), you can optimize these conversions by testing different messages or paths against each other and determining which is most effective. Use the Winning Path as you progressively rollout your feature to a wider audience.

For example, imagine that your ecommerce team has a new checkout page design that they believe will improve purchase conversion rates. When you release this feature, you can display the new page to 50% of your users for one month. If it performs better than the old design, you can increase the rollout traffic to 100%. If it performs poorly, you can turn it off completely and revisit the designs. In either case, you have avoided a poor experience for 50% of your users.

[1]: {% image_buster /assets/img_archive/Feature-Flag-1.png %} 
[2]: {% image_buster /assets/img_archive/Feature-Flag-2.png %}