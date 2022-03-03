---
nav_title: Phrasee
article_title: Phrasee
page_order: 1
description: "This article outlines the partnership between Braze and Phrasee, an AI and computational linguistics platform that allows you to enhance customer experiences by optimizing language used across the full customer journey. Phrasee's deep learning engine handles the testing, monitoring, and generating of a new language based on what it learns."
alias: /partners/phrasee/
page_type: partner
search_tag: Partner

---

# Phrasee

> [Phrasee][1] brings together artificial intelligence, computational linguistics, and a spirit of customer-centricity to help deploy brand language, at scale, across channels that are customized to your brand voice.

The Braze and Phrasee partnership allows you to enhance customer experiences by optimizing language used across the full customer journey. Phrasee's deep learning engine handles testing, monitoring, and generating new copy based on what it learns.

## Prerequisites

| Requirement | Description |
|---|---|
| Phrasee account | A [Phrasee account][3] is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `campaigns` permissions. <br><br> This can be created within the **Braze Dashboard > Developer Console > REST API Key > Create New API Key**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance][2]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration

With this integration, you can integrate email or push campaigns into Phrasee. The steps are detailed below for both.

{% tabs %}
{% tab Email Campaign %}

### Email campaign

#### Step 1: Set up your campaign in Phrasee to generate the variants of your split test

Set up your Phrasee email campaign as you normally would. Once you have approved your variants, you will be taken to the summary page. Here, you will need to copy the variants that will be added to your Braze campaign. If preferred, you can also click the **Download variants** button to download a .txt file containing all of your variants.

![An image of a Phrasee campaign showing the available variants.]({% image_buster /assets/img/phrasee/3_phrasee_braze1.png %})

#### Step 2: Create your Braze email campaign

Navigate to the Braze dashboard to create your email campaign. When creating your campaign, add the tag **Email Campaign**. If this tag does not yet exist, create it.

![The Braze email builder emphasizing the email tag that can be added directly under the campaign description field.]({% image_buster /assets/img/phrasee/4_braze_emailtag.png %})

Next, click **Edit Sending Info** for each variant to paste the Phrasee variant into the subject line. Ensure the number of variants matches between Phrasee and Braze.

You will not need to recreate each email from scratch; you can simply copy the first variant and then edit the subject line for each new variant.

![An image showing how to copy an existing email variant in Braze.]({% image_buster /assets/img/phrasee/5_copy_variant_braze.png %})

#### Step 3: Schedule your Braze campaign

Schedule your campaign to start at a specific time. You will need to know this time to plug into Phrasee.

![The delivery step in the campaign builder.]({% image_buster /assets/img/phrasee/6_braze_schedule.png %})

#### Step 4: Finalize the Braze campaign setup

Complete the remaining steps in Braze to set up your campaign. Under **A/B Testing**, check the box to **Send Winning Variant**. Then select how long to wait before sending the winning variant.

![The A/B testing portion of the campaign showing how the A/B tests and control group will be split. Also shown are settings allowing you to determine the winning variant, sending information, and preferences for if the test ends up being statistically insignificant.]({% image_buster /assets/img/phrasee/7_braze_send_winner.png %})

Finalize any other settings as needed and save your campaign.

#### Step 5: Phrasee integration inputs

Navigate back to your Phrasee campaign and click the **Braze integration** button.

The schedule campaign window will pop up. Here, select your Braze campaign from the dropdown list. Next, select the date and time your campaign is scheduled to start and complete. Lastly, input the send time your A/B test is scheduled to complete, and save the details. The time zone of your Braze account will appear below the campaign dropdown to ensure the times align between applications.

Launch your campaign in Braze, and Phrasee has it from here! When your campaign test results are in, they will automatically appear in Phrasee. 

![The Phrasee platform showing the schedule campaign window where you can adjust the send settings.]({% image_buster /assets/img/phrasee/8_braze_int_drawer.png %})

{% alert note %}
Ensure your scheduled date and time match Braze's configured schedule so that Phrasee pulls in the results at the correct time.
{% endalert %}

{% endtab %}
{% tab Push Campaign %}

### Push campaign

#### Step 1: Set up your push campaign in Phrasee to generate the variants of your split test

Set up your Phrasee email campaign as you normally would. Once you have approved your variants, you will be taken to the summary page. Here, you will need to copy the variants that will be added to your Braze campaign. If preferred, you can also click the **Download variants** button to download a .txt file containing all of your variants.

![An image of a Phrasee campaign showing the available variants.]({% image_buster /assets/img/phrasee/3_phrasee_braze1.png %})

#### Step 2: Setup your Braze push campaign

Phrasee’s integration will allow you to select both an iOS and an Android Braze push campaign to integrate into one Phrasee campaign if needed. To enable this functionality, ensure you tag it **Push Campaign**. This is required for step 4.

![The Braze email builder emphasizing the email tag that can be added directly under the campaign description field.]({% image_buster /assets/img/phrasee/9_braze_push_tag.png %})

#### Step 3: Copy the Phrasee variants into Braze

{% alert important %} 
For Phrasee to automatically pull the results of the variants within your push campaign, the variant text must be contained within the message body, not the Title.
{% endalert %}

A Phrasee language model can generate two-line variants split between the ‘Title’ and ‘Message’. Make sure that the second line is included in the message body; this way, Phrasee can automatically pull the results of the variants within your campaign.

![An example of Phrasee's two-line variant split language model shown in the Braze message composer.]({% image_buster /assets/img/phrasee/10_push_two_lines.png %})

You can also enter the whole Phrasee variant into the **Message body** for the results to be pulled correctly into Phrasee. In that instance, the ‘Title’ must remain constant across all variants to ensure an accurate test.

![An example of what a Phrasee variant may look like if you add the entire variant into the message body.]({% image_buster /assets/img/phrasee/11_push_messagebody.png %})

#### Step 4: Schedule your Braze campaign

Schedule your campaign to start at a specific time. You will need to know this time to plug into Phrasee.

![The delivery step in the campaign builder.]({% image_buster /assets/img/phrasee/6_braze_schedule.png %})

#### Step 5: Finalize the Braze campaign setup

Complete the remaining steps in Braze to set up your campaign. Under **A/B Testing**, check the box to **Send Winning Variant**. Then select how long to wait before sending the winning variant.

![The A/B testing portion of a campaign showing how the A/B tests and control group will be split. Also shown are settings allowing you to determine the winning variant, sending information, and preferences for if the test ends up being statistically insignificant.]({% image_buster /assets/img/phrasee/7_braze_send_winner.png %})

Finalize any other settings as needed and save your campaign.

#### Step 6: Phrasee integration inputs

Navigate back to your Phrasee campaign and click the **Braze integration** button.

The schedule campaign window will pop up. Here, select your Braze campaign from the dropdown list. Next, select the date and time your campaign is scheduled to start and complete. Lastly, input the send time your A/B test is scheduled to complete, and save the details. The time zone of your Braze account will appear below the campaign dropdown to ensure the times align between applications.

Launch your campaign in Braze, and Phrasee has it from here! When your campaign test results are in, they will automatically appear in Phrasee. 

![The Phrasee platform schedule campaign window where you can adjust the send settings.]({% image_buster /assets/img/phrasee/8_braze_int_drawer.png %})

{% alert note %}
Ensure your scheduled date and time match Braze's configured schedule so that Phrasee pulls in the results at the correct time.
{% endalert %}

{% endtab %}
{% endtabs %}

[1]: https://phrasee.co/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: mailto:awesome@phrasee.co
[4]: {% image_buster /assets/img/phrasee/1_create_apikey.png %}
[5]: {% image_buster /assets/img/phrasee/2_campaignaccess.png %}