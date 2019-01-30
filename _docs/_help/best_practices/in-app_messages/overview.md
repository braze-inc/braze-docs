---
nav_title: Overview
page_order: 0
---
# In-App Messages

With the ability to leverage multiple in-app message formats, you can choose a layout that best suits your content and campaign goal. Because these formats look and interact with your users differently, they are best suited for different use cases.

## Best Practices {#in-app-best-practices}

- This type of message is best for users who regularly visiting your app, as your audience will only see the greeting when the app is opened.
- Compared to an email correspondence or News Feed card, an in-app message generally appears for a set amount of time, so the text should be concise.
- They can be particularly effective in driving feature discovery, encouraging and rewarding discovery or upselling via in-app purchases.
- Add [protocol URLs][1] to direct your audience to another part of your app and personalize their experience.
- For in-app messages containing an image, Braze improves load times by using a global CDN to host the image.
- In-app messages are great for priming users to accept a permission request (i.e. [push priming][21]).
- The aspect ratio of images are maintained and fill whichever dimension that we hit the boundary for first. No part of the image that is positioned within the image safe zone will be cropped. We recommend that images fit on a 16:10 screen, which means:
  - A portrait fullscreen with text: 5:4 image
  - Portrait fullscreen (with image only): 10:16 image
  - Landscape fullscreen with test: 16:5 image
  - Landscape fullscreen (image only): 16:10 image

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
[21]: {{ site.baseurl }}/help/best_practices/push/creating_custom_opt-in_prompts/#creating-custom-opt-in-prompts
[22]: https://github.com/Appboy/appboy-custom-html5-in-app-message-templates
[23]: https://www.picsart.com?abButtonId=0
[25]: https://imageoptim.com/
