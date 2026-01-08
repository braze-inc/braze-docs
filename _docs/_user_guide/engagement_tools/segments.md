---
nav_title: Segments
article_title: Segments
page_order: 1
layout: dev_guide
guide_top_header: "Segments"
guide_top_text: "Audience segmentation is key to strategic marketing—it can keep you from over-targeting, bothering, or missing a potential connection with a customer. View the following articles to learn how to segment and filter your audience to your (and their) greatest benefit."
descriptions: "Audience segmentation is key to strategic marketing—it can keep you from over-targeting, bothering, or missing a potential connection with a customer. Check out this landing page to learn how to segment and filter your audience to your (and their) greatest benefit."
search_rank: 4
tool: Segments
page_type: landing
description: "This landing page covers articles on Segmentation within dashboard campaigns. Here, you can find information on how to set up a segment, filters, funnels, insights, extensions, and more."

guide_featured_title: "Popular articles"
guide_featured_list:
  - name: Create a Segment
    link: /docs/user_guide/engagement_tools/segments/creating_a_segment/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Manage Segments
    link: /docs/user_guide/engagement_tools/segments/managing_segments/
    image: /assets/img/braze_icons/edit-05.svg
  - name: Segmentation Filters
    link: /docs/user_guide/engagement_tools/segments/segmentation_filters/
    image: /assets/img/braze_icons/flag-02.svg
  - name: Segment Data
    link: /docs/viewing_and_understanding_segment_data/
    image: /assets/img/braze_icons/pie-chart-01.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: Segment Insights
    link: /docs/user_guide/engagement_tools/segments/segment_insights/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Segment Extension
    link: /docs/user_guide/engagement_tools/segments/segment_extension/
    image: /assets/img/braze_icons/users-01.svg
  - name: SQL Segments
    link: /docs/sql_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: Catalog Segments
    link: /docs/catalog_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: User Profiles
    link: /docs/user_guide/engagement_tools/segments/user_profiles/
    image: /assets/img/braze_icons/users-01.svg
  - name: Location Targeting
    link: /docs/user_guide/engagement_tools/segments/location_targeting/
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: Regular Expressions
    link: /docs/user_guide/engagement_tools/segments/regex/
    image: /assets/img/braze_icons/search-sm.svg
  - name: Suppression Lists
    link: /docs/user_guide/engagement_tools/segments/suppression_lists/
    image: /assets/img/braze_icons/list.svg 
  - name: Measuring Segment Size
    link: /docs/user_guide/engagement_tools/segments/measuring_segment_size/
    image: /assets/img/braze_icons/pie-chart-02.svg
  - name: Troubleshooting
    link: /docs/user_guide/engagement_tools/segments/troubleshooting/
    image: /assets/img/braze_icons/annotation-question.svg

guide_menu_title2: "Other"
guide_menu_list2:
  - name: Custom Attributes
    link: /docs/user_guide/data/custom_data/custom_attributes/
    image: /assets/img/braze_icons/table.svg

---

## About Braze segments

In Braze, segments are dynamic groups of users that fit specific criteria you define, such as user attributes, user behavior, and custom events. You can get granular with criteria by nesting segments within other segments and applying additional features, narrowing the scope of your audience so you can send highly personalized and engaging content to the right users.

You can create as many segments as you like to target users. Explore different combinations of segment features and segmentation filters to discover creative ways to utilize your user data, and unlock new ways to send relevant messages to users and increase engagement.

Check out the use cases below for a small preview of how Braze segments can help you target your users.

### Use cases

- **Welcome messages:** Segment new users so you can send onboarding emails or in-app messages that introduce them to your app.
- **Loyalty rewards:** Segment users based on their purchase frequency, membership anniversary, or other milestones, and send exclusive offers or rewards to your most loyal users.
- **Behavioral triggers:** Segment users based on their user actions, such as abandoning a cart at checkout, to trigger in-app messages or push notifications.
- **Item recommendations:** Segment users who purchased specific products and send them recommendations for complementary or higher-tier products.
- **A/B testing:** Segment users for A/B testing different messages, subject lines, or content to determine what resonates best with users of specific ages, genders, and other attributes.

#### Segment Extension use cases

You can further refine your segments by using [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) to target users based on custom event or purchase behavior stored for the lifetime of their user profile.

- **Historical purchases:** Segment users by whether they purchased a specific color of a specific product at least twice in the past two years.
- **Events and message interactions:** Segment users by whether they made a purchase in the last thirty days and also interacted with a specific in-app message.
- **Query data:** 
  - **Query Snowflake:** Segment users with data combined from Braze and external sources, such as a CRM or a data warehouse, by using [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) to query Snowflake.
  - **Sync from data warehouse:** Segment users with data directly synced from your data warehouse or file storage system to Braze by using [CDI Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

