---
nav_title: "Templates & Media"
page_order: 5
layout: featured
guide_top_header: "Templates & Media"
guide_top_text: "Templates & Media allow you to manage templates and upload images for messages in a single, centralized location. You can consolidate and organize your templates across the dashboard for a coherent look and feel."

guide_featured_title: "Popular Articles"
guide_featured_list:
  - name: Media Library
    link: /docs/user_guide/engagement_tools/templates_and_media/media_library/
    fa_icon: fas fa-book-open
  - name: Content Blocks
    link: /docs/user_guide/engagement_tools/templates_and_media/content_blocks/
    fa_icon: fas fa-columns
---

## About Templates & Media

To access this Templates & Media, navigate to __Engagement__ in your left navigation bar of your Braze account, then select __Templates & Media__.

![Templates and Media][1]

Aggregate templates across the following features:

- [Email Templates][2]
- [Content Blocks][7]
- [Webhook Templates][3]
- [Link Templates][6]
- [In-App Message Color Profiles][4]
- [Manage Assets in the Media Library][5]

<br>

## Duplicate Templates in Templates & Media

Duplicating a template can save a lot of time.  Braze now offers two different ways to duplicate a template

### Duplicate an individual Template
Duplicating an individual template can be achieved by clicking the cog located on the template grid screen and hitting 'duplicate' [template_duplicate_cog][8]

{% alert note %}
For Content Block templates, a 'draft' copy is created.  For all other templates a new duplicate copy is automatically created.
{% endalert %}


### Duplicate multiple Templates
Duplicating multiple templates can be achieved by selecting the checkbox next to the template name.  Select multiple templates and then click the "Duplicate" button that appears.  Duplicated templates can be found by sorting the 'last edited' column.  By default the new templates will by named "Copy of {{original template name}}"
[duplicate_multiple_template] [9]

## Archive Templates in Templates & Media

Archiving templates can help better organize the template section.

### Archive an individual Template
Archiving an individual template can be achieved by clicking the cog located on the template grid screen and hitting 'archive' [template_archive_cog][10]


### Archive multiple Templates
Archiving multiple templates can be achieved by selecting the checkbox next to the template name.  Select multiple templates and then click the "Archive" button that appears.  Archived templates can be found clicking the "Archived".  

[archive_multiple_template] [11]


{% alert note %}
Duplicating and Archiving is not currently available for Link Templates
{% endalert %}


[1]: {% image_buster /assets/img_archive/templates_and_media.png %}
[2]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[3]: {{ site.baseurl }}/user_guide/message_building_by_channel/webhooks/webhook_template/#creating-a-webhook-template
[4]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile
[5]: {{ site.baseurl }}/user_guide/engagement_tools/templates_and_media/media_library/#media-library
[6]: {{ site.baseurl }}/user_guide/message_building_by_channel/email/link_templates/#link-templates
[7]: {{ site.baseurl }}/user_guide/engagement_tools/templates_and_media/content_blocks/
[8]: {% image_buster /assets/img_archive/template_duplicate_cog.png %}
[9]: {% image_buster /assets/img_archive/duplicate_multiple_template.gif %}
[10]: {% image_buster /assets/img_archive/template_archive_cog.png %}
[11]: {% image_buster /assets/img_archive/archive_multiple_template.gif %}
