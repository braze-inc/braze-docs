---
nav_title: Transfer between workspaces
article_title: Transfer phone numbers and subscription groups between workspaces
page_order: 4
description: "This reference article covers how to transfer your WhatsApp phone number and subscription groups between workspaces."
page_type: reference
channel:
  - WhatsApp
---

# Transfer WhatsApp phone numbers and subscription groups between workspaces

> This page covers how you can move a WhatsApp Business Account (WABA) phone number and its associated subscription group from one workspace to another within Braze. This process streamlines your experience using WhatsApp with Braze, and reduce the need for engineering help.

## Prerequisites

- Confirm you have the [user permission]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) "Manage Subscription Groups" in both the original and new workspaces.
- The WABA can't cross multiple [Braze clusters]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). This is unlikely to happen if you’re working within one company. 

## Transferring a phone number and subscription group

### Step 1: Archive the subscription group

To archive a WhatsApp subscription group, follow these steps:

1. Go to the workspace where the subscription group currently exists.
2. Go to **Audience** > **Subscription Group Management** and find the subscription group associated with the WhatsApp phone number you want to move.
3. Hover over the status for the subscription group and select <i class="fa-solid fa-box-archive"></i> **Archive**, which will mark the subscription group as inactive but won't delete it.

!["Archive" button appearing while hovering over a subscription group's "Active" status.]({% image_buster /assets/img/whatsapp/archive_subscription_group.png %}){: style="max-width:70%;"}

### Step 2: Integrate the WhatsApp phone number into the new workspace

1. Go to the workspace where you want to move the WhatsApp phone number.
2. Go to **Partner Integrations** > **Technology Partners** > **WhatsApp**, then scroll to the **WhatsApp Messaging Integration** section. 
3. Select the option to **Create new subscription group and phone number**
4. Begin the integration process, during which you can select the phone number from the archived subscription group.

### Step 3: Verify the integration

1. After completing the integration, confirm that the WhatsApp phone number is now associated with the subscription group in the new workspace.
2. Test to confirm that messages can be sent and received through that WhatsApp phone number.

## Considerations

- If you need to transfer the WhatsApp phone number back to the original workspace, repeat the steps. Archive the subscription group in the destination workspace, then integrate it into the original workspace.
- You don't need to remove the WhatsApp phone number from your Meta Business Manager during the transfer.