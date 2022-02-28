---
nav_title: Segmentation Logic with And/Or
article_title: Segmentation Logic with And/Or
page_order: 3

page_type: solution
description: "This article walks you through the difference between AND and OR operators, and how you can use them to build powerful segments."
tool: Segments
---

# Segmentation logic with AND/OR

The `AND` and `OR` operators enable some very powerful filtering. There are two scenarios you may wish to apply using:
* [AND or OR](#using-and-or-or)
* [Both](#using-both)

## Using AND or OR

### AND

Use `AND` if you are interested in the intersection of two groups. This is what is similar between the two groups. For example let’s compare two animals. What dogs `AND` cats both have in common is fur, are mammals, and are human pets.

### OR

Use `OR` if you want to target users who meet at least one condition in a group of conditions. If you have three conditions linked together by `OR`, then one, two, or all of the conditions could be true in order for the statement to be true.

For example, imagine that you want to send a message to all your users except those users on version `1.0` or `1.1` of your app. You want to target the overlap of users that are not on version `1.0` and not on version `1.1.` You can create this segment in one of two ways:
    
- You can use two filters “is not `1.0`” or “is not `1.1`”. This targets all users that do not have those versions.
- The alternative may be a longer route. You will need to add a filter for every version of your app using the OR statement, making sure to exclude app versions `1.0` and `1.1`.

# Using both

Finally, check out this example where we use both `AND` and `OR`. Here, the target audience includes users who purchased Nike sneakers `OR` Adidas sneakers `AND` are opted in to receive email notifications.

![Example for segmentation logic][33]

Another way to ensure you’re building the right logic is to create your segment and [preview the users][35] who are falling into it based on your filters. This way you can make sure that their attributes, app version, or any other segmentation matches what you are seeing.

Still need help? Open a [support ticket]({{site.baseurl}}/braze_support/).

_Last updated on September 23, 2021_

[33]: {% image_buster /assets/img_archive/NikeSneakers.png %}
[35]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data
