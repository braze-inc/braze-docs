---
nav_title: Creating Placements
article_title: Creating Banner Card Placements for the Braze SDK
hidden: true
description: "This reference article covers Banner Cards and how to integrate them in the Braze SDK."
platform:
  - iOS
  - Android
  - Web
  
---

# Creating Banner Card placements

> Before launching a Banner Card campaign in your app, you'll need to create a placement in the Braze dashboard. Placements are locations that you define in your app that can display Banner Cards.

{% alert important %}
Banner Cards are currently in early access. Contact your Braze account manager if you’re interested in participating in this early access.
{% endalert %}

## Prerequisites

These are the minimum SDK versions to start using Banner Cards:

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 %}

## Creating a placement

### Step 1: Create a new placement

Go to **Settings** > **Banner Cards Placements**, then select **Create Placement**.

![Banner Card Placements section to create placement IDs.]({% image_buster /assets/img/banner_cards/create_placement.png %})

### Step 2: Fill in the details

Name your placement and give it a **Placement ID**. Optionally, you can add a description for your placement.

Work with your marketing team to create this ID. This is the ID you'll reference in your app's code, and your marketing team will use the ID to assign a campaign to the location in your app. 

{% alert important %}
Avoid editing your placement ID after launch, as this can break the integration with your app or website.
{% endalert %}

![Placement details that designate a Banner Card will display in the left sidebar for spring sale promotion campaigns.]({% image_buster /assets/img/banner_cards/placement_details_example.png %})

For steps on how to launch a Banner Card campaign, refer to [Creating a Banner Card]({{site.baseurl}}/create_banner_card/).

## Next steps

Now that you've created your Banner Card placements, you can:

- [Integrate Banner Cards]({{site.baseurl}}/developer_guide/banner_cards/integration/)
- [Create Banner Cards]({{site.baseurl}}/create_banner_card/)
