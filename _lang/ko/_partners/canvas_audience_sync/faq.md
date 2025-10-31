---
nav_title: FAQs
article_title: Audience Sync FAQ
alias: /partners/audience_sync_faq/
description: "This article provides answers to frequently asked questions about Audience Sync."
page_order: 80
Tool:
  - Canvas

---

# Frequently asked questions

> This article provides answers to some frequently asked questions about Audience Sync.

### How long does it take for my audiences to populate in my Audience Sync partner dashboard?

The time it takes to populate an audience depends on the specific partner. All networks will process the requests from Braze and attempt to match users. This process can typically take anywhere from 6-48 hours.

You can check the specific time range in the Troubleshooting section of the documentation for each Audience Sync partner.

### What type of first-party data can I use in my Audience Sync?

The specific fields used for each partner may vary depending on the partner's requirements. 

For example, when you configure an Audience Sync to Facebook, you will be able to use a wide variety of first-party fields like email, phone, first name, and last name, whereas, with Snapchat, you will only be able to select either email, phone, or mobile advertiser ID. 

It is important to note that the user fields you can select to sync correlate with Braze standard attributes and the mobile advertising IDs. You must ensure you appropriately pass this data via our SDKs or APIs. 

### What happens when my data is being processed to send to each Audience Sync partner?

The data you select to send to your Audience Sync destination will be normalized. Each partner may have different specifications for data normalization based on their API requirements, so please review each partner-specific endpoint for further details.

In addition, Braze will hash all data before syncing users with our Audience Sync partners, ensuring that all PII is hashed using SHA256.

### Why can I select multiple identifiers in one step for some partners, but can only select one identifier for others?

This is determined by the partner integration methods and not controlled by Braze. Some partners (such as Meta) allow multiple identifiers to be synced, and other partners (such as Google) only allow a single identifier to be synced with a user at any given time.

### How do I reconnect my integration?

If the prior user who connected the integration is no longer with your business, you’ll need to update the integration with the new user by selecting **Change Account**. Then, select **Confirm** and connect with the new user. We recommend changing users when active syncs aren't happening, such as before a scheduled entry of users into a Canvas, as syncing during a transition from the prior user to a new user may disrupt active Canvases. We recommend changing users when active syncs aren't happening, such as before a scheduled entry of users into a Canvas.

The user reconnecting must have both read and write access to all the audiences so users can successfully be synced over to the partners. Check that the user who is reconnecting the integration has access to the same ad accounts and audiences. You won't need to edit any existing Canvas steps. 

### What are common errors that can occur when creating and managing my Audience Syncs?

| Error | Reason | Solution |
| --- | --- | --- |
| Invalid Token | This can occur if you have changed your password to log into a specific ad network, or if your credentials have expired. | Go to the respective partner page to disconnect and reconnect your account. |
| Audience Size Too Low | This can occur if you have created an Audience Sync step that removes users from your audiences. If your audience size gets close to zero, the network can flag that the audience size is too low to serve. | Confirm that you're considering an Audience Sync strategy that regularly adds and removes users in a way that doesn’t fully deplete the audience size. |
| Audience Does Not Exist | The Audience Sync step uses an audience that does not exist. This can also be triggered if you don’t have the necessary permission to access the audience. | Add an active audience in your Audience Sync configuration or create a new audience. |
| Ad Account Access Attempt | This error occurs if you don’t have permission for the ad account, an audience that you selected, or both. | Work with the administrators of your ad account to get proper access and permissions. |
| Invalid Settings | This can occur if you haven't configured a specific Audience Sync destination in Canvas, including the ad account, audience, or user fields to match. | Complete the configuration of each partner before launching. |
| Terms of Service | For some Audience Sync destinations, like Facebook, it is required by the ad network to accept specific terms of service to use the Audience Sync feature. This error will trigger if you have not accepted the appropriate terms. | Confirm you have accepted each partner's required terms. For Facebook specifically, review [Facebook troubleshooting]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/#troubleshooting). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

