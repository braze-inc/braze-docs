---
nav_title: Intelligent Selection
page_order: 1
---

# Intelligent Selection {#intelligent-selection}

Intelligent Selection is a feature that analyzes the performance of a recurring campaign or Canvas twice a day and automatically adjusts the percentage of users that receive each message variant. A variant that appears to be performing better than others will go to more users, while variants that are underperforming will be targeted at fewer users. Each adjustment is made using a [statistical algorithm][227] that makes sure we are adjusting for real performance differences and not just random chance.

By looking at performance data in real-time and shifting campaign traffic toward winning variants gradually, Intelligent Selection ensures that more users receive your best performing variant, without any sacrifice in statistical confidence. Intelligent Selection will also rule out underperforming variants and identify high performing variants faster than a traditional A/B test. With Intelligent Selection, you can test more frequently and with greater confidence that your users will see your best message.

Intelligent Selection is ideal for campaigns that are scheduled to send multiple times. As Intelligent Selection needs initial results to begin adjusting your campaign, a campaign that sends only once will not benefit. For those campaigns, an A/B test per the above instructions would be more effective.

![Intelligent_Selection_Shot][271]


[2]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[3]: https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test
[10]: #introduction-to
[20]: #what-is
[30]: #the-benefits-of
[40]: #five-rules-for
[50]: #creating-tests
[60]: #how-to-create
[70]: #what-can-you-test
[80]: #choosing-a-segment
[90]: #intelligent-selection
[100]: #including-a-control-group
[110]: #understanding-your
[120]: #understanding-confidence
[130]: #statistically-insignificant-results
[140]: #recommended-follow-ups
[150]: #recap
[160]: {% image_buster /assets/img/ab_create_1.png %}
[170]: {% image_buster /assets/img/ab_create_2.gif %}
[175]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/scheduling_your_campaign/#scheduling-your-campaign
[180]: {% image_buster /assets/img/ab_create_4.png %}
[205]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events
[210]: {% image_buster /assets/img/ab_create_8.png %}
[225]: https://www.optimizely.com/resources/sample-size-calculator/
[227]: https://en.wikipedia.org/wiki/Multi-armed_bandit
[271]: {% image_buster /assets/img/intelligent_selection1.png %}
[272]: #intelligent-selection
[273]: {{ site.baseurl }}/help/best_practices/push/message_format/
[274]: {{ site.baseurl }}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/
