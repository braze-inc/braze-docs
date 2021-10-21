---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "This article outlines the partnership between Braze and Lob.com, which allows you to send direct mail like letters, postcards, and checks through the mail."
page_type: partner
search_tag: Partner

---

# Lob direct mail automation

> [Lob.com][38] is an online service which one can interact with through their API to send direct mail like letters, postcards, and checks through the mail.  

You can access Lob's services through Braze's webhook feature and send mail to your users.  To get started, sign up for an account on Lob.com and locate your API key in the settings section under your name in the dashboard.

![Lob API Key][33]

## HTTP url

The HTTP URL to request in the webhook is different for each action you can make to Lob. In this example we will be sending a postcard so the URL is https://api.lob.com/v1/postcards, however, the list of all the HTTP URL endpoints can be found in the [Lob documentation][39].

![Lob Endpoints][37]

## Request body

To specify an address in the webhook body requires nested objects, and as such it must be entered as "Raw Text" in JSON format.  If you are unfamiliar with the JSON format, an easy way to generate a sample request body is to copy the example CURL requests given on the Lob.com documentation and run it in your terminal (replacing their test API key with yours).  Once you run the code in the terminal, go to the Lob.com dashboard and check the "Logs" tab found under the "Requests" title.  If the API request worked, you will be able to click on the request and copy the request body into the dashboard.  You can then replace the data in the file to fit your desires.

![Lob Success Response][34]

## Request headers and method

Lob's documentation states that you must include your API key in the header to authorize the request.  To do so, simply navigate to the setting section and add a new pair.  For an authentication header, set the key to "Authorization".  Lob expects your API key to be base64 encoded, so use the Base64 filter in the header value: Basic {{'APIkey:' | base64_encode}}. You will need to add a ":" to the end of your API key when encoding as [Lob][40] expects the password to be left blank. Because the body of the request is in JSON format, you will also need to add a "Content-Type" key with the value "application/json".  The request method for this webhook is POST as specified on Lob's documentation.

![Lob Preview][35]

## Preview your request

At this point, your campaign should be ready to send. If you run into errors, check the Lob dashboard and the developer console error message logs found in the Braze dashboard.  Using these two resources you should be able to troubleshoot and debug your request. For example, the error below is caused by an incorrectly formatted authentication header.

![Error Log Message][36]

[33]: {% image_buster /assets/img_archive/lob_api_key.png %}
[34]: {% image_buster /assets/img_archive/lob_success_response.png %}
[35]: {% image_buster /assets/img_archive/lob_full_request.png %}
[36]: {% image_buster /assets/img_archive/error_log.png %}
[37]: {% image_buster /assets/img_archive/lob_api_endpoint.png %}
[38]: https://lob.com
[39]: https://lob.com/docs#intro
[40]: https://lob.com/docs#auth
