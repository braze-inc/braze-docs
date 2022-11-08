---
nav_title: Setting up Shopify
article_title: "Setting up Shopify"
description: "This article outlines how to set up Shopify, a global commerce company that allows you to seamlessly connect their Shopify store with Braze to pass select Shopify webhooks into Braze."
page_type: partner
search_tag: Partner
alias: "/setting_up_shopify/"
alias: "/shopify_subscription_states/"
page_order: 2
---

# Setting up Shopify

### Step 1: Locate Shopify within the dashboard
In Braze, go to the **Technology Partners** section and then search **Shopify**. On the Shopify partner page, select **Begin Setup** to start the integration process.

![Data Import and Web SDK Installation section of the Shopify partner page in Braze.][2]{: style="max-width:80%;"}

### Step 2: Braze’s setup wizard
Next, you are prompted by Braze’s setup wizard. Within this flow, you must enter your Shopify store name. Make sure to enter the store name, and not your Shopify domain. Note that currently, we can only connect one store per app group.

### Step 3: Flexible event selection
There will be a step explaining which events require us to implement the Braze Web SDK on your store and what to expect when this is added. Proceed to the next page to select the Shopify events you want Braze to track. Selecting any events with an * next to them will enable our Web SDK. The next step will ask you to confirm the selected events.

### Step 4: Enable in-browser message channel
You can optionally unlock a new channel on your Shopify store for in-browser messages. This will allow you to use our out-of-the-box message types like slideup, modal, full screen, simple surveys, and custom HTML. Note that enabling this will implement our Web SDK in your store. Check out our [guide]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) on how you can create your first in-browser message.

### Step 5: Collect email or SMS subscribers

{% alert important %}
Collecting email or SMS subscribers is in early access. Contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

At this step, select whether you want to collect email and SMS opt-ins from your Shopify store to sync to Braze.

![][77]{: style="max-width:60%;"}

- **Collect email subscribers**<br>If enabled, Braze will update the global email subscription state on the profile to `subscribed` so you can send emails to your users. You can also optionally add one or more [subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups) to automatically assign email subscribers to when they opt-in. 
- **Collect SMS subscribers**<br>If enabled, Braze will update the selected [SMS subscription group]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) on the profile to `subscribed` so you can send messages to your users. If you are collecting SMS opt-ins, you must select one subscription group. If no subscription group exists, or you would like to create a new subscription group, reach out to your Braze representative for support. 

If there is an existing global subscription state on a user profile within Braze that's different from Shopify, we recommend you enable **Override existing global subscription state for users**. This will override the Braze state to ensure it matches with Shopify.

{% alert important %}
If you do not override global subscription states, existing user's states may not match those found in Shopify. This can lead to unreceived and unintended messages.
{% endalert %}

### Step 6: Install Braze’s Shopify application
You’ll then be redirected to your Shopify store to install the Braze app. Once you select **Install Unlisted App**, you will be redirected to the Braze dashboard. 

### Step 7: Verify completion
That's it! The status of your integration appears in the **Data Import** section of the Shopify partner page. Once the Braze app has been successfully installed and the webhook creation is complete, you will be notified via email and ingestion will begin. In addition, the **Connection Pending** status will be updated to **Connected** and will display the timestamp of when the connection was established.

### Shopify setup within Braze

<br>![Workflow of setting up Shopify within Braze by entering the store name and navigating to Shopify to install the Braze app.][4]{: style="max-width:90%;"}

## Troubleshooting

{% details Why is my Shopify app install still pending? %}
Your install may still be pending for one of the following reasons: 
  - When Braze is setting up your Shopify webhooks
  - When Braze is communicating with Shopify

If your app installation is pending for 1 hour, Braze will fail the installation, and you will be prompted to Retry Setup.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details Why did my Shopify app install fail? %}
Your install may have failed for one of the following reasons: 
  - Braze could not reach Shopify
  - Braze failed to process the request 
  - Your Shopify access token is invalid 
  - The Braze Shopify app was deleted from your Shopify admin page

If this happens, you will be able to select **Retry Setup** and start the installation process again.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details How do I uninstall the Braze application from my Shopify store? %}
Go to your Shopify admin page located under **Apps**. You will then see an option to delete the Braze application.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details I am struggling reconciling my users, what might be the reason? %}

If you use the ScriptTag integration, and your Shopify store offers a "Buy Now" option that skips the cart, Braze may struggle to reconcile users as Shopify does not allow script tags to retrieve a `device_id` to map the events to a user who skips the cart.

{% enddetails %}


[2]: {% image_buster /assets/img/Shopify/shopify_integration2.png %} 
[3]: {% image_buster /assets/img/Shopify/scriptag.gif %} 
[77]: {% image_buster /assets/img/Shopify/shopify_integration77.png %}
[4]: {% image_buster /assets/img/Shopify/shopify_integration3-6.gif %}
