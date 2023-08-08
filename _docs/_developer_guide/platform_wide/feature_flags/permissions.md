---
nav_title: Feature Flag Filters
article_title: Feature Flag Filters
page_order: 40
description: "This reference article describes the user permissions required to manage feature flags"
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Feature Flag Permissions

Braze Feature Flags allow for fine-grained user access control to prevent unauthorized access and modifications.

To view the list of available feature flags, users must have the "Access Campaigns, Canvases, Cards, **Feature Flags**, ..." permission.

In order to create or edit existing feature flags, users must have access to the new "Manage Feature Flags" permission.

{% alert note %}
Administrator users automatically have access to manage feature flags. For limited users, you can explicitly allow or restrict access to Manage Feature Flags at a Workspace level. This is useful if certain users should only be able to modify feature flags for specific environments or business units.
{% endalert %}

![Manage Feature Flags permission][1]


[1]: {% image_buster /assets/img/feature_flags/feature-flags-manage-permission.png %}

