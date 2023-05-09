---
nav_title: "Test Currents Connectors"
permalink: "/test_currents_connectors/"
hidden: true
layout: dev_guide
---

# Braze Currents

The Currents tool is a real-time data stream of your engagement events that is the most robust yet granular export out of the Braze platform. It provides you data in an Avro file type to one of our many [data partners]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/), empowering you to use the unique and valuable data Braze creates to power your BI and analytics efforts in other best-in-class platforms.

* Stream Braze event data into a data warehouse or to one of our [analytics partners]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) for detailed analysis.
* Stream Braze event data continuously to power business intelligence tools, machine learning algorithms, and more.
* Route Braze event data to a variety of other systems using [Tealium]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium/), [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/) or [mParticle]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/).

Looking for more Currents guidance and examples? Refer to our [Currents documentation]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents).

## Test Currents connectors

Test Currents connectors are free versions of our existing connectors that can be used for testing and trying out different destinations. Test Currents have:
- No limit to the number of Test Currents connectors you may build.
- An aggregate max of 10,000 events per 30-day rolling period. This event total is updated hourly on the dashboard.

After your Test Currents connectors reach the sending limit, your connector will not send events until the next 30-day period.

To upgrade your Test Currents connector, edit the integration in the dashboard and select **Upgrade**.

{% alert important %}
Test Currents connectors are currently in early access. Contact your Braze account manager if you're interested in participating in the early access.
{% endalert %}