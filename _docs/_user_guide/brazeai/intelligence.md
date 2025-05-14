---
nav_title: Intelligence Suite
article_title: Intelligence Suite
page_order: 10
layout: dev_guide
search_rank: 12
guide_top_header: "Intelligence Suite"
guide_top_text: "The Braze Intelligence Suite helps you automate decision-making with data-based insights. From delivery time to multivariate testing, brands can use these tools and features to create dynamic, cross-channel experiences that optimize at scale. <br> <br> The Intelligence Suite comprises of three main features: Intelligent Timing, Intelligent Channel, and Intelligent Selection."
description: "The Braze Intelligence Suite helps you automate decision-making with data-based insights. From delivery time to multivariate testing, brands can use these tools and features to create dynamic, cross-channel experiences that optimize at scale."

Tool:
  - Dashboard

guide_featured_title: "Tools and features"
guide_featured_list:
- name: Intelligent Timing
  link: /docs/user_guide/brazeai/intelligence/intelligent_timing/
  image: /assets/img/braze_icons/clock.svg
- name: Intelligent Channel
  link: /docs/user_guide/brazeai/intelligence/intelligent_channel/
  image: /assets/img/braze_icons/mail-04.svg
- name: Intelligent Selection
  link: /docs/user_guide/brazeai/intelligence/intelligent_selection/
  image: /assets/img/braze_icons/hearts.svg

guide_menu_title: "Additional resources"
guide_menu_list:
- name: Intelligence FAQ
  link: /docs/user_guide/brazeai/intelligence/faqs/
  image: /assets/img/braze_icons/annotation-question.svg


---

## Use cases

The Intelligence Suite provides powerful features to analyze user history and campaign and Canvas performance, then make automatic adjustments to increase engagement, viewership, and conversions. For a few examples of how these features can benefit different industries, see the below use cases.

### eCommerce

- **Flash sales:** Use the [Intelligent Channel filter]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) to study user history to identify the users who are more responsive to push notifications versus emails, then send push notifications and emails to the respective users. Optionally, select a specific channel for users who don't have enough data to determine their preferred channel.
- **Promotional banners:** Use [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/) to analyze the performance of different promotional banners in a recurring campaign, then automatically select and send the banner that generates the highest click-through rates.

### Travel

- **Package offers:** Use Intelligent Selection to test different travel package offers in a recurring Canvas and gradually shift Canvas traffic to the best-performing variant to drive higher booking rates.
- **Travel deals:** Use the Intelligent Channel filter to send personalized travel deals through a user's most active channel, such as email or SMS, maximizing the likelihood of them engaging with your messaging.

### Entertainment

- **New content promotion:** Use [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) to send notifications about new movies, shows, music, and other types of content when users are most likely to open your messaging.
- **In-game purchases:** Use Intelligent Selection to test different promotional messages for in-game purchases and automatically select the one that generates the highest conversion rates.

### Quick service restaurant

Let's pretend we work at SandwichEmperor, a fast food restaurant that has a new limited-time menu item: the Royal Roast. We'll use two Intelligence Suite features to send personalized promotions in a Canvas.

#### Use Intelligent Timing for when to send notifications

We'll use Intelligent Timing to analyze our users' past interactions with our app and each messaging channel, then automatically select the best time to promote the Royal Roast to each user. Some users might receive the promotion in the afternoon, while others might receive it in the evening. 

We'll provide a fallback time for users who don't have enough past interactions to analyze: the most popular time to use the app among all users.

![Intelligent Timing delivery settings for a Message step.][1]

#### Use Intelligent Selection to select the promotion

For the actual promotional messages, we'll use Intelligent Selection to test three different messages (push notification, email, and SMS) for the Royal Roast. Intelligent Selection will analyze the performance of all our promotional messages twice a day, then gradually send more of the best-performing messages and less of the others.

After Intelligent Selection gathers enough data to determine the best-performing message, it will use that message in 100% of future sends.

![A/B Testing section of a Canvas with Intelligent Selection enabled.][3]

#### Launch the Canvas

With both Intelligent Timing and Intelligent Selection, we've set up our Royal Roast promotions to be optimized for timing and messaging. We can launch our Canvas and watch as our sends shift to accommodate user preferences.

[1]: {% image_buster /assets/img/intelligence_suite1.png %}
[3]: {% image_buster /assets/img_archive/canvas_intelligent_selection.png %}
