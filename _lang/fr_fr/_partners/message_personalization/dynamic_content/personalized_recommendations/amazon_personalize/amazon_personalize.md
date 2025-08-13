---
nav_title: ""
article_title: ""
alias: "/partners/amazon_personalize_overview/"
description: " "
page_type: partner
search_tag: Partner
---

# 
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
>  



## 

    



## 

| | |
| ---| ---| 
|  |   |
|  |   |
|  |   |







 
- 
- 
- 










- 
  - 
  - 
- 
  - 
  - 
- 
  - 
  - 

 




## 

###  

   

 
- <br><br>
  - 
  - 



 

###  

  

- 
- 
- 
- 

## 

 

1. <br>   <br><br>
2. <br>   

### 

  

## 


  

### 

<br><br>



```json
[
  {
    "id": "abc123",
    "url": "http://productpage.com/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn.com/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage.com/product/xyz987",
    "name": "Great Item",
    "price": 19.99,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
  ...
]
```

 



```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```



```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```





 


