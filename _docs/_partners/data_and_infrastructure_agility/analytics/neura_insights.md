---
nav_title: Neura Insights
article_title: Neura
alias: /partners/neura/
description: "This article outlines the partnership between Braze and Neura Actions and Insights, a behavior intelligence platform, providing mobile brands the tools to drive higher customer engagement and retention."
page_type: partner
search_tag: Partner

---

# Neura Actions and Insights

> [Neura][1] helps leading mobile brands drive higher customer engagement and retention with AI-powered, real-world behavioral insights, and advanced campaign segmentation and triggering.

{% tabs local %}
{% tab Actions %}

The Neura and Braze integration allows you to create segments and audiences with Neura's [True Personas™](https://dev.theneura.com/api-reference/persona/?ref=braze)) and trigger campaigns to reach users with [Neura Moments™](https://dev.theneura.com/api-reference/situations-and-moments/?ref=braze).

![Moments of availability]({% image_buster /assets/img_archive/neura-personas-moments.png %}){: style="border:0"}

{% endtab %}
{% tab Insights %}
The Braze and Neura integration allows you to leverage [Neura Insights](https://www.theneura.com/neura-insights/?ref=braze) to uncover the relationships between users real-world behavior and the actions they take in your app to find the best moment to engage with each user.

![Insights Bubble Graph]({% image_buster /assets/img/insights-bubble-graph.png %})
{% endtab %}
{% endtabs %}

## Prerequisites

| Requirement | Description |
|---|---|
| Neura account | A Neura account is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `users.track`, `users.alias.new`, and `users.export.ids` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Server region | This is your Braze REST API endpoint and can be found in our [Braze API documentation]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

To get started, ensure that both the Braze and Neura SDKs are properly integrated for both Android and iOS. 

{% tabs local %}
{% tab Actions %}
To integrate the Neura SDK, add short code snippets found in step 2 to your [AppDelegate on iOS](https://dev.theneura.com/tutorials/ios/?ref=braze) or [MainActivity class on Android](https://dev.theneura.com/tutorials/android/?ref=braze). You'll then begin receiving [Neura Moments™](https://dev.theneura.com/api-reference/situations-and-moments/?ref=braze) as Braze custom events. You'll also gain the ability to segment users based on their real-world lifestyles and habits, [True Personas™](https://dev.theneura.com/api-reference/persona/?ref=braze), received as Braze custom attributes.
{% endtab %}
{% tab Insights %}
To integrate the Neura SDK, add short code snippets found in step 2 to your [AppDelegate on iOS](https://dev.theneura.com/tutorials/ios/?ref=braze) or [MainActivity class on Android](https://dev.theneura.com/tutorials/android/?ref=braze). 
{% endtab %}
{% endtabs %}

### Step 1: Add Braze in Neura

Add a new mobile engagement platform in the [Neura console][7]. Here, you will be asked to provide the following information:

- API Key: The key you've created in the Braze platform.
- Region: Braze manages server endpoints in different regions. Use your region as the input to the "Server" field.
- Android/iOS App ID: We recommend providing a unique Braze application ID for each mobile platform, allowing you to segment the users for each platform individually.

![Neura MEP Details in Neura][12]

### Step 2: Map Neura users to Braze

Next, ensure that Braze and Neura users are mapped to one another. To do this, create a user alias labeled `neura_id` with your user's neura_id and set a custom user attribute with the key-value pair `neura, true`.

{% tabs local %}
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

Lastly, make sure the external ID is set. Similarly to when the `changeUser` method is called in Braze (as soon as the user gets identified, generally after logging in, to set the user id), we recommend also setting the user ID as an External ID in Neura:

{% tabs local %}
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

See the [Neura developer site][8] for more details, tutorials, and FAQs.

{% alert note %}
The Neura SDK requires that you enable location services.
{% endalert %}

## Neura Actions

### Trigger Campaign 

Once both SDKs are integrated, you can set up a campaign or Canvas in the Braze dashboard to be triggered by Neura Moments, available in the Braze platform as custom events.

![action-based-delivery.png]({% image_buster /assets/img/action-based-delivery.png %})

### Create Braze segment

Neura recognizes real-world behavioral traits for each user. Using Braze, you can create segments to target specific users based on their True Personas™, available in the Braze platform as custom attributes.

![segment-creation.png]( {% image_buster /assets/img/segment-creation.png %})

## Neura Insights

Neura's generic data import allows for two types of import methods:

1. Export your Currents data to Amazon S3. Our Customer Success team will work with you to translate the data to Neura.
2. Follow the instructions to use the Neura [Insights API](https://dev.theneura.com/pages/how-to-use-engagement-api/?ref=braze).

Neura closes the loop by sending actionable data back to Braze, so you can seamlessly execute on Neura's real-world insights right within Braze.
After you've identified the right engagement moment for the right user, easily create campaigns and Canvases with Neura Actions in Braze.

![insights-moments-personas.png]({% image_buster /assets/img/insights-moments-personas.png %})

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
[19]: {% image_buster /assets/img/insights-bubble-graph.png %}