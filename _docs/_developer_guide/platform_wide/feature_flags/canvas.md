---
nav_title: Feature Flags in Canvas 
article_title: Feature Flags in Canvas 
page_order: 30
description: "This reference article covers how feature flags can be used in Canvas."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Feature flags in Canvas

> Feature flags allow you to experiment and confirm your hypotheses around new features. Marketers can use feature flags to segment your audience in [Canvas][1] and track the impact of feature rollout on conversations. Moreover, [Experiment Paths][2] allow you optimize these conversions by testing different messages or paths against each other and determining which is most effective. Use the Winning Path as you progressively rollout your feature to a wider audience.

## Selecting a feature flag

![][3]{: style="float:right;max-width:40%;margin-left:15px;"}

To enable a feature flag for a user in a Canvas, add the Feature Flag step. Next, select the feature flag from the list. This list contains any feature flags that are not archived.

When a Canvas is stopped, or archived, or a step is removed, any user who has gone through that step will no longer receive the step's feature flag and its properties.

The user will still be subject to the default rollout percentage and audience segmentation for that feature flag and any other Canvases that might still be active.

Properties in a Canvas step can be changed after launch, and even after a user goes through the step. Users will always receive a real-time, dynamic version of the feature flag, instead of the older, previously saved version.

## Overwriting properties

When creating a feature flag you specify default properties. When setting up a feature flag Canvas step, you can either keep the default values, or overwrite the values for users who enter this step.

![][4]{: style="max-width:80%"}

Go to the **Messaging** > **Feature Flags** to edit, add, or remove additional properties.

## Canvas and rollout differences

Canvas and a feature flag rollout (dragging the slider) can work independently of each other. An important caveat is entry to a Canvas step will overwrite any default rollout configuration. This means if a user doesn't qualify for a feature flag, a Canvas step can enable the feature for that user.

Similarly, if a user qualifies for a feature flag rollout with certain properties, if they also enter into the Canvas step, they will receive any overwritten values from that Canvas step.

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths
[3]: {% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %} 
[4]: {% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %} 