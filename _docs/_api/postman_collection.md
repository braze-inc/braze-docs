---
nav_title: Postman & Sample Requests
article_title: Postman & Sample Requests
page_order: 3
description: "This reference article covers the Braze Postman Collection, what it is, how to set up and use the collection, as well as how to edit and send requests."
page_type: reference

---

# Sample API Requests

> Braze allows you to generate sample API requests for all of our endpoints via our Postman Collection. This reference article covers the Braze Postman Collection, what it is, how to set up and use the collection, as well as how to edit and send requests.

## What is Postman?

Postman is a free-to-use visual editing tool for building and testing API requests. As opposed to other methods for interacting with APIs (e.g. using cURL), Postman allows you to easily edit API requests, view header information, and much more. Postman has the ability for you to save Collections or libraries of sample pre-made API requests. To make it easy for our customers to get up and running with our REST API, we created a Collection with pre-made examples for all of our API endpoints.

You can see or [download our Postman Collection here.](https://www.getpostman.com/collections/29baa41d7ba930673ef0)

# Using Braze's Postman Collection

If you have a Postman account (macOS, Windows, and Linux versions can be downloaded from their website located [here][1]), you can open our Postman documentation in your own Postman app (click the orange `Run in Postman` button below). You can then [create an environment](#setting-up-your-postman-environment), or use our Braze REST API environment as a template, and edit the available   `POST` and `GET` requests to suit your own needs.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/29baa41d7ba930673ef0?action=collection%2Fimport)

## Setting Up Your Postman Environment

{% raw %}
The Braze Postman Collection uses a templating variable, `{{instance_url}}`, to substitute the REST API URL of your Braze instance into the pre-built requests and the `{{api_key}}` variable for your API Key. Rather than having to manually edit all requests in the Collection, you can set up this variable in your Postman environment. You can either select our templated environment (Braze REST API Environment Template) from the dropdown and replace the variable values with your own, or you can set up your own environment.
{% endraw %}

To set up your own, please follow the steps below:

1. Click on the gear icon in the top right corner of your Postman app.
2. Select "Manage Environments" to open a modal window that displays your active environments.
3. In the bottom right corner of the modal window, click "Add" to create a new environment.
4. Give this environment a name (e.g. "Braze API Requests") and add keys for `instance_url` and `api_key` with values corresponding to [your Braze instance][7] and [Braze REST API Key][8], as pictured below.

{% alert note %}
In `POST` request bodies, the `api_key` should be encapsulated in quotes: `"MY-API-KEY-EXAMPLE"`. In `GET` URLs, it should not be. We have already provided this formatting for you in this documentation's `POST` request bodies, `GET` URLs, and environment template for `YOUR-API-KEY-HERE`.
{% endalert %}

![Adding environment variables][3]

## Using the Pre-Built Requests from the Collection

Once you have configured your environment. You can use any of the pre-built requests in the collection as a template for building new API requests. To start using one of the pre-built requests, simply click on it within the 'Collections' menu on the left side of Postman. This will open the request as a new tab in the main window of the Postman app.

In general, there are two types of requests that Braze's API endpoints accept - `GET` and `POST`. Depending on which `HTTP` method the endpoint uses, you'll need to edit the pre-built request differently.

### Edit a POST Request

When editing a `POST` request, you'll need to open the request and navigate to the `Body` section in the request editor. For readability, select the `raw` radio button to format the `JSON` request body.

![Editing a POST request][4]

### Edit a GET Request

When editing a `GET` request, you will need to edit the parameters passed in the request URL. To edit these easily, select the `Params` button next to the URL bar and edit the key-value pairs in the fields that will appear below the URL bar.

![Editing a GET request][5]

## Send Your Request

Once your API request is ready to send, click on the 'Send' button next to the URL bar. The request will be sent and the response data will be populated in a section underneath the request editor. From here, you can view the raw data returned from Braze's API, see the HTTP response code, see how long the request took to process, and view header information.

![Response Data][6]

[1]: https://www.getpostman.com
[3]: {% image_buster /assets/img/postman_variable.png %}
[4]: {% image_buster /assets/img_archive/postman_post.png %}
[5]: {% image_buster /assets/img_archive/postman_get.png %}
[6]: {% image_buster /assets/img_archive/postman_response.png %}
[7]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[8]: {{site.baseurl}}/api/api_key/
