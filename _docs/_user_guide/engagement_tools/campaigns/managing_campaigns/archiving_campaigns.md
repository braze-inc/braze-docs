---
nav_title: Archiving Campaigns
article_title: Archiving Campaigns
page_order: 2
page_type: reference
description: "This reference article goes over how to archive a pre-existing campaign, the effects of archiving a campaign, and how to resume that campaign if needed."
tool:
  - Campaigns

---

# Archiving campaigns

> If you'd like to stop a campaign from sending or clear it from your dashboard, you can archive it. Go to the **Campaigns** page, click the gear icon next to the campaign's name and click **Archive**.

![]({% image_buster /assets/img_archive/Archiving.png %})

When you archive a campaign, no further messages from that campaign will be delivered. In the case of in-app messages, no further in-app messages from that campaign will be displayed to users.

There are also bulk actions you can use, such as deactivating and archiving multiple campaigns by checking the boxes next to the campaigns and clicking the relevant button.

![]({% image_buster /assets/img_archive/Archive_pause_selected.png %})

To view archived messages from the **Campaigns** page, select the **Archived** folder.

![]({% image_buster /assets/img_archive/Include_archived.png %})

## Unarchiving campaigns

While clicking on an archived campaign will allow you to view its past results, you won't be able to edit the campaign. You will need to unarchive campaign in order to edit it. To unarchive a campaign, you must select the campaign within the **Archived** folder and click **Unarchive Selected**.

![]({% image_buster /assets/img_archive/unarchive_selected.png %})

Unarchiving a campaign does not make it live. This will simply move your campaign to the **Active** campaign folder where you can make edits and review how the campaign is set up. At this point, your campaign will be stopped and won't send any messages. 

If you wish to resume the campaign and begin sending messages, click the gear icon next to the campaign and select **Resume**.

![]({% image_buster /assets/img_archive/resume_unarchived.png %})

{% alert warning %}
When you archive a Segment, any campaigns using it will also be archived.
{% endalert %}

[1]: {% image_buster /assets/img_archive/Archiving.png %}
[2]: {% image_buster /assets/img_archive/Include_archived.png %}
[3]: {% image_buster /assets/img_archive/Archive_pause_selected.png %}
[4]: {% image_buster /assets/img_archive/unarchive_selected.png %}
[5]: {% image_buster /assets/img_archive/resume_unarchived.png %}
