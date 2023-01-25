---
nav_title: Example Use Cases
article_title: Example Use Cases
hidden: false
page_order: 2
description: "Learn about common Feature Flag use cases"
platform:
  - iOS
  - Android
  - Web
channel:
  - feature flags 
---

# Example Use Cases

## Gradual Rollouts

In this example, we have decided to add a new "Live Chat Support" link to our app for faster customer service.

Normally we would release this to all customers at once, but that would be risky:

1. Our support team is still in training, and customers will be able to start support tickets once it's released. This doesn't give us any wiggle room in case the support team needs more time.
2. If our support team is overwhelmed, we can't quickly roll this back.
3. We are unsure of the volume of support cases we will get, so we might not be staffed appropriately.
4. There might be bugs introduced in the chat widget and we don't want customers to negatively rate our app as a result.

With Braze Feature Flags we can now gradually roll out the feature and mitigate all of these risk:

1. We will turn the "Live Chat Support" feature on at our leisure, only when the support team tells us they're ready.
2. We will enable this new feature for only 10% of users to determine if we're staffed appropriately.
3. If there are any bugs, we can quickly disable the feature instead of rushing to ship a new release.

In the Braze dashboard, all we have to do is create a new feature flag called `enable_live_chat`.

![Feature flag called "enable_live_chat"][7]

In our app code we will only show the Live Chat button when the Braze feature flag is enabled:

```javascript
import {useState} from "react";
import * as braze from "@braze/web-sdk";

// get the initial value from the Braze SDK
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

## Remote Configuration

In this example, our marketing team likes to put the latest sales as a link in our app's navigation. Normally, our engineers require 1 week lead time for any changes + 3 days for an app store review. 

But with Thanksgiving, Black Friday, Cyber Monday, Hannukah, Christmas, and New Years all within a 2 month period, we won't be able to meet these deadlines.

With Braze feature flags, we can now let Braze power the content of our app navigation link which lets our marketing manager make changes in minutes, rather than days.

In the Braze dashboard we will create a new Feature Flag called `navigation_promo_link`, and define the following initial properties:

![Feature flag showing "link" and "text" properties pointing to a generic sales page][1]

In our app, we read from Braze when building the navigation links:

```javascript
import * as braze from "@braze/web-sdk";
import {useState} from "react";

const featureFlag = braze.getFeatureFlag("navigation_promo_link");
// check if the Feature Flag is enabled
const [promoEnabled, setPromoEnabled] = useState(featureFlag.enabled);
// read the "link" property
const [promoLink, setPromoLink] = useState(featureFlag.getStringProperty("link"));
// read the "text" property
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

Now, the day before thanksgiving, all we have to do is change those property values in the Braze dashboard:

![Feature flag showing "link" and "text" properties pointing to a thanksgiving sales page][2]

As a result, the next time someone loads the app they will see the new Thanksgiving deals.


## Messaging Coordination

{% alert important %} 
This functionality is not yet supported in beta.
{% endalert %}

When marketing and product teams don't coordinate product launches it can be difficult to coordinate the timing of promotional messaging with a feature's rollout.

Feature Flags in Canvas let you apply the same sophisticated journey logic when it comes to enabling a feature for a select audience, and controlling any related messaging to those same users.

In this example, we are launching a new loyalty rewards program to customers. In our initial phased release, we will use a feature flag to only enable the loyalty program to our "high-value customers" segment.

![A feature flag named "show_loyalty_program"][3]

Rather than adjusting the rollout percentage, we will use a Canvas Feature Flag step to control when and who this feature is enabled for:

![Canvas flow showing an audience split where "high value customers" enable a "show_loyalty_program" feature flag][4]

Now, users in this segment will start to see the new loyalty program, and once it has been enabled, an email and survey will automatically be sent out to help our team gather feedback.


## Experimentation

{% alert important %} 
This functionality is not yet supported in beta.
{% endalert %}

A/B testing is a powerful strategy used to measure the impact to a metric when introducing a change.

In this example, our team has built a new checkout flow for our e-commerce app. Even though we're confident it's an improvement the user experience, we will run an a/b test to measure its impact on our app's revenue.

To begin, we'll create a new Feature Flag called "enable_checkout_v2". We won't add any audience or rollout percentage since we will once again use Canvas to split traffic, enable the feature, and measure the outcome.

In our app, we'll simply swap out the checkout flow component based on the Braze Feature Flag enabled status:

```javascript
import * as braze from "@braze/web-sdk";

const featureFlag = braze.getFeatureFlag("enable_checkout_v2");
if (featureFlag.enabled) {
  return <NewCheckoutFlow />
} else {
  return <OldCheckoutFlow />
}
```

In Canvas, we'll use an [Experiment Path][5], along side the Feature Flag Step to set up our a/b test.

Now, 50% of users will see the old experience, while the other 50% see the new experience. We can then analyze the two steps to determine which checkout flow resulted in a higher conversion rate.

![Canvas with an Experiment Path splitting traffic into two 50% groups][6]

Once we determine our winner, we can stop this Canvas, and increase the Rollout Percentage on the feature flag to 100% for all users while our engineering team hard-codes this into our next app release.

[1]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-1.png %}
[2]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-navigation-link-2.png %}
[3]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-loyalty.png %}
[4]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-flow.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step
[6]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-canvas-experiment-step.png %}
[7]: {% image_buster /assets/img/feature_flags/feature-flags-use-case-livechat-1.png %}
