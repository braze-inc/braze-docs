---
nav_title: "A/B testing"
article_title: "A/B testing"
page_order: 6
layout: dev_guide
guide_top_header: "A/B testing"
guide_top_text: "Run experiments to optimize your messaging. An A/B test compares users' responses to multiple versions of the same campaign, while a multivariate test extends this to two or more variables. In Braze, the terms are used interchangeably because the setup process is the same. Use A/B testing with <a href='/docs/user_guide/brazeai/intelligence/intelligent_selection/'>Intelligent Selection</a> to automatically optimize your results."

page_type: landing
description: "Set up and analyze A/B tests and multivariate experiments in Braze."

guide_featured_title: "Section articles"
guide_featured_list:
  - name: Concepts
    link: /docs/user_guide/messaging/ab_testing/concepts/
    image: /assets/img/braze_icons/lightbulb-02.svg
  - name: Create tests
    link: /docs/user_guide/messaging/ab_testing/create_tests/
    image: /assets/img/braze_icons/plus-circle.svg
  - name: Optimizations
    link: /docs/user_guide/messaging/ab_testing/optimizations/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Analytics
    link: /docs/user_guide/messaging/ab_testing/analytics/
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: FAQ
    link: /docs/user_guide/messaging/ab_testing/faq/
    image: /assets/img/braze_icons/annotation-question.svg
---

## When to use A/B testing

- **Trying a new messaging type:** Experiment and learn what resonates with your users.
- **Onboarding campaigns or recurring sends:** Ensure high-traffic campaigns are as effective as possible.
- **Multiple message ideas:** Run a test and make a data-driven decision.
- **Challenging assumptions:** Test whether conventional marketing tactics actually work for your specific audience.

## Tips

- **Use large samples** to ensure results reflect your average user and aren't swayed by outliers.
- **Randomize test groups** so that differing response rates reflect message differences, not sample differences.
- **Know what you're testing.** Isolating a single change identifies which element had the greatest impact; testing multiple differences lets you compare broader approaches.
- **Set a test duration upfront** and don't end the test early, even if early results look promising.
- **Add tests before launch.** Adding a test to a running campaign produces inaccurate results. Clone the campaign, stop the original, and add the test to the clone.
- **Include a [control group]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/#including-a-control-group)** to measure impact versus sending no message at all.

### Variant distribution

{% multi_lang_include multivariant_testing.md section='Variant distribution' %}
