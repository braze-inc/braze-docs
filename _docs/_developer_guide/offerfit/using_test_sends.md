---
nav_title: Using Test Sends
article_title: Test Sends
page_order: 3
description: "Learn..."
---

# Using test sends

> Learn how to use test sends, so you can...

## Prerequisites

Before you can use test sends, you'll need to partner with the OfferFit team to [build a use case]({{site.baseurl}}/developer_guide/offerfit/building_use_cases).

## Using test sends {#test-sends}

To use Test Sends, define a custom attribute for each message element you want to test—such as subject line, image URL, or call-to-action (CTA). Use the following naming pattern:

```plaintext
offerfit_experimenter_1_ATTRIBUTE_NAME
```

Replace `ATTRIBUTE_NAME` with a short, descriptive label for the element you're testing. Your attributes should be similar to the following:

```plaintext
offerfit_experimenter_1_subject_line  
offerfit_experimenter_1_image_url  
offerfit_experimenter_1_cta_text
```
