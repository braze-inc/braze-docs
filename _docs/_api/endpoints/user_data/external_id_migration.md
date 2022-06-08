---
nav_title: External ID Migration
article_title: "External ID Migration"
search_tag: Endpoint
page_order: 5
layout: dev_guide

description: "This landing page explains and lists the Braze External ID Migration feature."
page_type: landing

guide_top_header: "External ID Migration"
guide_top_text: "The External ID Migration API allows you to rename existing external IDs (creating a new primary ID and deprecating the existing ID) and remove deprecated IDs post-migration. <br><br> We've architected this solution to allow multiple External IDs in order to support a migration period whereby older versions of your apps still in the wild that use the previous External ID naming schema don’t break. We highly recommend removing deprecated External IDs once your old naming schema is no longer in use."

guide_featured_title: "External ID Migration Endpoints"
guide_featured_list:
  - name: "POST: Rename External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    fa_icon: fas fa-user
  - name: "POST: Remove Deprecated External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    fa_icon: fas fa-user-minus
---
