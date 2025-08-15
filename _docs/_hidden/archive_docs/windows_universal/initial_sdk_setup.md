---
nav_title: Initial SDK setup
article_title: Initial SDK Setup for Windows Universal
platform: Windows Universal
page_order: 0
description: "This reference article covers the initial SDK integration steps to integrate the Braze SDK on your Windows Universal platform."
search_rank: 1
hidden: true
---

# Initial SDK integration
{% multi_lang_include archive/windows_deprecation.md %}

The Braze SDK will provide you with an API to report information to be used in analytics, segmentation, and engagement, as well as the ability to register users for push and receive notifications.

>  The Windows Universal SDK is also compatible with Xamarin Windows Apps.

## Step 1: Install the SDK via the NuGet package manager

The Windows Universal SDK is installed via the [NuGet Package Manager](http://www.nuget.org/). To install the Braze Windows SDK via NuGet:

1. Right-click on the project file
2. Click on "Manage NuGet Packages"
3. Click "Online" in the dropdown menu on the left
4. Search in "NuGet.org" for "Appboy"
5. Click on the "AppboyPlatform.Universal.Release" NuGet Package and click Install

>  The Windows Universal Library should be used for all Windows 8.1, Windows Phone 8.1, and UWP applications.

## Step 2: Creation and configuration of AppboyConfiguration.xml

Create a file called `AppboyConfiguration.xml` in the root directory of your project and add the following code snippet into that file:

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```

>  Be sure to update `YOUR_API_KEY_HERE` with your API key which can be found on the [API Keys]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) page.

Once you've added that snippet, be sure to modify the following file properties for `AppboyConfiguration.xml`

1. Set the `Build Action` to `Content`
2. Set `Copy to Output Directory` to `Copy Always`

## Step 3: Configuring package.appxmanifest

Within the "Capabilities tab, ensure `Internet (Client)` is checked.
![]({% image_buster /assets/img_archive/internet_client.png %})

## Step 4: Editing your app class

- Add the following to the `usings` of your `App.xaml.cs` file:

```csharp
using AppboyPlatform.PCL.Managers;
using AppboyPlatform.Universal;
using AppboyPlatform.Universal.Managers.PushArgs;
```

- Call the following within your `OnLaunched` lifecycle method:

```csharp
Appboy.SharedInstance.OpenSession();
```

- Call the following within your `OnSuspending` lifecycle method:

```csharp
Appboy.SharedInstance.CloseSession();
```

## Basic SDK integration complete

Braze should now be collecting data from your application. See the following articles on how to log [attributes]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/), [events]({{site.baseurl}}/developer_guide/analytics/logging_events/), and [purchases]({{site.baseurl}}/developer_guide/analytics/logging_purchases/) to our SDK and how to instrument push messaging.

>  If you are using the Braze Unity project in the same app, you may have to fully qualify calls to Braze as "AppboyPlatform.Universal.Appboy"

