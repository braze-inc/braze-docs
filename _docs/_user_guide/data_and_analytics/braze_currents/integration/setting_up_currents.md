---
nav_title: Setting Up Currents
page_order: 0

page_type: tutorial
description: "This page outlines and describes the generic process for integrating and configuring Braze Currents."
tool: currents
---

# Setting Up Currents

Currents is included with certain Braze packages. Please contact your Customer Success Manager if you have any questions or want to gain access.

## Step 1: Choose Your Partner

Braze Currents allows you to integrate through Data Storage using flat files or to our Behavioral Analytics and Customer Data partners using a batched JSON payloads to a designated endpoint.  

Before you begin your integration, it’s best to decide which integration is best for your purposes. For example, if you already utilize mParticle and Segment and would like Braze data to stream there, it would be best to use a batched JSON payload. If you would prefer to manipulate the data on your own or have a more complex system of data analysis, it might be best to use Data Storage ([Braze uses this method]({{ site.baseurl }}/user_guide/data_and_analytics/braze_currents/advanced_topics/how_braze_uses_currents/)!)

## Step 2: Navigate to Currents
To get started, visit the Currents page in the left sidebar, in the "Integrations" section of the Dashboard. You'll be taken to the Currents integration management page.

![Currents]({% image_buster /assets/img_archive/currents-main-page.png %})

## Step 3: Add Partner
Add a partner, sometimes called a "Currents connector", by clicking the dropdown at the top right of the screen.

![Adding an Integration]({% image_buster /assets/img/new_current.png %}){: height="50%" width="50%"}

## Step 4: Configure
Each partner requires a different set of configuration steps. To enable each integration, [see the instructions in their respective pages]({{ site.baseurl }}/user_guide/data_and_analytics/braze_currents/integration/available_partners/).

## Step 5: Test Your Integration

You may test your integration or take a look at the sample Currents data in [our Currents Examples Github repo](https://github.com/Appboy/currents-examples).
