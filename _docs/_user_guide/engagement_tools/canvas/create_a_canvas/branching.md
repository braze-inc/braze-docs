---
nav_title: Branching
article_title: Branching
page_order: 2
page_type: reference
description: "This reference article defines branching and how it can be useful for your Canvases."
tool: Canvas

---

# Creating a branch

> This reference article defines branching and how it can be useful for your Canvases built with the original Canvas workflow. Check out our [Braze Learning course](https://learning.braze.com/canvas-course) to also learn more about branching!

{% alert important %}
As of February 28, 2023, you will no longer be able to create or duplicate Canvases using the original Canvas experience. 
{% endalert %}

To create a branch, click the <i class="fas fa-plus-circle"></i> plus button at the bottom of your Canvas component. Then, select one of the shadowed panels to create a new step.

![][1]{: style="max-width:70%;"}

You can also branch from the first step and create another step.

![][2]{: style="max-width:70%;"}

You can set up filters to determine how your users should flow to subsequent steps in your Canvas.

![][3]{: style="max-width:70%;"}

You can also have users flow between branches based upon actions that they take. This helps separate your users into their respective journeys. 

![][4]{: style="max-width:70%;"}

## Best practices

While branching can be useful to deliver personalized experiences for your users, keep in mind these best practices as you build your Canvas journey.

### Large number of entries

In general, it's best to keep your number of entries (the number of users and steps queued) at a minimum per Canvas use case. If you find that the number of entries is increasing, we recommend cloning your Canvases to [Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/) for more seamless Canvas management.

### Overlapping filters

When setting up your Canvas, ensure that the filters that you use to split users down different branches do not overlap. If a user can match multiple steps, Braze will pick a branch to send them down. For example, if a user first made a purchase seven days ago, they will be randomly slotted into one of the following branches.

![Two Delay Step branches with the overlapping filters "First made purchase less than 2 weeks ago" and "First made purchase less than 3 weeks ago".][5]

[1]: {% image_buster /assets/img_archive/canvas_branch_1.gif %}
[2]: {% image_buster /assets/img_archive/canvas_branch_2.gif %}
[3]: {% image_buster /assets/img_archive/canvas_branch_3.png %}
[4]: {% image_buster /assets/img_archive/canvas_branch_4.png %}
[5]: {% image_buster /assets/img_archive/canvas_branch_5.png %}