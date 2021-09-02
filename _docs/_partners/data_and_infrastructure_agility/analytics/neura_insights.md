---
nav_title: Neura Insights
article_title: Neura Insights
page_order: 0
alias: /partners/neura_insights/

description: "This article outlines the partnership between Braze and Neura Insights, an analytics platform that allows you to uncover the relationships between each user’s real-world behavior and the actions they take in your app in order to find the best moment to engage with each user."
page_type: partner
search_tag: Partner

---

# Neura Insights

> [Neura][1] helps leading mobile brands drive higher customer engagement & retention with AI-powered, real-world behavioral insights and advanced campaign segmentation & triggering.

*Leverage [Neura insights][2] to uncover the relationships between each user’s real-world behavior and the actions they take in your app in order to find the best moment to engage with each user.*

![insights-bubble-graph.png][9]

## Integration Details

To integrate the Neura SDK you simply add a few lines of code to your [AppDelegate on iOS][3] or [MainActivity class on Android][4].

First, find your App ID on the "Developer Console" section of the Braze Dashboard and create a new API Key with `users.track`, `users.alias.new` and `users.export.ids` permissions.

![neura-braze-api-key.png][10]

Complete the Mobile Engagement Platform section of your application in the [Neura Console][5], as follows:

**API Key:** Insert the key you've created in the Braze platform.

**Region:** Braze manages server endpoints in different regions. Use your region as the input to the "Server" field.

**Android/iOS App ID:** We recommend providing a unique Braze application ID for each mobile platform, allowing you to segment the users for each platform individually.

![neura-mep-details-in-neura.png][11]

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
Braze.getInstance(YOUR_ACTIVITY.this).getCurrentUser().addAlias(NEURA_USER_ID, "neura_id");
Braze.getInstance(YOUR_ACTIVITY.this).getCurrentUser().setCustomUserAttribute("neura", true);
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

## Sending Engagement Data to Neura

Neura's generic data import allows for two types of import methods:

1. Export your Currents data to Amazon S3. Our customer success team will work with you to translate the data to Neura.

2. Follow the instructions to use the Neura [Insights API][6].

Neura closes the loop by sending actionable data back to Braze, so you can seamlessly execute on Neura's real-world insights right within Braze.
After you've identified the right engagement moment for the right user, easily create campaigns and Canvases with [Neura Actions in Braze][7].

![insights-moments-personas.png][12]

See the [Neura developer site][8] for more details, tutorials, and FAQs.

{% alert note %}
The Neura SDK requires that you enable location services.
{% endalert %}


[1]: https://www.theneura.com/
[2]: https://www.theneura.com/neura-insights/?ref=braze
[3]: https://dev.theneura.com/tutorials/ios/?ref=braze
[4]: https://dev.theneura.com/tutorials/android/?ref=braze
[5]: https://dev.theneura.com/console/
[6]: https://dev.theneura.com/pages/how-to-use-engagement-api/?ref=braze
[7]: {{site.baseurl}}/partners/data_augmentation/contextual_location/neura
[8]: https://dev.theneura.com/?ref=braze

[9]: {% image_buster /assets/img/insights-bubble-graph.png %}
[10]: {% image_buster /assets/img/neura-braze-api-key.png %}
[11]: {% image_buster /assets/img_archive/neura-mep-details-in-neura.png %}
[12]: {% image_buster /assets/img/insights-moments-personas.png %}
