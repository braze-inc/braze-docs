---
nav_title: Reporting
page_order: 7
---
# Reporting {#IAM-Reporting}

In the details for an in-app message campaign, you can find detailed performance statistics. Below is an example campaign statistics page.

![Campaign Details][13]

It is important to understand the significance of and difference between the Current Audience, Unique Recipients, and Impressions.

- Current Audience refers to the number of users eligible to receive the message based on segmentation filters and [triggers][15] you set up in the campaign. A user would be counted multiple times in the Current Audience if they receive the campaign more than once.
- Unique Recipients represents the number of users whose SDK has received the message. As in-app messages are not delivered to the user until a new session is started, this number will climb up from zero as users in the Current Audience open the app.
- Impressions are the number of users whose devices have reported that the message has been displayed.

For an example of how Current Audience and Unique Recipients differ, imagine an in-app message campaign targeting a segment with 15K users. At the moment the campaign is launched, the Current Audience would be 15K. After an hour, if 5K users from the segment have started a new session, the number of Unique Recipients would only be 5K.

Impressions and Unique Recipients should be very similar numbers, however they can differ if you have customized the time in-app messages are displayed, in which case the impression can be recorded after the start of a new session, or if some users have recorded an impression but closed the app before the impression was sent to our servers, so the impression will be logged during their next session.

Previously, Unique Recipients were defined similarly to Current Audience. As Unique Recipients are used as the denominator for the conversion rate, conversion rates for current campaigns may be higher than those in older campaigns.

[1]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[5]: {% image_buster /assets/img_archive/inappexample.png %}
[7]: {{ site.baseurl }}/help/faqs/
[8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/#manually-queue-in-app-message-display
[9]: {{ site.baseurl }}/developer_guide/platform_integration_guides/web/in_app_messaging/#slideup-in-app-messages
[10]: {% image_buster /assets/img_archive/braze_fullscreen.png %}
[11]: {% image_buster /assets/img_archive/braze_modal.png %}
[12]: {% image_buster /assets/img_archive/stopwatch_slideup_IAM.gif %}
[13]: {% image_buster /assets/img_archive/braze_campaigndetails.png %}
[14]: {% image_buster /assets/img_archive/web-email-capture.png %}
[15]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#action-based-delivery-event-triggered-campaigns
[16]: {% image_buster /assets/img_archive/braze_customhtml.png %}
[17]: {% image_buster /assets/img_archive/HTML5.gif %}
[18]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_05.png %}
[19]: {% image_buster /assets/img_archive/In-AppMsg_Mockups+Specs_06.png %}
[20]: {% image_buster /assets/img_archive/braze_campaignpriority.png %}
[21]: {{ site.baseurl }}/help/best_practices/push/#creating-custom-opt-in-prompts
[22]: https://github.com/Appboy/appboy-custom-html5-in-app-message-templates
[23]: https://www.picsart.com?abButtonId=0
[25]: https://imageoptim.com/
