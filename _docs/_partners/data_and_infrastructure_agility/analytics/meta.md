---
nav_title: Facebook Lead Ads via Zapier
article_title: Facebook Lead Ads via Zapier
description: "This reference article outlines the partnership between Braze and Zapier, an automation web tool that allows you to share data between web apps, and use that information to automate actions."
alias: /partners/facebook_lead_ads_zapier/
page_type: partner
search_tag: Partner

---

# Facebook Lead Ads via Zapier integration

> With the Facebook Lead Ads integration via [Zapier][1], you can import your leads from Facebook into Braze along with tracking a custom event when leads are captured. By leveraging this integration, you will be able to automate the transfer of lead data from Facebook to Braze, enabling real-time engagement and personalized follow-up actions. 

Facebook Lead Ads is a type of Facebook ad format that allows businesses to collect lead information directly within the Facebook platform. These ads are designed to make the lead generation process easy and seamless.

## Prerequisites

| Requirements | Description |
|---|---|
| Zapier account | A Zapier account is required to take advantage of this partnership. This integration will require the usage of [premium Zapier apps](https://zapier.com/app/pricing), so check if your Zapier plan has access to premium apps. |
| Facebook Business Manager | A centralized tool to manage your brand’s Facebook assets (for example, ad accounts, pages, apps). |
| Facebook ad account | An active Facebook ad account tied to your brand’s business manager. <br>Ensure that you have Manage ad accounts permission for each ad account you plan to use with Braze, and that you have accepted your ad account terms and conditions. |
| Facebook page | An active Facebook page tied to your brand’s business manager, along with **Manage Pages** permissions for each Facebook page you plan to use with Braze. |
| Facebook Leads access | Facebook Leads access for each ad account you plan to use with Braze. |
| Braze REST endpoint | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance][0]. |
| Braze REST API key | A Braze REST API key with `users.track` permission. This can be created in the Braze dashboard from **Settings** > **API Keys**. |
{: .reset-td-br-1 .reset-td-br-2}

## Integration

### Step 1: Create a Lead Ads campaign with an instant form

From Facebook Ads Manager, create a [Facebook Leads campaign and Facebook Lead Ads form](https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink).

Include email or phone as a field in your form. You will then be able to use email or phone when making a request to users/track to update or create the user profile. If you're collecting first names or last names, collect those separately in your form instead of using full names.

### Step 2: Connect your Facebook Account to Zapier 

In Zapier, go to **Apps** to search for available Facebook apps. 

Note that Zapier has 2 methods of connecting your Facebook account to Zapier. For more information, please refer to the documentation links below: 
- [Facebook Lead Ads (for Business Admins)](https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329)
- [Facebook Lead Ads](https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG)

In addition, assign Zapier to Leads Access within your Business Manager. Within your Business Manager go to **Integrations** > **Leads Access** on the left-hand menu. 

Select your Facebook Page and then select CRMs. From here you will select Assign CRMs and add Zapier as you see below. 

For steps to assign Zapier as a CRM integration, refer to Facebook's [documentation](https://www.facebook.com/business/help/540596413257598?id=735435806665862). 

### Step 3: Create your Zap

#### Step 3a: Create the trigger 

Once you have connected your Facebook account, you can proceed to Create a Zap.

For the Trigger, select either Facebook Lead Ads or Facebook Lead Ads (for Business Admins). 

For the Trigger Event, select **New Leads** then **Continue**. 

Select your Facebook account then **Continue**. 

Select your Facebook page, Instant Form you previously created, and then **Continue**.

At this stage, test the Trigger you have just configured. Once you have validated your form output, you can select Continue with selected record.

#### Create an action

Add a new step and select Webhooks by Zapier. You will then select Custom Request and then Continue. 

Add the following configuration fields: 
* Method = Post 
* URL = Your Braze REST endpoint to users/track 
    * Example: https://rest.iad-06.braze.com/users/track
* Data Pass Through = False 
* Unflatten = Yes
* Headers
    * Content-Type = application/json
    * Authorization = Bearer <your Braze API key>
* Data - Here is an example of what you could add as the body of your request into users/track. In addition to adding user attributes and triggering events, note that we are identifying the user by email, setting a user alias, setting their subscription state, and adding the user to a new subscription group for Facebook leads. 

```
{
  "attributes": [
  {
    "email": "example@email.com",
    "first_name": "Diana",
    "last_name": "Kim",
    "lead_form": "{{214890246__form_name}}",
    "fb_campaign": "{{214890246__campaign_name}}",
    "fb_ad_set": "{{214890246__campaign_name}}",
    "fb_ad": "{{214890246__campaign_name}}",
    "email_subscribe": "subscribed",
    "subscription_groups" : [{
      "subscription_group_id": "<insert_subscription_group_id>",
      "subscription_state": "subscribed"
      }
      ]
    }
  ],
    "events": [
        {
            "email": "example@email.com",
            "name": "fb_lead_signup",
            "time": "2022-12-06T19:20:45+01:00",
            "_update_existing_only": false
            }
    ]
}
```

If you wish to include other Braze user profile fields that you are collecting from your form, you may do so by modifying the example. 

Once you have configured your webhook, select Continue and test. If the test is successful, you can then proceed to publish your Zap. 

### Step 3: Test your Facebook Lead Ads Zap

To test this end-to-end, you can utilize Facebook’s Leads Ads Testing Tool within your Facebook Developer Console. For more information, see [here](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/). 

## User identity management

This integration will allow you to attribute your Facebook leads by [email through the `/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-phone-number). If the email matches an existing user profile, Braze will simply update the profile with Facebook leads data. If there are multiple user profiles with the same email, Braze will prioritize the most recently updated profile with an external ID for updates. If the external ID doesn’t exist, Braze will then prioritize the most recently updated profile with the matching email. 

{% alert note %}
You can also use either external ID or phone as part of the request to Braze if those fields are available and the primary identifier you wish to for the integration. You must modify your request payload as indicated in []`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).
{% endalert %}

If no profile exists with the provided email, Braze will create a new profile and a new alias user profile will be created. 

To identify the newly created alias user profiles, you can later use the []`/users/identify` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/).

## Troubleshooting

#### I tested the Trigger and Action successfully, but why am I not able to publish my Zapier Zap?  

To use this integration, you must have a [Zapier plan](https://zapier.com/app/pricing) that supports premium apps. 

#### Why aren’t Facebook leads syncing to Braze?

1. Check your account permissions. You must have admin access to your Facebook page, ad account, and lead access. Ensure that you have these permissions and reconnect your account in Zapier. 
2. Check that the correct form is selected. Verify that the Instant Form you created in Facebook maps to the form selected within your Trigger step. 
3. Check that you have assigned Zapier to Leads Access. Go to Facebook Business Manager > Integrations > Lead Access to verify that you have properly assigned Zapier.

#### Why am I seeing duplicate user profiles with the same email?

Braze customers may have unique ways of creating and managing user profiles in Braze based on their [user profile lifecycle]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-profile-lifecycle). Depending on your internal processes and when you are triggering customers to be created within Braze, you may encounter duplicate user profiles due to a race condition of the user profile being created by the integration and when the user is created from your system. 

Braze does offer the ability to merge user profiles. For more information, please review our users/merge endpoint. 

#### I don’t have a Zapier account. How can I trigger Facebook Lead Ads webhooks into Braze? 

If you don’t use Zapier and don’t plan on using Zapier, you can build the integration directly from Facebook into Braze. For more information, please refer to Facebook’s [Lead Ads documentation](https://developers.facebook.com/docs/marketing-api/guides/lead-ads). 

For retrieving leads from Facebook, you can utilize [webhooks](https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks). For more information on getting started with webhooks within Facebook, see [here](https://developers.facebook.com/docs/graph-api/webhooks/getting-started). After you have established the webhooks URL within Facebook, you can create a [Data Transformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/overview/) in Braze. 

For more troubleshooting tips, visit Zapier’s [Facebook leads troubleshooting guide](https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423). 


[0]: {{site.baseurl}}/api/basics/#api-definitions
[1]: https://zapier.com/