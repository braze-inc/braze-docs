---
nav_title: Survicate
article_title: Survicate
description: "This reference article outlines the partnership between Braze and Survicate, a customer feedback platform that helps you collect, analyze, and act on customer insights across multiple channels and throughout the user journey."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

> [Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter) is a customer feedback platform that collects, analyzes, and acts on customer insights across multiple channels and throughout the user journey. [Watch a quick demo](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)

_This integration is maintained by Survicate._

## About the integration

Use the Survicate and Braze native integration to sync email, in-app, mobile, or web survey responses with Braze customer profiles. Survey responses sync automatically with Braze user profiles as custom attributes or events. Real-time feedback insights make it easy to track and analyze feedback alongside customer data and create target follow-ups and hyper-personalized segments. 

## Use cases

Braze and Survicate work together to cover a range of feedback use cases, helping you collect actionable user insights and improve the customer experience:

- Improve survey response rates with embedded surveys that can be answered from an email inbox. 
- Gather insights at critical stages of the customer journey via Braze In-App Message. 
- Use feedback stored in Survicate to create smarter segments in Braze. 
- Automate follow-up campaigns based on customer feedback. 
- Use customer insights to trigger personalized workflows. 
- Reach a wider audience with automatically translated surveys.
- Send events to Braze contact profiles when someone responds to your survey

## Prerequisites

| Requirement | Description |
| ----------- | ----------- |
| Survicate account | You need a Survicate account to activate this integration. |
| Braze REST API key | A Braze REST API key with the permission `users.track`. <br><br> This can be created in the Braze dashboard from **Settings** > **APIs and Identifiers**. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Your endpoint will depend on the Braze URL for your instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Key features of the integration

The Survicate and Braze integration offers real-time data syncing, so the most up-to-date information from Survicate surveys is immediately available in Braze. Based on survey responses, you can use this data to take timely, personalized actions.

- **Send survey responses to Braze as custom user attributes**: Enrich Braze user profiles with data from survey responses.
- **Trigger custom events in Braze**: Use events based on survey answers to target specific groups or initiate follow-up campaigns.
- **Build detailed segments**: Create Braze segments using data from Survicate surveys to personalize your outreach further.

## Integration

### Creating your surveys in Survicate

#### Embed your survey in an email or create a shareable link survey 

1.  In Survicate, click **+ Create new survey**, select any creation method (a template, using AI survey creation, or adding your own questions), and the Email or Shareable link survey type:
![Braze is selected in survey creator.]({% image_buster /assets/img/survicate/survicate_1.gif %})

{: start="2"}
2. In the Configure tab of the survey, select **Braze** as the tool to identify respondents with:
![Braze is selected in Configure tab of the survey.]({% image_buster /assets/img/survicate/survicate_2.png %})

{: start="3"}
3. After you set up your survey, go to the Share tab and decide how to send your email survey. There are two options: you can send your **survey as a link** or **embed the first question in the email** so that respondents start answering the survey right from the email.

{% details Survey link option %}

1. Grab a link to your survey from the Copy survey link button:

![Grab a link to your survey from the Copy survey link button.]({% image_buster /assets/img/survicate/survicate_3.png %})

{: start="2"}
2. Hide the survey link behind a CTA button or hyperlink in your Braze Email.

![Hide the survey link behind a CTA button or hyperlink in your Braze Email.]({% image_buster /assets/img/survicate/survicate_4.png %})

{% enddetails %}

{% details Email embed option %}

Display the first question directly in the email's body to start the survey from the email. Respondents are then redirected to a landing page to take the rest of the survey.

1. Click **Get email code** and then **Copy the HTML code**:

![Get email code]({% image_buster /assets/img/survicate/survicate_5.gif %})

{: start="2"}
2. Go to the Braze campaign you want to use for the survey, click **Edit email body**, and add an HTML block to your template:

![Get HTML block code]({% image_buster /assets/img/survicate/survicate_6.png %})

{: start="3"}
3. Replace the code with the one you copied from your Survicate survey. You then see the survey's first question in the template:

![Replace the code with the one you've copied from your Survicate survey]({% image_buster /assets/img/survicate/survicate_7.png %})

{: start="4"}
4. Schedule the email, choose your Target group, and your campaign is ready to send.

{% enddetails %}

### Braze In-App Message survey

1. Click **+ Create new survey**, select any creation method (a template, using AI survey creation, or adding your own questions), and then choose In-platform surveys and the Braze In-App Message survey type:

![Click on + Create new survey, select any creation method]({% image_buster /assets/img/survicate/survicate_8.gif %})

{: start="2"}
2. Launch your Braze In-App Message survey by navigating to your Braze account, then to **Messaging > Campaigns > Create campaign > In-app message**:
![Launch your Braze In-App Message survey]({% image_buster /assets/img/survicate/survicate_9.gif %})

### Launch your Braze In-App Messenger survey via the traditional editor

1. If you use the traditional editor, in the Message type, choose **Custom code**:

![choose Custom code]({% image_buster /assets/img/survicate/survicate_10.gif %})

{: start="2"}
2. Then paste the code from the Launch tab of your survey to the HTML field:

![paste the code from the Launch tab of your survey to the HTML field]({% image_buster /assets/img/survicate/survicate_11.gif %})

{% alert note %}
Braze displays in-app messages in an iframe by default while the app's background is blocked. To allow interaction with your app, while Survicate surveys appear, you must:<br><br>

- Add `opts.useBrazeIframeClipper = true` to your Survicate-Braze snippet.
- Install the `@survicate/braze-bridge-npm` [package](https://www.npmjs.com/package/@survicate/braze-bridge-npm) in the file where you initialize Braze and use the `initBrazeBridge` function.

You can find a sample snippet and React implementation [on Survicate's developers' site](https://developers.survicate.com/javascript/installation/#braze).
{% endalert %}

{: start="3"}
3. In your Braze campaign, set up the Target and Assign steps. When complete, your campaign is ready to launch. In the Review step, you can see how the campaign looks. The survey appears on your website in the place specified in the Survicate panel, as described above.

### Enabling the Braze integration

1. To enable the Braze integration, go to **Integrations**, and search for and select "Braze".

![Select Braze]({% image_buster /assets/img/survicate/survicate_12.gif %})

{: start="2"}
2. Click **Connect** to set up the authorization.

3. Insert your Braze account Workspace API Key and Braze Instance URL:

![Insert your Braze account Workspace API Key and Braze Instance URL]({% image_buster /assets/img/survicate/survicate_13.png %})

{% alert important %} 
To connect Survicate to Braze, the Braze API key needs to have `users.track` permissions.
{% endalert %}

### Connecting your surveys to Braze

Now that the Braze integration is connected, you can set up individual settings for each survey. Go to your survey, select the **Connect** tab, and choose **Braze** from the list of available integrations.

![Go to your survey, select the Connect tab, and choose Braze]({% image_buster /assets/img/survicate/survicate_14.png %})

### Sending responses to Braze as custom attributes

Set up survey responses to flow into Braze as custom attributes, which enriches your Braze user profiles with collected data.

1. In the Settings tab of Braze Integration, fine the **Update fields** section.

![Select Update fields section]({% image_buster /assets/img/survicate/survicate_15.png %})

{: start="2"}
2. Select the question you want to update the fields from. To avoid flooding your Braze user profiles with data, you can send responses to only chosen questions.

![Select the question you want to update the fields from]({% image_buster /assets/img/survicate/survicate_16.png %})

{% alert note %}
Ranking and Matrix questions are not supported with this Braze integration.
{% endalert %}

{: start="3"}
3. Add the name of the custom attribute you want to update under the **User** field:

![Add the name of the custom attribute you want to update under the User field]({% image_buster /assets/img/survicate/survicate_17.png %})

By default, Survicate sends the content of a survey response as an attribute value. You can change the label to make it shorter or fit your data structure by clicking **Edit mapping** to modify these values:

![Survey response as an attribute value]({% image_buster /assets/img/survicate/survicate_18.png %})

![Click edit mapping to modify these values]({% image_buster /assets/img/survicate/survicate_19.png %})

{% alert note %}
For NPS, Survicate sends mapped values based on the response group for the NPS® question. However, if you want to receive numeric values, you can switch on Send Answers as 0-10 values.
{% endalert %}

![Survicate sends values mapped based on the response group]({% image_buster /assets/img/survicate/survicate_20.png %})

{: start="4"}
4. Connect more questions to your integration by clicking **+ Add new** and applying the same steps.

![Connect more questions to your integration]({% image_buster /assets/img/survicate/survicate_21.png %})

### Sending events to Braze contacts' profiles

Apart from the previous settings, each time a respondent answers a survey question, Survicate can send a custom event in Braze named `survicate-question-answered`.
In the Survicate panel, under Send responses as custom attributes, you can choose if you want to send the event for all questions, questions chosen in the Update fields tab, or not at all:

![you can choose if you want to send the event for all questions]({% image_buster /assets/img/survicate/survicate_22.png %})

If you choose to send the events, you can see in the users' profiles how many times they responded to Survicate surveys and when they last responded:

![Responses ]({% image_buster /assets/img/survicate/survicate_23.png %})

The event contains event properties with the answer to the question and information about the survey, question, and respondent. You can use this event to create segments. For example, create a segment of users who responded to a survey after a particular date or a particular number of times:

![The event contains event properties with the answer]({% image_buster /assets/img/survicate/survicate_24.png %})

You can also use this data when creating a campaign in Braze.

![You can also use this data when creating a campaign in Braze]({% image_buster /assets/img/survicate/survicate_25.png %})

### Test the integration

When you have your survey ready and integration set up, you can test it without leaving Survicate by clicking the Test Integration button next to any attribute, tag, or new contact setup that you've created. Survicate creates a test contact (`braze-test@survicate.com`) in your Braze account. The contact's profile includes updated fields as per the setup.

![Click Test Integration button]({% image_buster /assets/img/survicate/survicate_26.png %})

In Braze, you see sample data from the mapped fields in the Survicate Dummy Contact:

![Sample data from the mapped fields in the Survicate Dummy Contact]({% image_buster /assets/img/survicate/survicate_27.png %})

### Analyzing your survey results

After collecting responses through your Braze survey, it's time to look into the feedback and insights your respondents have shared. Survicate allows you to easily review results, statistics, and trends to take further action.

### Feedback in Survicate

After your survey starts collecting responses, you see them immediately in the Analyze tab of the survey.

![Responses in Analyze tab]({% image_buster /assets/img/survicate/survicate_28.png %})

The Analyze tab shows you Overall results with statistics and over-time data, as well as individual responses to look into each survey submission in detail.

### Feedback in Braze

If you update user fields with survey responses or send responses as custom events, you can see the survey data synced in real time. In Braze, go to a specific contact who responded to your survey. You see both the response-based data and events in the contact's main view.

![survey data synced in real time]({% image_buster /assets/img/survicate/survicate_29.png %}) 