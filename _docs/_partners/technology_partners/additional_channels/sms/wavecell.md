---
nav_title: Wavecell
alias: /partners/wavecell/
---

# Wavecell
With Wavecell's cloud communication platform, businesses and developers alike can incorporate SMS functionality into their user engagement strategies. Utilizing SMS and Wavecell, not only is two factor authentication feasible, but with the help of [Key-Value Pairs]({{ site.baseurl }}/user_guide/personalization_and_dynamic_content/key_value_pairs/) and [Webhooks]({{ site.baseurl }}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/), so are interactive stories and endless possibilities.

# Pre-Requisites

Requirement   |Source| Notes
--------------|------|-------------
Wavecell API Key | [Wavecell Configuration](https://app.wavecell.com) | An initial key is automatically generated on signup.
Wavecell Sub-Account ID | [Wavcell Configuration](https://app.wavecell.com) | Required for setting up the webhook URL (see below).

# Webhook Integration
## Creating a Webhook
Assuming you have successfully logged into Wavecell's [Consumer Portal](https://app.wavecell.com), navigate to **Configuration** then **API Keys** as shown below.

![Wavecell Customer API View]({% image_buster /assets/img_archive/wavecell_customer_apiview.png %}){: height="80%" width="80%"}

An API key named *apiKey 1* where the actual key is under *Key* is generated on signup and can be copied by clicking the blue double document icon.
The Sub-Account ID(s) is also visible inside the API Keys page, and can be copied as well by clicking on the desired ID when needed.
After retrieving the Sub-Account ID and API key from Wavecell, navigate to your Braze account, and under **Engagement** click **Templates & Media** and select the **Webhook Templates** tab to create a new webhook template.

![Braze Template View]({% image_buster /assets/img_archive/braze_template_view.png %})

From there, select **Blank Template** to set up a new webhook.

![Braze Blank Template]({% image_buster /assets/img_archive/braze_blank_template.png %}){: height="60%" width="60%"}

Add ``https://api.wavecell.com/sms/v1/{subAccountId}/single`` under​ **WEBHOOK URL**​,​ where
``subAccountID`` is the Sub-Account ID from your API Keys page under Wavecell's Customer Portal.
``REQUEST BODY``​ should be the default option which is  ``JSON Key/Value Pairs​``.
Now add three new pairs in any order named **source**, **destination** and **text**. Source should be the sender ID which is the name or number you will see when you receive an SMS, destination is the mobile number in international format where you are sending the SMS and text is the body message of your SMS.
After it's successfully setup, it should look similar to the image below:

![Braze Webhook Configuration]({% image_buster /assets/img_archive/braze_webhook_config.png %}){: height="60%" width="60%"}

Now, from the​ **Settings**​ tab, add two new request headers named **Authorization**​, which has the value ```Bearer {{your_api_key}}``` and **Content-Type** which has the value ``application/json``.

![Braze Webhook Headers]({% image_buster /assets/img_archive/braze_webhook_headers.png %}){: height="80%" width="80%"}

Finally, to perform a test on the webhook, navigate to the ​**Test​** tab and click on the **Send Test** button. If everything is setup properly, a successful webhook response (200) message should appear as shown below.

![Braze Webhook Test]({% image_buster /assets/img_archive/braze_webhook_test.png %}){: height="75%" width="75%"}

After a successful test, click the **Save Template** button and your webhook will be established for future use within your app.

## Creating a Braze App

From your Braze account, go to **App Settings** and select **Manage App Group**.

Once inside, create an app by providing a name under **App Name** and clicking the **Add App** button. For
this example we will use WEB as the app type.

![Braze Create App]({% image_buster /assets/img_archive/braze_create_app.png %})

After creating your app, an API Key generated for you will be visible under your app settings.
(Below, it is listed under *Settings for MyApp*.)

![Braze App Settings]({% image_buster /assets/img_archive/braze_app_settings.png %}){: height="80%" width="80%"}

## Testing the App
To test your app, a custom event can be created by going to **Manage App Group**, then **Custom Events**. Click **Add Custom Events** and type *test event* or something similar to name the event and save.

![Braze Custom Event]({% image_buster /assets/img_archive/braze_custom_event.png %})

Copy and paste the following source code into an empty HTML file and save the file. (example: ``demo.html``).
{% alert important %}
Replace ``YOUR-API-KEY-HERE`` in ``appboy.initialize()`` on line 6 within the source code with the API Key generated for you before saving!
{% endalert %}
{% raw %}
```html
<html>
    <​head​​>
    <script type="text/javascript">
        +function(a,p,P,b,y){appboy={};appboyQueue=[];for(var s="initialize destroy getDeviceId toggleAppboyLogging setLogger openSession changeUser requestImmediateDataFlush requestFeedRefresh subscribeToFeedUpdates requestContentCardsRefresh subscribeToContentCardsUpdates logCardImpressions logCardClick logCardDismissal logFeedDisplayed logContentCardsDisplayed logInAppMessageImpression logInAppMessageClick logInAppMessageButtonClick logInAppMessageHtmlClick subscribeToInAppMessage subscribeToNewInAppMessages removeSubscription removeAllSubscriptions logCustomEvent logPurchase isPushSupported isPushBlocked isPushGranted isPushPermissionGranted registerAppboyPushMessages unregisterAppboyPushMessages submitFeedback trackLocation stopWebTracking resumeWebTracking wipeData ab ab.DeviceProperties ab.User ab.User.Genders ab.User.NotificationSubscriptionTypes ab.User.prototype.getUserId ab.User.prototype.setFirstName ab.User.prototype.setLastName ab.User.prototype.setEmail ab.User.prototype.setGender ab.User.prototype.setDateOfBirth ab.User.prototype.setCountry ab.User.prototype.setHomeCity ab.User.prototype.setLanguage ab.User.prototype.setEmailNotificationSubscriptionType ab.User.prototype.setPushNotificationSubscriptionType ab.User.prototype.setPhoneNumber ab.User.prototype.setAvatarImageUrl ab.User.prototype.setLastKnownLocation ab.User.prototype.setUserAttribute ab.User.prototype.setCustomUserAttribute ab.User.prototype.addToCustomAttributeArray ab.User.prototype.removeFromCustomAttributeArray ab.User.prototype.incrementCustomUserAttribute ab.User.prototype.addAlias ab.User.prototype.setCustomLocationAttribute ab.InAppMessage ab.InAppMessage.SlideFrom ab.InAppMessage.ClickAction ab.InAppMessage.DismissType ab.InAppMessage.OpenTarget ab.InAppMessage.ImageStyle ab.InAppMessage.TextAlignment ab.InAppMessage.Orientation ab.InAppMessage.CropType ab.InAppMessage.prototype.subscribeToClickedEvent ab.InAppMessage.prototype.subscribeToDismissedEvent ab.InAppMessage.prototype.removeSubscription ab.InAppMessage.prototype.removeAllSubscriptions ab.InAppMessage.Button ab.InAppMessage.Button.prototype.subscribeToClickedEvent ab.InAppMessage.Button.prototype.removeSubscription ab.InAppMessage.Button.prototype.removeAllSubscriptions ab.SlideUpMessage ab.ModalMessage ab.FullScreenMessage ab.HtmlMessage ab.ControlMessage ab.Feed ab.Feed.prototype.getUnreadCardCount ab.ContentCards ab.ContentCards.prototype.getUnviewedCardCount ab.Card ab.ClassicCard ab.CaptionedImage ab.Banner ab.ControlCard ab.WindowUtils display display.automaticallyShowNewInAppMessages display.showInAppMessage display.showFeed display.destroyFeed display.toggleFeed display.showContentCards display.hideContentCards display.toggleContentCards sharedLib".split(" "),i=0;i<s.length;i++){for(var m=s[i],k=appboy,l=m.split("."),j=0;j<l.length-1;j++)k=k[l[j]];k[l[j]]=(new Function("return function "+m.replace(/\./g,"_")+"(){appboyQueue.push(arguments); return true}"))()}appboy.getUser=function(){return new appboy.ab.User};appboy.getCachedFeed=function(){return new appboy.ab.Feed};appboy.getCachedContentCards=function(){return new appboy.ab.ContentCards};(y=p.createElement(P)).type='text/javascript';y.src='https://js.appboycdn.com/web-sdk/2.2/appboy.min.js';y.async=1;(b=p.getElementsByTagName(P)[0]).parentNode.insertBefore(y,b)}(window,document,'script');

        appboy.initialize('YOUR-API-KEY-HERE');
        appboy.display.automaticallyShowNewInAppMessages();

        appboy.openSession();
    </script>
    </head​​>
    <​body​​>
        <div​​>
            <h1> Braze test​ </h1​​>
            <button​​ ​ type​ = ​ "button"​ ​ id​ = ​ "myBtn"​ > ​ Click me!​ </button​​>
        </div​​>
        <div​​>
            ​<p​ id​ = ​ "demo"​><​/p>
        <​/div​​>
    <​/body>
    <footer>
        <script​​>
            document.getElementById("myBtn").addEventListener("click", function(){
            appboy.changeUser("wvc_1");
            window.appboy.logCustomEvent("test event");
            });
        </script>
    <​/footer>
</html>
```
{% endraw %}
Now an event, with the name specified previously, will be triggered every time the button is clicked.
### Triggering a Message via App
You can trigger a message by creating a new campaign. Navigate to **Campaigns**, then **Create Campaign** and choose
**Webhook** from the dropdown.

![Braze Webhook Campaign]({% image_buster /assets/img_archive/braze_campaign_webhook.png %}){: height="80%" width="80%"}

Enter a **Campaign Name** and then select the **webhook template** you created and click **Forward**.
Now under **Delivery**, select **Action-Based Delivery** then select the **Perform Custom Event** trigger action and click **Add Trigger**.

{% alert important %}
The Forward link is located on the bottom-right of the application just beside “Save as Draft” button.
{% endalert %}

![Braze Campaign Trigger]({% image_buster /assets/img_archive/braze_campaign_trigger.png %}){: height="80%" width="80%"}

Next, select the custom event you created previously. In this case it's ```test event```.

![Braze Campaign Select Trigger Event]({% image_buster /assets/img_archive/braze_campaign_trigger_selected.png %}){: height="80%" width="80%"}

Click **Forward** again to choose the target users under your app under **Add Segment**.

![Braze Campaign Target]({% image_buster /assets/img_archive/braze_campaign_target.png %}){: height="80%" width="80%"}

Click **Forward** again and this time assign a **conversion event**.

![Braze Campaign Conversion Event]({% image_buster /assets/img_archive/braze_campaign_conversion_event.png %}){: height="80%" width="80%"}

Under **Choose Conversion Event Type**, select **Performs Custom Event**, then select **test event** (or the custom event name) under **Choose A Custom Event**.

![Braze Campaign Conversion Type]({% image_buster /assets/img_archive/braze_campaign_conversion_type.png %}){: height="80%" width="80%"}

Once completed, click **Forward** once more. If everything has been setup and looks proper, click **Launch Campaign**.
Now, you can open the previously created HTML file in a web browser. After clicking on the **Click me** button, you should receive an SMS with the message “hello world” (or any text specified).
