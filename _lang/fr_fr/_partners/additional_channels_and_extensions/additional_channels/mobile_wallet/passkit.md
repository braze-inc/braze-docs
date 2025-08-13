---
nav_title: ""
article_title: ""
alias: /partners/passkit/
description: " "
page_type: partner
search_tag: Partner

---

# 

>  



## 

  

## 

|  |  |
| ----------- | ----------- |
|  |  |
|  |   |
|  |  <br><br>  |
|   |   |


## 

 


- 
- 
- 
- 



## 



1. <br><br><br>
2. <br><br>
3. <br>

## 

   

-  <br><br><br>
-  <br><br><br>
-   <br>



###  

 



|  |  |  |  |
| --------- | -------- | ---- | ----------- |
| |  |  |   |
|  |  |  |  |




#### 

```liquid
{
  "members.member.externalId": "{{${user_id}}}",
  "members.member.points": "100",
  "members.tier.name": "current_customer",
  "person.displayName": "{{${first_name}}} {{${last_name}}}",
  "person.externalId": "{{${user_id}}}",
  "universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"
}
```


###  





   

 

```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```


###  

 



```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```


 

```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```




```liquid
{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```


###  



```liquid
{{longURL}}
```





```liquid
{% capture base64JsonPayload %}{{passData|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longURL %}{{longURL | url_encode}}{% endcapture %}

{{longURL}}
```








###  

 

<br> 
 <br>


  

   

#### 






```liquid
{% assign projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```




```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","person.externalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```




```liquid
{{content_block.${passkit_SmartPass_url}}}
```








   

## 

  
- 
- 
- 

### 



|  |  |  |
| ---- | ---- | ----------- |
|  |  |   <br><br> |
|  <br><br>  |  |   |
|  |  |    |
|  |  |  |


###  

 


- 
-  

#### 

  


-  
- 
  -  
  - 


#### 



```json
{% raw %}{
  "externalId": "{{${user_id}}}",
  "campaignId": " 2xa1lRy8dBz4eEElBfmIz8",
  "expiryDate": "2020-05-10T00:00:00Z"
}{% endraw %}
```

###  

 




 <br>


## 






```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}} 
```







```json
{
    "redemptionDate": null,
    "redemptionCode": "",
    "lat": 0,
    "lon": 0,
    "alt": 0,
    "redemptionSource": "",
    "redemptionReference": "",
    "transactionReference": "",
    "transactionAmount": 0
}
```



```
UNREDEEMED 
```




