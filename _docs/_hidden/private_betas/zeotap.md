---
nav_title: Zeotap
description: ""
alias: /partners/zeotap/
page_type: partner
search_tag: Partner

---

# Zeotap

> [Judo](https://judo.app) is a server-driven UI platform that empowers publishers to efficiently deliver rich, engaging in-app user experiences without app updates.

Developers integrating Braze marketing automation with Judo experiences will find elevated value for their joint customers. Superior targeting, personalization, and campaign orchestration from Braze are linked to bespoke experiences from Judo. Instead of a simple, templated landing page experience, a Braze campaign may incorporate content that comprises multiple screens, modals, video, custom fonts, and support settings such as dark mode and accessibility built without code and deployed without app updates. Data from Braze may be used to support personalized content in a Judo experience. User events and data from the experience can feedback into Braze for attribution and targeting.

## Prerequisites

First, you will need to have already integrated both Braze and Judo into your apps.

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Judo Account | Judo | [Judo](https://www.judo.app/) | You'll need a Judo account in order to host Experiences for launch from Braze. |
| Judo SDK | Judo | [Judo iOS SDK](https://github.com/judoapp/judo-ios/) and [Judo Android SDK](https://github.com/judoapp/judo-android) | You'll need the Judo SDKs integrated into your iOS and/or Android apps. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Creating a Destination for Braze within Zeotap

Braze allows one destination per segment. From the Zeotap Unity platform:
1. Log into Unity and go to the __DESTINATIONS__ application.
2. Under the __All Channels__ section, search for Braze.
3. Click __Braze__ and enter the following details in the window that appears.
	1. Enter a name for the Destination.
	2. Enter the Client Name. This is the account name within Braze.
	3. Enter the API Key associated with the Braze account. You can find it under Settings → Developer Console → Rest API Keys. Your account might already have an existing API key available in this section but User data permissions are required for the API key to work. If the existing key does not have the required permissions, create a new key by clicking on “Create New API key” as below:

	Once generated, the API key would be available as below under the Identifier column:
	4. Choose the appropriate Instance that the account is associated with. Braze manages a number of different instances for the dashboard and REST Endpoints. When your account is provisioned you will log in to one of the corresponding URLs below. Use the correct REST Endpoint based on which instance you are provisioned to. If you are unsure, open a Braze support ticket or use the table below to match the URL of the dashboard you use to the correct REST Endpoint.
	5. Click Save Destination.

Creating a Segment for Braze within Zeotap
 
1. The following steps summarize the process of linking a Segment to a Destination within the Zeotap Unity Platform:
2. Log into Unity and go to the CONNECT application.
3. Create a Segment and push it to Braze.
4. Select the associated output identifier and then click Yes to activate the segment.

{% alert note %}
The identifiers that appear in the window are the ones that are available in the  segment and supported by Braze.
{% endalert %}

## Data Appearing on Braze Console

After you have successfully created a segment and the data is pushed and processed, the data appears within the Braze console.

As there is no concept of audience creation within Braze, there is no audience listing on the Braze console. You can search by User ID on the Braze console. Within Braze, each user ID is associated with a User Profile. You can also view the Custom Attributes associated with the User Profile.

The Custom Attributes section provides a list of segment names and the relevant Boolean value true indicating that the user is a part of the particular segment.

The following identifiers are supported for this integration:
- MAID
- sha256 email and phone

However, you can use only one of these identifiers while using the Braze integration. The identifier must be the same as the external ID that you have set while collecting data using the Braze SDK. Note that no other identifiers are recognised by Braze for the account.

To link the segment created in Zeotap within Braze and use the same in the campaigns, perform the following steps:
1. Click + Create Segment.
2. Select Custom Attribute and then add the segment that was created in Zeotap. 
3. Save the changes.
This segment can then be part of the campaigns to target the end users.

<!--
[2]: {% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %}
-->

