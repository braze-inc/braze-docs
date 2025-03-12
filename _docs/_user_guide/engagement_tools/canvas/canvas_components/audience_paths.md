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

> Canvas Audience Paths allow you to intuitively filter and segment users on a large scale with strategic priority-based user-groupings. 

This Canvas component replaces the need to create excessive audience-based full steps, allowing you to combine what might have been eight full components into one. This helps you simplify user targeting while clearing up your Canvases from unnecessary clutter and complexity. 

![An Audience Path with five groups.][0]{: style="float:right;max-width:13%;margin-left:15px;margin-top:15px;"}

## How it works

Audience Paths are similar to sorting funnels with ranking criteria. Users are evaluated for each criterion in priority order and sent down the path of the highest-ranking criteria they qualify. This reduces ambiguity of where users will go and what messages they will receive. Note that the rankings aren't [editable after launch]({{site.baseurl}}/post-launch_edits/).

With Audience Paths, you can:

- Send users down different Canvas paths based on audience criteria.
- Assign priority to different audience groups, so your messages get to the correct users. 
  - Previously, if users met the criteria of two potential full steps, they would be randomly assigned. 
- Precisely target users on a large scale.
  - Create up to eight audience groups (two default and six additional groups) per component, but you may want to connect multiple Audience Paths Steps to further sort your users. 

### Allowing time for user evaluations

Users are evaluated as soon as they reach the Audience Path step. After they have been evaluated, they will immediately progress to the next step. This makes it important to allow an appropriate time window to lapse if the Audience Path is determined by a user action.

![Canvas showing a 24-hour delay after a Message step, followed by an Audience Path.][5]{: style="float:right;max-width:40%;margin-left:15px;"}

For example, if users are sent Message A and the next step is an Audience Path that evaluates whether they interacted with that message, all users will progress to the step for those who haven't interacted with that message. This is because the users immediately progressed to the Audience Path step without time to interact with the message. In other words, users are evaluated for an interaction with the message almost immediately after the message sends.

To give users time to interact with a sent message, a delay needs to be between the Message step and Audience Path. For example, a 24-hour delay would give users 24 hours after the message sends to interact with Message A before being evaluation.

## Creating an Audience Path

![An Audience Path with two groups.][1]{: style="float:right;max-width:20%;margin-left:15px;"}

To add an Audience Paths step, do the following: 

1. Add a step to your Canvas. 
2. Drag and drop the component from the sidebar, or select <i class="fas fa-plus-circle"></i> **Add** at the bottom of a step and select **Audience Paths**.

The default Audience Paths component contains two default audience groups, **Group 1** and **Everybody Else**. The **Everybody Else** group includes any user who does not fall into a defined audience group. This group will always be ranked last.

### Defining audience groups

The following screenshot shows the layout of an expanded Audience Paths step. Here, you can define up to eight audience groups (one preset and seven customizable). To define an audience group, select the group name from the Audience Paths editor. You can rename your audience group, choose the filters and segments that apply to your group, and add or delete groups.

For example, if you wanted to send a group of users helpful food recommendations, you might select custom attribute filters you have already built out such as "Loves Asian Cuisine", "Loves Latin Cuisine", and "Loves European Cuisine". 

![An expanded Audience Path with groups for "Loves Asian Cuisine”, “Loves Latin Cuisine”, “Loves European Cuisine”, and "Everyone Else".][3]{: style="max-width:90%;margin-left:15px;"}

After the Audience Paths step is complete, each audience group will have a separate branch. You can continue using Audience Paths to further filter your audience, or continue your Canvas journey with the standard Canvas steps. 

![Two Audience Paths with different groups for various cusines.][4]{: style="max-width:90%;margin-left:15px;"}

### Testing audience groups

![The "User Lookup" section.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

After adding segments and filters to your audience, you can test if your audience groups are set up as expected by [looking up a user]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) to confirm they match the audience criteria. 

## Using Audience Paths

The true power of Audience Paths lies in the ability to assign priority. While this feature doesn't need to be used strategically, some marketers may find themselves pushing certain products to users such as specials or limited-edition releases. 

By assigning a high priority to these groups, you can target users that fall into specific filters and segments while still targeting users that might not fit those specific criteria—all in a single Canvas step.

![An Audience Path with groups for “Likes Big Brand Shoes”, “Likes Big Brand”, and "Everyone Else".][2]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

For example, let's say you wanted to send a group of users ads for new products. You'd start by ranking filters that fall under those products high on the Audience Path. If you were creating a marketing campaign for the company "Big Brand" and a new shoe brand had just released, you might select filters like "Likes Big Brand Shoes" or "Likes Big Brand", and send different email messages based on what filtered group they fall into. 

When users enter this Audience Paths component, they will first be evaluated if they fall under the highest-ranked audience group: Audience Group A "Likes Big Brand Shoes". If so, they will continue to the next component defined in your Canvas. If they don't "Like Big Brand Shoes", they will then be evaluated for the next audience group, Audience Group B "Likes Big Brand", and will continue to the next Canvas component if the criteria are met. Lastly, users don't fall into the previous groups would fall into the **Everybody Else** group and continue to the next Canvas component you define for that path.

You can also see the performance of this step using [Canvas analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#performance-visualization).

### Segmenting Audience Paths with random bucket numbers

If your Canvas uses a [rate limit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) (such as limiting the total number of users who will receive the Canvas), Braze recommends that you don't use random bucket numbers to segment your Audience Paths. 

A [random bucket number]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) is a user attribute that can be used to create uniformly distributed segments of random users. Braze uses the random bucket number to group users during the segmentation phase of Canvas entry, and each group is processed separately. Depending on which groups finish processing first, some users may be capped at entry due to the rate limit, which could cause an uneven distribution of users when they reach the Audience Paths step.

In this scenario, try using [Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) instead.

### Using Intelligent Channel filter with Audience Paths

Using a combination of Audience Paths steps and Intelligent Channel filters, you can tailor your messaging experience to each user's preferences and behaviors. This way, your users will receive the most relevant messages through the appropriate channels.

For example, in an Audience Paths step, you can create three audiences: Email, Mobile Push, and Everyone Else. For the Email audience, add the filter `Intelligent Channel is Email`. For the Mobile Push audience, add the filter `Intelligent Channel is Mobile Push`. Then, you can add a Message step for each of the audience paths to deliver personalized and relevant messages.

{% alert tip %}
Check out our [Braze Canvas templates]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) for examples on how you can customize these pre-built templates to your advantage.
{% endalert %}

[0]: {% image_buster /assets/img/audience_path/audience_path.png %}
[1]: {% image_buster /assets/img/audience_path/audience_path1.png %}
[2]: {% image_buster /assets/img/audience_path/audience_path2.png %}
[3]: {% image_buster /assets/img/audience_path/audience_path3.png %}
[4]: {% image_buster /assets/img/audience_path/audience_path4.png %}
[5]: {% image_buster /assets/img/audience_path/audience_path5.png %}
