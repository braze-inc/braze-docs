---
nav_title: ""
article_title: ""
description: ""
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# 

>  

 
-  
-  

## 

|  |  |
|---|---|
|  |  |
|  |  |
|  |  |
|  |   |


## 

###  



-   
-   


- 
-  



#### 

 

-  
- 
  -  
  - 



#### 

  


```json
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}", 
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```


###  







## 

  

## 

###  

1. <br><br>
2. <br><br>
3. <br><br><br>
4. 
- 
-  
- 
- 
  - <br><br>
5. <br><br>
6.   

###  



 

1. <br><br>
2. <br><br>
3. <br><br>
4.  <br><br>
5. <br><br>
6. <br><br><br>
7. <br><br>
8. 


