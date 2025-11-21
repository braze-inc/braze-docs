{% if include.section == "default behavior" %}

By default, Connected Content will set a `Content-Type` header on a GET HTTP request that it makes to `application/json` with `Accept: */*`. If you require another content type, specify it explicitly by adding `:content_type your/content-type` to the tag. Braze will then set both the Content-Type and Accept header to the type you specify.

{% raw %}
```js
{% connected_content http://numbersapi.com/random/trivia :content_type application/json %}
```
{% endraw %}

{% endif %}

{% if include.section == "http post" %}

By default, Connected Content makes an HTTP GET request to the specified URL. To make a POST request instead, specify `:method post`.

You can optionally provide a POST body by specifying `:body` followed by either a query string of the format `key1=value1&key2=value2&...` or a reference to captured values. Content-Type defaults to `application/x-www-form-urlencoded`. If you specify `:content_type application/json` and provide a form-urlencoded body such as `key1=value1&key2=value2`, Braze will automatically JSON-encode the body before sending.

Connected Content also does not cache POST calls by default. You can update this behavior by adding `:cache_max_age` to the Connected Content POST call.

{% tabs %}
{% tab Default content-type %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 %}
```
{% endraw %}

{% endtab %}
{% tab Application/JSON Content-Type %}

{% raw %}
```js
{% connected_content https://example.com/api/endpoint :method post :body key1=value1&key2=value2 :content_type application/json %}
```
{% endraw %}

{% endtab %}
{% endtabs %}


{% endif %}