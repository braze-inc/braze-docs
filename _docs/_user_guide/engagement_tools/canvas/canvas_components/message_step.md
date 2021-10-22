---
nav_title: Message Step
article_title: Message Step
alias: "/message_step/"
page_order: 5
page_type: reference
description: "This reference article covers how to create a stand-alone message using the Canvas messaging step."
tool: Canvas

---

# Message Step

Message Steps allow you to add a standalone message where you want in your Canvas flow.

{% alert important %}
Support for Canvas Message Steps is currently in early access. Please contact your Braze account manager if you are interested in participating in the early access.
{% endalert %}

## Create a Message Step

![Canvas Message Step][1]{: style="float:right;max-width:19%;margin-left:15px;"}

To create a Message Step, add a step to your Canvas. Then, use the drop-down at the top of the new step to select Message Step.

Then simply set up your messages as you do now in the “Messages” section of the Full Step.

With a Message Step, all users who enter the step advance to the next step when any one of the following conditions is met:
- Any message is sent
- A message is not sent because the user is not reachable with a channel
- A message is not sent because it is frequency capped
- A message is not sent because it is aborted

![Canvas Message Step][2]{: style="max-width:80%;"} 

## Analytics

| metric | description |
| `Entries` | Reflects the number of times the step has been entered. If your Canvas has re-eligibility and a user enters a Message Step twice, two entries will be recorded. |
| `Proceeded to Next Step` | Reflects the number of entries that proceeded to the next step in the Canvas. |
| `Sends` | Reflects the total number of messages the step has sent. If your Canvas re-eligibility and a user enters a Message Step twice, two entries will be recorded. |
| `Unique Recipients` | Reflects the number of users who have received messages from this step. |
{: .reset-td-br-1 .reset-td-br-2}

![Canvas Message Step][3]{: style="max-width:20%;"}


[1]: {% image_buster /assets/img/canvas_components/components1.png %}
[2]: {% image_buster /assets/img/canvas_components/components2.png %}
[3]: {% image_buster /assets/img/canvas_components/components3.png %}
