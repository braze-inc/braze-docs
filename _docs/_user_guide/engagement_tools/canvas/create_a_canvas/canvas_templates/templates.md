---
nav_title: Canvas templates
article_title: Canvas templates
alias: "/canvas_templates/templates/"
page_order: 0
description: "This reference article covers how to create available Canvas templates."
page_type: reference
---

# Canvas templates

> Braze has a selection of Canvas templates available for you to reference and use as best practices for common use cases. While these templates can't be edited, you can view them in **Templates** > **Braze templates** or use them in your Canvases.

![Braze templates in the Canvas templates section with thirteen available templates.]({% image_buster /assets/img/braze_canvas_templates.png %})

Select from the following available templates to reference or use as your Canvas.

## Standard Canvas templates

{% tabs %}
{% tab Abandoned Intent %}

### Abandoned intent

Engage with users in real-time to encourage them to complete their purchases.

Consider the following when using this template:

- Add a specific audience. Currently, the audience paths are triggered based on "Made Any Purchase", but you can tailor this to specific products you want to target.
- This template assumes you have a separate post-purchase journey, so making a purchase will cause users to exit the Canvas.
- Fill out the details in the Audience Sync step.

{% endtab %}
{% tab Back In Stock %}

### Back in stock

Drive purchases by notifying your users when an item is back in stock with personalized messaging. Consider the following when using this template:

- In **Entry Schedule**, select a catalog to use. This allows you to access data, such as products, discounts, and promotions, to further target your users.
- In **Target Audience**, add a segment to target users who indicated interest in a certain item.
- In the Message steps throughout the Canvas, update the Liquid to reference your catalog.

{% endtab %}
{% tab Feature Adoption %}

### Feature adoption

Deliver timely personalized messages to highlight the benefits and usage tips. Consider the following when using this template:

- Exclude users who have already adopted the feature. For example, in **Target Audience**, add a filter for a custom event such as "Activated Feature" that has already occurred.
- To use the Experiment Path step, define a conversion event. This event should be the event that signals feature adoption.
- Set up the Action Path step in the template with custom events for "Activated Feature" and "Taken Tour".
- Set up the custom attributes in the Message step named "Feedback Survey" to capture sentiment of feedback.

{% endtab %}
{% tab Lapsed User %}

### Lapsed user

Bring users back to your app with incentives based on their past engagements. Consider the following when using this template:

- In **Basics**, select a specific app to track conversions for.
- In the Canvas editor, add specific apps for the Action Paths steps.
- Configure the Audience Sync step with the partners and audiences for your use case.

{% endtab %}
{% tab Onboarding %}

### Onboarding

Create onboarding journeys that promote strong initial adoption and encourage lasting relationships with your users. Consider the following when using this template:

- In the Audience Paths step named "Audience Split", consider customizing the key actions for engaged users. In the template, the segment filter is "Has clicked email for step Welcome Email".

{% endtab %}
{% tab Post-Purchase Feedback %}

### Post-purchase feedback

Orchestrate personalized experiences that allow you to respond to feedback and build a relationship with your users. Consider the following when using this template:

- In the first step of the Canvas editor:
    - Specify the custom attributes in the in-app message to indicate the sentiment of the feedback based on the selected survey option. 
    - Specify attributes on links for each call-to-action to capture which option is selected. These attributes are referenced in the subsequent audience path.
- Customize the Audience Path with the attributes from the first step of this template.
- Set up the Audience Sync step named "Ad Retargeting".

{% endtab %}
{% endtabs %}

{% alert tip %}
For a step-by-step guide to creating an example Canvas using these Braze templates, see [Using Braze templates]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates).
{% endalert %}

## eCommerce Canvas templates

eCommerce Canvas templates are tailored specifically for eCommerce marketers, making it easier to implement essential strategies.

{% multi_lang_include canvas/ecommerce_templates.md %}