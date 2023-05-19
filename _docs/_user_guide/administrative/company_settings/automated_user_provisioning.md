---
nav_title: Automated User Provisioning
article_title: Automated User Provisioning
page_order: 10
page_type: reference
description: "This reference article covers what info you need to provide for automated user provisioning and how and where to use your generated SCIM token."
alias: /scim/automated_user_provisioning/

---

# Automated user provisioning

> Learn what you need to provide for automated user provisioning and how and where to use your generated SCIM token.

To access the **Automated User Provisioning** page, select your account dropdown and go to **Company Settings** > **Automated User Provisioning**.

{% alert note %}
If you're using our [updated navigation]({{site.baseurl}}/navigation), you can find **Automated User Provisioning** under **Settings** > **Company Settings** > **Admin Settings** > **Automated User Provisioning**.
{% endalert %}

## How to get your SCIM token

You will need to provide the following information to get your SCIM token:

1. Select a default workspace for new dashboard developers to be added to. If you do not specify a workspace in the [create users SCIM API call](/docs/post_create_user_account/), they will be added here.
2. Provide a service origin. The service origin is how Braze identifies where the request is coming from.
3. Optionally provide a comma-separated list or range of IP addresses allowed for SCIM requests. The `X-Origin-Request` header in each request will be used to check the request IP address against the allowlist.<br><br>

![][1]

Once you have completed the required fields, you can generate a SCIM token and see your SCIM API endpoint. **This token will only be presented once.** Braze expects all SCIM requests to contain the SCIM API bearer token attached via an HTTP `Authorization` header.

[1]: {% image_buster /assets/img/scim.png %}
