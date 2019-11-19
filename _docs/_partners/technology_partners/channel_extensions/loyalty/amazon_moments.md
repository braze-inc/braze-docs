---
nav_title: Amazon Moments
alias: /partners/amazon_moments/
---

# Amazon Moments

[Amazon Moments](https://developer.amazon.com/moments) is a cross-platform marketing tool that allows you to deliver physical and digital items to your customers in over 100 countries. Moments lets you increase engagement by offering tailored rewards delivered by Amazon when customers reach actions that matter in your apps and websites.

When using Moments, apps across industries have seen improvements in engagement — in gaming, one developer increased their percentage of first time payers by 20x. A streaming video service offered $10 worth of physical rewards and doubled the likelihood of winning back a subscriber.

{% alert important %}
This partnership is in early access beta. All features may not perform as exactly described. Please reach out to your Braze Account Manager for more information.
{% endalert %}

## Prerequisites

{% raw %}
Requirement   |Origin| Description
--------------|------|-------------
Amazon Developer Account   |[Amazon Developer Console](https://developer.amazon.com/)| You will need to have an Amazon Developer Account that can be created at https://developer.amazon.com/.
Register a new app within Amazon Moments   |[Amazon Moments](https://developer.amazon.com/moments/console/register) | You will need to register a new app within your Amazon Moments Console: https://developer.amazon.com/moments/console/register.
Moments Campaign Information   | Amazon Moments Campaign | You will need to include the App ID, Moments ID, Campaign ID, Reward Group, and API key from your Amazon Moments campaign to template into your Connected Content call.
{% endraw %}

## Integration

### Amazon Moments Setup & Campaign Creation

#### Step 1: Register Your App

![amazon_moments1]({% image_buster /assets/img/amazon_moments1.png %})

![amazon_moments2]({% image_buster /assets/img/amazon_moments2.png %})


#### Step 2: Create an Amazon Moments Campaign

![amazon_moments3]({% image_buster /assets/img/amazon_moments3.png %})

![amazon_moments4]({% image_buster /assets/img/amazon_moments4.gif %})

When setting up your Amazon Moments campaign, you will need to enter the following required campaign details:

{% raw %}
Detail | Description
--------------|-------------
Select Your App | Choose the app that you want to create a campaign for.
Campaign Name | This is a unique name for your campaign.
Campaign Duration  | Choose the start and end date of your campaign.
Total budget | Enter the total budget you want to allocate to this campaign (minimum $50). Click [here](https://developer.amazon.com/docs/moments-ug/config-billing.html) for more information about the maximum spend allowed per month.
Cost per Action | Amount you will spend each time a customer completes an action and gets the reward link.
Targeted marketplace  | Pick the Amazon marketplaces that your reward will be fulfilled from.
Reward Selection | Choose the rewards you'd like to offer to your users. This rewards catalog is a curated list of popular items gifted on Amazon.
Input Announcement & Redemption Messages | **Announcement Message** will be shown to customers who meet your Announcement Criteria. **Redemption Message** will be shown to users who completed the action you specified above. **Redemption Landing Page and Email Image** (3000x600px) will be shown to users who visit the reward redemption landing page on Amazon.
{% endraw %}

Once you have submitted your campaign, you will be able to view your Moments Reward API Parameters on the campaign details page that you will need to incorporate into your Braze Connected Content call.

![amazon_moments5]({% image_buster /assets/img/amazon_moments5.png %})

{% alert important %}
You will need to ensure your Moments campaign is live before proceeding further. This takes 7 (seven) days.
{% endalert %}

### Using Amazon Moments in Your Braze Campaigns & Canvases

Through Braze’s [Connected Content]({{ site.baseurl }}/user_guide/personalization_and_dynamic_content/connected_content/), you will be able to make outbound API requests, at time of message send, to fetch data outside of Braze for further personalization. This can allow you to dynamically insert copy, images, urls, and more with data not actively stored in Braze’s user profiles.  

There are two Amazon Moments REST API Endpoints:

{% raw %}
Endpoint   |URL| Description
--------------|------|-------------
`getRewardInfo` | https://dnxr7vm27d.execute-api.us-east-1.amazonaws.com/prod/GetRewardInfo | Retrieves information about a reward to be displayed to the customer for promotional purposes. Making this request will not consume a reward.
`getReward` |https://dnxr7vm27d.execute-api.us-east-1.amazonaws.com/prod/GetReward | Gets a specific reward for the customer to redeem. Calling this endpoint will consume one reward from the inventory. Each reward can be  only one time.
Moments Campaign Information   | Amazon Moments Campaign | You will need to include the App ID, Moments ID, Campaign ID, Reward Group, and API key from your Amazon Moments campaign to template into your Connected Content call.
{% endraw %}

The two endpoints use the same request parameters. The following workflow map shows the high-level interactions and when to use each endpoint:

![amazon_moments6]({% image_buster /assets/img/amazon_moments6.png %})

- Use the Moments Console to register the app and configure the rewards. [See Configure Your App.](https://developer.amazon.com/docs/moments/configure-app.html)
- If the campaign is a challenge , call the [getRewardInfo endpoint](https://s3-us-west-1.amazonaws.com/devportal-reference-docs/moments/swagger-en/index.html#/endpoints/GetRewardInfo) to get the content to notify the users that you want to target for this campaign.
- Your rule engine must evaluate whether the user qualifies for the campaign. If a user qualifies, you can call the [getReward endpoint](https://s3-us-west-1.amazonaws.com/devportal-reference-docs/moments/swagger-en/index.html#/endpoints/GetReward) to consume a reward and send the reward URL to the user.

{% alert warning %}
If the reward doesn't exist, the request returns an empty list.
{% endalert %}

To publish an Amazon Reward through Braze’s connected content, add the following code snippet to your email template:

{% raw %}
```
{% connected_content INSERT_API_URL_HERE :headers {"accept": "application/json"} :method post :body appId=APPID&momentId:MOMENTID&deviceType=DEVICETYPE&campaignID=CAMPAIGNID&rewardGroupId=REWARDGROUPID :content_type application/json :save moments %}
```

You will need to include the App ID, Moments ID, Campaign ID, Reward Group, and API key from your Amazon Moments campaign to template into your Connected Content call.

The entire [response body](https://developer.amazon.com/docs/moments-ug/rewards-api-endpoints.html#/endpoints/GetRewardInfo) is now stored in the variable, “moments.” To parse through and template certain objects in that response body please use the following [dot notation syntax](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#json-parsing), where “VALUE” is the property you would like to template (e.g. `rewardImageUrl` or `remainingRewardCount`)
- You can template in the reward image URL as the rich image with my push notification, you could simply template `{{moment.rewardImageUrl}}` as the redirect URL. If you wanted to template in the number of rewards the user had left in the current month you could templates `{{moments.remainingRewardCount}}}` into the email subject line or message body.

{% endraw %}

![amazon_moments7]({% image_buster /assets/img/amazon_moments7.png %})

## Troubleshooting

#### Unsuccessful API Requests

If the Moments service cannot complete the API request successfully, the `rewardNotificationText` field contains a text message to explain the error. For more information see Error Messages [here](https://developer.amazon.com/docs/moments/rewards-api.html#error-messages).
