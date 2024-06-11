---
nav_title: Initial SDK Setup
article_title: Initial SDK Setup for Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 0
description: "This article covers the initial iOS, Android, and FireOS SDK setup for the Xamarin platform."
search_rank: 1
---

# Initial SDK setup

> This reference article covers how to install the Braze SDK for Xamarin. Installing the Braze SDK will provide you with basic analytics functionality as well as working in-app messages with which you can engage your users. 

{% alert important %}
Starting in version 3.0.0, this SDK requires using .NET 6+ and removes support for projects using the Xamarin framework.
Starting in version 4.0.0., this SDK dropped support for Xamarin & Xamarin.Forms and added support for .NET MAUI.
See [Microsoft's policy][1] around the end of support for Xamarin.
{% endalert %}

## Android

### Step 1: Get the Xamarin binding

A Xamarin binding is a way to use native libraries in Xamarin apps. The implementation of a binding consists of building a C# interface to the library, and then using that interface in your application.  See the [Xamarin documentation][2].

There are two ways to include the Braze SDK binding:

#### Option 1: NuGet

The simplest integration method involves getting the Braze SDK from the [NuGet.org][3] central repository. In the Visual Studio sidebar, right click `Packages` folder and click `Add Packages...`.  Search for 'Braze' and install the [`BrazePlatform.BrazeAndroidBinding`][4] package into your project.

#### Option 2: Source

The second integration method is to include the [binding source][5]. Under [`appboy-component/src/androidnet6`][6] you will find our binding source code; adding a project reference to the ```BrazeAndroidBinding.csproj``` in your Xamarin application will cause the binding to be built with your project and provide you access to the Braze Android SDK.

>  The Braze NuGet package depends on the [`Xamarin.Android.Support.v4`][7] NuGet package.

### Step 2: Configure the Braze SDK in Braze.xml

Now that the libraries have been integrated, you have to create an `Braze.xml` file in your project's `Resources/values` folder. The contents of that file should resemble the following code snippet:

>  Be sure to substitute `REPLACE_WITH_YOUR_API_KEY` with the API key located at **Settings** > **API Keys** in the Braze dashboard.

{% alert note %}
If you are using the [older navigation]({{site.baseurl}}/navigation), you can find API keys at **Developer Console** > **API Settings**..
{% endalert %}

```xml
  <?xml version="1.0" encoding="utf-8"?>
  <resources>
    <string translatable="false" name="com_braze_api_key">REPLACE_WITH_YOUR_API_KEY</string>
    <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    <string-array name="com_braze_internal_sdk_metadata">
      <item>XAMARIN</item>
      <item>NUGET</item>
    </string-array>
  </resources>
```
If you are including the binding source manually, remove `<item>NUGET</item>` from your code.

For an example of your `Braze.xml`, see the [Android MAUI][8] sample app.

### Step 3: Add required permissions to Android manifest

Now that you've added your API key, you need to add the following permissions to your `AndroidManifest.xml` file:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```
For an example of your `AndroidManifest.xml`, see the [Android MAUI][9] sample app.

### Step 4: Tracking user sessions and registering for in-app messages
To enable user session tracking and register your app for in-app messages, add the following call to the `OnCreate()` lifecycle method of the `Application` class in your app:

```kotlin
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```

### SDK integration complete

You should now be able to launch your application and see sessions being logged to the Braze dashboard (along with device information and other analytics).  

> Consult the [Android integration instructions][10] for a more in-depth discussion of best practices for the basic SDK integration.

## iOS

{% alert important %}
The iOS bindings for Xamarin SDK version 4.0.0 and later use the [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/), while previous versions use the [legacy AppboyKit SDK](https://github.com/Appboy/Appboy-ios-sdk).
{% endalert %}

### Step 1: Get the Xamarin binding

A Xamarin binding is a way to use native libraries in Xamarin apps.  The implementation of a binding consists of building a C# interface to the library and then using that interface in your application.

There are two ways to include the Braze SDK binding.

#### Option 1: NuGet

The simplest integration method involves getting the Braze SDK from the [NuGet.org][3] central repository. In the Visual Studio sidebar, right-click `Packages` folder and click `Add Packages...`.  Search for 'Braze' and install the [`BrazePlatform.BrazeiOSBinding`][11] package into your project.

#### Option 2: Source

The second integration method is to include the [binding source][5]. Under [`appboy-component/src/iosnet6`][12] you will find our binding source code; adding a project reference to the ```BrazeiOSBinding.csproj``` in your Xamarin application will cause the binding to be built with your project and provide you access to the Braze iOS SDK. Make sure `BrazeiOSBinding.csproj` is showing in your project's "Reference" folder.

### Step 2: Update your app delegate and declare Xamarin usage

Within your `AppDelegate.cs` file, add the following snippet within your `FinishedLaunching` method:

>  Be sure to update `YOUR-API-KEY` with the correct value from the **Developer Console** page.

```csharp
// C#
 Appboy.StartWithApiKey ("YOUR-API-KEY", application, launchOptions, options);
 Appboy.SharedInstance.SdkFlavor = ABKSDKFlavor.Xamarin;
 Appboy.SharedInstance.AddSdkMetadata(new[] { ABKSdkMetadata.ABKSdkMetadataXamarin });
```
If you are including the binding source manually, remove `ABKSdkMetadata.ABKSdkMetadataNuGet` from your code.

See the `AppDelegate.cs` file in the [iOS MAUI Compat][13] sample app.

### SDK integration complete

Braze should now be collecting data from your application and your basic integration should be complete. See the following articles in order to enable [custom event tracking][14], [push messaging][15], and the complete suite of Braze features.

>  Our current public Xamarin binding for the iOS SDK does not connect to the iOS Facebook SDK (linking social data) and does not include sending the IDFA to Braze.

[1]: https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin
[2]: http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/
[3]: https://www.nuget.org/
[4]: https://www.nuget.org/packages/BrazePlatform.BrazeAndroidBinding/
[5]: https://github.com/braze-inc/braze-xamarin-sdk
[6]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidNet6Binding
[7]: https://www.nuget.org/packages/Xamarin.Android.Support.v4/
[8]: https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/Resources/values/Braze.xml
[9]: https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/AndroidManifest.xml
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/
[11]: https://www.nuget.org/packages/BrazePlatform.BrazeiOSBinding/
[12]: https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/iosnet6/BrazeiOSNet6Binding
[13]: https://github.com/braze-inc/braze-xamarin-sdk/blob/694e81dec05537f9ba82b8914d23c5c2381717fc/appboy-component/samples/ios-net-maui/BrazeiOSMauiCompatSampleApp/BrazeiOSMauiCompatSampleApp/Platforms/iOS/AppDelegate.cs#L15
[14]: {{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#tracking-custom-events
[15]: {{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/push_notifications/