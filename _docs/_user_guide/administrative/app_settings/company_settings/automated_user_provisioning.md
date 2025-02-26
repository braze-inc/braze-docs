---
nav_title: Automated User Provisioning
article_title: Automated User Provisioning
page_order: 10
page_type: reference
description: "This reference article covers what information you need to provide for automated user provisioning and how and where to use your generated System for Cross-domain Identity Management (SCIM) token."
alias: /scim/automated_user_provisioning/

---

# Automated user provisioning

> Learn what you need to provide for automated user provisioning and how and where to use your generated System for Cross-domain Identity Management (SCIM) token and SCIM API endpoint. You can then call this endpoint with your API to automatically provision new dashboard users.

To access this page, go to **Settings** > **Admin Settings** > **SCIM Provisioning**.

{% alert note %}
If you're using the [older navigation]({{site.baseurl}}/navigation), select your account dropdown and go to **Company Settings** > **Automated User Provisioning**.
{% endalert %}

## How to get your SCIM token

You will need to provide the following information to get your SCIM token:

1. Select a default workspace for new dashboard developers to be added to. If you do not specify a workspace in the [create users SCIM API call](/docs/post_create_user_account/), they will be added here.
2. Provide a service origin. The service origin is how Braze identifies where the request is coming from.
3. Optionally provide a comma-separated list or range of IP addresses allowed for SCIM requests. The `X-Origin-Request` header in each request will be used to check the request IP address against the allowlist.<br><br>

{% alert note %}
This SCIM endpoint does not directly integrate with identity providers.
{% endalert %}

![][1]

After completing the required fields, you can generate a SCIM token and see your SCIM API endpoint. **This token will only be presented once.** Braze expects all SCIM requests to contain the SCIM API bearer token attached via an HTTP `Authorization` header.

[1]: {% image_buster /assets/img/scim.png %}
