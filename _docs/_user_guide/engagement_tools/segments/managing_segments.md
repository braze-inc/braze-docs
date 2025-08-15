---
nav_title: Managing Segments
article_title: Managing Segments
page_order: 1
page_type: tutorial
tool: Segments
description: "This article covers the actions you can take to manage your segments, such as filtering a list of segments, creating segments, and editing segments."

---

# Managing Segments

> The Segments section allows you to view a comprehensive list of your existing segments, create new segments, and edit existing segments. You can refine the list of segments by selecting a variety of filters and columns so only the most relevant information to you is displayed.

![The Segments section displaying a list of Active segments.]({% image_buster /assets/img/segment/segments_page.png %})

## Customizing your view

Tailor your view of the segments list by using filters and changing the columns that you want to appear. When you leave the **Segments** section and return, the list will revert to the default view, clearing any filters you previously selected.

### Status filter

You can narrow the list to display only active or archived segments. Any non-archived segment is considered active.

### Filters

Sort through the segments in the list by adjusting the following filters:
- **Last Edited By:** The user that last edited the segments
- **Last Edited:** Time range in which the segments were last edited
- **Estimated Size:** Approximate range of how many users are in the segments
- **Tags:** Tags associated with the segments
- **Teams:** Teams associated with the segments
- **Advanced Tracking Segments Only:** View only the segments that have [Analytics Tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) enabled.

### Columns

These are the columns of information that you can select to display in the segment list:
- **Filters:** Number of filters in the segment
- **Last edited:** Date the segment was last edited
- **Last edited by:** The user that last edited the segment
- **Tags:** Tags associated with the segment
- **Teams:** Teams associated with the segment
- **Estimated size:** Estimated number of users in the segment
- **Canvases:** Number of Canvases that use the segment
- **Campaigns:** Number of campaigns that use the segment

### Show starred only

Selecting **Show Starred Only** narrows your view to the segments that were starred by you.

## Viewing a segment's messaging use

Go to a segment's **Messaging Use** section for an overview of where the segment is being used, such as within other segments, campaigns, and Canvases.

{% alert note %}
To prevent loops of segments referencing one another, segments that use the **Segment Membership** filter can't be referenced by other segments. For more details, refer to [Segmentation Filters]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).
{% endalert %}

## Managing specific segments

![The edit menu for a segment showing the options "Edit", "Duplicate", "Archive", and "Add to starred".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

To manage a specific segment, hover over it and select the menu icon at the end of the row to reveal the following options:
- **Edit:** Edit the filters in your segment.
- **Duplicate:** Make a copy of your segment.
- **Archive:** Archive the segment. Note that this will also archive any campaigns or Canvases that use that segment.
- **Add to starred:** Star the segment, which allows you to quickly access it by checking the Show starred only box in the segments section.
 
You can also perform bulk actions–specifically, bulk archiving and bulk tagging–by checking the boxes next to multiple segment names.

![Multiple segments selected with "CRM" selected in the "Tag As" dropdown field.]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Changes Since Last Viewed

The number of updates to the segments from other members of your team is tracked by the *Changes Since Last Viewed* metric on the segment overview page. Select **Changes Since Last Viewed** to view a changelog of updates to the segment's name, description, and target audience. For each update, you can see who performed the update and when. You can use this changelog to audit changes to your segment.

## Searching for segments
Search for segment names by entering terms into the search field. 

All terms and strings entered in this field will be searched for. For example, searching for “test segment 1” will return segments with “test”, “segment”, or “1” anywhere in their name. To search for an exact string, put quotes around your search term. Searching for [“test segment 1”] will return all segments that contain the exact phrase “test segment 1” in their name.

![The search results for entering "all users" into the search field include "All Users (Test)", "All Users", "All Users 15".]({% image_buster /assets/img/segment/segments_search.png %})

