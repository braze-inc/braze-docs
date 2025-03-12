## About Firebase Cloud Messaging API

If you haven't already, you'll need to migrate from Google's deprecated Cloud Messaging API to their fully-supported Firebase Cloud Messaging (FCM) API. For more information, see Google's [Firebase FAQ - 2023](https://firebase.google.com/support/faq#fcm-23-deprecation).

{% alert important %}
If this is your first time setting up the push integration for Android, see [Standard Android push integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android) instead.
{% endalert %}

## Rate limit

Firebase Cloud Messaging (FCM) API has a default rate limit of 600,000 requests per minute. If you reach this limit, Braze will automatically try again in a few minutes. To request an increase, contact [Firebase Support](https://firebase.google.com/support).

## Migrating to FCM

### Step 1: Verify your Project ID

First, open Google Cloud. On your project's home page, check the number in the **Project ID** field—you’ll compare this to the one in your Firebase project next.

![The Google Cloud project's home page with the "Project ID" highlighted.]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gcp.png %})

Next, open Firebase Console, then select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **Project settings**.

![The Firebase project with the "Settings" menu open.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

In the **General** tab, verify the **Project ID** matches the one listed in your Google Cloud project.

![The Firebase project's "Settings" page with the "Project ID" highlighted.]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gfb.png %})

### Step 2: Verify your Sender ID

First, open Braze, then select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **App Settings**.

![The "Settings" menu open in Braze with "App Settings" highlighted.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %}){: style="max-width:80%;"}

Under your Android app's **Push Notification Settings**, check the number in the **Firebase Cloud Messaging Sender ID** field&#8212;you'll compare this to the one in your Firebase project next.

![The form for "Push Notification Settings".]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id.png %})

Next, open Firebase Console, then select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **Project settings**.

![The Firebase project with the "Settings" menu open.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Select **Cloud Messaging**. Under **Cloud Messaging API (Legacy)**, verify the **Sender ID** matches the one listed in your Braze dashboard.

![The Firebase project's "Cloud Messaging" page with the "Sender ID" highlighted.]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id-firebase.png %})

### Step 3: Enable the Firebase Cloud Messaging API

In Google Cloud, select the project your Android app is using, then enable the [Firebase Cloud Messaging API](https://console.cloud.google.com/apis/library/fcm.googleapis.com).

![Enabled Firebase Cloud Messaging API]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### Step 4: Create a Service Account

Next, create a new service account, so Braze can make authorized API calls when registering FCM tokens. In Google Cloud, go to **Service Accounts**, then choose your project. On the **Service Accounts** page, select **Create Service Account**.

![A project's service account home page with "Create Service Account" highlighted.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

Enter a service account name, ID, and description, then select **Create and continue**.

![The form for "Service account details."]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

In the **Role** field, find and select **Firebase Cloud Messaging API Admin** from the list of roles. For more restrictive access, create a [custom role](https://cloud.google.com/iam/docs/creating-custom-roles) with the `cloudmessaging.messages.create` permission, then choose it from the list instead. When you're finished, select **Done**.

{% alert warning %}
Be sure to select _Firebase Cloud Messaging **API** Admin_, not _Firebase Cloud Messaging Admin_.
{% endalert %}

![The form for "Grant this service account access to project" with "Firebase Cloud Messaging API Admin" selected as the role.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### Step 5: Verify permissions (optional)

To verify which permissions your service account has, open Google Cloud, then go to your project and select **IAM**. Under **View By Principals**, select **Excess Permissions**.

![The "View By Principles" tab with the number of excess permissions listed for each principal.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-excess-permissions.png %})

Now you can review the current permissions assigned to your selected role.

![The list of current permissions assigned to the selected role.]({% image_buster /assets/img/android/push_integration/create_a_service_account/review-permissions.png %}){: style="max-width:75%;"}

### Step 6: Generate JSON credentials

Next, generate JSON credentials for your FCM service account. On Google Cloud IAM & Admin, go to **Service Accounts**, then choose your project. Locate the FCM service account [you created earlier](#step-4-create-a-service-account), then select <i class="fa-solid fa-ellipsis-vertical"></i>&nbsp;**Actions** > **Manage Keys**.

![The project's service account homepage with the "Actions" menu open.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

Select **Add Key** > **Create new key**.

{% alert note %}
Creating a new key will not remove your legacy ones. If you accidentally delete your new key by selecting **Revert Credentials**, Braze will use your legacy keys as a backup.
{% endalert %}

![The selected service account with the "Add Key" menu open.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

Choose **JSON**, then select **Create**. If you created your service account using a different Google Cloud project ID than your FCM project ID, you'll need to manually update the value assigned to the `project_id` in your JSON file.

Be sure to remember where you downloaded the key&#8212;you'll need it in the next step.

![The form for creating a private key with "JSON" selected.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
Private keys could pose a security risk if compromised. Store your JSON credentials in a secure location for now&#8212;you'll delete your key after you upload it to Braze.
{% endalert %}

### Step 7: Upload your JSON credentials to Braze

In Braze, select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **App Settings**.

![The "Settings" menu open in Braze with "App Settings" highlighted.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

Under **Push Notification Settings**, select **Upload JSON File**, then choose the file [you generated earlier](#step-6-generate-json-credentials). When you're finished, select **Save**.

![The form for "Push Notification Settings" with the private key updated in the "Firebase Cloud Messaging Server Key" field.]({% image_buster /assets/img/android/push_integration/migration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
Private keys could pose a security risk if compromised. Now that your key is uploaded to Braze, delete the file [you generated previously](#step-6-generate-json-credentials) from your computer.
{% endalert %}

### Step 8: Test your new credentials (optional)

As soon as you upload your credentials to Braze, you can start sending push notifications using your new credentials. To test your new credentials, send a real or test push notification to your app using FCM or Braze. If the push notification goes through, everything is working. If it doesn't:

- [Verify your sender ID](#step-2-verify-your-sender-id)
- [Verify your permissions](#step-5-verify-permissions-optional)
- Review push notification errors in your [message activity log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)

If you're still having trouble, see [Reverting your credentials](#reverting-your-credentials).

## Reverting your credentials

You can delete your new credentials and restore your legacy credentials at any time. As soon as your credentials are restored, you can start sending push notifications using your legacy credentials instead.

In Braze, select <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **App Settings**. Under **Push Notification Settings**, select **Revert Credentials**.

{% alert warning %}
If you delete your new credentials, you cannot restore them later. You'll need to [generate new credentials](#step-6-generate-json-credentials) and [upload them to Braze](#step-7-upload-your-json-credentials-to-braze) again.
{% endalert %}

![The form for "Push Notification Settings" with the "Revert Credentials" button highlighted.]({% image_buster /assets/img/android/push_integration/revert-credentials.png %})

## Frequently Asked Questions (FAQ) {#faq}

### How do I know my new credentials are working?

Your new credentials start working as soon as you upload them to Braze. To test them, select **Test Credentials**. If you get an error, you can always [revert your credentials](#reverting-your-credentials).

### Do I need to migrate to FCM for my unused apps or development apps?

No. However, your unused apps and development apps will continue to show a warning message asking you to migrate. To remove this message, you can either upload new credentials, or delete these apps from your workspace. If you choose to delete these apps, be sure to check with your team first in case someone is using them.

### Where can I check error messages?

You can review push notification errors in your [message activity log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/).

### Before migrating, do I need to update my app or SDK?

No. You only need to upload your new credentials to Braze.

### Do I need to delete my old legacy credentials first?

No. If you ever need to delete your new credentials, [your legacy credentials can be used instead](#reverting-your-credentials).

### After migrating, why is there still a warning message in Braze?

You'll continue to see this warning message if there's at least one Android app in your workspace you still need migrate. Be sure to migrate all of your Android apps over to Google's fully-supported FCM API.

### After migrating, how long until I send push notifications again?

After migrating, you can start sending push notifications using your new credentials right away.

### What if I created my service account using a different project than my FCM project?

If you created your service account using a different Google Cloud project ID than your FCM project ID, you'll need to manually update the value assigned to the `project_id` in your JSON file after you [create a new one](#step-6-generate-json-credentials).
