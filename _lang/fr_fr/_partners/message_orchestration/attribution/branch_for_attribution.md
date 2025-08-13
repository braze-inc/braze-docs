---
nav_title: ""
article_title: ""
alias: /partners/branch_for_attribution/
description: ""
page_type: partner
search_tag: Partner
---

# 



> 



## 



## 

|  |  |
|---|---|
|  |  |
|  |    |
|  |  |


## 

###  

####  

   



```java
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId); 
```


```kotlin
Branch.getInstance().setRequestMetadata("$braze_install_id", Braze.getInstance(context).deviceId)
```



#### 


 


 





```objc
[braze deviceIdOnQueue:dispatch_get_main_queue() completion:^(NSString * _Nonnull deviceId) {
  [[Branch getInstance] setRequestMetadataKey:@"$braze_install_id" value:deviceId];
  // Branch init
}];
```



```swift
braze.deviceId { deviceId in
  Branch.getInstance.setRequestMetadata("$braze_install_id", deviceId)
  // Branch init 
}
```




###  

 

  <br><br> 

###  

1. 
2.  
3.  
4. 

###  

  

 

## 

 

## 

 

    



  

```
{% if most_recently_used_device.${platform} == 'android' %}
user_data_aaid={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```




  


```
{% if most_recently_used_device.${platform} == 'ios' %}
user_data_idfv={{most_recently_used_device.${id}}}
{% endif %}
```





<br>




