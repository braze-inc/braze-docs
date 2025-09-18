---
nav_title: ""
article_title: ""
page_order: 1
alias: /partners/segment/
description: ""
page_type: partner
search_tag: Partner

---

# 



>  

 

- 
-  
-  

## 

|  |  |
| ----------- | ----------- |
|  |  |
|  | <br><br> |


## 

  

###  

 

###  



 





|  |  |
| ----------- | ------- |
| <br> |<br><br>  |
| <br> | <br><br> <br><br>|






#### 

 


 


  







<br>











 











<br>









 








 









  



 










#### 

  

 





###  

 




|  |  |
| ------- | ----------- |
|  |   | 
| <br> |  | 
|  |  | 
|  |  |





|  |  |
| ------- | ----------- |
|  |   | 
| <br> |  | 
|  |  |
|  |  |
|  |   |
|  |     |
|  |  | 
|  |   |
|  |  | 
|  |   |
|  | <br>  |
|  |     |
|  |   |
|  |    |
|  |    |
|  |    |
|  |    |
|  |    |
| |  |
|  | <br>  | 
|  |     |
|  |    |
|  |    |
|  | <br><br><br><br> |
|  | <br><br><br><br> |
|  | <br><br><br><br> | 
|  | <br><br><br><br> | 





|  |  |
| ------- | ----------- |
|  |   | 
|  |  | 
|  |  | 
|  | <br><br><br><br> |





###  

   





|  |  |
| --------------- | --------------------- |
|  |  |
|  |  |
|  |  |


  

  

      

  




#### 

 



|  |  |
| ------------- | ----------- |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |
|  |  |




##### 



 

1.  
2.   



```swift
analytics.identify(
  userId: "{your-user}",
  traits: [
    "braze_subscription_groups": [
      [
        "subscription_group_id": "{your-group-id}",
        "subscription_group_state": "subscribed"
      ],
      [
        "subscription_group_id", "{your-group-id}",
        "subscription_group_state": "unsubscribed"
      ]
    ]
  ]
)
```


```kotlin
analytics.identify(
  "{your-user}",
  buildJsonObject {
    put("braze_subscription_groups", buildJsonArray {
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "subscribed")
          }
        )
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "unsubscribed")
          }
        )
      }
    )
  }
)
```


```typescript
analytics.identify(
  "{your-user}",
  {
    braze_subscription_groups: [
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "subscribed"
      },
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "unsubscribed"
      }
    ]
  }
)
```



##### 



|  |  |  |
|---|---|---|
|  |  | <br> |
|  |  | <br> 
|  |  | <br>
|  |   |  |





   





#### 

 

 



|  |  |  |
|---|---|---|
|  |  |  <br>|
|  |  |  <br> |
|  |  |  <br> |


##### 








#### 








###  



  






 


##  

 

 

## 

  







## 



  





|  |  |
| ----------------- | ------------------ |
|  |  |
|  |  |


 




|  |  |
| ----------------- | ------------------ |
|  |  |
|  |  |


  







1. 
  -  <br><br>  

  
  
  


 
  -  





 

 





   




