---
nav_title: Neura Actions
alias: /partners/neura_actions/

description: "This article outlines the partnership between Braze and Neura Actions. This integration leads mobile brands to drive higher customer engagement and retention."
page_type: partner

---

# Neura Actions Integration

> [Neura][1] helps leading mobile brands drive higher customer engagement & retention with AI-powered, real-world behavioral insights and advanced campaign segmentation & triggering.

*Leverage Neura's [True Personas™][2] to create segments and audiences based on each users' lifestyle and preferences. Leverage [Neura Moments™][3] when triggering campaigns to reach each user when they're available and receptive.*

![moments-of-availability.png][9]

See the [Neura Insights][4] Braze integration for further details on how to uncover these real-world behavioral insights.

## Integration Details

To get started, ensure that both the Braze and Neura SDKs are properly integrated for Android and iOS.

To integrate the Neura SDK you simply add a few lines of code to your [AppDelegate on iOS][5] or [MainActivity class on Android][6]. You’ll then begin receiving [Neura Moments™][3] as Braze custom events. You’ll also gain the ability to segment users based on their real-world lifestyles and habits, [True Personas™][2], received as Braze custom attributes.

![neura-personas-moments.png][10]

First, find your App ID on the "Developer Console" section of the Braze Dashboard and create a new API Key with `users.track`, `users.alias.new` and `users.export.ids` permissions.

![neura-braze-api-key.png][11]

Complete the Mobile Engagement Platform section of your application in the [Neura console][7], as follows:

**API Key:** Insert the key you've created in the Braze platform.

**Region:** Braze manages server endpoints in different regions. Use your region as the input to the "Server" field.

**Android/iOS App ID:** We recommend providing a unique Braze application ID for each mobile platform, allowing you to segment the users for each platform individually.

![neura-mep-details-in-neura.png][12]

Last, ensure that Braze and Neura users are mapped:
Create a user alias labeled `neura_id` with your user's neura_id
Set a custom user attribue with the key-value pair `neura, true`

{% tabs %}
  {% tab iOS %}
```objc
[[Appboy sharedInstance].user addAlias:NEURA_USER_ID withLabel:@"neura_id"];
[[Appboy sharedInstance].user setCustomAttributeWithKey:@"neura" andBOOLValue:true];
```
  {% endtab %}
  {% tab Android %}
```java
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().addAlias(NEURA_USER_ID, "neura_id");
Appboy.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setCustomUserAttribute("neura", true);
```
  {% endtab %}
{% endtabs %}

Set External ID:  Similar to when the changeUser method should be called in Braze (as soon as the user gets identified, generally after logging in, in order to set the user id), we recommend also setting the user ID as an External ID in Neura:

{% tabs %}
  {% tab iOS %}
```objc
NExternalId *externalIdObj = [[NExternalId alloc] initWithExternalId:@"USER_ID"];
NeuraSDK.shared.externalId = externalIdObj;
```
  {% endtab %}
  {% tab Android %}
```java
mNeuraApiClient.setExternalId(USER_ID)
```
  {% endtab %}
{% endtabs %}

## Using Neura with Braze

Once both SDKs are integrated, you can set up a campaign or Canvas in the Braze Dashboard to be trigged by Neura Moments, which are available in the Braze platform as custom events.

![action-based-delivery.png][13]

In addition, Neura recognizes real-world behavioral traits for each individual user. Using Braze, you will be able to target specific users based on their True Personas™, which are available in the Braze platform as custom attributes.

![segment-creation.png][14]

See the [Neura developer site][8] for more details, tutorials, and FAQs.

{% alert note %}
The Neura SDK requires that you enable location services.
{% endalert %}


[1]: https://www.theneura.com/
[2]: https://dev.theneura.com/api-reference/persona/?ref=braze
[3]: https://dev.theneura.com/api-reference/situations-and-moments/?ref=braze
[4]: {{site.baseurl}}/partners/insights/behavioral_analytics/neura_insights
[5]: https://dev.theneura.com/tutorials/ios/?ref=braze
[6]: https://dev.theneura.com/tutorials/android/?ref=braze
[7]: https://dev.theneura.com/console/
[8]: https://dev.theneura.com/?ref=braze

[9]: {% image_buster /assets/img/moments-of-availability.png %}
[10]: {% image_buster /assets/img_archive/neura-personas-moments.png %}
[11]: {% image_buster /assets/img/neura-braze-api-key.png %}
[12]: {% image_buster /assets/img_archive/neura-mep-details-in-neura.png %}
[13]: {% image_buster /assets/img/action-based-delivery.png %}
[14]: {% image_buster /assets/img/segment-creation.png %}
