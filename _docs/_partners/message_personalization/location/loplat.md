---
nav_title: loplat
article_title: loplat
description: "This article outlines the partnership between Braze and loplat, an offline location-based marketing platform, to allow you to execute proximity marketing campaigns by adding location context."
alias: /partners/loplat/
page_type: partner
search_tag: Partner

---

# loplat

> [Loplat][1] is the leading offline location-based platform. Use loplat SDK to increase your store's footfall smartly and execute marketing campaigns that encourage in-store purchases. You can measure the store performance through footfall analysis after the campaign ends.

The Braze and loplat integration allows you to use loplat's location services (store POI and custom geofence) to trigger geo-contextual marketing campaigns and create custom events using offline segmentation. When users visit the targeted location you set in loplat X, the campaign and location information are sent immediately to Braze.

## Prerequisites

| Requirement | Description |
| --- | --- |
| loplat X account | A loplat X account is required to take advantage of this integration.<br><br>Email [support@loplat.com][3] to request a loplat X account. |
| loplat SDK | loplat SDK recognizes users' store visits, processes location events, and distinguishes whether users are staying at a place or moving. You can use loplat SDK to analyze your store's footfall, send push messages when users enter your store, etc.<br><br>Note that the SDK is only available for Android and iOS. |
| Braze REST API key | A Braze REST API key with the following permissions:<br>- `users.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br><br>This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key.** |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases

The custom event location information provided by loplat can be used in your campaigns to achieve use cases like:

- [Duty-free promotion alert][2]
    - Send duty-free shop discount coupons to the users who are near the boarding gates at the airport.
- Electric vehicle (EV) charging station location push
    - Set geofences around EV charging stations and notify users when they are nearby the station and encourage them to charge.

## Integration

### Step 1: Integrate the SDKs

Integrate the loplat SDK and the Braze SDK in your app using the steps provided in the [loplat-Braze integration][4] documentation.

### Step 2: Sync the Braze and loplat X dashboards and create a campaign

Create a new API key in the Braze dashboard. Copy the API key and paste it at **Settings > API Settings** in the loplat X dashboard. See the [loplat X user's guide](https://loplat-loplat.gitbook.io/loplat-x-user-guide-en/integration/braze) for more details.

#### API-triggered delivery

1. Create a Braze campaign or Canvas that sends with **API-Triggered Delivery**, and copy the campaign ID.
2. Launch the campaign in Braze after completing all steps.
3. Go to loplat X and create a campaign following the instructions in the [loplat X user's guide][5].
4. Paste the Braze campaign ID under the **Campaign Message Settings**, and launch the campaign.

![][7]

#### Action-based delivery

With the integration, you can apply location conditions by sending geofence information, region, brand name, or store name. In addition, you can add segments or assign conversion with the custom event you created.
1. Create a loplat X campaign following the instructions in the [loplat X user's guide][6].
2. Add a custom event under the **Campaign Message Settings** and launch the campaign.
3. Go to the Braze dashboard and create a campaign or Canvas that sends with **Action-Based Delivery**.
4. Select the custom event you created in loplat X to set a location trigger action.

![][8]

[1]: https://www.loplat.com/
[2]: https://www.loplat.com/loplat-x#usecase
[3]: mailto:support@loplat.com
[4]: https://developers.loplat.com/braze/
[5]: https://loplat-loplat.gitbook.io/loplat-x-user-guide-en/campaigns/create/campaign-integration#1.-braze-greater-than-loplat-x-api-triggered-delivery
[6]: https://loplat-loplat.gitbook.io/loplat-x-user-guide-en/campaigns/create/campaign-integration
[7]: {% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %}
[8]: {% image_buster /assets/img/loplat/loplat_action_based_delivery.png %}