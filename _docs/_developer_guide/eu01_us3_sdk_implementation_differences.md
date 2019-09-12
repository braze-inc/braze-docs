---
nav_title: EU-01 & US-03 Implementation Differences
config_only: false
layout: featured
page_order: 4
---

# EU-01 & US-03 Implementation Differences

Depending on your instance, you will have to configure your integration so that it points to the [correct endpoints]({{ site.baseurl }}/developer_guide/rest_api/basics/#endpoints). The following set of steps will go over relevant details on how to properly set this up should your dashboard be on the EU-01 Instance. For customers on this instance, please ensure you are contractually authorized to use the EU data center prior to using the following integration.

## SDK Implementation
If you are on the EU-01 Instance when integrating any of our SDKs, please point your SDK endpoints to `https://sdk.fra-01.braze.eu`.

Please note, if you have been set up with a custom endpoint your Customer Success Manager will advise you of the correct address. In that instance simply substitute the endpoint address listed above with the custom address supplied.

These instructions apply specifically to the EU-01 Instance, but can be applied to all other Instances so long as the correct endpoints are referenced.
