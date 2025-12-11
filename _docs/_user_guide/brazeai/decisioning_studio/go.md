---
nav_title: Decisioning Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 0
description: "Learn how to set up and integrate BrazeAI Decisioning Studio<sup>TM</sup> Go into Braze."
---

# BrazeAI Decisioning Studio™ Go

> Locate key information in Braze to begin integrating with BrazeAI Decisioning Studio™ Go.

## Essentials

### Creating a REST API key in Braze

To create a new REST API key:

1. In the Braze dashboard, go to **Settings** > **APIs and Identifiers** > **API Keys**.
2. Select **Create API Key**.
3. Enter a name for your API key. An example is "DecisioningStudioGoEmail".
4. Select the permissions based on the following categories:
    - **User Data:** select `users.track`, `users.delete`, `users.export.ids`, `users.export.segment`
    - **Messages:** select `messages.send`
    - **Campaigns:** select all listed permissions
    - **Canvas:** select all listed permissions
    - **Segments:** select all listed permissions
    - **Templates:** select all listed permissions
{: start="5"}
5. Select **Create API key**.
6. Then, copy the API key and paste it into your BrazeAI Decisioning Studio™ Go portal.

### Locating your Braze email display name

To find your Braze email display name:

1. In the Braze dashboard, go to **Settings** > **Email Preferences**.
2. Locate the display name to be used with BrazeAI Decisioning Studio™ Go.
3. Copy and paste the **From Display Name** into the BrazeAI Decisioning Studio™ Go portal as the **Email Display Name**.
4. Copy and paste the associated email address into your BrazeAI Decisioning Studio™ Go portal as the **From email address**, which combines the local part and the domain.

### Locating your user ID

To find your user ID:

1. In the Braze dashboard, go to **Audience** > **Search Users**.
2. Search for the user by their external user ID, user alias, email, phone number, or push token.
3. Copy the user ID to reference in your setup.

![Example user profile from locating a user with their ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

### Finding your Braze URL

To identify your Braze URL:

1. Go to the Braze dashboard.
2. In your browser window, your Braze URL is starts with `https://` and ends with `braze.com`. An example Braze URL is `https://dashboard-01.braze.com`.

### Finding your Braze API key

{% alert note %}
Braze offers app IDs (referred to as API keys in the Braze dashboard) that you can use for tracking purposes, such as to associate activity with a specific app in your workspace. If you use app IDs, BrazeAI Decisioning Studio™ Go supports associating an app ID with each experimenter.<br><br>If you do not use app IDs, you can enter any string of characters as a placeholder.
{% endalert %}

1. In the Braze dashboard, go to **Settings** > **App Settings**.
2. Go to the app you want to track.
3. Copy and paste the **API Key** into your BrazeAI Decisioning Studio™ Go portal.

### Setting up Klaviyo API keys

You must set up an API key to use Klaviyo for BrazeAI Decisioning Studio™ Go.

1. In Klaviyo, go to **Settings** > **API keys**.
2. Select **Create Private API Key**. 
3. Enter a name for the API key. An example is "Decisioning Studio Experimenters".
4. Select the following permissions for the API key:
    - Campaigns: Read Access
    - Data Privacy: Full Access
    - Events: Full Access
    - Flows: Full Access
    - Images: Read Access
    - List: Full Access
    - Metrics: Full Access
    - Profiles: Full Access
    - Segments: Read Access
    - Templates: Full Access
    - Webhooks: Read Access

![A Klaviyo API key with selected permissions.]({% image_buster /assets/img/decisioning_studio_go/klaviyo_api_key.png %})

{: start="5"}
5. Select **Create**. 
6. Copy this API key and paste it into the BrazeAI Decisioning Studio™ Go portal where prompted.

### Setting up an SFMC app package

To use Salesforce Marketing Cloud for BrazeAI Decisioning Studio™ Go, you must set up an app package in Salesforce Marketing Cloud. 

1. Go to your Marketing Cloud home page. 
2. Open the menu in the global header and select **Setup**.
3. Go to **Apps** under **Platform Tools** in the side panel navigation, then select **Installed Packages**.
4. Select **New** to create an app package.
5. Give the app package a name and description.

![An app package with the name "Experimenter 1 - Test 5".]({% image_buster /assets/img/decisioning_studio_go/sfmc_app_package1.png %})

{: start="6"}
6. Select **Add Component**.
7. For the **Component Type**, select **API Integration**. Then, select **Next**.
8. For the **Integration Type**, select **Server-to-server**. Then, select **Next**.
9. Then, select the following recommended scopes for your app package only:
    - Channels > Email > Read, Write, Send
    - Channels > OTT > Read
    - Channels > Push > Read
    - Channels > SMS > Read
    - Channels > Social > Read
    - Channels > Web > Read
    - Assets > Documents and Images > Read, Write
    - Assets > Saved Content > Read, Write
    - Automation > Automations > Read, Write, Execute
    - Automation > Journeys > Read, Write, Execute, Activate/Stop/Pause/Send/Schedule
    - Contacts > Audiences > Read
    - Contacts > List and Subscribers > Read, Write
    - Cross Cloud Platform > Market Audience > View
    - Cross Cloud Platform > Market Audience Member > View
    - Cross Cloud Platform > Marketing Cloud Connect > Read
    - Data > Data Extensions > Read, Write
    - Data > File Locations > Read
    - Data > Tracking Events > Read, Write
    - Event notifications > Callbacks > Read
    - Event notifications > Subscriptions > Read

{% details Show image of recommended scopes %}

![The recommended scopes for Salesforce Marketing Cloud app package.]({% image_buster /assets/img/decisioning_studio_go/app_package_scopes.png %})

{% enddetails %}

{: start="10"}
10. Select **Save**.
11. Copy and paste the following fields into the BrazeAI Decisioning Studio™ Go portal: **Client Id**, **Client Secret**, **Authentication Base URI**, **REST Base URI**, **SOAP Base URI**.