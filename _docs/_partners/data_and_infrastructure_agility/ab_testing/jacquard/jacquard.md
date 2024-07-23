---
nav_title: Jacquard
article_title: Jacquard
page_order: 1
description: "This reference article outlines the partnership between Braze and Jacquard, an AI and computational linguistics platform that allows you to enhance customer experiences by optimizing language used across the full customer journey. Jacquard's deep learning engine handles the testing, monitoring, and generating of a new language based on what it learns."
page_type: partner
search_tag: Partner

---

# Jacquard

> [Jacquard][1] brings together artificial intelligence, computational linguistics, and a spirit of customer-centricity to help deploy brand language, at scale, across channels that are customized to your brand voice.

The Braze and Jacquard partnership allows you to enhance customer experiences by optimizing language used across the full customer journey. Jacquard's deep learning engine handles testing, monitoring, and generating new copy based on what it learns. 

To include click tracking information for your subscribers, using Braze Currents and Connected Content, check out Jacquard's additional [Jacquard React]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/jacquard/phrasee_react/) integration.

## Prerequisites

| Requirement | Description |
|---|---|
| Jacquard account | A [Jacquard account][3] is required to take advantage of this partnership. |
| Braze REST API key | A Braze REST API key with `campaigns` permissions. <br><br> This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint  | Your REST endpoint URL. Your endpoint will depend on the [Braze URL for your instance][2]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Integration

With this integration, you can integrate email or push campaigns into Jacquard. The following steps are detailed for both.

{% tabs %}
{% tab Email Campaign %}

### Email campaign

#### Step 1: Set up your campaign in Jacquard to generate the variants of your split test

Set up your Jacquard email campaign as you normally would. After you have approved your variants, you will be taken to the summary page. Here, you will need to copy the variants that will be added to your Braze campaign. If preferred, you can also select the **Download variants** button to download a text file containing all of your variants.

![A Jacquard campaign showing the available variants.]({% image_buster /assets/img/jacquard/3_phrasee_braze1.png %})

#### Step 2: Create your Braze email campaign

Navigate to the Braze dashboard to create your email campaign. When creating your campaign, add the tag **Email Campaign**. If this tag does not yet exist, create it.

![The Braze email builder emphasizing the email tag that can be added directly under the campaign description field.]({% image_buster /assets/img/jacquard/4_braze_emailtag.png %})

Next, select **Edit Sending Info** for each variant to paste the Jacquard variant into the subject line. Ensure the number of variants matches between Jacquard and Braze.

You will not need to recreate each email from scratch; you can simply copy the first variant and then edit the subject line for each new variant.

![Option to copy an existing email variant in Braze.]({% image_buster /assets/img/jacquard/5_copy_variant_braze.png %})

#### Step 3: Schedule your Braze campaign

Schedule your campaign to start at a specific time, this can also be done using the API and the [`/campaign/trigger/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/). You will need to know this time to plug into Jacquard.

![A scheduled delivery campaign sent at a designated time.]({% image_buster /assets/img/jacquard/6_braze_schedule.png %})

#### Step 4: Finalize the Braze campaign setup

Complete the remaining steps in Braze to set up your campaign. Under **A/B Testing**, select **Send Winning Variant**. Then select how long to wait before sending the Winning Variant.

![The A/B testing portion of the campaign showing how the A/B tests and control group will be split. Also shown are settings allowing you to determine the Winning Variant, sending information, and preferences for if the test ends up being statistically insignificant.]({% image_buster /assets/img/jacquard/7_braze_send_winner.png %})

Finalize any other settings as needed and save your campaign.

#### Step 5: Jacquard integration inputs

Navigate back to your Jacquard campaign and select the **Braze integration** button.

The schedule campaign window will pop up. Here, select your Braze campaign from the dropdown list. Next, select the date and time your campaign is scheduled to start and complete. Lastly, input the send time your A/B test is scheduled to complete, and save the details. The time zone of your Braze account will appear near the campaign dropdown to ensure the times align between applications.

Launch your campaign in Braze, and Jacquard has it from here! When your campaign test results are in, they will automatically appear in Jacquard. 

![The Jacquard platform showing the schedule campaign window where you can adjust the send settings.]({% image_buster /assets/img/jacquard/8_braze_int_drawer.png %})

{% alert note %}
Ensure your scheduled date and time match Braze's configured schedule so that Jacquard pulls in the results at the correct time.
{% endalert %}

{% endtab %}
{% tab Push Campaign %}

### Push campaign

#### Step 1: Set up your push campaign in Jacquard to generate the variants of your split test

Set up your Jacquard email campaign as you normally would. After you have approved your variants, you will be taken to the summary page. Here, you will need to copy the variants that will be added to your Braze campaign. If preferred, you can also select the **Download variants** button to download a .txt file containing all of your variants.

![A Jacquard campaign showing the available variants.]({% image_buster /assets/img/jacquard/3_phrasee_braze1.png %})

#### Step 2: Setup your Braze push campaign

Jacquard's integration will allow you to select both an iOS and an Android Braze push campaign to integrate into one Jacquard campaign if needed. To enable this functionality, ensure you tag it **Push Campaign**. This is required for step 4.

![The Braze email builder emphasizing the email tag that can be added directly under the campaign description field.]({% image_buster /assets/img/jacquard/9_braze_push_tag.png %})

#### Step 3: Copy the Jacquard variants into Braze

{% alert important %} 
For Jacquard to automatically pull the results of the variants within your push campaign, the variant text must be contained within the message body, not the 'Title'.
{% endalert %}

A Jacquard language model can generate two-line variants split between the 'Title' and 'Message'. Make sure that the second line is included in the message body; this way, Jacquard can automatically pull the results of the variants within your campaign.

![An example of Jacquard's two-line variant split language model shown in the Braze message composer.]({% image_buster /assets/img/jacquard/10_push_two_lines.png %})

You can also enter the whole Jacquard variant into the **Message body** for the results to be pulled correctly into Jacquard. In that instance, the 'Title' must remain constant across all variants to ensure an accurate test.

![An example of what a Jacquard variant may look like if you add the entire variant into the message body.]({% image_buster /assets/img/jacquard/11_push_messagebody.png %})

#### Step 4: Schedule your Braze campaign

Schedule your campaign to start at a specific time, this can also be done using the API and the [`/campaign/trigger/send` endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/). You will need to know this time to plug into Jacquard.

![A scheduled delivery campaign sent at a designated time.]({% image_buster /assets/img/jacquard/6_braze_schedule.png %})

#### Step 5: Finalize the Braze campaign setup

Complete the remaining steps in Braze to set up your campaign. Under **A/B Testing**, check the box to **Send Winning Variant**. Then select how long to wait before sending the Winning Variant.

![The A/B testing portion of a campaign showing how the A/B tests and control group will be split. Also shown are settings allowing you to determine the Winning Variant, sending information, and preferences for if the test ends up being statistically insignificant.]({% image_buster /assets/img/jacquard/7_braze_send_winner.png %})

Finalize any other settings as needed and save your campaign.

#### Step 6: Jacquard integration inputs

Navigate back to your Jacquard campaign and select the **Braze integration** button.

The schedule campaign window will pop up. Here, select your Braze campaign from the dropdown list. Next, select the date and time your campaign is scheduled to start and complete. Lastly, input the send time your A/B test is scheduled to complete, and save the details. The time zone of your Braze account will appear near the campaign dropdown to ensure the times align between applications.

Launch your campaign in Braze, and Jacquard has it from here! When your campaign test results are in, they will automatically appear in Jacquard. 

![The Jacquard platform schedule campaign window where you can adjust the send settings.]({% image_buster /assets/img/jacquard/8_braze_int_drawer.png %})

{% alert note %}
Ensure your scheduled date and time match Braze's configured schedule so that Jacquard pulls in the results at the correct time.
{% endalert %}

{% endtab %}
{% endtabs %}

[1]: https://www.jacquard.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: mailto:awesome@phrasee.co
[4]: {% image_buster /assets/img/jacquard/1_create_apikey.png %}
[5]: {% image_buster /assets/img/jacquard/2_campaignaccess.png %}
