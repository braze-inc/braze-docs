---
nav_title: API endpoint documentation guidelines
article_title: API Endpoint Documentation Guidelines
description: "Guidelines for documenting Braze API endpoints."
page_order: 3
noindex: true
---

# API endpoint documentation guidelines

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

> In general, documentation for API endpoints should follow the guidelines indicated in the [General guidelines]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#general-guidelines). However, there are niche topics that may require different content guidelines listed in this document. 

Braze supports the following REST API methods:

* GET  
* DELETE  
* PATCH  
* POST  
* PUT

## Creating a new endpoint article

When creating a new endpoint article, be sure to also add this endpoint into the [Braze API guide]({{site.baseurl}}/api/home) so that the endpoint is searchable. Navigate to  **`_docs`** folder  **`> _api`** folder **`> home.md`** file to add the endpoint by its path and a one-sentence description.

## Referencing endpoints

In general, there isn't a clear convention for referring to endpoints in documentation. When referring to Braze endpoints, use your best judgment to determine how to refer to an endpoint depending on your use case. 

You can refer to an endpoint by its path (for example, `/users/track`) or by the endpoint's name appended with the word "endpoint" (for example, the track user endpoint). If you find that your path is especially long, refer to the endpoint name instead. 

Use sentence styling when referring to the endpoint by its name. Use code text when referring to the endpoint by its path.

Don't capitalize the word "endpoint" unless directly referring to a section name. Don't include the word "API" when directly referencing an endpoint. 

There are instances where an endpoint is referred to as an API. For example, this is an accurate statement: "Braze uses a REST API with many endpoints" when speaking generally about Braze endpoints.

Don't put quotation marks around the endpoint name. Don't use plain text when referring to the path.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Use the Generate preference center URL endpoint to complete the next steps.</td><td style="width: 50%;">Use <code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code> to complete the next steps.</td></tr>
<tr><td style="width: 50%;">Use the <code>/users/track</code> endpoint.</td><td style="width: 50%;">Use the "Users Track" API endpoint.</td></tr>
</tbody>
</table>
{:/}

### Linking to endpoint articles

When referencing endpoint articles, be sure to use [meaningful link text]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#writing-links) that can make sense out of context. If you're using the endpoint's path as a link, be sure to provide details in the surrounding text as the path may not clearly communicate the endpoint's function.    

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Delete user profiles using the Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user endpoint</a>.</td><td style="width: 50%;">Delete user profiles using the Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user</a> endpoint.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code> endpoint</a></td><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a> endpoint</td></tr>
</tbody>
</table>
{:/}

## Headings

The introduction of an endpoint article must include the following information:

* Request type and endpoint path URL  
* A brief description of the endpoint, starting with "Use this endpoint to…"  
* "See me in Postman" link  
* A note alert with the required REST API key permission

Use this checklist to ensure that the proper headings (and content) are included in each endpoint article and in the listed sequence. Note that there may be subheadings unique to an endpoint, such as different types of example requests.

* Rate limit  
* Path parameters  
* Request body  
* Request parameters  
* Example request  
* Response parameters  
* Example response  
* Troubleshooting (if applicable)

Refer to [Headings and titles]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#headings-and-titles) for formatting guidelines. 

### Path parameters

If there are path parameters for the endpoint, include a Path parameters header and table (similar to the Request parameters table)

If there are no path parameters for the endpoint, include a Path parameters header and the following callout: "There are no path parameters for this endpoint."

If there are no path or request parameters for the endpoint, merge the caveat into the same section as shown below.

{% raw %}
{::nomarkdown}
<div style="margin-left: 2em;">
<code>
## Path and request parameters <br>
There are no path or request parameters for this endpoint.
</code>
</div>
{:/}
{% endraw %}

## Naming conventions

Start each endpoint name with an active verb after its method. This lets users know the function of the endpoint immediately. 

Don't use the API method as the leading verb for the endpoint name.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">POST: Create new user alias</td><td style="width: 50%;">POST: New user alias</td></tr>
<tr><td style="width: 50%;">GET: Look up an existing dashboard user account</td><td style="width: 50%;">GET: Existing dashboard user account</td></tr>
</tbody>
</table>
{:/}

Exceptions to this naming convention are the endpoints in the [Export section]({{site.baseurl}}/api/endpoints/export) as the section name is a verb that indicates that the listed information can be exported.

## API key permissions

API key permissions are permissions you can assign a user or group to limit their access to certain API calls. For each endpoint documentation, include the following callout after the Postman documentation link: 

> To use this endpoint, you must generate an API key with the `permission_name_here` permission.

To find the full list of API key permissions, go to **Settings > API Keys** under **Setup and Testing** in the Braze dashboard. Select an API key with full access (the key name usually includes the phrase "full access"). Each permission name should generally match the endpoint name.

Note that SCIM endpoints do not have listed API key permissions since they're specific to the SCIM integration that occurs outside of the developer console. 

## Rate limits

In general, your rate limit should specify the number of requests and the allotted time. 

Be mindful of endpoints that share a total rate limit. For example, all asynchronous catalog item endpoints share a total rate limit, so it's important to indicate that in the respective articles.

### How to update rate limit file

If your endpoint documentation requires updating or listing a new rate limit, go to **_docs > _api > api_limits.md** to make edits to the rate limit.

## Parameters

Define both the request and response parameters in two separate tables.  These tables should contain the following columns:

* **Parameter**  
* **Required**  
* **Data Type**  
* **Description**

When directly referring to an endpoint's parameters and when listing the values in the **Parameters** column, use code text. When listing the values in the **Required**, **Data Type**, and **Description** columns, use initial caps. 

### Placeholder text

For placeholder text, use curly brackets with a brief description of what the user should include. 

For API key placeholders, use `YOUR_REST_API_KEY`, not `YOUR-REST-API-KEY`.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Do</th><th style="width: 50%;">Don't</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code></td><td style="width: 50%;"><code>/preference_center/v1/[preferenceCenterExternalId]</code></td></tr>
<tr><td style="width: 50%;"><code>/scim/v2/Users/{userId}</code></td><td style="width: 50%;"><code>/url/[userId]/scim/v2/Users/userID</code></td></tr>
</tbody>
</table>
{:/}

For API key placeholders, use `YOUR_REST_API_KEY` (with underscores), not `YOUR-REST-API-KEY` (with hyphens).

## Requests and responses

An API request includes the header and request parameters. The request parameters should be formatted like this:

```bash
parameter": (required/optional, data type) A brief description
```

Here's an example of a request body for the [Create new user alias endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/):

```bash
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "user_aliases": (required, array of new user alias object)
}
```

Use double straight quotation marks (" ") to identify parameters that are strings or arrays in an example request. Ensure that all open brackets and parentheses are closed.

An API response includes the response body, headers, and the HTTP status code. Always include an example response. This example must include a simple text example that describes the parameter. Here's an example response for the [Update user alias endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/#example-request).

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

### Status and error codes 

Status codes indicate whether a user's specific request has been successfully completed. It can be helpful to include the status codes for users to know what's considered a success. For example, 400 and 404 can be indicators of an error response for the endpoint.

If your endpoint documentation requires listing out error codes, link out to the [API Error and Responses]({{site.baseurl}}/api/errors/) article instead at **_docs** folder  **> _api** folder **> errors.md** file

## Sample code

Sample code, like sample requests and responses, should be able to be copied and used with minimal work. With the exception of placeholder text (for example, the API key in the header), example requests should work as-is. Use Postman to ensure that your request is formatted correctly. 

### Beautify versus minified code

If the endpoint's request contains a body, beautify the example in Postman. This makes it easier for developers learning Braze conventions to understand each piece of the request.  

If the endpoint's request body is very short or does not contain a body, minify the request so that unnecessary whitespace is removed. Use a tool like [JSON Minifier](https://codebeautify.org/jsonminifier) to do this. 

### Inline comments

Use two forward slashes (//) to indicate single-line comments in example code. 

Inline comments are valuable tools to call a user's attention to a specific section of code, explain the function of a code block, or provide additional context. 

Use inline comments to quickly show where a user's logic layer would be placed and how it would reference the SDK code. Use simple but realistic examples. For example, an example attribute of "favorite_movie" is stronger than "example_attribute." Even if the user's business doesn't track or care about an end user's favorite movie, this example shows the *sorts* of use cases that might be tracked through this attribute. Generic examples fail to elicit the same intuitive understanding.

Avoid inline comments that simply restate human-readable code or method names. Instead, use a variety of synonyms for the Braze-specific methods and parameters to provide scaffolding for non-native English speakers. 

In general, adhere to standard English conventions when providing inline comments. For example, begin sentences with a capital letter, spell out words completely, and so on.

## Additional resources

- [Google developer documentation style guide](https://developers.google.com/style)  
  - [API reference code and comments](https://developers.google.com/style/api-reference-comments)
