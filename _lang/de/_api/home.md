---
page_order: 0
nav_title: Startseite
article_title: Braze API-Leitfaden
layout: api_glossary
glossary_top_header: "Braze API Guide"
glossary_top_text: "Braze provides a high-performance REST API to allow you to track users, send messages, export data, and more. This page lists available Braze API endpoints and their uses."
page_type: glossary
description: "Diese Landing Page listet die verfügbaren Braze-API-Endpunkte und ihre Verwendung auf."
glossary_tag_name: Endpoint Type

glossary_filter_text: "Select endpoint type to narrow the glossary:"

glossary_mid_text: "Endpoint Search"
guide_featured_list:
  - name: API-Übersicht
    image: /assets/img/braze_icons/annotation-info.svg
    link: /docs/api/basics/
  - name: API-Bezeichner-Typen
    link: /docs/api/identifier_types/
    image: /assets/img/braze_icons/clipboard-check.svg
  - name: Objekte &amp; Filter
    link: /docs/api/objects_filters/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Fehler &amp; Antworten
    link: /docs/api/errors/
    image: /assets/img/braze_icons/list.svg
  - name: Aufbewahrung von Daten
    link: /docs/api/data_retention/
    image: /assets/img/braze_icons/laptop-02.svg
  - name: Raten-Grenzwerte
    link: /docs/api/api_limits/
    image: /assets/img/braze_icons/hand.svg

# channel to icon/fa or image mapping
glossary_tags:
  - name: Kampagnen
  - name: Segeltuch
  - name: Kataloge
  - name: Inhalt Blöcke
  - name: Benutzerdefinierte Ereignisse
  - name: E-Mail-Liste
  - name: E-Mail-Vorlagen
  - name: KPI
  - name: News Feed
  - name: Käufe
  - name: Präferenz-Center
  - name: Zeitplan-Nachrichten
  - name: SCIM
  - name: Segmente
  - name: Nachrichten senden
  - name: SMS
  - name: Abonnement-Gruppen
  - name: Benutzerdaten
  - name: Live Aktivität
  - name: Ingestion von Cloud-Daten

glossaries:
  - name: "<a href='/docs/api/endpoints/user_data/post_user_alias/'>/users/alias/new</a>"
    description: Fügen Sie neue Benutzer-Aliase für bestehende identifizierte Benutzer hinzu oder erstellen Sie neue nicht identifizierte Benutzer.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_alias_update/'>/users/alias/update</a>"
    description: Aktualisieren Sie bestehende Benutzer-Aliasnamen zu neuen Benutzer-Aliasnamen.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_delete/'>/users/delete</a>"
    description: "Löschen Sie ein beliebiges Benutzerprofil, indem Sie einen bekannten Benutzeridentifikator angeben."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_global_control_group/'>/users/export/global_control_group</a>"
    description: Exportieren Sie alle Benutzer innerhalb einer Globalen Kontrollgruppe.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_identifier/'>/users/export/ids</a>"
    description: "Exportieren Sie Daten aus einem beliebigen Benutzerprofil, indem Sie eine Benutzerkennung angeben."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_segment/'>/users/export/segment</a>"
    description: Exportieren Sie alle Benutzer innerhalb eines Segments.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/'>/users/external_ids/rename</a>"
    description: Benennen Sie die externen IDs Ihrer Benutzer um.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/'>/users/external_ids/remove</a>"
    description: "Entfernen Sie die alten, veralteten externen IDs Ihrer Benutzer."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_identify/'>/users/identify</a>"
    description: Identifizieren Sie einen nicht identifizierten Benutzer (nur Alias).
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_track/'>/users/track</a>"
    description: "Erfassen Sie benutzerdefinierte Ereignisse, Einkäufe und aktualisieren Sie die Attribute des Benutzerprofils."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_merge/'>/users/merge</a>"
    description: Ein Benutzerprofil mit einem anderen Benutzer zusammenführen.
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/'>/campaigns/trigger/send</a>"
    description: "Senden Sie sofortige, einmalige Nachrichten an bestimmte Benutzer über eine API-ausgelöste Zustellung. - Nachrichten senden"
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/'>/canvas/trigger/send</a>"
    description: Senden Sie Canvas-Nachrichten über API-gesteuerte Zustellung. - Nachrichten senden
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_messages/'>/nachrichten/senden</a>"
    description: "Senden Sie sofortige, einmalige Nachrichten an bestimmte Benutzer über die Braze API."
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids/'>/sends/id/create</a>"
    description: "Erstellen Sie Sende-IDs, die zum programmgesteuerten Senden von Nachrichten und zur Verfolgung der Nachrichtenleistung verwendet werden können, ohne dass für jede Sendung eine Kampagne erstellt werden muss."
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message/'>/transactional/v1/campaigns/{CAMPAIGN_ID}/send</a>"
    description: "Senden Sie sofortige, einmalige Transaktionsnachrichten an einen bestimmten Benutzer."
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/'>/campaigns/trigger/schedule/create</a>"
    description: Senden Sie vom Dashboard erstellte Kampagnennachrichten über eine API-gesteuerte Zustellung.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/'>/campaigns/trigger/schedule/delete</a>"
    description: "Stornieren Sie API-ausgelöste Kampagnennachrichten, die Sie zuvor geplant haben, bevor sie gesendet wurden."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/'>/campaigns/trigger/schedule/update</a>"
    description: "Aktualisieren Sie geplante API-ausgelöste Kampagnen, die im Dashboard erstellt wurden."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/'>/canvas/trigger/schedule/delete</a>"
    description: "Stornieren Sie eine Canvas-Nachricht, die Sie zuvor über API-ausgelöst geplant haben, bevor sie gesendet wurde."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/'>/canvas/trigger/schedule/create</a>"
    description: Planen Sie Canvas-Nachrichten durch eine API-gesteuerte Zustellung.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/'>/messages/schedule/update</a>"
    description: Aktualisieren Sie geplante Nachrichten. Dieser Endpunkt akzeptiert Aktualisierungen entweder der <code>schedule</code> oder <code>messages</code> Parameter oder beides.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/'>/messages/schedule/delete</a>"
    description: "Stornieren Sie eine Nachricht, die Sie zuvor geplant haben, bevor sie gesendet wurde."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/'>/messages/schedule/create</a>"
    description: "Planen Sie eine Kampagne, ein Canvas oder eine andere Nachricht, die zu einem bestimmten Zeitpunkt gesendet werden soll."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/'>/canvas/trigger/schedule/update</a>"
    description: "Aktualisieren Sie geplante API-ausgelöste Canvases, die im Dashboard erstellt wurden."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/'>/messages/scheduled_broadcasts</a>"
    description: Liefert eine JSON-Liste mit Informationen über geplante Kampagnen und Eintragsfenster zwischen jetzt und einem bestimmten Zeitpunkt. <code>end_time</code> in der Anfrage angegeben.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/live_activity/update/'>/messages/live_activity/update</a>"
    description: Aktualisieren Sie eine iOS Live-Aktivität.
    tags:
      - Live Activity
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/'>/subscription/status/set</a>"
    description: Aktualisieren Sie den Abonnementstatus von bis zu 50 Benutzern auf dem Braze-Dashboard im Stapel.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/'>/v2/subscription/status/set</a>"
    description: Aktualisieren Sie den Abonnementstatus von bis zu 50 Benutzern auf dem Braze-Dashboard im Stapel.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status/'>/subscription/status/get</a>"
    description: Ermittelt den Abonnementstatus eines Benutzers in einer Abonnementgruppe.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups/'>/subscription/user/status</a>"
    description: Auflisten und Abrufen der Abonnementgruppen eines bestimmten Benutzers.
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/email/post_blacklist/'>/email/blacklist</a>"
    description: "Melden Sie einen Benutzer von der E-Mail ab und markieren Sie ihn als \"hart gebounced\"."
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_hard_bounces/'>/email/bounce/remove</a>"
    description: Entfernen Sie E-Mail-Adressen aus Ihrer Braze Bounce-Liste.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_spam/'>/email/spam/remove</a>"
    description: Entfernen Sie E-Mail-Adressen aus Ihrer Braze-Spamliste.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_email_subscription_status/'>/email/status</a>"
    description: Legen Sie den E-Mail-Abonnementstatus für Ihre Benutzer fest.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_create_email_template/'>/templates/email/create</a>"
    description: Erstellen Sie E-Mail-Vorlagen auf dem Braze Dashboard.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_update_email_template/'>/templates/email/update</a>"
    description: Aktualisieren Sie E-Mail-Vorlagen auf dem Braze-Dashboard.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/email/get_list_hard_bounces/'>/email/hard_bounces</a>"
    description: "Erstellen Sie eine Liste der E-Mail-Adressen, die Ihre E-Mail-Nachrichten innerhalb eines bestimmten Zeitraums \"hart gebounced\" haben."
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses/'>/email/unsubscribes</a>"
    description: "Rücksendung von E-Mails, die während des Zeitraums von <code>start_date</code> zu <code>end_date</code>."
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information/'>/templates/email/info</a>"
    description: Informieren Sie sich über Ihre E-Mail-Vorlagen.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates/'>/templates/email/list</a>"
    description: Erhalten Sie eine Liste der verfügbaren E-Mail-Vorlagen in Ihrem Braze-Konto.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics/'>/campaigns/data_series</a>"
    description: Rufen Sie eine tägliche Serie von verschiedenen Statistiken für eine Kampagne im Laufe der Zeit ab.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_details/'>/campaigns/details</a>"
    description: Rufen Sie relevante Informationen zu einer bestimmten Kampagne ab.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaigns/'>/campaigns/list</a>"
    description: "Exportieren Sie eine Liste von Kampagnen, die jeweils den Namen, die API-Kennung der Kampagne, die Angabe, ob es sich um eine API-Kampagne handelt, und die mit der Kampagne verbundenen Tags enthält."
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_send_analytics/'>/sends/data_series</a>"
    description: Rufen Sie eine tägliche Serie verschiedener Statistiken für ein verfolgtes <code>send_id</code>.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics/'>/canvas/data_series</a>"
    description: Exportieren Sie Zeitreihendaten für ein Canvas.
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary/'>/canvas/data_summary</a>"
    description: "Exportieren Sie Rollups von Zeitreihendaten für ein Canvas, um eine übersichtliche Zusammenfassung der Ergebnisse eines Canvas zu erhalten."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_details/'>/canvas/details</a>"
    description: "Exportieren Sie Metadaten zu einem Canvas, z. B. den Namen, den Zeitpunkt der Erstellung, den aktuellen Status und mehr."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvases/'>/canvas/list</a>"
    description: "Exportieren Sie eine Liste von Canvases, einschließlich des Namens, der Canvas-API-Kennung und der zugehörigen Tags."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_analytics/'>/segments/data_series</a>"
    description: Rufen Sie eine tägliche Serie der geschätzten Größe eines Segments im Laufe der Zeit ab.
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_details/'>/segments/details</a>"
    description: Rufen Sie relevante Informationen über ein Segment ab.
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment/'>/segments/list</a>"
    description: "Exportieren Sie eine Liste von Segmenten, die jeweils den Namen, die Segment-API-Kennung und die Angabe enthalten, ob das analytische Tracking aktiviert ist."
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/sessions/get_sessions_analytics/'>/sessions/data_series</a>"
    description: Rufen Sie eine Reihe der Anzahl der Sitzungen für Ihre App über einen bestimmten Zeitraum ab.
    tags:
      - Sessions
  - name: "<a href='/docs/api/endpoints/export/custom_attributes/get_custom_attributes/'>/custom_attributes</a>"
    description: "Exportieren Sie eine Liste der benutzerdefinierten Attribute, einschließlich Name, Beschreibung, Datentyp, Array-Länge (falls zutreffend), Status und zugehörige Tags."
    tags:
      - Custom Attributes
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics/'>/events/data_series</a>"
    description: "Rufen Sie eine Reihe von Ereignissen in Ihrer App ab, die in einem bestimmten Zeitraum aufgetreten sind."
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_data/'>/events</a>"
    description: "Exportieren Sie eine Liste von benutzerdefinierten Ereignissen, einschließlich Name, Beschreibung, Status, zugehörige Tags und Einbeziehung in den Analysebericht."
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events/'>/events/list</a>"
    description: "Exportieren Sie eine Liste mit den Namen der benutzerdefinierten Ereignisse, die für Ihre App aufgezeichnet wurden."
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/'>/content_blocks/create</a>"
    description: Erstellen Sie einen E-Mail-Inhaltsblock.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block/'>/content_blocks/update</a>"
    description: Aktualisieren Sie einen E-Mail-Inhaltsblock.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/'>/content_blocks/info</a>"
    description: Rufen Sie Informationen für Ihren bestehenden E-Mail-Inhaltsblock auf.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/'>/content_blocks/list</a>"
    description: Listen Sie Ihre vorhandenen Content Blocks Informationen auf.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date/'>/kpi/dau/data_series</a>"
    description: Rufen Sie eine tägliche Reihe mit der Gesamtzahl der eindeutigen aktiven Benutzer an jedem Datum ab.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days/'>/kpi/mau/data_series</a>"
    description: Rufen Sie eine tägliche Reihe der Gesamtzahl eindeutiger aktiver Benutzer über ein rollendes 30-Tage-Fenster ab.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/'>/kpi/new_users/data_series</a>"
    description: Rufen Sie eine tägliche Reihe mit der Gesamtzahl der neuen Benutzer an jedem Datum ab.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/'>/kpi/uninstalls/data_series</a>"
    description: Rufen Sie eine tägliche Reihe der Gesamtzahl der Deinstallationen an jedem Datum ab.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/news_feed/get_news_feed_card_analytics/'>/feed/data_series</a>"
    description: Rufen Sie eine tägliche Serie von Engagement-Statistiken für eine Karte im Laufe der Zeit ab.
    tags:
      - News Feed
  - name: "<a href='/docs/api/endpoints/export/news_feed/get_news_feed_card_details/'>/feed/details</a>"
    description: Rufen Sie die relevanten Informationen auf einer Karte ab.
    tags:
      - News Feed
  - name: "<a href='/docs/api/endpoints/export/news_feed/get_news_feed_cards/'>/feed/list</a>"
    description: "Exportieren Sie eine Liste von News Feed-Karten, die jeweils den Namen und die API-Kennung der Karte enthalten."
    tags:
      - News Feed
  - name: "<a href='/docs/api/endpoints/sms/post_remove_invalid_numbers/'>/sms/invalid_phone_numbers/remove</a>"
    description: "Entfernen Sie \"ungültige\" Telefonnummern aus der Ungültigkeitsliste in Braze. Damit können Sie Telefonnummern erneut validieren, nachdem sie als ungültig markiert wurden."
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/sms/get_query_invalid_numbers/'>/sms/invalid_phone_numbers</a>"
    description: "Erstellen Sie eine Liste der Telefonnummern, die innerhalb eines bestimmten Zeitraums als \"ungültig\" eingestuft wurden."
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/export/purchases/get_list_product_id/'>/purchases/product_list</a>"
    description: Gibt eine paginierte Liste von Produkt-IDs zurück.
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_number_of_purchases/'>/purchases/quantity_series</a>"
    description: Gibt die Gesamtzahl der Käufe in Ihrer App über einen bestimmten Zeitraum zurück.
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_revenue_series/'>/purchases/revenue_series</a>"
    description: Geben Sie den Gesamtbetrag der Ausgaben in Ihrer App über einen bestimmten Zeitraum zurück.
    tags:
      - Purchases    
  - name: "<a href='/docs/api/endpoints/preference_center/get_create_url_preference_center'>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</a>"
    description: Erstellen Sie eine URL für ein Einstellungscenter.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_list_preference_center/'>/preference_center/v1/list</a>"
    description: Liste der verfügbaren Präferenzzentren.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_view_details_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>"
    description: "Sehen Sie sich die Details zu Ihren Präferenzzentren an, einschließlich des Zeitpunkts, zu dem sie erstellt und aktualisiert wurden."
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/post_create_preference_center'>/preference_center/v1</a>"
    description: "Erstellen Sie ein Einstellungszentrum, in dem Benutzer ihre Benachrichtigungspräferenzen für E-Mail-Kampagnen verwalten können."
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/put_update_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>"
    description: Aktualisieren Sie ein Präferenzzentrum.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>"
    description: Löschen Sie mehrere Artikel in Ihrem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Listen Sie einen Katalogartikel und seine Details auf.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: Bearbeiten Sie mehrere Artikel in Ihrem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: Erstellen Sie mehrere Artikel in Ihrem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/'>/catalogs/{catalog_name}</a>"
    description: Löschen Sie einen Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/'>/catalogs</a>"
    description: Erstellen Sie einen Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/'>/catalogs</a>"
    description: Listen Sie die Kataloge in einem Arbeitsbereich auf.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Erstellen Sie einen Artikel in einem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Einen Artikel in einem Katalog bearbeiten.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: Gibt mehrere Katalogartikel und deren Inhalt zurück.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Einen Artikel in einem Katalog löschen.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Aktualisieren Sie einen Artikel in einem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/'>/catalogs/{catalog_name}/items/</a>"
    description: Aktualisieren Sie mehrere Artikel in einem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields/'>/catalogs/{catalog_name}/fields/</a>"
    description: Erstellen Sie mehrere Felder in einem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field/'>/catalogs/{catalog_name}/fields/{field_name}</a>"
    description: Löschen Sie ein Feld aus einem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections/'>/catalogs/{catalog_name}/selections</a>"
    description: Erstellen Sie eine Auswahl in einem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection/'>/catalogs/{catalog_name}/selections/{selection_name}</a>"
    description: Eine Katalogauswahl löschen.
    tags:
      - Catalogs
  - name: "<a href='/docs/post_create_user_account/'>/scim/v2/Users</a>"
    description: "Erstellen Sie ein neues Dashboard-Benutzerkonto, indem Sie E-Mail, Vor- und Nachnamen sowie Berechtigungen (zum Festlegen von Berechtigungen auf Unternehmens-, Arbeitsbereichs- und Teamebene) angeben."
    tags:
      - SCIM
  - name: "<a href='/docs/get_see_user_account_information/'>/scim/v2/Users/{id}</a>"
    description: "Suchen Sie ein bestehendes Dashboard-Benutzerkonto, indem Sie dessen E-Mail angeben."
    tags:
      - SCIM
  - name: "<a href='/docs/post_update_existing_user_account/'>/scim/v2/Users/{id}</a>"
    description: "Aktualisieren Sie ein bestehendes Dashboard-Benutzerkonto, indem Sie E-Mail, Vor- und Nachnamen sowie Berechtigungen (zum Festlegen von Berechtigungen auf Unternehmens-, Arbeitsbereichs- und Teamebene) angeben."
    tags:
      - SCIM
  - name: "<a href='/docs/delete_existing_dashboard_user/'>/scim/v2/Users/{id}</a>"
    description: Einen bestehenden Dashboard-Benutzer dauerhaft löschen.
    tags:
      - SCIM
  - name: "<a href='/docs/get_search_existing_dashboard_user_email/'>/scim/v2/Users?filter={userName@example.com}</a>"
    description: "Suchen Sie ein bestehendes Dashboard-Benutzerkonto, indem Sie dessen E-Mail angeben."
    tags:
      - SCIM
  - name: "<a href='/docs/api/endpoints/cdi/get_integration_list/'>/cdi/integrations</a>"
    description: Gibt eine Liste der vorhandenen Integrationen zurück.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/post_job_sync/'>/cdi/integrations/{integration_id}/sync</a>"
    description: Lösen Sie eine Synchronisierung für eine bestimmte Integration aus.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/get_job_sync_status/'>/cdi/integrations/{integration_id}/job_sync_status</a>"
    description: Gibt eine Liste der Sync-Status zurück.
    tags:
      - Cloud Data Ingestion
---