---
nav_title: Catalogs
article_title: Catalogs
page_order: 6
layout: dev_guide

guide_top_header: "Catalogs"
guide_top_text: "Catalogs access data from imported CSV files and API endpoints to enrich your messages, similar to how you'd access custom attributes or custom event properties through Liquid."

description: "This landing page is home to catalogs. Use catalogs and filtered sets to leverage non-user data in your Braze campaigns to send personalized messages."

guide_featured_title: "Section articles"
guide_featured_list:
- name: Creating a Catalog
  link: /docs/user_guide/data/activation/catalogs/catalog/
  image: /assets/img/braze_icons/users-01.svg
- name: Using Catalogs
  link: /docs/user_guide/data/activation/catalogs/using_catalogs/
  image: /assets/img/braze_icons/users-01.svg
- name: Back-In-Stock Notifications
  link: /docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Price Drop Notifications
  link: /docs/price_drop_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Selections
  link: /docs/user_guide/data/activation/catalogs/selections/
  image: /assets/img/braze_icons/list.svg
- name: Catalogs API Endpoints
  link: /docs/api/endpoints/catalogs/
  image: /assets/img/braze_icons/server-01.svg

guide_menu_title: "Other articles"
guide_menu_list:
- name: Drag-and-Drop Product Blocks
  link: /docs/dnd_product_blocks/
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## Catalog use cases

You can bring in any type of data into a catalog. Typically, the data is metadata about offerings, such as products, discounts, promotions, events, and similar. See the use cases below for a few examples of how you can use this data to target users with highly relevant messaging.

### Retail and eCommerce

- **Seasonal promotions:** Import seasonal product collections and personalize messages to reflect current trends.
- **Localized messages:** Import your physical location addresses, hours, and services, then personalize notifications based on user locations.
- **Back-in-stock notifications:** Import product information that includes inventory quantity, then use [back-in-stock notifications]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/) and Braze custom events to trigger a campaign or Canvas that sends users a notification that a product is now stocked.
- **Price drop notifications:** Import product information that includes product prices, then use [price drop notifications]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/) and Braze custom events to trigger a Canvas that sends users a notification that a product's price dropped.

### Entertainment

- **Subscription plans:** Import subscription plans and promote add-ons to your users based on their usage patterns and the types of content they most often consume.
- **Upcoming events:** Import upcoming event listings and their locations and audience ages, then send personalized notifications to users who are within the area and of the target ages.
- **Media preferences:** Import information about movies and shows, then recommend content to your users based on their favorited titles and most-watched genres.

### Travel and hospitality

- **Destinations:** Import travel destinations and their most popular attractions, restaurants, and activities, then personalize recommendations to your users based on their previous trips.
- **Accommodations:** Import hotel properties and their amenities, room types, and pricing, then send promotions to your users based on their selected preferences.
- **Travel methods**: Import deals and promotions for travel modes (such as flights, trains, rental cars, and others), then send them to your users based on their recent search history.
- **Meal preferences:** Import information about meal offerings and use [selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) to send personalized messages to users who have specific meal preferences based on their most recently viewed food category.

## How catalogs and Liquid work together

Catalogs are a data storage feature. They contain large sets of data that can be referenced in your messages for personalization. To actually reference the data, you'll use [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) as the templating language. In other words, catalogs is storage where the data is held, and Liquid is the language that pulls the relevant data from the storage.

For examples of how you can use Liquid to pull catalog information, see the additional use cases in [Creating a catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#additional-use-cases/).

#### Data storage limitations

Data storage for catalogs is limited based on the size of the catalog items, which may be different from the sizes of uploaded CSV files.

For the free version of catalogs, the amount of storage allowed is up to 100&nbsp;MB. You can have unlimited items as long as the storage space does not exceed 100&nbsp;MB.

For Catalogs Pro, The storage size options are: 5&nbsp;GB, 10&nbsp;GB, 15&nbsp;GB or 50&nbsp;GB. Note that the free version's storage (100&nbsp;MB) is included in each of these plans.
