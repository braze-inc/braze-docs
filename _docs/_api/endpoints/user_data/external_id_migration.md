---
nav_title: External ID migration
article_title: "External ID Migration"
search_tag: Endpoint
page_order: 7
layout: dev_guide

description: "This landing page explains and lists the Braze external ID migration feature."
page_type: landing

guide_top_header: "External ID Migration"
guide_top_text: "The External ID Migration API allows you to rename existing external IDs (creating a new primary ID and deprecating the existing ID) and remove deprecated IDs post-migration. <br><br> We've designed this solution to allow multiple external IDs in order to support a migration period whereby older versions of your apps still in the wild that use the previous external ID naming schema don't break. We highly recommend removing deprecated external IDs when your old naming schema is no longer in use."

guide_featured_title: "External ID Migration Endpoints"
guide_featured_list:
  - name: "POST: Rename External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Remove Deprecated External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
