---
nav_title: Data protection technical assistance
article_title: Data Protection Technical Assistance in the Braze Services
page_order: 1
description: "This page provides technical instructions to enable you to manage, through the Braze Services, requests from individuals in relation to their personal data rights."
alias: /help/dp-technical-assistance/
permalink: /dp-technical-assistance/
hide_toc: true
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Data Protection Technical Assistance in the Braze Services

There are a range of data protection laws that regulate what organizations can do with personal data (“Data Protection Laws”), including the EU and UK General Data Protection Regulation (“GDPR”), the California Consumer Privacy Act (“CCPA”) and the Health Insurance Portability and Accountability Act (“HIPAA”). There are other national, state, and industry-specific Data Protection Laws and regulations that may apply to your business.

These Data Protection Laws grant individuals ‘privacy rights’ over their personal data. Organizations are required to receive and respond to requests from individuals who exercise their privacy rights. The Braze Services can assist you in your compliance with these Data Protection Laws by providing features to facilitate certain actions required under such laws. This document provides technical instructions to use these features to manage privacy rights requests. It is up to you to determine which Data Protection Laws apply to your business, and to act in compliance with them.

{% alert important %}
The Braze recommendations on this page do not apply to BrazeAI Decisioning Studio™. To manage any privacy rights requests relating to personal data in BrazeAI Decisioning Studio™, contact your account manager.
{% endalert %}

## Legal Disclaimer

None of the following is intended to be, nor shall it be deemed to be, legal advice by Braze. You are advised to seek the advice of your own counsel with respect to your particular situation and how Data Protection Laws apply to you and your use of the Braze Services.

## Terminology

For the purposes of this document, any reference to personal data may also be understood as a reference to personal information or personally identifiable information (“Personal Data”). For simplicity’s sake, we generally rely on the language of the GDPR when addressing the rights of end users. The language of the GDPR is often interchangeable or closely aligned with a defined term or concept from other Data Protection Laws.

## The Basics

Most privacy laws define three primary stakeholders who are involved in the processing of Personal Data: data subjects, data controllers, and data processors. Each group has different rights and responsibilities regarding the use of Personal Data:

- A data subject is an individual whose Personal Data is being processed by the data processor or data controller
- A data controller is an entity that determines the purposes and means of the processing of Personal Data
- A data processor is an entity that processes Personal Data on behalf and on the instructions of the data controller

In relation to the Braze Services:

- The data subjects are, for example, the end users of your customer application (e.g., your customers/clients) or your employees who are dashboard users in your instance of the Braze Services.
- You, the Braze customer, are the data controller who decides how and why the Personal Data of the data subjects will be collected and processed within the Braze Services.
- Braze is a data processor who processes Personal Data in the Braze Services on your behalf and in accordance with the instructions that we receive from you.

The above are GDPR terms, but for example, comparable terms under the CCPA are:

- “consumers” for data subjects.
- “businesses” for data controllers.
- “service providers” for data processors.

You will find below relevant information on the most common privacy rights requests from data subjects, including how you can respond to them through the Braze Service's technical features.

## The Right to Be Informed

The right to be informed encompasses your obligation to provide ‘fair processing information,’ typically through a privacy notice. It emphasizes the need for transparency over how you use Personal Data.

### Braze Recommendation

Most Data Protection Laws emphasize the need for transparency in connection with how you use Personal Data. This is the responsibility of the data controllers, who will typically maintain a privacy notice that is easily accessible to users of their products and services and covers the processing done by Braze.

## The Right of Access

Under Data Protection Laws, data subjects may have the right to obtain:

- Confirmation that their Personal Data is being processed,
- Access to their Personal Data, and
- Other supplementary information as determined by the applicable Data Protection Law.

### Braze Recommendation

In order to provide Personal Data from Braze in a machine-readable format in response to a data subject’s access request, you may export their end user Profile by making an API call to Braze’s [REST APIs](https://www.braze.com/docs/api/endpoints/export/#user-export) with either their user identifier (defined by you as the `external_id` provided to Braze) and/or their device identifier.

## The Right to Rectification

Individuals are entitled to have Personal Data corrected if it is inaccurate or incomplete. If you have disclosed the Personal Data in question to third parties, you may consider the necessity to inform them of the rectification where possible.

### Braze Recommendation

In the event that a Data Subject requests that you rectify inaccuracies within the Personal Data being processed by you or by Braze on your behalf, you can use the Braze SDKs or the Braze [REST APIs](https://www.braze.com/docs/api/endpoints/user_data/#user-track-endpoint) to correct such Personal Data.

## The Right to Erasure

The right to erasure is also known as 'the right to be forgotten' or 'right to be deleted.'

### Braze Recommendation

#### Standard Deletion 

Once you have halted data collection, you can use [Braze’s User Deletion REST API endpoint](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/) to delete an end user, which will remove all records of such end user from the Braze Services:

- For end users who have an external_id within the Braze Services, you can use that ID to delete that end user’s data.
- For anonymous end users who do not have an external_id within the Braze Services, you can retrieve that end user’s device identifier using the Braze SDK and can use the device identifier to find the end user profile associated with that device. You can then use the User Deletion API to delete the profile associated with that end user.

Deleting an end user from the Braze Services will permanently delete Braze’s centralized User Profile for that end user as defined by the `external_id` provided. This includes structured profile information that Braze collected by default or that you configured the Braze Services to collect, such as device information, country, language, and email address.

Note that the email address or phone number associated with the end user’s profile could still be stored by Braze, as they could be associated with another end user’s profile. Email addresses and phone numbers are not unique in the Braze Services. This means your team could have configured Braze to store the same email address or phone number on multiple user profiles. If your team has configured Braze in this way, be aware that you may need to delete all user profiles which represent a given data subject in order to comply with a request for deletion from a data subject, and your team would need to make multiple API calls to delete all the User Profiles that refer to a particular data subject.

#### Additional Deletion Considerations

<style>
#considerations td {
    word-break: break-word;
    width: 100%;
    font-size: 16px;
}
</style>

<table id="considerations">
<tbody>
  <tr>
    <td>
        <p>Customers can create custom fields for event properties and message extras. These fields are not intended for personal data, as a result these fields are not included in the default deletion process described above. If, however, you use Braze to enter or collect personal data through event properties and message extras, you can set up the deletion process triggered by the User Deletion REST API endpoint to also include these fields, so the data contained in these fields will be deleted too.</p>
        <p>Default settings are applied at the company level but you can elect to delete the following fields when the delete process runs, at the app group/workspace level:</p>
    <ul>
        <li>PROPERTIES for USERS_BEHAVIORS_CUSTOMEVENT</li>
        <li>PROPERTIES for USERS_BEHAVIORS_PURCHASE</li>
        <li>MESSAGE_EXTRAS for:</li>
            <ul>
            <li>USERS_MESSAGES_CONTENTCARD</li>
            <li>USERS_MESSAGES_EMAIL_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_RETRYSEND_SHARED</li>
            <li>USERS_MESSAGES_WEBHOOK_SEND</li>
            <li>USERS_MESSAGES_SMS_SEND</li>
            <li>Future message send events</li>
            </ul>
    </ul>
    <p>Settings for this may be accessed via <b>Company Settings</b> > <b>Admin Settings</b> > <b>Security Settings</b>. Data deletion preferences are set per event type or category. Only a user with Administrator preferences can make changes to these settings. Alternatively, an Administrator can delegate these permissions to another user.</p>
    <p>If an event type or message extra is set to be included in the deletion process, the data in this field will be deleted going forward for users for whom you’re running a User Delete REST API Endpoint. In addition, when you select this deletion preference, at the next scheduled deletion job, data from these fields will be deleted from any existing anonymised data sets that contain these fields. Restoring the deleted data fields will not be possible.</p>
    </td>
  </tr>
</tbody>
</table>

#### Analytics

In order to maintain the integrity of campaign and application usage analytics, anonymous aggregated data will not be modified when an end user is deleted. For example, Braze will not decrement an app’s total number of sessions when an end user is deleted. The session(s) when such end user visited the app will still be included in the total number of visits to that app, but that data will not be connected in any way to the profile of the forgotten end user, ensuring that this anonymized and aggregated data cannot be tied back to an individual end user.

Analytics within the Braze Services are tied to the Braze end user Identifier. After the end user’s profile has been deleted, the Braze User Identifier effectively becomes a completely anonymized identifier, as Braze is unable to tie it back to any individual end user.

#### Once Deletion has Happened

You are generally expected to make reasonable efforts to notify data subjects when you have complied with their request to erase their Personal Data. A deleted end user may re-register or re-engage with your app or service at a later date, and Braze will not be able to identify them as the deleted or forgotten user. The Braze Services are not able to create lists of deleted user identifiers or email addresses on your behalf.

## The Right to Restriction of Processing

Data subjects may have the right to ‘block’ or suppress the processing of their Personal Data in certain circumstances. Restricting processing means not carrying out any processing that a data subject has objected to.

### Braze Recommendation

The Braze Services do not support the restriction of processing of individual categories of Personal Data. If you have been asked by a data subject to restrict processing of certain subsets of that data subject’s Personal Data, you should use the [Braze APIs](https://www.braze.com/docs/api/home/) to export that end user’s entire profile(s) and then [delete](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint) it from Braze. Braze’s APIs can be used to re-import this data in the event that the end user subsequently allows you to process those particular subsets of its Personal Data. In addition, you should recommend that your end user uninstall or logout from any and all of your Applications that use the Braze SDK to stop collecting any additional data on the data subject.

## The Right to Data Portability

The right to data portability allows data subjects to obtain and reuse their Personal Data for their own purposes across different services. The Personal Data should be provided in a format that is structured, machine-readable, and commonly used.

### Braze Recommendation

Similar to the Right of Access, you may use the Braze [REST API](https://www.braze.com/docs/api/endpoints/export/#user-export) to export an end user's Personal Data and furnish it to the Data Subject pursuant to their request.

## The Right to Object

Individuals may have the right to object to:

- processing based on legitimate interests or the performance of a task in the public interest/exercise of official authority (including profiling);
- direct marketing (including profiling); and
- processing for purposes of scientific/historical research and statistics.

### Braze Recommendation

Braze provides the ability to mark a User Profile as being unsubscribed from SMS, emails or push notifications via both our [REST APIs](https://www.braze.com/docs/api/home/) and via the [iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/), [Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/), and [Web](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/) SDKs. If you receive objections from Data Subjects to receiving such messages, you can use Braze’s APIs to unsubscribe those end users.

If that is not sufficient, to avoid processing of end user Personal Data by Braze, the end user profile should be deleted in the same manner as specified under the ‘Right to Erasure’.

## Rights Related to Automated Decision Making and Profiling

Some Data Protection Laws prevent, or allow data subjects to opt out of, automated decision-making or profiling in certain circumstances, in particular for decisions that “produce a legal effect or a similarly significant effect on the individual.”

### Braze Recommendation

Braze does not perform any automated profiling or decision-making actions with legal or equivalent ramifications for data subjects. If you believe that your own usage of the Braze Services will have legal or equivalent impacts and you have received an objection to this, you may choose to delete the User Profile in the same manner as under the “Right to Erasure.”

## Targeting Advertising

Under some US state privacy laws, data subjects may object to the use of their Personal Data for targeted advertising purposes.

### Braze Recommendation

When building audiences for the purposes of targeting ads to your data subjects, you should ensure that you have excluded any data subjects who have objected to targeted advertising, for instance, California consumers who have exercised their “Do Not Sell or Share” right under the CCPA.

For more information on how to build audiences to sync with third-party platforms, refer to [Audience sync](https://www.braze.com/docs/partners/canvas_steps).

## The Right to Non-Discrimination 

Data subjects have the right to exercise their privacy rights without discrimination.

### Braze Recommendation

In their use of the Braze Services, customers must ensure that they do not discriminate against data subjects who have exercised their privacy rights. For instance, we recommend that data subjects who have exercised their privacy rights should not be segmented into audiences or otherwise targeted in such a way that could discriminate against them.