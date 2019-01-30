---
nav_title: For Android
page_order: 5
---

# For Android
To update the default endpoint in your integration of the Braze SDKs please add the following code to your `appboy.xml`:

``<string translatable="false" name="com_appboy_custom_endpoint">sdk.fra-01.braze.eu</string>``

SDK Endpoint configuration via `appboy.xml` is available starting with Braze Android SDK v2.1.1.

## For Xamarin Android

In your Application OnCreate:

```
Appboy.SetAppboyEndpointProvider(new CustomEndpointProvider());

Add the CustomEndpointProvider class:

class CustomEndpointProvider : Java.Lang.Object, IAppboyEndpointProvider
{
  public Android.Net.Uri GetApiEndpoint (Android.Net.Uri uri)
  {
    return uri.BuildUpon().Authority ("sdk.fra-01.braze.eu").Build();
  }
}
```
