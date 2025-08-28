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

![A Decision Split step named "Push enabled?" for users who aren't push enabled and users who are push enabled.]({% image_buster /assets/img/decision-split-1.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-top:15px;margin-bottom:15px;"}

This component can be used to create Canvas branches based on whether a user matches a query.

## Create a decision split 

To create a decision split in your workflow, add a step to your Canvas. Then, drag and drop the component from the sidebar, or select the <i class="fas fa-plus-circle"></i> plus button at the bottom of a step and select **Decision Split**.

### Define your split

How do you want to split your users? You can use [segments]({{site.baseurl}}/user_guide/engagement_tools/segments/) and filters to draw the line. Essentially, you're creating a `true` or `false` query that will evaluate your users and then funnel them to one step or another. You must use at least one segment or one filter. You do not need to use both a segment and a filter.

![A Decision Split step with the filter "Foreground Push Enabled is true" selected.]({% image_buster /assets/img/define-split-2.png %}){: style="max-width:90%;"}

{% alert note %} 
By default, segments and filters for a Decision Split step are checked right after receiving a previous step, unless you add a delay. 
{% endalert %} 

## Use your split

Using a decision split can help you distinguish paths for your users based on their segment or their attributes, even whether they use certain messaging channels to receive your messages!

Let's say that you're creating an onboarding flow. You might start with a welcome email upon signing up. Then, two days later, you want to send a push message, but only to users who are push enabled. After that, all users get another email three days after they signed up. You could also use your decision split to send an in-app message to users who don't have push enable to encourage them to enable push.

If there is no step following one of the paths, users who go down that path will exit the Canvas. 

![A Decision Split step named "Push enabled?" for users who aren't push enabled and those who are. For users who aren't push enabled, they'll experience a 3-day delay then receive an email message. For users who are push enabled, they will experience a 1-day delay, receive a push notification followed by a 2-day delay, then they'll receive the same email message as the users who aren't push enabled.]({% image_buster /assets/img/use-split-onboarding-3.png %}){: style="max-width:60%"}

## Analytics

Refer to the following table for descriptions of analytics for this step:

| Metric | Description |
|---|---|
| _Entered_ | The total number of times the step has been entered. If your Canvas has re-eligibility and a user enters a Decision Split step twice, two entries will be recorded. |
| _Yes_ | The number of entries that met the specified criteria and proceeded down the "yes" path. |
| _No_ | The number of entries that did not meet the specified criteria and proceeded down the "no" path. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

