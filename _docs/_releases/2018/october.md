---
nav_title: October
page_order: 4
noindex: true
page_type: update
description: "This article contains release notes for October 2018."
---
# October 2018

{% comment %}
  Add these in at a later time...
  Intelligent Selection Control Group Toggle
  The Intelligent Selection box now has a checkbox that allows you to [toggle the use of a control group on or off]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#including-a-control-group). When on, the control group will be 20% of the audience size and will change as the Intelligent Selection feature optimizes the per variant audience sizes.
  Canvas Entry Settings Wizard (Beta)
  The Canvas UI will be simplified to prevent missed tasks and resulting errors. Canvas configurations, specifically, will now be displayed in a wizard, similar to the design of the campaigns wizard. This is not currently reflected in our documentation, as it is being rolled out gradually. Check back for more on this soon!
  Subscription Group API (hidden)
  Braze has made a new GET call available to enable you to request based on an external ID or email address. You will then be provided all the subscription groups associated with that user.
{% endcomment %}

## Calculate exact audience stats for campaigns

You can now go to **Campaign Analytics** and calculate the exact statistics for your audience. Click **Calculate Exact Stats** in the footer of the **Target Audiences** section, and the exact audience stats will populate. You will have to save the campaign before calculating (draft campaigns will be saved as drafts).

## Windows 8 deprecation

Braze no longer supports Windows 8 as of October 10, 2018.

## Partnerships hub

You can now find a list of your integrations on the Braze platform under **Integrations**, along with integration keys and instructions.

## Email analytics calculations

Braze is now calculating all email analytics using our email sending partner's (ESP) event data in order to greatly improve the accuracy of our email analytics. This solution utilizes Postgres, an open source database solution, to ensure data integrity.

{% alert important %}
Unique Opens and Unique Clicks are currently still dependent on the aggregate data provided by our email sending partners. There is work in progress to calculate these uniqueness stats using the same infrastructure introduced in this release.
{% endalert %}

## Composer panel controls

The Message Composer controls have been refreshed to include wording associated with icons to enable better usability and navigation.

## Azure for Currents

Braze customers using Currents can now see [Azure]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents#microsoft-azure-blob-storage) as a potential integration.

## Input field expansions

You can now expand the input boxes for email subject lines and push titles.
