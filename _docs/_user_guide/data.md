---
nav_title: Data 
article_title: Data 
page_order: 3
description: "Learn about the Braze Data Platform, including how to unify, activate, and distribute your data."
---

# Braze Data Platform

> Learn about the Braze Data Platform, including how to unify, activate, and distribute your data.

The Braze Data Platform (BDP) is a comprehensive, composable set of data capabilities and partner integrations that empowers you to create personalized experiences for your customers. At Braze, we think about data in terms of three data-related jobs to be done: [Unification]({{site.baseurl}}/user_guide/data/unification), [Activation]({{site.baseurl}}/user_guide/data/activation), and [Distribution]({{site.baseurl}}/user_guide/data/distribution).

By using a combination of features in the Braze Data Platform, you can leverage your data to create meaningful, targeted messages that respond to what your customers do in real-time.

## How it works

### Unify your data

User data flows into Braze through many entry points. Collect and consolidate first-party data from any source using [APIs]({{site.baseurl}}/api/home) and [SDKs]({{site.baseurl}}/developer_guide/sdk_integration). You can also use built-in ingestion tools like [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) to create a direct integration from your data warehouse or file storage solution to Braze, or use [Data Transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation) to build and manage webhook integrations for transferring data into Braze.

### Activate your data

Clean, organize, and prepare your data for use. This involves understanding your customers' behaviors and preferences in real-time with user profiles and segments. Reference the [Reports metric glossary]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics/) as you create targeted messages, and use [catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/) to enrich your messages with product or content data. Identify how your customers are responding to these personalized experiences.

### Distribute your data

Stream and [export your data]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/) to external systems for next-step insights and decisions. Use [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) to stream Braze event data into a data warehouse to power business intelligence tools.

## Data infrastructure

Braze data infrastructure includes [data centers]({{site.baseurl}}/user_guide/data/infrastructure/data_centers) that help minimize latency—the time it takes for data to travel between the server and the user. This geographic distribution allows our services to be reliable and scalable. We also offer [field-level encryption]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption) to help protect sensitive data and minimize personally identifiable information (PII) shared in Braze. For more on usage and billing, see [Data points]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

## Core principles

Data plays a crucial role in enhancing your customer engagement strategy by enabling you to create personalized experiences, understand customer behavior, and optimize messaging strategies. At Braze, we build all data capabilities with three core principles in mind:

{% details Making your data work harder %}
- **Flexible and component-based:** Our overarching goal is to help you utilize your data more effectively and fully. Built with a composable architecture, you can leverage the technologies you need to make your data work harder, without unnecessary middleware.
- **Partner integrations:** Braze prioritizes integrations with best-of-breed ecosystem technologies (and offers APIs) that make real-time, bi-directional data sharing straightforward.
- **Stream-processing architecture:** You can trigger actions on any data point ingested into Braze for segmentation, orchestration, and personalization.
{% enddetails %}

{% details Enhancing data agility to drive performance %}
- **Flexible audience construction:** Reduce reliance on technical teams to create audiences and deliver personalized customer engagement at scale.
- **Speed and performance:** Engagement data and insights are delivered in real-time, which supports iterative, effective customer engagement, as well as broader business decision-making.
{% enddetails %}

{% details Keeping your data secure, safe, and compliant %}
- **Industry leading security practices:** We conduct regular third-party audits, including SOC 2 Type 2 and ISO 27001, to comply with the highest industry standards. We maintain a public bug bounty program to proactively address potential vulnerabilities and have a dedicated security team committed to safeguarding your data.
- **Industry compliance:** We provide tools that promote adherence to data protection regulations, including GDPR and CCPA.
- **Data privacy:** You can manage end-user consent, process requests, and action consumer rights.
{% enddetails %}
