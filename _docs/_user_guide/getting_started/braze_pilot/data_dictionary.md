---
nav_title: Data Dictionary
article_title: Data Dictionary for Braze Pilot
page_order: 3
page_type: reference
description: "This reference article briefly covers the integration steps required from your engineers or developers."
---

# Data dictionary

> Each app simulation in Braze Pilot is instrumented to collect a variety of events and attributes based on user activity in the app. 

## The approach to data

The app logs custom attributes and events typical of the industry represented by the fictional brand. You can use these attributes to power demos for a variety of common use cases. 
Generally, all events and attributes are prefixed with a short code that corresponds to the app simulation responsible for the data. For example:

- All data logged by the Steppington app simulation are prefixed with `st_`
- All data logged by the PantsLabyrinth app simulation are prefixed with `pl_`
- All data logged by the MovieCanon app simulation are prefixed with `mc_`

## List of logged events and attributes

The following table lists the events and attributes logged by Braze Pilot.

| Name | App | Type | Properties | When it's logged |
|---|---|---|---|---|
| `mc_entered_app` | MovieCanon | Event |  | When the user enters the MovieCanon app |
| `mc_watched_movie` | MovieCanon | Event | `title: string` | When the user finishes watching a video |
| `mc_viewed_movie_page` | MovieCanon | Event | `title: string` | When the user views a movie page |
| `pl_viewed_item` | PantsLabyrinth | Event | `item_name: string` | When the user views a product page |
| `pl_entered_app` | PantsLabyrinth | Event |  | When the user enters the PantsLabyrinth app |
| `pl_added_item_to_wishlist` | PantsLabyrinth | Event | `item_name: string` | When the user adds an item to their wish list |
| `pl_added_item_to_cart` | PantsLabyrinth | Event | `item_name: string` | When the user adds an item to their cart |
| `<purchase_event>` | PantsLabyrinth | Event | `name: string` <br> `price: number` | When the user completes a purchase |
| `st_entered_app` | Steppington | Event |  | When the user enters the Steppington app |
| `st_completed_class` | Steppington | Event | `class_type: string`<br>`calories_burned: number`<br>`workout_length: number` | When the user completes a workout |
| `st_viewed_premium_benefit` | Steppington | Event | `benefit_type: string` | When the user visits the Steppington+ tab (if it's enabled with feature flag) |
| `st_viewed_class` | Steppington | Event | `class_type: string` | When the user visits a workout page |
| `st_completed_class` | Steppington | Event | `class_type: string` <br> `calories_burned: number` <br> `workout_length: number` | When the user completes a workout |
| `st_most_recent_completed_class` | Steppington | Attribute | `string` | When the user completes a workout |
| `st_favorited_class` | Steppington | Event | `class_type: string` | When the user favorites a class |
| `st_unfavorited_class` | Steppington | Event | `class_type: string` | When the user unfavories a class |
| `st_started_free_trial` | Steppington | Event |  | When the user selects the **Start Free Trial** button |
| `st_set_goal` | Steppington | Event | `goal_name: string`<br>`goal: number`<br>`units: string` | When the user selects the **Start Free Trial** button. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }