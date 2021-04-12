---
nav_title: May
page_order: 8
---
# May 2020

## Google Tag Manager

Added documentation and examples of how to deploy and manage Braze's Android SDK using [Google Tag Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/android_google_tag_manager/).

## New Blacklist Email API Endpoint
You can now [blacklist]({{site.baseurl}}/api/endpoints/email/post_blacklist/) email addresses via the Braze API. Blacklisting an email address will unsubscribe the user from email and mark them as hard bounced.

## API Key Change for Braze API Endpoints

As of May 2020, Braze has changed how we read API keys to be more secure. Now API keys should be passed in as a request header. Examples can be found on individual endpoint pages under __Example Request__, as well as in the __API Key Explanation__ below.

Braze will continue to support the `api_key` being passed through the request body and URL parameters, but will eventually be sunset (TBD). __Please update your API calls accordingly.__ These changes have been updated within [Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) and will soon be input into the Braze [Swagger UI](https://www.braze.com/docs/api/interactive). 
{% details API Key Explanation %}
{% tabs %}
{% tab GET Request %}
This example uses the /email/hard_bounces endpoint.

__Before: API Key in Request Body__
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key=YOUR-REST-API-KEY&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
```
__Now: API Key in Header__
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endtab %}
{% tab POST Request %}
This example uses the /user/track endpoint.

__Before: API Key in Request Body__
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key": YOUR-API-KEY-HERE ,
	"attributes": [ 
 	{
 	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
__Now: API Key in Header__
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
	"attributes": [ 
 	{
	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
{% endtab %}
{% endtabs %}
{% enddetails %}


