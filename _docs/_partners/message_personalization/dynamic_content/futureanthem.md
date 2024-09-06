---
nav_title: Future Anthem
article_title: Future Anthem
description: "Learn how to integrate Future Anthem with Braze."
alias: /partners/futureanthem/
page_type: partner
search_tag: Partner
layout: dev_guide
---

# Future Anthem

Future Anthem's all-in-one product for the real money gaming industry, Amplifier AI, delivers content personalization, real-time experiences, and dynamic audiences. Amplifier AI works seamlessly across sports, casino, and lottery.

Amplifier AI and Braze's integration allows customers to enhance Braze's player profiles with industry-specific player attributes from Amplifier AI (e.g. favorite game, favorite team, engagement score, next bet recommendation, expected next bet, etc.)

The integration is currently in Early Access. Please reach out to your Future Anthem Customer Success Team to get started.

## Prerequisites

| Requirement              | Description                                            |
|--------------------------|--------------------------------------------------------|
| Future Anthem Account    | A Future Anthem account is required to ingest our data points |
| Braze REST API key       | A Braze REST API key with the following permissions: {::nomarkdown}<ul><li><code>users.export.ids</code></li></ul>{:/} <br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint      | Your Braze [REST endpoint](https://www.braze.com/docs/developer_guide/rest_api/basics/#endpoints) that corresponds to your instance (such as rest.iad-01.com) |


## Use Cases

- Identify users with high engagement scores and target them with personalized offers, such as exclusive promotions or VIP rewards.
- If a user enjoys a specific game, suggest similar games they might like.

## Integration

Reach out to your Future Anthem Customer Success Team to identify the most relevant attributes to send to Braze for your specific use cases.

![A screenshot of a sports game](images/image1.png)
![A screenshot of a computer](images/image2.png)

## Braze Custom Attributes


{% tabs local %}
{% tab Bet Recommendations %}

| Subcategory | Example | Datatype |
| ------- | ----------- |----------- |
| User preferences | Favorite: Sport, League, Market, Team, Player| Array |
| Single bet recommendations | Sports, Leagues, Events, Markets| Array |
| Accumulator bet recommendations | xx | xx |
| Bet builder recommendations | xx | xx |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Bonus Recommendations %}

| Subcategory | Example | Datatype |
| ------- | ----------- |----------- |
|NGR – Net Gaming revenue for the user’s lifetime | Favorite: Sport, League, Market, Team, Player| Array |
| NGR14 – Net Gaming revenue for the last 14 days of activity | x | x
| Player Profitability score| x | Array |
| Engagement Score | xx | xx |
| Churn Risk Score | xx | xx |
| Estimated Next Bet Date | xx | xx |
| Bet and Get - Bonus value recommendation | xx | xx |
| Other bonus value recommendations in the future | xx | xx |
| Future CLTV  | xx | xx |

{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Game Recommendations %}

| Subcategory | Example | Datatype |
| ------- | ----------- |----------- |
| Recommended For You | Favorite: Sport, League, Market, Team, Player| Array |
| Favourite Games | x | x
| Recommended New Games | x | Array |
| Players Like You Are Playing (Collaborative Filtering) | xx | xx |
| Because You Played (Game Similarity)| xx | xx |
| Up Next (Game Sequencing) | xx | xx |
| Popular Games | xx | xx |
| Trending Games | xx | xx |

{: .reset-td-br-1 .reset-td-br-2}
{% endtab %}

{% tab Player Cluster %}

| Subcategory | Example | Datatype |
| ------- | ----------- |----------- |
| Showcase what cluster the player is in | High Value Game Diverse| xx |
{: .reset-td-br-1 .reset-td-br-2}
{% endtab %}

{% tab Player Sustain (Player potential risk) %}

| Subcategory | Example | Datatype |
| ------- | ----------- |----------- |
| Risk Score | High Value Game Diverse| xx |
| Risky Player | High Value Game Diverse| xx |
{: .reset-td-br-1 .reset-td-br-2}
{% endtab %}
{% endtabs %}

More details on each attribute can be found in [Future Anthem's documentation](https://knowledge.futureanthem.com/getting-started).





