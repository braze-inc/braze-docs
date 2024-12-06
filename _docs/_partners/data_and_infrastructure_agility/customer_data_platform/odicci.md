---
title: Odicci Braze Integration
description: Step-by-step guide to integrating Odicci with Braze for personalized marketing campaigns.
---

# Odicci Braze Integration

## Overview
The Odicci Braze Integration allows you to connect the Odicci platform with Braze for seamless data sharing and campaign management. With this integration, you can:

- Automatically send audience data collected in Odicci experiences to Braze.
- Trigger personalized marketing campaigns based on user interactions.
- Map fields between Odicci and Braze to ensure accurate data synchronization.

---

## Prerequisites
Before you begin, ensure the following:

1. You have an active Odicci account with access to the **Integrations** section.
2. You have a Braze account with API access.
3. Your Braze REST API Key is available.

---

## Integration Steps
To set up the Odicci Braze integration, follow these steps:

### 1. Enable the Integration in Odicci
1. Log in to your Odicci account.
2. Navigate to the **Settings > Integrations** section.
3. Find the **Braze** integration and click **Connect**.

   ![Connect Braze Integration](/assets/img/odicci/braze_connect.png)

4. Enter your Braze REST API Key into the provided field.
5. Save the settings to activate the integration at the account level.

---

### 2. Obtain Your Braze REST API Key
1. Log in to your Braze account.
2. Go to **Developer Console > REST API Keys**.
3. Create a new API Key or copy an existing one with the required permissions (e.g., user profile management, data import).

   ![Braze API Key Setup](/assets/img/odicci/braze-endpoint.png)

---

### 3. Activate the Integration at the Experience Level
1. Create or open an **Experience** in Odicci Studio.
2. Navigate to **Studio > Settings > Integrations**.
3. Locate the **Braze** checkbox and tick it to activate the integration for the experience.
4. Save your changes.

---

### 4. Map Fields
1. After activating the integration, remain in the **Studio > Settings > Integrations** section.
2. Map the fields from your Odicci experience (e.g., `Email`, `Name`) to their corresponding fields in Braze.
3. Save your configuration.

   ![Field Mapping Configuration](/assets/img/odicci/braze_field_mapping.png)

---

### 5. Test the Integration
1. Run the experience in Odicci to collect test data.
2. Verify that the data syncs correctly to Braze by checking the Braze dashboard or data logs.
3. Ensure the mapped fields are correctly populated in Braze.

---

## Example Use Case
**Scenario**: A retailer uses Odicci’s gamified experiences to collect email addresses for a marketing campaign.

1. A customer completes a game in Odicci, providing their email address.
2. Odicci automatically syncs this data to Braze.
3. Braze triggers a personalized "Thank You" email and includes a discount code.

---

## Troubleshooting
If you experience issues with the integration, consider the following solutions:

### Issue: API Key Not Valid
- Double-check your Braze API Key and ensure it has the necessary permissions.
- Re-enter the API Key in the Odicci integration settings.

### Issue: Data Not Syncing
- Verify that the fields in the **Field Mapping** section are correctly configured.
- Ensure the API Key has permissions for user data imports.

### Issue: Campaign Not Triggering
- Check the Braze campaign settings to ensure the correct audience or trigger conditions are set.

For further assistance, contact [Odicci Support](https://help.odicci.com).

---

## Additional Information
- Learn more about Braze API permissions in the [Braze Developer Documentation](https://www.braze.com/docs/api/).
- Refer to the [Odicci Help Center](https://help.odicci.com) for additional resources and FAQs.
