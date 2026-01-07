---
nav_title: Braze overview
article_title: Getting Started&#58; Braze Overview
page_order: 1
page_type: reference
description: "Get acquainted with the core concepts you'll need to know when working in Braze."

---

# Get started: Braze overview

Welcome to Braze! This collection of articles will help you get started with our platform and introduce you to the key terms, features, and functionalities of Braze. This page introduces the core concepts you'll need to know when working in Braze.

{% alert tip %}
We highly recommend checking out our free [Braze Foundations for Everyone](https://learning.braze.com/page/braze-foundations-for-everyone) course along with these articles. No special login or account is needed for this course. If you're a developer looking for a technical rundown of Braze, check out [Getting Started for Developers]({{site.baseurl}}/developer_guide/getting_started/platform_overview/), too.
{% endalert %}

In the Getting Started sections, we focus on the common implementations of Braze. However, Braze is incredibly flexible and can be customized to bring value to your organization in various ways. To establish clarity and brevity, we've provided a descriptive overview of the default setup instead of offering rigid instructions. We recognize that every organization has its distinct needs, and Braze is built to cater to a diverse range of customization options that can be tailored to your specific requirements.

Let's explore the power of Braze together.

## How Braze works

Braze is a customer engagement platform that helps brands of all sizes create personalized and targeted campaigns across various channels. Braze gives you the ability to listen to your customers, understand what their behavior is signaling, and then act by sending customers the right message, through the right channel, at the right time.

{% alert tip %}
Make sure to [add your colleagues to Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/) so they can explore the platform with you.
{% endalert %}

## Users and segments

Users are your customers—the people receiving the messages you send using Braze. All the data you gather about a user and ingest into Braze is stored in their user profile, such as their demographics, personal information, preferences, and behaviors. This information powers your messaging and is how you can tailor your messages to the right user.

![]({% image_buster /assets/img/getting_started/user_profile.png %})

Segments divide your customer base into smaller groups that you can then target with specific messaging. You can use different variables to create segments, ranging from characteristics such as gender, location, and age to behaviors like interaction patterns with previous campaigns or where they are in the customer journey.

Segments are dynamic—users can move in and out of segments in real time based on their behavior and where they are in relation to your brand. This ensures that your customers receive the messaging most relevant to them at any given time. You can create as many segments as needed for your targeting and messaging purposes.

![]({% image_buster /assets/img/getting_started/segment.png %})

For more, check out: [Getting Started: Users and segments]({{site.baseurl}}/user_guide/getting_started/users_segments/).

## Campaigns and Canvases

Campaigns and Canvases are how you send messages to your users.

Campaigns are best for single messages sent to a specific audience segment across various channels. You can leverage any of our supported messaging channels in your campaign (email, push, in-app messages, SMS, and more).

Canvases are advanced campaign workflows that allow you to automate and orchestrate personalized customer journeys across multiple channels. Within a Canvas, you can set up branching logic, delays, decision points, and conversion events to guide customers through a series of interactions. Canvases help ensure consistent and seamless communication across different touchpoints, increasing the chances of customer engagement and conversion. 

For more, check out: [Getting Started: Campaigns and Canvases]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

## Workspaces

Workspaces group your data—users, segments, campaigns, and Canvases—into one location. Information isn't shared between workspaces, so keep that in mind when adding websites and apps to your workspaces. As a best practice, we suggest only putting different versions of the same or very similar apps together under one workspace.

Example uses for workspaces include:

- Different product lines or apps
- Different audiences (such as delivery drivers versus customers)
- Separate businesses
- Testing environment

For more, check out: [Getting Started: Workspaces]({{site.baseurl}}/user_guide/getting_started/workspaces/).

## Integrating Braze

Braze is designed to get up and running quickly and easily. Our average time-to-value is six weeks across our customer base of hundreds of brands.

![]({% image_buster /assets/img/getting_started/timetovalue.png %})

Here's the Braze framework for estimating the length of your integration based on four components you can work on in parallel. The typical range is 30 to 180 days, with most accounts completing their integration within 45 to 60 days.

- **Campaign migration complexity level:** The time it takes to migrate campaigns depends on how many you have, how personalized they are, and your resources. If you have under ten campaigns to migrate, it'll take less than 60 days. But if you have over 100 campaigns, it'll be more complicated. If it's only one person migrating 100 campaigns, that's different than 10 people migrating 100.

{% alert tip %}
Need help with your migration? Our [certified Braze partners](https://www.braze.com/partners/solutions-partners) can help!
{% endalert %}

- **Email volume:** To send emails, you'll need to warm up your IPs. [IP warming]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) is the process of building sender reputation with your newly assigned IP addresses. If you send less than 2–3 million emails per day, your IP warming should take 30 days or less. Keep in mind your peak sending. If you normally send 2 million emails a day but plan to send 7 million for a seasonal period, that "peak" sending is what you should warm up to. High-volume senders can use multiple IPs to speed up the warming process.
- **Organizational complexity:** Our onboarding process can adapt to your business needs. Whether you're a single business unit, have a Center of Excellence, multiple independent units, or use agencies to augment your teams, Braze has experience working in all scenarios.
- **Data infrastructure sophistication:** If you're only implementing the Braze SDK or already have a Customer Data Platform (CDP), it's possible to get everything set up in just 30 days. Using a modern CDP can speed up the process. But if you have many backend systems, tools, or databases to connect with Braze, it might take longer and need more dedicated resources to finish setup.

For more, check out: [Getting Started: Integration overview]({{site.baseurl}}/user_guide/getting_started/integration/).

