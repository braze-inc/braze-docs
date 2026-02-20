## Phase 1 Complete — Prioritized Backlog

**Total tickets parsed:** 89
**Actionable:** 65 | **Sensitive (skip):** 20 | **Support-Only (skip):** 4
**CSV matches:** 48 of 65 actionable tickets can be auto-drafted
**Ready to draft:** 48 | **Partial:** 11 | **Not ready:** 6

### Skipped Tickets (24)

| Ticket | Summary | Category | Team |
|--------|---------|----------|------|
| BD-4005 | HTTP 400 Bad Request error thrown in a webhook campaign. Wha... | Sensitive | Ingestion |
| BD-4021 | Successful Response From /users/delete or users/merge Endpoi... | Sensitive | Core Objects |
| BD-4048 | Deep Links on Android Not Working | Support-Only | SDKs |
| BD-4053 | Cloud Data Ingestion - Users Not Ingested/Imported By Braze | Sensitive | Datalake |
| BD-4063 | How do I Change the Data Type of a Custom Attribute? | Sensitive | Core Objects |
| BD-4085 | How Braze handles identifying an anonymous user as a NEW use... | Sensitive | Core Objects |
| BD-4114 | Missing Stats for Content Cards Campaigns | Sensitive | Content Cards |
| BD-4173 | Knowledge What is the Liquid for Templating in a Date/Time i... | Sensitive | Composition Infrastructure |
| BD-4202 | Knowledge How are Custom Event Property Values handled? | Sensitive | Core Objects |
| BD-4203 | What is the Difference Between a Full Sync and a Partial Syn... | Sensitive | SDKs |
| BD-4224 | What is the difference between Push Enabled and Background P... | Sensitive | Content Cards |
| BD-4225 | Test Push With Users That Have Multiple Devices | Sensitive | Content Cards |
| BD-4247 | Setting Custom Attribute as "" (blank) vs. null | Sensitive | Ingestion |
| BD-4253 | Deep Links Stripped in Gmail | Support-Only | SDKs |
| BD-4270 | How We Automatically Determine a User's Country | Sensitive | SDKs |
| BD-4279 | Can Content Cards Have an Expiry Longer than 30 Days | Support-Only | Content Cards |
| BD-4293 | SDK Is Not Updating User's Language And Country | Sensitive | SDKs |
| BD-4298 | Testing Content Cards in an iOS App | Support-Only | SDKs |
| BD-4311 | API Response: Access Denied | Sensitive | Ingestion |
| BD-4404 | Testing IAMs and Content Cards on Session Start for Web in C... | Sensitive | SDKs |
| BD-4466 | A Custom Event or Purchase Event is not logging in Braze | Sensitive | Core Objects |
| BD-4516 | Assign vs Capture Liquid Tags | Sensitive | Composition Infrastructure |
| BD-4529 | Targeting a Non-Existent User via API | Sensitive | Core Objects |
| BD-4652 | Nested Array Custom Attribute Segmentation Filters Not Worki... | Sensitive | Ingestion |

### Tickets Targeting Same Doc (can be batched)

- **`NEEDS MANUAL TARGET`** (10 tickets): BD-4514, BD-4476, BD-4424, BD-4385, BD-4370, BD-4369, BD-4269, BD-4138, BD-4075, BD-4036
- **`_docs/_user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users.md`** (2 tickets): BD-4591, BD-4144
- **`_docs/_developer_guide/sdk_integration.md`** (2 tickets): BD-4579, BD-4349
- **`_docs/_user_guide/message_building_by_channel/webhooks/creating_a_webhook/.md (NOT FOUND)`** (2 tickets): BD-4352, BD-4234
- **`_docs/_user_guide/data/user_data_collection/user_import/.md (NOT FOUND)`** (2 tickets): BD-4321, BD-4171
- **`_docs/_developer_guide/platforms/web/google_tag_manager/.md (NOT FOUND)`** (2 tickets): BD-4318, BD-4099

### Prioritized Actionable Backlog

| Rank | Ticket | Summary | Category | Priority | Team | Assignee (GH) | Target Doc | CSV Match | Ready |
|------|--------|---------|----------|----------|------|----------------|------------|-----------|-------|
| 1 | BD-4036 | Users Not Logging Sessions | Docs Gap | P2 | SDKs | zairro | `NEEDS MANUAL TARGET` | Yes | Yes |
| 2 | BD-4068 | User Profile Attribute "Language" | Docs Gap | P2 | Core Objects | rachel-feinberg | `_user_guide/data/user_data_collection/sdk_data_col` | Yes | Yes |
| 3 | BD-4075 | ChangeUser() SDK method FAQ | Docs Gap | P2 | SDKs | zairro | `NEEDS MANUAL TARGET` | Yes | Yes |
| 4 | BD-4078 | What is the minimum time interval between triggers for ... | Docs Gap | P2 | SDKs | zairro | `_developer_guide/platforms/android/in_app_messages` | Yes | Yes |
| 5 | BD-4080 | Formatting for DateTime datatype? | Docs Gap | P2 | Core Objects | rachel-feinberg | `_api/objects_filters/user_attributes_object.md` | Yes | Yes |
| 6 | BD-4099 | Custom Event Not Logging in Braze via Google Tag Manage... | Docs Gap | P2 | SDKs | zairro | `_developer_guide/platforms/web/google_tag_manager/` | Yes | Yes |
| 7 | BD-4138 | When might a user have 0 sessions recorded against thei... | Docs Gap | P2 | Ingestion | rachel-feinberg | `NEEDS MANUAL TARGET` | Yes | Yes |
| 8 | BD-4171 | How do I update Custom Attribute data types via CSV? | New Content | P2 | Ingestion | rachel-feinberg | `_user_guide/data/user_data_collection/user_import/` | Yes | Yes |
| 9 | BD-4174 | How is a Content Card's Expiration (Time In Feed) Calcu... | Docs Gap | P2 | Content Cards | lydia-xie | `_user_guide/message_building_by_channel/content_ca` | Yes | Yes |
| 10 | BD-4201 | Clicking on Push Notification Doesn't Open the App | Docs Gap | P2 | SDKs | zairro | `_user_guide/message_building_by_channel/push.md` | Yes | Yes |
| 11 | BD-4234 | How do I use the spacer.gif resource? | Docs Gap | P2 | Content Cards | lydia-xie | `_user_guide/message_building_by_channel/webhooks/c` | Yes | Yes |
| 12 | BD-4259 | Invalid API Key | Docs Gap | P2 | Ingestion | rachel-feinberg | `_api/errors.md` | Yes | Yes |
| 13 | BD-4278 | Limitations for Catalog | Docs Gap | P2 | Core Objects | rachel-feinberg | `_user_guide/personalization_and_dynamic_content/ca` | Yes | Yes |
| 14 | BD-4280 | In-App Message Impression Failure Error in Event User L... | Docs Gap | P2 | Ingestion | rachel-feinberg | `_user_guide/administrative/app_settings/event_user` | Yes | Yes |
| 15 | BD-4281 | How to find an anonymous user in the Web SDK | Docs Gap | P2 | SDKs | zairro | `_developer_guide/home.md` | Yes | Yes |
| 16 | BD-4282 | API rate Limit - Rolling Hour or Hourly Basis | Docs Gap | P2 | Ingestion | rachel-feinberg | `_api/basics.md` | Yes | Yes |
| 17 | BD-4290 | How are Currency Exchange Rates Calculated for the Braz... | Docs Gap | P2 | Ingestion | rachel-feinberg | `_user_guide/data/custom_data/purchase_events/.md (` | Yes | Yes |
| 18 | BD-4299 | Multiple IAMs Display In The Same Session if They Are B... | Docs Gap | P2 | SDKs | zairro | `_user_guide/message_building_by_channel/in-app_mes` | Yes | Yes |
| 19 | BD-4304 | API Success Message Received But No Message Delivered | Docs Gap | P2 | Ingestion | rachel-feinberg | `_api/errors/.md (NOT FOUND)` | Yes | Yes |
| 20 | BD-4307 | Slowness in Displaying Action-Based Content Cards | Docs Gap | P2 | Content Cards | lydia-xie | `_user_guide/message_building_by_channel/content_ca` | Yes | Yes |
| 21 | BD-4318 | How to Integrate a Web App With GTM (Google Tag Manager... | Docs Gap | P2 | SDKs | zairro | `_developer_guide/platforms/web/google_tag_manager/` | Yes | Yes |
| 22 | BD-4321 | User Import - CSV File Download Window | Docs Gap | P2 | Ingestion | rachel-feinberg | `_user_guide/data/user_data_collection/user_import/` | Yes | Yes |
| 23 | BD-4334 | Are GIF's Supported in Android? | Docs Gap | P2 | SDKs | zairro | `_user_guide/message_building_by_channel/push/best_` | Yes | Yes |
| 24 | BD-4349 | Push Issues Within mParticle Kit Integration (iOS) | Docs Gap | P2 | SDKs | zairro | `_developer_guide/sdk_integration.md` | Yes | Yes |
| 25 | BD-4350 | Identify Endpoint: User Alias not associated successful... | Docs Gap | P2 | Ingestion | rachel-feinberg | `_api/endpoints/user_data/post_user_identify.md` | Yes | Yes |
| 26 | BD-4352 | Braze to Braze Webhook > Error: 415 Unsupported Media T... | Docs Gap | P2 | Ingestion | rachel-feinberg | `_user_guide/message_building_by_channel/webhooks/c` | Yes | Yes |
| 27 | BD-4411 | What Could be the Reason for Large Number of Uninstalls... | Docs Gap | P2 | Content Cards | lydia-xie | `_user_guide/analytics/tracking/uninstall_tracking/` | Yes | Yes |
| 28 | BD-4413 | Correctly Sized GIF not Uploading to the Media Library | Docs Gap | P2 | Composition Infrastructure | rachel-feinberg | `_user_guide/engagement_tools/templates_and_media/f` | Yes | Yes |
| 29 | BD-4415 | Add Existing Users to a Subscription Group | Docs Gap | P2 | Ingestion | rachel-feinberg | `_api/endpoints/subscription_groups/post_update_use` | Yes | Yes |
| 30 | BD-4451 | "Open Web URL Inside App" Behaviour - draft mode | Docs Gap | P2 | Content Cards | lydia-xie | `_help/help_articles/push/push_clicks_unexpectedly_` | Yes | Yes |
| 31 | BD-4460 | The Difference Between "Send to Production" and "Send t... | Docs Gap | P2 | Content Cards | lydia-xie | `_user_guide/message_building_by_channel/push/ios_p` | Yes | Yes |
| 32 | BD-4472 | Security Risks Associated with API Key Exposure | Docs Gap | P2 | Ingestion | rachel-feinberg | `_user_guide/administrative/app_settings/api_settin` | Yes | Yes |
| 33 | BD-4480 | How to Set Up SDK Authentication to Prevent Unwanted Re... | Docs Gap | P2 | SDKs | zairro | `_developer_guide/sdk_integration/authentication.md` | Yes | Yes |
| 34 | BD-4502 | Push Notification Titles Appear Correctly on Android bu... | Docs Gap | P2 | Content Cards | lydia-xie | `_user_guide/message_building_by_channel/push/troub` | Yes | Yes |
| 35 | BD-4504 | Liquid Error Occurs On The Dashboard When Previewing So... | Docs Gap | P2 | Composition Infrastructure | rachel-feinberg | `_user_guide/personalization_and_dynamic_content/li` | Yes | Yes |
| 36 | BD-4514 | Testing Nested Custom Attributes and Nested Objects for... | Docs Gap | P2 | Core Objects | rachel-feinberg | `NEEDS MANUAL TARGET` | Yes | Yes |
| 37 | BD-4569 | When do we evaluate the abort logic of an IAM? | Docs Gap | P2 | Composition Infrastructure | rachel-feinberg | `_user_guide/personalization_and_dynamic_content/li` | Yes | Yes |
| 38 | BD-4591 | How To Prevent Tracking Anonymous Users | Docs Gap | P2 | SDKs | zairro | `_user_guide/data/unification/user_data/user_profil` | Yes | Yes |
| 39 | BD-4593 | When Does Braze Log Sends for Content Card Deliveries? | Docs Gap | P2 | Content Cards | lydia-xie | `_help/help_articles/campaigns_and_canvas/know_befo` | Yes | Yes |
| 40 | BD-4595 | Content Card Image Not Rendering / Is Broken Due To Bad... | Docs Gap | P2 | Content Cards | lydia-xie | `_user_guide/message_building_by_channel/content_ca` | Yes | Yes |
| 41 | BD-4597 | How to Log a Custom Event Using GTM (Google Tag Manager... | New Content | P2 | SDKs | zairro | `_developer_guide/sdk_integration/.md (NOT FOUND)` | Yes | Yes |
| 42 | BD-4604 | iOS Universal Links Not Working When ABKURLDelegate Ret... | Docs Gap | P2 | SDKs | zairro | `_user_guide/message_building_by_channel/email/univ` | Yes | Yes |
| 43 | BD-4660 | Why Are React Native Deep Links Not Working? | Docs Gap | P2 | SDKs | zairro | `_developer_guide/push_notifications/.md (NOT FOUND` | Yes | Yes |
| 44 | BD-3965 | adding more information on example for data consumption | Docs Gap | P2 | Ingestion | rachel-feinberg | `_user_guide/data/infrastructure/data_points.md` | No | No |
| 45 | BD-3978 | Adding content card testing for web in our docs | Docs Gap | P2 | SDKs | zairro | `_developer_guide/platforms/web/content_cards/.md (` | No | No |
| 46 | BD-3985 | Adding more information on syntax for boolean | Docs Gap | P2 | Composition Infrastructure | rachel-feinberg | `_user_guide/data/custom_data/custom_attributes/.md` | No | No |
| 47 | BD-3994 | Adding common troubleshooting steps for Logging Custom ... | Docs Gap | P2 | SDKs | zairro | `_help/home.md` | No | No |
| 48 | BD-4144 | Delete Anonymous Users via /users/delete Endpoint | Docs Gap | P2 | Core Objects | rachel-feinberg | `_user_guide/data/unification/user_data/user_profil` | No | Partial |
| 49 | BD-4269 | Most Recently Used Device Feature For Push Messaging | Docs Gap | P2 | Content Cards | lydia-xie | `NEEDS MANUAL TARGET` | No | Partial |
| 50 | BD-4338 | All possible errors for the User Track endpoint | Docs Gap | P2 | Ingestion | rachel-feinberg | `_api/endpoints/user_data/post_user_track/.md (NOT ` | No | Partial |
| 51 | BD-4348 | How To Find App's SDK Version | Docs Gap | P2 | SDKs | zairro | `_developer_guide/getting_started/sdk_overview/.md ` | No | Partial |
| 52 | BD-4424 | Using Liquid If Statements with Catalog Items | Docs Gap | P2 | Core Objects | rachel-feinberg | `NEEDS MANUAL TARGET` | No | Partial |
| 53 | BD-4473 | Troubleshoot uploading .p12 Certificate to Braze | Docs Gap | P2 | SDKs | zairro | `_developer_guide/platforms/legacy_sdks/ios/push_no` | No | Partial |
| 54 | BD-4476 | What does the InvalidProviderToken Error mean? iOS Push... | Docs Gap | P2 | Content Cards | lydia-xie | `NEEDS MANUAL TARGET` | No | Partial |
| 55 | BD-4535 | Submitting a “Request Timed Out” Support Ticket | Docs Gap | P2 | Onboarding | zairro | `_user_guide/engagement_tools/canvas/faqs.md` | No | Partial |
| 56 | BD-4541 | Catalogs use cases Vs Catalogs Selections use cases | Docs Gap | P2 | Core Objects | rachel-feinberg | `_api/endpoints/catalogs.md` | No | Partial |
| 57 | BD-4576 | Add Line Breaks Reason to Liquid FAQs | Docs Gap | P2 | Composition Infrastructure | rachel-feinberg | `_user_guide/personalization_and_dynamic_content/li` | No | No |
| 58 | BD-4579 | Adding how to log session on anonymous users on web | Docs Gap | P2 | SDKs | zairro | `_developer_guide/sdk_integration.md` | No | No |
| 59 | BD-4611 | iOS Push Notification 'TopicDisallowed' | New Content | P2 | SDKs | zairro | `_user_guide/message_building_by_channel/push/push_` | No | Partial |
| 60 | BD-4651 | Maximum Recipient Limit is not Respected for a Campaign | Docs Gap | P2 | Ingestion | rachel-feinberg | `_user_guide/engagement_tools/campaigns/faq/.md (NO` | No | Partial |
| 61 | BD-4263 | None of the selected users have matching push tokens fo... | Docs Gap | P4 | Content Cards | lydia-xie | `_user_guide/engagement_tools/campaigns/testing_and` | Yes | Yes |
| 62 | BD-4369 | How can I be notified of SDK updates? | Docs Gap | P4 | SDKs | zairro | `NEEDS MANUAL TARGET` | Yes | Yes |
| 63 | BD-4370 | Content block inclusion count | New Content | P4 | Composition Infrastructure | rachel-feinberg | `NEEDS MANUAL TARGET` | Yes | Yes |
| 64 | BD-4385 | When is a user's account flagged as having uninstalled ... | Docs Gap | P4 | Content Cards | lydia-xie | `NEEDS MANUAL TARGET` | Yes | Yes |
| 65 | BD-4511 | Common Safari Web Push Issues | Docs Gap | P4 | SDKs | zairro | `_developer_guide/push_notifications/troubleshootin` | Yes | Yes |

### Per-Ticket Detail

#### 1. [BD-4036] Users Not Logging Sessions
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: (not specified)
- **Recommended Action**: Add the reason why some users might be logging sessions and others not: "This may coincide with changes made to an app, specifically how the SDK is initialized. For example, if there is conditional logic applied before triggering the SDK, this may pr
- **Target Doc**: `NEEDS MANUAL TARGET` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000HHIzYAO/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Comments** (2 shown):
  - [5f86c5b6ecee350069f9759d] <p><a href="https://jira.atl.braze.com/secure/ViewProfile.jspa?accountId=712020%3A8e897d8e-2a14-4cf0-b8d3-d5227546b472" cla
  - [5f86c5b6ecee350069f9759d] <p><a href="https://jira.atl.braze.com/secure/ViewProfile.jspa?accountId=712020%3Ac02a883d-7dfa-4c66-9ba6-13805ec95642" cla

#### 2. [BD-4068] User Profile Attribute "Language"
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Core Objects
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: Braze docs currently does not have this information
- **Recommended Action**: Add a small section with the following information: "A user's profile language is based on Device Locale, which takes into account the language of the operating system on the device. For example, if a user lived in the U.S. and their device OS langua
- **Target Doc**: `_docs/_user_guide/data/user_data_collection/sdk_data_collection/.md (NOT FOUND)` [NOT FOUND]
- **Target Doc**: `_docs/_user_guide/engagement_tools/segments/user_profiles/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000IlBlYAK/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: n.a.

#### 3. [BD-4075] ChangeUser() SDK method FAQ
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: We do not have a concise place explaining about these behaviour and warning customers about what might happen if they do not use it right.
- **Recommended Action**: Add in our public docs, in the begining of their SDK integration, the details below.
- **Target Doc**: `NEEDS MANUAL TARGET` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/articles/Knowledge/changeUser-method-FAQ
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 4. [BD-4078] What is the minimum time interval between triggers for IAMs?
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: This information is missing and can improve their SDK integration.
- **Recommended Action**: In production apps, we do not recommend making this value any smaller than 10, to avoid spamming the user with notifications. In our sample apps, we have reduced that time to 5 seconds . Are there any downsides to setting the minimal time interval be
- **Target Doc**: `_docs/_developer_guide/platforms/android/in_app_messages/delivery.md (NOT FOUND)` [NOT FOUND]
- **Target Doc**: `_docs/_developer_guide/platforms/web/in_app_messages/delivery.md (NOT FOUND)` [NOT FOUND]
- **Target Doc**: `_docs/_developer_guide/platforms/swift/in_app_messages/message_delivery/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/articles/Knowledge/InApp-Messages-Minimum-Time-Interval-Between-Triggers
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 5. [BD-4080] Formatting for DateTime datatype?
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Core Objects
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: We don't have all the information within the article in our docs.
- **Recommended Action**: This is what is missing: Keep in mind that if not setting a timezone, or setting timezone incorrectly, we will always default to UTC. Time will always appear in company timezone on the dashboard. So if you wanted to set the time for October 31, 2019 
- **Target Doc**: `_docs/_api/objects_filters/user_attributes_object.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/articles/Knowledge/DateTime-Format
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: not sensitive, but the screenshot should not be migrated.

#### 6. [BD-4099] Custom Event Not Logging in Braze via Google Tag Manager (GTM)
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: We have a troubleshooting steps section but the info in this KA is not included in our Docs.
- **Recommended Action**: I suggest adding this KA as a troubleshooting step as Google Tag manager cases do come up fairly often.
- **Target Doc**: `_docs/_developer_guide/platforms/web/google_tag_manager/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000IerpYAC/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 7. [BD-4138] When might a user have 0 sessions recorded against their profile?
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: We do not have this in our docs currently and I think it could be beneficial to include these reasons why users show 0 sessions.
- **Recommended Action**: Add content from KA article to docs.
- **Target Doc**: `NEEDS MANUAL TARGET` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000CV6TYAW/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 8. [BD-4171] How do I update Custom Attribute data types via CSV?
- **Category**: New Content
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: The article outlines the procedure in updating the data type which is not covered in the user import page.
- **Recommended Action**: The article only really points out that data types must be changed in the 'Custom Attribute' page first so this only requires a brief sentence explaining that the data type needs to be changed first and then the CSV import can be uploaded with the ne
- **Target Doc**: `_docs/_user_guide/data/user_data_collection/user_import/.md (NOT FOUND)` [NOT FOUND]
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 9. [BD-4174] How is a Content Card's Expiration (Time In Feed) Calculated?
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Content Cards
- **Assignee**: Lydia Xie (GitHub: `lydia-xie`)
- **Linked Cases**: 0
- **Knowledge Gap**: Braze docs mentions expiration time for content cards, but does not explain how it is calculated.
- **Recommended Action**: Add a paragraph at the bottom of the "Overview" section for the campaign tab: "Regardless of selected option, the Expiration (Time In Feed) is calculated from its Send Time. For a scheduled send , it will be the time after the campaign is launched. F
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/content_cards/create/card_creation/.md (NOT FOUND)` [NOT FOUND]
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/content_cards/create/card_creation/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000JOppYAG/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: n.a.

#### 10. [BD-4201] Clicking on Push Notification Doesn't Open the App
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: Our docs does have an faq or section that addresses this
- **Recommended Action**: Add a section that shows steps on how to resolve this issue in iOS and Android SDK which is stated in the resolution part of the KA.
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/push.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000JYCTYA4/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: no sensitive information

#### 11. [BD-4234] How do I use the spacer.gif resource?
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Content Cards
- **Assignee**: Lydia Xie (GitHub: `lydia-xie`)
- **Linked Cases**: 0
- **Knowledge Gap**: the use of the spacer.gif in webhooks for a canvas step is not mentioned in our docs.
- **Recommended Action**: Add the following into the Canvas documentation for a webhook step : "We have a hack of our webhooks by calling a resource we host called spacer.gif. The spacer.gif image will not be sent or displayed to any users, but the webhook call will be succes
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/webhooks/creating_a_webhook/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000FxqzYAC/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Comments** (1 shown):
  - [5f86c5b6ecee350069f9759d] <p>Would love to get Product's pov on this , if we should make it public. Seem like we have 39 case where this was a soluti

#### 12. [BD-4259] Invalid API Key
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: Our docs don't give specific examples of real-life errors the way the KA does. It also provides different reasons for why it might be happening and how to solve them.
- **Recommended Action**: Please make sure to include the images and steps shown in the KA
- **Target Doc**: `_docs/_api/errors.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000JdqTYAS/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: it doesn't look like this ka has any information that can't be shared
- **Comments** (1 shown):
  - [5f86c5b6ecee350069f9759d] <p>Hi <a href="https://jira.atl.braze.com/secure/ViewProfile.jspa?accountId=712020%3A4086c852-034c-409c-a41c-f18fb31de9f7" 

#### 13. [BD-4278] Limitations for Catalog
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Core Objects
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: Here is what the KA has and what should be moved over and added to a table. CSV file size Up to 100 MB for all CSV files combined across your company Up to 2 GB for a single CSV file Characters limit for item value Up to 5,000 characters in one value
- **Recommended Action**: Add this to the following Docs section: Unable to render embedded object: File (Screenshot 2025-03-13 at 5.41.01 PM.png) not found. * https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/#preparing-your-csv-file*
- **Target Doc**: `_docs/_user_guide/personalization_and_dynamic_content/catalogs/catalog/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000JpzhYAC/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 14. [BD-4280] In-App Message Impression Failure Error in Event User Logs
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: color: Color value is invalid : Our docs do not mention any error codes to look for in the raw logs in the event user logs.
- **Recommended Action**: Add a section that has information of an error code "tf" in the raw data of an SDK request
- **Target Doc**: `_docs/_user_guide/administrative/app_settings/event_user_log_tab.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000Fu0HYAS/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: in the screenshot there is no sensitive information, but i do not think it's necessary to include the screenshot.

#### 15. [BD-4281] How to find an anonymous user in the Web SDK
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: Our docs do not mention how to find anonymous user in the Web SDK.
- **Recommended Action**: Add a section that show customers how to find an anonymous user in the Web SDK. In a web browser go to In a web browser's developer tools. For example, in Google Chrome, go to View > Developer > Developer tools or use short-cut Command + Option + J o
- **Target Doc**: `_docs/_developer_guide/home.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000Jj6HYAS/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: in the screenshots of the ka, there is no sensitive information. { }

#### 16. [BD-4282] API rate Limit - Rolling Hour or Hourly Basis
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: { }Looked in the docs and there's no information on this.
- **Recommended Action**: { }Add a section that let users know that API rate limit is based on a hourly basis.
- **Target Doc**: `_docs/_api/basics.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP0000009cm1YAA/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 17. [BD-4290] How are Currency Exchange Rates Calculated for the Braze Dashboard
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: { }Our documentation does not have any information on how Currency Exchange Rates Calculated for the Braze Dashboard
- **Recommended Action**: Suggest additional content that should be included. This could be a brief summary or draft of the content, or specific examples that will complement the user’s understanding. For example, “Add a section that warns users of unexpected results when add
- **Target Doc**: `_docs/_user_guide/data/custom_data/purchase_events/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000IBhlYAG/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: n/a { }

#### 18. [BD-4299] Multiple IAMs Display In The Same Session if They Are Both Triggered by 'Session Start'?
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: Our docs don't mention that multiple IAMs won't display for the user in the same session. We state that we display based on priority, but we should clarify that this requires the user to log a new session to get the next IAM in the priority list.
- **Recommended Action**: Answer this question: Can two or more IAMs display in the same session if they both trigger off of 'Session Start'? Which is "no", one IAM per session. Further explain how priority and recency of the IAM being created will play into the order of the 
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/in-app_messages/traditional/create/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000Ixo1YAC/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: related pq:

#### 19. [BD-4304] API Success Message Received But No Message Delivered
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: We mention in our docs that a success message from a messaging endpoint just means the call was received for processing and why this doesn't guarantee delivery of messages. What we don't mention is that for endpoints like /users/identify, the success
- **Recommended Action**: Add the following context to the docs at the link below: For example, for /users/identify, if the request synax and format is correct, it will return a success message. This means that Braze has received the request for processing. However, after pro
- **Target Doc**: `_docs/_api/errors/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000HLEXYA4/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 20. [BD-4307] Slowness in Displaying Action-Based Content Cards
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Content Cards
- **Assignee**: Lydia Xie (GitHub: `lydia-xie`)
- **Linked Cases**: 0
- **Knowledge Gap**: Action Based content delivery for campaigns is not instant and its expected.
- **Recommended Action**: From the KA: For action-based delivery campaigns(like session start), it is expected that there will be a short but indeterminate delay between the event and the card being available. For better understanding, the backend process for content cards tr
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/content_cards/create/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000HsDhYAK/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 21. [BD-4318] How to Integrate a Web App With GTM (Google Tag Manager) and Initialize Braze
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: The lack of readable step-by-step instructions in the KA article do not persist in the documentation
- **Recommended Action**: Include the screenshots or the code of where the code snippets should go in a customer's GTM project, and also the ways they can test the integration
- **Target Doc**: `_docs/_developer_guide/platforms/web/google_tag_manager/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000JluTYAS/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 22. [BD-4321] User Import - CSV File Download Window
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: It shares with clients how long after they can download a csv upload.
- **Recommended Action**: Adding a section sharing that: CSV user imports are available to download from the dashboard for 14 days (after the time of upload).
- **Target Doc**: `_docs/_user_guide/data/user_data_collection/user_import/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000IA8zYAG/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: no info is sensitive but i don't think it is needed to add "this file also gets deleted from where it is stored after this period. therefore, there is

#### 23. [BD-4334] Are GIF's Supported in Android?
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: Making it easy for customers to know this isn't a Braze issue is important. We should publicly call that out.
- **Recommended Action**: Add a callout on our Push doc page.
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/push/best_practices/message_format/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000HUphYAG/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 24. [BD-4349] Push Issues Within mParticle Kit Integration (iOS)
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: { }Our docs don't mention steps to resolve push Issues Within mParticle Kit Integration (iOS)
- **Recommended Action**: Add a section that mentions steps to resolve push Issues Within mParticle Kit Integration (iOS)
- **Target Doc**: `_docs/_developer_guide/sdk_integration.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000Hx5JYAS/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: n/a { }

#### 25. [BD-4350] Identify Endpoint: User Alias not associated successfully with external ID after 201 response
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: Our docs don’t mention unexpected results when User Alias not associated successfully with external ID after 201 response using Braze REST endpoint /users/identify. The user alias is case-sensitive and the alias_name field must match the capitalizati
- **Recommended Action**: Add a section provide information on unexpected results when User Alias not associated successfully with external ID after 201 response using Braze REST endpoint /users/identify. For example: A user with no external ID has an assigned user alias "Jim
- **Target Doc**: `_docs/_api/endpoints/user_data/post_user_identify/.md (NOT FOUND)` [NOT FOUND]
- **Target Doc**: `_docs/_api/endpoints/user_data/post_user_identify.md` [EXISTS]
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: there is sensitive information in the ka as one of our support reps used their email as an example. { }

#### 26. [BD-4352] Braze to Braze Webhook > Error: 415 Unsupported Media Type
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: Our docs don’t mention an error 415 Unsupported Media Type
- **Recommended Action**: Add a section that warn users of an error 415 when a webhook campaign calls REST API endpoint { }
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/webhooks/creating_a_webhook/.md (NOT FOUND)` [NOT FOUND]
- **Target Doc**: `_docs/_api/errors/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000FoXZYA0/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: n/a { }

#### 27. [BD-4411] What Could be the Reason for Large Number of Uninstalls of an Application
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Content Cards
- **Assignee**: Lydia Xie (GitHub: `lydia-xie`)
- **Linked Cases**: 0
- **Knowledge Gap**: Educate the client on very common reasons that their app may experience spikes in uninstall rates.
- **Recommended Action**: include all information from the knowledge article. explain how to check for a specific message that may have lead to uninstalls explain how the presence of the push notification error 'BadDeviceToken' can indicate users are uninstalling the app. If 
- **Target Doc**: `_docs/_user_guide/analytics/tracking/uninstall_tracking/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP0000008wGXYAY/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 28. [BD-4413] Correctly Sized GIF not Uploading to the Media Library
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Composition Infrastructure
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: The only known 'limitations' for adding a gif or media to the Media library is file size. However, there are instances when certain gif files fail to upload and customers do not know why.
- **Recommended Action**: Include all information from the knowledge article
- **Target Doc**: `_docs/_user_guide/engagement_tools/templates_and_media/faqs.md` [EXISTS]
- **Target Doc**: `_docs/_user_guide/engagement_tools/templates_and_media/media_library.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000IKgDYAW/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 29. [BD-4415] Add Existing Users to a Subscription Group
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: I believe this support article was created because if you use the article title as search terms on the public docs, this endpoint article does not come up as a suggestion. We could benefit by making this use case much more straightforward.
- **Recommended Action**: Include language on the endpoint doc that explicitly mentions how this endpoint can be used when you want to update existing users. I know we already have language about how for new users, they should use /users/track.
- **Target Doc**: `_docs/_api/endpoints/subscription_groups/post_update_user_subscription_group_status.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000E1nRYAS/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 30. [BD-4451] "Open Web URL Inside App" Behaviour - draft mode
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Content Cards
- **Assignee**: Lydia Xie (GitHub: `lydia-xie`)
- **Linked Cases**: 0
- **Knowledge Gap**: Our docs do not mention how this behavior is expected to work when in draft mode { }
- **Recommended Action**: Add a blurb within the below documentation link explaining the behavior for the Open Web Url inside App functions within draft mode of a canvas or campaign
- **Target Doc**: `_docs/_help/help_articles/push/push_clicks_unexpectedly_open_in_app.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000KFfdYAG/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 31. [BD-4460] The Difference Between "Send to Production" and "Send to Development" When Adding an Apple Push Certificate
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Content Cards
- **Assignee**: Lydia Xie (GitHub: `lydia-xie`)
- **Linked Cases**: 0
- **Knowledge Gap**: "Currently, Braze Docs may not clearly explain the distinction between sending push notifications through Apple's development gateway versus the production gateway. This information is essential for users to correctly configure push notifications for
- **Recommended Action**: "Add a section that details the purpose of the 'Send to Production' and 'Send to Development' options when configuring Apple Push Certificates. Explain that 'Send to Development' is used for apps built in development mode, which require push notifica
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/push/ios_push_notifications.md (NOT FOUND)` [NOT FOUND]
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/push/faq/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000K9C1YAK/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: "no sensitive information identified in the provided content."

#### 32. [BD-4472] Security Risks Associated with API Key Exposure
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: The docs do note discuss how REST API keys should remain private while SDK keys don't have to. This may be obvious to most devs but an article denoting this may help increase security for our customers.
- **Recommended Action**: This could be part of our API Keys article or a separate one.
- **Target Doc**: `_docs/_user_guide/administrative/app_settings/api_settings_tab/.md (NOT FOUND)` [NOT FOUND]
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 33. [BD-4480] How to Set Up SDK Authentication to Prevent Unwanted Requests? + FAQs
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: The KA mentions some nuances in the FAQ that can be incorporated into the docs.
- **Recommended Action**: The docs have an FAQ section of their own but some things like SDK authentication only being available for external ids is not noted.
- **Target Doc**: `_docs/_developer_guide/sdk_integration/authentication.md` [EXISTS]
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 34. [BD-4502] Push Notification Titles Appear Correctly on Android but not iOS
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Content Cards
- **Assignee**: Lydia Xie (GitHub: `lydia-xie`)
- **Linked Cases**: 0
- **Knowledge Gap**: I'm not seeing this information about formatting push titles differently for Android vs iOS in our docs currently, and this feels like an important callout.
- **Recommended Action**: Issue When using Liquid to send a customised push campaign, the push displays correctly and in full for Android. However, for iOS, the title seems to be cut off as soon as any Liquid variable is reached.For example: a customised title reading " Regar
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/push/troubleshooting.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000FYe5YAG/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 35. [BD-4504] Liquid Error Occurs On The Dashboard When Previewing Some Data Types
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Composition Infrastructure
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: from what I saw in our docs, we don't have any information concerning an error message being shown when previewing a message where liquid filters or operations are applied to some persistent entry properties, event properties, or purchase objects.
- **Recommended Action**: I believe including all of the KA would be beneficial to the customer in this instance
- **Target Doc**: `_docs/_user_guide/personalization_and_dynamic_content/liquid/faq.md` [EXISTS]
- **Target Doc**: `_docs/_user_guide/personalization_and_dynamic_content/liquid/operators.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000JENRYA4/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: there doesn't seem to be any sensitive data in this ka

#### 36. [BD-4514] Testing Nested Custom Attributes and Nested Objects for Custom Event Properties
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Core Objects
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: Our docs explain what Nested Custom Attributes are, and how to import them to Braze. But they don't explain how to test messaging that references a Nested Custom Attribute or Nested Objects for Custom Event Properties via liquid. Our Preview & Test t
- **Recommended Action**: Add a section called "Testing Nested Custom Attributes" and "Testing Nested Objects" to the relevant feature pages. This could be written step-by-step or a video walk-through "Testing Nested Custom Attributes" Prerequisites: campaign that references 
- **Target Doc**: `NEEDS MANUAL TARGET` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000KpUbYAK/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 37. [BD-4569] When do we evaluate the abort logic of an IAM?
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Composition Infrastructure
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: I could not find this information under our IAM or Liquid abort docs.
- **Recommended Action**: I would suggest we add it to our Liquid abort docs. Maybe consider expanding it to include when it is evaluated for other messaging mediums.
- **Target Doc**: `_docs/_user_guide/personalization_and_dynamic_content/liquid/aborting_messages.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000Eln3YAC/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 38. [BD-4591] How To Prevent Tracking Anonymous Users
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: Provides tips for preventing tracking of anon users if this is required to fulfill the customer's use case
- **Recommended Action**: Add the entirety of this article's content to our docs page
- **Target Doc**: `_docs/_user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000LU37YAG/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 39. [BD-4593] When Does Braze Log Sends for Content Card Deliveries?
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Content Cards
- **Assignee**: Lydia Xie (GitHub: `lydia-xie`)
- **Linked Cases**: 0
- **Knowledge Gap**: additional context for customers to be aware of
- **Recommended Action**: add the entire contents of the article to the 'know before you send - content cards' section of our Braze docs
- **Target Doc**: `_docs/_help/help_articles/campaigns_and_canvas/know_before_send/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000L4WrYAK/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 40. [BD-4595] Content Card Image Not Rendering / Is Broken Due To Bad URL
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Content Cards
- **Assignee**: Lydia Xie (GitHub: `lydia-xie`)
- **Linked Cases**: 0
- **Knowledge Gap**: Provide customers with additional troubleshooting context for content card images that are not loading properly when accessed via URL.
- **Recommended Action**: Supplement the braze docs with all content from the knowledge article. As a suggestion: Add contents to the 'Test checklist' subsection
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/content_cards/testing/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000LQQvYAO/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 41. [BD-4597] How to Log a Custom Event Using GTM (Google Tag Manager)
- **Category**: New Content
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: Our public docs don’t provide clear instructions / examples for how to log a Custom Event with GTM. Our docs say that our customers can use the Braze Action tag to log analytics, but clicking "logging analytics" links out to a broken page (404). This
- **Recommended Action**: Add a section (or a new page) that outlines how to log a Custom Event with GTM, including an example. The Knowledge Article includes the steps
- **Target Doc**: `_docs/_developer_guide/sdk_integration/.md (NOT FOUND)` [NOT FOUND]
- **Target Doc**: `_docs/_developer_guide/sdk_integration/.md (NOT FOUND)` [NOT FOUND]
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 42. [BD-4604] iOS Universal Links Not Working When ABKURLDelegate Returns True
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: this information is not in the docs in case a customer runs into this issue
- **Recommended Action**: Add this information for customers to be aware of
- **Target Doc**: `_docs/_user_guide/brazeai/intelligence/intelligent_timing/.md (NOT FOUND)` [NOT FOUND]
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/email/universal_links.md` [EXISTS]
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)
- **Sensitive Content Flag**: n/

#### 43. [BD-4660] Why Are React Native Deep Links Not Working?
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: Our docs do not mention what is mentioned in the "Resolution" section of the KA.
- **Recommended Action**: In the KA, at the very end there is a line "if that does not solve the issue, further troubleshooting will be required" which might come off as a little vague, and maybe they should instead write in to Support
- **Target Doc**: `_docs/_developer_guide/push_notifications/.md (NOT FOUND)` [NOT FOUND]
- **Target Doc**: `_docs/_developer_guide/push_notifications/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000Lo1pYAC/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 44. [BD-3965] adding more information on example for data consumption
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: Request from Alan Zaki(alan.zaki@braze.com) Request_Type standard Description could we add additional information to the note maybe with an example: Updating a custom attribute object to null also consumes a data point. ADD: assuming I've got an arra
- **Recommended Action**: (not specified)
- **Target Doc**: `_docs/_user_guide/data/infrastructure/data_points.md` [EXISTS]
- **CSV Match**: No
- **Ready to Draft**: No — needs SF article content
- **Comments** (3 shown):
  - [5f86c5b6ecee350069f9759d] <p>KA - <a href="https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000HImvYAG/view" class="external-link
  - [5f86c5b6ecee350069f9759d] <p><a href="https://jira.atl.braze.com/secure/ViewProfile.jspa?accountId=712020%3A960e958a-0a42-4846-9423-6dca8c9571a4" cla
  - [712020:960e958a-0a42-4846-9423-6dca8c9571a4] <p><a href="https://jira.atl.braze.com/secure/ViewProfile.jspa?accountId=5f86c5b6ecee350069f9759d" class

#### 45. [BD-3978] Adding content card testing for web in our docs
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: Request from Alan Zaki(alan.zaki@braze.com) Request_Type standard Description While integrating the Web SDK, is it possible to test the content card integration? Yes. Using the browser developer tools (Chrome Console) you can test the content cards. 
- **Recommended Action**: (not specified)
- **Target Doc**: `_docs/_developer_guide/platforms/web/content_cards/.md (NOT FOUND)` [NOT FOUND]
- **CSV Match**: No
- **Ready to Draft**: No — needs SF article content
- **Comments** (3 shown):
  - [5f86c5b6ecee350069f9759d] <p>KA - <a href="https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000IJSQYA4/view" class="external-link
  - [5f86c5b6ecee350069f9759d] <p>Could this be included in a Troubleshooting section? </p>
  - [712020:960e958a-0a42-4846-9423-6dca8c9571a4] <p><a href="https://jira.atl.braze.com/secure/ViewProfile.jspa?accountId=5f86c5b6ecee350069f9759d" class

#### 46. [BD-3985] Adding more information on syntax for boolean
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Composition Infrastructure
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: Request from Alan Zaki(alan.zaki@braze.com) Request_Type standard Description I wonder if we can add a section where we specify that the data type of the custom attribute being called in the Liquid matches the data type of the attribute in the dashbo
- **Recommended Action**: (not specified)
- **Target Doc**: `_docs/_user_guide/data/custom_data/custom_attributes/.md (NOT FOUND)` [NOT FOUND]
- **CSV Match**: No
- **Ready to Draft**: No — needs SF article content
- **Comments** (3 shown):
  - [5f86c5b6ecee350069f9759d] <p>KA - <a href="https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000I1vJYAS/view" class="external-link
  - [712020:960e958a-0a42-4846-9423-6dca8c9571a4] <p>imo it would not hurt to have this information and example added in the link provided but happy for t
  - [5f86c5b6ecee350069f9759d] <p><a href="https://jira.atl.braze.com/secure/ViewProfile.jspa?accountId=712020%3A960e958a-0a42-4846-9423-6dca8c9571a4" cla

#### 47. [BD-3994] Adding common troubleshooting steps for Logging Custom Events
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: Request from Rory Prutton(rory.prutton@braze.com) Request_Type standard Description There isn't any information which we can give the customer for generic troubleshooting which is ambiguous of the specific SDK (as they all generally follow the same r
- **Recommended Action**: (not specified)
- **Target Doc**: `_docs/_help/home.md` [EXISTS]
- **CSV Match**: No
- **Ready to Draft**: No — needs SF article content
- **Comments** (3 shown):
  - [712020:6d31060b-0599-4afd-b814-c66a0f8f2952] <p>KA link -<a href="https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000I1YjYAK/vie
  - [712020:c02a883d-7dfa-4c66-9ba6-13805ec95642] <p>Hi <a href="https://jira.atl.braze.com/secure/ViewProfile.jspa?accountId=712020%3A6d31060b-0599-4afd-
  - [5f86c5b6ecee350069f9759d] <p><a href="https://jira.atl.braze.com/secure/ViewProfile.jspa?accountId=712020%3A6d31060b-0599-4afd-b814-c66a0f8f2952" cla

#### 48. [BD-4144] Delete Anonymous Users via /users/delete Endpoint
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Core Objects
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: Customers do ask support to delete anonymous users on their behalf and if they have the knowledge to do it themselves it would make things go by faster for them
- **Recommended Action**: Include a section in the documentation that informs the customer on how to delete anonymous users
- **Target Doc**: `_docs/_user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000HgCXYA0/view
- **CSV Match**: No
- **Ready to Draft**: Partial — ticket has detail but no CSV match

#### 49. [BD-4269] Most Recently Used Device Feature For Push Messaging
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Content Cards
- **Assignee**: Lydia Xie (GitHub: `lydia-xie`)
- **Linked Cases**: 0
- **Knowledge Gap**: The public docs mention this feature and how it works. But, the Knowledge Article has an additional point that is missing from our public docs - which device will Braze target? Is "most recently used device" defined by sessions, or the timestamp when
- **Recommended Action**: Update the public docs to include this information from the Knowledge Article: " Enabling this feature will target push delivery for only one device, based on which device has the most recently updated Push token. It does not target the device with t
- **Target Doc**: `NEEDS MANUAL TARGET` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000IloTYAS/view
- **CSV Match**: No
- **Ready to Draft**: Partial — ticket has detail but no CSV match

#### 50. [BD-4338] All possible errors for the User Track endpoint
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: color: Color value is invalid : From what I could find we do not have possible errors listed out for clients to perform minor troubleshooting with the users/track endpoint.
- **Recommended Action**: Add the below table to our docs: Error Details BAD_DEVICE_ID "token import with 'device_id' must have a device_id less than 255 bytes and at least 8 bytes" BAD_EMAIL_SUBSCRIPTION_STATE "'email_subscribe' must be 'subscribed', 'unsubscribed', or 'opte
- **Target Doc**: `_docs/_api/endpoints/user_data/post_user_track/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000Hex7YAC/view
- **CSV Match**: No
- **Ready to Draft**: Partial — ticket has detail but no CSV match

#### 51. [BD-4348] How To Find App's SDK Version
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: Our docs already state one way to find a customer's app sdk version, however there is another way on how to retrieve it.
- **Recommended Action**: { }Add the other way that customer's can determine their app's SDK version which is listed in the KA, which is: If the SDK versions are not located in the dashboard in this section you can search your Braze email for the following subject lines. Plea
- **Target Doc**: `_docs/_developer_guide/getting_started/sdk_overview/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000ELNxYAO/view
- **CSV Match**: No
- **Ready to Draft**: Partial — ticket has detail but no CSV match
- **Sensitive Content Flag**: n/a { }

#### 52. [BD-4424] Using Liquid If Statements with Catalog Items
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Core Objects
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: The current documentation does not address how to effectively use Liquid if statements with catalog items and selections, which is essential for users looking to implement conditional logic in their messaging.
- **Recommended Action**: Update the documentation to include: Using Liquid If Statements with Catalog Items : To be able to use catalog items as a variable with liquid, you would need to first declare the catalog list before you are able to retrieve the variable to use with 
- **Target Doc**: `NEEDS MANUAL TARGET` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000J3i9YAC/view
- **CSV Match**: No
- **Ready to Draft**: Partial — ticket has detail but no CSV match
- **Sensitive Content Flag**: no sensitive information identified.

#### 53. [BD-4473] Troubleshoot uploading .p12 Certificate to Braze
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: Our public docs don't outline the Warning when trying to upload the .p12 Certificate to Braze. "Warning: The legacy .p12 and .pem certificate file types are deprecated in favor of .p8 files. Unlike .p8 files, the legacy file types expire annually and
- **Recommended Action**: Using the content from the Knowledge Article, add the warning message and what it may mean: "As mentioned in the warning, .p12 files require error-prone manual updating and our customers should be aware of this before proceeding further. "
- **Target Doc**: `_docs/_developer_guide/platforms/legacy_sdks/ios/push_notifications/integration.md` [EXISTS]
- **Target Doc**: `_docs/_hidden/other/support_contact.md` [EXISTS]
- **Target Doc**: `_docs/_developer_guide/push_notifications.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000Dc13YAC/view
- **CSV Match**: No
- **Ready to Draft**: Partial — ticket has detail but no CSV match

#### 54. [BD-4476] What does the InvalidProviderToken Error mean? iOS Push Error Message
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Content Cards
- **Assignee**: Lydia Xie (GitHub: `lydia-xie`)
- **Linked Cases**: 0
- **Knowledge Gap**: color: Color value is invalid : Our public docs don't outline the meaning of the Error InvalidProviderToken
- **Recommended Action**: Using the content from the Knowledge Article, add a section on the meaning of the color: Color value is invalid InvalidProviderToken
- **Target Doc**: `NEEDS MANUAL TARGET` [NOT FOUND]
- **SF Knowledge Article**: https://www.braze.com/docs/user_guide/message_building_by_channel/push/push_error_codes/?tab=ios
- **CSV Match**: No
- **Ready to Draft**: Partial — ticket has detail but no CSV match

#### 55. [BD-4535] Submitting a “Request Timed Out” Support Ticket
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Onboarding
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: The current documentation does not provide detailed guidance on how to effectively report "Request Timed Out" errors to Braze Support, which can hinder timely resolution of issues.
- **Recommended Action**: Update the documentation to include: Information to Include When Raising a Ticket for "Request Timed Out" Errors : Screen Recording : Provide a screen recording of the steps taken before seeing the error message. This helps Braze Support reproduce th
- **Target Doc**: `_docs/_user_guide/engagement_tools/campaigns/faq/.md (NOT FOUND)` [NOT FOUND]
- **Target Doc**: `_docs/_user_guide/engagement_tools/canvas/faqs.md` [EXISTS]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000EhczYAC/view
- **CSV Match**: No
- **Ready to Draft**: Partial — ticket has detail but no CSV match
- **Sensitive Content Flag**: no sensitive information identified.
- **Comments** (1 shown):
  - [63c9a720b1262586707aefec] <p><a href="https://jira.atl.braze.com/secure/ViewProfile.jspa?accountId=712020%3Ab901bd0c-d883-4f9a-9cd9-878e34f895b1" cla

#### 56. [BD-4541] Catalogs use cases Vs Catalogs Selections use cases
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Core Objects
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: The current documentation does not provide clear guidance on how to effectively structure Catalog data for various use cases, nor does it explain the differences between using standard Catalog calls and Catalog Selections.
- **Recommended Action**: Update the documentation to include: Structuring Your Catalog Data in Braze : When planning how to structure your Catalog data in Braze, it's important to think backwards from your end use case. Each row in the Catalog refers to an “item” (with a uni
- **Target Doc**: `_docs/_api/endpoints/catalogs.md` [EXISTS]
- **Target Doc**: `_docs/_user_guide/personalization_and_dynamic_content/catalogs/selections/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000Ku2rYAC/view
- **CSV Match**: No
- **Ready to Draft**: Partial — ticket has detail but no CSV match
- **Sensitive Content Flag**: no sensitive information identified.

#### 57. [BD-4576] Add Line Breaks Reason to Liquid FAQs
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Composition Infrastructure
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: Request from Rory Prutton(rory.prutton@braze.com) Request_Type standard Description We can mention about how line breaks can appear in Liquid as per this KA: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000GCmoYAG/view Request
- **Recommended Action**: (not specified)
- **Target Doc**: `_docs/_user_guide/personalization_and_dynamic_content/liquid/faq/.md (NOT FOUND)` [NOT FOUND]
- **CSV Match**: No
- **Ready to Draft**: No — needs SF article content

#### 58. [BD-4579] Adding how to log session on anonymous users on web
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: Request from Rory Prutton(rory.prutton@braze.com) Request_Type standard Description This KA helps describe how we can make sure to get session data on anonymous users, which could be worthwhile to customers https://braze.lightning.force.com/lightning
- **Recommended Action**: (not specified)
- **Target Doc**: `_docs/_developer_guide/sdk_integration.md` [EXISTS]
- **Target Doc**: `_docs/_developer_guide/sdk_integration.md` [EXISTS]
- **CSV Match**: No
- **Ready to Draft**: No — needs SF article content

#### 59. [BD-4611] iOS Push Notification 'TopicDisallowed'
- **Category**: New Content
- **Priority**: P2
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: Our docs do not mention anything about `TopicDisallowed` push error
- **Recommended Action**: Add new section to "Common push error messages" and add `TopicDisallowed`.
- **Target Doc**: `_docs/_user_guide/message_building_by_channel/push/push_error_codes/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000LOovYAG/view
- **CSV Match**: No
- **Ready to Draft**: Partial — ticket has detail but no CSV match

#### 60. [BD-4651] Maximum Recipient Limit is not Respected for a Campaign
- **Category**: Docs Gap
- **Priority**: P2
- **Team**: Ingestion
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: it helps customers know possible scenario for misalignment between send data and max recipient.
- **Recommended Action**: Add an additional FAQ to the docs outlining that making changes to max recipient to an active Campaign may cause misalignment with send analytics . If the maximum recipient limit was added post-launch, the campaign may have been respecting the rule a
- **Target Doc**: `_docs/_user_guide/engagement_tools/campaigns/faq/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000Dp9ZYAS/view
- **CSV Match**: No
- **Ready to Draft**: Partial — ticket has detail but no CSV match
- **Sensitive Content Flag**: none { }

#### 61. [BD-4263] None of the selected users have matching push tokens for iOS/Android Push
- **Category**: Docs Gap
- **Priority**: P4
- **Team**: Content Cards
- **Assignee**: Lydia Xie (GitHub: `lydia-xie`)
- **Linked Cases**: 0
- **Knowledge Gap**: The documentation correctly outlines push registration process and common push error messages. However, it doesn't outline explanation for typical error ` None of the selected users have matching push tokens for Android/iOS Push`
- **Recommended Action**: Add a warning that user will see an error if their user is not registered for push notifications
- **Target Doc**: `_docs/_user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000JbBxYAK/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

#### 62. [BD-4369] How can I be notified of SDK updates?
- **Category**: Docs Gap
- **Priority**: P4
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: The documentation could be updated to advise clients how they can monitor the various GITHUB SDK update pages and be automatically notified of new updates. KA contains the detail on how to do this by altering the github settings.
- **Recommended Action**: (not specified)
- **Target Doc**: `NEEDS MANUAL TARGET` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000H5HqYAK/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match available)

#### 63. [BD-4370] Content block inclusion count
- **Category**: New Content
- **Priority**: P4
- **Team**: Composition Infrastructure
- **Assignee**: Rachel Feinberg (GitHub: `rachel-feinberg`)
- **Linked Cases**: 0
- **Knowledge Gap**: Describes that the Inclusion Count column in the Content Block Library represents the number of messages or Content Blocks in which the Content Block is used. This information is not covered in the documentation.
- **Recommended Action**: (not specified)
- **Target Doc**: `NEEDS MANUAL TARGET` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000FsphYAC/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match available)

#### 64. [BD-4385] When is a user's account flagged as having uninstalled the app? When are they considered to have installed the app?
- **Category**: Docs Gap
- **Priority**: P4
- **Team**: Content Cards
- **Assignee**: Lydia Xie (GitHub: `lydia-xie`)
- **Linked Cases**: 0
- **Knowledge Gap**: This article explains how/ when a user uninstalls and reinstalls an app. "Uninstall tracking "tags" users who have uninstalled the app. In the case a client uses the "has not uninstalled" filter for a campaign, these tagged users will not receive the
- **Recommended Action**: (not specified)
- **Target Doc**: `NEEDS MANUAL TARGET` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP0000005PIjYAM/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match available)

#### 65. [BD-4511] Common Safari Web Push Issues
- **Category**: Docs Gap
- **Priority**: P4
- **Team**: SDKs
- **Assignee**: Zair Kelley Ortiz (GitHub: `zairro`)
- **Linked Cases**: 0
- **Knowledge Gap**: These steps are available in our knowledge base, but I am unable to find them in our docs. There is a push troubleshooting section in our docs, but nothing specific to safari. The standard web troubleshooting steps do not appear to contain this info.
- **Recommended Action**: Add a safari section in Push Notification troubleshooting that includes this information.
- **Target Doc**: `_docs/_developer_guide/push_notifications/troubleshooting/.md (NOT FOUND)` [NOT FOUND]
- **SF Knowledge Article**: https://braze.lightning.force.com/lightning/r/Knowledge__kav/ka0VP000000F9hJYAS/view
- **CSV Match**: Yes
- **Ready to Draft**: Yes (CSV match + detailed ticket)

---

**48 of 65 actionable tickets have CSV matches and can be auto-drafted.**
To proceed, say: "Run Phase 2 for the top N tickets" or "Run Phase 2 for BD-XXXX".
For tickets without CSV matches, paste the article content manually.