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

## Accessing SCIM provisioning settings

1. In the Braze dashboard, go to **Settings** > **Admin Settings** > **SCIM Provisioning** and add an identity provider.
2. In the **Braze provisioning** step, select a proivisioning method and provide access settings.

![A page to set up the SCIM integration with sections for selecting a provisioning method and providing access settings.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3. In the **IdP configuration** step, follow the steps within the platform for your selected provisioning method.

{% tabs %}
{% tab Okta - Braze app %}

## Step 1: Setup SCIM provisioning

1. Enable SCIM:
    1.1. Go to your Braze app in Okta.
    1.2. Select the **General** tab.
    1.3. In the **App Settings** section, click **Edit**.
    1.4. In the **Provisioning** field, select **SCIM**, and then click **Save**.
2. Setup SCIM integration:
    2.1. Select the **Provisioning** tab.
    2.2. In **Settings** > **Integration** > **SCIM Connection** click **Edit** and fill in the field values that populate within the table in Braze.
3. Test the API credentials by selecting **Test API Credentials**. A verification message will appear if the integration is successful and you can save.
4. Enable provisioning to app
    4.1. In **Provisioning** > **Settings** > **To App** > **Provisioning to App**, click **Edit**.
    4.2. Enable the following:
        - Create Users
        - Update Users Attributes
        - Deactivate Users
    4.3. Review and configure the **Attribute Mapping** section with the mappings that populate within the table in Braze.

## Step 2: Assign users to the app

1. Select the **Assignment** tab.
2. Click **Assign** and select an option.
3. Assign the app to the people that should have access to Braze.
4. Click **Done** when you’ve completed the assignment.

![SCIM provisioning setup for the Okta Braze app.]({% image_buster /assets/img_archive/okta_braze_app.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Okta - Custom app integration %}

## Step 1: Setup SCIM provisioning

1. Enable SCIM:
    1.1. Go to your Braze app in Okta.
    1.2. Select the **General** tab.
    1.3. In the **App Settings** section, click **Edit**.
    1.4. In the **Provisioning** field, select **SCIM**, and then click **Save**.
2. Setup SCIM integration:
    2.1. Select the **Provisioning** tab.
    2.2. In **Settings** > **Integration** > **SCIM Connection** click **Edit** and fill in the field values that populate within the table in Braze.
3. Test the API credentials by selecting **Test API Credentials**. A verification message will appear if the integration is successful and you can save.
4. Enable provisioning to app
    4.1. In **Provisioning** > **Settings** > **To App** > **Provisioning to App**, click **Edit**.
    4.2. Enable the following:
        - Create Users
        - Update Users Attributes
        - Deactivate Users
    4.3. Review and configure the **Attribute Mapping** section with the mappings that populate within the table in Braze.

## Step 2: Assign users to the app

1. Select the **Assignment** tab.
2. Click **Assign** and select an option.
3. Assign the app to the people that should have access to Braze.
4. Click **Done** when you’ve completed the assignment.

![SCIM provisioning setup for the Okta Braze custom integration.]({% image_buster /assets/img_archive/braze_okta_custom.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Entra ID %}

## Step 1: Setup SCIM provisioning app

1. Log into your Microsoft Entra admin center.
2. Create and setup your SCIM app:
    2.1. In the left menu, go to **Entra ID** > **Enterprise apps**.
    2.2. Select **New application**.
    2.3. Select **Create your own application**.
    2.4. In the right panel, input a name for your app.
    2.5. In the **What are you looking to do with your application?** section, select **Integrate application you don't find in the gallery (Non-gallery)**.
    2.6. Click **Create**.
3. Setup SCIM integration:
    3.1. Go to the **Manage** > **Provisioning** section of your SCIM application.
    3.2. Select **Connect** your application or **New configuration** and fill in the following field values that populate within the table in Braze.
4. Enable provisioning to app:
    4.1. Go to the **Manage** > **Attribute mapping (Preview)** section of your SCIM application.
    4.2. Select **Provision Microsoft Entra ID Users**.
    4.3. Review and configure the **Attribute Mapping** section to match the attributes that populate within the table in Braze.
    4.4. Close the **Attribute Mapping** page when you are done.

## Step 2: Assign users to the app

1. Go to **Manage** > **Users and Groups**.
2. Click **Add user/group**.
3. Click **None Selected** to assign users to the app.
4. Click **Select** to confirm assignment.

![SCIM provisioning setup for the Entra integration.]({% image_buster /assets/img_archive/entra_scim.png %}){: style="max-width:50%;"}

{% endtab %}
{% tab Custom %}

## Step 1: Configure your SCIM settings

- **Default Workspace:** Select the workspace where new users will be added by default. If you don’t specify a workspace in your [SCIM API request]({{site.baseurl}}/post_create_user_account/), Braze assigns users to this workspace. 
- **Service Origin:** Enter the origin domain of your SCIM requests. Braze uses this in the `X-Request-Origin` header to verify where requests are coming from.
- **IP Allowlisting (optional):** You can restrict SCIM requests to specific IP addresses. Enter a comma-separated list or range of IP addresses to allow. The `X-Request-Origin` header in each request will be used to check the request IP address against the allowlist.

![SCIM Provisioning settings form with three fields: Default Workspace, Service Origin , and optional IP Allowlisting. The “Generate SCIM Token” button is disabled.]({% image_buster /assets/img/scim_unfilled.png %})

## Step 2: Generate a SCIM token

After completing the required fields, press **Generate SCIM token** to generate a SCIM token and see your SCIM API endpoint. Make sure to copy the SCIM token before you navigate away. **This token will only be presented once.** 

![SCIM API Endpoint and SCIM Token fields displayed with masked values and copy buttons. Below the token field is a “Reset Token” button.]({% image_buster /assets/img/scim.png %})

Braze expects all SCIM requests to contain the SCIM API bearer token attached via an HTTP `Authorization` header.

{% endtab %}
{% endtabs %}