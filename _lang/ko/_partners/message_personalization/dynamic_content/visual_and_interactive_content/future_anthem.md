---
nav_title: Future Anthem
article_title: Future Anthem
description: "Learn how to integrate Future Anthem with Braze."
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# Future Anthem

> 리얼 머니 게임 업계를 위한 [퓨처 앤섬의](https://www.futureanthem.com/) 올인원 제품인 Amplifier AI는 콘텐츠 개인화, 실시간 경험, 동적 오디언스를 제공합니다. Amplifier AI works seamlessly across sports, casino, and lottery, allowing customers to enhance Braze player profiles with industry-specific player attributes, such as favorite game, favorite team, engagement score, next bet recommendation, expected next bet, and more.

{% alert important %}
This feature is currently in Early Access. 시작하려면 Future Anthem 고객 성공 팀에 문의하세요.
{% endalert %}

## Prerequisites

| Requirement              | Description                                            |
|--------------------------|--------------------------------------------------------|
| Future Anthem Account    | A Future Anthem account. |
| Braze REST API key       | A Braze REST API key with the [`users.track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). This can be created in the Braze dashboard from **Settings** > **API Keys**. |
| Braze REST endpoint      | The Braze [REST endpoint]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) that matches your instance, such as `rest.iad-01.com`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Use Cases

With this integration, you can:

- Identify users with high engagement scores and target them with personalized offers, such as exclusive promotions or VIP rewards.
- Suggest similar games to a user based on the games they already like.

## Integration

The Future Anthem Customer Success team will help set up your integration. 고객 성공 담당자에게 문의하면 가장 관련성이 높은 속성을 식별하여 Braze에 전송할 수 있도록 도와드릴 것입니다.

|Example attributes in Future Anthem|Example attributes in Braze|
|-----------------------------------|---------------------------|
|![사용자 프로필의 속성입니다.]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %})|![객체 속성입니다.]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %})|

## Braze custom attributes

These are the available Braze custom attributes. For more detailed information, see [Future Anthem: Getting Started](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab Bet Recommendations %}

| Subcategory | Example (JSON) | Datatype |
| ------- | ----------- |----------- |
| User Preferences | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| Object |
| Single Bet Recommendations | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| Object |
| Accumulator Bet Recommendations | `{"Bet_1": "Halland Goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}`| Object |
| Accumulator Bet Recommendations | `{"Bet_1": 1.5, "Bet_2": 2}` | Object |
| Bet Builder Bet Recommendations | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahwaks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}`| Object |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Player Cluster %}

| Subcategory | Example | Datatype |
| ------- | ----------- |----------- |
| Showcase what cluster the player is in | High Value Game Diverse| String |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Player Sustain - Player potential risk %}

| Subcategory | Example | Datatype |
| ------- | ----------- |----------- |
| Risk Score | 0.5| Number |
| Risky Player | True | Boolean |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}
