---
nav_title: GDPR Compliance
page_order: 8
---

# GDPR Compliance

The European Union General Data Protection Regulation (GDPR) is a comprehensive data protection law that governs how entities operating in the EU or targeting products and services to individuals in the EU or monitoring the behavior of EU data subjects handle personal information. The GDPR is intended to provide more personal data privacy protections, in order to protect and empower all EU data subjects in regards to their data privacy and to reshape the way organizations approach data privacy. More information is available at the [EU GDPR homepage](https://www.eugdpr.org/). The GDPR came into force on May 25, 2018.

## GDPR and Your Braze integration

The GDPR defines three primary entities who are involved in the processing of personal data: Data Controllers, Data Subjects, and Data Processors. Each group has different roles and requirements regarding their interactions with customer personal data:

* A _Data Subject_ is an end user whose personal data is being processed by the Data Processor on behalf of the Data Controller.
* A _Data Controller_ is the entity that determines the purposes and means of the processing of personal data.
* A _Data Processor_ is an entity which processes personal data on behalf and on the instructions of the controller (i.e., a service provider such as Braze).

In relation to the Braze Services:

* The Data Subjects are the end users, customers or other individuals who provide their personal data to you.
* You are the Data Controller who decides how and why the personal data of the Data Subjects will be processed.
* Braze is a Data Processor who processes personal data on your behalf and in accordance with the instructions that we receive from you.

This page outlines the ways that the Braze Services enable customers to fulfill their responsibilities as Data Controllers under GDPR in connection with their use of the Braze Services.

## Legal Disclaimer

As a Data Controller, you are required by the GDPR to enable end users from whom you have collected personal data to exercise numerous rights, each described in greater detail below. None of the following is intended to be, nor shall it be deemed to be, legal advice by Braze on how to comply with GDPR. You are advised to seek the advice of your own counsel with respect to our particular situation and how GDPR applies to you and your use of the Braze Services. You can find the [full GDPR text here](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2016.119.01.0001.01.ENG&toc=OJ:L:2016:119:TOC).

## The Right to Be Informed

The right to be informed encompasses your obligation to provide ‘fair processing information’, typically through a privacy notice. It emphasizes the need for transparency over how you use personal data.

### Braze Recommendation

Under GDPR, Braze customers, as Data Controllers, must enable Data Subjects to understand how they will process any personal data that they collect. Many Data Controllers fulfill this obligation through a privacy notice on their website. The GDPR emphasizes the need for transparency in connection with how you use personal data. *This is the responsibility of the Data Controller.* Accordingly, you should maintain a privacy policy that is easily accessible to users of your products and services. Additionally, your Privacy Policy should also disclose that you may share personal data with third parties who may process that personal data on your behalf, and provide sufficient disclosure about that processing so that the Data Subject is informed about what you and your Data Processors will be doing with personal data.

## The Right of Access by the Data Subject

Under GDPR, individuals have the right to obtain:

* Confirmation that their data is being processed,
* Access to their personal data, and
* Other supplementary information – this largely corresponds to the information that should be provided in a privacy notice (see [GDPR Article 15](https://gdpr-info.eu/art-15-gdpr/)).

### Braze Recommendation

The Braze Services can be configured to access an end user’s User Identifier (defined by you) and/or  device identifier. You may use either of these identifiers to export an end user Profile containing personal data from Braze’s [REST APIs]({{ site.baseurl }}/developer_guide/rest_api/export/#user-export), and to provide such personal data to a Data Subject in response to their request to access any personal data being processed by Braze as a Data Processor on your behalf.

For example, you can export a user's [user identifier]({{ site.baseurl }}/user_guide/data_and_analytics/user_data_collection/#user-profile-lifecycle) or device identifier, and your support team can then make an API call (or use a system that makes API calls) to retrieve and furnish the personal data stored by Braze to a given Data Subject.

## The Right to Rectification

Individuals are entitled to have personal data rectified if it is inaccurate or incomplete. If you have disclosed the personal data in question to third parties, you must inform them of the rectification where possible.

### Braze Recommendation

In the event that a Data Subject requests that you rectify inaccuracies within the personal data being processed by you or by Braze on your behalf,  you can use the Braze SDKs or the Braze [REST APIs]({{ site.baseurl }}/developer_guide/rest_api/user_data/#user-track-endpoint) to correct such personal data.

## The Right to Erasure

The right to erasure is also known as 'the right to be forgotten'.

### Braze Recommendation

Braze offers two solutions to stop additional processing of data by Braze:

* The Braze SDKs allow customers to disable all Braze operations. This will prevent all data from being sent to Braze from that website or application. The Braze Documentation provides detailed instructions on how to disable the SDK on the platform-specific documentation pages ([iOS]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/initial_sdk_setup/), [Android]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/), and [Web]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)).
* Alternatively, you can recommend that your Users uninstall or logout from any and all of your Applications that use the Braze SDK.

Once you have halted data collection, you can use Braze’s [User Deletion REST API endpoint]({{ site.baseurl }}/developer_guide/rest_api/user_data/#user-delete-endpoint) to delete an end user, which will remove all records of such end user from the Braze’s Services:

* For Users who have an `external_id` within the Services, you can use that ID to delete that end user’s data.
* For anonymous end users who do not have an external_id within the Services, you  can retrieve that end user’s device identifier using the Braze SDK and can use the device identifier to find the end user profile associated with that device. You can then use the [User Deletion API]({{ site.baseurl }}/developer_guide/rest_api/user_data/#user-delete-endpoint) to delete the profile associated with that end user.

Under GDPR, You must make reasonable efforts to notify Data Subjects when you have complied with their request to erase their personal data.

Braze will not be able to identify if a deleted (or 'forgotten') end user subsequently attempts to log into or re-register with your app or service.  To address this,  you may [disable login or] seek to  obtain positive confirmation that the end user consents to processing of their personal data. The Braze Services are not able to create blacklists of user identifiers or email addresses on behalf of customers.

Deleting an end user's data will erase person data from Braze. In order to maintain the integrity of campaign and application usage analytics, anonymous aggregated data will not be modified when an end user is deleted (for example, Braze will not decrement an app's total number of sessions when an end user is deleted.  The session(s) when such end user visited the app will still be included in the total number of visits to that app, but that data will not be connected in any way to the profile of the forgotten end user, ensuring that this anonymized and aggregated data cannot be tied back to an individual end user.

## Deletion Details

Deleting an end user from the Braze Services will _permanently_ delete Braze's centralized User Profile for that end user. This includes all personal data, including structured profile information, that Braze collected automatically or that you configured the Braze Services to collect, such as device information, country, language and email address.

Analytics within the Braze Services are tied to the Braze end user Identifier. Once the end user’s profile has been deleted, the Braze User Identifier effectively becomes a completely anonymized identifier, as Braze is unable to tie it back to any individual end user.

## The Right to Restriction of Processing

Data Subjects have the right to ‘block’ or suppress processing of certain subsets of their personal data in the event of inaccurate or improperly obtained data. When processing is restricted, you are permitted to store the personal data, but not further process it. You can retain just enough information about the individual to ensure that the restriction is respected in future.

### Braze Recommendation

The Braze Services do not support restriction of processing of individual categories of personal data. If you have been asked by a Data Subject to restrict processing of certain subsets of that Data Subjects’ personal data, you should use the [Braze APIs](https://www.braze.com/documentation/REST_API/#user-export) to export that end user’s entire profile and then [delete]({{ site.baseurl }}/developer_guide/rest_api/user_data/#user-delete-endpoint) it from Braze. Braze’s APIs can be used to re-import this data in the event that the end user allows you to process those particular subsets of its personal data.

## The Right to Data Portability

The right to data portability allows individuals to obtain and reuse their personal data for their own purposes across different services.

### Braze Recommendation

Similar to the Right of Access, you may use the Braze [REST API]({{ site.baseurl }}/developer_guide/rest_api/export/#user-export) to export an end user's personal data and furnish it to the Data Subject pursuant to his/her request.

## The Right to Object

Individuals have the right to object to:

* processing based on legitimate interests or the performance of a task in the public interest/exercise of official authority (including profiling);
* direct marketing (including profiling); and
* processing for purposes of scientific/historical research and statistics.

### Braze Recommendation

Braze provides the ability to mark a User Profile as being unsubscribed from emails or push notifications via both our [REST APIs]({{ site.baseurl }}/developer_guide/Platform_Integration_Guides/Android/Analytics/Setting_Custom_Attributes/#setting-a-custom-attribute-via-the-rest-api) and via the [iOS]({{ site.baseurl }}/developer_guide/Platform_Integration_Guides/Xamarin/iOS/Analytics/Setting_Custom_Attributes/), [Android]({{ site.baseurl }}/developer_guide/Platform_Integration_Guides/React_Native/Android_and_FireOS/Analytics/Attribute_Tracking/#setting-custom-attributes), and [Web]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/) SDKs. Customers who receive objections from Data Subjects to receiving such messages can use Braze’s APIs to unsubscribe those end users.

If that is not sufficient, to avoid processing of end user Personal Data by Braze, the end user profile should be deleted in the same manner as specified under the 'Right to Erasure'.

## Rights Related to Automated Decision Making and Profiling

The GDPR prevents automated decision-making without human intervention in certain circumstances, in particular for decisions that "produce a legal effect or a similarly significant effect on the individual."

### Braze Recommendation

Braze does not perform any automated profiling or decision making actions with legal or equivalent ramifications for end users. If you believe that your own usage of the Braze platform will have legal or equivalent impacts based upon your own usage, you may choose to delete the User Profile in the same manner as under the “Right to Erasure.”
