---
nav_title: Decision Split 
article_title: Decision Split 
alias: /decision_split/
page_order: 2
page_type: reference
description: "This reference article covers how to create and use decision splits in your Canvas."
tool: Canvas

---

# Decision Split 

> The Decision Split component in Canvas allows you to deliver personalized, real-time experiences for your users. 

This component can be used to create Canvas branches based on whether a user matches a query.

![][1]{: style="float:right;max-width:20%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

## Create a decision split 

To create a decision split in your workflow, first add a step to your Canvas. Drag and drop the component from the sidebar, or click the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Decision Split**.

### Define your split

How do you want to split your users? You can use [segments][5] and filters to draw the line. Essentially, you're creating a `true` or `false` query that will evaluate your users and then funnel them to one step or another. You must use at least one segment or one filter. You do not need to use both a segment and a filter.

![][2]{: style="max-width:90%;"}

{% alert note %} 
By default, segments and filters for a Decision Split component are checked right after receiving a previous step, unless you add a delay. 
{% endalert %} 

## Use your split

Using a decision split can help you distinguish paths for your users based on their segment or their attributes, even whether they use certain messaging channels to receive your messages!

Let's say that you're creating an onboarding flow. You might start with a welcome email upon signing up. Then, two days later, you want to send a push message, but only to users who are push enabled. After that, all users get another email three days after they signed up. You could also use your decision split to send an in-app message to users who don't have push enable to encourage them to enable push.

![][3]{: style="max-width:60%;"}

If there is no step following one of the paths, users who go down that path will exit the Canvas. 

{% alert important %}
A decision split cannot have full step sibling steps. In other words, you can't create a full step that branches into a filter step and a full step. This restriction exists because if there was a branch with a filter step and a full step, it wouldn't be clear which branch users would go down.
<br>
A filter step can only connect to one next step.
{% endalert %}

## Analytics

Refer to the following table for descriptions of analytics for this step:

| Metric | Description |
|---|---|
| _Entered_ | The total number of times the step has been entered. If your Canvas has re-eligibility and a user enters a Decision Split step twice, two entries will be recorded. |
| _Yes_ | The number of entries that met the specified criteria and proceeded down the "yes" path. |
| _No_ | The number of entries that did not meet the specified criteria and proceeded down the "no" path. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[1]: {% image_buster /assets/img/decision-split-1.png %}
[2]: {% image_buster /assets/img/define-split-2.png %}
[3]: {% image_buster /assets/img/use-split-onboarding-3.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/
