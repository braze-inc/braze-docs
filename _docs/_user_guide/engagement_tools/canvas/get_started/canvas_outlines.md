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

## Canvas Flow

Using Canvas Flow, check out these four outlines that demonstrate how you can build a user journey for common use cases.

{% tabs %}
  {% tab Onboarding %}
    Let's say your restaurant wants to help onboard users to make their first reservation. An ideal time for the Canvas to launch would be at session start for all new customers since this is solely for onboarding. For a quick and effective way of reaching your dining audience, you can use the SMS messaging channel.
  {% endtab %}

  {% tab Upsell %}
    Upselling your subscriptions can also be encouraged through building and sending effective Canvases. For example, if you want to upgrade active users who are on a free version of your app, you can create an action-based Canvas to trigger when a customer has reached the custom event "3 hours streamed". Using a Message step, you can prompt these customers to sign up for your premium subscriptions.
  {% endtab %}

  {% tab Cart abandonment %}
    Retail businesses may often find themselves needing to remind customers of incomplete purchases. With an action-based Canvas, you can send a reminder to all registered customers to purchase the items in their abandoned carts. 
  {% endtab %}

  {% tab Educate %}
    You can use Canvases to educate customers on resources. For example, you can create a Canvas that primes customers who have booked for travel in three days by scheduling a weekly email with their flight information and related airport FAQs.
  {% endtab %}
{% endtabs %}


## Original workflow editor

These four outlines show a previous version of the Canvas entry step in the original Canvas editor. 

{% tabs %}
  {% tab Onboarding %}
  	Restaurant reservation<br>**What**: Onboarding users to their first reservation<br>**When**: Triggered at session start<br>**Who**: All New Customers<br>**Why**: Perform custom event “completed reservation”<br>**Where**: Push, Email<br>**How**: Channel, Content (test)<br>![]({% image_buster /assets/img_archive/Journey_8-audience_options.png %})
  {% endtab %}

  {% tab Upsell %}
  	Music streaming<br>**What**: Upgrading active freeloaders to basic premium subscription<br>**When**: Triggered after custom event of “milestone - 3 hours music streamed”<br>**Who**: All Active, but free customers<br>**Why**: Perform custom event "visit pricing page"<br>**Where**: Push, Email, Webhook<br>**How**: Content, Discount<br>![]({% image_buster /assets/img_archive/Journey_9.png %})
  {% endtab %}

  {% tab Cart abandonment %}
  	Clothing retail<br>**What**: Reminding customers of incomplete purchases<br>**When**: Triggered after custom event “abandoned cart”<br>**Who**: All registered customers<br>**Why**: Make Purchase<br>**Where**: Push, Email<br>**How**: Channel, Trigger (test)<br>![]({% image_buster /assets/img_archive/Journey_10.png %})
  {% endtab %}

  {% tab Educate %}
  	Airline<br>**What**: Educate customers on resources and prime them for good flight and airport experiences<br>**When**: Scheduled daily until January 1 <br>**Who**: Customers booked for travel in two days with the app <br>**Why**: Start Session <br>**Where**: Push <br>**How**: Channel, Cadence (test)<br>![]({% image_buster /assets/img_archive/Journey_11-audience_options.png %})
  {% endtab %}
{% endtabs %}

