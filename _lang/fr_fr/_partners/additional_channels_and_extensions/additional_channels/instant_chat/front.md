---
nav_title: ""
article_title: ""
description: ""
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# 

> 

  

  

## 



|              |                                                                |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
|             | |
|  | |
|          |  |

## 

- 
- 

## 

###  

 

1. 
2. 
3.  
4. 
    
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    

    

    


  


###  



####  




```liquid
{{event_properties.${message_body}}}
```






#### 






 






###  





###  

  





###  



|||
|---|---|
|||
|||


####  

 

|||
|---|---|
|||
||  |
|||




####  








```liquid
{ 
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```






####  

 







####  

 

####  

 



####  

 





1. 
2. 
3. 



## 

### 

-   
- 

### 

  

### 



### 



###  


