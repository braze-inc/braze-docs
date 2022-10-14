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

## Original workflow editor

The four outlines show a previous version of the Canvas entry step in the original Canvas editor. 

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

