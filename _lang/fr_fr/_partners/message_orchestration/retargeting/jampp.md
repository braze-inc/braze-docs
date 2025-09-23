---
nav_title: ""
article_title: ""
alias: /partners/jampp/
description: ""
page_type: partner
search_tag: Partner

---

# 

>  



## 

 


- 
- 
- 

## 



|  |  |
|---|---|
|  |  |
|  |  |
|  |  |
|  |  | 
|  | 


## 

###  






-  
- 

```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```



-  
- 
-  




 


#### 



-  
- 
  - 



#### 



###  

  


 <br>



