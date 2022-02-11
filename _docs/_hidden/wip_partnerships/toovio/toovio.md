---
nav_title: Toovio
article_title: Toovio
page_order: 1

description: "Toovio is a data-as-a-service company powered by Artificial Intelligence."
alias: /partners/toovio/

page_type: partner
search_tag: toovio
hidden: true
---

# Toovio

> Toovio is a data-as-a-service company powered by Artificial Intelligence, that helps you discover your actionable data & use the most important elements to drive incremental results based on pre-defined objectives.

Toovio is an ideal partner with complementary software and product set that enhances the power of the execution and delivery capability of Braze.

**Real Time Triggers:** Coupled with Brazes comprehensive profiles on individual users, Toovio can trigger near real time messages to these users based on their behaviors & pre-defined outcomes.

**Drive Incremental Performance –** Users will be able to drive positive results over time among their customer base based on pre-defined objectives

**Advanced Campaign Measurement –** Toovio’s unique Closed Loop measurement tool identifies what campaigns are working, what’s not & most importantly, the reasons why by using test versus control & experiments.

## Prerequisites

Toovio integration is dependent on:
- Toovio account.
- [Braze Currents][1]. Braze Currents allows Braze clients to stream event / behavior data to a braze data partner (AWS S3, Google Cloud Storage or Microsoft Azure Blob Storage) for processing external to the Braze platform.
- [Braze REST API Key][2]. This can be created within the Braze Dashboard -> Developer Console -> REST API Key -> Create New API Key
                                                                                  |

## Integration

The following integration allows Toovio to generate triggers targeting specific customers and communicate in near real-time.
Integrating Toovio to Braze will be made via SDK-to-SDK. Triggers determined by Toovio will be transmitted to Braze via the Braze SDK ([Track API][3])

### Step 1: Define Data Partner (Currents)

A drop location for the current feed should be shared with Toovio. This allows Toovio to gain access and process event / behavior client data.

### Step 2: Setup Triggered Campaign

Create a [triggered campaign][4] based on the targeted customer events that Toovio triggers will target. Additionally target user attributes and values should be defined that will trigger the campaign.

### Step 3: Setup Toovio Account

Contact Toovio at [info@toovio.com](mailto:info@toovio.com?subject=New%20Customer%20Request) with the Subject: New Customer Request to setup an account.

### Step 4: Setup Toovio Modelling / Trigger

Toovio will work with clients to setup triggers and underlying models.


[1]: https://www.braze.com/docs/user_guide/data_and_analytics/braze_currents/
[2]: https://www.braze.com/docs/api/api_key/
[3]: https://www.braze.com/docs/api/endpoints/user_data/post_user_track/
[4]: https://www.braze.com/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/