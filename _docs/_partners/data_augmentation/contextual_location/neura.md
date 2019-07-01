---
nav_title: Neura
alias: /partners/neura/
---

# Neura Integration

Braze enables you to unlock the power of real-world engagement opportunities and drive effective and intelligent customer journeys. Braze provides a seamless product integration with consumer-centric intelligence company [Neura][1]. Transform Neura’s live consumer insights into action in near real-time using Braze to create personal experiences between users and your brand.

-   Leverage Neura’s [True Personas™][2] segment users based on their behavioral traits.
-   Leverage [Neura Moments™][3] when triggering campaigns to deliver personal messaging experiences.

![neura-real-world-personas-moments.png][11]

## Integration Details

To get started, ensure that the Braze and Neura SDKs are properly integrated for Android and iOS.

To integrate the Neura SDK you simply add a few lines of code to your [AppDelegate on iOS][8] or [MainActivity class on Android][4]. You’ll then begin receiving [Neura Moments™][3], on the device or to a webhook, as Braze custom events. You’ll also gain the ability to segment users based on their real-world lifestyles and habits, [True Personas™][2], and turn those into Braze user attributes.

![neura-personas-moments.png][10]

In order to properly map the Braze and Neura SDKs, you will need to set the `external_id` chosen by you as the `external_id` inside Neura’s SDK. Neura will add a user alias with Neura’s id to bind between the ids.

Next, find your App ID on the Developer Console section of the Braze Dashboard and create a new API Key with `users.track` and `users.alias.new` permissions.

![neura-braze-api-key.png][12]

Enter your Braze REST API Key and (optionally) App IDs in the Neura Console (for each integrated mobile platform):

![neura-mep-details-in-neura.png][13]

Once you have configured the Neura Console, the Neura API will automatically uncover engagement opportunities and forward them to Braze, allowing you to target and segment your customers. See the [Neura developer site][6] for more details, tutorials, and FAQs.

{% alert note %}
The Neura SDK requires that you enable location services.
{% endalert %}


[1]: https://www.theneura.com/
[2]: https://dev.theneura.com/api-reference/persona/?ref=braze
[3]: https://dev.theneura.com/api-reference/situations-and-moments/?ref=braze
[4]: https://dev.theneura.com/tutorials/android/?ref=braze
[5]: https://dev.theneura.com/tutorials/android
[6]: https://dev.theneura.com/?ref=braze
[7]: https://dev.theneura.com/api-reference/behavioral-profile/?ref=braze
[8]: https://dev.theneura.com/tutorials/ios/?ref=braze

[10]: {% image_buster /assets/img_archive/neura-personas-moments.png %}
[11]: {% image_buster /assets/img_archive/neura-real-world-personas-moments.png %}
[12]: {% image_buster /assets/img_archive/neura-braze-api-key.png %}
[13]: {% image_buster /assets/img_archive/neura-mep-details-in-neura.png %}
[14]: {% image_buster /assets/img_archive/neura-persona_diagram.png %}
[15]: {% image_buster /assets/img_archive/neura-personas-in-braze.png %}
[16]: {% image_buster /assets/img_archive/neura-moments_diagram.png %}
[17]: {% image_buster /assets/img_archive/neura-moments-in-braze.png %}
