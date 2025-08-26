---
nav_title: Postman and sample requests
article_title: Postman and Sample Requests
page_order: 3
description: "This reference article covers the Braze Postman Collection, what it is, how to set up and use the collection, as well as how to edit and send requests."
page_type: reference

---

# Postman and sample requests

> Braze allows you to generate sample API requests for all of our endpoints through our Postman Collection. This reference article covers the Braze Postman Collection, what it is, how to set up and use the collection, as well as how to edit and send requests.

## What is Postman?

Postman is a free-to-use visual editing tool for building and testing API requests. As opposed to other methods for interacting with APIs (for example, using cURL), Postman allows you to easily edit API requests, view header information, and much more. Postman has the ability for you to save Collections or libraries of sample pre-made API requests. To make it easy for our customers to get up and running with our REST API, we created a Collection with pre-made examples for all of our API endpoints.

View or download our Postman Collection by clicking **Run in Postman** in our [Postman docs](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) to get started.

## Using the Braze Postman collection

If you have a Postman account (you can download macOS, Windows, and Linux versions from the [Postman website](https://www.getpostman.com)), you can open our Postman documentation in your own Postman app by clicking the orange **Run in Postman** button. You can then [create an environment](#setting-up-your-postman-environment), or use our Braze REST API environment as a template, and edit the available `POST` and `GET` requests to suit your own needs.

### Setting up your Postman environment

{% raw %}
The Braze Postman Collection uses a templating variable, `{{instance_url}}`, to substitute the REST API URL of your Braze instance into the pre-built requests, and the `{{api_key}}` variable for your API Key. Rather than having to manually edit all requests in the Collection, you can set up this variable in your Postman environment. You can either select our templated environment (Braze REST API Environment Template) from the dropdown and replace the variable values with your own, or you can set up your own environment.
{% endraw %}

To set up your own environment, perform the following steps:

1. From the **Workspaces** tab, select **Environments**.
2. Click the **+** plus button to create a new environment.
3. Give this environment a name (for example, "Braze API Requests") and add keys for `instance_url` and `api_key` with values corresponding to your [Braze instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) and [Braze REST API Key]({{site.baseurl}}/api/api_key/).
4. Click **Save**.

{% alert note %}
In `POST` request bodies, the `api_key` should be encapsulated in quotes: `"MY-API-KEY-EXAMPLE"`. In `GET` URLs, it should not be. We have already provided this formatting for you in this documentation's `POST` request bodies, `GET` URLs, and environment template for `YOUR-API-KEY-HERE`.
{% endalert %}

![Adding variables for API key and instance URL to the Braze REST API environment in Postman.]({% image_buster /assets/img_archive/postman_variable.png %})

### Using the pre-built requests from the collection

After you have configured your environment, you can use any of the pre-built requests in the collection as a template for building new API requests. To start using one of the pre-built requests, click on it within the **Collections** menu of Postman. This will open the request as a new tab in the main window of the Postman app.

In general, there are two types of requests that Braze API endpoints accept - `GET` and `POST`. Depending on which `HTTP` method the endpoint uses, you'll need to edit the pre-built request differently.

#### Edit a POST request

When editing a `POST` request, open the request and navigate to the **Body** section in the request editor. For readability, select the **raw** radio button to format the `JSON` request body.

![Body tab when editing a POST User Track request in Postman]({% image_buster /assets/img_archive/postman_post.png %})

#### Edit a GET request

When editing a `GET` request, edit the parameters passed in the request URL. To do so, select the **Params** tab and edit the key-value pairs in the fields that appear.

![Params tab when editing a GET Query List of Unsubscribed Email Addresses request in Postman.]({% image_buster /assets/img_archive/postman_get.png %})

### Send your request

After your API request is ready, click **Send**. The request sends and the response data populates in a section underneath the request editor. From here, you can view the raw data returned from the Braze API, see the HTTP response code, see how long the request took to process, and view header information.

![Example body response data from a POST request with a status of 201 Created and response time of 269 milliseconds.]({% image_buster /assets/img_archive/postman_response.png %})

