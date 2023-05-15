---
nav_title: Blocklisting or Deleting Custom Data
article_title: Blocklisting or Deleting Custom Data
page_order: 2
page_type: reference
description: "This reference article covers how to blocklist or delete custom events, custom attributes, or purchase events."
---

# Blocklisting or deleting custom data

> You may occasionally identify custom attributes, custom events, or purchase events that are either consuming too many data points, are no longer useful to your marketing strategy, or were recorded in error. To stop this data from being sent to Braze, you can blocklist a custom data object while your engineering team works to remove it from the backend of your app or website.

## Blocklisting custom data

Blocklisting prevents a particular custom data object from being recorded by Braze going forward. Blocklisting does not remove data from user profiles or retroactively decrease the amount of data points incurred for that custom data object. For specific details, refer to [Custom event and attribute management]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/custom_event_and_attribute_management/#blocklisting-custom-attributes-custom-events-and-products).

## Deleting custom data

After you have blocklisted the custom data object and removed references to it from your app or website, the custom data will be deleted.

Deleting custom data does the following:

- Removes the custom attribute, custom event, or purchase event from segment filter selections and analytics pages.
- Removes the custom attribute, custom event, or purchase event from the respective page under **Manage Settings**.

{% alert important %}
Deleting does not remove data already recorded on user profiles, or prevent additional recording of the custom data objects on user profiles. Make sure the custom data is no longer being recorded before having the event or attribute deleted.
{% endalert %}

[1]: {% image_buster/assets/img_archive/blocklist_warning.png %}