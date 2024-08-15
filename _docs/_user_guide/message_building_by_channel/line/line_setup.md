---
nav_title: LINE Setup
article_title: LINE Setup
description: "This article covers how to set up the Braze LINE channel, including prerequisites and suggested next steps."
page_type: partner
search_tag: Partner
page_order: 0
channel:
 - LINE
hidden: true
permalink: /line/line_setup/
---


# LINE setup

> This article covers how to set up the LINE channel in Braze and is part of the LINE beta collection. [Return to the main page](https://www.braze.com/docs/line/).

{% alert important %}
LINE access is in beta and only available in select Braze packages. Reach out to your account manager or customer success manager to get started.
{% endalert %}

## Prerequisites

You'll need the following to integrate LINE with Braze:

- [LINE business account](https://www.linebiz.com/jp-en/manual/OfficialAccountManager/tutorial-steps/?list=7171)
- [Premium or verified account](https://www.infobip.com/docs/line/get-started#premium-id-line-official-account) status (necessary for syncing existing followers)
   - View [LINE's account guidelines](https://terms2.line.me/official_account_guideline_oth)
- [LINE developers account](https://developers.line.biz/en/docs/line-developers-console/login-account/)
- [LINE messaging API channel](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)

## Types of LINE accounts

| Account type | Description |
| --- | --- |
| Unverified account | An unreviewed account that can be obtained by anyone (individual or corporate). This account is represented with a gray badge and won't appear in search results within the LINE app. |
| Verified account | An account that has passed the LINE Yahoo screening. This account is represented with a blue badge and will appear in search results within the LINE app.<br><br>This account is only available for accounts based in Japan, Taiwan, Thailand, and Indonesia.  |
| Premium account | An account that has passed the LINE Yahoo screening. This account is represented with a green badge and will appear in search results within the LINE app. This account type is automatically granted during the screening at LINE's discretion. |
{: .reset-td-br-1 .resest-td-br-2}

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

If you want to sync users who followed a specific channel before that channel was synced with Braze, ask your customer success manager or account manager to [submit a request](https://servicedesk.braze.com/plugins/servlet/desk/portal/12) to the WhatsApp team.

## Integrating LINE

Follow these steps to set up consistent user updates, bring over existing users' LINE IDs, and sync them all to LINE’s subscription states:

1. [Import or update existing known users](#step-1-import-or-update-existing-line-users)
2. [Integrate the LINE channel](#step-2-integrate-line-channel)
3. [Request subscription status sync](#step-3-request-a-subscription-status-sync)
4. [Update user update methods](#step-4-change-your-user-update-methods)
5. [(Optional) Merge users](#step-5-merge-profiles-optional)

## Step 1: Import or update existing LINE users

Users can be imported or updated by any of the methods that Braze supports, including the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) endpoint, [CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import), or [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion.). 

Regardless of the method you use, update the `native_line_id` to provide the user’s LINE ID. 

{% alert note %}
The subscription group state shouldn't be specified, and it will be ignored. LINE is the source of truth for user subscription status, which will be synced to Braze either through the subscription sync tool or by event updates.
{% endalert %}

## Step 2: Integrate LINE channel

After your existing LINE user base is imported into or updated in Braze, you can integrate your channel. After integration, new followers of your LINE channel will have unidentified user profiles created when they follow the channel.

### Step 2a: Connect your LINE channel to Braze

1. In LINE, go the **Messaging API** tab and edit your **Webhook settings**:
   - Set the **Webhook URL** to `https://anna.braze.com/line/events`.
      - Braze will automatically change this to a different URL when integrating, based on your dashboard cluster.
   - Turn on **Use webhook** and **Webhook redelivery**. <br><br> ![Webhook settings page to verify or edit the webhook URL, toggling on or off "Use webhook", "Webhook redelivery", and "Error statistics aggregation".][1]{: style="max-width:70%;"}
2. Take note of the following information in the **Providers** tab:

| Information type | Location |
| --- | --- |
| Provider ID | Select your provider and then go to ***Settings** > **Basic information** |
| Channel ID | Select your provider and then go to **Channels** > your channel > **Basic settings** |
| Channel secret | Select your provider and then go to **Channels** > your channel > **Basic settings** |
| Channel access token | Select your provider and then go to **Channels** > your channel > **Messaging API**. If there isn't a channel access token, select **Issue**. |
{: .reset-td-br-1 .reset-td-br-2}

{: start="3"}
3. Go to your **Settings** page > **Response settings** and do the following:
   - Turn off **Greeting message**. This can be handled in Braze via trigger on follow.
   - Turn off **Auto-response messages**. All triggered messaging should be through Braze. This won't prevent you from sending directly from the LINE console.
   - Turn on **Webhooks**.

![Response settings page with toggles for how your account will handle chats.][2]{: style="max-width:80%;"}

### Step 2b: Set up your LINE subscription group in Braze

1. Go to the Braze Technology Partners page for LINE and input the information you noted from your LINE **Providers** tab:
   - Provider ID
   - Channel ID
   - Channel secret
   - Channel access token

![LINE messaging integration page with LINE integration section.][3]{: style="max-width:80%;"}

{: start="2"}
2. After connecting, Braze will automatically generate a Braze subscription group for each LINE integration that's successfully added to your workspace. <br><br> Any changes to your followers list (such as new followers or unfollowers) will be automatically pushed into Braze.

![LINE subscription groups section displaying one subscription group for the "LINE" channel.][4]{: style="max-width:80%;"}

## Step 3: Request a subscription status sync

We recommend syncing all LINE followers before going live. This updates all followers' user profiles with the correct subscription status. That way, if users follow your LINE channel before they're identified in your app, there's an existing user profile to update or merge.

## Step 4: Change your user update methods 

Assuming you already have a method to provide user updates to Braze, you’ll need to update that to include the new field `native_line_id` so that subsequent user updates sent to Braze will include that field.

Unidentified user profiles with a `native_line_id` may exist in Braze that were created as part of the subscription status sync process, or when a new follower followed your channel. 

When a LINE user is identified in your application through [user reconciliation](#user-id-reconciliation) or other means, you can target a potential unidentified user profile in Braze using the [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) endpoint. Every unidentified user profile with a `native_line_id` also has a user alias `line_id` that can be used to target the user profile to identify.

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

LINE users known in your application can be updated through the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) endpoint by passing their external identifiers and `native_line_id`. If an unidentified user profile already exists for a user and the same `native_line_id` is added to a different user profile through `/users/track`, it will inherit all the subscription states of the unidentified user profile. However, duplicate user profiles will exist with the same `native_line_id`. Any subsequent subscription updates from event updates will update all profiles accordingly. 

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

As described above, there's a possibilty for multiple user profiles to exist with the same `native_line_id`. If your update methods create duplicate user profiles, you can merge unidentified user profiles to identified user profiles with the `/user/merge` endpoint. 

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

## User setup

LINE is the source of truth for user subscription states. Even if you have the LINE ID for a user (`native_line_id`), if that user hasn't followed the LINE channel you're sending from, LINE won't deliver that channel's messages to the user.

To help manage this, Braze offers tooling and logic that supports a well-integrated user base, including subscription syncing and event updates for LINE follows and unfollows.

### Subscription syncing and event logic

1. **Subscription sync tool:** This can be used to gather the list of all the LINE IDs that are following your channel. There are two ways to use this tool:

| Usage | Description |
| --- | --- |
| Only update existing user profiles | All Braze user profiles that have a `native_line_id` that follows the LINE channel will be updated to have a subscription group status of “Subscribed”. |
| Update existing profile and create new | All Braze user profiles that have a `native_line_id` that follows the LINE channel will be updated to have a subscription group status of “Subscribed”. <br><br> Any follower of the LINE channel that doesn't have a Braze user profile with the `native_line_id` will have:<br> - An anonymous user profile created with `native_line_id` set to the user LINE ID following the channel <br>- A user alias `line_id` set to the user LINE ID following the channel <br>- A subscription group status of “Subscribed”. |
{: .reset-td-br-1 .reset-td-br-2}

{: start="2"}
2. **Event updates:** These can be used to update a user's subscription status. When Braze receives user event updates for the integrated LINE channel and the event is a follow, the user profile will have a subscription group status of “Subscribed”. If the event is an unfollow, the user profile will have a subscription group status of “Unsubscribed”.<br><br>- All Braze user profiles with a matching `native_line_id` will be automatically updated. <br>- If no matching user profile exists for an event, Braze will [create an anonymous user](https://www.braze.com/docs/line/user_management/).

## Use cases

These are use cases of how users can be updated after you follow the setup steps above.

##### Existing user profile follows LINE channel 

1. The Braze user profile is updated with a `native_line_id` attribute. Its default subscription status is “Unsubscribed”.
2. The subscription sync tool is run, finds that the user is following the LINE channel, and then updates the user profile with the subscription status “Subscribed”.
3. If any subscription status changes occur (such as the user blocks, unfriends, or refollows the channel), Braze receives the update from LINE and updates the user profile with the `native_line_id` accordingly.

##### Existing user profile blocks, unfriends, or unfollows LINE channel 

1. The Braze user profile is updated with a `native_line_id` attribute. Its default subscription status is “Unsubscribed”.
2. The subscription sync tool doesn't find that the user is following the LINE channel and the user’s subscription status remains as “Unsubscribed”.
3. If the user later follows the channel, Braze receives the update from LINE and updates the user profile with the subscription status “Subscribed”.

##### User profile creation occurs after LINE follow

1. The channel gets a new LINE follower.
2. Braze creates an anonymous user profile with the `native_line_id` attribute set to be the follower’s LINE ID, and a user alias of `line_id` set to be the follower’s LINE ID. The profile has a subscription status of “Subscribed”.
3. The user is identified as having the LINE ID through [user reconciliation](#user-id-reconciliation).
  - The anonymous user profile can become identified using the [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify) endpoint. Subsequent updates (through the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) endpoint, [CSV import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import), or [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion)) to this user profile can target the user by this known `external_id`.

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

  - A new user profile can be created (through the [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) endpoint, [CSV import]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#csv-import), or [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion)) by setting the `native_line_id`. This new profile will inherit the subscription status state of the existing anonymous user profile. Note that this will result in multiple profiles sharing the same `native_line_id`. These can be merged at any time using the `/users/merge` endpoint in the process outlined in [Step 5](#step-5-merge-profiles-optional).

##### User profile creation occurs before LINE follow

1. You acquire a new user and send the information to Braze. A new user profile is created (profile 1).
2. The user follows your LINE account.
3. Braze receives a follow event and creates an anonymous user profile (profile 2).
4. The user is identified as having the LINE ID through [user reconciliation](#user-id-reconciliation).
5. You update profile 1 to set the `native_line_id` attribute. This profile inherits the subscription status state of profile 2.
  - Now there are two user profiles with the same `native_line_id`. These can be merged at any time using the `/users/merge` endpoint in the process outlined in [Step 5](#step-5-merge-profiles-optional).

## User ID reconciliation 

LINE IDs are automatically received by Braze when a user follows your channel, or when you use the one-time “sync followers” workflow. LINE IDs are also specific to the channel that users follow, so it's unlikely that users can provide their LINE IDs.

To combine a LINE ID with an existing Braze user profile, you can use the LINE login method.

### LINE login

This method uses social media logins for reconciliation. When a user logs into your app, they're given the option to use the LINE login to create a user account or log in.

1. Implement the LINE login feature so users can log into your app. For details about implementation, refer to the LINE developer page. After implementation, you can get an access token by calling the [issue access token](https://developers.line.biz/en/reference/line-login/#oauth/) endpoint of the LINE login API. After that, you can get the user’s profile information from ID tokens that are included in the response from the [issue access token](https://developers.line.biz/en/reference/line-login/#oauth/) request.

2. After you get the profile information of a LINE follower, send their LINE user ID to Braze by calling the [user/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/) endpoint.

## Creating LINE test users in Braze

You can test your LINE channel before setting up [user reconciliation](#user-id-reconciliation) by creating a "Who am I" Canvas or campaign.

1. Set up a Canvas that returns a user's Braze user ID on a specific trigger word. <br><br>Example trigger <br><br>![Trigger to send the campaign to users who sent an inbound LINE to a specific subscription group.][7]{: style="max-width:80%;"}<br><br>Example message<br><br>![LINE message stating the Braze user ID.][8]{: style="max-width:40%;"}<br><br>

2. In Braze, you can use the Braze ID to search for specific users and modify them as needed.

{% alert important %}
Make sure the Canvas doesn't have global control or control groups preventing sends.
{% endalert %}


[1]: {% image_buster /assets/img/line/webhook_settings.png %}
[2]: {% image_buster /assets/img/line/response_settings.png %}
[3]: {% image_buster /assets/img/line/integration.png %}
[4]: {% image_buster /assets/img/line/line_subscription_groups.png %}
[5]: {% image_buster /assets/img/line/filter_group.png %}
[6]: {% image_buster /assets/img/line/csv_export_user_data.png %}
[7]: {% image_buster /assets/img/line/trigger.png %}
[8]: {% image_buster /assets/img/line/message.png %}
