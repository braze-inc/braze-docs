---
nav_title: Install Attribution Campaign
platform: Campaigns
subplatform: Ideas and Strategies
page_order: 7

page_type: reference
description: "This reference article describes user installs (install attribution tracking) and different ways to apply this information within your campaign."
tool:
- Campaigns
- Segments
---
# Understanding User Installs

> This reference article goes over the concept of user installs (install attribution tracking) and different ways to apply this information within your campaign.

Install attribution tracking is a great way to improve your initial relationship with your user. Knowing how, where, and even more importantly, why a user installs your app allows you to get a better understanding of who your user is and how you should introduce them to your app. While Braze does not provide install attribution tracking, we can integrate with services such as Fiksu and Tune to seamlessly provide you with install data.

## Segment Your Users

Once your user installs your app, you can begin segmenting them based on the following [install attribution filters][2]. For instance, a travel app could add users that came from an ad relating to beach vacation deals to a "Beach Lovers" segment. Similarly, a music app could segment users based on the genre of music displayed in the advertisement that led to the install.

## Best Practices

### Personalized Onboarding

Now that you have more information about your user, you can personalize their onboarding process. This could be as simple as changing the images in your messages to fit their preferences, or as complex as creating a unique user onboarding for each ad that could lead to an install. To scale out a fully comprehensive sequence of messages that can take user behavior into consideration, please take a look at our documentation on [Canvas][5]

![Install Attribute Onboarding][3]

### Reference Data from the Ad

Users may be attracted to your app by a promotional offer or giveaway. Using install attribution data allows you to send campaigns containing discount codes or offers to only the users who installed due to these promotions. In a similar manner, if your ad contains information on a particular product (such as a specific movie in a video app or sale in an eCommerce app), you can send campaigns directing users to the correct page of your app.

## Evaluate Advertising Efforts

Install attribution data can be valuable in assessing the effectiveness of different marketing campaigns. Looking through to see which ads and campaigns are leading to the most installs and which are falling behind can be used to focus your resources in the most compelling ads.

[2]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#install-attribution
[3]: {% image_buster /assets/img_archive/install_onboarding.png %}
[5]: {{site.baseurl}}/developer_guide/rest_api/messaging/#canvas
