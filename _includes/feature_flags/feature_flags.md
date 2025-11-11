# Feature flags

> Feature flags allow you to remotely enable or disable functionality for a specific or random selection of users. Importantly, they let you turn a feature on and off in production without additional code deployment or app store updates. This allows you to safely roll out new features with confidence.

{% alert tip %}
When you're ready to create your own feature flags, check out [Creating feature flags]({{site.baseurl}}/developer_guide/feature_flags/create/).
{% endalert %}

## Prerequisites

These are the minimum SDK versions needed to start using feature flags:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## Use cases

### Gradual rollouts

Use feature flags to gradually enable features to a sample population. For example, you can soft launch a new feature to your VIP users first. This strategy helps mitigate risks associated with shipping new features to everyone at once and helps catch bugs early.

![Moving image of rollout traffic slider going from 0% to 100%.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %})

For example, let's say we've decided to add a new "Live Chat Support" link to our app for faster customer service. We could release this feature to all customers at once. However, a wide release carries risks, such as: 

* Our Support team is still in training, and customers can start support tickets after it's released. This doesn't give us any leeway in case the Support team needs more time.
* We're unsure of the actual volume of new support cases we'll get, so we might not be staffed appropriately.
* If our Support team is overwhelmed, we have no strategy to quickly turn this feature off again.
* There might be bugs introduced in the chat widget, and we don't want customers to have a negative experience.

With Braze feature flags, we can instead gradually roll out the feature and mitigate all of these risks:

* We will turn on the "Live Chat Support" feature when the Support team says they're ready.
* We will enable this new feature for only 10% of users to determine if we're staffed appropriately.
* If there are any bugs, we can quickly disable the feature instead of rushing to ship a new release.

To gradually roll out this feature, we can [create a feature flag]({{site.baseurl}}/developer_guide/feature_flags/create/) named "Live Chat Widget."

![Feature flag details for an example named Live Chat Widget. The ID is enable_live_chat. This feature flag description reads that the live chat widget will show on the support page.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %})

In our app code, we will only show the **Start Live Chat** button when the Braze feature flag is enabled:

{% tabs %}
{% tab JavaScript %}

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// Get the initial value from the Braze SDK
const featureFlag = braze.getFeatureFlag("enable_live_chat");
const [liveChatEnabled, setLiveChatEnabled] = useState(featureFlag.enabled);

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(() => {
    const newValue = braze.getFeatureFlag("enable_live_chat").enabled;
    setLiveChatEnabled(newValue);
});

// Only show the Live Chat if the Braze SDK determines it is enabled
return (<>
  Need help? <button>Email Our Team</button>
  {liveChatEnabled && <button>Start Live Chat</button>}
</>)
```

{% endtab %}
{% tab Java %}

```java
// Get the initial value from the Braze SDK
FeatureFlag featureFlag = braze.getFeatureFlag("enable_live_chat");
Boolean liveChatEnabled = featureFlag != null && featureFlag.getEnabled();

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates(event -> {
  FeatureFlag newFeatureFlag = braze.getFeatureFlag("enable_live_chat");
  Boolean newValue = newFeatureFlag != null && newFeatureFlag.getEnabled();
  liveChatEnabled = newValue;
});

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Get the initial value from the Braze SDK
val featureFlag = braze.getFeatureFlag("enable_live_chat")
var liveChatEnabled = featureFlag?.enabled

// Listen for updates from the Braze SDK
braze.subscribeToFeatureFlagsUpdates() { event ->
  val newValue = braze.getFeatureFlag("enable_live_chat")?.enabled
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
if (liveChatEnabled) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}

```

{% endtab %}
{% tab Swift %}

```swift
// Get the initial value from the Braze SDK
let featureFlag = braze.featureFlags.featureFlag(id: "enable_live_chat")
var liveChatEnabled = featureFlag?.enabled ?? false

// Listen for updates from the Braze SDK
braze.featureFlags.subscribeToUpdates() { _ in  
  let newValue = braze.featureFlags.featureFlag(id: "enable_live_chat")?.enabled ?? false
  liveChatEnabled = newValue
}

// Only show the Live Chat view if the Braze SDK determines it is enabled
liveChatView.isHidden = !liveChatEnabled
```

{% endtab %}
{% endtabs %}

### Remotely control app variables

Use feature flags to modify your app's functionality in production. This can be particularly important for mobile apps, where app store approvals prevent rolling out changes quickly to all users.

For example, let's say that our marketing team wants to list our current sales and promotions in our app's navigation. Normally, our engineers require one week's lead time for any changes and three days for an app store review. But with Thanksgiving, Black Friday, Cyber Monday, Hanukkah, Christmas, and New Year's Day all within two months, we won't be able to meet these tight deadlines.

With feature flags, we can let Braze power the content of our app navigation link, letting our marketing manager make changes in minutes rather than days.

To remotely configure this feature, we'll create a new feature flag called `navigation_promo_link` and define the following initial properties:

![Feature flag with link and text properties directing to a generic sales page.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %})

In our app, we'll use getter methods by Braze to retrieve this feature flag's properties and build the navigation links based on those values:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// Check if the feature flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// Read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// Read the "text" property
const [promoText, setPromoText] = useState(featureFlag.getStringProperty("text"));

return (<>
  <div>
    <a href="/">Home</a>
    { promoEnabled && <a href={promoLink}>{promoText}</a> }
    <a href="/products">Products</a>
    <a href="/categories">Categories
  </div>
</>)
```

{% endtab %}
{% tab Java %}

```java
// liveChatView is the View container for the Live Chat UI
FeatureFlag featureFlag = braze.getFeatureFlag("navigation_promo_link");
if (featureFlag != null && featureFlag.getEnabled()) {
  liveChatView.setVisibility(View.VISIBLE);
} else {
  liveChatView.setVisibility(View.GONE);
}
liveChatView.setPromoLink(featureFlag.getStringProperty("link"));
liveChatView.setPromoText(featureFlag.getStringProperty("text"));

```

{% endtab %}
{% tab Kotlin %}

```kotlin
// liveChatView is the View container for the Live Chat UI
val featureFlag = braze.getFeatureFlag("navigation_promo_link")
if (featureFlag?.enabled == true) {
  liveChatView.visibility = View.VISIBLE
} else {
  liveChatView.visibility = View.GONE
}
liveChatView.promoLink = featureFlag?.getStringProperty("link")
liveChatView.promoText = featureFlag?.getStringProperty("text")
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "navigation_promo_link")
if let featureFlag {
  liveChatView.isHidden = !featureFlag.enabled
} else {
  liveChatView.isHidden = true
}
liveChatView.promoLink = featureFlag?.stringProperty("link")
liveChatView.promoText = featureFlag?.stringProperty("text")
```

{% endtab %}
{% endtabs %}

Now, the day before Thanksgiving, we only have to change those property values in the Braze dashboard.

![Feature flag with link and text properties directing to a Thanksgiving sales page.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %})

As a result, the next time someone loads the app, they will see the new Thanksgiving deals.

### Message coordination

Use feature flags to synchronize a feature's rollout and messaging. This will allow you to use Braze as the source of truth for both your user experience and its relevant messaging. To achieve this, target the new feature to a particular segment or filtered portion of your audience. Then, create a campaign or Canvas that only targets that segment. 

Let's say that we're launching a new loyalty rewards program for our users. It can be difficult for marketing and product teams to perfectly coordinate the timing of promotional messaging with a feature's rollout. Feature flags in Canvas let you apply sophisticated logic when it comes to enabling a feature for a select audience and controlling the related messaging to those same users.

To effectively coordinate feature rollout and messaging, we'll create a new feature flag called `show_loyalty_program`. For our initial phased release, we'll let Canvas control when and for whom the feature flag is enabled. For now, we'll leave the rollout percentage at 0% and not select any target segments.

![A feature flag with the name Loyalty Rewards Program. The ID is show_loyalty_program, and the description that this shows the new loyalty rewards program on the home screen and profile page.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %})

Then, in Canvas, we'll create a [Feature Flag step]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) that enables the `show_loyalty_program` feature flag for our "High Value Customers" segment:

![An example of a Canvas with an Audience Split step where the high-value customers segment turns on the show_loyalty_program feature flag.]({% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %})

Now, users in this segment will start to see the new loyalty program, and after it's enabled, an email and survey will be sent out automatically to help our team gather feedback.

### Feature experimentation

Use feature flags to experiment and confirm your hypotheses around your new feature. By splitting traffic into two or more groups, you can compare the impact of a feature flag across groups, and determine the best course of action based on the results.

An [A/B test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) is a powerful tool that compares users' responses to multiple versions of a variable.

In this example, our team has built a new checkout flow for our eCommerce app. Even though we're confident it's improving the user experience, we want to run an A/B test to measure its impact on our app's revenue.

To begin, we'll create a new feature flag called `enable_checkout_v2`. We won't add an audience or rollout percentage. Instead, we'll use a feature flag experiment to split traffic, enable the feature, and measure the outcome.

In our app, we'll check if the feature flag is enabled or not and swap out the checkout flow based on the response:

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag?.enabled) {
  return <NewCheckoutFlow />  
} else {
  return <OldCheckoutFlow />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("enable_checkout_v2");
braze.logFeatureFlagImpression("enable_checkout_v2");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewCheckoutFlow();
} else {
  return new OldCheckoutFlow();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("enable_checkout_v2")
braze.logFeatureFlagImpression("enable_checkout_v2")
if (featureFlag?.enabled == true) {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "enable_checkout_v2")
braze.featureFlags.logFeatureFlagImpression(id: "enable_checkout_v2")
if let featureFlag, featureFlag.enabled {
  return NewCheckoutFlow()
} else {
  return OldCheckoutFlow()
}
```

{% endtab %}
{% endtabs %}

We'll set up our A/B test in a [Feature Flag Experiment]({{site.baseurl}}/developer_guide/feature_flags/experiments/).

Now, 50% of users will see the old experience, while the other 50% will see the new experience. We can then analyze the two variants to determine which checkout flow resulted in a higher conversion rate. {% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

![A feature flag experiment splitting traffic into two 50 percent groups.]({% image_buster /assets/img/feature_flags/feature-flag-use-case-campaign-experiment.png %})

Once we determine our winner, we can stop this campaign and increase the rollout percentage on the feature flag to 100% for all users while our engineering team hard-codes this into our next app release.

### Segmentation

Use the **Feature Flag** filter to create a segment or target messaging at users based on whether they have a feature flag enabled. For example, let's say we have a feature flag that controls premium content in our app. We could create a segment that filters for users who don't have the feature flag enabled, and then send that segment a message urging them to upgrade their account to view premium content.

![]({% image_buster /assets/img/feature_flags/feature_flag_segmentation_filter.png %})

For more information about filtering on segments, see [Creating a segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

{% alert note %}
To prevent recursive segments, it is not possible to create a segment that references other feature flags.
{% endalert %}

## Plan limitations

These are the feature flag limitations for free and paid plans.

| Feature                                                                                                   | Free version     | Paid version      |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| [Active feature flags](#active-feature-flags)                                                                     | 10 per workspace | 110 per workspace |
| [Active campaign experiments]({{site.baseurl}}/developer_guide/feature_flags/experiments/)          | 1 per workspace  | 100 per workspace |
| [Feature Flag Canvas steps]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) | Unlimited        | Unlimited         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A feature flag is considered active and will count toward your limit if any of the following apply:

- Rollout is more than 0%
- Used in an active Canvas
- Used in an active experiment

Even if the same feature flag matches multiple criteria, such as if it's used in a Canvas and the rollout is 50%, it will only count as 1 active feature flag toward your limit.

{% alert note %}
To purchase the paid version of feature flags, contact your Braze account manager, or request an upgrade in the Braze dashboard.
{% endalert %}