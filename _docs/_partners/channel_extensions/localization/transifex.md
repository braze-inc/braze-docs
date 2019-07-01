---
nav_title: Transifex
alias: /partners/transifex/
---

# About Transifex

Transifex enables powerful localization across your user base, no matter what the language is. Transifex and Braze's Connected Content feature empower you to automate translation so your teams are freed up to focus on delivering brilliant customer experiences.

# Pre-Requisites

| Requirement| Origin| Access| Description|
| ---| ---| ---|
|Transifex Account | Transifex | https://www.transifex.com/signin/ | You must first have a Transifex account to access their SDK integration information. |

Set up basic authentication for your account in the __Connected Content__ tab in __Manage App Group__.

![Basic Authentication Credential Management][34]

Click __New Credential__. You can then name your credential and put in your username and password for that account.

![Basic Authentication Credential Creation][35]

You can then use this basic authentication credential for calls to Transifex.

# SDK Integration

This integration will allow you to type in a source string instead of copying and pasting the translation for every language into the message composer.

The code for our Transifex integration was built using Transifex's translation [strings API][31].

The following CURL will allow you to see if your Transifex account has context values associated with translations:

```
curl -i -L --user username:password -X GET https://www.transifex.com/api/2/project/<project_name>/resource/<resource_name>/translation/en/strings
```

Input the project and resource name into CURL. You can find these values in the URL of your Transifex account.

![Transifex_account][32]

An example response with a blank context field is pictured below:

![terminal_response][33]

## Transifex Integration Code Example

Here is example code which utilizes the Transifex Strings API and the user's "language" attribute.

{% raw %}
```
{% assign key = "<Insert Key Here>" %}
{% assign context = "<Insert Context Here>" %}
{% assign source_string = key | append: ':' | append: context %}
{% assign project = "<Insert Project Name Here>" %}
{% assign resource = "<Insert Resource Name Here" %}
{% assign source_hash = source_string | md5 %}

{% if {{${language}}} == "en" or {{${language}}} == "it" or {{${language}}} == "de" or {{${language}}} == "another_language_you_support"  %}
{% connected_content https://www.transifex.com/api/2/project/{{project}}/resource/{{resource}}/translation/{{${language}}}/string/{{source_hash}}/ :basic_auth <Insert Basic Auth Credential Name Here> :save strings %}
{% endif %}

{% if {{strings}} != null and {{strings.translation}} != "" and {{${language}}} != null %}
  {{strings.translation}}
{% else %}
  {% abort_message('null or blank') %}
{% endif %}
```

You can also leverage the user's `{{${most_recent_locale}}}` if you want to include a variation based upon a user's specific version of a language such as `zh_CN` or `pt_BR`.

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
