---
nav_title: Local Connected Content Variables
platform: Message_Building_and_Personalization
subplatform: Personalization
page_order: 1
description: "This reference article covers how to use and store local Connected Content variables."
---

# Local Connected Content Variables

Braze makes a standard GET request at send time to the endpoint specified within the `connected_content` tag. If the endpoint returns JSON, it is automatically parsed and stored in a variable called `connected`.  If the endpoint returns text, it will be directly inserted into the message in place of the `connected_content` tag.

>  If you want to save your response to a variable, it’s recommended to return JSON objects. And if you want the response of Connected Content to replace the tag with the text, make sure the response is not valid JSON (as defined by [json.org][46])

You can also specify `:save your_variable_name` after the url in order to save the data as something else. For example, the following `connected_content` tag will store the response to a local variable called `localweather` (you can save multiple `connected_content` JSON variables):

{% raw %}

```
{% connected_content https://www.metaweather.com/api/location/2459115/ :save localweather %}
```
{% endraw %}

Metaweather is a free weather API that uses a "Where-on-Earth ID" to return weather in an area. Use this code for testing / learning purposes only. For more information about this API, see [here](https://www.metaweather.com/api/ "Metaweather API Details").

>  The stored variable can only be accessed within the field which contains the `connected_content` request. For example, if you wanted to use the `localweather` variable in both the message and title field, you should make the `connected_content` request within both fields. If the request is identical, Braze will use the cached results, rather than making a second request to the destination server. However, Connected Content calls made via HTTP POST do not cache by default and will make a second request to the destination server. If you wish to add caching to POST calls, refer to the "cache_max_age" option below.

### JSON Parsing

Connected Content will interpret any JSON-formatted results into a local variable, when you specify `:save`. For example, a weather-related Connected Content endpoint returns the following JSON object, which you store into a local variable `localweather` by specifying `:save localweather`.
{% raw %}

```js
{
  "consolidated_weather": [
    {
      "id": 5.8143475362693e+15,
      "weather_state_name": "Clear",
      "weather_state_abbr": "c",
      "wind_direction_compass": "WSW",
      "created": "2017-06-12T14:14:46.268110Z",
      "applicable_date": "2017-06-12",
      "min_temp": 22.511666666667,
      "max_temp": 31.963333333333,
      "the_temp": 27.803333333333,
      "wind_speed": 6.8884690250312,
      "wind_direction": 251.62921994166,
      "air_pressure": 1021.335,
      "humidity": 50,
      "visibility": 14.945530601288,
      "predictability": 68
    },
    .
    .
    .
    "title": "New York",
    "location_type": "City",
    "woeid": 2459115,
    "latt_long": "40.71455,-74.007118",
    "timezone": "US\/Eastern"
  }
```

You can test whether or not it's raining by referencing `{{localweather.consolidated_weather[0].weather_state_name}}`, which if used on the object above would return `Clear`. If you want to also personalize with the resulting location name, `{{localweather.title}}` returns `New York`.
{% endraw %}

The following image illustrates the type of syntax highlighting you should see in the dashboard if you're setting things up correctly. It also demonstrates how you could leverage the `connected_content` request above!

![Connected Content Syntax Example][6]

If the API responded with {%raw%}`{{localweather.consolidated_weather[0].weather_state_name}}`{%endraw%} returning `Rain`, the user would then receive this push.

![Connected Content Push Example][17]

By default, Connected Content will set a Content-Type header on a GET HTTP request that it makes to `application/json` with `Accept: */*`. If you require another content type, specify it explicitly by adding `:content_type your/content-type` to the tag. Braze will then set both the Content-Type and Accept header to the type you specify.

{% raw %}
```
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

### HTTP POST

By default, Connected Content makes an HTTP GET request to the specified URL. To make a POST request instead, specify `:method post`.

You can optionally provide a POST body by specifying `:body` followed by a query string of the format `key1=value1&key2=value2&...`. Content-Type defaults to `application/x-www-form-urlencoded` unless you specify `:content_type application/json`, in which case Braze will automatically JSON-encode the body before sending.

{% raw %}
```
{% connected_content https://post.example.com/someEndpoint :method post :body key1=value1&key2=value2 %}
```
{% endraw %}

{% details Query String Serialization Example %}

##### Example POST Body
```json
{
  "sorts": [
    {
      "field": "startdate",
      "direction": "asc"
    }
  ],
  "filters": [
    {
      "field": "startdate",
      "type": "range",
      "rangeFilters": {
        "time_zone": "-07:00",
        "gte": "now+1d/d",
        "lt": "now+2d/d"
      }
    }
  ]
}
```
##### Example POST Body Formatting
{% raw %}
```json
{% connected_content https://example.com/api
  :method post
    :headers {
      "Content-Type": "application/json"
    }  
  :body sorts[0][field]=startdate&sorts[0][direction]=asc&filters[0][field]=startdate&filters[0][type]=range&filters[0][rangeFilters][time_zone]=-07:00&filters[0][rangeFilters][gte]=now+1d/d&filters[0][rangeFilters][lt]=now+2d/d
  :save result %}
```
{% endraw %}
{% enddetails %}

### HTTP Status Codes

You can utilize the HTTP status from a Connected Content call by first saving it as a local variable and then using the `__http_status_code__` key. For example:

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :save result %}
{% if result.__http_status_code__ != 200 %}
  {% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert important %}
This key will only be automatically added to the Connected Content object if the endpoint returns a JSON object. If the endpoint returns an array or other type, then that key cannot be set automatically in the response.
{% endalert %}

### Configurable Caching
Connected Content will cache the value it returns from GET endpoints for a minimum of 5 minutes. If a cache time is not specified, the default cache time is 5 minutes. 

Connected Content cache time can be configured to be longer with `:cache_max_age`, as shown below. The minimum cache time is 5 minutes and the maximum cache time is 4 hours. Connected Content data is cached in-memory using a volatile cache system, such as memcached. As a result, regardless of the specified cache time, Connected Content data may be evicted from Braze's in-memory cache earlier than specified. This means the cache durations are suggestions and may not actually represent the duration that the data is guaranteed to be cached by Braze and you may see more Connected Content requests than you may expect with a given cache duration.

By default, Connected Content does not cache POST calls. You can change this behavior by adding `:cache_max_age` to the Connected Content POST call. 

#### Cache for Specified Seconds

This example will cache for 900 seconds (or 15 minutes).
{% raw %}
```
{% connected_content https://example.com/webservice.json :cache_max_age 900 %}
```
{% endraw %}


#### Cache Busting

To prevent Connected Content from caching the value it returns from a GET request, you can use the `:no_cache` configuration, as shown below. 

{% raw %}
```js
{% connected_content https://example.com/webservice.json :no_cache %}
```
{% endraw %}

{% alert important %}
Be certain the provided Connected Content endpoint can handle large bursts of traffic before using this option, or you will likely see increased sending latency (increased delays or wider time intervals between request and response) due to Braze making Connected Content requests for every single message.
{% endalert %}

With a `POST` you don't need to cache bust, as Braze never caches the results from `POST` requests.

[6]: {% image_buster /assets/img_archive/Connected_Content_Syntax.png %} "Connected Content Syntax Usage Example"
[16]: [success@braze.com](mailto:success@braze.com)
[17]: {% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"
[46]: http://www.json.org
