---
nav_title: Google Play Privacy Questionnaire
article_title: Answers for Google Play Store Privacy Questions
page_order: 9
platform: 
  - Android
  - FireOS
description: "This article covers how to answer Google Play Privacy questions."
---
<style>
table td {
    word-break: break-word;
}
</style>

# Google Play privacy questionnaire

As of April 2022, Android developers must complete Google Play's [Data safety form][4] to disclose privacy and security practices. This guide provides instructions on how to fill out this new form with information on how Braze handles your app data. 

As the app developer, you are in control of what data you send to Braze. Data received by Braze is processed according to your instructions. This is what Google classifies as a [service provider][3]. 

{% alert important %}
This article provides information related to the data the Braze SDK processes as related to the Google safety section questionnaire. This article is not providing legal advice, so we recommend consulting with your legal team before submitting any information to Google.
{% endalert %}

## Questions

|Questions|Answers for Braze SDK|
|---|---|
|Does your app collect or share any of the required user data types?|Yes, the Braze Android SDK collects data as configured by the app developer. |
|Is all of the user data collected by your app encrypted in transit?|Yes.|
|Do you provide a way for users to request that their data be deleted?|Yes.|

For more information about handling user requests for their data and deletion, see [Braze Data Retention Information][1].

## Data collection

The data collected by Braze is determined by your specific integration and the user data you choose to collect. To learn more about what data Braze collects by default and how to disable certain attributes, see our [SDK data collection options][5].

<table id="datatypes">
    <thead>
        <tr>
            <th width="25%">Category</th>
            <th width="25%">Data type</th>
            <th width="50%">Braze Usage</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="2">Location</td>
            <td>Approximate location</td>
            <td rowspan="15">Not collected by default.</td>
        </tr>
        <tr>
            <td>Precise location</td>
        </tr>
        <tr>
            <td rowspan="9">Personal Info</td>
            <td>Name</td>
        </tr>
        <tr>
            <td>Email address</td>
        </tr>
        <tr>
            <td>User IDs</td>
        </tr>
        <tr>
            <td>Address</td>
        </tr>
        <tr>
            <td>Phone number</td>
        </tr>
        <tr>
            <td>Race and ethnicity</td>
        </tr>
        <tr>
            <td>Political or regligious beliefs</td>
        </tr>
        <tr>
            <td>Sexual orientation</td>
        </tr>
        <tr>
            <td>Other info</td>
        </tr>
        <tr>
            <td rowspan="4">Financial info</td>
            <td>User payment info</td>
        </tr>
        <tr>
            <td>Purchase history</td>
        </tr>
        <tr>
            <td>Credit score</td>
        </tr>
        <tr>
            <td>Other financial info</td>      
        </tr>
        <tr>
            <td rowspan="2">Health and fitness</td>
            <td>Health info</td>
            <td rowspan="2">Not collected by default.</td>
        </tr>
        <tr>
            <td>Fitness info</td>     
        </tr>
        <tr>
            <td rowspan="3">Messages</td>
            <td>Emails</td>
            <td rowspan="2">Not collected by default.</td>
        </tr>
        <tr>
            <td>SMS or MMS</td>          
        </tr>
        <tr>
            <td>Other in-app messages</td>
            <td>If you send In-app messages or push notifications through Braze, we collect information on when users have opened or read these messages.</td>
        </tr>
        <tr>
            <td rowspan="2">Photos and videos</td>
            <td>Photos</td>
            <td rowspan="8">Not collected.</td>
        </tr>
        <tr>
            <td>Videos</td>
        </tr>
        <tr>
            <td rowspan="3">Audio files</td>
            <td>Voice or sound recordings</td>
        </tr>        
        <tr>
            <td>Music files</td>
        </tr>
        <tr>
            <td>Other audio files</td>
        </tr>
        <tr>
            <td>Files and docs</td>
            <td>Files and docs</td>
        </tr>
        <tr>
            <td>Calendar</td>
            <td>Calendar events</td>
        </tr>
        <tr>
            <td>Contacts</td>
            <td>Contacts</td>
        </tr>
        <tr>
            <td rowspan="5">App activity</td>
            <td>App interactions</td>
            <td>Braze collects session activity data by default. All other interactions and activity is determined by your app's custom integration.</td>
        </tr>
        <tr>
            <td>In-app search history</td>
            <td>Not collected.</td>            
        </tr>
        <tr>
            <td>Installed apps</td>
            <td>Not collected.</td>            
        </tr>
        <tr>
            <td>Other user-generated content</td>
            <td rowspan="2">Not collected by default.</td>            
        </tr>
        <tr>
            <td>Other actions</td>
        </tr>
        <tr>
            <td>Web browsing</td>
            <td>Web browsing history</td>
            <td>Not collected.</td>
        </tr>
        <tr>
            <td rowspan="3">App info and performance</td>
            <td>Crash logs</td>
            <td>Braze collects crash logs for errors that occur within the SDK. This contains the user's phone model and OS level, along with a Braze specific user ID.</td>
        </tr>
        <tr>
            <td>Diagnostics</td>
            <td>Not collected.</td>            
        </tr>
        <tr>
            <td>Other app performance data</td>
            <td>Not collected.</td>
        </tr>
        <tr>
            <td>Device or other IDs</td>
            <td>Device or other IDs</td>
            <td>Braze generates a device ID to differentiate users’ devices, and ensure messages are sent to the correct intended device.</td>
        </tr>
    </tbody>
</table>

To learn more about other device data that Braze collects which may fall outside the scope of Google Play's data safety guidelines, see our [Android storage overview][2] and our [SDK data collection options][5].

[1]: https://www.braze.com/docs/api/data_retention/
[2]: https://www.braze.com/docs/developer_guide/platform_integration_guides/android/storage
[3]: https://support.google.com/googleplay/android-developer/answer/10787469?hl=en#zippy=%2Cwhat-kinds-of-activities-can-service-providers-perform
[4]: https://support.google.com/googleplay/android-developer/answer/10787469
[5]: https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#minimum-integration