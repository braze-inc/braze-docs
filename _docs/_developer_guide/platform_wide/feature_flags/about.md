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

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 roku:0.2.0 %}

## Use cases
Feature flags have a few different strategic uses, outlined below. To learn how you would implement these example use cases, see the [feature flag use cases][2] article.

### Gradual rollouts
Use feature flags to gradually enable features to a sample population. For example, you can soft launch a new feature to your VIP users first. This strategy helps mitigate risks associated with shipping new features to everyone at once and helps catch bugs early. 

![Moving image of rollout traffic slider going from 0% to 100%.][1]

For example, imagine that you have an ecommerce product that now comes in multiple colors and you want to implement a new color selector so users can specify which color to purchase. You can release this new feature but only enable it for 5% of your users in Braze. If all goes well, you can gradually increase to 20%, 50%, and eventually 100%. If a critical bug is discovered, you can roll back feature enablement to 0% without requiring an additional code release. 

### Remotely control app variables 
Use feature flags to modify your app's functionality in production. This can be particularly important for mobile apps, where app store approvals prevent rolling out changes quickly to all users.

For example, you can use a feature flag's property values to quickly change your app's homepage links or text. You can even dynamically personalize this content using Braze profile attributes.

### Message coordination

Use feature flags to synchronize a feature's rollout and messaging. This will allow you to use Braze as the source of truth for both your user experience and its relevant messaging. To achieve this, target the new feature to a particular segment or filtered portion of your audience. Then, create a Campaign or Canvas that only targets that segment. 

### Feature experimentation

Use feature flags to experiment and confirm your hypotheses around your new feature. By splitting traffic into two or more groups, you can compare the impact of a feature flag across groups, and determine the best course of action based on the results.

With Canvas, you can track the impact of feature rollout on conversations. And, using [Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths), you can optimize these conversions by testing different messages or paths against each other and determining which is most effective. Use the Winning Path as you progressively rollout your feature to a wider audience.

<!-- For example, imagine that your ecommerce team has a new checkout page design that they believe will improve purchase conversion rates. When you release this feature, you can display the new page to 50% of your users for one month. If it performs better than the old design, you can increase the rollout traffic to 100%. If it performs poorly, you can turn it off completely and revisit the designs. In either case, you have avoided a poor experience for 50% of your users. -->

[1]: {% image_buster /assets/img/feature_flags/feature-flags-rollout.gif %} 
[2]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/use_cases/
[3]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/
