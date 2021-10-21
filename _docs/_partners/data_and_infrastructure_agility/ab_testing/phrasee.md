---
nav_title: Phrasee
article_title: Phrasee
page_order: 1
description: "This article outlines the partnership between Braze and Phrasee, an AI and computational linguistics platform that allows you to deploy brand language, at scale, across channels that are customized to your brand voice. Phrasee’s deep learning engine handles the testing, monitors the results, and generates new language based on what it’s learned."
alias: /partners/phrasee/
page_type: partner
search_tag: Partner

---

# Phrasee

> Enhance customer experiences by optimizing language used across the full customer journey. the [Phrasee][1] platform brings together artificial intelligence, computational linguistics, and a spirit of customer-centricity as the only provider of its kind to generate, optimize, automate, and analyze language in real-time. Let us handle the content minutiae while your team focuses on the big picture.

Braze customer engagement develops relationships through multichannel marketing. Working together with Phrasee, Braze can deploy brand language, at scale, across channels that are customized to your brand voice. Phrasee’s deep learning engine handles the testing, monitors the results, and generates new language based on what it’s learned.

## Requirements

| Requirement | Origin | Description |
|---|---|---|
| Braze API Key | Braze | You will need to create a new API Key.<br>This can be created in the Developer Console -> API Settings -> **Create New API Key with Campaigns permissions**. | 
| Braze REST Endpoint | Braze | Your REST Endpoint URL. Your endpoint will depend on the Braze URL for [your instance][2]. |
| Phrasee Account | Phrasee | Contact [Phrasee][3] to sign up. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Server-to-server integration

Phrasee requires server-to-server application details to check for results in Braze while you are not logged in.

### Create a new Braze Phrasee API key

Navigate to the developer console within Braze and click __Create a New API Key__.

![api_key][4]

This API Key will only require access to **Campaigns**.

![campaigns][5]

Save and share this API Key along with your Braze REST Endpoint with Phrasee so we can complete the integration and link your campaigns.

## Using this integration

With this integration, you can integrate email or push campaigns into Phrasee. The steps are detailed below for both.

{% tabs %}
{% tab Email Campaign %}

### Email campaign

#### Step 1: Set up your campaign in Phrasee to generate the variants of your split test

Setup your Phrasee email campaign as you normally would. Once you have approved your variants, you will then be taken to the summary page. Here, you will need to copy the variants that will be added to your Braze campaign. If preferred, you can also click the **Download variants** button to download a .txt file containing all of your variants.

![phrasee_campaign]({% image_buster /assets/img/phrasee/3_phrasee_braze1.png %})

#### Step 2: Create your Braze email campaign

Navigate to the Braze dashboard to create your email campaign. When creating your campaign, add the tag __Email Campaign__. If this tag does not yet exist, create it.

![tag]({% image_buster /assets/img/phrasee/4_braze_emailtag.png %})

Next for each variant, click __Edit Sending Info__ to paste the Phrasee Variant into the Subject Line. **Ensure the number of variants match between Phrasee and Braze.** 

Please note that you will not need to recreate each email from scratch, you can simply copy the first variant and then edit the subject line for each new variant.

![copy_variant]({% image_buster /assets/img/phrasee/5_copy_variant_braze.png %})

#### Step 3: Schedule your Braze campaign

Schedule your campaign to start at a specific time. __You’ll need to know this time to plug into Phrasee.__

![schedule_braze]({% image_buster /assets/img/phrasee/6_braze_schedule.png %})

#### Step 4: Finalize the Braze campaign setup

Complete the remaining steps in Braze to set up your campaign. Check the box to Send Winning Variant. Then select how long to wait before sending the Winning Variant.

![send_winner]({% image_buster /assets/img/phrasee/7_braze_send_winner.png %})

Finalize any other settings as needed and save your campaign.

#### Step 5: Phrasee integration inputs

Navigate back to your Phrasee campaign and click the __Braze integration__ button.

The integration window will pop out:
1. Select your Braze campaign from the dropdown list.
2. Select the date and time that your Braze campaign is scheduled to start. The time zone of your Braze account will appear below the campaign dropdown to ensure the times align between applications.
3. Select the date and time that your Braze A/B test is scheduled to complete.
4. Select the date and time that your Braze campaign will complete. This is the date when the final results will be pulled into the Phrasee system.
6. Save the details.

![phrasee_drawer]({% image_buster /assets/img/phrasee/8_braze_int_drawer.png %})

{% alert note %}
Ensure your scheduled date and time match what was configured within Braze so that Phrasee pulls in the results at the correct time.
{% endalert %}

Launch your campaign in Braze and Phrasee has it from here! When your campaign test results are in, they will automatically appear in Phrasee. 

{% endtab %}
{% tab Push Campaign %}

### Push campaign

#### Step 1: Set up your push campaign in Phrasee to generate the variants of your split test

Setup your Phrasee push campaign as you normally would. Once you have approved your variants, you will then be taken to the summary page. Here, you will need to copy the variants that will be added to your Braze campaign. If preferred, you can also click the **Download variants** button to download a .txt file containing all of your variants.

![phrasee_campaign]({% image_buster /assets/img/phrasee/3_phrasee_braze1.png %})

#### Step 2: Setup your Braze push campaign

Phrasee’s integration will allow you to select both an iOS and an Android Braze push campaign to integrate into one Phrasee campaign if needed. To enable this functionality, when creating your push campaign in Braze, ensure you tag it __Push Campaign__ (as seen below). __This is required for step 4.__

![push_tag]({% image_buster /assets/img/phrasee/9_braze_push_tag.png %})

#### Step 3: Copy the Phrasee variants into Braze

{% alert important %} 
For Phrasee to automatically pull the results of the variants within your push campaign, the variant text must be contained within the message body, not the Title.
{% endalert %}

With a Phrasee language model, it is capable of generating two line variants that can be split between the ‘Title’ and ‘Message’. Make sure that the second line is included in the message body, this way, Phrasee can automatically pull the results of the variants within your campaign.

![push_twolines]({% image_buster /assets/img/phrasee/10_push_two_lines.png %})

You can also enter the whole Phrasee variant into the **Message body** for the results to be pulled correctly into Phrasee. __In that instance, the ‘Title’ must remain constant across all variants to ensure an accurate test.__

![push_oneline]({% image_buster /assets/img/phrasee/11_push_messagebody.png %})

#### Step 4: Schedule your Braze campaign

Schedule your campaign to start at a specific time. __You’ll need to know this time to plug into Phrasee.__

![schedule_braze]({% image_buster /assets/img/phrasee/6_braze_schedule.png %})

#### Step 5: Finalize the Braze campaign setup

Complete the remaining steps in Braze to set up your campaign. Check the box to __Send Winning Variant__. Then select how long to wait before sending the Winning Variant.

![send_winner]({% image_buster /assets/img/phrasee/7_braze_send_winner.png %})

#### Step 6: Phrasee integration inputs

Navigate back to your Phrasee campaign and click the __Braze integration__ button.

The integration window will pop out:
1. Select your Braze campaign(s) from the dropdown list.
2. Select the date and time that your Braze campaign is scheduled to start. The time zone of your Braze account will appear below the campaign dropdown to ensure the times align between applications.
3. Select the date and time that your Braze A/B test is scheduled to complete.
4. Select the date and time that your Braze campaign will complete. This is the date when the final results will be pulled into the Phrasee system.
6. Save the details.

![phrasee_drawer]({% image_buster /assets/img/phrasee/8_braze_int_drawer.png %})

{% alert note %}
Ensure your scheduled date and time match what you configured within Braze so that Phrasee pulls in the results at the correct time.
{% endalert %}

Launch your campaign in Braze and Phrasee has it from here! When your campaign test results are in, they will automatically appear in Phrasee. 

{% endtab %}
{% endtabs %}

[1]: https://phrasee.co/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: mailto:awesome@phrasee.co
[4]: {% image_buster /assets/img/phrasee/1_create_apikey.png %}
[5]: {% image_buster /assets/img/phrasee/2_campaignaccess.png %}
