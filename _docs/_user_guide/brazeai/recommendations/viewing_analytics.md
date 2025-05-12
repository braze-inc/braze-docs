---
nav_title: Viewing analytics
article_title: "Viewing item recommendation analytics"
description: "Learn how to view analytics for your item recommendations."
page_order: 1.3
---

# Viewing item recommendation analytics

> Learn how to view analytics for item recommendations you've created in Braze.

## Viewing analytics

You can view analytics for your recommendation to see which items users were recommended and how accurate the recommendation model was.

1. Go to **Analytics** > **Item Recommendation**.
2. Select your recommendation from the list.

At the top of the page, you can find statistics about your recommendation, such as precision and coverage.

![Recommendation audience metrics showing precision (25.3%), coverage (54.3%), and recommendation types split between personalized and most popular items.]({% image_buster /assets/img/item_recs_analytics_1.png %})

These metrics are defined in the following table. 

| Metric              | Description |
| ------------------- | ---------- |
| Precision           | The percentage of time the model correctly guessed the next item a user purchased. Precision is heavily dependent on your specific catalog size and mix, and should be used as a guide to understand how often the model is correct.<br><br>In past testing, we have seen models perform well with precision numbers ranging from 6-20%. This metric updates when the model next retrains.  |
| Coverage            | What percentage of available items in the catalog are recommended to at least one user. You can expect to see higher item coverage with personalized item recommendations over most popular ones. |
| Recommendation type | Percentage of users who will receive personalized or most recent recommendations versus the fallback of most popular items. The fallback is sent to users who don’t have enough data to generate a personalized or most recent recommendation. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

The next section shows a breakdown of items in the catalog, split into two possible columns:

- **Personalized items** or **Most recent items:** This column lists each item in the catalog in descending order of most often recommended to users. This column also shows how many users were assigned each item by the model.
- **Most Popular items:** This column lists each item in the catalog in descending order of popularity. Popularity here refers to items in the catalog that users interact with most often in the entire workspace. Most popular is used as the fallback when personalized or most recent cannot be calculated for an individual user.

![Side-by-side tables listing items assigned to users, separated by personalized recommendations and most popular recommendations.]({% image_buster /assets/img/item_recs_analytics_2.png %})

The **Recommendation overview** shows a summary of your chosen recommendation configuration, including when the recommendation was last updated.

![Recommendation overview table displaying type, catalog, event type, custom event name, property name, and last updated date.]({% image_buster /assets/img/item_recs_analytics_3.png %}){: style="max-width:50%" }
