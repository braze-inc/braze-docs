---
nav_title: ""
article_title: ""
description: ""
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# 

>   

## 


|  |  |
|---|---|
|  | |
|  | |
|   |  |

## 



## 

###  

1. 
2. 
3. 
4. 



###  



####  



```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```








```liquid
{% assign body = {{api_trigger_properties.${msg_body}}} %}
{% assign msg = body | split: "
" %}
New message from Zendesk: 
{{msg[2]}}
 
Feel free to respond directly to this number!
```




####  









###  



1. 
2. 
3. 
- 
-  



  




```liquid
{
    "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
			"trigger_properties": {
    "msg_body": "{{ticket.latest_public_comment_html}}"
		},
		"attributes": {
        "zendesk_ticket" : "{{ticket.id}}",
	"zendesk_ticket_open" : "true"
    }
        }
    ]
}
```



###  








-  
- 



 




```liquid
{
    "campaign_id": "{{YOUR_API_KEY}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
"trigger_properties": {
    "msg_body": "Your ticket has been closed"
		},
,
			"attributes": {
	"zendesk_ticket_open" : "false"
    }
        }
    ]
}
```


###  

 

###  



|            |                                                                               |
|--------------------|--------------------------------------------------------------------------------------|
|  |                                                      |
|  |  |


####  

 

|             |                                                                                                                |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
|  |                                                                  |
|          |                                                                                   |
|     |  |




####  

 


- 
-  
- 
- 
-   
-  


```liquid
{
  "ticket": {
    "subject": "Action Needed",
    "comment": {
      "body": "{{sms.${inbound_message_body}}}"
    },
"requester":{
"name": "{{${first_name}}} {{${last_name}}}",
"user_fields": {
"braze_external_id": "{{${user_id}}}"
}
},
    "priority": "normal",
    "type": "problem"
  }
}
```





####  

 







####  






```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```



- 
-  
- 
    - 
    -  

 


```liquid
{
  "ticket": {
    "comment": {
      "body": "Inbound message from {{${first_name}}} {{${last_name}}}: {{sms.${inbound_message_body}}}"
    }
}
}
```


####  
- 
- 
- 


