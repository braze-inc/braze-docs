---
nav_title: ""
article_title: ""
description: ""
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# 

>  

## 

 

## 



|           |                                                                                                                                 |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|    |                                                                      |
|    |   |
|    |  |

## 



## 

  





###  

 


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>  <code>campaign_slug</code> <br><br><code>https://api.seen.io/v1/campaigns/{campaign_slug}/receivers/</code></td>
    </tr>
    <tr>
      <td></td>
      <td> <code>POST</code> </td>
    </tr>
    <tr>
      <td></td>
      <td><br><br><pre><code>[
    {
    "first_name":"{{${first_name}}}",
    "last_name":"{{${last_name}}}",
    "email":"{{${email_address}}}",
    "customer_id":"{{${braze_id}}}"
    }
]</code></pre><br></td>
    </tr>
    <tr>
      <td></td>
      <td><br> <code>Token {token}</code><br> <code>application/json</code><br><br></td>
    </tr>
  </tbody>
</table>





 

###  

1.  
2. 
3.  
4. 
5. 

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.customer_id,
      "_update_existing_only": true,
      "landing_page_url": payload.landing_page_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```

 



  

```json
{
        "customer_id": "101",
        "campaign_slug": "onboarding",
        "landing_page_url": "your.subdomain.com/v/12345",
        "video_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/output.m3u8",
        "thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/thumbnail.jpg",
        "email_thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/email_thumbnail.jpg"
       
}
```


 
 
