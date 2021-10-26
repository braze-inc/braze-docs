---
nav_title: Scroll Bar Overlap
article_title: Scroll Bar Overlap
page_order: 0

page_type: solution
description: "This help article walks Mac users through how to resolve scroll bars overlapping content within Braze docs."
---

# Scroll bar overlap

Are you using a Mac and find that your scroll bars are overlapping content within Braze Docs like the example below?

![Scroll Bar Overlap][1]

Check if your scroll bar overlaps the code block below:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.S3.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.S3.integration.<integration-id>+<partition>+<offset>.avro
```

If your scroll bar overlaps the code block, we suggest changing the `Show scroll bars:` setting to "Always" in your General Settings. This will expand features in Docs (like code blocks) to always show the scroll bar and prevent illegibility.

![General Settings][2]

Here's what your updated scroll bar should look like now:

![Scroll Fixed][3]

_Last updated on March 27, 2019_

{% comment %}
Insert this where there is a single line of long code that might cause issues:
_Can't see the code because of the scroll bar? See how to fix that [here]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/)._
{% endcomment %}

[1]: {% image_buster /assets/img/scroll-overlap.png %}
[2]: {% image_buster /assets/img/general-on-mac.png %}
[3]: {% image_buster /assets/img/scroll-bar-on.png %}
