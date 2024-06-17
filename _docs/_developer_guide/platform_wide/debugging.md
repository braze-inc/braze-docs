---
nav_title: Debugging
article_title: Debugging the Braze SDK 
description: "Learn how to use the Braze SDK's built-in debugger, so you can troubleshoot issues for your SDK-powered channels, without needing to enable verbose logging in your app."
page_order: 3
---

# Debugging the Braze SDK

> Learn how to use the Braze SDK's built-in debugger, so you can troubleshoot issues for your SDK-powered channels, without needing to enable verbose logging in your app.

{% alert important %}
Currently, this feature is only available for native iOS and Android apps. To enable debugging for the Braze Web SDK, you can [use a URL parameter]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#logging) instead.
{% endalert %}

## Prerequisites

To use the Braze SDK debugger, ensure your SDKs are up to date with at least these minimum versions:

XXX XXX XXX 

## Debugging the Braze SDK

### Step 1: Close your app

Before you start your session, close the app that's currently experiencing issues. You can relaunch the app at the start of your session. 

### Step 2: Create a debugging session

In Braze, go to **Settings**, then under **Setup and Testing**, select **SDK Debugger**.

![ALT_TEXT]()

Select **Create debugging session**.

![ALT_TEXT]()
 
Search for a user using their email address, `external_id`, user alias, or push token. When you're ready, select the user.

![Image of user search and selection.]()

### Step 3: Start your session

When you're ready to start your debugging session for the selected user, select **Start Session**.

![Image of modal of selected user to debug.]()

### Step 4: Complete the reproduction steps

Open your app, then follow the reproduction steps for your error.

{% alert tip %}
When you are reproducing the error, be sure to follow the reproduction steps as closely as possible so your [debug logs](#step-6-export-your-session-logs-optional) are as helpful as possible.
{% endalert %}

![Image of modal of debug in progress.]()

### Step 5: End your session

When you're finished with your reproduction steps, select **TODO**.

![Image of End Session button.]()

### Step 6: Export your session logs (optional)

After your session, you can export your session logs as a CSV file.

![Image of where to download S3 file in table view.]()

{% alert note %}
It may take a few minutes to generate your logs depending on your session length and network connectivity.
{% endalert %}

### Step 7: Share your session ID (optional)

After your session, you can copy and share your session ID to others so they can export the session logs.

![Image of modal of Session ID for copy.]()
