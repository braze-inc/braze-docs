## Integrating the .NET MAUI SDK

Integrating the Braze .NET MAUI SDK will provide you with basic analytics functionality as well as working in-app messages with which you can engage your users. 

### Prerequisites

Before you can integrate the .NET MAUI Braze SDK, be sure you meet the following requirements:

- Starting in `version 3.0.0`, this SDK requires using .NET 6+ and removes support for projects using the Xamarin framework.
- Starting in `version 4.0.0`, this SDK dropped support for Xamarin & Xamarin.Forms and added support for .NET MAUI. See [Microsoft's policy](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin) around the end of support for Xamarin.

### Step 1: Get the .NET MAUI binding

{% tabs %}
{% tab android %}
A .NET MAUI binding is a way to use native libraries in .NET MAUI apps. The implementation of a binding consists of building a C# interface to the library, and then using that interface in your application.  See the [Xamarin documentation](http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/). There are two ways to include the Braze SDK binding: using NuGet or compiling from source.

{% subtabs local %}
{% subtab NuGet %}
The simplest integration method involves getting the Braze SDK from the [NuGet.org](https://www.nuget.org/) central repository. In the Visual Studio sidebar, right click `Packages` folder and click `Add Packages...`.  Search for 'Braze' and install the [`BrazePlatform.BrazeAndroidBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidBinding/) package into your project.
{% endsubtab %}

{% subtab Source %}
The second integration method is to include the [binding source](https://github.com/braze-inc/braze-xamarin-sdk). Under [`appboy-component/src/androidnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidNet6Binding) you will find our binding source code; adding a project reference to the ```BrazeAndroidBinding.csproj``` in your .NET MAUI application will cause the binding to be built with your project and provide you access to the Braze Android SDK.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ios %}
{% alert important %}
The iOS bindings for .NET MAUI SDK version 4.0.0 and later use the [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/), while previous versions use the [legacy AppboyKit SDK](https://github.com/Appboy/Appboy-ios-sdk).
{% endalert %}

A .NET MAUI binding is a way to use native libraries in .NET MAUI apps.  The implementation of a binding consists of building a C# interface to the library and then using that interface in your application. There are two ways to include the Braze SDK binding: using NuGet or compiling from source.

{% subtabs local %}
{% subtab NuGet %}
The simplest integration method involves getting the Braze SDK from the [NuGet.org](https://www.nuget.org/) central repository. In the Visual Studio sidebar, right-click `Packages` folder and click `Add Packages...`.  Search for 'Braze' and install the latest .NET MAUI iOS NuGet packages: [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit), [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI), and [Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation) into your project.

We also provide the compatibility libraries packages: [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat) and [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat), to help make your migration to .NET MAUI easier.
{% endsubtab %}

{% subtab Source %}
The second integration method is to include the [binding source](https://github.com/braze-inc/braze-xamarin-sdk). Under [`appboy-component/src/iosnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/iosnet6/BrazeiOSNet6Binding) you will find our binding source code; adding a project reference to the ```BrazeiOSBinding.csproj``` in your .NET MAUI application will cause the binding to be built with your project and provide you access to the Braze iOS SDK. Make sure `BrazeiOSBinding.csproj` is showing in your project's "Reference" folder.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Step 2: Configure your Braze instance

{% tabs %}
{% tab android %}
#### Step 2.1: Configure the Braze SDK in Braze.xml

Now that the libraries have been integrated, you have to create an `Braze.xml` file in your project's `Resources/values` folder. The contents of that file should resemble the following code snippet:

{% alert note %}
Be sure to substitute `YOUR_API_KEY` with the API key located at **Settings** > **API Keys** in the Braze dashboard.
<br><br>
If you are using the [older navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), you can find API keys at **Developer Console** > **API Settings**..
{% endalert %}

```xml
  <?xml version="1.0" encoding="utf-8"?>
  <resources>
    <string translatable="false" name="com_braze_api_key">YOUR_API_KEY</string>
    <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    <string-array name="com_braze_internal_sdk_metadata">
      <item>XAMARIN</item>
      <item>NUGET</item>
    </string-array>
  </resources>
```
If you are including the binding source manually, remove `<item>NUGET</item>` from your code.

{% alert tip %}
To see an example `Braze.xml`, check out our [Android MAUI sample app](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/Resources/values/Braze.xml).
{% endalert %}

#### Step 2.2: Add required permissions to Android manifest

Now that you've added your API key, you need to add the following permissions to your `AndroidManifest.xml` file:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```
For an example of your `AndroidManifest.xml`, see the [Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/AndroidManifest.xml) sample application.

#### Step 2.3: Track user sessions and registering for in-app messages

To enable user session tracking and register your app for in-app messages, add the following call to the `OnCreate()` lifecycle method of the `Application` class in your app:

```kotlin
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```
{% endtab %}

{% tab ios %}
When setting up your Braze instance, add the following snippet to configure your instance:

{% alert note %}
Be sure to substitute `YOUR_API_KEY` with the API key located at **Settings** > **API Keys** in the Braze dashboard.

If you are using the [older navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), you can find API keys at **Developer Console** > **API Settings**..
{% endalert %}

```csharp
var configuration = new BRZConfiguration("YOUR_API_KEY", "YOUR_ENDPOINT");
configuration.Api.AddSDKMetadata(new[] { BRZSDKMetadata.Xamarin });
braze = new Braze(configuration);
```

See the `App.xaml.cs` file in the [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/App.xaml.cs) sample application.
{% endtab %}
{% endtabs %}

### Step 3: Test the integration

{% tabs %}
{% tab android %}
Now you can launch your application and see sessions being logged to the Braze dashboard (along with device information and other analytics). For a more in-depth discussion of best practices for the basic SDK integration, consult the [Android integration instructions]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).
{% endtab %}

{% tab ios %}
Now you can launch your application and see sessions being logged to the Braze dashboard. For a more in-depth discussion of best practices for the basic SDK integration, consult the [iOS integration instructions]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift).

{% alert important %}
Our current public .NET MAUI binding for the iOS SDK does not connect to the iOS Facebook SDK (linking social data) and does not include sending the IDFA to Braze.
{% endalert %}
{% endtab %}
{% endtabs %}
