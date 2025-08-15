---
nav_title: Saving drafts for Canvas
article_title: Saving Drafts for Canvas
alias: "/save_as_draft/"
page_order: 1
description: "This reference article covers how to save a draft for a Canvas that has already launched."
page_type: reference
tool: Canvas
---

# Saving drafts for Canvas

> As you create and launch Canvases, you can edit an active Canvas and save it as a draft, allowing you to pilot your changes before another launch. 

If you have an active Canvas that requires large-scale changes, you can use this feature to to build, save, and quality-check **prior** to launching these changes in the active Canvas. 

As with any Canvas, only one user can edit a draft at a time, and a Canvas can only have one draft at a time. These drafts don't have any analytics because the draft changes haven't been launched yet.

![An example draft Canvas with a banner that indicates to the user that they're editing a draft Canvas with an option to view the active Canvas. The footer has options to go back to the analytics view, save as draft, or launch draft.]({% image_buster /assets/img_archive/canvas_draft1.png %})

## Creating a draft

To create a draft:

1. Go to an active Canvas.
2. Select the **Save as Draft** button in the Canvas footer. 

Note that edits to the active Canvas cannot be made while a draft of a Canvas exists. You can update the Canvas to apply changes or discard the draft.

## Referencing the active draft

To reference the active Canvas, select **View Active Canvas** in the footer from the analytics view or the Canvas header from the draft. To return to an active Canvas, select **Edit Draft** from the analytics view or the active Canvas view.

You can only reference steps that have already been launched before the draft was created. This means if you created a step or channel **after** the draft was created, it can't be referenced in your draft.

{% alert note %}
If a Content Block is referenced in a Canvas draft, the Canvas is listed in the Content Block inclusion count. However, if the Content Block is referenced in a draft of an **active** Canvas, the Canvas won't be listed in the Content Block inclusion count.
{% endalert %}

### In-app message prioritization

For drafts of an active Canvas, the in-app message priority within the Canvas builder will be updated immediately when a user changes the priority. This means Canvas-level in-app message priority is applied to the active Canvas immediately, even when a draft exists. 

However, step-level in-app message priority changes are saved as a draft and applied when the Canvas is updated. For example, in a Message step, the priority sorter will be updated when a user launches the draft since step settings apply at a step level.

