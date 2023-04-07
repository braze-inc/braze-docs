---
nav_title: Most Popular Products
article_title: Most Popular Products
alias: "/catalogs/"
page_order: 13
description: "This reference article covers how to create a Recommendation for Most Popular Products."
---

# Most Popular Produts

{% alert important %} 
Most Popular Products is currently in early access. Contact your Braze customer success manager if you're interested in participating. 
{% endalert %} 


## Getting started

Most Popular Product can be created from two starting points in the Braze dashboard. Starting in the Predictions section, click __Create Prediction__ and select __Item Recommendation__. Alternatively, you can click __Create a Recommendation__ from an individual Catalog's page.

## Creating a Most Popular Products Recommendation

![][1]{: style="max-width:80%;"} 

### Give it a name

Enter a descriptive name and optional description for this recommendation.

### Select a catalog

If not already populated, choose the Catalog from which this recommendation will calculate Most Popular Products.

### Type

In the "Type" dropdown, select "Most popular products".

### Product IDs

The final step is to tell Braze where to find the product IDs in the purchase events. In order to create this or any other Recommendation, the unique values in the `id` field of the Catalog must also be in the `product_id`  field of the purchase events or in the top level fields of the `properties` of those evengts.  The dropdown labeled Product IDs on the creation page will be prepopulated with those fields sent via SDK to Braze. Select the one that corresponds to the product IDs.

{% alert important %} 
The product IDs must be in a top level field of the properties of the Purchase event. No nested properties or custom event fields are supported at this time.
{% endalert %} 

### Go!

Click "Create Recommmendation"! This process can take several hours to complete. You will receive an e-mail with notification of its success or an explanation of why the creation may have failed.


## Including Most Popular Products in Messaging

[1]: {% image_buster /assets/img/mostPopular.png %}

 