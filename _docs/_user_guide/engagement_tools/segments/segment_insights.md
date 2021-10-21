---
nav_title: Segment Insights
article_title: Segment Insights
page_order: 4
page_type: tutorial
tool: 
  - Segments
  - Reports
description: "This how-to article will walk you through how to use, interpret, and share Segment Insights."
---
# Segment insights

> This how-to article will walk you through how to use, interpret, and share Segment Insights. 
> <br>
> <br> 
> These insights can be used to target users and develop effective marketing campaigns.


![Segment Insights Dash][1]

Segment Insights allows you to quickly and easily see how a segment is performing compared to another across a set of pre-selected KPIs. From the segment section of your dashboard, clicking on the “Segment Insights” button in the top right of the page brings you to a screen where up to four different segments can be compared against a baseline. The baseline can either be a specific segment you select or the stats for all of your users.  Currently, Braze can compare the following statistics on the Segment Insights page:

| Measurement | Description | Formula |
| --------------------- | ------------- | ------------- |
| Session Frequency | Average number of segment users' sessions per day | (total # of sessions)/(# days since first session) |
| Time Since First Session | Average time between segment users' first session and now | today - date of first session |
| Time Since Last Session | Average time between segment users' last session and now | today - date of last session |
| Lifetime Revenue | Average lifetime revenue for segment users | user lifetime spend |
| Time to First Purchase | Average time between segment users' first session and first purchase | date of first purchase - date of first session |
| Time Since Last Purchase | Average time between segment users' last purchase and now | today - date of last purchase |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

You can easily share specific comparisons with the page’s unique URL, and users can also click beneath each segment to reveal more information about that segment. These comparisons will reset when a user changes app groups.

![Segment Insights Expanded][2]

Segment Insights have also been built right into the segment details view. When looking at a particular segment you’ve previously set up, you can find the same six statistics outlined within the dynamic, grey Segment Statistics box. From here, you can quickly launch the Segment Insights tool to compare this particular segment with any others you’ve previously set up, but note that this will overwrite any segments you've previously selected within the Segment Insights tool.

![Segment Insights Details][3]

## Sample use cases {#insights-use-cases}

### Comparing demographic usage and purchasing patterns

One of the best usages of Segment Insights is answering questions about the impact of user demographics on app usage and campaign effectiveness, such as:

- Are certain user demographics performing significantly better or worse than average?
- Should I rethink the localization of a particular campaign?
- Is a campaign engaging a certain demographic?
- What goals should I set for a campaign aimed at a certain demographic?

Segment Insights can help uncover differences between user demographics. The example below shows a comparison of an app's user base by their language, illustrating how English speakers tend to have a higher LTV and activity levels than speakers of other languages.

![Segment Insights by Language][5]

Notice that on average, German speakers signed up longer ago, which might explain why they're no longer as active. This could be due to a multitude of factors, for example if the app first launched in Europe but is now more popular in the U.S., where most people speak English or Spanish. For more robust findings, when analyzing KPIs across demographics, it's sensible to test the findings from a general study of demographics (e.g. if language impacts LTV in all users) by looking at a smaller, more similar population and seeing if the findings persist.

To improve conversions among speakers of languages other than English, a good first step would be to [localize campaigns][10] to the user's device language and making sure that the copy of those messages is engaging users by using a [multivariate campaign][11] to test different versions of the foreign language copy.

### Understanding indicators of higher revenue

Getting users to convert to purchasers can be difficult, and trying to push new, inactive or disengaged users directly toward purchasing may lead the user to uninstall your app. Segment Insights can help you discover actions that lead users further down the purchase funnel without requiring them to purchase just yet, for example, adding items to their wish list, sharing on social media or favoriting content. Below is an example charting out the impact on purchases different behaviors within an e-commerce app.

![User Actions contributing to purchases][7]

We can see that relatively few users are currently signed up for the newsletter, but these users are generally more active. To keep new users engaged, it would be a good idea to include an invitation to order the newsletter in onboarding campaigns. To re-engage lapsed users, a good plan would be to send out a typical [lapsed user campaign][9] and [target users who converted][12] with a subsequent campaign to sign up for the newsletter.

[1]: {% image_buster /assets/img_archive/segment_insights.png %}
[2]: {% image_buster /assets/img_archive/Segment_Insights_Info.png %}
[3]: {% image_buster /assets/img_archive/Segment_Segment_Insights.png %}
[5]: {% image_buster /assets/img_archive/Segment_Language_Insights.png %}
[7]: {% image_buster /assets/img_archive/Segment_Insights_Events1.png %}
[8]: {{site.baseurl}}/help/best_practices/user_onboarding/#user-onboarding
[9]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/capturing_lapsing_users/#capturing-lapsing-users
[10]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[11]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#creating-tests
[12]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#converted-from-campaign-filter
