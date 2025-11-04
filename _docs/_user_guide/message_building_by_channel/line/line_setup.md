---
nav_title: LINE setup
article_title: LINE Setup
description: "This article covers how to set up the Braze LINE channel, including prerequisites and suggested next steps."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
alias: /line/line_setup/
---


# LINE setup

> This article covers how to set up the LINE channel in Braze, including how to set up users, reconcile user IDs, and create LINE test users in Braze.

## Prerequisites

You'll need the following to integrate LINE with Braze:

- [LINE business account](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- Premium or verified account status (necessary for syncing existing followers)
   - View [LINE's account guidelines](https://terms2.line.me/official_account_guideline_oth)
- [LINE developers account](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE messaging API channel](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

Sending LINE messages from Braze will draw from your account's Message Credits.

## Types of LINE accounts

| Account type | Description |
| --- | --- |
| Unverified account | An unreviewed account that can be obtained by anyone (individual or corporate). This account is represented with a gray badge and won't appear in search results within the LINE app. |
| Verified account | An account that has passed the LINE Yahoo screening. This account is represented with a blue badge and will appear in search results within the LINE app.<br><br>This account is only available for accounts based in Japan, Taiwan, Thailand, and Indonesia.  |
| Premium account | An account that has passed the LINE Yahoo screening. This account is represented with a green badge and will appear in search results within the LINE app. This account type is automatically granted during the screening at LINE's discretion. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Required account type

To sync followers into Braze, your LINE account needs to be verified or premium. When you create an account, its default status will be unverified. You'll need to request account verification.

### Applying for a verified LINE account

{% alert important %}
Verified accounts are only available for accounts based in Japan, Taiwan, Thailand, and Indonesia.
{% endalert %}

1. On the LINE **Official Account** page, select **Settings**.
2. Under **Information Disclosure Verification Status**, select **Request Account Verification**.
3. Enter the required information.
4. Wait for a notification with the review results.

## Integrating LINE

To set up consistent user updates, bring over existing users' LINE IDs, and sync them all to LINE’s subscription states:

1. [Import or update existing known users](#step-1-import-or-update-existing-line-users)
2. [Integrate the LINE channel](#step-2-integrate-line-channel)
3. [Reconcile user IDs](#step-3-reconcile-user-ids)
4. [Change user update methods](#step-4-change-your-user-update-methods)
5. [(Optional) Merge user profiles](#step-5-merge-profiles-optional)

{% alert note %}
You can only have one LINE account in a single workspace. If you have multiple LINE accounts, we recommend using each one in a different workspace.
{% endalert %}

## Step 1: Import or update existing LINE users

This step is necessary if you have an existing and identified LINE user, as Braze will later automatically pull their subscription state and update the correct user profile. If you haven’t previously reconciled users with their LINE ID, skip this step. 

You can import or update users using any of the methods that Braze supports, including the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint, [CSV import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import), or [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/). 

Regardless of the method you use, update the `native_line_id` to provide the user’s LINE ID. To learn more the `native_line_id`, see [User setup](#user-setup).

{% alert note %}
The subscription group state shouldn't be specified, and it will be ignored. LINE is the source of truth for user subscription status, which will be synced to Braze either through the subscription sync tool or by event updates.
{% endalert %}

## Step 2: Integrate LINE channel

After the integration process completes, Braze will automatically pull that channel’s LINE followers into Braze. For any LINE IDs that are already associated with a Braze user profile, each profile will be updated with the “subscribed” status, and any LINE IDs that are remaining will generate anonymous users. Additionally, new followers of your LINE channel will have unidentified user profiles created when they follow the channel.

### Step 2.1: Edit webhook settings

1. In LINE, go the **Messaging API** tab and edit your **Webhook settings**:
   - Set the **Webhook URL** to `https://anna.braze.com/line/events`.
      - Braze will automatically change this to a different URL when integrating, based on your dashboard cluster.
   - Turn on **Use webhook** and **Webhook redelivery**. <br><br> ![Webhook settings page to verify or edit the webhook URL, toggling on or off "Use webhook", "Webhook redelivery", and "Error statistics aggregation".]({% image_buster /assets/img/line/webhook_settings.png %}){: style="max-width:70%;"}
2. Take note of the following information in the **Providers** tab:

| Information type | Location |
| --- | --- |
| Provider ID | Select your provider and then go to ***Settings** > **Basic information** |
| Channel ID | Select your provider and then go to **Channels** > your channel > **Basic settings** |
| Channel secret | Select your provider and then go to **Channels** > your channel > **Basic settings**. |
| Channel access token | Select your provider and then go to **Channels** > your channel > **Messaging API**. If there isn't a channel access token, select **Issue**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="3"}
3. Go to your **Settings** page > **Response settings** and do the following:
   - Turn off **Greeting message**. This can be handled in Braze via trigger on follow.
   - Turn off **Auto-response messages**. All triggered messaging should be through Braze. This won't prevent you from sending directly from the LINE console.
   - Turn on **Webhooks**.

![Response settings page with toggles for how your account will handle chats.]({% image_buster /assets/img/line/response_settings.png %}){: style="max-width:80%;"}

### Step 2.2: Generate LINE subscription groups in Braze

1. Go to the Braze Technology Partners page for LINE and input the information you noted from your LINE **Providers** tab:
   - Provider ID
   - Channel ID
   - Channel secret
   - Channel access token

If you want to add IP whitelisting in your LINE account, add all of the IP addresses listed for your cluster in [IP allowlisting]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#ip-allowlisting) to your allowlist.

{% alert important %}
During integration, be sure to check that your channel secret is correct. If it's incorrect, there may be inconsistencies in the subscription status.
{% endalert %}

![LINE messaging integration page with LINE integration section.]({% image_buster /assets/img/line/integration.png %}){: style="max-width:80%;"}

{: start="2"}
2. After connecting, Braze will automatically generate a Braze subscription group for each LINE integration that's successfully added to your workspace. <br><br> Any changes to your followers list (such as new followers or unfollowers) will be automatically pushed into Braze.

![LINE subscription groups section displaying one subscription group for the "LINE" channel.]({% image_buster /assets/img/line/line_subscription_groups.png %}){: style="max-width:80%;"}

## Step 3: Reconcile user IDs

Combine your users' LINE IDs with their existing Braze user profiles by following the steps in [User ID reconciliation](#user-id-reconciliation).

## Step 4: Change your user update methods 

Assuming you already have a method to provide user updates to Braze, you’ll need to update that to include the new field `native_line_id` so that subsequent user updates sent to Braze will include that field.

Unidentified user profiles with a `native_line_id` may exist in Braze that were created as part of the subscription status sync process, or when a new follower followed your channel. 

When a LINE user is identified in your application through [user reconciliation](#user-id-reconciliation) or other means, you can target a potential unidentified user profile in Braze using the [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) endpoint. Every unidentified user profile with a `native_line_id` also has a user alias `line_id` that can be used to target the user profile to identify.

Here is an example payload to `/users/identify` that targets an unidentified user profile by the user alias `line_id`: 

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

If no existing user profile exists for your provided `external_id`, it will be added to the unidentified user profile, making it identified. If a user profile does exist for the `external_id`, all attributes that are exclusively on the unidentified user profile will be copied to the known user profile, including `native_line_id` and the user’s subscription status.

You can update LINE users that are known in your application through the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint by passing their external identifiers and `native_line_id`. If an unidentified user profile already exists for a user and the same `native_line_id` is added to a different user profile through `/users/track`, it will inherit all the subscription states of the unidentified user profile. However, duplicate user profiles will exist with the same `native_line_id`. Any subsequent subscription updates from event updates will update all profiles accordingly. 

Here is an example payload to `/users/track` that updates a user profile by the external user ID to add a `native_line_id`: 

{% raw %}
```json
{
   "attributes": [
       {
           "external_id": "known_external_id_from_your_application",
           "native_line_id": "U89f4a626548ccd48482f529a482f138b",
           "other": "attribute"
       }
   ]
}
```
{% endraw %}

## Step 5: Merge profiles (optional)

As described above, there's a possibility for multiple user profiles to exist with the same `native_line_id`. If your update methods create duplicate user profiles, you can merge unidentified user profiles to identified user profiles with the `/user/merge` endpoint. 

Here's an example payload to `/users/merge` that targets an unidentified user profile by user alias `line_id`:

{% raw %}
```json
{
 "merge_updates": [
   {
     "identifier_to_merge": {
       "user_alias": {
         "alias_name": "U89f4a626548ccd48482f529a482f138b",
         "alias_label": "line_id"
       }
     },
     "identifier_to_keep": {
       "external_id": "known_external_id_from_your_application"
     }
   }
 ]
}
```
{% endraw %}

{% alert tip %}
To learn more about managing duplicate users in Braze, see [Duplicate Users]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users).
{% endalert %}

## User setup

LINE is the source of truth for user subscription states. Even if you have the LINE ID for a user (`native_line_id`), if that user hasn't followed the LINE channel you're sending from, LINE won't deliver messages to the user.

To help manage this, Braze offers tooling and logic that supports a well-integrated user base, including subscription syncing and event updates for LINE follows and unfollows.

### Subscription syncing and event logic

1. **Subscription sync tool:** This tool is automatically deployed after a successful LINE channel integration. Use it to update existing profiles and create new profiles.<br><br>All Braze user profiles that have a `native_line_id` that follows the LINE channel will be updated to have a subscription group status of `subscribed`. Any follower of the LINE channel that doesn't have a Braze user profile with the `native_line_id` will have:<br><br>- An anonymous user profile created with `native_line_id` set to the user LINE ID following the channel <br>- A user alias `line_id` set to the user LINE ID following the channel <br>- A subscription group status of `subscribed`

{: start="2"}
2. **Event updates:** These are used to update a user's subscription status. When Braze receives user event updates for the integrated LINE channel and the event is a follow, the user profile will have a subscription group status of `subscribed`. If the event is an unfollow, the user profile will have a subscription group status of `unsubscribed`.<br><br>- All Braze user profiles with a matching `native_line_id` will be automatically updated. <br>- If no matching user profile exists for an event, Braze will [create an anonymous user]({{site.baseurl}}/line/user_management/).

## Use cases

These are use cases of how users can be updated after you follow the setup steps above.

##### Existing Braze user profile already follows LINE channel

1. The Braze user profile is updated with a `native_line_id` attribute. Its default subscription status is `unsubscribed`.
2. The subscription sync tool is run, finds that the user is following the LINE channel, and then updates the user profile with the subscription status `subscribed`.
3. If any subscription status changes occur (such as the user blocks, unfriends, or refollows the channel), Braze receives the update from LINE and updates the user profile with the `native_line_id` accordingly.

##### Existing user profile has blocked, unfriended, or unfollowed LINE channel 

1. The Braze user profile is updated with a `native_line_id` attribute. Its default subscription status is `unsubscribed`.
2. The subscription sync tool doesn't find that the user is following the LINE channel and the user’s subscription status remains as `unsubscribed`.
3. If the user later follows the channel, Braze receives the update from LINE and updates the user profile with the subscription status `subscribed`.

##### User profile creation occurs after LINE follow

1. The channel gets a new LINE follower.
2. Braze creates an anonymous user profile with the `native_line_id` attribute set to be the follower’s LINE ID, and a user alias of `line_id` set to be the follower’s LINE ID. The profile has a subscription status of `subscribed`.
3. The user is identified as having the LINE ID through [user reconciliation](#user-id-reconciliation).
  - The anonymous user profile can become identified using the [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) endpoint. Subsequent updates (through the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint, [CSV import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import), or [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) to this user profile can target the user by this known `external_id`.

{% raw %}
```json
{
   "aliases_to_identify": [
       {
           "external_id": "known_external_id_from_your_application",
           "user_alias": {
               "alias_name": "U89f4a626548ccd48482f529a482f138b",
               "alias_label": "line_id"
           }
       }
   ]
}
```
{% endraw %}

  - A new user profile can be created (through the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) endpoint, [CSV import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import), or [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/)) by setting the `native_line_id`. This new profile will inherit the subscription status state of the existing anonymous user profile. Note that this will result in multiple profiles sharing the same `native_line_id`. These can be merged at any time using the `/users/merge` endpoint in the process outlined in [Step 5](#step-5-merge-profiles-optional).

##### User profile creation occurs before LINE follow

1. You acquire a new user and send the information to Braze. A new user profile is created (profile 1).
2. The user follows your LINE account.
3. Braze receives a follow event and creates an anonymous user profile (profile 2).
4. The user is identified as having the LINE ID through [user reconciliation](#user-id-reconciliation).
5. You update profile 1 to set the `native_line_id` attribute. This profile inherits the subscription status state of profile 2.
  - Now there are two user profiles with the same `native_line_id`. These can be merged at any time using the `/users/merge` endpoint in the process outlined in [Step 5](#step-5-merge-profiles-optional).

## User ID reconciliation 

LINE IDs are automatically received by Braze when a user follows your channel, or when you use the one-time “sync followers” workflow. LINE IDs are also specific to the channel that users follow, so it's unlikely that users can provide their LINE IDs.

There are two ways to combine a LINE ID with an existing Braze user profile:

- [LINE login](#line-login)
- [User account linking](#user-account-linking)

### LINE Login

This method uses social media logins for reconciliation. When a user logs into your app, they're given the option to use [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) to create a user account or log in.

{% alert note %}
To acquire the correct LINE ID for each user, set up LINE Login under the same provider as your Braze-integrated LINE official account or channel. 
{% endalert %}

1. Go to the LINE Developer Console and [request permission to obtain the email addresses of users](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission) who log into your app through LINE Login.

2. Follow the appropriate steps provided by LINE to implement LINE Login:<br><br>
  - [Web app directions](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
  - [Native app directions](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-openid-to-register-new-users)<br><br>Make sure to include `email` in the [scope set up](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes) for verification requests. 

{: start="3"}
3. Use the [Verify ID token call](https://developers.line.biz/en/reference/line-login/#verify-id-token) to acquire the user’s email. 

4. Save the user’s LINE ID (`native_line_id`) to the user’s profile with a matching email in your database, or create a new user profile with the user’s email and LINE ID.

5. Send the new or updated user information to Braze using the [`/user/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/), [CSV import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import), or [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/).

#### Workflows

##### Existing follower uses LINE Login

**Scenario:** An anonymous user was created during initial subscriber sync or after integration through a “follow” event.

1. The user logs into your app using LINE Login.
2. LINE provides you the user’s email.
3. You send Braze the updated user (the existing user profile with that email to add the LINE ID) or you update the anonymous user with the email.

##### New follower uses LINE Login

**Scenario:** No user profile exists in Braze with the user’s LINE ID.

1. The user logs into your app using LINE Login.
2. LINE provides you with the user’s email.
3. You either:
  - Update an existing user profile with that email to also have the user’s LINE ID.
  - Create a new user profile with the email and LINE ID.
4. When the user follows your LINE Official Account, Braze receives a follow event and updates the user’s subscription status to `subscribed`.

### User account linking 

This method allows users to link their LINE account to your app’s user account. You can then use Liquid in Braze, such as {% raw %}`{{line_id}}`{% endraw %}, to create a personalized URL for the user that passes the user's LINE ID back to your website or app, which can then be associated with a known user.

1. Create an action-based Canvas that is based on a subscription state change and triggers when a user subscribes to your LINE channel.<br>![Canvas that triggers when a user subscribes to the LINE channel.]({% image_buster /assets/img/line/account_link_1.png %})
2. Create a message incentivizing users to log into your website or app, passing the user's LINE ID as a query parameter (through Liquid), such as:

```
Thanks for following Flash n' Thread on LINE! For personalized offers and 20% off your next purchase, sign-in to your account: https://flashandthread.com/sign_in?line_user_id={{line_id}}
```

{: start="3"}
3. Create a follow-up message that delivers the coupon code.
4. (Optional) Create an action-based campaign or Canvas that triggers when the LINE user is identified to send the user their coupon code. <br>![Action-based campaign that triggers when the LINE user is identified.]({% image_buster /assets/img/line/account_link_2.png %})

#### How it works

After the user logs in, a change is made on your website or app so that the user ID is sent back to Braze to associate it with the LINE ID that was passed as part of the URL, with example code such as:

```json
const currentUrl = new URL(window.location.href)
const queryParams = new URLSearchParams(currentUrl.search);
const lineUserId = queryParams.get("line_user_id")

if (user && isLoggedIn && lineUserId) {
  post(
   "https://rest.iad-03.braze.com	/users/identify",
   {
     "aliases_to_identify": [
       {
   "external_id": user.getUserId(),
   "user_alias": {
     "alias_name": lineUserId,
     "alias_label": "line_id"
   }
 }
      ]
    }
  )
  braze.logCustomEvent("identified_line_user_for_promotion");
}
```

#### Workflows

##### Existing user follows your LINE channel

**Scenario:** An existing user in Braze follows your channel on LINE.

1. LINE sends Braze a follow event.
2. Braze creates an anonymous user profile with the LINE ID, `line_id` user alias, and LINE subscription group status of `subscribed`.
3. The user receives a LINE message with a link to your website and app and logs in. Their user profile is now known.
4. The anonymous user profile that was created is identified and is merged through the [/users/identify endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) onto the user’s known user profile. The known user profile now contains the LINE ID and has a subscription status of `subscribed`.
5. (Optional) The user receives a LINE message with the coupon code and Braze logs the send to the Braze user profile.

## Creating LINE test users in Braze

You can test your LINE channel before setting up [user reconciliation](#user-id-reconciliation) by creating a "Who am I" Canvas or campaign.

1. Set up a Canvas that returns a user's Braze user ID on a specific trigger word. <br><br>Example trigger <br><br>![Trigger to send the campaign to users who sent an inbound LINE to a specific subscription group.]({% image_buster /assets/img/line/trigger.png %}){: style="max-width:80%;"}<br><br>Example message<br><br>![LINE message stating the Braze user ID.]({% image_buster /assets/img/line/message.png %}){: style="max-width:40%;"}<br><br>

2. In Braze, you can use the Braze ID to search for specific users and modify them as needed.

{% alert important %}
Make sure the Canvas doesn't have global control or control groups preventing sends.
{% endalert %}


