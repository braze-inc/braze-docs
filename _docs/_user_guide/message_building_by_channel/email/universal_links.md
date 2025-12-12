---
nav_title: Universal links and app links
article_title: Universal Links and App Links
page_order: 6.4
page_type: reference
description: "This help article walks you through how to set up Apple universal links and Android App Links."
channel: email
---

# Universal links and App Links

Apple universal links and Android App Links are mechanisms devised to provide a seamless transition between web content and mobile apps. While universal links are specific to iOS, Android App Links serve the same purpose for Android applications.

## How universal links and App Links work

Universal links (iOS) and App Links (Android) are standard web links (`http://mydomain.com`) that point to both a web page and a piece of content inside an app.

When a universal link or App Link is opened, the operating system checks to see if any installed app is registered for that domain. If an app is found, it's launched immediately without ever loading the web page. If no app is found, the web URL is loaded in the user's default web browser, which could also be configured to redirect to the App Store or Google Play Store respectively.

Plainly, universal links allow a website to associate its web pages with specific app screens, so when a user clicks a link to a web page that corresponds to an app screen, the app can be opened directly (if the app is currently installed).

This table outlines the key differences between universal links and traditional deep links:

|                        | Universal Links and App Links                                  | Deep Links                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| Platform Compatibility | iOS (version 9 and later) and Android (version 6.0 and later)  | Used in various mobile OS    |
| Purpose                | Seamlessly link web and app content on iOS and Android devices | Link to specific app content |
| Function               | Directs to web pages or app content based on context           | Opens specific app screens   |
| App Installation       | Opens app if the app is installed, otherwise opens web content | Requires app to be installed |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Use cases

Universal links and App Links are most commonly used for email campaigns, as emails can be opened and clicked from both desktop and mobile devices.

Some channels don't work well with these links. For example, push notifications, in-app messages, and Content Cards should use scheme-based deep links (`mydomain://`).

{% alert note %}
Android App Links require a custom `IBrazeDeeplinkHandler` with logic to handle links from their domains separately from other web URLs. It may be easier to use deep links instead and to keep linking practices uniform for channels other than email.
{% endalert %}

## Prerequisites

To use universal links and App Links:

- Your website must be accessible via HTTPS
- Your app must be available in the App Store (iOS) or Google Play Store (Android)

## Setting up universal links and App Links

For apps to support universal links or App Links, both iOS and Android require a special permissions file to be hosted at the link domain. This file contains definitions of which apps are able to open links from that domain and, for iOS, which paths these apps are allowed to open:

- **iOS:** Apple App Site Association (AASA) file
- **Android:** Digital Asset Links file

In addition to this permissions file, there are hard-coded definitions of which link domains the app is allowed to open that are set up within the app:

- **iOS:** Set as “Associated Domains” in Xcode
- **Android:** Defined in the app’s `AndroidManifest.xml` file

This two-part domain-app association is required for a universal link or App Link to work and prevents any app from hijacking links from a particular domain or any domain from opening a particular app.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

These steps are adapted from the Apple developer documentation. For more information, refer to [Allowing apps and websites to link to your content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc).

### Step 1: Configure your app entitlements

{% alert note %}
[In Xcode 13 and later](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/), Xcode can handle entitlement provisioning for you automatically. You can likely skip to [step&nbsp;1c](#step-1c) and refer back to these instructions if you have issues.
{% endalert %}

#### Step 1a: Register your app {#step-1a}

1. Go do developer.apple.com and log in.
2. Click **Certificates, Identifiers & Profiles**.
3. Click **Identifiers**.
4. If you don't have a registered App Identifier yet, click + to create one.
   a. Enter a **Name**. This can be anything you want.
   b. Enter the **Bundle ID**. You can find your bundle ID from the **General** tab of your Xcode project for the proper build target.

#### Step 1b: Turn on Associated Domains in your app identifier

1. In your existing or newly created App Identifier, locate the **App Services** section.
2. Select **Associated Domains**.
3. Click **Save**.

![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### Step 1c: Turn on Associated Domains in your Xcode project {#step-1c}

Before you proceed, make sure that your Xcode project has the same team selected as where you just registered your App Identifier. 

1. In Xcode, go to the **Capabilities** tab of your project file.
2. Turn on **Associated Domains**.

##### Troubleshooting tip

If you see the error "An App ID with Identifier 'your-app-id' is not available. Please enter a different string", do the following:

1. Check that you have the correct team selected.
2. Check that your Bundle ID ([step 1a](#step-1a)) of your Xcode project matches the one used to register the App Identifier.

#### Step 1d: Add the domain entitlement

In the domains section, add the appropriate domain tag. You must prefix it with `applinks:`. In this case, you can see we added `applinks:yourdomain.com`.

![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### Step 1e: Confirm that the entitlements file is included at build

In the project browser, make sure that your new entitlements file is selected under **Target Membership**.

Xcode should handle this automatically.

### Step 2: Configure your website to host the AASA file

To associate your website domain with your native app on iOS, you need to host the Apple App Site Association (AASA) file on your website. This file serves as a secure way to verify domain ownership to iOS. Prior to iOS 9, developers could register any URI scheme to open their apps, without any verification. However, with AASA, this process has become much more secure and reliable.

The AASA file contains a JSON object with a list of apps and the URL paths on the domain that should be included or excluded as universal links. Here is a sample AASA file:

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": “JHGFJHHYX.com.facebook.ios",
        "paths": [
          "*"
        ]
      }
    ]
  }
}
```

- `appID`: Built by combining your app’s **Team ID** (go to `https://developer.apple.com/account/#/membership/` to get the team ID) and the **Bundle Identifier**. In the example above, "JHGFJHHYX" is the team ID, and "com.facebook.ios" is the bundle ID.
- `paths`: Array of strings that specify which paths are included or excluded from association. You can use `NOT` before the path to disable paths. In this example, all the links on this path will go to the web instead of opening the app. You can use `*` as a wildcard to enable all paths in a directory and `?` to match a single character (such as /archives/201?/ to match all numbers from 2010–2019).

{% alert note %}
These strings are case-sensitive and query strings and fragment identifiers are ignored.
{% endalert %}

### Step 3: Host the AASA file on your domain

When you are ready with your AASA file, you can now host it on your domain either at `https://<<yourdomain>>/apple-app-site-association` or at `https://<<yourdomain>>/.well-known/apple-app-site-association`.

Upload the `apple-app-site-association` file to your HTTPS web server. You can place the file at the root of your server or in the `.well-known` subdirectory. Don’t append `.json` to the filename.

{% alert important %}
iOS will only attempt to fetch the AASA file over a secure connection (HTTPS).
{% endalert %}

While hosting the AASA file, make sure that the file follows these guidelines:

- Is served over HTTPS.
- Uses `application/json` MIME type.
- Does not exceed 128 KB (requirement in iOS 9.3.1 onwards)

### Step 4: Prepare your app to handle universal links

When a user taps a universal link on an iOS device, the device launches the app and sends it an [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) object. The app can then query the NSUserActivity object to determine how it was launched.

To support universal links in your app, take the following steps:

1. Add an entitlement that specifies the domains your app supports.
2. Update your app delegate to respond appropriately when it receives the NSUserActivity object.

In Xcode, open the **Associated Domains** section in the **Capabilities** tab and add an entry for each domain that your app supports, prefixed with `applinks:`. For example, `applinks:www.mywebsite.com`.

{% alert note %}
Apple recommends limiting this list to no more than 20 to 30 domains.
{% endalert %}

### Step 5: Test your universal link

Add the universal link to an email and send it to a testing device. Pasting a universal link directly into the Safari URL field won't cause the app to open automatically. If you do this, you will have to manually pull the website down so that a prompt will appear at the top asking you to open the respective app.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

These steps are adapted from the Android developer documentation. For more information, refer to [Add Android App Links](https://developer.android.com/training/app-links#add-app-links) and [Create Deep Links to App Content](https://developer.android.com/training/app-links/deep-linking).

{% alert note %}
Android App Links require a custom `IBrazeDeeplinkHandler` with logic to handle links from their domains separately from other web URLs. It may be easier to use deep links instead and to keep linking practices uniform for channels other than email.
{% endalert %}

### Step 1: Create deep links

First, you need to create deep links for your Android app. This can be done by adding [intent filters](https://developer.android.com/guide/components/intents-filters) in your `AndroidManifest.xml` file. The intent filter should include the `VIEW` action and `BROWSABLE` category, along with your website's URL in the data element.

### Step 2: Associate your app with your website

You need to associate your app with your website. This can be done by creating a Digital Asset Links file. This file should be in JSON format and it includes details about the Android apps that can open links to your website. It should be placed in the `.well-known` directory of your website.

### Step 3: Update your app manifest file

In your `AndroidManifest.xml` file, add a meta-data element inside the application element. The meta-data element should have an `android:name` attribute of "asset_statements" and an `android:resource` attribute that points to a resource file with a string array that includes your website's URL.

### Step 4: Prepare your app to handle deep links

In your Android app, you need to handle the incoming deep links. You can do this by getting the intent that started your activity and extracting the data from it.

### Step 5: Testing your deep links

Finally, you can test your deep links. Sending yourself a link through a messaging app or email and click on it. If everything is set up correctly, it should open your app.

{% endtab %}
{% endtabs %}

## Universal links, App Links, and click-tracking

{% alert note %}
Click-tracking links are typically set up as part of your onboarding for email. If this was not completed during customer onboarding, contact your account manager for help.
{% endalert %}

Our email sending partners, SendGrid and SparkPost, use click-tracking domains to wrap all links and include URL parameters for click-tracking in Braze emails.

For example, a link like `https://www.example.com` becomes something like `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`.

To allow email links with click-tracking to function as universal links or App Links, you'll need to perform some additional setup. Make sure to add the click-tracking domain (`links.email.example.com`) as a domain that the app is allowed to open. Furthermore, the click-tracking domain should serve the AASA (iOS) or Digital Asset Links (Android) files. This will help ensure that email links with click-tracking work seamlessly.

If you don't want every click-tracking link to be a universal link or App Link, you can specify which links should be universal links based on the email sending partner. Refer to the following sections for details.

### SendGrid

To treat a SendGrid click-tracking link as a universal link:

1. Set up your AASA or AndroidManifest pathPrefix values to only treat links with `/uni/` in the URL path as universal links.
2. Add the attribute `universal="true"` to your link's anchor tag (`<a>`). This changes the URL path of the wrapped link to include `/uni/`.

{% alert note %}
For AMP emails, this attribute should be data-universal="true".
{% endalert %}

For example:

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3. Make sure your app is set up to handle the wrapped links properly. Refer to SendGrid's article on [Resolving SendGrid Click Tracking Links](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) and follow the steps for your operating system. This article contains example code for [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) and [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android).

With this configuration, links with `/uni/` in the URL path will function as universal links, while all other links will work as web links.

### SparkPost

To treat a SparkPost click-tracking link as a universal link, add the following attribute to the Attributes section of the drag-and-drop editor for email, or manually edit the link HTML to include the following attribute in your link's anchor tag: `data-msys-sublink="custom_path"`.

This custom path allows you to selectively treat URLs with that value as a universal link.

For example:

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

Then, make sure your app is set up to handle the custom path properly. Refer to SparkPost's article on [Using SparkPost click tracking on deep links](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links). This article contains example code for [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) and [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost).

### Turning off click-tracking on a link-to-link basis

You can turn off click tracking for specific links by adding HTML code to your email message for the HTML editor or to an HTML block for the drag-and-drop editor.

#### SendGrid

If your email service provider is SendGrid, use the HTML code `clicktracking=off` like this:

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost 

If your email service provider is SparkPost, use the HTML code `data-msys-clicktrack="0"` like this:

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

If your email service provider is Amazon SES, use the HTML code `ses:no-track` like this:

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### Drag-and-drop editor

When using the drag-and-drop email editor, enter your HTML code as a custom attribute if your link is attached to text, a button, or an image.

##### Custom attribute for a text link

#### SendGrid

Select the following for the custom attribute:

- **Name:** `clicktracking`
- **Value:** `off`

#### SparkPost

Select the following for the custom attribute:

- **Name:** `data-msys-clicktrack`
- **Value:** `0`

![A custom attribute for a text link.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### Custom attribute for a button or image

#### SendGrid

Select the following for the custom attribute:

- **Name:** `clicktracking`
- **Value:** `off`
- **Type:** Link

#### SparkPost

Select the following for the custom attribute:

- **Name:** `data-msys-clicktrack`
- **Value:** `0`
- **Type:** Link

![A custom attribute for a button.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### Troubleshooting universal links with click-tracking

If your universal links aren't working as expected in your emails, such as navigating the recipient from their email app to the web browser before finally redirecting to the app, refer to these tips to troubleshoot your universal link setup.

#### Verify link file location

Make sure the AASA file (iOS) or Digital Asset Links file (Android) is located in the correct place:

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

It's important to ensure that these files are always publicly accessible. If you can't access them, you may have missed a step in setting up universal links for email.

#### Verify domain definitions

Make sure you have the correct definitions for domains your app is allowed to open.

- **iOS:** Review the Associated Domains set up in Xcode for your app ([step 1c]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c)). Check that the click-tracking domain is included in that list.
- **Android:** Open the app info page (long press the app icon and click ⓘ). Within the app info menu, locate **Open by default** and tap that. This should show a screen with all verified links the app is allowed to open. Check that the click-tracking domain is included in that list.

