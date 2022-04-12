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

This guide will give you information on how Braze handles your app data to help you answer the questions. As the app developer, you are in control of what data Braze receives. Data received by Braze is processed according to your instructions. This is what Google classifies as a [service provider][3]. 

|Questions|Answers for Braze SDK|
|---|---|
|Does your app collect or share any of the required user data types?|Yes, but what data is collected is configured by the app developer|
|Is all of the user data collected by your app encrypted in transit?|Yes|
|Do you provide a way for users to request that their data is deleted?|Yes|

For more information about how to handle user requests for their data and deletion, see [Braze Data Retention Information][1]

For the data collected by Braze, that's going to be dependent on what data you as an app developer choose to collect.  While Braze has fields for the most common data (name, email, etc), users may also use Custom Attributes in order to store any information.  

|Data Type|Braze Usage|
|----|---|
|Location|Only data that is configured to go to us.|
|Personal info|Only data that is configured to go to us.|
|Financial info|Only data that is configured to go to us.|
|Health and fitness|Only data that is configured to go to us. ENCOURAGE HIPAA SERVER?|
|Messages|Only data that is configured to go to us.  NOTE: Braze may generate In-App Messages and Push notification that are sent to users.|
|Photos and videos|No.|
|Audio files|No.|
|Files and docs|No.|
|Calendar events|Only data that is configured to go to us.|
|Contacts|Only data that is configured to go to us.|
|App activity|Only data that is configured to go to us.|
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