---
nav_title: Canvas Outlines
article_title: Canvas Outlines
page_order: 2
page_type: reference
description: "This reference article covers four helpful Canvas use cases."
tool: Canvas

---

# Canvas outlines

[![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/page/courses){: style="float:right;width:120px;border:0;" class="noimgborder"}

Braze Learning offers several dedicated Canvas courses that go over common Canvas outlines. Check them out for valuable insights into technical terms and concepts explained through a mix of videos, lessons, and interactive exercises. 
- [Create customer journeys with Canvas](https://learning.braze.com/canvas-course)
- [Lapsed user Canvas](https://learning.braze.com/lapsed-user-canvas)
- [Abandoned intent Canvas](https://learning.braze.com/abandoned-intent-canvas)
- [Use case: onboarding](https://learning.braze.com/onboarding-canvas)
- [Canvas use cases for retail](https://learning.braze.com/canvas-use-cases-for-retail)

Here are several examples that demonstrate how you can use Canvas to accomplish targeted, personalized messaging using a combination of [Delay]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) and [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) steps.

{% alert important %}
As of February 28, 2023, you will no longer be able to create or duplicate Canvases using the original Canvas experience. Braze recommends that customers who use the original Canvas experience move to Canvas Flow. It's an improved editing experience to better build and manage Canvases. Learn more about [cloning your Canvases to Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

### Onboarding

Let's say your restaurant wants to help onboard users to make their first reservation. Since this Canvas is just for onboarding, an ideal time for the Canvas to launch would be at session start for all new customers. For a quick and effective way of reaching your dining audience, you can use the SMS messaging channel.

{% tabs %}
  {% tab Canvas Flow %}
    ![]({% image_buster /assets/img_archive/canvas_outline_onboarding.png %}){: style="max-width:90%;"}
  {% endtab %}

  {% tab Original Editor %}
    ![]({% image_buster /assets/img_archive/Journey_8-audience_options.png %})
  {% endtab %}
{% endtabs %}


### Upsell

Upselling your subscriptions can also be encouraged through building and sending effective Canvases. For example, if you want to upgrade active users who are on a free version of your app, you can create an action-based Canvas to trigger when a customer has reached the custom event "3 hours streamed". Using a Message step, you can prompt these customers to sign up for your premium subscriptions.

{% tabs %}
  {% tab Canvas Flow %}
    ![]({% image_buster /assets/img_archive/canvas_outline_upsell.png %}){: style="max-width:90%;"}
  {% endtab %}

  {% tab Original Editor %}
    ![]({% image_buster /assets/img_archive/Journey_9.png %})
  {% endtab %}
{% endtabs %}


### Abandoned carts

Retail businesses may often find themselves needing to remind customers of incomplete purchases. With an action-based Canvas, you can send a reminder to all registered customers to purchase the items in their abandoned carts. You can also test how receptive your customers will be to your messaging with different delay times.

{% tabs %}
  {% tab Canvas Flow %}
    ![]({% image_buster /assets/img_archive/canvas_outline_cart.png %}){: style="max-width:90%;"}
  {% endtab %}

  {% tab Original Editor %}
    ![]({% image_buster /assets/img_archive/Journey_11-audience_options.png %})
  {% endtab %}
{% endtabs %}


### Customer resources

You can use Canvases to educate customers on resources. For example, for airline businesses, you can create a Canvas that primes customers who have booked for travel in three days by scheduling a weekly email with their flight information and related airport FAQs.

{% tabs %}

  {% tab Canvas Flow %}
    ![]({% image_buster /assets/img_archive/canvas_outline_resource.png %}){: style="max-width:90%;"}
  {% endtab %}

  {% tab Original Editor %}
    ![]({% image_buster /assets/img_archive/Journey_11-audience_options.png %})
  {% endtab %}

{% endtabs %}

