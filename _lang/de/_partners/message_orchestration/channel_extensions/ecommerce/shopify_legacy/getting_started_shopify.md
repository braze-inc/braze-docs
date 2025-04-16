---
nav_title: Erste Schritte
article_title: "Erste Schritte mit Shopify"
description: ""
page_type: partner
search_tag: Partner
alias: /getting_started_shopify_legacy/
page_order: 1
---

# Erste Schritte mit Shopify

>  

## 

1. 
2. 
3. 

## 

  





### Unterstützte Funktionen

|Symbol| Definition 
|-------------|-------------
| | Unterstützt
| | Nicht unterstützt
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

| Features |  |  | 
|-------------|-------------|-------------|------------
|       | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i>          
|    | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> 
|      | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-times" title="Nicht unterstützt"></i>   | <i class="fas fa-times" title="Nicht unterstützt"></i>                                        
| <br> <br> Warenkorb-Abbruch   | <i class="fas fa-check" title="Unterstützt"></i> |<i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> 
| <br> <br> <br> <br> <br> <br> <br> <br>  | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i>
|  | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-check" title="Unterstützt"></i>  
|   |<i class="fas fa-check" title="Unterstützt"></i> |<i class="fas fa-check" title="Unterstützt"></i>  |<i class="fas fa-check" title="Unterstützt"></i>
|     | <i class="fas fa-check" title="Unterstützt"></i>| <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-check" title="Unterstützt"></i>     
|    | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-times" title="Nicht unterstützt"></i>     
|    | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i>   
|      | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }    

{% tabs %}


### 

  



{% alert important %}

{% endalert %}

#### 

  

  

#### 

 

 

####  

 

 

 
-  
- 

 
-  
- 

##### 

 

 

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}



- 
- 



{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}



- 
- 



1. 

{% raw %}
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
{% endraw %}

{: start="2"}
2\. 
3\. 

4\. 
5\. 
6\. 

{% alert note %}
 
{% endalert %}

#### 



 







**Monatlich aktive Nutzer:innen (MAU)**

   Bei mobilen Geräten sind anonyme Nutzer:innen geräteabhängig. Für Internet-Nutzer:innen sind anonyme Nutzer:innen vom Browser-Cache abhängig.

{% endtab %}



### 


- 
- Google Tag Manager 

 

  

#### 

  

 
- 
- 

####  

 

 

 
-  
- 

 
-  
- 

##### 

 

 

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}



- 
- 



{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}



- 
- 



1. 

{% raw %}
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
{% endraw %}

{: start="2"}
2\. 
3\. 

4\. 
5\. 
6\. 

{% alert note %}
 
{% endalert %}

#### 



 







**Monatlich aktive Nutzer:innen (MAU)**

   Bei mobilen Geräten sind anonyme Nutzer:innen geräteabhängig. Für Internet-Nutzer:innen sind anonyme Nutzer:innen vom Browser-Cache abhängig.

{% endtab %}


### 

  

#### 



 
- 
- 

#### 



  
-  
  - 
-  
  -  
  - "alias_name": "example@email.com"

  

{% alert note %}

{% endalert %}

#### 

   

 

{% alert tip %}
 
{% endalert %}

  

1. 

2.   

{% raw %}
```javascript
{
  "user_alias": {
    "alias_name": 1234,
    "alias_label": "temp_user_id"
  }
}
```
{% endraw %}

{% subtabs %}
{% subtab API approach %}

{: start="3"}
3\.    


{% endsubtab %}
{% subtab Non-API approach %}

{: start="3"}
3\. 

{% endsubtab %}
{% endsubtabs %}

{: start="4"}
4\.  <br><br>

{: start="5"}
5\.  <br><br>

{: start="6"}
6\.  <br><br>

{: start="7"}
7\. <br><br> 

{% raw %}
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
{% endraw %}

{% alert tip %}
 
{% endalert %}

{: start="8"}
8\. 

{% endtab %}
{% endtabs %}
