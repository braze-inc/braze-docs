---
nav_title: Feature flags
article_title: Feature Flags
page_order: 8
page_type: reference
description: "This reference article covers how feature flags can be used in Canvas."
tool: Canvas
local_redirect:
  create-a-feature-flag: '/docs/user_guide/engagement_tools/canvas/canvas_components/feature_flags/#creating-a-feature-flag'
---

# Feature flags

> Feature flags allow you to experiment and confirm your hypotheses around new features. Marketers can use feature flags to segment your audience in [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) and track the impact of feature rollout on conversions. Moreover, [Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) allow you optimize these conversions by testing different messages or paths against each other and determining which is most effective. Use the Winning Path as you progressively rollout your feature to a wider audience.

Looking for more information about feature flags and how they can be used in Braze? Check out our dedicated [Feature flags]({{site.baseurl}}/developer_guide/feature_flags/) articles.

## Creating a feature flag

![An example Feature Flag step for the Live Chat Button feature.]({% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

To create a Feature Flag component, first add a step to your Canvas. Drag and drop the component from the sidebar, or click the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Feature Flag**. Next, select the feature flag from the dropdown, which contains any feature flags that are not archived.

## How this step works

When a Canvas is stopped, or archived, or a step is removed, any user who has gone through that step will no longer receive the step's feature flag and its properties. The user will still be subject to the default rollout percentage and audience segmentation for that feature flag and any other Canvases that might still be active.

Properties in a Canvas step can be changed after launch, and even after a user goes through the step. Users will always receive a real-time, dynamic version of the feature flag, instead of the older, previously saved version.

## Overwriting properties

When creating a feature flag you specify default properties. When setting up a feature flag Canvas step, you can either keep the default values, or overwrite the values for users who enter this step.

![A feature flag "Preference Center" with "String" as the property, "url" as the property key, and a value.]({% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %}){: style="max-width:90%"}

Go to **Messaging** > **Feature Flags** to edit, add, or remove additional properties.

## Canvas and rollout differences

Canvas and a feature flag rollout (dragging the slider) can work independently of each other. An important caveat is entry to a Canvas step will overwrite any default rollout configuration. This means if a user doesn't qualify for a feature flag, a Canvas step can enable the feature for that user.

Similarly, if a user qualifies for a feature flag rollout with certain properties, if they also enter into the Canvas step, they will receive any overwritten values from that Canvas step.

