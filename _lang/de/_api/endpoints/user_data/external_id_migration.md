---
nav_title: Externe ID-Migration
article_title: "Externe ID-Migration"
search_tag: Endpoint
page_order: 7
layout: dev_guide

description: "Auf dieser Landing Page wird die Funktion zur Migration externer IDs von Braze erklärt und aufgelistet."
page_type: landing

guide_top_header: "Externe ID-Migration"
guide_top_text: "Mit der API für die Migration externer IDs können Sie bestehende externe IDs umbenennen (indem Sie eine neue primäre ID erstellen und die bestehende ID veralten lassen) und veraltete IDs nach der Migration entfernen. <br><br> Wir haben diese Lösung so konzipiert, dass sie mehrere externe IDs zulässt, um eine Migrationsphase zu unterstützen, in der ältere Versionen Ihrer Anwendungen, die noch im Umlauf sind und das vorherige Namensschema für externe IDs verwenden, nicht kaputt gehen. Wir empfehlen dringend, veraltete externe IDs zu entfernen, wenn Ihr altes Benennungsschema nicht mehr verwendet wird."

guide_featured_title: "Externe ID-Migrationsendpunkte"
guide_featured_list:
  - name: "POST: Externe IDs umbenennen"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST: Veraltete externe IDs entfernen"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
