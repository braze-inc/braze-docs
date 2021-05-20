---
nav_title: Data Protection Technical Assistance
page_order: 8
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Data Protection Technical Assistance

In recent years there has been a range of new data protection laws that regulate what organizations can do with personal data (__Data Protection Laws__), including the European Union General Data Protection Regulation (__GDPR__), the California Consumer Privacy Act (__CCPA__) along with more established laws like the Health Insurance Portability and Accountability Act (__HIPAA__). There are other national, state, and industry-specific Data Protection Laws and regulations that may apply to your business.

The Braze Platform can assist you in your compliance with these Data Protection Laws by providing technical features to facilitate certain actions required under such laws. It is up to each customer to determine which Data Protection Laws apply to their business, and to act in compliance with them. 

This document provides technical instructions to enable you to manage, through the Braze Platform, requests from individuals in relation to their personal data rights.

For the purposes of this document, any reference to personal data may also be understood as a reference to personal information or personally identifiable information (__Personal Data__). In the interests of simplicity, we rely on the language of the GDPR when explaining the rights of end users and how you may facilitate these. The language of the GDPR is often interchangeable or closely aligned with a defined term or concept from other Data Protection Laws. For example, the section below on “The Right To Erasure” may be equated with the “Right to Delete” under the CCPA.  

## Legal Disclaimer

None of the following is intended to be, nor shall it be deemed to be, legal advice by Braze on how to comply with the GDPR, CCPA, or applicable Data Protection Laws. You are advised to seek the advice of your own counsel with respect to your particular situation and how Data Protection Laws apply to you and your use of the Braze Services.

## The Basics

Most privacy laws define three primary stakeholders who are involved in the processing of Personal Data: Data Subjects, Data Controllers, and Data Processors. Each group has different rights and responsibilities regarding the use of Personal Data:
- A Data Subject is an individual whose Personal Data is being processed by the Data Processor or Data Controller
- A Data Controller is the entity that determines the purposes and means of the processing of Personal Data
- A Data Processor is an entity that processes Personal Data on behalf and on the instructions of the Data Controller

In relation to the Braze Platform:
- The Data Subjects are for example the end users of your customer application (e.g., your customers/clients) or your employees who are dashboard users in your instance of the Braze Platform. 
- You, the Braze customer, are the Data Controller who decides how and why the Personal Data of the Data Subjects will be collected and processed.
- Braze is a Data Processor who processes Personal Data on your behalf and in accordance with the instructions that we receive from you.

The above are GDPR terms, but for example, comparable terms under the CCPA are:
- “Consumers” for Data Subjects.
- “Businesses” for Data Controllers. 
- “Service Providers” for Data Processors.

As a Data Controller, you may be required by applicable Data Protection Laws to enable Data Subjects to exercise numerous rights, each described in greater detail below.

## The Right to Be Informed

The right to be informed encompasses your obligation to provide ‘fair processing information,’ typically through a privacy notice. It emphasizes the need for transparency over how you use Personal Data.

### Braze Recommendation
Under certain Data Protection Laws, Braze customers, as Data Controllers, must enable Data Subjects to understand how they will process any Personal Data that they collect. Many Data Controllers fulfill this obligation through a privacy notice on their website. Most Data Protection Laws will emphasize the need for transparency in connection with how you use Personal Data. This is the responsibility of the Data Controller. Accordingly, you should maintain a privacy notice that is easily accessible to users of your products and services. Additionally, your privacy notice should also disclose that you may share Personal Data with third parties who may process that Personal Data on your behalf, and provide sufficient disclosure about that processing so that the Data Subject is informed about what you and your Data Processors will be doing with Personal Data.

## The Right of Access 

Under certain Data Protection Laws, individuals may have the right to obtain:
- Confirmation that their Personal Data is being processed,
- Access to their Personal Data, and
- Other supplementary information – this largely corresponds to the information that should be provided in a privacy notice.

### Braze Recommendation

The Braze Services can be configured to access an end user’s User Identifier (defined by you as the external_id provided to Braze) and/or device identifier. You may use either of these identifiers to export an end user Profile containing Personal Data from Braze’s [REST APIs](https://www.braze.com/docs/api/endpoints/export/#user-export), and to provide such Personal Data to a Data Subject in response to their request to access any Personal Data being processed by Braze as a Data Processor on your behalf.

For example, you can export an end user’s [User Identifier](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-profile-lifecycle) or device identifier, and your support team can then make an API call (or use a system that makes API calls) to retrieve and furnish the Personal Data stored by Braze to a given Data Subject.

## The Right to Rectification

Individuals are entitled to have Personal Data corrected if it is inaccurate or incomplete. If you have disclosed the Personal Data in question to third parties, you must inform them of the rectification where possible.

### Braze Recommendation

In the event that a Data Subject requests that you rectify inaccuracies within the Personal Data being processed by you or by Braze on your behalf, you can use the Braze SDKs or the Braze [REST APIs](https://www.braze.com/docs/api/endpoints/user_data/#user-track-endpoint) to correct such Personal Data.

## The Right to Erasure

The right to erasure is also known as ‘the right to be forgotten’ or ‘right to be deleted.’

### Braze Recommendation

Braze offers two solutions to stop additional processing of data by Braze:
- The Braze SDKs allow customers to disable all Braze operations. This will prevent all data from being sent to Braze from that website or application. The Braze Documentation provides detailed instructions on how to disable the SDK on the platform-specific documentation pages ([iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/), [Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/), and [Web](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/initial_sdk_setup/)).
- Alternatively, you can recommend that your end user uninstall or logout from any and all of your Applications that use the Braze SDK.

Once you have halted data collection, you can use Braze’s [User Deletion REST API endpoint](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint) to delete an end user, which will remove all records of such end user from the Braze’s Services:
- For end users who have an `external_id` within the Services, you can use that ID to delete that end user’s data.
- For anonymous end users who do not have an external_id within the Services, you can retrieve that end user’s device identifier using the Braze SDK and can use the device identifier to find the end user profile associated with that device. You can then use the [User Deletion API](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint) to delete the profile associated with that end user.

Deleting an end user from the Braze Services will _permanently_ delete Braze’s centralized User Profile for that end user as defined by the external_id provided. This includes all Personal Data, including structured profile information, that Braze collected by default or that you configured the Braze Services to collect, such as device information, country, language, and email address. 

Note that the email address or phone number associated with the end user’s profile could still be stored by Braze, as they could be associated with other end user’s profile. Email addresses and phone numbers are not unique in the Braze Services. This means your team could have configured Braze to store the same email address or phone number on multiple user profiles. If your team has configured Braze in this way, be aware that you may need to delete all user profiles which represent a given Data Subject in order to comply with a request for deletion from a Data Subject, and your team would need to make multiple API calls to delete all the User Profiles that refer to a particular Data Subject.

#### Analytics

In order to maintain the integrity of campaign and application usage analytics, anonymous aggregated data will not be modified when an end user is deleted. For example, Braze will not decrement an app’s total number of sessions when an end user is deleted. The session(s) when such end user visited the app will still be included in the total number of visits to that app, but that data will not be connected in any way to the profile of the forgotten end user, ensuring that this anonymized and aggregated data cannot be tied back to an individual end user.

Analytics within the Braze Services are tied to the Braze end user Identifier. Once the end user’s profile has been deleted, the Braze User Identifier effectively becomes a completely anonymized identifier, as Braze is unable to tie it back to any individual end user.

#### Once deletion has happened

You are generally expected to make reasonable efforts to notify Data Subjects when you have complied with their request to erase their Personal Data.
A deleted end user may re-register or re-engage with your app or service at a later date and Braze will not be able to identify them as the deleted or forgotten user. The Braze Services are not able to create lists of deleted user identifiers or email addresses on behalf of customers. 

## The Right to Restriction of Processing

Data Subjects may have the right to ‘block’ or suppress the processing of certain subsets of their Personal Data in the event of inaccurate or improperly obtained data. When processing is restricted, you are permitted to store the Personal Data, but not further process it. You can retain just enough information about the individual to ensure that the restriction is respected in the future.

### Braze Recommendation

The Braze Services do not support the restriction of processing of individual categories of Personal Data. If you have been asked by a Data Subject to restrict processing of certain subsets of that Data Subject’s Personal Data, you should use the [Braze APIs](https://www.braze.com/docs/api/basics/) to export that end user’s entire profile(s) and then [delete](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint) it from Braze. Braze’s APIs can be used to re-import this data in the event that the end user subsequently allows you to process those particular subsets of its Personal Data.

## The Right to Data Portability

The right to data portability allows Data Subjects to obtain and reuse their Personal Data for their own purposes across different services. The Personal Data should be provided in a format that is structured, machine-readable, and commonly used. 

### Braze Recommendation

Similar to the Right of Access, you may use the Braze [REST API](https://www.braze.com/docs/api/endpoints/export/#user-export) to export an end user’s Personal Data and furnish it to the Data Subject pursuant to their request.

## The Right to Object

Individuals may have the right to object to:
- processing based on legitimate interests or the performance of a task in the public interest/exercise of official authority (including profiling);
- direct marketing (including profiling); and
- processing for purposes of scientific/historical research and statistics.

### Braze Recommendation

Braze provides the ability to mark a User Profile as being unsubscribed from SMS, emails or push notifications via both our [REST APIs](https://www.braze.com/docs/api/basics/) and via the [iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/), [Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/), and [Web](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/) SDKs. If you receive objections from Data Subjects to receiving such messages, you can use Braze’s APIs to unsubscribe those end users.

If that is not sufficient, to avoid processing of end user Personal Data by Braze, the end user profile should be deleted in the same manner as specified under the ‘Right to Erasure’.

## Rights Related to Automated Decision Making and Profiling

Certain Data Protection Laws prevent automated decision-making without human intervention in certain circumstances, in particular for decisions that “produce a legal effect or a similarly significant effect on the individual.”

### Braze Recommendation

Braze does not perform any automated profiling or decision making actions with legal or equivalent ramifications for end users. If you believe that your own usage of the Braze Platform will have legal or equivalent impacts based upon your own usage and you have received an objection to this, you may choose to delete the User Profile in the same manner as under the “Right to Erasure.”



