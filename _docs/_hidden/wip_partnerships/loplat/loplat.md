---
nav_title: loplat
article_title: loplat
page_order: 1

description: "This article outlines the partnership between Braze and loplat, an offline location-based marketing platform, to allow you to execute proximity marketing campaigns by adding location context."
alias: /partners/loplat/

page_type: partner
search_tag: Partner
hidden: true

---

# loplat

> [Loplat][loplat] is the leading offline location-based platform. Use loplat SDK to increase your store's footfall smartly and execute marketing campaigns that encourage in-store purchases. You can measure the store performance through footfall analysis after the campaign ends.

The Braze and loplat integration allows you to use loplat’s location services (store POI and custom geofence) to trigger geo-contextual marketing campaigns and create custom events using offline segmentation. When users visit the targeted location you set in loplat X, the campaign and location information are sent immediately to Braze.

## Prerequisites

| Requirement | Description |
| --- | --- |
| loplat X account | A loplat X account is required to take advantage of this integration. |
| loplat SDK | loplat SDK recognizes users’ store visits, processes location events, and distinguishes whether users are staying at a place or moving. You can use loplat SDK to analyze your store’s footfall, send push messages when users enter your store, etc.<br>(SDK is available only for Android and iOS.) |
| Braze REST API key | A Braze REST API key with the below permissions.<br>**Permissions**<br>- `user.track`<br>- `campaigns.trigger.send`<br>- `campaigns.list`<br>- `canvas.trigger.send`<br>- `canvas.list`<br>This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key.** |
{: .reset-td-br-1 .reset-td-br-2}

## Use cases
The custom event location information provided by loplat can be used in your campaigns to achieve use cases like:

- [Duty-free promotion alert][usecase]
    - Send duty-free shop discount coupons to the users who are near the boarding gates at the airport.
- EV charging station location push
    - Set geofences around EV charging stations and notify users when they are nearby the station and encourage them to charge.

## Integration
### Step 1: Create a loplat X account
Email [support@loplat.com][support] to request a loplat X account.
### Step 2: Integrate the SDKs
Integrate the loplat SDK and the Braze SDK in your app using the steps provided in the [loplat-Braze integration][integration] documentation.
### Step 3: Sync the Braze and loplat X dashboards and create a campaign
Create a new API key in the Braze dashboard. Copy the API key and paste it at Settings > API Settings in the loplat X dashboard. See the [loplat X User’s Guide](https://loplat-loplat.gitbook.io/loplat-x-user-guide-en/integration/braze) for more details.
#### API-Triggered Delivery
- Create a Braze campaign or Canvas that sends with **API-Triggered Delivery**, and copy the campaign ID.
- Launch the campaign in Braze after completing all steps.
- Go to loplat X and create a campaign following the instructions in the [loplat X User’s Guide][api-triggered-guide].
- Paste the Braze campaign ID under the **Campaign Message Settings**, and launch the campaign.
![API Triggered Delivery][img-api-triggered]
#### Action-Based Delivery
With the integration, you can apply location conditions by sending geofence information, region, brand name, or store name. In addition, you can add segments or assign conversion with the custom event you created.
- Create a loplat X campaign following the instructions in the [loplat X User’s Guide][custom-event-guide].
- Add a custom event under the **Campaign Message Settings** and launch the campaign.
- Go to the Braze dashboard and create a campaign or Canvas that sends with **Action-Based Delivery**.
- Select the custom event you created in loplat X to set a location trigger action.
![Action Based Delivery][img-action-based]

[loplat]: https://www.loplat.com/
[usecase]: https://www.loplat.com/loplat-x#usecase
[support]: mailto:support@loplat.com
[integration]: https://developers.loplat.com/braze/
[api-triggered-guide]: https://loplat-loplat.gitbook.io/loplat-x-user-guide-en/campaigns/create/campaign-integration#1.-braze-greater-than-loplat-x-api-triggered-delivery
[custom-event-guide]: https://loplat-loplat.gitbook.io/loplat-x-user-guide-en/campaigns/create/campaign-integration
[img-api-triggered]: {% image_buster /assets/img/loplat/loplat_api_triggered_delivery.png %}
[img-action-based]: {% image_buster /assets/img/loplat/loplat_action_based_delivery.png %}