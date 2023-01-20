---
nav_title: Pre and Post-Launch Checklist
article_title: Pre and Post-Launch Checklist
page_order: 2
description: "This article provides a guideline for things to check before and after you launch a Canvas."
tool: Canvas

---

# Pre and post-launch checklist

## Things to consider before launch

Before sending a Canvas to your audience, there are several details you may want to double-check to ensure that your messaging and send times align with your audience's preferences. 

### Review time zone settings

If you're entering users according to their local time zone using Scheduled entry, you should launch your Canvas at least 24 hours prior to when you want users to enter your Canvas. 

For example, here’s a Canvas that isn’t leaving enough time between the launch and the scheduled entry time. You’ll see an alert if you haven’t built in enough of a buffer.

### Consider using regex for audience filters

Check over your segments or filters in your **Target Audience** settings, and review the Target Population summary at the bottom of the screen.

If you notice that your target audience is smaller than expected, try using “Matches Regex” or “Does Not Match Regex” instead of “Equals” or “Does Not Equal.” This may account for those missing users, and target a larger audience.

Regex is a string, which means it recognizes patterns and takes into account characters, instead of things like capitalization. This means that if you're using Equals / Does Not Equal, you could be limiting your audience size because of simple syntax errors.

You may consider using regex for segments or filters in audience paths components, delivery validation settings in message components, and decision split components as well.
 
### Identify entry settings and race conditions

A race condition can occur when you've used the same entry criteria in both your Entry Schedule and Target Audience settings. If you’re using Action-Based entry in your Entry Schedule, check that you haven’t used the same trigger action here as in your Target Audience. A race condition may occur in which the user is not in the audience at the time they perform the trigger event, which means they won’t enter the Canvas.

### Check Canvas entry properties and event properties

Though similar in name, Canvas entry properties and event properties function differently within your Canvas workflows. Canvas entry properties are tied to your entry settings, and they can be referenced in any message component throughout your Canvas. Canvas entry properties are properties of the event or API call that triggers a user’s entry into a Canvas, using Action-Based or API-Triggered entry settings.

Event properties, on the other hand, can only be referenced in the first message component following an action paths component. Event properties are properties of a custom event or purchase event that the user performed during the evaluation window of an action paths component, and that triggers their progression down one of the defined action paths.

Check your message preview for any message components referencing Canvas entry properties or event properties.

### Review message components for user advancement

By default, users will advance through all message components regardless of whether they received the message. If you would like instead to advance only those users who receive a particular message, you can do so by adding a decision split component directly after your message component. Add the filter “Received Message from Canvas Step” as criteria for your split, and select the correct Canvas and message component from the two dropdown menus.

For message components with in-app messaging, you may want to use an action paths component instead of the decision split component. This will allow you to advance users based on whether they’ve viewed your in-app message. Define an action group by adding the filter “Interact with Step” and select “View in app message.” Then, set the evaluation window of the component to the expiration window of the in-app message.

For message components with multi-channel messaging, we recommend:
* For any multi-channel message component, include a delay component in between your message component and decision split component and set the delay to at least 5 seconds
* For a multi-channel message component that includes Intelligent Timing, set the delay to 24 hours
* For a multi-channel message component that includes rate limiting, split your messages into several single-channel message components and connect them together. Then connect the decision split component directly after the last message component to check whether a user received any of the messages. You can also use this method as an alternative for a multi-channel message component with Intelligent Timing.

## Things to consider after launch



