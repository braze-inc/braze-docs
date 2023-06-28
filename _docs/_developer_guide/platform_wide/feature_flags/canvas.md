---
nav_title: Feature Flags in Canvas 
article_title: Feature Flags in Canvas 
page_order: 30
description: "This reference article covers how to feature flags can be used in Canvas."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Feature Flags in Canvas

## Selecting a Feature Flag

To enable a Feature Flag for a user in a canvas, add the Feature Flag step.

Next, choose the Feature Flag from the list. This list contains any feature flags which are not archived.

## Overwriting Properties

When creating a feature flag you specify default properties. When setting up a Feature Flag Canvas step, you can either keep the default values, or overwrite the values for users who enter this step.

To add additional properties, that should be done in the Feature Flag management screen, outside of the Canvas.


## Canvas vs. Rollout Differences

Canvas and a Feature Flag Rollout (dragging the slider) can work independently of each other.

The important caveat is that entry to a Canvas step will overwrite any default rollout configuration. For example, if a user does not qualify for a feature flag, a canvas step can enable the feature for that user.

Similarly, if a user qualifies for a feature flag rollout with certian properties, if they also enter into the canvas step, they will receive any overwritten values from that canvas step.


## Frequently Asked Questions

1. What happens when I turn off a Canvas or delete a Feature Flag step?

When a Canvas is stopped, or archived, or a step is removed, any user who had gone through that step will no longer receive the step's feature flag and its properties.

The user will still be subject to the default rollout % and audience segmentation for that feature flag, and any other canvases that might still be active.

2. What happens if I change properties of a Feature Flag after I launch the canvas?

Properties in a Canvas step can be changed after launch, and even after a user goes through the step. Users will always receive a real-time, dynamic version of the Feature Flag, instead of the older, previously saved version.
