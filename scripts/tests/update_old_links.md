---
article_title: Update old links testing

guide_featured_title: "More links"
guide_featured_list:
- name: Good link 1
  link: https://www.braze.com/docs/developer_guide/platform_wide/getting_started/analytics_overview
- name: Good link 2
  link: /docs/developer_guide/getting_started/analytics_overview
- name: Bad link 1
  link: /docs/best_practices/#android-push-category
- name: Bad link 2
  link: /docs/user_guide/message_building_by_channel/email/link_templates/
- name: Bad link 3
  link: /docs/user_guide/message_building_by_channel/email/link_templates/
---

This is a test page for testing `ulinks`. When adding "bad links", the syntax needs to match the syntax on this page:

https://www.braze.com/docs/contributing/content_management/cross_referencing

i.e. no `/docs` should be found in the `site.baseurl`.

Here's some bad links:
1. [Bad link 1]({{site.baseurl}}/best_practices/).
2. [Bad link 2]({{site.baseurl}}/best_practices/#android-push-category).
3. [Bad link 3]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/).

Here's two good links:
1. [Good link 1](https://www.braze.com/docs/developer_guide/platform_wide/getting_started/analytics_overview)
2. [Good link 2]({{site.baseurl}}/developer_guide/getting_started/analytics_overview)
