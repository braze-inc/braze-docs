---
alias: /partners/ketch
title: Ketch
nav_title: Ketch
hidden: true
page_type: reference
layout: dev_guide
---

# Ketch

> [Ketch](https://www.ketch.com) enables businesses to be responsible stewards of data. We provide simplified privacy operations and complete, dynamic data control and intelligence.

The Ketch partnership with Braze allows you to control customer communication preferences within the Ketch preference center to be automatically propagated to Braze in order to manage customer communication and privacy preferences. 

## Prerequisites

| Requirements | Description |
|---|---|
| Ketch Account | A [Ketch](https://www.ketch.com) account with admin privileges is required activate this integration. |
| Braze API key | A Braze REST API key with `users.track, subscription.status.get, subscription.status.set, users.delete, users.alias.new, users.export.ids, email.unsubscribe,`and `email.blacklist` permissions.<br><br>This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

The following steps will alllow you to configure and setup your Ketch and Braze systems so that Ketch can orchestrate user communications and preference signals directly to Braze

### Step 1: Setup the Braze Connection within Ketch
To get start, log into your [Ketch instance](https://app.ketch.com)

1. Navigate to **Data Systems**, and search for **Braze**<br><br> 
2. Click on the the **Braze** system, and click **New Connection**.<br><br>
3. Give your Braze connection an identifiable name, note that a code will also be created for that connection, this code should be unique across all connections and will be used to refer to this connection in API based processes.<br><br>
4. Confirm the identity mapping of the users, by default, we will map user identities based off of email addresses for the user, but we can also configure it based off of external_id in Braze.<br><br>
5. Next, add in the braze API key you created with the proper permissions and then provide the rest API endpoint, note the reset API end-point is based on which braze instance your organization is using. You can use this document to find your [Braze API end-point](https://www.braze.com/docs/api/basics/#endpoints).<br><br>


### Step 2: Configuring Subscription Preferences
1. To configure Subscriptions in Ketch, go to **Policy Center > Subsriptions**. If you do not see the subscriptions tab under Policy Center, please make sure you have purchased the marketing preference center and verify that you have the correct account permissions to access this portion of the product.<br><br> 
2. The subscriptions tab displays the available subscriptions. Each subscription represents a specific marketing category, while the channels under each topic represent the medium by which your users will be contacted on those topics. There is also the Global Control tab which controls the universal opt-outs from your user.<br><br> 
3. To create a topic, you can click the create new subscription button. Each subscription will have a name and a code, the code will be how each subscription gets referred to when referenced by the API. You can also add language translations for each of your topics in case this marketing preference center is deployed to sites supporting multiple languages. Next, you will want to add the channels which you send the subscription topics through. For each channel that you enable, that option will show up in the marketing preference center for your users.<br><br>
4. Under each channel that you enable, you can also add the details of how you want the Ketch preference center to orchestrate the signals of that particular opt-in or opt-out.<br><br>
5. For the integration with Braze, select the Braze connection you would like to orchestrate the opt-in and opt-out signals, and then fill in the `subscription_group_id` for the particular subscription group you want to propagate the user preferences to in Braze.<br><br>

{% raw %}
```
![Braze Subscription Group ID][1]
```
{% endraw %}


{% alert note %}
In order for Subscription Preferences to collect and orchestrate user opt-in and opt-out signals, identities must be properly configured. We recommend configuring email as the identity to orchestrate user preference signals for this integration
{% endalert %}

### Step 3: Configuring Identities
The ability for an end user to see marketing preference center is gated behind whether or not we can capture a proper marketing preference identity for that user. If we cannot capture the user identity properly, then we will not show the marketing preferences page since we would not be able to orchestrate any user preferences without knowing how they are identified.

1. In order to configure the marketing preference identity, first head to the settings page of the Ketch platform and then click on the **Identity space**. You will need to either create a new identity space or edit an existing identity space to assign that identity space as the marketing preference identity.<br><br>
2. Once you have selected the desired identity space as the marketing preference identity. We will need to make sure the Ketch tag deployed on the property properly captures that identity space.<br><br>
3. Head over to the **Experience Server > Properties** and edit the desired property. Under the data layer for that property, make sure you enable custom identity space and then configure how the marketing preference identity that you have configured earlier is captured on this site.<br><br>
4. Once you have the identity space configured, you can then open the preference center on the site where the ketch tag has been deployed, and test to see if the preference center shows up.<br><br>

{% raw %}
```
[1]: {% image_buster /assets/img/ketch/ketch1.png %}
```
{% endraw %}
