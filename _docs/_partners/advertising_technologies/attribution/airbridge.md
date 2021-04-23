---
nav_title: Airbridge
alias: /partners/airbridge/

description: "This article outlines the partnership between Braze and Airbridge, which offers people-based attribution and incrementality measurement to measure true marketing effectiveness across devices, identities, and platforms."
page_type: partner

---

# Airbridge

> Airbridge offers people-based attribution and incrementality measurement to measure and analyze true marketing effectiveness across devices, identities, and platforms.

With Airbridge and Braze, you can pass every organic and non-organic install attribution data to Braze to build more personalized marketing campaigns and understand exactly where users were acquired.


## Integration

To learn more about Airbridge and Braze integration, please visit [this link](https://developers.airbridge.io/v1.0-en-us/docs/braze).

### Step 1: Integration Requirements

* This integration supports iOS and Android apps.
* Your app will need Braze's SDK and Airbridge's SDK installed.

### Step 2: Including the Code Snippet

Integrating Airbridge to Braze will be made via SDK-to-SDK. Attribution Data collected by Airbridge SDK will be transmitted to Braze, via Braze SDK, so you will need to include the below code snippet.


{% tabs %}
{% tab Android %}
If you have an Android app, you will need to include the code snippet below.

#### Java
```java
AirbridgeConfig config = new AirbridgeConfig.Builder(BuildConfig.AIRBRIDGE_APP_NAME, BuildConfig.AIRBRIDGE_APP_TOKEN)
        .setOnAttributionResultReceiveListener(new OnAttributionResultReceiveListener() {
            @Override
            public void onAttributionResultReceived(Map<String, String> result) {
                AttributionData data = new AttributionData(
                    result.get("attributedChannel"),
                    result.get("attributedCampaign"),
                    result.get("attributedAdGroup"),
                    result.get("attributedAdCreative")
                );
              
                Appboy.getInstance(applicationContext).getCurrentUser().setAttributionData(data);

                // NOTE: Data point will be consumed
                Appboy.getInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_ad_content", result.get("attributedContent"));
                Appboy.getInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_term", result.get("attributedTerm"));
                Appboy.getInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_sub_id", result.get("attributedSubPublisher"));
                Appboy.getInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_sub_id_1", result.get("attributedSubSubPublisher1"));
                Appboy.getInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_sub_id_2", result.get("attributedSubSubPublisher2"));
                Appboy.getInstance(applicationContext).getCurrentUser().setCustomUserAttribute("airbridge_sub_id_3", result.get("attributedSubSubPublisher3"));
            }
        })
        .build();
Airbridge.init(this, config);
```

#### Kotlin
```kotlin
val config = AirbridgeConfig.Builder(BuildConfig.AIRBRIDGE_APP_NAME, BuildConfig.AIRBRIDGE_APP_TOKEN)
        .setOnAttributionResultReceiveListener(object : OnAttributionResultReceiveListener {
            override fun onAttributionResultReceived(result: Map<String, String>) {
                val data = AttributionData(
                    result["attributedChannel"],
                    result["attributedCampaign"],
                    result["attributedAdGroup"],
                    result["attributedAdCreative"]
                )

                Appboy.getInstance(applicationContext).currentUser?.setAttributionData(data)
                  
                // NOTE: Data point will be consumed
                Appboy.getInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_ad_content", result["attributedContent"])
                Appboy.getInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_term", result["attributedTerm"])
                Appboy.getInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_sub_id", result["attributedSubPublisher"])
                Appboy.getInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_sub_id_1", result["attributedSubSubPublisher1"])
                Appboy.getInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_sub_id_2", result["attributedSubSubPublisher2"])
                Appboy.getInstance(applicationContext).currentUser?.setCustomUserAttribute("airbridge_sub_id_3", result["attributedSubSubPublisher3"])
            }
        })
        .build()
Airbridge.init(this, config)
```
{% endtab %}

{% tab iOS %}
If you have an iOS app, you will need to include the code snippet below.

#### Swift
```swift
@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
    func application(_ application: UIApplication, 
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AirBridge.setting()?.attributionCallback = { attribution in
            let data = ABKAttributionData(network: attribution["attributedChannel"],
                                          campaign: attribution["attributedCampaign"],
                                          adGroup: attribution["attributedAdGroup"],
                                          creative: attribution["attributedAdCreative"])
            
            // NOTE: Data point will be consumed
            Appboy.sharedInstance()?.user.attributionData = data
            
            [
                "attributedContent": "airbridge_content",
                "attributedTerm": "airbridge_term",
                "attributedSubPublisher": "airbridge_sub_id",
                "attributedSubSubPublisher1": "airbridge_sub_id_1",
                "attributedSubSubPublisher2": "airbridge_sub_id_2",
                "attributedSubSubPublisher3": "airbridge_sub_id_3",
            ].forEach { (key, brazeKey) in
                guard let value = attribution[key] else {
                    return
                }
                
                Appboy.sharedInstance()?.user.setCustomAttributeWithKey(brazeKey, andStringValue: value)
            }
            
            Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
        }
      
        AirBridge.getInstance("YOUR_APP_TOKEN", appName: "YOUR_APP_NAME", withLaunchOptions: launchOptions)
      
        return true
    }
}
```

#### Objective-C
```objc
@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
    AirBridge.setting.attributionCallback = ^(NSDictionary<NSString*, NSString*>* _Nonnull attribution) {
        ABKAttributionData* data = [[ABKAttributionData alloc] initWithNetwork:attribution[@"attributedChannel"]
                                                                      campaign:attribution[@"attributedCampaign"]
                                                                       adGroup:attribution[@"attributedAdGroup"]
                                                                      creative:attribution[@"attributedAdCreative"]];
        [Appboy.sharedInstance.user setAttributionData:data];

        // NOTE: Data point will be consumed
        NSDictionary* keyMap = @{
            @"attributedContent": @"airbridge_content",
            @"attributedTerm": @"airbridge_term",
            @"attributedSubPublisher": @"airbridge_sub_id",
            @"attributedSubSubPublisher1": @"airbridge_sub_id_1",
            @"attributedSubSubPublisher2": @"airbridge_sub_id_2",
            @"attributedSubSubPublisher3": @"airbridge_sub_id_3",
        };
        
        for (NSString* key in keyMap.allKeys) {
            NSString* brazeKey = keyMap[key];
            NSString* value = attribution[key];
            
            [Appboy.sharedInstance.user setCustomAttributeWithKey:brazeKey andStringValue:value];
        }
        
        [Appboy.sharedInstance flushDataAndProcessRequestQueue];
    };
  
    [AirBridge getInstance:"YOUR_APP_TOKEN" appName:"YOUR_APP_NAME" withLaunchOptions:launchOptions];

    return YES;
}

@end
```
{% endtab %}
{% endtabs %}


## Integratable Data Types
Airbridge can send seven types of data to Braze as in the following. These data are used for User Install Attribution and Custom Attribution. You can view it on Dashboard and use it for filtering.
In addition to the four basic data types (Source, Campaign, Ad Group, Ad) provided by Braze, Airbridge offers three additional data types such as airbridge_ad_content, airbridge_sub_id, and airbridge_term as a Custom Attribute. Among these, airbirdge_search_keyword delivers a keyword to the value when it comes from search ads.

{% alert important %}
Braze data points will be used when you send data marked as optional because it is transmitted as Custom User Attribute.
{% endalert %}

| Airbridge Data Field | Braze Segment Filter | Type |
| -------------------- | --------------------- | --------------------- |
| attributedChannel | Install Attribution Source | Install Attribution Data |
| attributedCampaign | Install Attribution Campaign | Install Attribution Data |
| attributedAdGroup | Install Attribution Ad Group | Install Attribution Data |
| attributedAdCreative | Install Attribution Ad | Install Attribution Data |
| attributedContent (Optional) | airbridge_content | Custom User Attribute |
| attributedTerm (Optional) | airbridge_term | Custom User Attribute |
| attributedSubPublisher (Optional) | airbridge_sub_id | Custom User Attribute |
| attributedSubSubPublisher1 (Optional) | airbridge_sub_id_1 | Custom User Attribute |
| attributedSubSubPublisher2 (Optional)	| airbridge_sub_id_2 | Custom User Attribute |
| attributedSubSubPublisher3 (Optional)	| airbridge_sub_id_3 | Custom User Attribute |



## Airbridge Click Tracking URLs in Braze (Optional)

Using click tracking links in your Braze campaigns will allow you to easily see which campaigns are driving app installs and re-engagement. As a result, you'll be able to measure your marketing efforts more effectively and make data-driven decisions on where to invest more resources for the maximum ROI.

To get started with Airbridge click tracking links, visit this [documentation](https://help.airbridge.io/hc/en-us/articles/900001037886-Tracking-Link-Generation/). You can insert the Airbridge click tracking links into your Braze campaigns directly. Airbridge will then use its [probabilistic attribution methodologies](https://help.airbridge.io/hc/en-us/articles/900003300526-Airbridge-Identity-Matching-Logic) to attribute the user that has clicked on the link. To improve the accuracy of attributions from your Braze campaigns, we recommend appending your Airbridge tracking links with a device identifier. This will deterministically attribute the user that has clicked on the link.

{% tabs %}
{% tab Android %}
For Android, Braze allows customers to opt-in to [Google Advertising ID collection (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). The GAID is also collected natively through the Airbridge SDK integration. You can include the GAID in your Adjust click tracking links by utilizing the Liquid logic below:
{% raw %}

```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
For iOS, both Braze and Airbridge automatically collect the IDFV natively through our SDK integrations. This can be used as the device identifier. You can include the IDFV in your Airbridge click tracking links by utilizing the Liquid logic below:

{% raw %}

```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

__This recommendation is purely optional__<br>
If you currently do not use any device identifiers - such as the IDFV or GAID - in your click tracking links, or do not plan to in the future, Airbridge will still be able to attribute these clicks through probabilistic modeling.


