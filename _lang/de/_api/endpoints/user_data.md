---
nav_title: Nutzerdaten
article_title: Nutzerdaten Endpunkte
search_tag: Endpoint
page_order: 9

local_redirect: #event-object-specification #purchase-object-specification
  event-object-specification: '/docs/api/objects_filters/event_object/'
  purchase-object-specification: '/docs/api/objects_filters/purchase_object/'

layout: dev_guide

#Required
description: "Diese Landing Page listet die Endpunkte der Nutzerdaten von Braze auf."
page_type: landing

guide_top_header: "Nutzerdaten Endpunkte"
guide_top_text: "Die Endpunkte von Braze User Data ermöglichen es Ihnen, Informationen über Ihre Nutzer:innen zu tracken, indem Sie Daten über Ihre Nutzer:innen protokollieren, die von außerhalb Ihrer mobilen App stammen. Sie können diese API auch verwenden, um Nutzer:innen zu Test- oder anderen Zwecken zu löschen. <br> <br> Alle API Endpunkte haben ein Limit für die Daten-Nutzlast von 4 MB. Der Versuch, mehr als 4 MB Daten zu posten, schlägt mit der Meldung HTTP 413 Request Entity Too Large fehl. <br> <br> Die Beispiele in diesem Abschnitt enthalten die URL https://rest.iad-01.braze.com. Möglicherweise müssen Sie jedoch eine andere Endpunkt-URL verwenden (z. B. wenn Sie im Braze EU-Datenzentrum gehostet werden oder eine spezielle Braze-Installation haben). Ihr Customer-Success-Manager:in von Braze wird Sie informieren, wenn Sie eine andere Endpunkt-URL verwenden sollten."

guide_featured_title: "Nutzerdaten Endpunkte"
guide_featured_list:
  - name: "POST: Erstellen eines neuen Nutzer:in-Alias"
    link: /docs/api/endpoints/user_data/post_user_alias/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Update eines Nutzer:in-Alias"
    link: /docs/api/endpoints/user_data/post_users_alias_update/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Nutzerdaten löschen"
    link: /docs/api/endpoints/user_data/post_user_delete/
    image: /assets/img/braze_icons/user-minus-01.svg
  - name: "POST: Bezeichner eines Nutzers:in"
    link: /docs/api/endpoints/user_data/post_user_identify/
    image: /assets/img/braze_icons/user-circle.svg
  - name: "POST: Nutzer:innen tracken"
    link: /docs/api/endpoints/user_data/post_user_track/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST: Nutzer:innen verfolgen (Synchron)"
    link: /docs/api/endpoints/user_data/post_user_track_synchronous/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST: Nutzer:innen zusammenführen"
    link: /docs/api/endpoints/user_data/post_users_merge/
    image: /assets/img/braze_icons/users-01.svg

guide_menu_title: "External ID migration endpoints"
guide_menu_list:
  - name: "POST: Externe IDs umbenennen"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Veraltete externe IDs entfernen"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
