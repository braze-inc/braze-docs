---
page_order: 1.3
nav_title: Debugging
article_title: Debugging the Braze SDK 
description: "Learn how to use the Braze SDK debugger, so you can troubleshoot issues for your SDK-powered channels, without enabling verbose logging in your app manually."
---

# Debugging the Braze SDK

> Learn how to use the Braze SDK's built-in debugger, so you can troubleshoot issues for your SDK-powered channels, without needing to enable verbose logging in your app.

## Prerequisites

To use the Braze SDK debugger, you'll need "View PII" and "View User Profiles PII Compliant" permissions. To download your debugging session logs, you'll also need the "Export User Data" permission. Additionally, your Braze SDK needs to meet or point to the following minimum versions: 

{% sdk_min_versions swift:10.2.0 android:32.1.0 %}

## Debugging the Braze SDK

{% alert tip %}
To enable debugging for the Braze Web SDK, you can [use a URL parameter]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging).
{% endalert %}

### Step 1: Close your app

Before you start your debugging session, close the app that's currently experiencing issues. You can relaunch the app at the start of your session.

### Step 2: Create a debugging session

In Braze, go to **Settings**, then under **Setup and Testing**, select **SDK Debugger**.

![The "Setup and Testing" section with "SDK Debugger" highlighted.]({% image_buster /assets/img/sdk_debugger/select_sdk_debugger.png %})

Select **Create debugging session**.

![The "SDK Debugger" page.]({% image_buster /assets/img/sdk_debugger/select_create_debugging_session.png %})

### Step 3: Select a user

Search for a user using their email address, `external_id`, user alias, or push token. When you're ready to start your session, select **Select User**.

![The debugging page for the selected user.]({% image_buster /assets/img/sdk_debugger/search_and_select_user.png %}){: style="max-width:85%;"}

### Step 4: Relaunch the app

First, launch the app and confirm that your device is paired. If the pairing is successful, relaunch your app&#8212;this will ensure that app's initialization logs are fully captured.

### Step 5: Complete the reproduction steps

After relaunching your app, follow the steps to reproduce the error.

{% alert tip %}
When you're reproducing the error, be sure to follow the reproduction steps as closely as possible, so you can create [quality logs](#step-6-export-your-session-logs-optional).
{% endalert %}

### Step 6: End your session

When you're finished with your reproduction steps, select **End Session** > **Close**.

![The debugging session showing the "End Session" button.]({% image_buster /assets/img/sdk_debugger/close_debugging_session.png %}){: style="max-width:85%;"}

{% alert note %}
It may take a few minutes to generate your logs depending on your session length and network connectivity.
{% endalert %}

### Step 7: Share or export your session (optional)

After your session, you can export your session logs as a CSV file. Additionally, others can use your **Session ID** to search for your debug session, so you don't need to send them your logs directly.

![The debugging page with "Export Logs" and "Copy Session ID" shown after the session.]({% image_buster /assets/img/sdk_debugger/copy_id_and_export_logs.png %})
