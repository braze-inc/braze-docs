\<\!-- In most cases, the ARTICLE\_TITLE will be your company name. If your tool requires several seperate pages on Braze Docs, you can add a relevant page descriptor to your title, such as "MyCompany Analytics." \--\>  
\# Kameleoon

\<\!-- The description starts with a '\>' character and contains an introduction to your company, a link to your main site, and a consice overview of your integration. In a following paragraph, highlight the the relationship between your company and Braze and how this partnership helps your customers. \--\>  
\>\[Kameleoon\]([https://www.kameleoon.com](https://www.kameleoon.com)) is the only optimization solution with Experiment, AI-Powered Personalization, and Feature Management capabilities in a single unified platform.

ADDITIONAL\_INFORMATION.

\<\!-- Most partner integrations will require the following prerequisites. However, you may add additional prerequisites as needed. \--\>  
\#\# Prerequisites

Before you start, you'll need the following:

| Requirement | Description |  
| \--- | \--- |  
| Kameleoon account | A Kameleoon account is required to take advantage of this partnership.|  
| Braze account| An active Braze account with the [Braze Web SDK](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=web) integrated on your webpage. You’ll also need event property segmentation enabled. To request it, see [Considerations](https://www.braze.com/docs/partners/data_and_analytics/ab_testing/vwo#request-event-property-segmentation).|  
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

\<\!-- An optional section you can use to outline the typical or atypical use cases for your integration. \--\>  
\#\# Use cases

Kameleoon sends custom events to Braze to identify users participating in experimentation and personalization campaigns, enabling more precise targeting and personalized messaging.

\<\!-- Create step-by-step instructions for integrating your tool with Braze. It's important to be concise and only outline the minimum neccesary steps. \--\>  
\#\# Integrating Kameleoon

This integration runs as a JavaScript tracker via Kameleoon’s engine.js. It can be quickly enabled from within Kameleoon’s UI.

\#\#\# Step 1: Navigate to the Kameleoon Integrations page

Log in to your Kameleoon App, click on \*\*Admin\*\* and then \*\*Integrations\*\* down the sidebar.

\<\!-- Use the "Make a post request", "Default behavior," and "Rate limit" sections to outline how users can make a POST request. If this information isn't required for your integration, you can remove these sections. →

\#\#\# Step 2: Install the “Braze” tool

By default, the tool is not installed. This is signaled by this icon:

By clicking on \*\*Install the tool\*\*, you will be able to select the projects on which you want to activate it, so that Kameleoon data can be correctly reported to Braze.

Once you have configured the tool, click on \*\*Validate\*\* in the bottom-right corner: the configuration panel will close. You will then see an \*\*ON\*\* toggle to the right of the tool’s logo, as well as the number of projects the tool is configured on.

{% alert important %}  
This feature is in Beta. \[Join Kameleoon Beta Program\]\[1\] to start using this integration.  
{% endalert %}  
    
\#\#\# Step 3: Associate Braze with Kameleoon Campaigns

### \#\#\#\#In the Graphic/Code editor

When finalizing your experiment, click the \*\*Integrations\*\* step to configure Braze as a tracking tool.  
Select \*\*Braze\*\*

Braze will be mentioned in the summary before going live. Kameleoon will automatically transmit the data to Braze, and you will be able to use it for analysis and segmentation directly in the Braze interface.

## \#\#\#\#On the personalization creation page

In the same way as A/B testing, you can select Braze among the reporting tools for a personalization.

## \#\#\#\#On the feature flag creation page

Set up the integration in the feature flag environment in the integrations section. Enable it for the environments where you want it active.

## \#\#\#\#On the results page

Once Braze is set as a reporting tool for an experiment, you can select (or unselect) it via the Kameleoon results page.

To do this, click on \*\*Experiment configuration\*\* in the kebab menu on the top right to open the corresponding menu.

{% alert note %}  
This integration require a \[hybrid implementation\]\[0\] and are only compatible with Web SDKs.

{% endalert %}

The reporting tools associated with the experiment are displayed. Click \*\*Edit\*\* to edit this selection.

\#\#\# Step 4: Analyze and Leverage Your Kameleoon Data in Braze

Once the integration has been set up, Kameleoon will send custom events called “kameleoon\_exposure” with properties such as \*\*Experiment name\*\*, \*\*Experiment ID\*\*, \*\*Variation name\*\*, \*\*Variation ID\*\* to Braze.

You’ll then be able to view this data in the Custom Events, create custom event reports to identify Kameleoon campaign exposure and enable segmentation based on event properties. Custom events can be leveraged when creating subsequent or linked campaigns and canvasses through \[Action Paths\]\[3\], \[Action-based Triggers\]\[4\] or creating \[Segments\]\[5\]

Furthermore, these events will be accessible through \*\*\[Currents Custom Event objects\]\*\*\[2\] to allow for comprehensive reporting and analysis.

\[0\]: [https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en\#sending-exposure-events-to-third-party-analytics](https://developers.braze-presentation.preview.kameleoon.net/core-concepts/hybrid-experimentation?language=en#sending-exposure-events-to-third-party-analytics)   
\[1\]: [https://help.kameleoon.com/account-and-team-management/join-beta-program/](https://help.kameleoon.com/account-and-team-management/join-beta-program/)   
\[2\]: [https://www.braze.com/docs/user\_guide/data/distribution/braze\_currents/event\_glossary/customer\_behavior\_events](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)   
\[3\]: [https://www.braze.com/docs/user\_guide/engagement\_tools/canvas/canvas\_components/action\_paths/\#action-groups](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/action_paths/#action-groups)   
\[4\]:[https://www.braze.com/docs/user\_guide/engagement\_tools/campaigns/building\_campaigns/delivery\_types/triggered\_delivery](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery)   
\[5\]:[https://www.braze.com/docs/user\_guide/engagement\_tools/segments/creating\_a\_segment/\#step-1-navigate-to-the-segments-section](https://www.braze.com/docs/user_guide/engagement_tools/segments/creating_a_segment/#step-1-navigate-to-the-segments-section) 