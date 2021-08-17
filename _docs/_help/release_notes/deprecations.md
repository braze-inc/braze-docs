---
nav_title: Deprecations
page_order: 9
layout: featured

guide_top_header: "Deprecations"
guide_top_text: "Technology is always moving - inside Braze and outside it! And we do our best to keep up with it. Here, you'll find the origins of Braze and its technology - how we supported people in the 'before time' - before now, anyway... <br> <br> You might have gotten here from searching a term for an integration or feature that no longer exists. This is our attempt to keep you informed on our progress and movement within the technology industry. <br> <br> You can find a list of deprecated and unsupported features below. You can also read deprecated articles by clicking on the buttons below."

page_type: landing
description: "This landing page includes references to deprecated articles and provides a list of deprecated and unsupported features."

guide_featured_title: "Deprecated Articles"
guide_featured_list:
  - name: Apptimize Partnership
    link: /docs/help/release_notes/deprecations/apptimize/
    fa_icon: fas fa-vials
  - name: Eclipse SDK Setup
    link: /docs/help/release_notes/deprecations/eclipse_setup_deprecated/
    fa_icon: fas fa-circle
  - name: "TLS 1.0 & 1.1 Deprecation"
    link: /docs/help/release_notes/deprecations/tls_deprecation/
    fa_icon: fas fa-lock


---


## Apptimize

_Braze Partnership_

_Support withdrawn: August 2019_

If you are currently using [Apptimize with Braze]({{site.baseurl}}/help/release_notes/deprecations/apptimize), you will not experience a disruption of service. You can still set Apptimize custom attributes to Braze user profiles. However, no formal escalation support with the partner will be provided.


## Original In-App Messages

_Replaced by: [In-App Messaging]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creating_an_in-app_message)_

_Braze Feature_

_Support completely withdrawn: February 2019_

Braze has improved the look and feel of In-App Messages to adhere to the latest UX and UI best practices and no longer supports original in-app messages.

Braze moved over to a new form of in-app messages with the following SDK releases:

- iOS: `2.19.0`
- Android: `1.13.0`
- Web: `1.3.0`

Prior to these releases, Braze supported "original in-app messages." Previously, support for original in-app messages was provided for any customer who ran an in-app campaign prior to the new release. All of the campaign stats were unaffected by the change, and those who had sent original in-app messages had the opportunity to send others via the **Create Campaign** button on the **Campaign** page.

![Choices][15]


## Feedback

_Braze Feature_

_Support to be completely withdrawn July 1, 2019._

The Braze SDK provided a feedback widget that could be added to your app to allow users to leave feedback using the submitFeedback method and pass it into either Desk.com or Zendesk and was managed on the dashboard.

## Google Cloud Messaging (GCM)

_Replaced by: [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase)_

_Integration_

_Support withdrawn: July 2018 (Braze removal of support) and May 29, 2019 (Google removal of support)._

[Google has removed support for GCM](https://developers.googleblog.com/2018/04/time-to-upgrade-from-gcm-to-fcm.html) as of May 29, 2019. Braze removed support for GCM from the Android SDKs in July 2018, which was noted within [our Android SDK changelogs](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md). This means that existing GCM tokens will continue to work and you will be able to message your existing users. However, you will not be able to message new users.

Customers that have not already migrated to [Firebase Cloud Messaging (FCM)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-1-enable-firebase) may be affected by this change.

If you have not transitioned to FCM, all GCM push tokens registrations will fail. If your apps are currently supporting GCM, you’ll need to work with your development teams on [transitioning from GCM to Firebase Cloud Messaging (FCM)](https://developers.google.com/cloud-messaging/android/android-migrate-fcm).

## Eclipse

_Replaced by: [Android Studio]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#using-android-studio)_

_Integration_

_Support withdrawn: 2014-2015_

Braze has removed support for the Eclipse IDE due to [Google sunsetting support for the Eclipse Android Developer Tools Plugin](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). If you need assistance with your Eclipse integration prior to migration please [email Support]({{site.baseurl}}/support_contact/) for assistance.

## The Raw Event Stream (RES)

_Replaced by: [Currents]({{site.baseurl}}/partners/braze_currents/about/)_

_Braze Feature_

_Support withdrawn: July 2018_

The Raw Event Stream was the predecessor to [Currents]({{site.baseurl}}/partners/braze_currents/about/) and was deprecated to make room for the future of Braze data.

## Delay While Idle

_Replaced by: n/a_

_GCM Feature_

_Support withdrawn: November 2016_

The Delay While Idle parameter was previously a part of the [GCM push options](https://developers.google.com/cloud-messaging/http-server-ref). Google withdrew support for this option on November 15th 2016. Previously, when set to **true**, it indicated that the message should not be sent until the device becomes active.

## Custom Endpoints

_Replaced by: n/a_

_Braze Feature_

_Support withdrawn: December 2019_

Removal of Custom Endpoints. If you have a custom endpoint, you can still continue to use it, but Braze no longer gives them out.




[15]: {% image_buster /assets/img_archive/in-app-choices.png %}
