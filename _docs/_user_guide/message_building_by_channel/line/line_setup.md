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

## Integration

### Step 1: Connect your LINE channel to Braze

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

### Step 2: Set up your LINE page in Braze

1. Go to the Braze Technology Partners page for LINE and input the information you noted from your LINE **Providers** tab:
   - Provider ID
   - Channel ID
   - Channel secret
   - Channel access token

![LINE messaging integration page with LINE integration section.][3]{: style="max-width:80%;"}

{: start="2"}
2. After connecting, Braze will automatically generate a Braze subscription group for each LINE integration that's successfully added to your workspace. <br><br> Any changes to your followers list (such as new followers or unfollowers) will be automatically pushed into Braze.

![LINE subscription groups section displaying one subscription group for the "LINE" channel.][4]{: style="max-width:80%;"}

## Types of LINE accounts

| Account type | Description |
| --- | --- |
| Unverified account | An unreviewed account that can be obtained by anyone (individual or corporate). This account is represented with a gray badge and won't appear in search results within the LINE app. |
| Verified account | An account that has passed the LINE Yahoo screening. This account is represented with a blue badge and will appear in search results within the LINE app.<br><br>This account is only available for accounts based in Japan, Taiwan, Thailand, and Indonesia.  |
| Premium account | An account that has passed the LINE Yahoo screening. This account is represented with a green badge and will appear in search results within the LINE app. This account type is automatically granted during the screening at LINE's discretion. |
{: .reset-td-br-1 .resest-td-br-2}

## Sync existing followers into Braze

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

## User ID reconciliation 

LINE IDs are automatically received by Braze when a user follows your channel, or when you use the one-time “sync followers” workflow. LINE IDs are also specific to the channel that users follow, so it's unlikely that users can provide their LINE IDs.

To combine a LINE ID with an existing Braze user profile, you can use the LINE login method.

### LINE login

This method uses social media logins for reconciliation. When a user logs into your app, they're given the option to use the LINE login to create a user account or log in.

1. Implement the LINE login feature so users can log into your app. For details about implementation, refer to the LINE developer page. After implementation, you can get an access token by calling the [issue access token](https://developers.line.biz/en/reference/line-login/#oauth/) endpoint of the LINE login API. After that, you can get the user’s profile information from ID tokens that are included in the response from the [issue access token](https://developers.line.biz/en/reference/line-login/#oauth/) request.

2. After you get the profile information of a LINE follower, send their LINE user ID to Braze by calling the [user/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users/) endpoint.

## Create LINE test users in Braze

You can test your LINE channel before setting up user reconciliation in two ways:

### Reference your LINE segment

1. After connecting your account, follow your LINE channel.

2. In Braze, go to **Segments** and create a segment for your LINE subscription group. <br><br>![Filter group with a subscription group.][5]{: style="max-width:80%;"}<br><br>

3. Select **User Data** > **CSV Export User Data**. <br><br>![Segment Details with a segment named "line subscribed" and the "User Data" menu with a list of export options.][6]{: style="max-width:80%;"}<br><br>

4. In the CSV download, reference the `created_at` field and when you followed your LINE channel to find your users.

5. In Braze, use the Appboy ID to search for specific users and modify them as needed.

### Create a "Who am I" Canvas or campaign

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