---
nav_title: Phrasee
page_order: 1

description: "This is the Google Search and SEO description that will appear, try to make this informative and concise, yet brief."
alias: /partners/phrasee/

page_type: partner
hidden: true
---

# Phrasee

Enhance customer experiences by optimizing language used across the full customer journey.\
The Phrasee platform brings together artificial intelligence, computational linguistics, and a spirit
of customer-centricity as the only provider of its kind to generate, optimize, automate, and
analyze language in real-time. Let us handle the content minutiae while your team focuses on the big picture.

Braze customer engagement develops relationships through multichannel marketing. Working
together with Phrasee, Braze can deploy brand language, at scale, across channels that’s
customized to your brand voice.

Phrasee’s deep learning engine handles the testing, monitors the results, and generates new
language based on what it’s learned. Just set it up and click the magic button.

For more information, check out the [Phrasee Website][1].

## Requirements or Pre-Requisites

| Requirement | Origin | Access | Description |
|---|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key. This can be created in the Developer Console -> API Settings -> **Create New API Key with Campaigns permissions**. | You can name this Phrasee App API Key |
| Braze REST Endpoint | Braze | [Braze REST Endpoint List][2] | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for your instance. |
| Phrasee Account | Phrasee | Contact Phrasee | Email: [awesome@phrasee.co][3] |

## Server to Server Integration

Phrasee requires server-to-server application details in order to check for results in Braze while
you are not logged in.

### Step 1: Create a new Braze Phrasee API Key

Navigate to the Developer Console within Braze and click to create a New API Key.

![api_key][4]

This API Key will only require access to **Campaigns**.

![campaigns][5]

Save and share this API Key along with your Braze REST Endpoint with Phrasee so we can
complete the integration and link your campaigns.

## Using This Integration

With this integration, you can integrate Email or Push Campaigns into Phrasee. The steps are
detailed below for both.

### Email Campaign

### Step 1: Setup your campaign in Phrasee to generate the variants of your split test.

Setup your Phrasee email campaign as you normally would. Once you have approved your
variants, you’ll be taken to the summary page.
From here, you’ll need to copy the variants to paste into your Braze campaign. If preferred, you
can click the **Download variants** button to download a .txt file containing all of your variants
for easy copy and paste into Braze.

![phrasee_campaign][6]

### Step 2: Create your Braze Email Campaign

Navigate to Braze to create your Braze email campaign.

When creating your Braze campaign, add the tag ‘Email Campaign’. If this tag does not yet
exist, you can add it.

![tag][7]

Next for each variant, click ‘Edit Sending Info’ to paste the Phrasee Variant into the Subject
Line. **Ensure the number of variants match between Phrasee and Braze.**
You will not need to recreate each email from scratch. Simply copy Variant 1 and then just edit
the subject line for each new variant.

![copy_variant][8]

### Step 3: Schedule your Braze Campaign

Schedule your Campaign to start at a specific time.
>You’ll need to know this time to plug into Phrasee.

![schedule_braze][9]

### Step 4: Finalize the Braze Campaign Setup

Check the box to ‘Send Winning Variant’. Then select how long to wait prior to sending the
Winning Variant.

![send_winner][10]

Finalize any other settings as needed and Save your Campaign.

### Step 5: Phrasee Integration Inputs

Navigate back to Phrasee and your campaign. Click the Braze Integration button.

![phrasee_campaign][6]

The integration drawer will pop out:
1. Select your Braze campaign from the dropdown list.
2. Select the date and time that your Braze campaign is scheduled to start. The time zone of your Braze Account will appear below the campaign dropdown to ensure the
times align between applications.
3. Select the date and time that your Braze A/B test is scheduled to complete.
4. Select the date and time that your Braze Campaign will complete.
5. This is the date when the final results will be pulled into the Phrasee system.
6. Save the details

{% alert note %}
Ensure your schedule date and time match what you configured within Braze so that Phrasee pulls in the results at the correct time.
{% endalert %}

![phrasee_drawer][11]

{% alert important %} Launch your Campaign in Braze and Phrasee has it from here! When your
Campaign test results are in, they will automatically appear in Phrasee. {% endalert %}

### Push Campaign

### Step 1: Setup your Push Campaign in Phrasee to generate the variants of your split test

Setup your Phrasee Push Campaign as you normally would. Once you have approved your
variants, you’ll be taken to the summary page.
From here, you’ll need to copy the variants to paste into your Braze campaign.

![phrasee_campaign][6]

### Step 2: Setup your Braze Push Campaign

Phrasee’s integration will allow you to select both an iOS and an Android Braze push campaign
to integrate into one Phrasee campaign if needed.
>To enable this functionality, when creating your Push campaign in Braze, ensure you tag it
‘Push Campaign’ (as seen below). This is required for Step 4.

![push_tag][12]

### Step 3: Copy the Phrasee Variants into Braze

{% alert important %} In order for Phrasee to automatically pull the results of the variants within
your push campaign, the variant text must be contained within the Message body, not the Title.
{% endalert %}
With a Phrasee language model capable of generating two line variants, you can split the lines
between the ‘Title’ and ‘Message’. Just make sure that the second line is included in the
Message body.
This way Phrasee can automatically pull the results of the variants within your campaign.

![push_twolines][13]

You can also enter the whole Phrasee variant into the **Message body** in order for the results
to be pulled correctly into Phrasee.
**In that instance, the ‘Title’ must remain constant across all variants to ensure an accurate
test.**

![push_oneline][14]

### Step 4: Schedule your Braze Campaign

Schedule your Campaign to start at a specific time.

>You’ll need to know this time to plug into Phrasee.

![schedule_braze][9]

### Step 5: Finalize the Braze Campaign Setup

Complete the remaining steps in Braze to setup your campaign. Check the box to ‘Send
Winning Variant’. Then select how long to wait prior to sending the Winning Variant.

![send_winner][10]

### Step 6: Phrasee Integration Inputs

Return to the Phrasee application
Click the Braze Integration button on your Campaign.

![phrasee_campaign][6]

### Step 7: Phrasee Integration Inputs

Navigate back to Phrasee and your campaign. Click the Braze Integration button.
The integration drawer will pop out:
1. Select your Braze campaign(s) from the dropdown list.
2. Select the date and time that your Braze campaign is scheduled to start. The time zone of your Braze Account will appear below the campaign dropdown to ensure the
times align between applications.
3. Select the date and time that your Braze A/B test is scheduled to complete.
4. Select the date and time that your Braze Campaign will complete.
5. This is the date when the final results will be pulled into the Phrasee system.
6. Save the details.

{% alert note %}
Ensure your schedule date and time match what you configured within Braze so that Phrasee pulls in the results at the correct time.
{% endalert %}

![phrasee_drawer][11]

{% alert important %} Launch your Campaign in Braze and Phrasee has it from here! When your
Campaign test results are in, they will automatically appear in Phrasee. {% endalert %}
[1]: https://phrasee.co/
[2]: https://www.braze.com/docs/developer_guide/rest_api/basics/#endpoints
[3]: mailto:awesome@phrasee.co
[4]: {% image_buster /assets/img/phrasee/1_Create_APIKey.png %}
[5]: {% image_buster /assets/img/phrasee/2_CampaignAccess.png %}
[6]: {% image_buster /assets/img/phrasee/3_Phrasee_Braze1.png %}
[7]: {% image_buster /assets/img/phrasee/4_Braze_Emailtag.png %}
[8]: {% image_buster /assets/img/phrasee/5_Copy_Variant_Braze.png %}
[9]: {% image_buster /assets/img/phrasee/6_Braze_Schedule.png %}
[10]: {% image_buster /assets/img/phrasee/7_Braze_Send_Winner.png %}
[11]: {% image_buster /assets/img/phrasee/8_Braze_Int_Drawer.png %}
[12]: {% image_buster /assets/img/phrasee/9_Braze_Push_Tag.png %}
[13]: {% image_buster /assets/img/phrasee/10_Push_Two_Lines.png %}
[14]: {% image_buster /assets/img/phrasee/11_Push_MessageBody.png %}