---
nav_title: Automated user provisioning
article_title: Automated User Provisioning
page_order: 3
page_type: reference
description: "This reference article covers what information you need to provide for automated user provisioning and how and where to use your generated System for Cross-domain Identity Management (SCIM) token."
alias: /scim/automated_user_provisioning/

---

# Automated user provisioning

> Use SCIM provisioning to automatically create and manage Braze users through API. This article walks you through what information to provide, how to generate your SCIM token, and where to find your SCIM API endpoint.

{% include early_access_beta_alert.md feature='SCIM provisioning' %}

## Accessing SCIM provisioning settings

1. In the Braze dashboard, go to **Settings** > **Admin Settings** > **SCIM Provisioning**, and then select **Configure SCIM integration**.
2. In the **Braze configuration** step, select a provisioning method and provide access settings.

![A page to set up the SCIM integration with sections for selecting a provisioning method and providing access settings.]({% image_buster /assets/img_archive/scim_braze_config.png %}){: style="max-width:70%;"}

{: start="3"}
3. In the **IdP configuration** step, follow the steps within the platform for your selected provisioning method.

{% tabs %}
{% tab Okta - Braze app %}

{% include early_access_beta_alert.md feature='The Okta integration' %}

Use the **Okta - Braze app** option if you set up the Braze app for SAML SSO in Okta. If you set up a custom app for SSO, follow the instructions in the [Okta - Custom app integration]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/?tab=okta%20-%20custom%20app%20integration#step-1-set-up-scim-provisioning) tab.

## Step 1: Set up SCIM provisioning

### Step 1.1: Enable SCIM

1. In Okta, go to **Applications** > **Applications**, then select **Create App Integration**. Select **SAML 2.0** as the sign-in method.
2. Fill in the following details (which are located in the Braze [**IdP configuration** step](#accessing-scim-provisioning-settings)) to create a custom app:
- App logo
- Single sign-on URL
- Audience URL (SP entity ID)
3. Select **Finish**.
4. Select the **General** tab. 
5. In the **App Settings** section, select **Edit**.
6. In the **Provisioning** field, select **SCIM**. 

### Step 1.2: Disable application visibility

1. In the **Application visibility** field, select the **Do not display application icon to user** checkbox. This prevents users from accessing SSO through the app, which is intended solely for SCIM. 
2. Select **Save**.

### Step 1.3: Set up the SCIM integration

1. Select the **Provisioning** tab.
2. In **Settings** > **Integration** > **SCIM Connection** select **Edit** and fill in the field values that populate within the table on the **Setup SCIM provisioning** page.

### Step 1.4: Test the API credentials

Select **Test API Credentials**. A verification message appears if the integration is successful and you can save.

### Step 1.5: Enable provisioning to the app

1. In **Provisioning** > **Settings** > **To App** > **Provisioning to App**, select **Edit**.
2. Enable the following:
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. Review and configure the **Attribute Mapping** section with the mappings that populate within the table on the **Setup SCIM provisioning** page.

## Step 2: Assign users to the app

1. Select the **Assignment** tab.
2. Select **Assign** and select an option.
3. Assign the app to the people who should have access to Braze.
4. Select **Done** when you’ve completed the assignment.

{% endtab %}
{% tab Okta - Custom app integration %}

{% include early_access_beta_alert.md feature='The Okta integration' %}

Use the **Okta - Custom app integration** option if you set up a custom app for SSO. If you set up the Braze app for SAML SSO in Okta, follow the instructions in the [Okta - Braze app]({{site.baseurl}}/user_guide/administer/global/user_management/automated_user_provisioning/?tab=okta%20-%20braze%20app#step-1-set-up-scim-provisioning) tab.

## Step 1: Set up SCIM provisioning

### Step 1.1: Enable SCIM

1. In Okta, go to your Braze app.
2. Select the **General** tab.
3. In the **App Settings** section, select **Edit**.
4. In the **Provisioning** field, select **SCIM**.
5. Select **Save**.

### Step 1.2: Set up SCIM integration

1. Select the **Provisioning** tab.
2. In **Settings** > **Integration** > **SCIM Connection**, select **Edit**, and fill in the field values that populate within the table on the **Setup SCIM provisioning** page.
3. Test the API credentials by selecting **Test API Credentials**.
4. Select **Save**.

### Step 1.3: Enable provisioning to the app

1. In **Provisioning** > **Settings** > **To App** > **Provisioning to App**, select **Edit**.
2. Enable the following:
    - Create Users
    - Update Users Attributes
    - Deactivate Users
3. Review and configure the **Attribute Mapping** section with the mappings that populate within the table on the **Setup SCIM provisioning** page.

## Step 2: Assign users to the app

1. Select the **Assignment** tab.
2. Select **Assign** and select an option.
3. Assign the app to the people who should have access to Braze.
4. Select **Done**.

{% endtab %}
{% tab Entra ID %}

{% include early_access_beta_alert.md feature='The Entra ID integration' %}

## Step 1: Set up SCIM provisioning app

### Step 1.1: Log into Microsoft Entra admin center

Log in to your Microsoft Entra admin center.

### Step 1.2: Create and set up your SCIM app

1. In the navigation menu, go to **Entra ID** > **Enterprise apps**.
2. Select **New application**.
3. Select **Create your own application**.
4. In the panel, input a name for your app.
5. In the **What are you looking to do with your application?** section, select **Integrate application you don't find in the gallery (Non-gallery)**.
6. Select **Create**.

### Step 1.3: Set up SCIM integration

1. Go to the **Manage** > **Provisioning** section of your SCIM application.
2. Select **Connect your application** or **New configuration** and fill in the field values that populate within the table on the **Setup SCIM provisioning** page.

### Step 1.4: Enable provisioning to the app

1. Go to the **Manage** > **Attribute mapping (Preview)** section of your SCIM application.
2. Select **Provision Microsoft Entra ID Users**.
3. Review and configure the **Attribute Mapping** section to match the attributes that populate within the table on the **Setup SCIM provisioning** page.
4. Close the **Attribute Mapping** page.

## Step 2: Assign users to the app

1. Go to **Manage** > **Users and Groups**.
2. Select **Add user/group**.
3. Select **None Selected** to assign users to the app.
4. Select the **Select** button to confirm assignment.

{% endtab %}
{% tab Custom %}

## Step 1: Configure your SCIM settings

- **Default Workspace:** Select the workspace where new users should be added by default. If you don’t specify a workspace in your [SCIM API request]({{site.baseurl}}/post_create_user_account/), Braze assigns users to this workspace.
- **Service Origin:** Enter the origin domain of your SCIM requests. Braze uses this in the `X-Request-Origin` header to verify where requests are coming from.
- **IP Allowlisting (optional):** You can restrict SCIM requests to specific IP addresses. Enter a comma-separated list or range of IP addresses to allow. The `X-Request-Origin` header in each request is used to check the request IP address against the allowlist.

![SCIM Provisioning settings form with three fields: Default Workspace, Service Origin, and optional IP Allowlisting. The “Generate SCIM Token” button is disabled.]({% image_buster /assets/img/scim_unfilled.png %})

## Step 2: Generate a SCIM token

After completing the required fields, press **Generate SCIM token** to generate a SCIM token and see your SCIM API endpoint. Make sure to copy the SCIM token before you navigate away. **This token appears only once.** 

![SCIM API Endpoint and SCIM Token fields displayed with masked values and copy buttons. Below the token field is a “Reset Token” button.]({% image_buster /assets/img/scim.png %})

Braze expects all SCIM requests to contain the SCIM API bearer token attached via an HTTP `Authorization` header.

{% endtab %}
{% endtabs %}
