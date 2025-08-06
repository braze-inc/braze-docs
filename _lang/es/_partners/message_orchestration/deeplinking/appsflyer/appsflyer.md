---
nav_title: ""
article_title: ""
alias: /partners/appsflyer/
description: ""
page_type: partner
search_tag: Partner

---

# 



> 

 

 

## 

|  |  |
|---|---|
|  |  |
|  |    |
|  | 
|  |  |
|  |  |


## 

###  



 

 

```kotlin
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
   customData["brazeCustomerId"] = deviceId
   setAdditionalData(customData)
}
```




 


 






```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]
```



```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
    @"brazeDeviceId": braze.deviceId
}];
```







```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```



###  

 

  <br><br> 

###  

1.  
2. 
3.  
4. 



###  

  

 

###  

#### 



|  |  |
| -------------------- | --------------------- |
|  |  |
|  |  |
|  |  |
|  |  |




      




 


## 

 


     


###  

1.   
2.  

###  











1. 
    *  
        *  
        * 
        *  
    * 
2.   










1. 
    *  
        *  
        * 
        *   
    * 
2.  












####  


1. 
    *  
        *  
        * 
        *  
    * 
2.   







####  
  

1. 
2. 


####  


1. 
    *  
        *  
        * 
        *   
    * 
2.  







####  
  

1. 
2. 






###  





####  


1. 
2. 
3. 
4.  
 

####  
1.  
2. 



####  





```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

####  
    






####  


1. 
2. 
3. 
4.  

####  
 
1.  
2.  
3. 


####  





```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

####  
 

1.  
2.  





 

### 

  

   



  

```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```




  


```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```






