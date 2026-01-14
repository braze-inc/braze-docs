---
nav_title: Facebook Lead Ads via Zapier
article_title: Facebook Lead Ads via Zapier
description: "This reference article outlines the integration between Braze and Facebook Lead Ads via Zapier to automate the transfer of lead data from Facebook to Braze, enabling real-time engagement and personalized follow-up actions."
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner

---

# Facebook Lead Ads via Zapier integration

> With the Facebook Lead Ads integration via <a href="https://zapier.com/" target="_blank">Zapier</a>, you can import your leads from Facebook into Braze and track a custom event when leads are captured. 

Facebook Lead Ads is an ad format that allows businesses to collect lead information directly in Facebook. These ads are designed to make the lead generation process easy and seamless. By leveraging a Zapier integration and Braze, you can automate the transfer of lead data from Facebook to Braze, enabling real-time engagement and personalized follow-up actions. 

## Prerequisites

| Requirements | Description |
|---|---|
| Zapier account | A Zapier account is required to take advantage of this partnership. This integration requires use of <a href="https://zapier.com/app/pricing/" target="_blank">premium Zapier apps</a>, so check that your Zapier plan has access to premium apps. |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Facebook Leads access</a> | Facebook Leads access is required for each ad account you plan to use with Braze. |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Facebook Business Manager</a> | You will use Facebook Business Manager, a centralized tool to manage your brand’s Facebook assets (for example, ad accounts, pages, and apps), as part of this integration. |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Facebook ad account</a> | You will need an active Facebook ad account tied to your brand’s business manager. <br><br>Ensure that you have the "Manage ad accounts" permission for each ad account you plan to use with Braze, and that you have accepted your ad account terms and conditions. |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">Facebook Page</a> | You will need an active Facebook Page tied to your brand’s business manager. <br><br>Ensure that you have the "Manage Pages" permissions for each Facebook Page you plan to use with Braze. |
| Braze REST endpoint | Ensure you know your [REST endpoint URL]({{site.baseurl}}/api/basics/#api-definitions). Your API endpoint matches the dashboard URL for your Braze instance. <br><br> For example, if your dashboard URL is `https://dashboard-03.braze.com`, your endpoint will be `dashboard-03`. |
| Braze REST API key | Ensure you have a Braze REST API key with `users.track` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Step 1: Create a Lead Ads campaign with an instant form

From Facebook Ads Manager, create a <a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">Facebook Leads campaign and Facebook Lead Ads form</a>.

You can use either an email address or phone number when making a request to the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) to update or create the user profile. For this reason, include a **Contact field** for **email** or **phone** in your lead ad form. If you're collecting first names or last names, collect those separately in your form instead of using full names.

### Step 2: Connect your Facebook account to Zapier 

#### Step 2a: Select your connection method in Zapier

In Zapier, go to **Apps** to search for available Facebook apps. Select either **Facebook Lead Ads** or **Facebook Lead Ads (for Business admins)**.

For more information on these two methods of connecting your Facebook account to Zapier, refer to:

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebook Lead Ads (for Business Admins)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Facebook Lead Ads</a>

![]({% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}){: style="max-width:80%;"}

#### Step 2b: Add Zapier to Leads Access in Facebook Business Manager

In your Facebook Business Manager, go to **Integrations** > **Leads Access** on the left-hand menu. Select your Facebook Page, then click **CRMs**. On the CRM tab, select **Assign CRMs** and add **Zapier**.

![]({% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}){: style="max-width:80%;"}

For steps to assign Zapier as a CRM integration, refer to Facebook's <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">documentation</a>.

### Step 3: Create your Zap

#### Step 3a: Create the trigger 

Once you have connected your Facebook account, you can proceed to create a Zap. For the **Trigger**, select **Facebook Lead Ads** or **Facebook Lead Ads (for Business Admins)** based on your choice from step 2. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}){: style="max-width:80%;"}

For the **Event**, select **New Leads** > **Continue**. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}){: style="max-width:80%;"}

Select your Facebook account, then **Continue**. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}){: style="max-width:80%;"}

Select your Facebook Page and instant form you previously created, then **Continue**.

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}){: style="max-width:80%;"}

Next, test this trigger. After validating your form output, select **Continue with selected record**.

#### Step 3b: Create an action

Add a new step, then select **Webhooks by Zapier**. Next, select **Custom Request** for the **Event** field, then click **Continue**. 

![]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}){: style="max-width:80%;"}

Lastly, set up your custom request by inserting fields in your payload. The following code snippet shows an example payload. 

```
{
    "attributes": [
        {
            "email": "<insert_email_field>",
            "first_name": "<insert_first_name_field>",
            "last_name": "<insert_last_name_field>",
            "lead_form": "<insert_form_name_field>",
            "fb_campaign": "<insert_campaign_id_field>",
            "fb_ad_set": "<insert_campaign_id_field>",
            "fb_ad": "<insert_campaign_id_field>",
            "email_subscribe": "subscribed",
            "subscription_groups" : [{
                "subscription_group_id": "<subscription_group_id>",
                "subscription_state": "subscribed"
                }
            ]
        }
    ],
    "events": [
        {
            "email": "<insert_email_field>",
            "name": "<insert_custom_event_name>",
            "time": "<insert_timestamp_field>",
            "_update_existing_only": false
        }
    ]
}`
```

Here's an example of what this looks like in Zapier:

![]({% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}){: style="max-width:80%;"}

After configuring your webhook, select **Continue and test**. If the test is successful, you can publish your Zap.

### Step 4: Test your Facebook Lead Ads Zap

To test this end-to-end, use Facebook’s Leads Ads Testing Tool in your Facebook Developer Console. For more information, see <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">Testing and Troubleshooting</a>.

## User identity management

This integration allows you to attribute your Facebook leads by email through the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-phone-number).

* If the email matches an existing user profile, Braze will update the profile with Facebook leads data.
* If there are multiple user profiles with the same email, Braze will prioritize the most recently updated profile with an external ID for updates.
* If the external ID doesn’t exist, Braze will prioritize the most recently updated profile with the matching email.
* If no profile exists with the provided email, Braze will create a new profile and a new alias user profile will be created. To identify the newly created alias user profiles, use the [`/users/identify` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).

{% alert note %}
You can also use a phone number or external ID as part of the request to Braze if those fields are available and the primary identifier you wish to for the integration. To do this, modify your request payload as indicated in the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).
{% endalert %}

## Troubleshooting

{% details I tested the Trigger and Action successfully, so why am I unable to publish my Zapier Zap? %}
To use this integration, you must have a <a href="https://zapier.com/app/pricing/" target="_blank">Zapier plan</a> that supports premium apps. 
{% enddetails %}

{% details Why aren’t Facebook leads syncing to Braze? %}
1. Check that you have administrator access to your Facebook Page, ad account, and lead access. Then, reconnect your account in Zapier.
2. Verify that the instant form you created in Facebook maps to the form selected in your Trigger step. 
3. Check that you have assigned Zapier to Leads Access by going to **Facebook Business Manager** > **Integrations** > **Lead Access**.
{% enddetails %}

{% details Why am I seeing duplicate user profiles with the same email? %}
There are unique ways of creating and managing user profiles in Braze based on their [user profile lifecycle]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle).

Depending on your internal processes and when you are triggering customers to be created within Braze, you may encounter duplicate user profiles due to a race condition of the user profile being created by the integration and when the user is created from your system. You can [merge user profiles]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) in Braze.
{% enddetails %}

{% details I don’t have a Zapier account. How can I trigger Facebook Lead Ads webhooks into Braze? %}
If you don’t use Zapier and don’t plan on using Zapier, you can build the integration directly from Facebook into Braze. Refer to <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">Lead Ads documentation</a> for more information.

For retrieving leads from Facebook, use <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">webhooks</a>. Refer to <a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">Webhooks documentation</a> to get started with webhooks in Facebook.

After establishing the webhooks URL in Facebook, work with your team to determine the best path to forward the data to the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Similar to the Zapier approach, we’d recommend making a [request by email]({{site.baseurl}}/api/endpoints/user_data/post_user_track#example-request-for-updating-a-user-profile-by-phone-number) through the `users/track` endpoint.
{% enddetails %}

{% alert tip %}
For more troubleshooting tips, refer to Zapier’s <a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">Facebook leads troubleshooting guide</a>.
{% endalert %}


