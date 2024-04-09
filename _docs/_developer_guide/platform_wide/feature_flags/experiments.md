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

# Creating a feature flag experiment

> Feature flag experiments let you A/B test changes to your applications to optimize conversion rates. Marketers can use feature flags to determine whether a new feature positively or negatively impacts conversion rates, or which set of feature flag properties is most optimal.

## Prerequisites

Before you can track user data in the experiment, your app needs to record when a user interacts with a feature flag. This is called a feature flag impression. Make sure to log a feature flag impression whenever a user sees or could have seen the feature you're testing, even if they're in the control group.

To learn more about logging feature flag impressions, see [Creating feature flags][6].

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}

```

## Step 1: Create an experiment

1. Go to **Messaging** > **Campaigns** and click **+ Create Campaign**.
2. Select **Feature Flag Experiment**.
3. Name your campaign something clear and meaningful.

## Step 2: Add experiment variants

Next, create variations. For each variant, choose the feature flag you want to turn on or off and review the assigned properties.

To test the impact of your feature, use variants to split traffic into two or more groups. Name one group "My control group" and turn its feature flags off.

### Overwriting properties

Though you specified default properties when you originally set up your feature flag, you can choose to overwrite those values for users who receive a specific campaign variant.

![][image1]{: style="max-width:80%"}

To edit, add, or remove additional default properties, edit the feature flag itself from **Messaging** > **Feature Flags**.

## Step 3: Choose users to target

Next, you need to [target users][4] by choosing segments or filters to narrow down your audience. Segment membership is calculated when feature flags are refreshed for a given user.

{% alert note %}
Your target audience will be eligible for the feature flag as soon as you save a rollout greater than 0%. Changes are made available once your app refreshes feature flags, or when a new session is started.
{% endalert %}

## Step 4: Distribute variants

Choose the percentage distribution for your experiment. As a best practice, you should not change the distribution once your experiment has been launched.

## Step 5: Assign conversions

Braze lets you to track how often users perform specific actions, [conversion events][5], after receiving a campaign. Specify up to a 30-day window during which a conversion will be counted if the user takes the specified action.

## Step 6: Review and launch

After you’ve finished building the last of your experiment, review its details, then click **Launch Experiment**.


[1]: {{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/
[3]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/
[5]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/
[6]: {{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions

[image1]: {% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %} 
