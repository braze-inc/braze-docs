---
nav_title: Using Segmentation Logic with And/Or
article_title: Using Segmentation Logic with And/Or
page_order: 1

page_type: solution
description: "This article walks you through the difference between AND and OR operators, and how you can use them to build powerful segments."
tool: Segments
---

# Using Segmentation Logic With And/Or

The **AND** and **OR** operators enable some very powerful filtering. There are 2 scenarios you may wish to apply:
* [Using AND or OR](#using-and-or-or)
* [Using Both](#using-both)

## Using AND or OR

### AND

Use **AND** if you are interested in the intersection of two groups. This is, what is similar between the two groups. For example let’s compare two animals. What dogs **AND** cats both have in common is fur, are mammals, and are human pets:

![Venn Diagram Definition][30]

### OR

Use **OR** if you want to target users who meet at least one condition in a group of conditions. If you have three conditions linked together by "OR", then one, two, or all of the conditions could be true in order for the statement to be true.

For example, imagine that you want to send a message to all your users __except__ those users on version `1.0` or `1.1` of your app. You want to target the overlap of users that are not on version `1.0` and not on version `1.1.` You can create this segment in one of two ways:

    
* You can use two filters “is not `1.0`” OR “is not `1.1`”. Using this **OR** filter you are targeting all users that do not have those versions.
	
* The alternative may be a longer route. You will need to add a filter for every version of your app using the OR statement, making sure to exclude app versions `1.0` and `1.1`.


# Using Both

Finally, look at the example below where we are using both the **AND** and **OR**. The target audience here are users who purchased Nike Sneakers **OR** Adidas sneakers **AND** are opted in to receive email notifications.

![Sneaker Shoppers Example][33]

![Venn Diagram Example][34]

Another way to ensure you’re building the right logic is to create your segment and [preview the users][35] who are falling into it based on your filters. This way you can make sure that their attributes, app version, or any other segmentation matches what you are seeing.

Still need help? [Open a support ticket]({{site.baseurl}}/support_contact/).

[30]: {% image_buster /assets/img_archive/trouble10.png %}
[33]: {% image_buster /assets/img_archive/NikeSneakers.png %}
[34]: {% image_buster /assets/img_archive/VennDiagram.png %}
[35]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/viewing_and_understanding_segment_data/#viewing-and-understanding-segment-data
