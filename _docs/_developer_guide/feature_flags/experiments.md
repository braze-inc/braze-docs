---
nav_title: Feature Flag Experiments
article_title: Feature Flag Experiments
page_order: 40
description: "Feature flag experiments let you A/B test changes to your applications to optimize conversion rates."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Feature flag experiments

> Feature flag experiments let you A/B test changes to your applications to optimize conversion rates. Marketers can use feature flags to determine whether a new feature positively or negatively impacts conversion rates, or which set of feature flag properties is most optimal.

## Prerequisites

Before you can track user data in the experiment, your app needs to record when a user interacts with a feature flag. This is called a feature flag impression. Make sure to log a feature flag impression whenever a user sees or could have seen the feature you're testing, even if they're in the control group.

To learn more about logging feature flag impressions, see [Creating feature flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions).

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}

```

## Creating a feature flag experiment

### Step 1: Create an experiment

1. Go to **Messaging** > **Campaigns**, then select **+ Create Campaign**.
2. Select **Feature Flag Experiment**.
3. Give your campaign a clear and meaningful name.

### Step 2: Add experiment variants

Next, create variations. For each variant, choose the feature flag you want to turn on or off, then review its assigned properties.

To test the impact of your feature, use variants to split traffic into two or more groups. Name one group "My control group" and turn its feature flags off.

### Step 3: Overwrite properties (optional)

You can choose to overwrite the default properties you initially set up for users who receive a specific campaign variant.

To edit, add, or remove additional default properties, edit the feature flag itself from **Messaging** > **Feature Flags**. When a variant is disabled, the SDK will return an empty properties object for the given feature flag.

![]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### Step 4: Choose users to target

Use one of your segments or filters to choose your [target users]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/). For example, you can use the **Received Feature Flag Variant** filter to retarget users who have already received an A/B test.

![The 'Target' page in a feature flag experiment with 'Received Feature Flag Variant' highlighted in the filter group search bar.]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
Segment membership is calculated when feature flags are refreshed for a given user. Changes are made available after your app refreshes feature flags, or when a new session is started.
{% endalert %}

### Step 5: Distribute variants

Choose the percentage distribution for your experiment. As a best practice, you should not change the distribution after your experiment has been launched.

### Step 6: Assign conversions

Braze lets you to track how often users perform specific actions, [conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), after receiving a campaign. Specify up to a 30-day window during which a conversion will be counted if the user takes the specified action.

### Step 7: Review and launch

After you’ve finished building the last of your experiment, review its details, then select **Launch Experiment**.
