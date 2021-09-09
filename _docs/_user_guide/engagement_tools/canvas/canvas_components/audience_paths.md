---
nav_title: Audience Paths Step
article_title: Audience Path Step
alias: /audience_paths/
page_order: 5
description: "This reference article describes how to use Audience Paths in your Canvas to intuitively filter and segment users on a large scale with strategic priority-based user-groupings."
page_type: reference
tool: Canvas

---

# Audience Paths Step

> Canvas Audience Paths allows you to intuitively filter and segment users on a large scale with strategic priority-based user-groupings. This new Canvas step replaces the need to create excessive audience-based full steps, allowing you to combine what might have been 8 full steps into one! The introduction of this new step will help you simplify user targeting while clearing up your Canvases from unnecessary clutter and complexity. 

![Audience Paths][0]{: style="float:right;max-width:13%;margin-left:15px;margin-top:15px;"}

Audience Paths are similar to sorting funnels with ranking criteria. Users will be evaluated for each criterion in priority order and be sent down the path of the highest-ranking criteria they qualify. This means there will never be any ambiguity as to where users will go, and what messages they will receive. 

Audience Paths allows you to:
- __Send users down different paths based on audience criteria__
- __Assign priority to different audience groups__, so your messages get to the correct users. 
  - Previously, if users met the criteria of two potential full steps, they would be randomly assigned. 
- __Precisely target users on a large scale__
  - Audience Paths allows you to create up to 8 audience groups (2 default groups and 6 additional) per step, though users may want to connect multiple Audience Path steps to further sort their users. 

## Create Audience Paths
![Audience Paths][1]{: style="float:right;max-width:20%;margin-left:15px;"}

To create Audience Paths, add a step to your Canvas. Then, using the drop-down at the top of the new step, select `Audience Paths`.

In the default Audience Paths step show to the right, there are already two default audience groups, __Group 1__ and __Everybody Else__. The Everybody Else group includes any user who does not fall into a defined audience group. This group will always be ranked last.
<br><br><br>

### Define Audience Groups

Below, you are shown the layout of an expanded Audience Paths step. Here you can define up to 8 audience groups (1 preset and 7 customizable). To define an audience group, select the group name from the Audience Paths wizard. Here, you can rename your audience group, choose the filters and segments that apply to your group, and add or delete groups.

For example, if you wanted to send a group of users helpful food recommendations, you might select custom attribute filters you have already built out such as "Loves Asian Cuisine", "Loves Latin Cuisine", "Loves European Cuisine", etc. 

![Audience Paths][3]{: style="max-width:90%;margin-left:15px;"}

Once the Audience Paths Step has been completed, each audience group will have a separate branch, allowing you to continue to use Audience Paths to further filter your audience as needed, or continue on your Canvas journey with the standard Canvas steps. 

![Audience Paths][4]{: style="max-width:90%;margin-left:15px;"}

## Using Audience Paths

The true power of Audience Paths lies in the ability to assign priority. While this feature does not need to be used strategically, some marketers may find themselves pushing certain products to users, for example, specials or limited-edition releases. By assigning a high priority to these groups, you can target users that fall into specific filters and segments while still targeting users that might not fit those specific criteria, all in a single Canvas step.

![Audience Paths][2]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}
For example, if you wanted to send a group of users ads for new products, you would rank filters that fall under those products high on the Audience Path. Let's say you were trying to send out a marketing campaign for the company "Big Brand" and a new brand of shoe was just released, you might select filters like "Likes Big Brand Shoes", "Likes Big Brand", etc. and send out different types of email messages based on what group they fall into. 

When users enter this Audience Paths step, they will first be evaluated if they fall under the highest-ranked audience group, audience group 1 "Likes Big Brand Shoes", if so, they will continue to the next step defined in your Canvas. If that user did not "Like Big Brand Shoes", they will then be evaluated for the next audience group, audience group 2 "Likes Big Brand", and will commence to the next Canvas step if the criteria are met. Lastly, if there exist users that failed to fall into the previous groups, they would fall into the Everybody Else group and would continue onto the next Canvas step you define for that path. 

[0]: {% image_buster /assets/img/audience_path/audience_path.png %}
[1]: {% image_buster /assets/img/audience_path/audience_path1.png %}
[1]: {% image_buster /assets/img/audience_path/audience_path1.png %}
[2]: {% image_buster /assets/img/audience_path/audience_path2.png %}
[3]: {% image_buster /assets/img/audience_path/audience_path3.png %}
[4]: {% image_buster /assets/img/audience_path/audience_path4.png %}
