---
nav_title: Automated user provisioning
article_title: Automated User Provisioning
page_order: 10
page_type: reference
description: "This reference article covers what information you need to provide for automated user provisioning and how and where to use your generated System for Cross-domain Identity Management (SCIM) token."
alias: /scim/automated_user_provisioning/

---

# Automated user provisioning

> Use SCIM provisioning to automatically create and manage Braze users through API. This article walks you through what information to provide, how to generate your SCIM token, and where to find your SCIM API endpoint.

## Step 1: Access SCIM privioning settings

In the Braze dashboard, go to **Settings** > **Admin Settings** > **SCIM Provisioning**.

## Step 2: Configure your SCIM settings

To enable SCIM provisioning, provide the following information:

- **Default Workspace:** Select the workspace where new users will be added by default. If you don’t specify a workspace in your [SCIM API request]({{site.baseurl}}/post_create_user_account/), Braze assigns users to this workspace.
- **Service Origin:** Enter the origin domain of your SCIM requests. Braze uses this in the `X-Request-Origin` header to verify where requests are coming from.
- **IP Allowlisting (optional):** You can restrict SCIM requests to specific IP addresses.
Enter a comma-separated list or range of IP addresses to allow. The `X-Request-Origin` header in each request will be used to check the request IP address against the allowlist.

{% alert note %}
This SCIM endpoint does not directly integrate with identity providers.
{% endalert %}

![SCIM Provisioning settings form with three fields: Default Workspace, Service Origin , and optional IP Allowlisting. The “Generate SCIM Token” button is disabled.]({% image_buster /assets/img/scim_unfilled.png %})

## Step 3: Get your SCIM token and endpoint

After completing the required fields, press **Generate SCIM token** to generate a SCIM token and see your SCIM API endpoint. Make sure to copy the SCIM token before you navigate away. **This token will only be presented once.** 

![SCIM API Endpoint and SCIM Token fields displayed with masked values and copy buttons. Below the token field is a “Reset Token” button.]({% image_buster /assets/img/scim.png %})

Braze expects all SCIM requests to contain the SCIM API bearer token attached via an HTTP `Authorization` header.

