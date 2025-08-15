---
nav_title: Getting started
article_title: "Getting started with Shopify"
description: "This reference article outlines how to implement the Braze Web SDK onto your Shopify website."
page_type: partner
search_tag: Partner
alias: /getting_started_shopify_legacy/
page_order: 1
---

# Getting started with Shopify

> This article outlines how to implement the Braze Web SDK onto your Shopify website. After implementation, view [Setting up Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview) to learn how to finish setting up the Shopify integration with Braze.

{% multi_lang_include alerts/important_alerts.md alert='Shopify deprecation' %}

## Integration setup checklist

1. [Implement the Braze Web SDK](#implement-web-sdk)
2. [Set up Shopify in Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview)
3. Test the Shopify integration

## Implementing the Web SDK on your Shopify website {#implement-web-sdk}

The [Braze Web SDK]({{site.baseurl}}/user_guide/getting_started/web_sdk/) is a powerful tool used to track the behavior of your Shopify store customers. With the Web SDK, you can collect session data, identify users, and record user behavior data from a web or mobile browser. You can also unlock native messaging channels like in-browser messages.

Although the Shopify integration offers a robust set of default features, keep in mind that if you have use cases to add onsite tracking for [events not supported by the Shopify integration]({{site.baseurl}}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/) or want to add channels like [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), you need to implement the Web SDK directly onto your Shopify site.

Before you begin onboarding the integration, please review the following with your team on which path you want to take to implement the Web SDK.

### Supported features

|Icon| Definition 
|-------------|-------------
|<i aria-hidden="true" class="fas fa-check" title="Supported"></i><span class="sr-only">Supported</span> | Supported
|<i aria-hidden="true" class="fas fa-times" title="Not supported"></i><span class="sr-only">Supported</span> | Not supported
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

| Features | Web SDK via Shopify ScriptTag | Direct web SDK integration via theme.liquid | Direct web SDK integration via Shopify Hydrogen
|-------------|-------------|-------------|------------
| Default on-site tracking      | <i class="fas fa-check" title="Supported"></i> | <i class="fas fa-times" title="Not supported"></i> | <i class="fas fa-times" title="Not supported"></i>          
| Capture form user reconciliation (Low engineering lift required)   | <i class="fas fa-check" title="Supported"></i> | <i class="fas fa-check" title="Supported"></i> | <i class="fas fa-times" title="Not supported"></i> 
| Checkout user reconciliation     | <i class="fas fa-check" title="Supported"></i>  | <i class="fas fa-times" title="Not supported"></i>   | <i class="fas fa-times" title="Not supported"></i>                                        
| Product viewed<br> Product clicked<br> Abandoned cart   | <i class="fas fa-check" title="Supported"></i> |<i class="fas fa-check" title="Supported"></i> | <i class="fas fa-times" title="Not supported"></i> 
| Abandoned checkout<br> Created order<br> Braze Purchase<br> Order paid<br> Partially fulfilled order<br> Fulfilled order<br> Cancelled order<br> Created refund<br> Customer create & update | <i class="fas fa-check" title="Supported"></i> | <i class="fas fa-check" title="Supported"></i> | <i class="fas fa-check" title="Supported"></i>
| Historical backfill | <i class="fas fa-check" title="Supported"></i>  | <i class="fas fa-check" title="Supported"></i>  | <i class="fas fa-check" title="Supported"></i>  
| Catalog sync  |<i class="fas fa-check" title="Supported"></i> |<i class="fas fa-check" title="Supported"></i>  |<i class="fas fa-check" title="Supported"></i>
| Email and SMS subscriber collection    | <i class="fas fa-check" title="Supported"></i>| <i class="fas fa-check" title="Supported"></i>  | <i class="fas fa-check" title="Supported"></i>     
| Default in-app message support   | <i class="fas fa-check" title="Supported"></i>  | <i class="fas fa-check" title="Supported"></i>  | <i class="fas fa-times" title="Not supported"></i>     
| Default content cards support   | <i class="fas fa-times" title="Not supported"></i> | <i class="fas fa-times" title="Not supported"></i> | <i class="fas fa-times" title="Not supported"></i>   
| Default web push support     | <i class="fas fa-times" title="Not supported"></i> | <i class="fas fa-times" title="Not supported"></i> | <i class="fas fa-times" title="Not supported"></i>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }    

{% tabs %}
{% tab Shopify ScriptTag %}

### Implementing Braze Web SDK via Shopify ScriptTag

[Shopify ScriptTag](https://shopify.dev/api/admin-rest/2021-10/resources/scripttag#top) is a remote JavaScript code loaded into the pages of your store or the order status page of checkout. When a store page is loaded, Shopify will check to see if any script tags need to be loaded to the site page. 

If you want to get started with Braze quickly, you have the option to allow Braze to load a pre-defined script for the Braze Web SDK directly onto your Shopify store site.

{% alert important %}
The pre-defined script for the Braze Web SDK for this integration method is not customizable.
{% endalert %}

#### How it works with the Shopify integration

When your Shopify site is loaded, Shopify will check to see if any script tags need to be loaded to the page. During the process, the Braze Web SDK scripts will be loaded onto the pages of your store or the order status page of checkout. 

We’ll also add pre-defined scripts if you have selected product viewed, product clicked, and abandoned cart events that require Shopify ScriptTag or in-app messaging as a channel.  

#### How to enable

To automatically enable the Braze Web SDK scripts as part of your integration, select the supported Shopify ScriptTag events or enable in-app messaging as a channel during your [Shopify integration setup]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview). 

From the Shopify setup composer, the events denoted with an asterisk (*) are supported by the Web SDK. If you select these events or include in-browser messaging, Braze will add the Web SDK implementation via Shopify ScriptTag to your Shopify store as part of your setup.

#### Shopify email capture forms and user reconciliation 

Capture forms obtain identifiable customer information early in the customer’s lifecycle for downstream messaging and engagement. 

The Web SDK tracks Shopify onsite behavior and anonymous users by using the `device_id`. The Braze Shopify ScriptTag integration assigns emails from Shopify email capture forms, such as a newsletter signup, to the user’s `device_id`.

Typical email capture forms include: 
- Email capture form 
- Newsletter signup form

There are two ways to reconcile the user's email and `device_id`: 
- Using the Braze automated email capture script 
- Calling the `setEmail` or `setPhoneNumber` methods

##### Capturing email or phone signups

With Braze, you can use our [email]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) and [SMS and WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) sign-up forms to leverage the Web SDK and in-app messages. 

If using a Shopify email or phone number capture, or a third-party capture form, you can be set directly on the user that is tracked by the Braze Web SDK. For example, if you obtain the customer’s email address, you can set it on their user profile like this:

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

For details on setting these values, refer to these Javascript resources:

- Setting the user’s [email](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail)
- Setting the user’s [phone number](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber)

You can also set the users’ subscription state as you collect their email or phone number, like this:

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

For details on setting these values, refer to these Javascript resources:

- Setting the user’s [email notification subscription type](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)
- Adding the user to a [subscription group](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)

**Example third-party capture form implementation**

1. In `theme.liquid`, copy the following snippet in the `head tag`:

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2. We first call `setInterval` so that the script is loaded first
3. Replace `{FORM_ID}` with the element ID of the form you want to capture
(such as “ContactFooter”.)
4. Replace `{INPUT_EMAIL_ID}` with the element ID of the email input field inside the form
5. When the form is submitted, the script will call `setEmail` with the email input value
6. After the script loads, we call `clearInterval` so that it loads only once

{% alert note %}
At this time, the Braze email capture form will not create a Shopify customer. As a result, you could have Braze user profiles without associated Shopify user profiles until the customer goes through checkout or creates an account. 
{% endalert %}

#### What to expect after implementation

**Braze Web SDK initialization**

The Web SDK will initialize upon session start. Braze will need to collect the `device_id` for tracking anonymous user data as other identifiers like the Shopify customer ID, email, or phone number may not be readily available for guest visitors of your Shopify store.

The `device_id` will also be used to reconcile user data to the anonymous user profile as a customer provides more identifiable information (such as an email address or phone number) after the checkout process.

**Braze Web SDK version**

The current version of the Braze Web SDK via Shopify ScriptTag integration is v4.2.

**Monthly Active Users (MAU)**

The Web SDK tracks sessions of your Shopify customers and guests. As a result, this will accrue as MAU within your Braze dashboard reporting and toward your MAU allotments. It is important to note that anonymous users will also count toward your MAU. For mobile devices, anonymous users are device-dependent. For web users, anonymous users are browser cache-dependent.

{% endtab %}

{% tab theme liquid %}

### Implementing the Web SDK directly onto your Shopify site’s theme.liquid

Braze offers multiple ways to implement the Web SDK including:
- Adding the Web SDK directly to your Shopify `theme.liquid` file
- Google Tag Manager 

If you already have the Web SDK installed on your Shopify store, you can still proceed with setting up the Shopify ScriptTag within the onboarding process. 

During the installation process, Braze will check if instances of the Web SDK are already available on your Shopify store. If there is an existing implementation, Braze will not load the pre-defined scripts for enabling the Web SDK. We’ll then add the necessary scripts to make sure you can track the selected events or enable in-browser messaging.

#### How to enable

To manually implement the Web SDK, view [Initial SDK setup]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web). To implement the Web SDK via Google Tag Manager, view [Google Tag Manager for Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager#google-tag-manager). 

With either implementation path, make sure that your Web SDK integration includes the following or the Shopify integration will not be supported: 
- Web SDK version of v4.0+
- Web SDK initializes upon session start

#### Shopify email capture forms and user reconciliation 

Capture forms obtain identifiable customer information early in the customer’s lifecycle for downstream messaging and engagement. 

The Web SDK tracks Shopify onsite behavior and anonymous users by using the `device_id`. The Braze Shopify ScriptTag integration assigns emails from Shopify email capture forms, such as a newsletter signup, to the user’s `device_id`.

Typical email capture forms include: 
- Email capture form 
- Newsletter signup form

There are two ways to reconcile the user's email and `device_id`: 
- Using the Braze automated email capture script 
- Calling the `setEmail` or `setPhoneNumber` methods

##### Capturing email or phone signups

With Braze, you can use our [email]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) and [SMS and WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) sign-up forms to leverage the Web SDK and in-app messages. 

If using a Shopify email or phone number capture, or a third-party capture form, you can be set directly on the user object that is tracked by the Braze Web SDK. For example, if you obtain the customer’s email address, you can set it on their user profile like this:

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

For details on setting these values, refer to these Javascript resources:

- Setting the user’s [email](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail)
- Setting the user’s [phone number](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber)

You can also set the users’ subscription state as you are collecting their email or phone number like this:

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

For details on setting these values, refer to these Javascript resources:

- Setting the user’s [email notification subscription type](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)
- Adding the user to a [subscription group](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)

**Example third-party capture form implementation**

1. In `theme.liquid`, copy the following snippet in the `head tag`:

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2. We first call `setInterval` so that the script is loaded first
3. Replace `{FORM_ID}` with the element ID of the form you want to capture
(such as “ContactFooter”.)
4. Replace `{INPUT_EMAIL_ID}` with the element ID of the email input field inside the form
5. When the form is submitted, the script will call `setEmail` with the email input value
6. After the script loads, we call `clearInterval` so that it loads only once

{% alert note %}
At this time, the Braze email capture form will not create a Shopify customer. As a result, you could have Braze user profiles without associated Shopify user profiles until the customer goes through checkout or creates an account. 
{% endalert %}

#### What to expect after integration

**Braze Web SDK initialization**

The Web SDK will initialize upon session start. Braze will need to collect the `device_id` for tracking anonymous user data as other identifiers like the Shopify customer ID, email, or phone number may not be readily available for guest visitors of your Shopify store.

The `device_id` will also be used to reconcile user data to the anonymous user profile as a customer provides more identifiable information (such as their email or phone number) during and after the checkout process.

**Braze Web SDK version**

The current version of the Braze Web SDK should be v4.0+.

**Monthly Active Users (MAU)**

The Web SDK tracks the sessions of your Shopify customers and guests. As a result, this will accrue as MAU within your Braze dashboard reporting and toward your MAU allotments. It is important to note that anonymous users will also count toward your MAU. For mobile devices, anonymous users are device-dependent. For web users, anonymous users are browser cache-dependent.

{% endtab %}
{% tab Headless Shopify site %}

### Implementing the Web SDK directly onto your headless Shopify site {#headless-site}

The Braze Shopify ScriptTag integration is incompatible with headless Shopify sites. As a result, you will not be able to get default support for product viewed, product clicked, or abandoned cart events, or enable in-app messaging through our pre-defined scripts. 

#### How to enable

To directly integrate the Web SDK to your headless Shopify site, refer to [Inital SDK Setup for Web]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web).

Make sure that your Web SDK integration includes the following: 
- Web SDK version should be v4.0+
- Web SDK initializes upon session start

#### Setting up Shopify forms for user reconciliation

eCommerce brands likely have experiences on their Shopify site to capture identifiable information from customers ahead of checkout, like email capture forms.

The Web SDK tracks Shopify onsite behavior and anonymous users with the `device_id`. To confirm that email addresses are added to the anonymous user profile, add the following to either a newsletter or email capture form: 
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) 
  - For email capture or newsletter signups
- [addAlias](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addalias) 
  - "alias_label": "shopify_email" 
  - "alias_name": "example@email.com"

When users register or log into their account, you may want to [identify the user profile]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) with an external ID. After the user registers and logs in, add the [changeUser](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) method to assign an external ID if a user creates an account or logs in. 

{% alert note %}
If you set a temporary alias on the user profile, you can proceed to make a request to the [users/merge endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) endpoint to identify the user at a later point. 
{% endalert %}

#### Setting up checkout user reconciliation {#headless-checkout}

When you enable the abandoned checkout event, Braze will receive the Shopify checkouts/create webhook. Braze will attempt to match to an existing user profile by either email address, phone number, or Shopify customer ID. If no match exists, Braze will create an alias profile. 

To make sure that the user profile tracked onsite merges with the Shopify alias user profile created by the Shopify webhooks, you can use the [`/users/merge` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) by following the steps below. 

{% alert tip %}
You can log a custom event via the SDK or API call made on the `theme.liquid` file to trigger a Canvas that includes a request to the `users/merge` endpoint. These methods are outlined below.
{% endalert %}

As soon as a customer visits your Shopify site, an anonymous user is created. This user is automatically assigned a Braze `device_id`. 

1. Randomly assign a unique [user alias]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) for your site visitor upon a new session.

2. As users perform actions on your site, log them as [custom events]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web) or [capture user attributes]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web). When the user proceeds to checkout and inputs their email into a Shopify form, a Shopify customer ID is created. Braze will process Shopify webhooks and create a new user profile if the email, phone, or Shopify alias doesn’t match an existing user.

{% raw %}
```javascript
{
  "user_alias": {
    "alias_name": 1234,
    "alias_label": "temp_user_id"
  }
}
```
{% endraw %}

{% subtabs %}
{% subtab API approach %}

{: start="3"}
3. To prevent duplicate user profiles, you need to merge the user profile containing the Braze `device_id` with the user profile containing the Shopify alias profile. You can create an API-triggered Canvas that will set a delay, update your user with the `do_not_merge` attribute, and make a request to the [`/users/merge` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/). You can also log a custom event like `merge_user` to trigger your Canvas. 


{% endsubtab %}
{% subtab Non-API approach %}

{: start="3"}
3. When users exit the flow or complete checkout, you can log a custom event, like `merge_user`, to trigger a Canvas that will set a delay, update your user with the `do_not_merge` attribute, and make a request to the [`/users/merge` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).

{% endsubtab %}
{% endsubtabs %}

{: start="4"}
4. In your Canvas entry criteria, target only unidentified user profiles, meaning that they don’t have an external ID and `do_not_merge` is not true. <br><br>![The "Entry Audience" step in the Canvas composer with `do_not_merge` as a filter.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_entrycriteria.png %})

{: start="5"}
5. After configuring your Canvas entry criteria, you can create your Canvas. Make the first step of your Canvas a **Delay** step to prevent possible race conditions during processing.<br><br>![Delay step in the Canvas composer.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_delay.png %})

{: start="6"}
6. You can create a **User Update** step to update `do_not_merge` custom attribute to “true” as these users will be merged in the next step. <br><br>![User update step in the Canvas composer with `do_not_merge` selected as an attribute.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_userupdate.png %})

{: start="7"}
7. Next, create a **Message** step with a webhook.<br><br>![Message step in the Canvas composer with a Webhook messaging channel.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_webhook.png %}) 

{% raw %}
```javascript
{
  "merge_updates": [
    {
      "identifier_to_merge": {
           "user_alias": {
                "alias_label": "temp_user_id",
                "alias_name": "{{canvas_entry_properties.${temp_user_id}}}"
            }
      },
      "identifier_to_keep": {
           "user_alias": {
                "alias_label": "shopify_customer_id",
                "alias_name": "{{canvas_entry_properties.${shopify_customer_id}}}"
            }
      }
    }
  ]
}
```
{% endraw %}

{% alert tip %}
For information about `merge_users` behavior, see [POST: Merge users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior). 
{% endalert %}

{: start="8"}
8. As users exit the flow or complete checkout, subsequent Shopify webhooks will be matched by email address or phone number or using the Shopify alias.

{% endtab %}
{% endtabs %}
