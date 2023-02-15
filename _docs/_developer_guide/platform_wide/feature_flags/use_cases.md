---
nav_title: Example Use Cases
article_title: Example Use Cases
page_order: 3
description: "Learn about common feature flag use cases"
platform:
  - iOS
  - Android
  - Web
channel:
  - feature flags 
---

# Example use cases

> This article describes specific examples of using feature flags to improve your user experience. Looking for steps on how to create a feature flag in Braze? Refer to [Creating feature flags][8].

{% alert important %} 
Feature flags are currently in beta. Contact your Braze account manager if you're interested in participating in the early access. 
{% endalert %}

## Gradual rollouts

For this example, let's say we've decided to add a new "Live Chat Support" link to our app for faster customer service. We could release this feature to all customers at once. However, a wide release carries risks, such as: 

* Our Support team is still in training, and customers will be able to start support tickets once it's released. This doesn't give us any wiggle room in case the Support team needs more time.
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

## Remote configuration

Let's say that our Marketing team wants to list our current sales and promotions in our app's navigation. Normally, our engineers require one week lead time for any changes and three days for an app store review. But with Thanksgiving, Black Friday, Cyber Monday, Hanukah, Christmas, and New Years all within a two month period, we won't be able to make these tight deadlines .

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


## Messaging coordination

{% alert important %} 
This functionality is not yet supported in beta.
{% endalert %}

Let's say that we're launching a new loyalty rewards program for our end users. It can be difficult for Marketing and Product teams to perfectly coordinate the timing of promotional messaging with a feature's rollout. Feature flags in Canvas let you apply sophisticated logic when it comes to enabling a feature for a select audience, and controlling the related messaging to those same users.

To effectively coordinate feature rollout and messaging, we'll create a new feature flag called `show_loyalty_program`. For our initial phased release, we'll let Canvas control when and for whom the feature flag is enabled. For now, we'll leave the rollout percentage at 0% and not select any target segments.

![A feature flag named "show_loyalty_program"][3]

Then, in Canvas Flow, we'll create a Canvas Feature Flag step that enables the `show_loyalty_program` feature flag for our "High Value Customers" segment:

![Canvas flow showing an audience split where "high value customers" enable a "show_loyalty_program" feature flag][4]

Now, users in this segment will start to see the new loyalty program, and once it has been enabled, an email and survey will automatically be sent out to help our team gather feedback.


## Experimentation

{% alert important %} 
This functionality is not yet supported in beta.
{% endalert %}

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

In Canvas, we'll use an [Experiment Path][5] and a Feature Flag step to set up our A/B test.

Now, 50% of users will see the old experience, while the other 50% see the new experience. We can then analyze the two steps to determine which checkout flow resulted in a higher conversion rate.

![Canvas with an Experiment Path splitting traffic into two 50% groups][6]

Once we determine our winner, we can stop this Canvas, and increase the rollout percentage on the feature flag to 100% for all users while our engineering team hard-codes this into our next app release.

[1]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %}
[2]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %}
[3]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %}
[4]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step
[6]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-experiment-step.png %}
[7]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %}
[8]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/
