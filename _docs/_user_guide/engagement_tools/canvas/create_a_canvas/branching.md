---
nav_title: Branching
article_title: Branching
page_order: 2
page_type: reference
description: "This reference article covers what branching is, and how it can be useful in your Canvases."
tool: Canvas

---

# Branching

> this reference article covers what branching is, and how it can be useful in your canvases.

## Create a branch

You can harness the power of Braze’s action-based delivery and powerful realtime segmentation to deliver personalized experiences for your users.

To create a branch, click on the blue circle at the bottom of a Step. Then click on one of the shadowed icons to create a new step.

![Canvas Create Branch 1][1]

Create another step, branching from the first:

![Canvas Create Branch 2][2]

You can set up filters to determine how users should flow to subsequent steps.

![Canvas Create Branch 3][3]

Or you can have users flow between branches based upon actions that they take.

![Canvas Create Branch 4][4]

## Warnings

### Overlapping filters

When setting up your Canvas, you should ensure that the Filters that you use to split users down different branches do not overlap. If a user can match multiple steps, Braze will pick a branch to send them down. For example:

![Canvas Create Branch 5][5]

If a user first made a purchase 7 days ago, they will be randomly slotted into one of the branches above.

[1]: {% image_buster /assets/img_archive/canvas_branch_1.gif %}
[2]: {% image_buster /assets/img_archive/canvas_branch_2.gif %}
[3]: {% image_buster /assets/img_archive/canvas_branch_3.png %}
[4]: {% image_buster /assets/img_archive/canvas_branch_4.png %}
[5]: {% image_buster /assets/img_archive/canvas_branch_5.png %}

