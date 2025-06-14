---
nav_title: Use Case
article_title: Use Case Drive Content Discovery After Viewing
description: "This example shows how a fictional brand uses Braze AI item recommendations to deliver personalized content and product suggestions across key customer moments."
page_type: tutorial
---

# Use case: Drive content discovery after viewing

> This example shows how a fictional brand uses Braze AI item recommendations to deliver personalized content and product suggestions across key customer moments. Learn how recommendation logic can improve engagement, increase conversions, and reduce manual effort.

Camila is a CRM manager at MovieCanon, a fake streaming platform featuring curated films and series. 

Camila’s goal is to keep viewers engaged after they finish watching something. Historically, MovieCanon’s "You might also like" messages were based on broad genre matching and sent at arbitrary times—often hours or days after a session. Engagement was low, and her team knew they could do better.

Using [AI Item Recommendations][1], Camila sets up a system to automatically recommend new titles based on each viewer’s watching history, delivered immediately after a user finishes a film or episode. It’s a smarter, more personal way to help users discover content they’ll actually want to watch next and keep them engaged with the platform.

![In-app message reading "Next up, just for you. Because you watched "Nomads of the Sun", with an image, title name, description, and CTA to "Watch now" or "Skip" to the next recommendation.][img1]

This tutorial walks through how Camila:

- A personalized message triggered when a user finishes watching something
- Recommendations that are tailored to the viewer’s preferences—automatically pulled from MovieCanon’s catalog and inserted into the message 

## Step 1: Create a churn prediction model

Camila starts by creating a recommendation that will surface relevant titles whenever a user finishes watching something. She wants it to be dynamic, so users receive different suggestions based on what they’ve watched recently.

1. In the Braze dashboard, Camila navigates to **AI Item Recommendations**.
2. She creates a new recommendation and names it "Post-viewing suggestions".
3. For the recommendation type she chooses **AI Personalized**, so each user sees tailored recommendations based on past behaviors.
4. She selects **Do not recommend items users have previously interacted with** so users don't get recommendations for something they've already watched. 
5. She selects the catalog containing MovieCanon’s current content library. Camila doesn't add a catalog selection, since she wants all items in the catalog to be eligible items for recommendation.
6. Camila links the recommendation to the `Watched Content` custom event, which tracks completed views, and sets the **Property Name** to the content's title.
7. She creates the recommendation.

## Step 2: Set up an in-app message

Once the recommendation has finished training, Camila builds a messaging flow that reaches the user at the right moment: immediately after they finish a title. The message includes a list of three personalized suggestions pulled directly from the catalog.

1. Camila creates an in-app message campaign using the drag-and-drop editor.
2. She sets the trigger to her custom event: `Watched Content`.
3. She designs a multi-page in-app message with title images, names, and a “Watch now” CTA.

!["Add Personalization" modal open in the Braze editor, with "Item recommendation" selected as the personalization type.][img2]

{: start="4"}

4. In the message body, Camila uses the [Add Personalization modal][2] to add variables like the recommended title's name, description, and thumbnail using Liquid, which dynamically populates content from the catalog. She templates in a custom attribute for `Last Watched Movie` to let users know this recommendation is based on their watch history. 

![In-app message editor with raw Liquid to template in specific fields from catalog items from the recommendation.][img3]

{% details Show Liquid used in image %}

{% raw %}

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].name }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].description }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].thumbnail }}
```

{% endraw %}

{% enddetails %}

{: start="5"}

5. Camila then duplicates her page and increments the Liquid array {% raw %} (`{{ items[0]}}` to `{{items[1]}}`) {% endraw %} in each variable to template in the next item in the recommendation list.

## Step 3: Measure and optimize

With the campaign live, Camila monitors open rates, CTRs, and follow-up viewing behavior. She compares performance against previous static recommendation campaigns and sees higher engagement—and more content sessions per user.

She also plans to A/B test:

- Timing (immediate vs. 10 minutes post-watch)
- Content layout (carousel versus list)
- CTA variations (“Watch now” versus “Add to queue”)

By pairing event-driven messaging with AI Item Recommendations, Camila turns content discovery into an automatic, personalized experience. MovieCanon keeps users engaged without guesswork—delivering relevant content at just the right time to drive session depth and reduce churn.


[1]: {(site.baseurl)}/user_guide/brazeai/recommendations/ai_item_recommendations
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables
[3]: {{site.baseurl}}/user_guide/brazeai/recommendations/using_recommendations/#accessing-individual-items


[img1]: {% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %}
[img2]: {% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %}
[img3]: {% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %}





