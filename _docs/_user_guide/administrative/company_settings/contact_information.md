---
nav_title: Contact Information
article_title: Contact Information
page_order: 0
page_type: reference
description: "This reference article covers important information for admins on managing your company's contact information and time zone in Braze."

---

# Contact information

<style>
.fa-crown {
  color: gold;
}
</style>

> This page covers important information for admins on managing your company's contact information and time zone in Braze.

You can get to the **Company Settings** section by clicking on your name, then selecting **Company Settings** in the drop-down. If you're an admin (you'll see a <i class="fas  fa-crown" aria-label="crown icon"></i> next to your username). 

{% alert note %}
If you're using our [updated navigation]({{site.baseurl}}/navigation), you can find **Contact Information** under **Settings** > **Company Settings** > **Admin Settings** > **Contact Information**.
{% endalert %}

This page is where you can manage your company's contact information and time zone. Make sure to hit **Save** before you leave the page!

### Consequences of switching your time zone

{% alert warning %}

Switching time zones can cause some data discrepancies around the point when the time zone was changed. If someone switches their time zone, we make a good faith effort to convert things over accurately, but it is not always a perfect conversion. You may notice a discontinuity in your data, where it may switch between time zones.

{% endalert %}

If you choose to switch your time zone, you may experience a variety of consequences, including:

- While campaigns scheduled for specific times in specific locations (i.e., 9 pm Eastern Time) will run properly on schedule until edited, both campaign analytics and future campaign schedules will be affected by the change.
- Any card scheduling that is not assigned to local time may be affected, with active cards potentially appearing as finished (or vice versa).
- Segmentation filters of the form "Has done X before/after `Date`" will have the time adjusted because the initial date will now be localized in Pacific Time.