---
nav_title: Auto Advance
permalink: /auto_advance/
---

# Auto Advance

Auto-Advance is an option on Canvas Steps that allows users to continue down the Canvas, even if they do not receive a message from that particular step.

![auto.png][1]

When Auto-Advance **is not selected,** users must receive one or more messages from a step in order to be eligible for subsequent steps. Customers who do not receive at least one message for a given step will exit the Canvas and will not be evaluated for subsequent steps.

When Auto-Advance **is selected** for a step, users who are eligible for the step but do not receive one or more messages from the step continue to make their way down the Canvas and are evaluated for subsequent steps.

If Auto-Advance is selected, users will be Auto-Advanced when the following scenarios occur:

**User Was Not Eligible For Channel**

• Customer does not receive an iOS push message because they do have a push token for iOS push

• Customer does not receive a push because they are not subscribed to push

• Customer does not receive an email because they do not have a valid email address

• Customer does not receive an email because they are not subscribed to email

**Message Aborts For Customer**

• Customer does not receive a message because the "Abort Message" liquid tag was called

Users will not be Auto-Advanced if they are frequency capped from the Canvas Step. If a user does not receive a Canvas Step due to frequency capping, they will exit the Canvas.


**Note** users must be eligible for a step in order to be Auto-Advanced through it. If a user does not meet the audience options for a step they will not be evaluated for that step, therefore they will not be eligible for Auto-Advance. If a user performs an exception event for a step, they are not eligible for the step and will exit the Canvas.

**Note** customers who advance through a step without receiving messages will not be counted as a unique recipient for the step. Users must receive one or more messages from a step to be counted as a unique recipient.

**Note** When sending a multichannel step with intelligent delivery, we may send or attempt to send messages at different times for different channels. Braze will Auto-Advance users at the time that the first message in a step attempts to send.   

[1]: {% image_buster /assets/img_archive/auto.png %} "Auto-Advance"
