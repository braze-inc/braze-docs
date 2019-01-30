---
nav_title: In-App Message Specs
page_order: 4
---

# In-App Message Specs

## Character and Image Limits:

| Type                               | Aspect Ratio | Recommended Image Size | Max Image Size |   File Types  | Max Character Count |
|------------------------------------|:------------:|:----------------------:|:--------------:|:-------------:|:-------------------:|
| Portrait Full Screen (With Text)   |      5:4     |          500KB         |       5MB      | PNG, JPG, GIF |         240         |
| Portrait Full Screen (Image Only)  |     10:16    |          500KB         |       5MB      | PNG, JPG, GIF |         240         |
| Landscape Full Screen (With Text)  |     16:5     |          500KB         |       5MB      | PNG, JPG, GIF |         240         |
| Landscape Full Screen (Image Only) |     16:10    |          500KB         |       5MB      | PNG, JPG, GIF |         240         |
| Slideup                            |      1:1     |          500KB         |       5MB      | PNG, JPG, GIF |         140         |
| Modal (Image Only)                 |      1:1     |          500KB         |       5MB      | PNG, JPG, GIF |         140         |
| Modal (With Text)                  |     29:10    |          500KB         |       5MB      | PNG, JPG, GIF |         140         |


## Keeping In-App Message File Sizes Small

Braze recommends you keep your images, and HTML assets zips as small as possible for several reasons:

- Smaller HTML & image message payloads will download faster, and display more quickly and reliably for your customers.
- Smaller HTML & image message payloads will keep your customer's data costs down as well. Braze in-app messages are downloaded in the background on session start so they can be triggered in real-time based upon whatever criteria you select. As a result, if you have 10 HTML in-app messages of 1MB each, your customers would all incur 10MB of data charges even if they never triggered all of those messages. This can add up quickly over time, even though the in-app messages are cached and not re-downloaded session to session.

The following strategies are helpful for keeping file sizes down:

- Reference fonts embedded in your application / website to customize your HTML in-app messages rather than including the font files in your HTML asset zip folder.
- Ensure no extraneous or duplicative CSS or JS are included in your HTML asset zips.
- Use [ImageOptim][25] on all images to compress images to their minimum possible size with no reduction in quality.

### iPhone 5 Specs:
![iPhone 5 Specs][18]

### iPhone 6 Specs:
![iPhone 6 Specs][19]

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
