---
nav_title: Connected Content Retries
platform: Message_Building_and_Personalization
subplatform: Personalization
page_order: 4
---

# Connected Content Retries

{% raw %}

Because Connected Content relies on receiving data from APIs, there is the possibility that an API is intermittently unavailable while Braze makes the call. In this case, Braze supports retry logic to re-attempt the request using exponential backoff. To enable retries, add `:retry` in the Connected Content call, as shown below:

```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```

If the API call fails and this is enabled, Braze will retry the call while respecting the [rate limit][47] you set for each resend. Braze will move any failed messages to the "back of the queue" and add additional minutes, if necessary, to the total minutes it would take to send your message.

Please note that if a retried attempt succeeds, the message is sent and no further retries are attempted for that message. If the Connected Content call errors out 5 times, the message is aborted similar to if an [abort message tag][1] was triggered.

Connected Content `:retry` is available in webhooks, emails, and push notifications.

{% endraw %}

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
[26]: http://factual.com/products/cpg
[27]: http://blog.clearbit.com/logo
[28]: http://api.tfl.gov.uk/#Line
[29]: http://datamine.mta.info/
[30]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
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
[47]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting
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
[60]: {% image_buster /assets/img_archive/Accuweather_APIKey2.png %}
[61]: https://developer.accuweather.com/weather-icons
[62]: {{ site.baseurl }}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
