---
nav_title: Decision Split Step
article_title: Decision Split Step
alias: /decision_split/
page_order: 1
page_type: reference
description: "This reference article covers how to create and implement decision split steps within your Canvas."
tool: Canvas

---

# Decision Split Step for Canvas

Decision Split Steps in Canvas allow you to deliver personalized, real-time experiences for your users. Decision split steps can be used to create Canvas branches based on whether a user matches a query.
![Decision Split Step][1]{: style="float:right;max-width:20%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}
## Create a Decision Split Step
To create a Decision Split Step, add a step to your Canvas. Then, use the drop-down at the top of the new step to select `Decision Split Step`.

### Define Your Split
How do you want to split your users? You can use Segments and Filters to draw the line. Essentially, you're creating a `true` or `false` query that will evaluate your users and then funnel them to one step or another. You must use at least one Segment or one Filter. You do not need to use both a Segment and a Filter.

![Define Split][2]{: style="max-width:80%;"}

{% alert note %} By default, Filters and Segments for **Decision Split Steps** are checked right after receiving a previous step, unless you add a delay. {% endalert %} 

## Use Split Steps
Using the Decision Split step can help you distinguish paths for your users based on their segment or their attributes, even whether they utilize certain messaging channels to receive your messages!

Let’s say that you’re creating an onboarding flow. You might start with a welcome email upon signing up. Then, two days later, you want to send a push message, but only to users who are push enabled. After that, all users get another email three days after they signed up. You could also use your decision split to send an in-app message to users who don't have push enable to encourage them to enable push.

![Use Split in Onboarding][3]{: style="max-width:60%;"}

If there is no step following one of the paths, users who go down that path will exit the Canvas. 

{% alert important %}
A decision split cannot have full step sibling steps. In other words, you cannot create a full step that branches into a filter step and a full step. This restriction exists because if there was a branch with a filter step and a full step, it wouldn’t be clear which branch users would go down.
<br>
A filter step can only connect to one next step.
{% endalert %}

## Analytics

| Metric | Description |
|---|---|
|Entered | The total number of times the step has been entered. If your Canvas has re-eligibility and a user enters a decision split step twice, two entries will be recorded. |
|Yes | The number of entries that met the specified criteria and proceeded down the “yes” path. |
|No | The number of entries that did not meet the specified criteria and proceeded down the “no” path. |
{: .reset-td-br-1 .reset-td-br-2}

![Decision Step Analytics][4]{: style="max-width:80%;"}

[1]: {% image_buster /assets/img/decision-split-1.png %}
[2]: {% image_buster /assets/img/define-split-2.png %}
[3]: {% image_buster /assets/img/use-split-onboarding-3.png %}
[4]: {% image_buster /assets/img/decision-step-analytics-4.png %}
