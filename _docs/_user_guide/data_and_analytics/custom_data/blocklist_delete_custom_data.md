---
nav_title: Blocklisting or Deleting Custom Data
article_title: Blocklisting or Deleting Custom Data
page_order: 2
page_type: reference
description: "This reference article how to blocklist or delete custom events, custom attributes, or purchase events."
---

# Blocklisting or deleting custom data

You may occasionally identify custom attributes, custom events, or purchase events that are either consuming too many data points, are no longer useful to your marketing strategy, or were recorded in error. To stop this data from being sent to Braze, you can blocklist a custom data object while your engineering team works to remove it from the backend of your app or website.

The process to retire a custom data object looks like this:

1. You [blocklist](#blocklisting-custom-data) the custom data object so it is no longer recorded.
2. You remove the code from your deployments of the Braze SDK, CDP configurations, or other data sources (i.e., data sent from your backend to Braze via API) that record this custom data object.
3. Your customer success manager or the Braze Support team delete the custom data object from the list of custom attributes, custom events, or purchase events.

## Blocklisting custom data

Blocklisting prevents a particular custom data object from being recorded by Braze going forward.

{% alert important %}
Blocklisting does not remove data from user profiles or retroactively decrease the amount of data points incurred for that custom data object.
{% endalert %}

To blocklist a custom data object:

1. In Braze, go to **Manage Settings**.
2. Select the relevant page for the custom data object you want to blocklist: **Custom Attributes**, **Custom Events**, or **Products**.
3. Find the custom data object in the table.
4. Select **Blocklist**.

![Warning that prevents you from blocklisting a custom data object and lists where the custom data is currently being referenced.][1]{: style="max-width:50%;float:right;margin-left:15px;"}

If the custom data object is still in use, you need to remove it from the segment filters or campaign triggers it is referenced in before you can blocklist it. You can see where the custom data is currently in use when you attempt to blocklist it.

If the custom data is being referenced in too many places, or if you want to blocklist many items at once, please reach out to support for help.

## Deleting custom data

After you have blocklisted the custom data object and removed references to it from your app or website, your customer success manager or the Support team will delete the custom data.

Deleting custom data does the following:

- Removes the custom attribute, custom event, or purchase event from segment filter selections and analytics pages.
- Removes the custom attribute, custom event, or purchase event from the respective page under **Manage Settings**.

{% alert important %}
Deleting does not remove data already recorded on user profiles, or prevent additional recording of the custom data objects on user profiles. Make sure the custom data is no longer being recorded before having the event or attribute deleted.
{% endalert %}

[1]: {% image_buster/assets/img_archive/blocklist_warning.png %}