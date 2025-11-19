{% if include.page == "testing" %}While [composing your Banner message]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/#compose-a-banner), select{% elsif include.page == "campaigns" %}Select{% endif %} **Preview** to you preview your Banner or send a test message.

![Preview tab of the Banner composer.]({% image_buster /assets/img/banners/select_preview.png %}){: style="max-width:50%;"}

Keep in mind, your preview may not be identical to the final render on a user's device due to differences across hardware.

To send a test message, add either a content test group or one or more individual users as **Test Recipients**, then select **Send Test**. You'll be able to view your test message on the device for up to 5 minutes. You can then select **Copy preview link** to generate and copy a shareable preview link that shows what the banner will look like for a random user. The link will last for seven days before it needs to be regenerated.

![Preview tab of the Banner composer.]({% image_buster /assets/img/banners/preview_banner.png %})

While reviewing your test Banner, verify the following:

- Is your Banner campaign assigned to a placement?
- Do the images and media show up and act as expected on your targeted device types and screen sizes?
- Do your links and buttons direct the user to where they should go?
- Does the Liquid function as expected? Have you accounted for a default attribute value in the event that the Liquid returns no information?
- Is your copy clear, concise, and correct?
