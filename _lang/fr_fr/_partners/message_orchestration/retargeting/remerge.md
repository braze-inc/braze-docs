---
nav_title: ""
article_title: ""
alias: /partners/remerge/
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
|  |  |
|  |  |
|  |  |
|  |  | 


## 

###  

 




-  
- 

```liquid
{% assign event_name = 'your_remerge_event_name' %} 
{% assign android_app_id = 'your_android_app_id' %} 
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'event_name','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

https://remerge.events/event?partner=braze&app_id=\{% if most_recently_used_device.${idfa} == blank %}android_app_id{% else %}iOS_app_id{% endif %}&key=1cs3p12k&ts='now' | date: '%s' }}&{% if {{most_recently_used_device.${idfa} == blank%}aaid=custom_attribute.${aaid}{% else %}idfa=most_recently_used_device.${idfa{%endif%}&event=event_name&non_app_event=true&data=json | url_param_escape

{% if most_recently_used_device.${idfa} == blank and custom_attribute.${aaid} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```



- 
-  
- 
- 




 


#### 



-  
- 
  - 



#### 



##  

  


 <br>



