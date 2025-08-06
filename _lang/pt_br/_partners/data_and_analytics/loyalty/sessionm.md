--- 
nav_title: ""
article_title: ""
description: ""
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
--- 

# 

> 

## 

|  |  |  |
| --- | --- | --- |
|  |  |   |
|  |  |   |
|  |  |   |
|  |  |  |
|  |  |   |
|  |  |    |
|  |  |    |
|  |  |   |
|  |  |    |
|  |  |   |




 

## 



- 
- 
- 
- 
- 

## 

###  

 



###  

####  

  

 

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```




    
      







<br><br>
 


```bash
curl --location -g --request POST '{{endpoint_core}}/priv/v1/apps/{{apikey_core}}/users/{{user_id}}/tags' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic {{base64_encoded_string}}' \
--data-raw '{
"tags":[
"tagname1",
"tagname2"
],
"ttl":20000
}'
```



####  



## 

 

  

###  

 





###  



  




```
{% capture postbody %}
{"retailer_id":"YOUR-RETAIL-ID","user_id":"{{${user_id}}}","skip":0,"take":1000,"include_pending_extended_data":false,"culture":"en-US"}
{% endcapture %}

{% connected_content
     {{endpoint_connect}}/offers/api/2.0/offers/get_user_offers
:method post     
:headers {
       "Content-Type": "application/json",
       "Authorization": "Basic YOUR-BASE64-ENCODED-KEY"
  }
     :body {{postbody}}
     :save wallet
%}
```


###  

 


```
{
    "status": "ok",
    "payload": {
      "user": {
        "opted_in": false,
        "activated": false,
        ...
      },
      "user_id": "00000000-0000-0000-0000-000000000000",
      "user_offers": [
        {
          "offer_id": "1a2b3324-1da6-4e49-b921-afc386dabb60",
          "offer_group_id": "00000000-0000-0000-0000-000000000000",
          "offer_type": "manual_fulfillment",
          ...
        }
      ],
      "total_records": 1,
      "offer_groups": [
        {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "offer_categories": [
        {
          "id": "9a82f973-aae6-4e10-839b-7117a852cf9e",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "total_points": 1000,
      "available_points": 100
    }
}
```


 


 


## 



###  

 


- 
- 
- 
- 
- 







- 
- 
-  
- 

 

###  

 







 

###  








```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```




 






