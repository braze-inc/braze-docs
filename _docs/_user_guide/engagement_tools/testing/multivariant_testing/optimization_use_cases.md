---
nav_title: Use Cases
article_title: Winning Variant and Personalized Variants Use Cases
description: "This example shows how a fictional brand uses Braze AI item recommendations to deliver personalized content and product suggestions across key customer moments."
page_order: 20
page_type: tutorial
---

# Winning Variant and Personalized Variants use cases

> These examples show how fictional brands use Braze Winning Variant and Personalized Variant to optimize messaging with less guesswork. Instead of relying on manual A/B tests or broad segmentation, marketers use BrazeAI™ to automatically determine the best-performing messages—either for the audience as a whole or for each individual recipient.

## Use case: Personalize push messaging tone

**Feature:** [Personalized Variant][1]

Lina is a campaign strategist at PamperHer, a fake beauty and skincare brand with a loyal but diverse customer base.

She’s planning a one-time push campaign for PamperHer’s spring weekend sale. Her goal is to drive clicks—but she knows a single tone won’t work for everyone. Some customers prefer gentle, self-care messaging, while others respond better to direct value.

In the past, she might have split her audience manually or gone with whichever message felt strongest. This time, she uses Personalized Variant, which automatically delivers the version of the message each user is most likely to engage with—based on their historical behavior and profile traits.

This tutorial walks through how Lina:

- Created a push campaign with two message tones
- Used Personalized Variant to optimize delivery per user
- Reviewed results to understand performance and plan what's next

### Step 1: Create a push campaign with Personalized Variant optimization

1. Lina creates a new [push campaign][3].
2. She adds two variants and generates content for them using the AI copywriting assistant and her team's default [brand guidelines][4]:
   - **Variant 1:** Routine-focused tone
      - Title: Your skincare routine, simplified
      - Message: Cleanse, treat, and moisturize with dermatologist-backed essentials—no guesswork needed.
   - **Variant 2:** Self-care tone
      - Title: Take time for you
      - Message: Whether it’s five minutes or a full evening, our calming formulas help you recharge.

![][img1]

{: start="3"}

3. In the **Target Audiences** step, Lina sets the **Optimization** method for her campaign to **Personalized Variant**.

![][img2]

{: start="4"}

4. She sets the success metric to her primary conversion event "Starts Session", since her goal is to drive engagement to the app.
5. She selects her target segment and schedules the campaign to send once on Friday at noon, when engagement is typically highest.

### Step 2: Launch the campaign and let Braze personalize delivery

When the campaign launches, Braze begins by sending both variants randomly to a subset of the audience. It analyzes each recipient’s traits—like prior engagement, purchase history, and lifecycle stage—to understand which version drives more clicks for which types of users.

Once the model gathers enough signal, Braze begins personalizing delivery for the rest of the audience—matching each user to the variant they’re most likely to engage with. There is no single “winning” variant. Instead, every user receives a version that’s tailored to how they interact with the brand.

### Step 3: Review results and apply insights

After the campaign sends, Lina opens the **A/B Test Result** view in her campaign's analytics to see how each message variant performed.

She starts with the **Initial Test** tab. Braze shows her how both variants performed when sent randomly to the test group—20% of her total audience. Variant 1 had a slightly higher click rate (almost 60%) and a higher conversion rate (9.83%) than Variant 2 (55% click, 7.98% conversion), with a confidence score of 96.35%.

![][img3]

At this point, Lina could have picked Variant 1 as the winner. But because she chose Personalized Variant, Braze didn’t stop there—it used the initial results to learn which types of users were more likely to engage with each message. 

Lina reviews the custom event impact table, showing which past actions correlated with message preference. She sees:

- Users who had previously opened promotional emails or applied coupons were more likely to get the routine-focused variant
- Users who had interacted with wellness content or browsed blog posts leaned toward the self-care tone

She switches to the **Personalized Variant** tab. There, she sees:

- A projected lift of **12%** in overall click-through rate compared to sending just the top-performing variant to everyone
- A delivery breakdown showing how Braze personalized message selection across the remaining 80% of users

This gives Lina a clear picture of how each variant performed, and why. She now has evidence-backed guidance for how tone preferences show up across different user traits, helping her build more personalized campaigns moving forward. She uses these learnings to refine future creative and considers running a follow-up test with additional variants—or even extending personalization to other channels like in-app messages.

With Personalized Variant, Lina moves beyond assumptions. Every message feels more relevant, and her team now has a scalable strategy for optimizing tone—one user at a time.

## Use case: Test CTA wording to drive clicks

<!-- Arjun uses they/them pronouns -->

**Feature:** [Winning Variant][2]

Arjun is a lifecycle marketing lead at Decorumsoft, a fake mobile game publisher known for role-based adventures. 

They're launching a one-time email campaign to announce a new in-game feature: the Marketplace, where users can browse and redeem collectibles. Arjun's goal is to drive highly engaged players into the Marketplace—but what’s the right way to frame the call to action?

In the past, their team used CTAs like “Start exploring” or “See what’s new,” but click rates were inconsistent. Some team members believe direct prompts work best—others prefer a softer approach. Rather than pick one version and hope for the best, Arjun uses Winning Variant, which lets Braze automatically test both CTAs with a subset of users and scale the best performer to the rest of the audience.

This tutorial walks through how Arjun:

- Sets up a multivariate test focused on CTA performance
- Lets Braze select and scale the top performer automatically
- Applies results to future campaigns for long-term gains

### Step 1: Build a multivariate campaign

1. Arjun creates a new email campaign.
2. They start by building two message variants for their Marketplace announcement. They are intentionally changing only one variable to keep the test clean. The body, header, and visuals are the same—but the CTA differs:
   - **Variant A:** CTA reads “Enter the Marketplace”
   - **Variant B:** CTA reads “Browse Items”

![][img4]{:style="max-width: 80%; border:none"}

{: start="3"}

3. In the Target Audiences step, Arjun sets the **Optimization** method to **Winning Variant**.
4. They choose **Unique Clicks** as the success metric—because their goal is to get users to click through to the marketplace.
5. They set the distribution:
   - 50% of the audience for testing (25% each variant)
   - 50% of the audience to receive the Winning Variant

![][img5]

{: start="6"}

6. Arjun selects a segment of highly engaged users and schedules the campaign to go out at 10 AM on a Saturday, a high-traffic time for gameplay re-engagement.

### Step 2: Launch and let Braze select the winner

When the campaign launches, Braze begins by randomly assigning the two variants to the test group. As users engage, Braze collects real-time performance data—specifically, which version drives more unique clicks.

Once enough data is collected, Braze automatically scales the top performer to the remaining 50% of users—no need for Arjun to log in and choose.

### Step 3: Review and reuse the best CTA

After the campaign wraps, Arjun checks performance in the campaign’s A/B Test Results view.

They see that “Enter the Marketplace” drove a 22% higher *Unique Click Rate* than “Browse Items,” with a confidence score of 97%. This gives Arjun a clear signal: action-oriented language outperformed softer phrasing in this context.

While only the Winning Variant was scaled, both provided insight into what resonates with users. Arjun uses this data to update his messaging guidelines and plans to reuse the stronger CTA in future promotions. Next, they plan to use [funnel reporting][5] to explore how clicks translate into purchases in the marketplace.




[1]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/#personalized-variant
[2]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/#winning-variant
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message
[4]: {{site.baseurl}}/user_guide/brazeai/generative_ai/brand_guidelines
[5]: {{site.baseurl}}/user_guide/analytics/reporting/funnel_reports


[img1]: {% image_buster /assets/img/ai_use_cases/tone_testing_variants.png %}
[img2]: {% image_buster /assets/img/ai_use_cases/ab_test_personalized_variant.png %}
[img3]: {% image_buster /assets/img/ai_use_cases/winning_variant_results.png %}
[img4]: {% image_buster /assets/img/ai_use_cases/cta_testing_variants.png %}
[img5]: {% image_buster /assets/img/ai_use_cases/ab_test_winning_variant.png %}