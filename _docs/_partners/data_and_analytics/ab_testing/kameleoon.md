---
nav_title: Kameleoon
article_title: Kameleoon
description: "Learn how to integrate Kameleoon with Braze"
alias: /partners/kameleoon/
page_type: partner
search_tag: Partner
---

# Kameleoon

>[Kameleoon](https://www.kameleoon.com) is an optimization solution with experiment, AI-powered personalization, and feature management capabilities in a single unified platform.

## Prerequisites

Before you start, you'll need the following:

| Requirement | Description |  
| --- | --- |  
| Kameleoon account | A Kameleoon account is required to take advantage of this partnership.|  
| Braze account| An active Braze account with the [Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) integrated on your webpage. You’ll also need event property segmentation enabled. To request it, refer to [Considerations](#considerations).|  
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Use cases

Kameleoon sends custom events to Braze to identify users participating in experimentation and personalization campaigns, enabling more precise targeting and personalized messaging.

## Integrating Kameleoon

This integration runs as a JavaScript tracker through Kameleoon’s engine.js. It can be quickly enabled from within Kameleoon’s platform.

### Step 1: Go to the Kameleoon Integrations page

In your Kameleoon app, select **Admin** and then **Integrations** on the sidebar.

![The Admin panel in the Kameleoon platform.]({% image_buster /assets/img/kameleoon/img_1.png %}){: style="max-width:70%;"}

### Step 2: Install the Braze tool

By default, the Braze tool isn't installed. Look for the Braze icon, then select **Install the tool**. ![A grey square with a downward-pointing arrow.]({% image_buster /assets/img/kameleoon/img_2.png %})

Select the projects for which you want to activate the Braze tool, so that Kameleoon data will correctly report to Braze.

![The Braze tool icon in Kameloon.]({% image_buster /assets/img/kameleoon/img_3.png %})

After configuring the tool, select **Validate**, which will close the configuration panel. You will then see an **ON** toggle next to the Braze tool’s icon, including the number of projects the tool is configured on.

![The Braze tool toggled "On" in Kameleoon.]({% image_buster /assets/img/kameleoon/img_4.png %})

{% alert important %}  
This feature is in beta. Join the [Kameleoon Beta Program](https://help.kameleoon.com/account-and-team-management/join-beta-program/) to start using this integration.  
{% endalert %}  
    
### Step 3: Associate Braze with Kameleoon campaigns

#### In the Graphic/Code editor

To finalize your experiment, select the **Integrations** step to configure Braze as a tracking tool, then select **Braze**.

![The Integrations dashboard in Kameleoon showing all available integrations, including the active integration Braze.]({% image_buster /assets/img/kameleoon/img_5.png %})

Braze will be mentioned in the summary before going live. Kameleoon will automatically transmit the data to Braze, and you'll be able to use it for analysis and segmentation directly in Braze.

##### Personalization creation

On the **Personalization Creation** page, you can select Braze among the reporting tools to personalize your reporting.

![Reporting Tools section showing integrations such as Heap, Mixpanel, Clarity, with Braze selected.]({% image_buster /assets/img/kameleoon/img_6.png %})

##### Feature flag creation

Set up the integration in the feature flag environment in the **Integrations** section. Enable it for the environments where you want it active.

![The Feature Flag page in Kameleoon with available integrations. There are two switches for each partner, "Delivery rules" and "Feature experiments".]({% image_buster /assets/img/kameleoon/img_7.png %})

##### Results page

After Braze is set as a reporting tool for an experiment, you can select (or unselect) it on the Kameleoon results page in the **Experiment configuration** menu.

{% alert note %}  
This integration requires a [hybrid implementation](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics) and is only compatible with web SDKs.
{% endalert %}

![The side panel of the results page in Kameleoon.]({% image_buster /assets/img/kameleoon/img_8.png %}){: style="max-width:50%;" }

The reporting tools associated with the experiment will display. Select **Edit** to edit this selection.

### Step 4: Analyze and Leverage Your Kameleoon Data in Braze

After the integration is set up, Kameleoon will send custom events called `kameleoon_exposure` with properties such as **Experiment name**, **Experiment ID**, **Variation name**, **Variation ID** to Braze.

![The custom event user log in Braze, showing an example payload of the event that has been received by Braze from Kameleoon.]({% image_buster /assets/img/kameleoon/img_9.png %})

You can then view this data in the Custom Events, create custom event reports to identify Kameleoon campaign exposure, and enable segmentation based on event properties. You can use custom events when creating subsequent or linked campaigns and Canvases through [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups), [action-based triggers]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery) or creating [segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)

Furthermore, these events will be accessible through [Currents custom event objects]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) to allow for comprehensive reporting and analysis.

## Considerations

### Request event property segmentation

Before you can use event property segmentation, you'll need it enabled in Braze. Use the following template to contact your Braze CSM or the support team for access.

   <table>
   <thead>
      <tr>
         <th>Field</th>
         <th>Details</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><strong>Subject</strong></td>
         <td>Request to Enable Event Property Segmentation for Kameleoon Integration</td>
      </tr>
      <tr>
         <td><strong>Body</strong></td>
         <td>
         Hello Braze Team,<br><br>
         We would like to enable event property segmentation for events sent from our Kameleoon&lt;&gt;Braze integration. Here are the details:<br><br>
         - <strong>Event Name:</strong> Kameleoon<br>
         - <strong>Event Properties:</strong> <code>kameleoon_campaign_name</code>, <code>kameleoon_variation_name</code><br><br>
         Please confirm once the properties have been enabled in our account.<br><br>
         Thank you.
         </td>
      </tr>
   </tbody>
   </table>
   {: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Braze data points

The custom event sent from Kameleoon to Braze&#8212;including any event properties enabled for segmentation&#8212;will log data points in your Braze instance.