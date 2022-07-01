---
nav_title: Setting up Shopify
article_title: "Setting up Shopify"
description: "This article outlines how to set up Shopify, a global commerce company that allows you to seamlessly connect their Shopify store with Braze to pass select Shopify webhooks into Braze."
page_type: partner
search_tag: Partner
permalink: "/setting_up_shopify/"
hidden: true

---

# Setting up Shopify

> [Shopify](https://www.shopify.com/) is a leading global commerce company providing trusted tools to start, grow, market, and manage a retail business of any size. Shopify makes commerce better for everyone with a platform and services engineered for reliability while delivering a better shopping experience for consumers everywhere. 

The Shopify and Braze integration allows brands to connect their Shopify store seamlessly to pass select Shopify webhooks into Braze. Leverage Braze's cross-channel strategies and Canvas to retarget your users with abandoned checkout messaging to nudge customers to complete their purchase or retarget users based on their previous purchases. 

## Prerequisites

All Braze customers looking to utilize the Shopify integration must sign Braze's Shopify order form. Reach out to your account executive for more details.

This integration will create alias user profiles if we are unable to match Shopify data using the email or phone number. Refer to the following section for more information on [Shopify user reconciliation]({{site.baseurl}}/shopify_data/#user-reconciliation). Consult with your development teams around the downstream impacts and need to merge these user profiles as part of your user lifecycle before you enable the integration. 

| Requirement | Description |
| ----------- | ----------- |
| Shopify store | You must have an active [Shopify](https://www.shopify.com) store.<br><br>Note that at this time, you are only able to connect one Shopify store per app group. |
| Event property segmentation enabled | To ensure you can segment your Shopify events properties, you must work with your customer success manager or [Braze support]({{site.baseurl}}/braze_support/) to confirm that you have event property segmentation enabled for your dashboard. |
| Nested custom attribute support | This will be enabled with the Spotify integration.<br><br>You will be given access to this feature to receive Shopify marketing opt-in custom attributes. |
{: .reset-td-br-1 .reset-td-br-2}

## What's supported in the integration?

- Integrating the Braze Web SDK via Shopify ScriptTag
- Shopify user data syncing into Braze
- Ability to orchestrate the following multi-channel eCommerce user cases:
   - Path to purchase user journeys
   - Abandoned cart and checkout user journeys
   - Post-purchase retargeting
   - Transactional messaging

## Integration

The types of Shopify use cases you intend on supporting will determine the integration path you will set up within the onboarding process in the Braze dashboard.

<style>
    table {
        table-layout: fixed;
        width: 100%;
    }
    table td {
    word-break: break-word;
    }
</style>

| Intended use case | Integration method |
| -------- | ------------------ |
| Retarget customers as they start their path to purchase. You can retarget using the following top-of-funnel eCommerce events:<br>   • Product clicked<br>   • Product viewed<br>   • Abandoned cart | Braze Web SDK via Shopify ScriptTag |
| Support abandoned checkout, purchase, and post-purchase targeting:<br>   • Abandoned checkout<br>   • Order created<br>   • Braze purchase event | Shopify webhooks |
| Support transactional marketing messaging:<br>   • Order paid<br>   • Order fulfillment<br>   • Partial order fulfilment<br>   • Order cancellation<br>   • Order refund | Shopify webhooks |
|Anonymous user tracking | Braze Web SDK via Shopify ScriptTag |
| Channel support:<br>   • In-browser messaging | Braze Web SDK via Shopify ScriptTag |

### Step 1: Locate Shopify within the dashboard
In Braze, go to the **Technology Partners** section and then search **Shopify**. On the Shopify partner page, select **Begin Setup** to start the integration process.

![Data Import and Web SDK Installation section of the Shopify partner page in Braze.][2]{: style="max-width:80%;"}

### Step 2: Shopify set up
![][3]{: style="float:right;max-width:30%;margin-top:15px;"} 

As you go through the onboarding process, you will be expected to:
1. Connect your Shopify store name
2. Select Shopify events
3. Enable a Braze channel
4. Installation of the Braze app into your storefront
<br><br>

### Step 2a: Connect Shopify store name

When you click **Begin Setup**, you'll be prompted to input your **Shopify Store Name**. Ensure that you input your store name, not the [Shopify domain](https://help.shopify.com/en/manual/domains).

![][6]{: style="max-width:65%;"} 

#### Step 2b: Web SDK

In the next step of the setup wizard, you'll be presented with information about the Braze Web SDK. The Braze Web SDK can be integrated via Shopify ScriptTag to unlock the following functionality:
- One-click Braze Web SDK integration onto your Shopify store
- Anonymous user tracking
- Out-of-the-box tracking for top-of-funnel eCommerce events:
  - Product viewed
  - Product clicked
  - Abandoned cart
- Option to enable in-browser messaging

Keep in mind that when you enable the Braze Web SDK, it will begin tracking monthly active users, and the user data collected will count towards your data consumption.


![][4]{: style="max-width:65%;"} 

{% alert note %}
- For a deeper understanding of the required integration review the [Web SDK Integration via Shopify ScriptTag]({{site.baseurl}}/scripttag_web_sdk_integration/) guide.
- For more general information about Braze's Web SDK, visit our [Web SDK overview]({{site.baseurl}}/user_guide/onboarding_with_braze/web_sdk/).
{% endalert %}

### Step 2c: Select Shopify events

Next, you'll be able to select which Shopify events you wish to integrate with Braze.

For the events denoted with an asterisk (&#42;), you will be required to integrate with the Braze Web SDK to track these events.

![][7]{: style="max-width:65%;"} 

### Step 2d: In-browser messages (optional)

Once you have selected and confirmed which Shopify events to collect, you'll have the option to include in-browser messages as part of your integration. In-browser messages allow brands to deliver rich content within their Shopify store to promote deals, collect email and SMS opt-ins, and so much more. To learn more, visit [In-app messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/#potential-use-cases).

![][5]{: style="max-width:65%;"} 

### Step 2e: Install Braze app in your storefront

After you select your Shopify events and channels, you can confirm your integration settings within the setup wizard. Once confirmed, select **Go to Shopify** to install Braze's Shopify app. After selecting **Install App**, you will be redirected back to Braze to complete the app installation and display your integration settings.

![][8]{: style="max-width:85%;"} 

## Troubleshooting

{% details Why is my Shopify app install still pending? %}
Your install may still be pending for one of the following reasons: 
  - When Braze is setting up your Shopify webhooks
  - When Braze is communicating with Shopify

If your app installation is pending for 1 hour, Braze will fail the installation and you will be prompted to Retry Setup.<br><br>
![]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details Why did my Shopify app install fail? %}
Your install may have failed for one of the following reasons: 
  - Braze could not reach Shopify
  - Braze failed to process the request 
  - Your Shopify access token is invalid 
  - The Braze Shopify app was deleted from your Shopify admin page

If this happens, you will be able to select **Retry Setup** and start the installation process again.<br><br>
![]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details How do I uninstall the Braze application from my Shopify store? %}
You will need to go to your Shopify admin page located under **Apps**. You will then see an option to delete the Braze application<br><br>
![]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:80%;"}
{% enddetails %}

[2]: {% image_buster /assets/img/Shopify/shopify_integration2.png %} 
[3]: {% image_buster /assets/img/Shopify/scripttag1.png %} 
[4]: {% image_buster /assets/img/Shopify/scripttag2.png %} 
[5]: {% image_buster /assets/img/Shopify/scripttag3.png %} 
[6]: {% image_buster /assets/img/Shopify/scripttag4.png %} 
[7]: {% image_buster /assets/img/Shopify/scripttag5.png %} 
[8]: {% image_buster /assets/img/Shopify/scripttag.gif %} 