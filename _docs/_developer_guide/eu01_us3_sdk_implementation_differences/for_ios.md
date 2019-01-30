---
nav_title: For iOS
page_order: 5
---

# For iOS

To update the default endpoint in your integration of the Braze SDKs please add the following code:

Starting with Braze iOS SDK v3.0.2, you can set a custom endpoint using the `Info.plist` file. Add the `Appboy` dictionary to your Info.plist file. Inside the `Appboy` dictionary, add the `Endpoint` string subentry and set the value to your custom endpoint url’s authority (for example, `sdk.iad-01.braze.com`, not `https://sdk.iad-01.braze.com`).

In versions prior to 3.0.2, add the following class to your application, and then instantiate it and pass it in the `appboyOptions` dictionary you pass to `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` with the key: `ABKAppboyEndpointDelegateKey`.

```
#import "Foundation/Foundation.h"
#import "ABKAppboyEndpointDelegate.h"

@interface AppboyEndpointDelegate : NSObject <ABKAppboyEndpointDelegate>
@end

@implementation AppboyEndpointDelegate
- (NSString *) getApiEndpoint:(NSString *)appboyApiEndpoint {
    return [appboyApiEndpoint stringByReplacingOccurrencesOfString:@"dev.appboy.com" withString:@"sdk.fra-01.braze.eu"];
}

@end
```

## For Xamarin iOS

Pass into your StartWithApiKey call:

```
NSDictionary appboyOptions = new NSDictionary("ABKAppboyEndpointDelegate", new AppboyEndpointDelegate());

Add the AppboyEndpointDelegate class:

class AppboyEndpointDelegate : ABKAppboyEndpointDelegate
{
  public override String GetApiEndpoint(String appboyApiEndpoint)
  {
    return appboyApiEndpoint.Replace("dev.appboy.com", "sdk.fra-01.braze.eu");
  }
}
```
