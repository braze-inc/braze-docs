---
nav_title: Benutzerdaten
article_title: Endpunkte für Benutzerdaten
search_tag: Endpoint
page_order: 9

local_redirect: #event-object-specification #purchase-object-specification
  event-object-specification: '/docs/api/objects_filters/event_object/'
  purchase-object-specification: '/docs/api/objects_filters/purchase_object/'

layout: dev_guide

#Required
description: "Diese Landing Page listet die Endpunkte für Braze-Benutzerdaten auf."
page_type: landing

guide_top_header: "Endpunkte für Benutzerdaten"
guide_top_text: "Die Braze User Data-Endpunkte ermöglichen es Ihnen, Informationen über Ihre Benutzer zu verfolgen, indem Sie Daten über Ihre Benutzer protokollieren, die von außerhalb Ihrer mobilen App stammen. Sie können diese API auch verwenden, um Benutzer zu Test- oder anderen Zwecken zu löschen. <br> <br> Alle API-Endpunkte haben ein Limit von 4 MB für die Nutzdaten. Der Versuch, mehr als 4 MB Daten zu posten, schlägt mit einer HTTP 413 Request Entity Too Large fehl. <br> <br> Die Beispiele in diesem Abschnitt enthalten die URL https://rest.iad-01.braze.com. Möglicherweise müssen Sie jedoch eine andere Endpunkt-URL verwenden (z. B. wenn Sie im Braze EU-Rechenzentrum gehostet werden oder eine eigene Braze-Installation haben). Ihr Braze Customer Success Manager wird Sie informieren, wenn Sie eine andere Endpunkt-URL verwenden sollten."

guide_featured_title: "Endpunkte für Benutzerdaten"
guide_featured_list:
  - name: "POST: Einen neuen Benutzer-Alias erstellen"
    link: /docs/api/endpoints/user_data/post_user_alias/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Einen Benutzer-Alias aktualisieren"
    link: /docs/api/endpoints/user_data/post_users_alias_update/
    image: /assets/img/braze_icons/user-edit.svg
  - name: "POST: Benutzerdaten löschen"
    link: /docs/api/endpoints/user_data/post_user_delete/
    image: /assets/img/braze_icons/user-minus-01.svg
  - name: "POST: Identifizieren Sie einen Benutzer"
    link: /docs/api/endpoints/user_data/post_user_identify/
    image: /assets/img/braze_icons/user-circle.svg
  - name: "POST: Benutzer verfolgen"
    link: /docs/api/endpoints/user_data/post_user_track/
    image: /assets/img/braze_icons/database-01.svg
  - name: "POST: Benutzer zusammenführen"
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
