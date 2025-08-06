---
nav_title: ""
article_title: ""
description: " "
page_type: partner
search_tag: Partner
---

# 

> 





   



## 

| | |
| ---| ---| 
|  | |
|  |   |
|  |  |
|  |  |





### 




- 
- 
- 
-  




### 

  
- 
- 




## 

###  

 
1.  <br><br>
2.  



###  

 

1.  <br><br>
2.   <br><br>
3.   <br><br>
4. <br><br>
5.   

###  


- 
- 



1.  <br><br>
2.   <br><br>
3.  <br><br> 
4.    <br><br>
5.     <br><br>
6.  <br><br>
7. <br><br>
8. 



###  

 

 







```liquid
{% connected_content
     https://personalization.us-west-2.hightouch.com/v1/collections/customer/records/id/12345
     :method get
     :headers {
       "Authorization": "Bearer {{YOUR-API-KEY}}"
  }
     :content_type application/json
     :save customer
%}
```






```json
{
    "user_id": 12345,
    "full_name": "Jane Doe",
    "lifetime_value": 1492.18,
    "churn_risk": 0.04,
    "90_day_summary": {
        "num_songs_listened": 813,
        "top_genres": [
            "house",
            "techno",
            "ambient"
        ],
        "top_artists": [
            "deadmau5",
            "Marsh",
            "Enamour"
        ],
    },
    "recommendations": {
        "concerts": [
            {
                "artist": "Aphex Twin",
                "location": "San Francisco, CA",
                "event_date": "2023-01-31"
            },
            {
                "artist": "Sultan + Shepard",
                "location": "San Francisco, CA",
                "event_date": "2023-02-25"
            }
        ],
        "upcoming_album_release": {
            "title": "Universal Language",
            "artist": "Simon Doty",
            "label": "Anjunadeep",
            "release_date": "2023-04-28"
        }
    },
}
```



|  |  |
| --- | --- |
| |  |
| |  |
| |  |


## 



