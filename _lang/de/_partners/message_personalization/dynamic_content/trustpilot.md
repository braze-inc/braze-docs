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

## Voraussetzungen



| Voraussetzung | Beschreibung |
| --- | --- |
|  |  |
|  |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Integration

### Schritt 1: 

1.   
2.    
   1.   
   2. 

## 

### Schritt 1:  

 
   *   
   *  POST  
   * 

### Schritt 2: Zugriffstoken abrufen

1. 
2.   
  
{% raw %}

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

{% alert tip %}

{% endalert %}

## 

  

{% raw %}
```liquid
{% connected_content https://api.trustpilot.com/v1/product-reviews/business-units/66ea0530xxxxxx/reviews?sku={{event_properties.${item_sku}}}&stars=5
   :method get
   :headers {"apikey": "xxxxx"}
   :content_type application/json :save result %}
```
{% endraw %}





{% raw %}
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

