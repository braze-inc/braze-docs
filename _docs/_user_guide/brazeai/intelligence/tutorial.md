---
nav_title: "Tutorial: Quick service restaurant"
article_title: Intelligence suite tutorial
page_order: 10
search_rank: 12
description: "New to the Braze intelligence suite? Start with this tutorial."
tool:
  - Dashboard
---

# Intelligence suite tutorial

> New to the Braze intelligence suite? Start with this tutorial! For more general information, see [Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence/).

## Tutorial: Quick service restaurant

Let's pretend we work at SandwichEmperor, a fast food restaurant that has a new limited-time menu item: the Royal Roast. We'll use two Intelligence Suite features to send personalized promotions in a Canvas.

### Step 1: Use Intelligent Timing for when to send notifications

We'll use Intelligent Timing to analyze our users' past interactions with our app and each messaging channel, then automatically select the best time to promote the Royal Roast to each user. Some users might receive the promotion in the afternoon, while others might receive it in the evening. 

We'll provide a fallback time for users who don't have enough past interactions to analyze: the most popular time to use the app among all users.

![Intelligent Timing delivery settings for a Message step.]({% image_buster /assets/img/intelligence_suite1.png %})

### Step 2: Use Intelligent Selection to select the promotion

For the actual promotional messages, we'll use Intelligent Selection to test three different messages (push notification, email, and SMS) for the Royal Roast. Intelligent Selection will analyze the performance of all our promotional messages twice a day, then gradually send more of the best-performing messages and less of the others.

After Intelligent Selection gathers enough data to determine the best-performing message, it will use that message in 100% of future sends.

![A/B Testing section of a Canvas with Intelligent Selection enabled.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### Step 3: Launch the Canvas

With both Intelligent Timing and Intelligent Selection, we've set up our Royal Roast promotions to be optimized for timing and messaging. We can launch our Canvas and watch as our sends shift to accommodate user preferences.
