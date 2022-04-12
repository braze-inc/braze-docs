---
nav_title: Answers for Google Play Store Privacy Questions
article_title: Answers for Google Play Store Privacy Questions
page_order: 9
platform: 
  - Android
  - FireOS
description: "This article covers how to answer Google Play Privacy questions"
---
<br>

# Google Play Privacy Questionaire

Google requires you to disclose your apps' privacy and security practices when submitting to the Google Play Consolse.

This guide will give you information on how Braze handles your app data to help you answer the questions. As the app developer, you are in control of what data Braze receives. Data received by Braze is processed in the manner you request. This is what Google classifies as a [service provider][3]. 

|Questions|Answers for Braze SDK|
|---|---|
|Does your app collect or share any of the required user data types?|Yes, but what data is collected is configured by the app developer|
|Is all of the user data collected by your app encrypted in transit?|Yes|
|Do you provide a way for users to request that their data is deleted?|Yes|

For more information about how to handle user requests for their data and deletion, see [Braze Data Retention Information][1]

|Data Type|Braze Usage|
|---|---|
|Location|If configured to do so by app configuration.|
|Personal info|If configured to do so by app configuration.|
|Financial info|If the app is using Braze to log purchase events, we will have purchase history.|
|Health and fitness|If configured to do so by app configuration. ENCOURAGE HIPAA SERVER?|
|Messages|If configured to do so by app configuration.  NOTE: Braze may generate In-App Messages and Push notification that are sent to users.|
|Photos and videos|Braze does not store large data.|
|Audio files|Braze does not store large data.|
|Files and docs|Braze does not store large data.|
|Calendar events|If configured to do so by app configuration.|
|Contacts|If configured to do so by app configuration.|
|App activity|If configured to do so by app configuration.|
|Web browsing|No.|
|App info and performance|Yes, app version is stored in crash reports.|
|Crash logs|Yes, Braze does collect crash logs for errors that occur within the SDK. This contains the user's phone model and OS level, along with a Braze specific user ID.|
|Diagnostics|No.|
|Other app performance data|No.|
|Device or other IDs|Yes, Braze generates a random ID for your device.|

You can also see the other device data that Braze collects, along with how to disable them, that falls oustide of Google Play's Data Safety guidelines [here][2]

[1]: https://www.braze.com/docs/api/data_retention/
[2]: https://www.braze.com/docs/developer_guide/platform_integration_guides/android/storage
[3]: https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform