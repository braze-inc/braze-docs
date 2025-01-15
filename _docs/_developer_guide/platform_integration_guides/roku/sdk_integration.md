---
nav_title: SDK Integration
article_title: Integrating the Braze Roku SDK
platform: Roku
page_order: 0
page_type: reference
description: "This page describes initial setup steps for the Braze Roku SDK."
search_rank: 1
---

# Integrating the Braze Roku SDK

> Learn how to integrate and customize the Braze Roku SDK. To see our Roku sample app,checkout [TorchieTV](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv) on GitHub.

## Integrating the SDK

### Step 1: Add files

Braze SDK files can be found in the `sdk_files` directory in the [Braze Roku SDK repository](https://github.com/braze-inc/braze-roku-sdk).

1. Add `BrazeSDK.brs` to your app in the `source` directory.
2. Add `BrazeTask.brs` and `BrazeTask.xml` to your app in the `components` directory.

### Step 2: Add references

Add a reference to `BrazeSDK.brs` in your main scene using the following `script` element:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### Step 3: Configure

Within `main.brs`, set the Braze configuration on the global node:

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

You can find your [SDK endpoint]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) and API key within the Braze dashboard.

### Step 4: Initialize Braze

Initialize the Braze instance:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Optional configurations

### Logging

To debug your Braze integration, you can view the Roku debug console for Braze logs. Refer to [Debugging code](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) from Roku Developers to learn more.
