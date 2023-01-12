---
nav_title: Creating an Email
article_title: Creating an Email
page_order: 1
description: "This reference article covers how to create an email using the Braze platform. Included are best practices on how to compose your messages, preview your content, and schedule your campaign or Canvas."
tool:
  - Campaigns
channel:
  - email
  
---

# Creating an email campaign

> This article covers how to create an email campaign in Braze. Here, we'll cover steps and best practices on how to compose your message, preview your content, and schedule your campaign.

Email messages are great for delivering content to your users on their terms. They are also excellent tools to re-engage users who may have even uninstalled your app. Sending customized and tailored email messages will enhance your users' experience, and help your users get the most value out of your app. To see examples of email campaigns, check out our [Case Studies](https://www.braze.com/customers). 

{% alert tip %}
If this is your first time creating an email campaign, we highly recommend that you check out the following Braze Learning courses:<br>

- [Email](https://learning.braze.com/messaging-channels-email)
- [Project: Build a basic email marketing program](https://learning.braze.com/project-build-a-basic-email-marketing-program)

{% endalert %}

## Step 1: Choose where to build your message

Not sure whether your message should be sent using a campaign or a Canvas? Campaigns are better for single, simple messaging campaigns, while Canvases are better for multi-step user journeys.

{% tabs %}
{% tab Campaign %}
**Steps:**

1. Go to the **Campaigns** page and click <i class="fas fa-plus"></i> **Create Campaign**.
2. Select **Email**, or, for campaigns targeting multiple channels, select **Multichannel Campaign**.
3. Name your campaign something clear and meaningful.
4. Add [Teams]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) and [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) as needed.
   * Tags make your campaigns easier to find and build reports out of. For example, when using the [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), you can filter by particular tags.
5. Add and name as many variants as you need for your campaign. For more on this topic, refer to [Multivariate and A/B testing]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
If all of the messages in your campaign are going to be similar or have the same content, compose your message before adding additional variants. You can then choose **Copy from Variant** from the **Add Variant** dropdown.
{% endalert %}
{% endtab %}
{% tab Canvas %}

**Steps:**

1. [Create your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) using the Canvas wizard.
2. After you've set up your Canvas, add a step in the Canvas builder. Name your step something clear and meaningful.
3. Choose a [step schedule]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) and specify a delay as needed.
4. Filter your Audience for this step, as necessary. You can further refine the recipients of this step by specifying segments and adding additional filters. Audience options will be checked after the delay, at the time messages are sent.
5. Choose your [advancement behavior]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choose any other messaging channels that you would like to pair with your message.
{% endtab %}
{% endtabs %}

## Step 2: Select your editing experience {#step-2-choose-your-template-and-compose-your-email}

Braze offers two editing experiences when creating an email campaign: our [Drag & Drop editor]({{site.baseurl}}/dnd/) and our standard HTML editor. Click on the appropriate tile to select which editing experience you'd prefer. 

![Choosing between Drag & Drop Editor or HTML editor for your email editing experience.][3]{: style="max-width:75%" }

Then, you can either select an existing [email template][10], [upload a template][18] from a file (HTML editor only), or use a blank template. 

{% alert tip %}
We recommend selecting one editing experience per email campaign. For example, choose either the HTML Classic or Block editor in a single email campaign rather than switching between editors.
{% endalert %}

## Step 3: Compose your email

After you've selected your template, you'll see an overview of your email where you can quickly jump to the full-screen editor to draft your email, change your sending info, and view warnings about deliverability or law compliance. 

Composing your email in the Drag & Drop editor? Refer to the [Drag & Drop Editor overview]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/) for help composing your email. 

![Email Variants panel for composing your email.][14]{: style="max-width:75%" }

{% alert tip %}
Need help creating awesome copy? Try using the [AI copywriting assistant]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/). Input a product name or description and the AI will generate human-like marketing copy for use in your messaging.

![Launch AI Copywriter button, located in the Body tab of the email composer.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

{% alert important %}
Braze will automatically remove HTML event handlers referenced as attributes. Note that this does modify the HTML, and it is recommended to validate or re-check the email once completed. Learn more about [HTML handlers](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

### Step 3a: Add email headers

To add email headers, click **Edit Sending Info** and select **Add New Header**.

Email headers contain information about the email being sent. These [key-value pairs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) typically have information about the sender, recipient, authentication protocols, and contain email routing information. Braze automatically adds the necessary header information required by the RFC for emails to be delivered to your inbox provider properly.

However, Braze does allow you the flexibility to add additional email headers as needed for advanced use cases. There are a few reserved fields that the Braze platform will overwrite during sending. 

Avoid using the following keys:

<style>
#reserved-fields td {
    word-break: break-word;
    width: 33%;
}
</style>

<table id="reserved-fields">
<thead>
  <tr>
    <th>Reserved Fields</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BCC</td>
    <td>dkim-signature</td>
    <td>Reply-To</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>From</td>
    <td>Subject</td>
  </tr>
  <tr>
    <td>Content-Transfer-Encoding</td>
    <td>MIME-Version</td>
    <td>To</td>
  </tr>
  <tr>
    <td>Content-Type</td>
    <td>Received</td>
    <td>x-sg-eid</td>
  </tr>
  <tr>
    <td>DKIM-Signature</td>
    <td>received</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

### Step 3b: Preview and test your message

After you finish composing your perfect email, you need to test it before sending it out.

From the bottom of the overview screen, click **Preview and Test**. Here you can preview how your email will appear in a customer's inbox. With **Preview as User** selected, you can preview your email as a random user, select a specific user, or create a custom user. This allows you to test that your Connected Content and personalization calls are working as they should.

You can also switch between desktop, mobile, and plaintext views to get a sense of how your message will appear in different contexts.

{% alert tip %}
Curious about what your email looks like for dark mode users? Select the **Dark Mode Preview** toggle located in the **Preview and Test** section (Drag & Drop Editor only).
{% endalert %}

When you're ready for a final check, select **Test Send** and send a test message to yourself or a group of content testers to ensure that your email displays properly on a variety of devices and email clients.

![Test Send option and example email preview when composing your email.][15]

If you see any issues with your email, or want to make any changes, click **Edit Email** to return to the editor.

{% alert tip %}
Email clients that support preview text always pull in enough characters to fill all available preview text space. However, this can leave you in situations where the preview text is incomplete or unoptimized.
<br><br>To avoid this, you can create white space after your desired preview text so that email clients don’t pull other distracting text or characters into the envelope content. To do so, add a chain of zero-width non-joiners (‌`&zwnj;`) and non-breaking spaces (`&nbsp;`) after the preview text that you want displayed. <br><br>When added to the end of your preview text in the preheader section, the following piece of code will add the white space you’re looking for:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```

{% endalert %}

### Step 3c: Check for email errors

The editor will call out any problems it catches with your message before you send it. Here's a list of errors that are accounted for in our editor:

- **From Display Name** and **Header** not specified together
- Invalid **From** and **Reply-To** addresses
- Duplicate **Header** keys
- Liquid syntax problems
- Email bodies larger than 400kb (bodies are highly recommended to be [smaller than 102kb][16])
- Emails with a blank **Body** or **Subject**
- Emails without an unsubscribe link
- Email you're sending from is not whitelisted (sends will be highly limited to ensure deliverability)

## Step 4: Build the remainder of your campaign or Canvas

{% tabs %}
{% tab Campaign %}
Next, build the remainder of your campaign! See the following sections for further details on how to best utilize our tools to build your email campaign.

#### Choose delivery schedule or trigger

Emails can be delivered based on a scheduled time, an action, or based on an API trigger. For more, refer to [Scheduling your campaign]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

{% alert note %}
For API-triggered campaigns, when the trigger action is set to **Interact With Campaign**, selecting a **Receive** option as the interaction will cause your new campaign to trigger as soon as Braze marks the selected campaign as sent, even if that message bounces or fails to be delivered.
{% endalert %}

You can also set the campaign's duration, specify [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours), and set [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) rules.

#### Choose users to target

Next, you need to [target users]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) by choosing segments or filters to narrow down your audience. You'll automatically be given a snapshot of what that segment population looks like right now, including how many users within that segment are reachable via email. Keep in mind that exact segment membership is always calculated just before the message is sent.

You can also choose to only send your campaign to users who have a specific [subscription status]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), such as those who are subscribed and opted in to email.

Optionally, you can also limit delivery to a specified number of users within the segment, or allow users to receive the same message twice upon a recurrence of the campaign.

##### Multichannel campaigns with email and push

For multichannel campaigns targeting both email and push channels, you may want to limit your campaign so that only the users who are explicitly opted in will receive the message (excluding subscribed or unsubscribed users). For example, say you have three users of different opt-in statuses:

- **User A** is subscribed to email and is push enabled. This user doesn't receive the email but will receive the push.
- **User B** is opted-in to email but is not push enabled. This user will receive the email but doesn't receive the push.
- **User C** is opted-in to email and is push enabled. This user will receive both the email and the push.

To do so, under **Audience Summary**, select to send this campaign to "opted-in users only". This option will ensure that only opted-in users will receive your email, and Braze will only send your push to users who are push enabled by default.

{% alert important %}
With this configuration, don't include any filters in the **Target Users** step that limit the audience to a single channel (e.g., `Push Enabled = True` or `Email Subscription = Opted-In`).
{% endalert %}

#### Choose conversion events

Braze allows you to track how often users perform specific actions, [conversion events]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), after receiving a campaign. You can specify any of the following actions as a conversion event:

- Opens app
- Makes purchase (This can be a generic purchase or a specific item)
- Performs specific custom event
- Opens email

You can allow up to a 30-day window during which a conversion will be counted if the user takes the specified action. While Braze automatically tracks opens and clicks for your campaign, you may wish to set the conversion event to be when a user opens or clicks on an email address to take advantage of Braze's [Intelligent Selection]({{site.baseurl}}/user_guide/intelligence/intelligent_selection/) feature.
{% endtab %}

{% tab Canvas %}
If you haven't done so already, complete the remaining sections of your Canvas components. For further details on how build out the rest of your Canvas, implement multivariate testing and Intelligent Selection, and more, refer to the [Build your Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) step of our Canvas documentation.
{% endtab %}
{% endtabs %}

## Step 5: Review and deploy

The final page will give you a summary of the campaign you've just designed. Confirm all the relevant details and click **Launch Campaign** to enable it for sending.

Now just wait for all the data to roll in! Next, check out [Email reporting]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) to learn how you can access the results of your email campaigns.

[3]: {% image_buster /assets/img_archive/choose_email_creation.png %}
[5]: {% image_buster /assets/img_archive/targetsegment_email_new.png %}
[6]: {% image_buster /assets/img_archive/confirm_email.png %}
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[13]: {{site.baseurl}}/user_guide/intelligence/intelligent_selection/
[14]: {% image_buster /assets/img/email.png %}
[15]: {% image_buster /assets/img_archive/newEmailTest.png %}
[16]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size
[18]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/
[19]: {% image_buster /assets/img_archive/new_campaign_email.png %}
[20]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/
[21]: {{site.baseurl}}/user_guide/intelligence/intelligent_timing/
[22]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/
