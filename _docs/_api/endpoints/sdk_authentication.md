---
nav_title: "SDK Authentication"
page_order: 14
layout: api_page

page_type: reference
platform: API
description: "This article outlines details about the SDK authentication endpoints within the Braze REST API."
---

# SDK Authentication API Endpoints

Use these endpoints to create and manage SDK Authentication keys for your workspace.

{% apiref post %}/app_group/sdk_auth_key/create{% endapiref %} Create a new SDK Authentication key for your app.<br><br>
{% apiref get %}/app_group/sdk_auth_keys{% endapiref %} Get all SDK Authentication keys for your app.<br><br>
{% apiref put %}/app_group/sdk_auth_key/primary{% endapiref %} Mark an SDK Authentication key as the primary key.<br><br>
{% apiref delete %}/app_group/sdk_auth_key/delete{% endapiref %} Delete an SDK Authentication key.
