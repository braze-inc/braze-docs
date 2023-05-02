Audience Sync to LinkedIn
Using the Braze Audience Sync to LinkedIn, brands can elect to add user data from their own Braze integration to LinkedIn customer lists to deliver advertisements based upon behavioral triggers, segmentation and more. Any criteria you’d normally use to trigger a message (Push, Email, SMS, Webhook, etc) in a Braze Canvas based upon your user data can now be used to trigger an ad to that user in your LinkedIn customer lists.

Common use cases for audience syncing include:

Targeting high value users via multiple channels to drive purchases or engagement
Retargeting users who are less responsive to other marketing channels
Creating suppression audiences to prevent users from receiving advertisements when they’re already loyal consumers of your brand

This feature gives brands the option to control what specific first-party data is shared with LinkedIn. At Braze, the integrations you can and cannot share your first-party data with are given the utmost consideration. For more information, refer to our privacy policy.

Important:
Audience Sync to LinkedIn is currently in beta. Contact your Braze account manager if you’re interested in participating in the beta
Integration requirements 
You will need to ensure that you have the following items created and/or completed prior to setting up your Audience Sync to LinkedIn.

Requirement
Origin
Description
LinkedIn ad account
LinkedIn
An active LinkedIn ad account tied to your brand.

Please ensure that you have accepted any relevant LinkedIn terms and conditions to access and use that account and that your LinkedIn admin has granted you the appropriate permissions to manage Audiences.
TOS 
LinkedIn



Integration 
Step 1: Connect to LinkedIn
In the Braze dashboard, go to Technology Partners and select LinkedIn. In the LinkedIn Audience Export module, click Connect LinkedIn.


You’ll then be redirected to the LinkedIn OAuth page to authorize Braze for the permissions related to your Audience Sync integration.

Once you have selected confirm, you’ll then be redirected back into Braze to select which LinkedIn ad accounts you wish to sync to. 


Once you have successfully connected, you will be taken back to the partner page, where you can view which accounts are connected and disconnect existing accounts.



Your LinkedIn connection will be applied at the Braze app group level. If your LinkedIn admin removes you from your LinkedIn ad account, Braze will detect an invalid token. As a result, your active Canvases using LinkedIn will show errors, and Braze will not be able to sync users.

Step 2: Configure your Canvas entry criteria
When building audiences for Ad Tracking, you may wish to include or exclude certain users based on their preferences, and in order to comply with privacy laws, such as the “Do Not Sell or Share” right under the CCPA . Marketers should implement the relevant filters for users’ eligibility within their Canvas entry criteria. Below we list some options.
If you have collected the iOS IDFA through the Braze SDK, you will be able to use the Ads Tracking Enabled filter. Select the value as true to only send users into Audience Sync destinations where they have opted in.

If you are collecting ‘opt-ins’, ‘opt-outs’, ‘Do Not Sell Or Share’ or any other relevant custom attributes, you should include these within your Canvas entry criteria as a filter:

To learn more on how to comply with these Data Protection laws within the Braze platform, please see Data Protection Technical Assistance.
Step 3: Add an Audience Sync Step with LinkedIn
Add a component in your Canvas and select Audience Sync.

Step 4: Sync setup
Click on the Custom Audience button to open the component editor.

Select LinkedIn as the desired Audience Sync partner. 



Then select your desired LinkedIn ad account. Under the Choose a New or Existing Audience dropdown, type in the name of a new or existing audience.

Create a New Audience
Enter a name for the new audience, select Add Users to Audience and select which fields you would like to sync with LinkedIn. For this integration we currently support: 
Email
First and Last name
Android GAID

Next, save your audience by clicking the Create Audience button at the bottom of the step editor.


Users will be notified at the top of the step editor if the audience is created successfully or if errors arise during this process. Users can also reference this audience for user removal later in the Canvas journey because the audience was created in draft mode.


When you launch a Canvas with a new audience, Braze sync users in near real-time as they enter the Audience Sync component.
Sync with an Existing Audience
Braze also offers the ability to either add users to existing LinkedIn audiences to ensure that these audiences are up-to-date. To sync with an existing audience, type the existing audience name in the dropdown and Add to the Audience. Braze will then either add users in near real-time as they enter the Audience Sync component.


Step 5: Launch Canvas
Once you have configured your Audience Sync to LinkedIn, simply launch the Canvas! The new audience will be created, and users who flow through the Audience Sync step will be passed into this audience on LinkedIn. If your Canvas contains subsequent components, your users will then advance to the next step in their user journey.

You can view the audience in LinkedIn by going into your ad account and then selecting Audiences under the Assets section of the navigation. From the Audiences page, you can see the size of each audience after it reaches more than 300 members.


User syncing and rate limit considerations
As users reach the Audience Sync Step, Braze will sync these users in near real-time while also respecting LinkedIn’s API rate limits. What this means in practice is that Braze will try to batch and process as many users every 5 seconds before sending these users to LinkedIn.

LinkedIn’s API rate limit states no more than 10 queries per second and 100k users per request. If a Braze customer reaches this rate limit, Braze the Canvas will retry the sync for up to ~13 hours. If the sync is not possible, these users are listed under the Users Errored metric.
Understanding analytics
The following table includes metrics and descriptions to help you better understand analytics from your Audience Sync component.

| METRIC | DESCRIPTION |
| ------ | ----------- | 
| Entered | Number of users who entered this component to be synced to LinkedIn. |
| Proceeded to Next Step | How many users advanced to the next component if there is one. All users will auto-advance if this is the last step in the Canvas branch. |
| Users Synced | Number of users who have successfully been synced to LinkedIn. |
| Users Not Synced | Number of users that have not been synced due to missing fields to match. |
| Users Pending | Number of users currently being processed by Braze to sync into LinkedIn. |
| Users Errored | Number of users who were not synced to LinkedIn due to an API error after about 13 hours of retries. Potential causes of errors can include an invalid LinkedIn token or if the audience was deleted on LinkedIn. |
| Exited Canvas | Number of users who have exited the Canvas. This occurs when the last step in a Canvas is an Audience Sync component. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Remember that there will be a delay in reporting for users synced and users errored metrics due to the bulk flusher and the 13-hour retry, respectively.
{% endalert %}

## Troubleshooting

{% details How long will it take for the audience sizes to populate in LinkedIn? %}
There is up to a 48 hour delay to view the audiences within your LinkedIn account.
{% enddetails %}

{% details What is the minimum audience size for LinkedIn to populate within your ad account?  %}
The audience must include at least 300 members to populate the audience size within your LinkedIn account.
{% enddetails %}

{% details What should I do next if I receive an invalid token error? %}
You can simply disconnect and reconnect your LinkedIn account on the LinkedIn partner page. Ensure with your LinkedIn admin that you have the appropriate permissions to the ad account you wish to sync with.
{% enddetails %}

{% details Why is my Canvas not allowed to launch? %}
Please ensure that your LinkedIn ad account has successfully connected to Braze on the LinkedIn partner page.
Make sure you have selected an ad account, entered a name for the new audience, and selected fields to match.
{% enddetails %}

{% details How do I know if users have matched after passing users to LinkedIn? %}
LinkedIn does provide information around match rates within their dashboard. You can review within LinkedIn under the Audiences section.
{% enddetails %} 

{% details How many audiences can LinkedIn support? %}
At this time, there is no limit on the number of audiences in your LinkedIn ad account.
{% enddetails %}

{% details Why is a segment stuck in BUILDING status and not updated? %}
A segment is considered unused and set to ARCHIVED after it is not continuously used for 30 days in a draft or active campaign. Because of this, a segment may appear "stuck" in BUILDING when updates are streamed to an ARCHIVED segment, thus pushing it into the BUILDING state, and right before it is archived again, new updates are streamed to the unused segment.
{% enddetails %}



