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

>  The stored variable can only be accessed within the field which contains the `connected_content` request. For example, if you wanted to use the `localweather` variable in both the message and title field, you should make the `connected_content` request within both fields. If the request is identical, Braze will use the cached results, rather than making a second request to the destination server. However, Connected Content calls made via HTTP POST do not cache and will make a second request to the destination server.

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

If the API responded with `{{localweather.consolidated_weather[0].weather_state_name}}` returning `Rain`, the user would then receive this push.

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
Connected Content will cache the value it returns from GET endpoints for a minimum of 5 minutes.

If a cache time is not specified, the default cache time is 5 minutes. However, this cache time can be configured to be longer with `:cache_max_age`, as shown below. The maximum cache time is 4 hours.

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

[1]: #aborting-connected-content
[6]: {% image_buster /assets/img_archive/Connected_Content_Syntax.png %} "Connected Content Syntax Usage Example"
[7]: http://openweathermap.org/api
[8]: http://developer.nytimes.com/docs/read/article_search_api_v2
[9]: http://open-platform.theguardian.com/documentation/
[10]: http://alchemyapi.readme.io/v1.0/docs/introduction
[11]: http://platform.seatgeek.com/
[12]: http://developer.tmsapi.com/docs/read/data_v1_1/movies/movie_showtimes
[13]: http://www.bandsintown.com/api/overview
[14]: http://www.last.fm/api
[15]: http://developer.ebay.com/devzone/shopping/docs/concepts/shoppingapiguide.html
[16]: [success@braze.com](mailto:success@braze.com)
[17]: {% image_buster /assets/img_archive/connected_weather_push2.png %} "Connected Content Push Usage Example"
[18]: http://numbersapi.com/
[19]: http://developer.eventbrite.com/
[20]: http://api.eventful.com/
[21]: http://www.discogs.com/developers/
[22]: http://www.songkick.com/developer
[23]: http://www.enclout.com/api/v1/yahoo_finance
[24]: http://www.apple.com/itunes/affiliates/resources/documentation/itunes-store-web-service-search-api.html
[25]: http://www.semantics3.com/products/pull
[27]: http://blog.clearbit.com/logo
[28]: http://api.tfl.gov.uk/#Line
[29]: http://datamine.mta.info/
[30]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[31]: https://docs.transifex.com/api/translation-strings
[32]: {% image_buster /assets/img_archive/TransifexUI.png %}
[33]: {% image_buster /assets/img_archive/terminal.png %}
[34]: {% image_buster /assets/img_archive/basic_auth_mgmt.png %}
[35]: {% image_buster /assets/img_archive/basic_auth_token.png %}
[36]: https://www.barchartondemand.com/free
[37]: https://www.coindesk.com/api/
[38]: http://developer.ticketmaster.com/products-and-docs/apis/getting-started/
[39]: https://sunrise-sunset.org/api
[40]: http://www.brewerydb.com/
[41]: https://developers.zomato.com/api
[42]: https://airvisual.com/api
[43]: https://developer.nutritionix.com/
[44]: https://open.fda.gov/api/
[45]: https://ndb.nal.usda.gov/ndb/doc/index
[46]: http://www.json.org
[47]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting
[48]: https://developer.accuweather.com/accuweather-locations-api/apis
[49]: https://developer.accuweather.com/accuweather-forecast-api/apis
[50]: https://developer.accuweather.com/accuweather-current-conditions-api/apis
[51]: https://developer.accuweather.com/accuweather-indices-api/apis
[52]: https://developer.accuweather.com/accuweather-weather-alarms-api/apis
[53]: https://developer.accuweather.com/accuweather-alerts-api/apis
[54]: https://developer.accuweather.com/accuweather-imagery-api/apis
[55]: https://developer.accuweather.com/accuweather-tropical-api/apis
[56]: https://developer.accuweather.com/accuweather-translations-api/apis
[57]: https://developer.accuweather.com
[58]: https://developer.accuweather.com/user/me/apps
[59]: https://developer.accuweather.com/weather-alarm-thresholds
[61]: https://developer.accuweather.com/weather-icons
[62]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
