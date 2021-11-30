---
nav_title: Archiving Campaigns
article_title: Archiving Campaigns
page_order: 1
page_type: reference
description: "This reference article goes over how to archive a pre-existing campaign, the effects of archiving a campaign, and how to resume that campaign if needed."
tool:
  - Campaigns

---

# Archiving campaigns

> This reference article goes over how to archive a pre-existing campaign, the effects of archiving a campaign, and how to resume that campaign if needed.

If you'd like to stop a campaign from sending or clear it from your dashboard, you can archive it. Go to the **Campaigns** page, click the gear icon next to the campaign's name and click **Archive**.

![Archiving][1]

Archiving a campaign will accomplish the following:

- No further messages from that campaign will be delivered. In the case of in-app messages, no further in-app messages from that campaign will be displayed to users.
- The campaign's indicators will be removed from:
	- The Detailed Statistics graph on the **Overview** page
	- The Detailed Statistics graph on the **Revenue** page
	- The Custom Events Over Time graph

There are also bulk actions you can use, such as deactivating and archiving multiple campaigns by checking the boxes next to the campaigns and clicking the Revelant button.

![Archive Selected][3]

To view archived messages from the **Campaigns** page, select the **Archived** folder.

![Include Archived][2]

## Unarchiving campaigns

While clicking on an archived campaign will allow you to view its past results, you won't be able to edit the campaign. You will need to unarchive campaign in order to edit it. To unarchive a campaign, you must select the campaign within the **Archived** folder and click **Unarchive Selected**.

![Unarchive Campaign][4]

Unarchiving a campaign does not make it live. This will simply move your campaign to the **Active** campaign folder where you can make edits and review how the campaign is set up. At this point, your campaign will be stopped and won't send any messages. 

If you wish to resume the campaign and begin sending messages, click the gear icon next to the campaign and select **Resume**.

![Resume Campaign][5]

{% alert warning %}
When you archive a Segment, any campaigns using it will __also be archived__.
{% endalert %}

[1]: {% image_buster /assets/img_archive/Archiving.png %}
[2]: {% image_buster /assets/img_archive/Include_archived.png %}
[3]: {% image_buster /assets/img_archive/Archive_pause_selected.png %}
[4]: {% image_buster /assets/img_archive/unarchive_selected.png %}
[5]: {% image_buster /assets/img_archive/resume_unarchived.png %}
