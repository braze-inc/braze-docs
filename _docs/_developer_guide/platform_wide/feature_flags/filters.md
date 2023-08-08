---
nav_title: Feature Flag Filters
article_title: Feature Flag Filters
page_order: 40
description: "This reference article describes ways to create segments based on users' feature flag membership."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Feature Flag Filters

Braze automatically keeps track of which users are currently eligible or participating in a Feature Flag.

You can create a segment, or target messaging using the new Feature Flag Membership filter.

1. Choose the new "Feature Flag" segementation filter, listed under "User Activity":

![Segmentation filter named "Feature Flag"][1]

2. Choose a Feature Flag name/ID from the list of active feature flags.

![Segmentation filter with a feature flag ID selected][2]

{% alert note %}
To prevent recursive segments, it is not possible to create a segment that references other feature flags.
{% endalert %}

[1]: {% image_buster /assets/img/feature_flags/feature-flags-filter-name.png %}
[2]: {% image_buster /assets/img/feature_flags/feature-flags-filter-selection.png %}

