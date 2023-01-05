---
nav_title: About Feature Flags
article_title: About Feature Flags
hidden: true
permalink: "/about_feature_flags/"
page_order: 3
description: "Learn how to coordinate new feature rollouts with Braze feature flags."
platform:
  - iOS
  - Android
  - Web
---

# About feature flags

> This reference article covers the basics of feature flags and why you would use them in Braze. Looking for steps on how to create a feature flag in Braze? Refer to [Creating feature flags]({{site.baseurl}}/creating_feature_flags).

Feature flags allow a developer to remotely enable or disable functionality for a specific or random selection of users. Importantly, they let you turn a feature on and off in production without additional code deployment or app store updates. This allows you to safely roll out new features with confidence. 

Create a new feature flag within the Braze dashboard by providing a name and an `ID`, a target audience, and a percentage of users for whom to enable to this feature. Then, using that same `ID` in your app or website's code, your engineering team can conditionally run certain parts of your business logic.

For example, if your team has built a new profile page for your ride-sharing app, instead of releasing it (and potential bugs) to your entire user base, you can roll out the new profile page to just 5% of all users as a way to mitigate risk. 

{% alert important %} 
Feature flags are currently in beta. Contact your Braze account manager if you’re interested in participating in the early access. 
{% endalert %}

## Prerequisites

To use feature flags, ensure your SDKs are up to date with at least these minimum versions:
<!-- TODO -->
{% sdk_min_versions android:9999 web:4.4.0 swift:9999 %}

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