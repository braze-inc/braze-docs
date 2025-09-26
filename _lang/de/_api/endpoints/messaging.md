---
nav_title: Nachrichten
article_title: Messaging Endpunkte
search_tag: Endpoint
page_order: 3
local_redirect: #app-group-rest-api-key #app-identifier #external-user-id #segment-identifier #campaign-identifier #canvas-identifier #trigger-properties #canvas-identifier #server-responses #fatal-errors #responses-for-tracked-send-ids #messaging-queued #canvas-entry-properties
  app-group-rest-api-key: '/docs/api/basics/#rest-api-key'
  app-identifier: '/docs/api/identifier_types/'
  external-user-id: '/docs/api/objects_filters/user_attributes_object/#braze-user-profile-fields'
  segment-identifier: '/docs/api/identifier_types/'
  campaign-identifier: '/docs/api/identifier_types/'
  canvas-identifier: '/docs/api/identifier_types/'
  send-identifier: '/docs/api/identifier_types/'
  trigger-properties: '/docs/api/objects_filters/trigger_properties_object'
  canvas-entry-properties: '/docs/api/objects_filters/canvas_entry_properties_object'
  server-responses: '/docs/api/errors/'
  messaging-queued: '/docs/api/errors/'
  responses-for-tracked-send-ids: '/docs/api/errors/'
  fatal-errors: '/docs/api/errors/'

layout: dev_guide

#Required
description: "Diese Landing Page listet die Messaging Endpunkte von Braze auf."
page_type: landing

guide_top_header: "Messaging Endpunkte"
guide_top_text: "Die Braze Messaging API bietet Ihnen zwei verschiedene Optionen für den Versand von Nachrichten an Ihre Nutzer:innen. Sie können den Inhalt der Nachrichten und die Konfiguration in der API-Anfrage mit dem <code class='highlighter-rouge'>/messages/send</code> und `/messages/schedule` Endpunkte. Alternativ können Sie die Details Ihrer Nachricht mit einer API-getriggerten Kampagne im Braze-Dashboard verwalten und mit den Endpunkten `/campaigns/trigger/send` und `/campaigns/trigger/schedule` einfach kontrollieren, wann und an wen sie gesendet wird. In den folgenden Abschnitten wird die Spezifikation der Anfrage für beide Methoden erläutert. <br> <br> Ähnlich wie bei anderen Kampagnen können Sie die Anzahl der Male, die ein bestimmter Nutzer eine Messaging-API-Kampagne erhalten kann, begrenzen, indem Sie im Braze-Dashboard [Wiederzulassungseinstellungen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/#re-eligibility-with-api-triggered-campaigns) konfigurieren. Braze wird keine API Nachrichten an Nutzer:innen zustellen, die sich nicht wieder für die Kampagne qualifiziert haben, unabhängig davon, wie viele Anfragen an die API gesendet werden. <br> <br> Mit den Endpunkten für das Senden von Nachrichten können Sie sofortige Nachrichten an bestimmte Nutzer:innen senden. Wenn Sie ein Segment Targeting betreiben, wird eine Aufzeichnung Ihrer Anfrage im **Messaging Activity Log** gespeichert. Verwenden Sie die Endpunkte Nachricht planen, um Nachrichten zu einem bestimmten Zeitpunkt zu versenden und bereits geplante Nachrichten zu ändern oder abzubrechen."

guide_featured_title: "Zeitplan für Nachrichten Endpunkte"
guide_featured_list:
  - name: "GET: Liste geplanter Kampagnen und Canvase"
    link: /docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Geplante Nachrichten löschen"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Geplante, API-getriggerte Kampagnen löschen"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Geplante, API-getriggerte Canvase löschen"
    link: /docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: "POST: Zeitplan Nachrichten"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/
    image: /assets/img/braze_icons/calendar-plus-01.svg
  - name: "POST: Zeitplan für API-getriggerte Kampagnen-Nachrichten"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Zeitplan für API-getriggerte Canvas Nachrichten"
    link: /docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: "POST: Geplante Nachrichten aktualisieren"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Aktualisieren Sie die Zeitpläne für API-getriggerte Kampagnen-Nachrichten"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/
    image: /assets/img/braze_icons/calendar-date.svg
  - name: "POST: Update von API-getriggerten Canvas Nachrichten nach Zeitplan"
    link: /docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/
    image: /assets/img/braze_icons/calendar-check-02.svg

guide_menu_title: "Send messages endpoints"
guide_menu_list:
  - name: "POST: Sende-IDs erstellen"
    link: /docs/api/endpoints/messaging/send_messages/post_create_send_ids/
    image: /assets/img/braze_icons/user-square.svg
  - name: "POST: Nachrichten sofort versenden"
    link: /docs/api/endpoints/messaging/send_messages/post_send_messages/
    image: /assets/img/braze_icons/send-01.svg
  - name: "POST: Sofortige Versendung von API-getriggerten Nachrichten für Kampagnen"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
    image: /assets/img/braze_icons/inbox-01.svg
  - name: "POST: Senden Sie API-getriggerte Canvas Nachrichten sofort"
    link: /docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/
    image: /assets/img/braze_icons/inbox-01.svg

guide_menu_title2: "Duplicate message endpoints"
guide_menu_list2:
  - name: "POST: Duplizierte Kampagnen"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_campaigns/
    image: /assets/img/braze_icons/copy-04.svg
  - name: "POST: Canvase duplizieren"
    link: /docs/api/endpoints/messaging/duplicate_messages/post_duplicate_canvases/
    image: /assets/img/braze_icons/copy-04.svg

guide_menu_title3: "Live Activity endpoints"
guide_menu_list3:
  - name: "POST: Live-Aktivität aktualisieren"
    link: /docs/api/endpoints/messaging/live_activity/update/
    image: /assets/img/braze_icons/tablet-01.svg
---
