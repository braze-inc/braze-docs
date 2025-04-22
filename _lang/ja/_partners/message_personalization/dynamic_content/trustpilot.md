---
nav_title: ""
article_title: ""
description: ""
alias: /partners/trustpilot/
page_type: partner
search_tag: Partner
---

# 

> 



*   
* 

## 前提条件

開始する前に、次のものが必要になります。

| 前提条件 | 説明 |
| --- | --- |
|  |  |
|  |  |


## 統合

### ステップ1:

1.   
2. APIキーをまだ持っていない場合は、新規に作成する：  
   1.   
   2. 

## 

### ステップ1: 


   * [Webhook URL](https://developers.trustpilot.com/invitation-api?_gl=1*1hxojlc*_ga*MjEzMDkzNjQ5NS4xNzMxNjgxOTQ0*_ga_3TEL80JZSG*MTczNjU0MzY0Ny45LjAuMTczNjU0MzY0Ny4wLjAuMA..#create-invitation(s)): `https://invitations-api.trustpilot.com/v1/private/business-units/{businessUnitId}/email-invitations`  
   * POST  
   * 

### ステップ2: アクセストークンを取得する

1. 
2. 
  


```liquid
{% connected_content 
https://api.trustpilot.com/v1/oauth/oauth-business-users-for-applications/accesstoken
:method post
:headers {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "Basic {{'API_KEY:API_SECRET' | base64_encode}}" }
:body grant_type=client_credentials
:save token
:retry
:cache_max_age 3600 %}

{{token.access_token}}

```

{% endraw %}

{: start="3"}
3\.





## 




```liquid
{% connected_content https://api.trustpilot.com/v1/product-reviews/business-units/66ea0530xxxxxx/reviews?sku={{event_properties.${item_sku}}}&stars=5
   :method get
   :headers {"apikey": "xxxxx"}
   :content_type application/json :save result %}
```







```liquid
  {
   "productReviews": [
       {
           "id": "670d5810ba62e6b31de97de9",
           "createdAt": "2024-10-14T17:42:40.286Z",
           "stars": 5,
           "content": "Such a great toy truck, my kids really enjoy it! ",
           "consumer": {
               "id": "6176xxxx",
               "displayName": "Kevin Bob"
           },
           "language": "en",
           "attributeRatings": [],
           "attachments": [],
           "firstCompanyComment": null
       }
   ],
   "links": []
 ```
{% endraw %}

{: start="2"}
2\.

