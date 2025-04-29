---
nav_title: About Item Recommendations
article_title: About Item Recommendations
description: "This reference article describes different use cases for recommending items to customers using Braze."
page_order: 10
---

# About item recommendations

In this article, you’ll learn about the different ways you can suggest items that your customers are interested in, and get inspiration for common use cases for creating recommendation engines using Braze.

## Prerequisites

All recommendation types require you to have at least one [catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/) set up, as that’s where your recommended items are pulled from.

## Types of recommendations

When setting out to recommend items to your customers, there are a few approaches you can take:

- [AI Personalized](#ai)
- [Most popular](#most-popular)
- [Most recent](#most-recent)
- [Selections-based](#selections-based)
- [Rules-based](#rules-based)
- [Trending](#trending)

### AI Personalized recommendations {#ai}

As part of the [AI item recommendations][1] feature, AI Personalized recommendations take advantage of deep learning to predict what your users are most likely to be interested in next based on what they’ve shown interest in in the past. This method provides a dynamic and tailored recommendation system that adapts to user behavior.

AI Personalized recommendations use the last 6 months of item interaction data, like purchases or custom events, to build the recommendation model. For users without enough data for a personalized list, the most popular items serve as a fallback so your users are still getting relevant suggestions.

With AI item recommendations, you can also further filter the items available with 
[selections]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/). However, selections with Liquid cannot be used in AI recommendations, so keep that in mind when building your catalog selections.

For examples, see the [Use cases](#use-cases) section in this article.

{% alert tip %}
AI Personalized recommendations work best with hundreds or thousands of items and typically at least 30,000 users with purchase or interaction data. This is only a rough guide and can vary. The other recommendation types can work with less data.
{% endalert %}

### Most popular item recommendations {#most-popular}

In addition to the "AI Personalized" model, the [AI item recommendations][1] feature also includes a recommendation model for "Most popular", which features items that users engage with most.

Based on the interaction data being tracked, use cases for this model could include recommending:

- [Most popular items](#most-popular-items)
- [Most popular liked items](#liked-items)
- [Most viewed items](#most-viewed-items)
- [Popular items in users’ carts](#popular-items-in-users-carts)

### Most recent item recommendations {#most-recent}

In addition to the "AI Personalized" model, the [AI item recommendations][1] feature also includes a recommendation model for "Most recent", which features items that users engage with most. Use this model to reduce churn by encouraging lapsing users to re-engage with relevant content.

Based on the interaction data being tracked, use cases for this model could include recommending:

- [Recently clicked items](#recently-clicked-items)
- [Recently liked items](#liked-items)
- [Recently engaged with or purchased items](#recently-engaged-with-or-purchased-items)
- [Items recently added to cart](#items-recently-added-to-cart)

### Trending item recommendations {#trending}

In addition to the "AI Personalized" model, the [AI item recommendations][1] feature also includes a recommendation model for "Trending", which features items that had the most positive momentum when it comes to recent user interactions. 

Unlike the "Most Popular" model, which features items with consistently high interaction, this model features items that have experienced an uptick in interactions. You can use it to recommend products that are up-and-coming, and currently seeing increased traction.

Based on the interaction data being tracked, use cases for this model could include recommending:

- [Trending purchased items](#trending-purchased-items)
- [Trending liked items](#trending-liked-items)

### Selections-based recommendations {#selections-based}

[Selections]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) are specific groups of catalog data. When you use a selection, you're essentially setting up custom filters based on specific columns in your catalog. This could include filters for brand, size, location, date added, and more. It gives you control over what you’re recommending by allowing you to define criteria that items must meet to be shown to users.

The previous three types all involve setting up and training a recommendation model in Braze. While you can use selections in those models as well, you can also accomplish some recommendation use cases with just catalog selections and Liquid personalization.

Some use cases include recommending:

- [New items](#new-items)
- [Random items](#random-items)

### Rules-based recommendations {#rules-based}

A [rules-based recommendation]({{site.baseurl}}/rules_based_recommendations/) engine uses user data and product information to suggest relevant items to users within messages. It uses Liquid and either Braze catalogs or Connected Content to dynamically personalize content based on user behavior and attributes.

Rules-based recommendations are based on fixed logic that you must manually set. This means your recommendations won’t adjust to a user's individual purchase history and tastes unless you update the logic, therefore this method is best for recommendations that don’t need frequent updates.

Some use cases include:

- **Restock reminders:** Sending restock reminders for items with a predictable usage cycle, like monthly vitamins or weekly groceries, based on their last purchase date.
- **First-time buyers:** Recommend starter kits or introductory offers to first-time buyers to encourage a second purchase.
Loyalty programs: Highlight products that would maximize a customer’s loyalty points or rewards based on their current points balance.
- **Educational content:** Suggest new courses or content based on the topics of previously consumed or purchased materials.

## Use cases

### Items a user is most likely to purchase next

Predict and recommend the items a user is most likely to purchase next, based on purchase events or custom events related to purchases. For example:

- A travel site could suggest vacation packages, flights, or hotel stays based on a user's browsing history and previous bookings, anticipating their next travel destination and making it easier for them to plan their trip.
- A streaming platform can analyze viewing habits to recommend shows or movies a user is most likely to watch next, keeping them engaged and reducing churn rates.

{% details Requirements %}

- AI item recommendations
- Catalog of relevant items
- A method for tracking purchases, either a purchase object or custom event

{% enddetails %}

{% details How to set up %}

1. Create an [AI item recommendation]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Set the **Type** to **AI Personalized**.
3. Select your catalog.
4. (Optional) Add a selection to filter your recommendation to only relevant items.
5. Choose how you currently track purchase events and the corresponding event property.
6. Train the recommendation.
7. [Use the recommendation in messaging]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Items recently added to cart

Remind users of their interest in items that they recently added to their cart, but haven’t purchased yet. For example, an online retailer could send reminders or offer limited-time discounts on the items in their cart, encouraging users to complete their purchases before the offers expire.

{% details Requirements %}

- AI item recommendations
- Catalog of relevant items
- Custom event for added to cart

{% enddetails %}

{% details How to set up %}

1. Create an [AI item recommendation]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Set the **Type** to **Most recent**.
3. Select your catalog.
4. (Optional) Add a selection to filter your recommendation to only relevant items.
5. Choose **Custom Event** and select your custom event for added to cart from the list.
6. Train the recommendation.
7. [Use the recommendation in messaging]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Liked items

Encourage users to explore items that they’ve recently liked or items that are popularly liked, based on a custom event for likes. For example, a music streaming app could create personalized playlists or suggest new album releases based on the genres or artists a user has liked in the past, enhancing user engagement and time spent on the app.

{% details Requirements %}

- AI item recommendations
- Catalog of relevant items
- Custom event for likes

{% enddetails %}

{% details How to set up %}

1. Create an [AI item recommendation]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Set the **Type** to **Most recent**.
3. Select your catalog.
4. (Optional) Add a selection to filter your recommendation to only relevant items.
5. Choose **Custom Event** and select your custom event for likes from the list.
6. Train the recommendation.
7. [Use the recommendation in messaging]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Most popular items

Encourage users to explore popular items in your catalog based on purchases. To make sure you’re only surfacing relevant content, we recommend filtering with a selection. For example, a food delivery service could highlight top-rated dishes or restaurants within a user's area, based on the popularity of orders across the platform, encouraging trial and discovery.

{% details Requirements %}

- AI item recommendations
- Catalog of relevant items
- A purchase object or any custom event

{% enddetails %}

{% details How to set up %}

1. Create an [AI item recommendation]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Set the **Type** to **Most popular**.
3. Select your catalog.
4. (Optional) Add a selection to filter your recommendation to only relevant items. For example, the food delivery service might have a selection to filter for restaurant location or type of dish.
5. Choose how you currently track events and the corresponding event property.
6. Train the recommendation.
7. [Use the recommendation in messaging]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Most viewed items

Highlight items that have gained attention across your user base through views to encourage engagement or purchases. For example, a real estate website could display the most viewed listings in a user's search area to highlight properties that are attracting a lot of attention, potentially indicating good deals or desirable locations.

{% details Requirements %}

- AI item recommendations
- Catalog of relevant items
- Custom event for views

{% enddetails %}

{% details How to set up %}

1. Create an [AI item recommendation]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Set the **Type** to **Most popular**.
3. Select your catalog.
4. (Optional) Add a selection to filter your recommendation to only relevant items.
5. Choose **Custom Event** and select your custom event for views from the list.
6. Train the recommendation.
7. [Use the recommendation in messaging]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### New items

This scenario doesn't rely directly on user actions but rather on catalog data. You can filter for new items based on their addition date to the catalog and promote these through targeted campaigns or Canvases without needing to train a recommendation model.

For example, a tech eCommerce platform could alert tech enthusiasts about the latest gadgets or upcoming pre-orders, using filters to target items that have been recently added to the catalog.

{% details Requirements %}

- Catalog of relevant items with a field for date added

{% enddetails %}

{% details How to set up %}

1. Create a selection based on your catalog. Make sure your catalog has a time field (field with a **Data type** set to **Time**) that corresponds to the date the item was added.
2. (Optional) Add any filters if desired.
3. Make sure **Randomize Sort Order** is turned off.
4. For **Sort Field**, select your date added field.
5. Set **Sort Order** to descending.
6. [Use the selection in messaging]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#using-selections-in-messaging).

{% enddetails %}

### Popular items in users' carts

Showcase items that are added to carts by many other shoppers, providing users with a glimpse into the current trends among your offerings.

For example, a fashion retailer could promote clothes and accessories that are trending based on popular additions to carts by other customers. They can then create a dynamic "Trending Now" section on their homepage and mobile app, which updates in real-time to encourage shoppers to purchase before items sell out.

{% details Requirements %}

- AI item recommendations
- Catalog of relevant items
- Custom event for added to cart

{% enddetails %}

{% details How to set up %}

1. Create an [AI item recommendation]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Set the **Type** to **Most popular**.
3. Select your catalog.
4. (Optional) Add a selection to filter your recommendation to only relevant items.
5. Choose **Custom Event** and select your custom event for added to cart from the list.
6. Train the recommendation.
7. [Use the recommendation in messaging]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Random items

For a diverse user experience, recommending random items can introduce variety and potentially spark interest in less-visited catalog areas. This method doesn't require specific models or events but rather uses a catalog selection to ensure items are displayed randomly.

For example, an online bookstore could offer a "Surprise Me" feature, recommending a random book based on the user's past purchases or browsing habits, encouraging exploration outside of their normal reading genres.

{% details Requirements %}

- Catalog of relevant items
- Selection with **Randomize Sort Order** turned on

{% enddetails %}

{% details How to set up %}

1. [Create a selection]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#creating-a-selection) based on your catalog.
2. (Optional) Add any filters if desired.
3. Turn on **Randomize Sort Order**.
4. [Use the selection in messaging]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#using-selections-in-messaging).

{% enddetails %}

### Recently clicked items

Encourage users to revisit items that they’ve recently clicked on, based on a custom event for clicks. For example, an online fashion retailer could create a recommendation to send follow-up emails or push notifications featuring clothes that a user has shown interest in by clicking on them, encouraging the user to revisit the item and make a purchase.

{% details Requirements %}

- AI item recommendations
- Catalog of relevant items
- Custom event for clicks

{% enddetails %}

{% details How to set up %}

1. Create an [AI item recommendation]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Set the **Type** to **Most recent**.
3. Select your catalog.
4. (Optional) Add a selection to filter your recommendation to only relevant items.
5. Choose **Custom Event** and select your custom event for clicks from the list.
6. Train the recommendation.
7. [Use the recommendation in messaging]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Recently engaged with or purchased items

Promote items that users have recently interacted with, including views, clicks, or purchases. This approach keeps your recommendations fresh and aligned with the user's latest interests​. For example:

- **Education:** An online education platform could encourage users who have recently watched an educational video but haven't enrolled in a course to check out similar courses or subjects of interest to keep the user engaged and motivated to start learning.
- **Fitness:** A fitness app can suggest workouts or challenges that are similar to the ones a user has recently completed or interacted with, keeping their exercise routine varied and engaging.
- **Home improvement retailer:** After a customer purchases a power tool, a home improvement retailer can recommend related accessories or safety gear based on their recent purchase, enhancing the user's experience and safety.

{% details Requirements %}

- AI item recommendations
- Catalog of relevant items
- A purchase object or any custom event for an engagement interaction

{% enddetails %}

{% details How to set up %}

1. Create an [AI item recommendation]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
2. Set the **Type** to **Most recent**.
3. Select your catalog.
4. (Optional) Add a selection to filter your recommendation to only relevant items.
5. Choose **Custom Event** and select your custom event for clicks from the list.
6. Train the recommendation.
7. [Use the recommendation in messaging]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging).

{% enddetails %}

### Trending purchased items

Highlight items that your users have recently purchased with increased frequency. For example, an eCommerce business could recommend seasonal items that users are starting to stock up on during their preparations for the next season. 

{% details Requirements %}

- AI item recommendations
- Catalog of relevant items
- A method for tracking purchases (either a purchase object or custom event)

{% enddetails %}

{% details How to set up %}

1. Create an [AI item recommendation]({{site.baseurl}}/ai_item_recommendations/).
2. Set the **Type** to **Trending**.
3. Select your catalog.
4. (Optional) Add a selection to filter your recommendation to only relevant items.
5. Choose either a purchase event or a custom event that tracks purchases, along with the corresponding property.
6. Train the recommendation.
7. [Use the recommendation in messaging.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging)

{% enddetails %}

### Trending liked items

Highlight items that your users have recently liked with increased frequency. For example, a music app could feature up-and-coming artists who have experienced a recent surge in user likes.

{% details Requirements %}

- AI item recommendations
- Catalog of relevant items
- Custom event for tracking likes

{% enddetails %}

{% details How to set up %}

1. Create an [AI item recommendation]({{site.baseurl}}/ai_item_recommendations/).
2. Set the **Type** to **Trending**.
3. Select your catalog.
4. (Optional) Add a selection to filter your recommendation to only relevant items.
5. Choose your custom event for tracking likes, along with the corresponding property.
6. Train the recommendation.
7. [Use the recommendation in messaging.]({{site.baseurl}}/user_guide/sage_ai/recommendations/ai_item_recommendations/#using-recommendations-in-messaging/)

{% enddetails %}

[1]: {{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/
