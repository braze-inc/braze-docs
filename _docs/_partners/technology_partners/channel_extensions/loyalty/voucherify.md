---
nav_title: Voucherify
alias: /partners/voucherify/
---

# Voucherify

[Voucherify](https://www.voucherify.io/) is an all-in-one promotional platform that allows for personalized campaigns and loyalty programs that drive user engagement and overall retention. Now, with the Braze and Voucherify integration, users can automatically send 1-to-1 coupons, discounts, and more, all through their Braze account while tracking redemptions and campaign growth at every step. Leverage the power of Voucherify and grow your mobile-first campaigns by sending vouchers through Braze's **connected content** or through Braze's **custom attributes.**


# Prerequisites
{% raw %}
Requirement   |Origin| Description
--------------|------|-------------
Braze API Key    |[Braze Settings](https://dashboard.braze.com/sign_in)| A REST API Key linked to your Braze account with the **users.track** permission enabled <br> (**only** needed to publish via custom attributes)
{% endraw %}

# Integration
## Publish Vouchers via Connected Content
To publish a voucher through Braze's connected content, add the following code snippet to your email template:
{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.voucherify.io/v1/vouchers/publish
     :method post
     :headers {
       "X-App-Id": "VOUCHERIFY-APP-ID",
       "X-App-Token": "VOUCHERIFY-APP-TOKEN"
 	}
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}
Where ```${user_id}``` is the **external_id** of the user in Braze and will be set as the **source_id** for the customer in Voucherify.

To display the voucher code, also add the following code snippet as needed within the email template:
```
{{publication.voucher.code}}
```

{% alert important %}
* Assigning the **campaign_name** variable is a workaround to pass campaign names which include spaces and can alternatively be replaced by passing a campaign id directly in the :body
* When testing email templates be aware of the Connected Content cache (at least 5 minutes). If you want each test preview to publish a new voucher, you can omit the cache by appending a query parameter to the URL, e.g. ```?t=1``` and increment the number with each test.
* **X-Voucherify-API-Version** is optional. However, if your project uses an API Version older than **v2017-04-20**, then you should use ```:save voucher``` instead of ```:save publication``` in your template and ``{{voucher.code}}`` instead of ``{{publication.voucher.code}}`` to display the code.
{% endalert %}
## Publish Vouchers via Custom Attributes
To begin publishing vouchers via Custom Attributes, navigate to the **Integration Directory** from you Voucherify dashboard.

![VOUCHERIFY INTEGRATION DIRECTORY]({% image_buster /assets/img/voucherify_integration_directory.png %})

After clicking the checkbox to enable the **Braze** integration, input the API KEY collected previously, with the **users.track** permission enabled, in the **App Group ID** field and click the connect button to establish a connection.

![VOUCHERIFY ESTABLISH CONNECTION]({% image_buster /assets/img/voucherify_establish_connection.png %})

After a connection has been established, navigate to **Distributions** from the left-hand menu and click the red **plus icon** to start a new Braze distribution from the dashboard.

![VOUCHERIFY NEW DISTRIBUTION]({% image_buster /assets/img/voucherify_new_distribution.png %})

### Setting Distribution Details
From the distribution manager, go through first 6 stages to set distribution details:
#### Step One: Setting the Distribution Mode
The first decision to be made is whether the Braze distribution should be set to **manual**, i.e if the message should be sent to the chosen customer/customers right after you confirm the distribution, or **automatic**, i.e if messages should be sent everytime a customer meets specific criteria defined in the Distribution Manager by using customer segments.

![VOUCHERIFY DISTRIBUTION MODE]({% image_buster /assets/img/voucherify_distribution_mode.png %})

#### Step Two: Distribution Purpose
Next, decide on the distribution's purpose and what type of message you would like to send. Voucherify supplies three options to choose from:
* A message that informs eligible customers about a cart-level promotion 
* A message with unique codes from a campaign
* A message without codes sent in your customized template

![VOUCHERIFY DISTRIBUTION PURPOSE]({% image_buster /assets/img/voucherify_distribution_purpose.png %})

#### Step Three: Choosing Your Audience
Now, determine your audience, or who will be receiving messages from this distribution. 

![VOUCHERIFY DISTRIBUTION AUDIENCE]({% image_buster /assets/img/voucherify_distribution_audience.png %})

If you chose an **automatic** distribution mode, you can choose your receivers by specifying [customer segments](https://support.voucherify.io/article/51-customer-segments), in which the app will push out a message every time a new customer meets a certain criteria and enters a chosen segment.

Alternatively, you can also choose your receivers based on **events performed by customers** such as and order being **created**, **updated**, **paid for**, or **cancelled**.

Optionally, there is also the **voucher has been published** event if you would like to trigger a distribution based on a voucher publication. With this event, when a voucher has been published to the customer (if you assign a code to a particular user), the app will automatically deliver it in a message defined in the distribution manager. In case of a manual message, you can choose a receiver from your list or create a distribution to customers from a particular segment. Likewise, the segment can be chosen from the existing ones or created from scratch.

If you chose a **manual** distribution mode, you must choose either a single customer or a segment of customers to which you would like to deliver a message.

#### Step Four: Message Title
After specifying your audience, add a subject line for your message/messages as shown below.

![VOUCHERIFY DISTRIBUTION TITLE]({% image_buster /assets/img/voucherify_distribution_title.png %})

#### Step Five: Setting the Distribution Channel
Fianlly, select **Braze** as the distribution channel, as shown below, and select a custom attribute name that will later be used for putting code in the Braze message.

![VOUCHERIFY DISTRIBUTION CHANNEL]({% image_buster /assets/img/voucherify_distribution_channel.png %})


Now, select **SEND** to test your distribution - as a result, you should see a user with a Voucherify code along with an assigned QR/barcode. 

![VOUCHERIFY TEST]({% image_buster /assets/img/voucherify_test.png %})

Voucherify users can also be found from within Braze by supplying the specified **UserID (source_id)**, found on the Voucherify user profile page, to Braze's user search tool.

### Testing Your Custom Attribute
In order to send an email in Braze with an embeded code, you must first create a campaign if you have not already done so. 

From your Braze Dashboard, navigate to **Campaign** and click **Create Campaign** and choose **email** from the drop down menu as shown below.

![VOUCHERIFY BRAZE CAMPAIGN]({% image_buster /assets/img/voucherify_braze_campaign.png %})

Afterwords, select **Blank Template** and navigate to **Edit Email Body** and switch to the **Body** tab.

Now, customize your template and add the `Custom Attributes` defined in the Voucherify distribution.

![VOUCHERIFY CUSTOM ATTRIBUTES]({% image_buster /assets/img/voucherify_custom_attributes.png %})

If the custom attributes were properly configured, you should now see the embeded code displayed in the message preview.

![VOUCHERIFY BRAZE CAMPAIGN PREVIEW]({% image_buster /assets/img/voucherify_braze_campaign_preview.png %})

Lastly, if everything is in order, confirm your template by selecting **DONE**, followed by **FORWARD** to finish editing your campaign.