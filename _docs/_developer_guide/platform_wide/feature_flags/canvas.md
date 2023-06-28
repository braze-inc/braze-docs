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
