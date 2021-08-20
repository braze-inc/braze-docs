---
nav_title: Initial SDK Setup
article_title: Xamarin Initial SDK Setup
platform: Xamarin
page_order: 0
description: "This article covers the inital iOS, Android, and FireOS SDK setup for the Xamarin platform."

---

# Initial SDK Setup

Installing the Braze SDK will provide you with basic analytics functionality as well as working in-app messages with which you can engage your users.

## Android

### Step 1: Get the Xamarin binding

A Xamarin binding is a way to use native libraries in Xamarin apps. The implementation of a binding consists of building a C# interface to the library, and then using that interface in your application.  See [the Xamarin documentation][2].

There are two ways to include the Braze SDK binding.

#### Option 1: Nuget

The simplest integration method involves getting the Braze SDK Bindings from the [Nuget.org][9] central repository. In the Visual Studio sidebar, right click `Packages` folder and click `Add Packages...`.  Search for 'Braze' and install the [`AppboyPlatform.AndroidBinding`][13] package into your project.

#### Option 2: Source

The second integration method is to include the binding source found [here][3].  Under `appboy-component\src\android` you will find our binding source code; adding a project reference to the ```AppboyPlatform.XamarinAndroidBinding.csproj``` in your Xamarin application will cause the binding to be built with your project and provide you access to the Braze Android SDK.

>  The Braze Nuget package depends on the [`Xamarin.Android.Support.v4`][12] Nuget package.

### Step 2: Configure the Braze SDK in braze.xml
Now that the libraries have been integrated, you have to create an `braze.xml` file in your project's `Resources/values` folder. The contents of that file should resemble the following code snippet:

>  Be sure to substitute `REPLACE_WITH_YOUR_API_KEY` with the API key located the [Settings][4] page of the Braze dashboard.

```java
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
    <string name="com_appboy_api_key">REPLACE_WITH_YOUR_API_KEY</string>
    <string translatable="false" name="com_appboy_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    </resources>
```

### Step 3: Add Required Permissions to Android Manifest
Now that you've added your API key, you need to add the following permissions to your `AndroidManifest.xml` file:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

### Step 4: Tracking User Sessions and Registering for In-App Messages
To enable user session tracking and register your app for in-app messages, add the following call to the `OnCreate()` lifecycle method of the `Application` class in your app:

```csharp
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```

### SDK Integration Complete

You should now be able to launch your application and see sessions being logged to the Braze dashboard (along with device information and other analytics).  

> Consult the [Android integration instructions][8] for a more in-depth discussion of best practices for the basic SDK integration.

## iOS

### Step 1: Get the Xamarin binding

A Xamarin binding is a way to use native libraries in Xamarin apps.  The implementation of a binding consists of building a C# interface to the library and then using that interface in your application.

There are two ways to include the Braze SDK binding.

#### Option 1: Nuget

The simplest integration method involves getting the Braze SDK Bindings from the [Nuget.org][19] central repository. In the Visual Studio sidebar, right-click `Packages` folder and click `Add Packages...`.  Search for 'Braze' and install the [`AppboyPlatformXamariniOSBinding`][111] package into your project.

#### Option 2: Source

The second integration method is to include the binding source found [here][113].  In [our github repo][17] you will find our binding source code; adding a project reference to the ```AppboyPlatformXamariniOSBinding.csproj``` in your Xamarin application will cause the binding to be built with your project and provide you access to the Braze iOS SDK. Please make sure `AppboyPlatformXamariniOSBinding` is showing in your project's "Reference" folder.

### Step 2: Update your App Delegate and Declare Xamarin Usage

Within your `AppDelegate.cs` file, add the following snippet within your `FinishedLaunching` method:

>  Be sure to update `YOUR-API-KEY` with the correct value from your [Settings][5] page.

```csharp
// C#
 Appboy.StartWithApiKey ("YOUR-API-KEY", UIApplication.SharedApplication, options);
 Appboy.SharedInstance.SdkFlavor = ABKSDKFlavor.Xamarin;
```

**Implementation Example**

See the `AppDelegate.cs` file in the [TestApp.XamariniOS][110] sample app.

### Step 3: Add your SDK endpoint to your Info.plist file

Within your `Info.plist` file, add the following snippet:

>  Be sure to update `YOUR-SDK-ENDPOINT` with the correct value from your [Settings][5] page.

```csharp
// C#
<key>Braze</key>
<dict>
 <key>Endpoint</key>
 <string>YOUR-SDK-ENDPOINT</string>
</dict>
```

You can optionally include verbose logging by including the following snippet:

```csharp
// C#
<key>Braze</key>
<dict>
 <key>LogLevel</key>
 <string>0</string>
 <key>Endpoint</key>
 <string>YOUR-SDK-ENDPOINT</string>
</dict>
```

Note that prior to Braze iOS SDK v4.0.2, the dictionary key `Appboy` must be used in place of `Braze`.

### SDK Integration Complete

Braze should now be collecting data from your application and your basic integration should be complete. Please see the following sections in order to enable custom event tracking, push messaging, the news-feed and the complete suite of Braze features.

>  Our current public Xamarin binding for the iOS SDK does not connect to the iOS Facebook SDK (linking social data) and does not include sending the IDFA to Braze.

[2]: http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/
[3]: https://github.com/Appboy/appboy-xamarin-bindings
[4]: https://dashboard-01.braze.com/app_settings/app_settings/ "Settings"
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/
[9]: https://www.nuget.org/
[12]: https://www.nuget.org/packages/Xamarin.Android.Support.v4/
[13]: https://www.nuget.org/packages/AppboyPlatform.AndroidBinding/
[113]: https://github.com/Appboy/appboy-xamarin-bindings
[15]: https://dashboard-01.braze.com/app_settings/app_settings/ "Settings"
[17]: https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/src/ios-unified
[19]: https://www.nuget.org/
[110]: https://github.com/Appboy/appboy-xamarin-bindings/tree/master/appboy-component/samples/ios-unified/TestApp.XamariniOS
[111]: https://www.nuget.org/packages/AppboyPlatformXamariniOSBinding/

