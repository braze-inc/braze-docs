---
nav_title: For Web
page_order: 2

page_type: reference
description: "This article describes extra Web implementation steps customers on the EU-01 instance will need to take."
platform: Web
---

# For Web

For [Web SDK integrations](https://github.com/Appboy/appboy-web-sdk#getting-started) initialize the SDK with a baseUrl key pointing to our EU endpoint in the options paramater. For example:

Replace `appboy.initialize('YOUR-API-KEY-HERE')`

with

`appboy.initialize('YOUR-API-KEY-HERE',{baseUrl:'https://sdk.fra-01.braze.eu/api/v3'})`
