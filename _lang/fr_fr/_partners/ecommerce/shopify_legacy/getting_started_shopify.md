---
nav_title: ""
article_title: ""
description: ""
page_type: partner
search_tag: Partner
alias: /getting_started_shopify_legacy/
page_order: 1
---

# 

>  



## 

1. 
2. 
3. 

## 

  





### 

||  
|-------------|-------------
| | 
| | 
 

|  |  |  | 
|-------------|-------------|-------------|------------
|       |  |  |           
|    |  |  |  
|      |   |    |                                         
| <br> <br>    |  | |  
| <br> <br> <br> <br> <br> <br> <br> <br>  |  |  | 
|  |   |   |   
|   | |  |
|     | |   |      
|    |   |   |      
|    |  |  |    
|      |  |  | 
    




### 

  







#### 

  

  

#### 

 

 

####  

 

 

 
-  
- 

 
-  
- 

##### 

 

 


```javascript
braze.getUser().setEmail(<email address>);
```




- 
- 




```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```




- 
- 



1. 


```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```



 
 

 
 
 


 


#### 



 









    





### 


- 
-  

 

  

#### 

  

 
- 
- 

####  

 

 

 
-  
- 

 
-  
- 

##### 

 

 


```javascript
braze.getUser().setEmail(<email address>);
```




- 
- 




```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```




- 
- 



1. 


```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```



 
 

 
 
 


 


#### 



 









    




### 

  

#### 



 
- 
- 

#### 



  
-  
  - 
-  
  -  
  - 

  





#### 

   

 


 


  

1. 

2.   


```javascript
{
  "user_alias": {
    "alias_name": 1234,
    "alias_label": "temp_user_id"
  }
}
```






    






 





  <br><br>


  <br><br>


  <br><br>


 <br><br> 


```javascript
{
  "merge_updates": [
    {
      "identifier_to_merge": {
           "user_alias": {
                "alias_label": "temp_user_id",
                "alias_name": "{{canvas_entry_properties.${temp_user_id}}}"
            }
      },
      "identifier_to_keep": {
           "user_alias": {
                "alias_label": "shopify_customer_id",
                "alias_name": "{{canvas_entry_properties.${shopify_customer_id}}}"
            }
      }
    }
  ]
}
```



 



 



