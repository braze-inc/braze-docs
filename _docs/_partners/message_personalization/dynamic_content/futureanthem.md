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
| Future Anthem Account    | A Future Anthem account is required |
| Braze REST API key       | A Braze REST API key with the following permissions: {::nomarkdown}<ul><li><code>users.track</code></li></ul>{:/} <br>This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint      | Your Braze [REST endpoint](https://www.braze.com/docs/developer_guide/rest_api/basics/#endpoints) that corresponds to your instance (such as rest.iad-01.com) |


## Use Cases

- Identify users with high engagement scores and target them with personalized offers, such as exclusive promotions or VIP rewards.
- If a user enjoys a specific game, suggest similar games they might like.

## Integration

Reach out to your Future Anthem Customer Success Team to identify the most relevant attributes to send to Braze for your specific use cases.

![A screenshot of the attributes on the user's profile.]({% image_buster /assets/img/futureanthem/fa_image1.png %})
![A screenshot of the object attribute.]({% image_buster /assets/img/futureanthem/fa_image2.png %})

## Braze Custom Attributes


{% tabs local %}
{% tab Bet Recommendations %}

| Subcategory | Example | Datatype |
| ------- | ----------- |----------- |
| User Preferences | ```json {"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}| Object |
| Single Bet Recommendations | ```json {"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}| Object |
| Accumulator Bet Recommendations | ```json {"Bet_1": "Halland Goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}| Object |
| Accumulator Bet Recommendations | ```json {"Bet_1": 1.5, "Bet_2": 2} | xx |
| Bet Builder Bet Recommendations | ```json {"Sport":"American Football", "Competition":"NFL", "Event":"Seahwaks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"} | Object |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Bonus Recommendations %}

| Subcategory | Example | Datatype |
| ------- | ----------- |----------- |
|NGR – Net Gaming revenue for the user’s lifetime | 2232| Number|
| NGR14 – Net Gaming revenue for the last 14 days of activity | 42 | Number
| Player Profitability score| 130 | Number |
| Engagement Score | 0.78 | Number |
| Churn Risk Score | 0.02 | Number |
| Estimated Next Bet Date | 2024-08-29 | Time |
| Bet and Get - Bonus value recommendation | 20 | Number |
| Other bonus value recommendations in the future | 0 | Number |
| Future CLTV  | 3126 | Number |

{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Game Recommendations %}

| Subcategory | Example | Datatype |
| ------- | ----------- |----------- |
| Recommended For You | Fluffy Favourites, Fishin’ Frenzy, Big Bass Bonanza, Rainbow Gold, Wild West| Array |
| Favourite Games | Fishin' Frenzy | Array |
| Recommended New Games | Sticky Bees, Beware the Deep Megaways, Gold Party, The Flintstones| Array |
| Players Like You Are Playing (Collaborative Filtering) |Gold Blitz, Big Bass Splash, Rick and Morty, Book of Dead, Gates of Olympus, Luck O’ the Irish | Array |
| Because You Played (Game Similarity)|Fluffy Favourites 2, Luck Rish Express, Gold Cash, Aztec Treasure Hunt, Stars Bonanza | Array |
| Up Next (Game Sequencing) | Fishin’ Frenzy The Big Catch, Big Banker, 9 Masks Of Fire, Super Lion, Fishin’ Bigger Pots Of Gold | Array |
| Popular Games | Temple of Iris, Fishin’ Frenzy, Rishing Reward, Crazy Time, Fluffy Favourites | Array |
| Trending Games | Pig Banker, Hyper Gold, Pyramid King, Gold Cash | Array |

{: .reset-td-br-1 .reset-td-br-2}
{% endtab %}

{% tab Player Cluster %}

| Subcategory | Example | Datatype |
| ------- | ----------- |----------- |
| Showcase what cluster the player is in | High Value Game Diverse| String |
{: .reset-td-br-1 .reset-td-br-2}
{% endtab %}

{% tab Player Sustain (Player potential risk) %}

| Subcategory | Example | Datatype |
| ------- | ----------- |----------- |
| Risk Score | 0.5| Number |
| Risky Player | True | Boolean |
{: .reset-td-br-1 .reset-td-br-2}
{% endtab %}
{% endtabs %}

More details on each attribute can be found in [Future Anthem's documentation](https://knowledge.futureanthem.com/getting-started).





