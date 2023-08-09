---
nav_title: About Feature Flags
article_title: About Feature Flags
page_order: 1
description: "This reference article covers an overview of feature flags including prerequisites and use cases."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# About feature flags

> Feature flags allow you to remotely enable or disable functionality for a specific or random selection of users. Importantly, they let you turn a feature on and off in production without additional code deployment or app store updates. This allows you to safely roll out new features with confidence. 

Looking for steps on how to create a feature flag in Braze? Refer to [Creating feature flags][3].

{% alert important %} 
Feature flags are currently in beta. [Click here](https://dashboard.braze.com/engagement/feature_flags) to learn more about joining the beta program.
{% endalert %}

## Prerequisites

To use feature flags, ensure your SDKs are up to date with at least these minimum versions:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

## Use cases
Feature flags have a few different strategic uses, outlined below. To learn how you would implement these example use cases, see the [feature flag use cases][2] article.

### Gradual rollouts
Use feature flags to gradually enable features to a sample population. For example, you can soft launch a new feature to your VIP users first. This strategy helps mitigate risks associated with shipping new features to everyone at once and helps catch bugs early. 

![Moving image of rollout traffic slider going from 0% to 100%.][1]

For example, let's say we've decided to add a new "Live Chat Support" link to our app for faster customer service. We could release this feature to all customers at once. However, a wide release carries risks, such as: 

* Our Support team is still in training, and customers will be able to start support tickets after it's released. This doesn't give us any wiggle room in case the Support team needs more time.
* We're unsure of the actual volume of new support cases we'll get, so we might not be staffed appropriately.
* If our Support team is overwhelmed, we have no strategy to quickly to turn this feature off again.
* There might be bugs introduced in the chat widget and we don't want customers to have a negative experience.

With Braze feature flags, we can instead gradually roll out the feature and mitigate all of these risk:

* We will turn on the "Live Chat Support" feature when the Support team says they're ready.
* We will enable this new feature for only 10% of users to determine if we're staffed appropriately.
* If there are any bugs, we can quickly disable the feature instead of rushing to ship a new release.

To gradually roll out this feature, we create a new feature flag called `enable_live_chat` in the Braze dashboard.

![Feature flag called "enable_live_chat"][7]

In our app code, we will only show the **Start Live Chat** button when the Braze feature flag is enabled:

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

### Remotely control app variables 
Use feature flags to modify your app's functionality in production. This can be particularly important for mobile apps, where app store approvals prevent rolling out changes quickly to all users.

For example, let's say that our marketing team wants to list our current sales and promotions in our app's navigation. Normally, our engineers require one week lead time for any changes and three days for an app store review. But with Thanksgiving, Black Friday, Cyber Monday, Hanukah, Christmas, and New Years all within a two month period, we won't be able to make these tight deadlines .

With feature flags, we can let Braze power the content of our app navigation link, letting our marketing manager make changes in minutes rather than days.

To remotely configure this feature, we'll create a new feature flag called `navigation_promo_link` and define the following initial properties:

![Feature flag showing "link" and "text" properties pointing to a generic sales page][1]

In our app, we'll use Braze's getter methods to retrieve this feature flag's properties and build the navigation links based on those values:

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

Now, the day before Thanksgiving, all we have to do is change those property values in the Braze dashboard:

![Feature flag showing "link" and "text" properties pointing to a Thanksgiving sales page][2]

As a result, the next time someone loads the app they will see the new Thanksgiving deals.

### Message coordination

Use feature flags to synchronize a feature's rollout and messaging. This will allow you to use Braze as the source of truth for both your user experience and its relevant messaging. To achieve this, target the new feature to a particular segment or filtered portion of your audience. Then, create a campaign or Canvas that only targets that segment. 

Let's say that we're launching a new loyalty rewards program for our users. It can be difficult for Marketing and Product teams to perfectly coordinate the timing of promotional messaging with a feature's rollout. Feature flags in Canvas let you apply sophisticated logic when it comes to enabling a feature for a select audience, and controlling the related messaging to those same users.

To effectively coordinate feature rollout and messaging, we'll create a new feature flag called `show_loyalty_program`. For our initial phased release, we'll let Canvas control when and for whom the feature flag is enabled. For now, we'll leave the rollout percentage at 0% and not select any target segments.

![A feature flag named "show_loyalty_program"][3]

Then, in Canvas Flow, we'll create a Canvas Feature Flag step that enables the `show_loyalty_program` feature flag for our "High Value Customers" segment:

![Canvas flow showing an audience split where "high value customers" enable a "show_loyalty_program" feature flag][4]

Now, users in this segment will start to see the new loyalty program, and after it's enabled, an email and survey will automatically be sent out to help our team gather feedback.

### Feature experimentation

Use feature flags to experiment and confirm your hypotheses around your new feature. By splitting traffic into two or more groups, you can compare the impact of a feature flag across groups, and determine the best course of action based on the results.

An A/B test is a powerful tool that compares users' responses to multiple versions of a variable.

In this example, our team has built a new checkout flow for our e-commerce app. Even though we're confident it's an improvement the user experience, we want to run an A/B test to measure its impact on our app's revenue.

To begin, we'll create a new feature flag called `enable_checkout_v2`. We won't add an audience or rollout percentage. Instead, we'll use Canvas to split traffic, enable the feature, and measure the outcome.

In our app, we'll check if the feature flag is enabled or not and swap out the checkout flow based on the response:

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
if (featureFlag.enabled) {
  return <NewCheckoutFlow />
} else {
  return <OldCheckoutFlow />
}
```

In Canvas, we'll use an [Experiment Path][5] step and a Feature Flag step to set up our A/B test.

Now, 50% of users will see the old experience, while the other 50% see the new experience. We can then analyze the two steps to determine which checkout flow resulted in a higher conversion rate.

![Canvas with an experiment path splitting traffic into two 50% groups][6]{: height="55%" width="55%"}

Once we determine our winner, we can stop this Canvas and increase the rollout percentage on the feature flag to 100% for all users while our engineering team hard-codes this into our next app release.

[1]: {% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %} 
[2]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/use_cases/
[3]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/
[4]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step
[6]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-experiment-step.png %}
[7]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %}
[8]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/
[9]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %}
[10]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %}
[11]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %}