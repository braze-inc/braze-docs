---
nav_title: Decisioning Studio Go
article_title: BrazeAI Decisioning Studio Go
page_order: 0
description: "Learn how to set up and integrate BrazeAI Decisioning Studio<sup>TM</sup> Go into Braze."
---

# BrazeAI Decisioning Studio™ Go

> Learn how to locate key information in Braze to begin integrating with BrazeAI Decisioning Studio™ Go. 

## Essentials

### Creating an API key

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

1. In the Braze dashboard, go to **Settings** > **Email Preferences**.
2. Locate the display name to be used with BrazeAI Decisioning Studio™ Go.
3. Copy and paste the **From Display Name** into the BrazeAI Decisioning Studio™ Go portal as the **Email Display Name**.
4. Copy and paste the associated email address into your BrazeAI Decisioning Studio™ Go portal as the **From email address**, which combines the local part and the domain.

### Locating your user ID

1. In the Braze dashboard, go to **Audience** > **Search Users**.
2. Search for the user by their external user ID, user alias, email, phone number, or push token.
3. Copy the user ID to reference in your setup.

![Example user profile from locating a user with their ID.]({% image_buster /assets/img/decisioning_studio_go/user_id.png %})

### Finding your Braze URL

1. Go to the Braze dashboard.
2. In your browser window, your Braze URL is starts with `https://` and ends with `braze.com`. An example Braze URL is `https://dashboard-01.braze.com`.

### Finding your Braze API key

{% alert note %}
Braze offers app IDs (referred to as API keys in the Braze dashboard) that you can use for tracking purposes, such as to associate activity with a specific app in your workspace. If you use app IDs, BrazeAI Decisioning Studio™ Go supports associating an app ID with each experimenter.<br><br>If you do not use app IDs, you can enter any string of characters as a placeholder.
{% endalert %}

1. In the Braze dashboard, go to **Settings** > **App Settings**.
2. Go to the app you want to track.
3. Copy and paste the **API Key** into your BrazeAI Decisioning Studio™ Go portal.
