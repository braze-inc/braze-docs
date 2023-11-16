---
nav_title: Facebook Lead Ads via Zapier
article_title: Facebook Lead Ads via Zapier
description: "This reference article outlines the integration between Braze and Facebook Lead Ads via Zapier to automate the transfer of lead data from Facebook to Braze, enabling real-time engagement and personalized follow-up actions."
alias: /partners/facebook_lead_ads_zapier/
page_type: partner
search_tag: Partner

---

# Facebook Lead Ads via Zapier integration

> With the Facebook Lead Ads integration via [Zapier][1], you can import your leads from Facebook into Braze along with tracking a custom event when leads are captured. Facebook Lead Ads is a type of ad format that allows businesses to collect lead information directly in Facebook. These ads are designed to make the lead generation process easy and seamless.

By leveraging this integration and Braze, you can automate the transfer of lead data from Facebook to Braze, enabling real-time engagement and personalized follow-up actions. 

## Prerequisites

| Requirements | Description |
|---|---|
| Zapier account | A Zapier account is required to take advantage of this partnership. This integration requires isomg [premium Zapier apps](https://zapier.com/app/pricing), so check that your Zapier plan has access to premium apps. |
| Facebook Business Manager | A centralized tool to manage your brand’s Facebook assets (for example, ad accounts, pages, apps). |
| Facebook ad account | An active Facebook ad account tied to your brand’s business manager. <br><br>Ensure that you have the "Manage ad accounts" permission for each ad account you plan to use with Braze, and that you have accepted your ad account terms and conditions. |
| Facebook Page | An active Facebook Page tied to your brand’s business manager and with "Manage Pages" permissions for each Facebook Page you plan to use with Braze. |
| Facebook Leads access | Facebook Leads access for each ad account you plan to use with Braze. |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance][0]. |
| Braze REST API key | A Braze REST API key with `users.track` permission. This can be created in the Braze dashboard from **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Create a Lead Ads campaign with an instant form

From Facebook Ads Manager, create a [Facebook Leads campaign and Facebook Lead Ads form](https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink).

Include email or phone as a field in your form. You can use an email address or phone number when making a request to the `/users/track` endpoint to update or create the user profile. If you're collecting first names or last names, collect those separately in your form instead of using full names.

### Step 2: Connect your Facebook Account to Zapier 

In Zapier, go to **Apps** to search for available Facebook apps select either **Facebook Lead Ads** or **Facebook Lead Ads (for Business admins).

Note that Zapier has two methods of connecting your Facebook account to Zapier. For more information, refer to:

- [Facebook Lead Ads (for Business Admins)](https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329)
- [Facebook Lead Ads](https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG)

![][2]

Next, assign Zapier to Leads Access within your Business Manager. In your Business Manager, go to **Integrations** > **Leads Access** on the left-hand menu. Select your Facebook Page, then click **CRMs**. From here, select **Assign CRMs** and add **Zapier**.

![][3]

For steps to assign Zapier as a CRM integration, refer to Facebook's [documentation](https://www.facebook.com/business/help/540596413257598?id=735435806665862). 

### Step 3: Create your Zap

#### Step 3a: Create the trigger 

Once you have connected your Facebook account, you can proceed to create a Zap. For the **Trigger**, select **Facebook Lead Ads** or **Facebook Lead Ads (for Business Admins)**. 

![][4]

For the **Event**, select **New Leads** > **Continue**. 

![][5]

Select your Facebook account, then **Continue**. 

![][6]

Select your Facebook Page and instant form you previously created, then **Continue**.

![][7]

Next, test this trigger. After validating your form output, select **Continue with selected record**.

#### Step 3b: Create an action

Add a new step, then select **Webhooks by Zapier**. Next, select **Custom Request** for the **Event** field, then click **Continue**. 

![][8]

Next, add the following configuration fields: 

| Field | Configuration |
|---|---|
| Method | POST |
| URL | Your Braze REST endpoint to `/users/track`. An example is `https://rest.iad-06.braze.com/users/track`. |
| Data Pass Through | False |
| Unflatten | Yes |
| Content-Type Header | `application/json` |
| Authorization Header  | `Bearer <your Braze API key>` |
| Data | The following image is an example of what you can add as the body of your request into the `/users/track` endpoint. <br><br> In addition to adding user attributes and triggering events, note that we are identifying the user by email, setting a user alias, setting their subscription state, and adding the user to a new subscription group for Facebook leads. To include additional Braze user profile fields you're collecting from your form, you can modify the following example. |
{: .reset-td-br-1 .reset-td-br-2}

![][9]

After configuring your webhook, select **Continue and test**. If the test is successful, you can publish your Zap. 

### Step 4: Test your Facebook Lead Ads Zap

To test this end-to-end, use Facebook’s Leads Ads Testing Tool in your Facebook Developer Console. For more information, see [Testing and Troubleshooting](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/). 

## User identity management

This integration allows you to attribute your Facebook leads by email through the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-phone-number).

* If the email matches an existing user profile, Braze will update the profile with Facebook leads data.
* If there are multiple user profiles with the same email, Braze will prioritize the most recently updated profile with an external ID for updates.
* If the external ID doesn’t exist, Braze will prioritize the most recently updated profile with the matching email.
* If no profile exists with the provided email, Braze will create a new profile and a new alias user profile will be created. To identify the newly created alias user profiles, use the [`/users/identify` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).

{% alert note %}
You can also use an external ID or phone number as part of the request to Braze if those fields are available and the primary identifier you wish to for the integration. To do this, modify your request payload as indicated in the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).
{% endalert %}

## Troubleshooting

#### I tested the Trigger and Action successfully, so why am I unable to publish my Zapier Zap?

To use this integration, you must have a [Zapier plan](https://zapier.com/app/pricing) that supports premium apps. 

#### Why aren’t Facebook leads syncing to Braze?

1. Check that you have administrator access to your Facebook Page, ad account, and lead access. Then, reconnect your account in Zapier.
2. Verify that the instant form you created in Facebook maps to the form selected in your Trigger step. 
3. Check that you have assigned Zapier to Leads Access* by going to **Facebook Business Manager** > **Integrations** > **Lead Access**.

#### Why am I seeing duplicate user profiles with the same email?

There are unique ways of creating and managing user profiles in Braze based on their [user profile lifecycle]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle). 

Depending on your internal processes and when you are triggering customers to be created within Braze, you may encounter duplicate user profiles due to a race condition of the user profile being created by the integration and when the user is created from your system. You can [merge user profiles]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) in Braze. 

#### I don’t have a Zapier account. How can I trigger Facebook Lead Ads webhooks into Braze? 

If you don’t use Zapier and don’t plan on using Zapier, you can build the integration directly from Facebook into Braze. Refer to [Lead Ads documentation](https://developers.facebook.com/docs/marketing-api/guides/lead-ads) for more information. 

For retrieving leads from Facebook, use [webhooks](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks). Refer to [Webhooks documentation](https://developers.facebook.com/docs/graph-api/webhooks/getting-started) to get started with webhooks in Facebook.

After establishing the webhooks URL within Facebook, you can create a [Data Transformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/) in Braze. 

For more troubleshooting tips, refer to Zapier’s [Facebook leads troubleshooting guide](https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423). 


[0]: {{site.baseurl}}/api/basics/#api-definitions
[1]: https://zapier.com/
[2]: {% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}
[3]: {% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}
[4]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}
[5]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}
[6]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}
[7]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}
[8]: {% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}
[9]: {% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}