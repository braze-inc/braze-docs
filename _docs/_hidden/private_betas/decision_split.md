---
nav_title: Decision Split Step for Canvas
permalink: /decision_split/
hidden: true
---

# Decision Split Step for Canvas

{% alert note %}
This Canvas feature is currently in Beta. Please reach out to your Braze account manager for more information.
{% endalert %}

Decision Split Steps in Canvas allow you to deliver personalized, real-time experiences for your users. Decision split steps can be used to create Canvas branches based on whether a user matches a query.

## Create a Decision Split Step
To create a Decision Split Step, add a step to your Canvas. Then, use the drop down at the top of the new step to select `Decision Split Step`.

![Decision Split Step][1]{: height="50%" width="50%"}

### Define Your Split
How do you want to split your users? You can use Segments and Filters to draw the line. Essentially, you're creating a `true` or `false` query that will evaluate your users and then funnel them to one step or another. You must use at least one Segment or one Filter. You do not need to use both a Segment and a Filter.

![Define Split][2]{: height="70%" width="70%"}

## Use Split Steps
Using the Decision Split step can help you distinguish paths for your users based on their segment or their attributes, even whether they utilize certain messaging channels to receive your messages!

Let’s say that you’re creating an onboarding flow. You might start off with a welcome email upon signing up. Then, two days later, you want to send a push message, but only to users who are push enabled. After that, all users get another email three days after they signed up. You could also use your decision split to send an in-app message to users who don't have push enable to encourage them to enable push.

![Use Split in Onboarding][3]{: height="50%" width="50%"}

{% alert important %}
A decision split cannot have full step sibling steps. In other words, you cannot create a full step that branches into a filter step and a full step. This restriction exists because if there was a branch with a filter step and a full step, it wouldn’t be clear which branch users would go down.
<br>
A filter step can only connect to one next step.
{% endalert %}

## Analytics

| Metric | Description |
|---|---|
|Entered | The total number of times the step has been entered. If your canvas has re-eligibility and a user enters a decision split step twice, two entries will be recorded. |
|Yes | The number of entries that met the specified criteria and proceeded down the “yes” path. |
|No | The number of entries that did not met the specified criteria and proceeded down the “no” path. |
{: .reset-td-br-1 .reset-td-br-2}

![Decision Step Analytics][4]{: height="50%" width="50%"}

[1]: {% image_buster /assets/img/decision-split-1.png %}
[2]: {% image_buster /assets/img/define-split-2.png %}
[3]: {% image_buster /assets/img/use-split-onboarding-3.png %}
[4]: {% image_buster /assets/img/decision-step-analytics-4.png %}
