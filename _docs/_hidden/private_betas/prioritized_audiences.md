---
nav_title: Canvas Prioritized Audiences
description: ""
---

# Prioritized Audiences

> Prioritized audiences can be used to assign priority to different user groups or audiences. While this functionality was capable with Canvas through a workaround, Braze has built out a new, dedicated, and intuitive option for users. 

Prioritized Audiences allow you to:
- Send users down different paths based on audience criteria
- Users can have a total of 8 audience groups (2 default groups and 6 additional).

## Old Behavior
To achieve this with Full Steps, marketers would connect several Full Steps to one node and set different Audience criteria for each Full Step. When users reach this stage, they are evaluated for every Full Step. If a user qualifies for more than one Full Step, the system randomly chooses one. 	

## Create an Audience Path

To create an Audience Path, add a step to your Canvas. Then, use the drop-down at the top of a new step to select `Audience Paths`.

In the default Audience Step, there will already be two audience groups, __Group 1__ and __Everybody Else__. The Everybody else group is required and serves as a backup bucket that users who did not fall into any of the previous categories would fall in. 

IMAGE ON RIGHT

### Define Audience Groups

Below, you are shown the layout of an Audience Step. Here you can define up to 8 audience groups (1 Default and 7 customizable steps.) To define an audience group, select the group name from the Audience Path dropdown. Here you can rename your audience group and choose the filters and segments that would apply.

For example, if you wanted to send a group of users helpful food recommendations, you might select filters you have already built out such as "Loves Asian Cuisine", "Loves Latin Cuisine", "Loves European Cuisine", etc. 

Once the Audience Step has been built out, each group will have a separate box, allowing you to continue to filter and define the behavior of the groups. 

## Using Audience Paths

Audience Paths should be seen as a sorting funnel with ranking criteria. Users are evaluated for each criterion in priority order, so there is no ambiguity as to where users will go. Users will always be sent down the path of the highest-ranking criteria for which they qualify. Audience Paths allow you to create up to 8 audience groups per step, though marketers may want to connect multiple Audience Path steps together to further sort their users. 

The true power of audience paths lies in the ability to assign priority. While this feature does not need to be used in a strategic way, some marketers may find themselves pushing certain products to users, for example, specials or limited-edition releases. By assigning a high priority to these groups, users can emphasize filters and segments while still targeting many users that might not fit those specific criteria. 

For example, if you wanted to send a group of users ads for new products, you would rank filters that fall under those products high on the audience path. For example, if you were trying to sell "Big Brand" shoes, you might select filters like "Likes to purchase Shoes", "Likes Big Brand clothing", etc. 

Audience Paths allow you to express priority without the hassle of including excessive steps to achieve this same behavior. 

