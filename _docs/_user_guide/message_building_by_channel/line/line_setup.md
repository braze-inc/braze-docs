---
nav_title: LINE Setup
article_title: LINE Setup
alias: /partners/line/
description: "This article covers how to set up the Braze LINE channel, including prerequisites and suggested next steps."
page_type: partner
search_tag: Partner
page_order: 0
channel:
  - LINE
search_rank: 2
---

# LINE setup

> MSD_COPY

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
    - Turn on **Use webhook** and **Webhook redelivery**. <br><br> ![][]
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

![][]

### Step 2: Set up your LINE page in Braze

1. Go to the Braze Technology Partners page for LINE and input the information you noted from your LINE **Providers** tab:
    - Provider ID
    - Channel ID
    - Channel secret
    - Channel access token

2. After connecting, Braze will automatically generate a Braze subscription group for each LINE integration that's successfully added to your workspace. <br><br> Any changes to your followers list (such as new followers or unfollowers) will be automatically pushed into Braze. Learn more about LINE follows in [Line Follows]().

![][]

## Types of LINE accounts