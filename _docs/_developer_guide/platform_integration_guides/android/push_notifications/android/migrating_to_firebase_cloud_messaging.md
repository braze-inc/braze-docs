---
nav_title: Migrating to Firebase Cloud Messaging
article_title: Migrating to the Firebase Cloud Messaging API
platform: Android
page_order: 29
description: "This article covers how to migrate from Google's deprecated Cloud Messaging API to Firebase Cloud Messaging (FCM)."
channel:
  - push
search_rank: 3
---

# Migrating to the Firebase Cloud Messaging API

> Learn how to migrate from Google's deprecated Cloud Messaging API to their fully-supported Firebase Cloud Messaging (FCM) API. For more information, see Google's [Firebase FAQ - 2023](https://firebase.google.com/support/faq#fcm-23-deprecation).

{% alert important %}
If this is your first time setting up the push integration for Android, see [Standard Android push integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration) instead.
{% endalert %}

## Step 1: Verify your Sender ID

First, open Braze, then select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **App Settings**.

![The "Settings" menu open in Braze with "App Settings" highlighted.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

Under your Android app's **Push Notification Settings**, check the number in the **Firebase Cloud Messaging Sender ID** field&#8212;you'll compare this to the one in your Firebase project next.

![The form for "Push Notification Settings".]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id.png %})

Next, open Firebase Console, then select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **Project settings**.

![The Firebase project with the "Settings" menu open.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Select **Cloud Messaging**. Under **Cloud Messaging API (Legacy)**, verify the **Sender ID** matches the one listed in your Braze dashboard.

![The Firebase project's "Cloud Messaging" page with the "Sender ID" highlighted.]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id-firebase.png %})

## Step 2: Create a service account

Next, create a new service account, so Braze can make authorized API calls when registering FCM tokens. In Google Cloud, go to **Service Accounts**, then choose your project. On the **Service Accounts** page, select **Create Service Account**.

![A project's service account home page with "Create Service Account" highlighted.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

Enter a service account name, ID, and description, then select **Create and continue**.

![The form for "Service account details."]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

In the **Role** field, find and select **Firebase Cloud Messaging API Admin** from the list of roles. For more restrictive access, create a [custom role](https://cloud.google.com/iam/docs/creating-custom-roles) with the `cloudmessaging.messages.create` permission, then choose it from the list instead. When you're finished, select **Done**.

{% alert warning %}
Be sure to select **Firebase Cloud Messaging _API_ Admin**, not **Firebase Cloud Messaging Admin**.
{% endalert %}

![The form for "Grant this service account access to project" with "Firebase Cloud Messaging API Admin" selected as the role.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

## Step 3: Generate JSON credentials

Next, generate JSON credentials for your FCM service account. On Google Cloud IAM & Admin, go to **Service Accounts**, then choose your project. Locate the FCM service account [you created earlier](#step-2-create-a-service-account), then select <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Actions** > **Manage Keys**.

![The project's service account homepage with the "Actions" menu open.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

Select **Add Key** > **Create new key**.

![The selected service account with the "Add Key" menu open.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

Choose **JSON**, then select **Create**.

![The form for creating a private key with "JSON" selected.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
Private keys could pose a security risk if compromised. Store your JSON credentials in a secure location for now&#8212;you'll delete your key after you upload it to Braze.
{% endalert %}

## Step 4: Upload your JSON credentials to Braze

In Braze, select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **App Settings**.

![The "Settings" menu open in Braze with "App Settings" highlighted.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

Under **Push Notification Settings**, select **Upload JSON File**, then choose the file [you generated earlier](#step-3-generate-json-credentials). When you're finished, select **Save**.

![The form for "Push Notification Settings" with the private key updated in the "Firebase Cloud Messaging Server Key" field.]({% image_buster /assets/img/android/push_integration/migration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
Private keys could pose a security risk if compromised. Now that your key is uploaded to Braze, delete the file [you generated previously](#step-4-generate-json-credentials).
{% endalert %}
