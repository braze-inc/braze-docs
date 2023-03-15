---
nav_title: Audience Paths 
article_title: Audience Paths 
alias: /audience_paths/
page_order: 1
page_type: reference
description: "This reference article describes how to use Audience Paths in your Canvas to intuitively filter and segment users on a large scale with strategic priority-based user-groupings."
tool: Canvas

---

# Audience Paths 

> Canvas Audience Paths allow you to intuitively filter and segment users on a large scale with strategic priority-based user-groupings. This Canvas component replaces the need to create excessive audience-based full steps, allowing you to combine what might have been 8 full components into one! The Audience Paths component will help you simplify user targeting while clearing up your Canvases from unnecessary clutter and complexity. 

![][0]{: style="float:right;max-width:13%;margin-left:15px;margin-top:15px;"}

Audience Paths are similar to sorting funnels with ranking criteria. Users will be evaluated for each criterion in priority order and be sent down the path of the highest-ranking criteria they qualify. This means there will never be any ambiguity as to where users will go, and what messages they will receive. 

With Audience Paths, you can:

- Send users down different paths based on audience criteria.
- Assign priority to different audience groups, so your messages get to the correct users. 
  - Previously, if users met the criteria of two potential full steps, they would be randomly assigned. 
- Precisely target users on a large scale.
  - Create up to 8 audience groups (2 default and 6 additional groups) per component, but users may want to connect multiple Audience Paths Steps to further sort their users. 

## Create Audience Paths

![][1]{: style="float:right;max-width:20%;margin-left:15px;"}

To create Audience Paths, first add a step to your Canvas. Drag and drop the component from the sidebar, or click the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Audience Paths**.

In the default Audience Paths component show to the right, there are already two default audience groups, **Group 1** and **Everybody Else**. The Everybody Else group includes any user who does not fall into a defined audience group. This group will always be ranked last.
<br><br><br>

### Define audience groups

In the following screenshot, you are shown the layout of an expanded Audience Paths component. Here, you can define up to 8 audience groups (1 preset and 7 customizable). To define an audience group, select the group name from the Audience Paths wizard. Here, you can rename your audience group, choose the filters and segments that apply to your group, and add or delete groups.

For example, if you wanted to send a group of users helpful food recommendations, you might select custom attribute filters you have already built out such as "Loves Asian Cuisine", "Loves Latin Cuisine", "Loves European Cuisine", etc. 

![][3]{: style="max-width:90%;margin-left:15px;"}

Once the Audience Paths component has been completed, each audience group will have a separate branch, allowing you to continue using Audience Paths to further filter your audience as needed, or continue on your Canvas journey with the standard Canvas components. 

![][4]{: style="max-width:90%;margin-left:15px;"}

### Testing audience groups

After adding segments and filters to your audience, you can test if your audience groups are set up as expected by [looking up a user]({{site.baseurl}}/user_guide/engagement_tools/segments/user_lookup/) to confirm if they match the audience criteria.

![]({% image_buster /assets/img_archive/user_lookup.png %})

## Using Audience Paths

The true power of Audience Paths lies in the ability to assign priority. While this feature does not need to be used strategically, some marketers may find themselves pushing certain products to users such as specials or limited-edition releases. 

By assigning a high priority to these groups, you can target users that fall into specific filters and segments while still targeting users that might not fit those specific criteria—all in a single Canvas component.

![][2]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}
For example, let's say you wanted to send a group of users ads for new products. You'd start by ranking filters that fall under those products high on the Audience Path. If you were trying to send out a marketing campaign for the company "Big Brand" and a new brand of shoe was just released, you might select filters like "Likes Big Brand Shoes" or "Likes Big Brand", and send out different types of email messages based on what group they fall into. 

When users enter this Audience Paths component, they will first be evaluated if they fall under the highest-ranked audience group, audience group 1 "Likes Big Brand Shoes". If so, they will continue to the next component defined in your Canvas. If that user did not "Like Big Brand Shoes", they will then be evaluated for the next audience group, which would be audience group 2 "Likes Big Brand", and will commence to the next Canvas component if the criteria are met. Lastly, for users that fail to fall into the previous groups, they would fall into the **Everybody Else** group and would continue onto the next Canvas component you define for that path.

You can also see the performance of this component using [Canvas analytics][5].

### Audience Paths and random bucket numbers

If your Canvas uses a [rate limit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) (such as limiting the total number of users who will receive the Canvas), Braze recommends that you don't use random bucket numbers to segment your Audience Paths. 

A [random bucket number]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/ab_testing_with_random_buckets/) is a user attribute that can be used to create uniformly distributed segments of random users. Braze uses the random bucket number to group users during the segmentation phase of Canvas entry, and each group is processed separately. Depending on which groups finish processing first, some users may be capped at entry due to the rate limit, which could cause an uneven distribution of users when they reach the Audience Paths step.

In this scenario, try using [Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) instead.

[0]: {% image_buster /assets/img/audience_path/audience_path.png %}
[1]: {% image_buster /assets/img/audience_path/audience_path1.png %}
[1]: {% image_buster /assets/img/audience_path/audience_path1.png %}
[2]: {% image_buster /assets/img/audience_path/audience_path2.png %}
[3]: {% image_buster /assets/img/audience_path/audience_path3.png %}
[4]: {% image_buster /assets/img/audience_path/audience_path4.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#performance-visualization
