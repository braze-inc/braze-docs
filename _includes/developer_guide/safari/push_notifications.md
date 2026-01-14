{% multi_lang_include developer_guide/prerequisites/web.md %} You'll also need to [set up push notifications]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) for the Web SDK. Note that you can only send push notifications to iOS and iPadOS users that are using [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) or later.

## Setting up Safari push for mobile

### Step 1: Create a manifest file {#manifest}

A [Web Application Manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest) is a JSON file that controls how your website is presented when installed to a user's home screen.

For example, you can set the background theme color and icon that the [App Switcher](https://support.apple.com/en-us/HT202070) uses, whether it renders as full screen to resemble a native app, or whether the app should open in landscape or portrait mode.

Create a new `manifest.json` file in your website's root directory, with the following mandatory fields. 

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

The full list of supported fields can be found [here](https://developer.mozilla.org/en-US/docs/Web/Manifest).

### Step 2: Link the manifest file {#manifest-link}

Add the following `<link>` tag to your website's `<head>` element pointing to where your manifest file is hosted.

```html
<link rel="manifest" href="/manifest.json" />
```

### Step 3: Add a service worker {#service-worker}

Your website must have a service worker file that imports the Braze service-worker library, as described in our [web push integration guide]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-1-configure-your-sites-service-worker).

### Step 4: Add to home screen {#add-to-homescreen}

Popular browsers (such as Safari, Chrome, FireFox, and Edge) all support web push notifications in their later versions. To request push permission on iOS or iPadOS, your website must be added to the user's home screen by selecting **Share To** > **Add to Home Screen**. [Add to Homescreen](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) lets users bookmark your website, adding your icon to their valuable home screen real estate.

![An iPhone showing options to bookmark a website and save to the home screen]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### Step 5: Show the native push prompt {#push-prompt}
After the app has been added to your home screen you can now request push permission when the user takes an action (such as clicking a button). This can be done using the [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) method, or with a [no-code push primer in-app message]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

{% alert note %}
After you accept or decline the prompt, you need to delete and reinstall the website to your home screen to be able to show the prompt again.
{% endalert %}

![A push prompt asking to "allow" or "don't allow" Notifications]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

For example:

```typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
};
```

## Next steps

Next, send yourself a [test message]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) to validate the integration. After your integration is complete, you can use our [no-code push primer messages]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) to optimize your push opt-in rates.
