Before you can send an iOS push notification using Braze, you must provide your `.p8`  push notification file provided by Apple. As described on the Apple [developer documentation](https://developer.apple.com/documentation/usernotifications):

1. In your Apple developer account, go to [**Certificates, Identifiers & Profiles**](https://developer.apple.com/account/ios/certificate).
2. Under **Keys**, select **All** and click the add button (+) in the upper-right corner.
3. Under **Key Description**, enter a unique name for the signing key.
4. Under **Key Services**, select the **Apple Push Notification service (APNs)** checkbox, then click **Continue**. Click **Confirm**.
5. Note the key ID. Click **Download** to generate and download the key. Make sure to save the downloaded file in a secure place, as you cannot download this more than once.
6. In Braze, go to **Settings** > **App Settings** and upload the `.p8` file under **Apple Push Certificate**. You can upload either your development or production push certificate. To test push notifications after your app is live in the App Store, its recommended to set up a separate workspace for the development version of your app.
7. When prompted, enter your app's [bundle ID](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier), [key ID](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/), and [team ID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id), then click **Save**.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can upload your `.p8` file from **Manage Settings** > **Settings**.
{% endalert %}

{% alert important %}
For step 7, you must indicate whether to send notifications to the production or development (sandbox) environment. The app’s environment is defined by its provisioning profile.
{% endalert %}