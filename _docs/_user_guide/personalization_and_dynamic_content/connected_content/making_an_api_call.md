---
nav_title: Making an API Call
platform: Message_Building_and_Personalization
subplatform: Personalization
page_order: 0
description: "This reference article covers how to make an Connected Content API call, as well as helpful examples and advanced Connected Content use cases."
---

# Making an API Call

{% raw %}

Messages sent by Braze can retrieve content from a web server to be included in a message by using the `{% connected_content %}` tag. Using this tag, you can assign or declare variables by using `:save`. Aspects of these variables can be referenced later in the message with [Liquid][2]. For example, the following message body will access the url `http://numbersapi.com/random/trivia` and include a fun trivia fact in your message:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is fun some trivia for you!: {{result.text}}
```

You can also include user profile attributes as variables in the URL string when making Connected Content requests. As an example, you may have a web service that returns content based on a user's email address and ID. If you're passing attributes containing special characters, such as @, make sure to use the Liquid filter `url_param_escape` to replace any characters not allowed in URLs with their URL-friendly escaped versions, as shown in the e-mail address attribute below.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```

If the URL is unavailable, Braze will render an empty string in its place. Because Braze delivers messages at a very fast rate, be sure that your server can handle thousands of concurrent connections so we do not overload your server when pulling down content. When using public APIs, ensure your usage will not violate any rate-limiting that the API provider may employ. Braze requires that server response time is less than 2 seconds for performance reasons; if the server takes longer than 2 seconds to respond, the content will not be inserted.

If the endpoint returns JSON, you can detect that by checking if the `connected` value is null, and then [conditionally abort the message][1]. Braze only allows URLs that communicate over port 80 (HTTP) and 443 (HTTPS).
{% endraw %}

{% alert note %}
* Attribute values must be surrounded by `${}` in order to operate properly within Braze's version of Liquid Syntax.
* Connected Content calls will happen at the time the message is sent, with the exception of In-App Messages, which will make this call at the time the message is viewed.
* Connected Content calls do not follow redirects.
* Braze's systems may make the same Connected Content API call more than once per recipient. That is because Braze may need to make a Connected Content API call to render a message payload, and message payloads can be rendered multiple times per recipient for the purposes of validation, retry logic, or other internal purposes. Your systems should be able to tolerate the same Connected Content call being made more than one time per recipient.
{% endalert %}

{% raw %}
## Using Basic Authentication

If the URL requires basic authentication, Braze can generate a basic authentication credential for you to use in your API call. In the Connected Content tab in Manage App Group, you can manage existing basic authentication credentials and add new ones.

![Basic Authentication Credential Management][34]

To add a new credential, click Add Credential. You can then name your credential and put in the username and password.

![Basic Authentication Credential Creation][35]

You can then use this basic authentication credential in your API calls by referencing the token's name:

```
Hi there, here is fun some trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```

>  If you delete a credential, keep in mind that any Connected Content calls trying to use it will be aborted.

{% endraw %}

## Using Token Authentication 

When making use of Braze's Connected Content, you may find that certain APIs require a token instead of a username and password. Included below is a code snippet to reference and model your messages off of. 

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://your_API_link_here/
     :method post
     :headers {
       "X-App-Id": "YOUR-APP-ID",
       "X-App-Token": "YOUR-APP-TOKEN"
 	}
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

## Connected Content IP Whitelisting

When a message using Connected Content is sent from Braze, the Braze servers automatically make network requests to our customers’ or third parties’ servers to pull back data.  

With IP whitelisting, you can verify that Connected Content requests are actually coming from Braze, adding an additional layer of security.

Braze will send Connected Content requests from the IP ranges below. Braze has a reserved a set of IPs that are used for all services, not all of which are active at a given time.  This ensures that if Braze needs to send from a different data center, or do maintenance, Braze can do so without impact to customers. Braze may use one, a subset or all of the IPs listed below when making Connected Content requests.

| For Instances `US-01`, `US-02`, `US-03`, `US-04`, `US-06` and `US-08`: |
|---|
| `23.21.118.191`
| `34.206.23.173`
| `50.16.249.9`
| `52.4.160.214`
| `54.87.8.34`
| `54.156.35.251`
| `52.54.89.238`
| `18.205.178.15`

| For Instance `EU-01`: |
|---|
| `52.58.142.242`
| `52.29.193.121`
| `35.158.29.228`



[1]: #aborting-connected-content
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#liquid-usage-use-cases--overview
[16]: [success@braze.com](mailto:success@braze.com)
[34]: {% image_buster /assets/img_archive/basic_auth_mgmt.png %}
[35]: {% image_buster /assets/img_archive/basic_auth_token.png %}
