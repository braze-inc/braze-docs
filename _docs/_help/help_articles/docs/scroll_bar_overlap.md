---
nav_title: Scroll bar overlap
article_title: Scroll Bar Overlap
page_order: 0

page_type: solution
description: "This help article walks Mac users through how to resolve scroll bars overlapping content within Braze docs."
---

# Scroll bar overlap

Are you using a Mac and find that your scroll bars are overlapping content within Braze Docs like in the following example?

![Example of scroll bar overlap]({% image_buster /assets/img/scroll-overlap.png %})

Check if your scroll bar overlaps the following code block:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.S3.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.S3.integration.<integration-id>+<partition>+<offset>.avro
```

If your scroll bar overlaps the code block, we suggest changing the **Show scroll bars:** setting to **Always** in your **General Settings**. This will expand features in Docs (like code blocks) to always show the scroll bar and prevent illegibility.

![MacOS General Settings]({% image_buster /assets/img/general-on-mac.png %})

Here's what your updated scroll bar should look like now:

![Example of fixed scroll bar without overlap]({% image_buster /assets/img/scroll-bar-on.png %})

_Last updated on March 27, 2019_

{% comment %}
Insert this where there is a single line of long code that might cause issues:
_Can't see the code because of the scroll bar? See how to fix that [here]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/)._
{% endcomment %}

