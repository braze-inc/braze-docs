---
nav_title: Branching
article_title: Branching
page_order: 2
page_type: reference
description: "This reference article defines branching and how it can be useful for your Canvases."
tool: Canvas

---

# Creating a branch

> This reference article defines branching and how it can be useful for your Canvases. You can also check out our [LAB course](https://lab.braze.com/canvas-course) to learn more about branching for Canvas.

You can harness the power of Braze’s action-based delivery and powerful realtime segmentation to deliver personalized experiences for your users. To create a branch, click the <i class="fas fa-plus-circle"></i> plus button at the bottom of your step. Then, select one of the shadowed panels to create a new step.

![][1]

You can also branch from the first step and create another step.

![][2]

You can set up filters to determine how your users should flow to subsequent steps in your Canvas.

![][3]

You can also have users flow between branches based upon actions that they take. This helps separate your users into their respective journeys. 

![][4]

## Warnings

### Overlapping filters

When setting up your Canvas, you should ensure that the filters that you use to split users down different branches do not overlap. If a user can match multiple steps, Braze will pick a branch to send them down. For example, if a user first made a purchase 7 days ago, they will be randomly slotted into one of the branches below.

![Two Delay Step branches with the overlapping filters "First made purchase less than 2 weeks ago" and "First made purchase less than 3 weeks ago".][5]

[1]: {% image_buster /assets/img_archive/canvas_branch_1.gif %}
[2]: {% image_buster /assets/img_archive/canvas_branch_2.gif %}
[3]: {% image_buster /assets/img_archive/canvas_branch_3.png %}
[4]: {% image_buster /assets/img_archive/canvas_branch_4.png %}
[5]: {% image_buster /assets/img_archive/canvas_branch_5.png %}