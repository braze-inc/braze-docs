---
nav_title: Canvas components
article_title: Canvas Components
page_order: 2
alias: "/user_guide/engagement_tools/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "Canvas Components"
guide_top_text: "Enhance your Canvas journey with Canvas components. Canvas components can be used to simplify the process of determining the effectiveness of your Canvas by replacing excessive full steps with just one. Components in Canvas refer to the personalized user journey in your Canvas branches."

page_type: landing
description: "This landing page is home to Canvas component articles that will help you create more advanced Canvases. Some of these components include the message step, delay step, decision split step, and more."
tool: Canvas

guide_featured_title: "Section articles"
guide_featured_list:
  - name: Message Step
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/message_step/
    image: /assets/img/braze_icons/message-square-02.svg
  - name: Delay Step
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/delay_step/
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: Decision Split Step
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/decision_split/
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: Audience Paths Step
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/audience_paths/
    image: /assets/img/braze_icons/users-01.svg 
  - name: Action Paths Step  
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/action_paths/
    image: /assets/img/braze_icons/zap.svg
  - name: Experiment Paths Step
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/experiment_step/
    image: /assets/img/braze_icons/columns-01.svg
  - name: User Update Step
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/user_update/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: Feature Flags in Canvas
    link: /docs/developer_guide/feature_flags/canvas/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: Canvas Audience Sync
    link: /docs/partners/canvas_audience_sync/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
---

## About Canvas components

With Canvas components, you can unlock new user journeys to improve your process and increase the effectiveness of your audience outreach.

### Customizing user journeys

![Example of a Canvas user journey with a Decision Split step followed by Delay steps and Message steps.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

Use [Action Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths) to split your user journey based on actions and engagement events such as making a purchase. If you want to filter through and target your audiences, [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) help simplify your user targeting by sending your users down different Canvas paths based on audience criteria.

[Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) components use a simple "yes or no" logic to create two mutually exclusive paths for your user journeys that are based on an action or a user attribute. This can help identify and target your user groups.

[Delay]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step) components allow you to delay a single step in your Canvas. This stand-alone delay step in your Canvas is best used for communicating messages to your users at a specific time. Additionally, Delay components may also increase your audience outreach by allowing more time for your audience to meet the component's criteria.

### Testing

When creating your user journeys, you may want to also test for the most effective Canvas path. With [Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step), you can test multiple Canvas paths at any step. You can also use the connections between steps as a high-level preview. Orange connections indicate the prior step will immediately advance users to the next step.

### Integration

Want to sync up with your brand's first-party user data? Leverage the available audience sync options for [Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) and [Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).

