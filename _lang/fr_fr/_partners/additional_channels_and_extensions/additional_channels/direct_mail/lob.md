---
nav_title: ""
article_title: "" 
alias: /partners/lob/
description: ""
page_type: partner
search_tag: Partner

---

# 

> 



## 



- 
- 

## 

|| |
| ---| ---|
| |  |
|  |  |


## 

###  

 

|  |  |
| ------------ | ------------------- |
|  | <br><br><br><br><br><br><br><br><br><br><br><br><br>|


###  

 





- 
-  

#### 

   

-  
- 
  -  
  - 



#### 

 


```json
"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}"
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"
```


###  

   


 <br>


 

##  

 


 


###  

1. 
2. 
3. 
4.  

###  

 


 


```json
// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JavaScript dot notation, such as payload.x.y.z

// In this example, this function removes the periods and underscores of the event_type.id sent in the Lob payload so that an event id that is formatted like: `letter.processed_for_delivery` will log an event to Braze with the name `letter processed for delivery`.

function formatString(input) {
    return input.replace(/[._]/g, ' ');
}

let braze_event = formatString(payload.event_type.id);

// In this example, a metadata value passed in the Lob Webhook called 'external_ID' is being used to match the Event to the corresponding Braze user.

let brazecall = {
  "attributes": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "Most Recent Mailer": payload.body.description
    }
  ],
  "events": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "name": braze_event,
      "time": new Date().toISOString(),
// Customize the properties to the Lob event you are syncing. Our example below pulls in the Tracking Events array of objects associated with certain Lob events.
      "properties": {
        "tracking_events": payload.body.tracking_events
      }
    }
  ]
};
// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

###  

1. 
2. 
