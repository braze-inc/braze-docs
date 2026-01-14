{% if include.alert == "Liquid email display name and reply-to address" %}

{% alert tip %}
You can use [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) in the **From Display Name + Address** and **Reply-To Address** fields to dynamically template these based on custom attributes. This allows you to send from different brands, regions, or departments using a single email campaign or Canvas step.
{% endalert %}

{% endif %}

{% if include.alert == "Reference properties from triggering event" %}

{% alert tip %}
You don't need a Context step to reference properties from the triggering event in [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) or [Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) steps. You can reference the properties directly in the filter groups with the **Context Variable** filter. Make sure to select the correct data type.
{% endalert %}

{% endif %}