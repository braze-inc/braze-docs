---
page_order: 0
nav_title: Home
article_title: Braze API-Leitfaden
layout: api_glossary
glossary_top_header: "Braze API Guide"
glossary_top_text: "Braze provides a high-performance REST API to allow you to track users, send messages, export data, and more. This page lists available Braze API endpoints and their uses."
page_type: glossary
description: "Diese Landing Page listet die verfügbaren Braze API Endpunkte und ihre Verwendung auf."
glossary_tag_name: Endpoint Type

glossary_filter_text: "Select endpoint type to narrow the glossary:"

glossary_mid_text: "Endpoint Search"
guide_featured_list:
  - name: API-Übersicht
    image: /assets/img/braze_icons/annotation-info.svg
    link: /docs/api/basics/
  - name: API Bezeichner Typen
    link: /docs/api/identifier_types/
    image: /assets/img/braze_icons/clipboard-check.svg
  - name: Objekte &amp; Filter
    link: /docs/api/objects_filters/
    image: /assets/img/braze_icons/settings-01.svg
  - name: Fehler &amp; Antworten
    link: /docs/api/errors/
    image: /assets/img/braze_icons/list.svg
  - name: Datenaufbewahrung
    link: /docs/api/data_retention/
    image: /assets/img/braze_icons/laptop-02.svg
  - name: Rate-Limits
    link: /docs/api/api_limits/
    image: /assets/img/braze_icons/hand.svg

# channel to icon/fa or image mapping
glossary_tags:
  - name: Kampagnen
  - name: Canvas
  - name: Kataloge
  - name: Content-Blöcke
  - name: Angepasste Events
  - name: E-Mail-Liste
  - name: E-Mail-Templates
  - name: KPI
  - name: Käufe
  - name: Präferenzzentrum
  - name: Zeitplan Nachrichten
  - name: SCIM
  - name: SDK-Authentifizierung
  - name: Segmente
  - name: Nachrichten senden
  - name: SMS
  - name: Abo-Gruppen
  - name: Nutzerdaten
  - name: Live Aktivität
  - name: Cloud-Datenaufnahme

glossaries:
  - name: "<a href='/docs/api/endpoints/user_data/post_user_alias/'>/benutzer/alias/new</a>"
    description: "Fügen Sie neue User-Alias für bestehende identifizierte Nutzer:innen hinzu oder erstellen Sie neue nicht identifizierte Nutzer:innen."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_alias_update/'>/benutzer/alias/update</a>"
    description: "Update der bestehenden Nutzer:innen-Alias-Namen auf neue Nutzer:innen-Alias-Namen."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_delete/'>/benutzer:innen/löschen</a>"
    description: "Löschen Sie ein beliebiges Nutzerprofil, indem Sie einen bekannten Bezeichner für Nutzer:innen angeben."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_global_control_group/'>/benutzer/export/global_control_group</a>"
    description: "Exportieren Sie alle Nutzer:innen in einer globalen Kontrollgruppe."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_identifier/'>/benutzer/export/ids</a>"
    description: "Exportieren Sie Daten aus einem beliebigen Nutzerprofil, indem Sie einen Bezeichner für den Nutzer:innen angeben."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_segment/'>/benutzer/export/segmente</a>"
    description: "Exportieren Sie alle Nutzer:innen eines Segments."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/'>/benutzer/external_ids/rename</a>"
    description: "Benennen Sie die externen IDs Ihrer Nutzer:innen um."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/'>/benutzer/external_ids/remove</a>"
    description: "Entfernen Sie die alten, veralteten externen IDs Ihrer Nutzer:innen."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_identify/'>/benutzer:innen/identify</a>"
    description: "Identifizieren Sie einen nicht identifizierten Nutzer:in (nur Alias)."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_track/'>/benutzer:innen/track</a>"
    description: "Erfassen Sie angepasste Events, Käufe und aktualisieren Sie die Attribute des Nutzerprofils."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_merge/'>/nutzer:innen/merge</a>"
    description: "Zusammenführen eines Nutzerprofils mit einem anderen Nutzer:in."
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/'>/kampagnen/triggern/senden</a>"
    description: "Senden Sie sofortige, einmalige Nachrichten an bestimmte Nutzer:innen durch eine API-getriggerte Zustellung. - Nachrichten senden"
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/'>/canvas/triggern/senden</a>"
    description: Senden Sie Canvas Nachrichten über eine API-getriggerte Zustellung. - Nachrichten senden
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_messages/'>/nachrichten/senden</a>"
    description: "Senden Sie sofortige, einmalige Nachrichten an bestimmte Nutzer:innen über die Braze API."
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids/'>/sends/id/create</a>"
    description: "Erstellen Sie Sende-IDs, mit denen Sie programmgesteuert Nachrichten versenden und die Performance der Nachrichten verfolgen können, ohne für jede Sendung eine Kampagne erstellen zu müssen."
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message/'>/transactional/v1/campagnen/{CAMPAIGN_ID}/send</a>"
    description: "Senden Sie sofortige, einmalige transaktionsbezogene Nachrichten an einen bestimmten Nutzer:innen."
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/'>/kampagnen/triggern/zeitplan/erstellen</a>"
    description: Senden Sie auf dem Dashboard erstellte Kampagnen-Nachrichten durch eine API-getriggerte Zustellung.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/'>/kampagnen/triggern/zeitplan/loeschen</a>"
    description: "Stornieren Sie API-getriggerte Kampagnen-Nachrichten, die Sie zuvor geplant haben, bevor sie gesendet wurden."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/'>/kampagnen/ausloesen/zeitplan/update</a>"
    description: "Aktualisieren Sie geplante, durch APIs getriggerte Kampagnen, die im Dashboard erstellt wurden."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/'>/canvas/triggern/zeitplan/loeschen</a>"
    description: "Stornieren Sie eine Canvas Nachricht, die Sie zuvor über API-getriggert geplant haben, bevor sie gesendet wurde."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/'>/canvas/trigger/zeitplan/erstellen</a>"
    description: Planen Sie Canvas Nachrichten durch eine API-getriggerte Zustellung.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/'>/nachrichten/zeitplan/update</a>"
    description: Aktualisieren Sie geplante Nachrichten. Dieser Endpunkt akzeptiert Updates entweder in der <code>schedule</code> oder <code>messages</code> Parameter oder beides.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/'>/nachrichten/zeitplan/loeschen</a>"
    description: "Stornieren Sie eine Nachricht, die Sie zuvor geplant haben, bevor sie gesendet wurde."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/'>/nachrichten/zeitplan/erstellen</a>"
    description: "Planen Sie eine Kampagne, ein Canvas oder eine andere Nachricht, die zu einem bestimmten Zeitpunkt gesendet werden soll."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/'>/canvas/triggern/zeitplan/update</a>"
    description: "Aktualisieren Sie geplante, durch APIs getriggerte Canvase, die im Dashboard erstellt wurden."
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/'>/nachrichten/geplante_ausstrahlungen</a>"
    description: Gibt eine JSON-Liste mit Informationen über geplante Kampagnen und Eingänge Canvase zwischen jetzt und einem bestimmten Zeitpunkt zurück. <code>end_time</code> in der Anfrage angegeben.
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/live_activity/update/'>/messages/live_activity/update</a>"
    description: Aktualisieren Sie eine iOS Live-Aktivität.
    tags:
      - Live Activity
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/'>/abo/status/set</a>"
    description: "Batch-Update des Abo-Status von bis zu 50 Nutzer:innen auf dem Braze-Dashboard."
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/'>/v2/abo/status/set</a>"
    description: "Batch-Update des Abo-Status von bis zu 50 Nutzer:innen auf dem Braze-Dashboard."
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status/'>/abo/status/get</a>"
    description: "Holen Sie sich den Abo-Status eines Nutzers:innen in einer Abo-Gruppe."
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups/'>/abonnement/benutzer/status</a>"
    description: "Auflisten und Abrufen der Abo-Gruppen eines bestimmten Nutzer:innen."
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/email/post_blacklist/'>/email/blacklist</a>"
    description: "Nutzer:innen von E-Mails abmelden und als \"hard bounced\" markieren."
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_hard_bounces/'>/email/bounce/remove</a>"
    description: Entfernen Sie E-Mail-Adressen aus Ihrer Braze Bounce-Liste.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_spam/'>/email/spam/remove</a>"
    description: Entfernen Sie E-Mail-Adressen aus Ihrer Braze Spam-Liste.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_email_subscription_status/'>/email/status</a>"
    description: "Legen Sie den Status des E-Mail-Abos für Ihre Nutzer:innen fest."
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_create_email_template/'>/templates/email/create</a>"
    description: Erstellen Sie E-Mail-Templates auf dem Braze-Dashboard.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_update_email_template/'>/templates/email/update</a>"
    description: Update der E-Mail Templates auf dem Braze-Dashboard.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/email/get_list_hard_bounces/'>/email/hard_bounces</a>"
    description: "Erstellen Sie eine Liste der E-Mail-Adressen, die Ihre Nachrichten innerhalb eines bestimmten Zeitrahmens \"gebounct\" haben."
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses/'>/email/abgemeldet</a>"
    description: "E-Mails zurücksenden, die während des Zeitraums von abgemeldet wurden <code>start_date</code> an <code>end_date</code>."
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information/'>/templates/email/info</a>"
    description: Informieren Sie sich über Ihre E-Mail Templates.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates/'>/templates/email/list</a>"
    description: Erhalten Sie eine Liste der verfügbaren E-Mail Templates in Ihrem Braze-Konto.
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics/'>/kampagnen/daten_serie</a>"
    description: Rufen Sie eine tägliche Reihe verschiedener Statistiken für eine Kampagne im Laufe der Zeit ab.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_details/'>/kampagnen/details</a>"
    description: Rufen Sie relevante Informationen zu einer bestimmten Kampagne ab.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaigns/'>/kampagnen/liste</a>"
    description: "Exportieren Sie eine Liste von Kampagnen, die jeweils den Namen, den API-Bezeichner der Kampagne, die Angabe, ob es sich um eine API-Kampagne handelt, und die mit der Kampagne verbundenen Tags enthält."
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_send_analytics/'>/sends/data_series</a>"
    description: Ruft eine tägliche Reihe verschiedener Statistiken für ein Tracking ab <code>send_id</code>.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics/'>/canvas/data_series</a>"
    description: Exportieren Sie Zeitreihendaten für ein Canvas.
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary/'>/canvas/daten_zusammenfassung</a>"
    description: "Exportieren Sie Rollups von Zeitreihendaten für ein Canvas, um eine übersichtliche Zusammenfassung der Ergebnisse eines Canvas zu erhalten."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_details/'>/canvas/details</a>"
    description: "Exportieren Sie Metadaten zu einem Canvas, z. B. den Namen, den Zeitpunkt der Erstellung, den aktuellen Status und mehr."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvases/'>/canvas/liste</a>"
    description: "Exportieren Sie eine Liste von Canvase, einschließlich des Namens, des Canvas API Bezeichners und der zugehörigen Tags."
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_analytics/'>/segmente/data_series</a>"
    description: Rufen Sie eine tägliche Serie der geschätzten Größe eines Segments im Laufe der Zeit ab.
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_details/'>/segmente/details</a>"
    description: Rufen Sie relevante Informationen über ein Segment ab.
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment/'>/segmente/liste</a>"
    description: "Exportieren Sie eine Liste von Segmenten, die jeweils den Namen, den Bezeichner der Segment API und die Angabe, ob das Analytics Tracking aktiviert ist, enthalten."
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/sessions/get_sessions_analytics/'>/sessions/data_series</a>"
    description: Rufen Sie eine Reihe von Sitzungen für Ihre App über einen bestimmten Zeitraum ab.
    tags:
      - Sessions
  - name: "<a href='/docs/api/endpoints/export/custom_attributes/get_custom_attributes/'>/custom_attributes</a>"
    description: "Exportieren Sie eine Liste angepasster Attribute, einschließlich Name, Beschreibung, Datentyp, Array-Länge (falls zutreffend), Status und zugehörige Tags."
    tags:
      - Custom Attributes
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics/'>/ereignisse/daten_serien</a>"
    description: Rufen Sie eine Reihe der Vorkommen eines angepassten Events in Ihrer App über einen bestimmten Zeitraum ab.
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_data/'>/Ereignisse</a>"
    description: "Exportieren Sie eine Liste angepasster Events mit Name, Beschreibung, Status, zugehörigen Tags und Einbeziehung in Analytics-Berichte."
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events/'>/ereignisse/liste</a>"
    description: "Exportieren Sie eine Liste mit den Namen der angepassten Events, die für Ihre App aufgezeichnet wurden."
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/'>/inhalt_blöcke/erstellen</a>"
    description: Erstellen Sie einen E-Mail Content-Block.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block/'>/content_blocks/update</a>"
    description: Aktualisieren Sie einen E-Mail Content-Block.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/'>/inhalt_blöcke/info</a>"
    description: Rufen Sie Informationen für Ihren bestehenden E-Mail Content-Block auf.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/'>/inhalt_blöcke/liste</a>"
    description: Listen Sie die Informationen Ihrer bestehenden Content-Blöcke auf.
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date/'>/kpi/dau/data_series</a>"
    description: "Rufen Sie eine tägliche Reihe der Gesamtzahl eindeutiger aktiver Nutzer:innen zu jedem Datum ab."
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days/'>/kpi/mau/data_series</a>"
    description: "Rufen Sie eine tägliche Reihe der Gesamtzahl eindeutiger aktiver Nutzer:innen über ein rollierendes 30-Tage-Fenster ab."
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/'>/kpi/new_users/data_series</a>"
    description: "Rufen Sie eine tägliche Reihe der Gesamtzahl der neuen Nutzer:innen an jedem Datum ab."
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/'>/kpi/uninstalls/data_series</a>"
    description: Rufen Sie eine tägliche Reihe der Gesamtzahl der Deinstallationen an jedem Datum ab.
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/sms/post_remove_invalid_numbers/'>/sms/invalid_phone_numbers/remove</a>"
    description: "Entfernen Sie \"ungültige\" Telefonnummern aus der Liste der ungültigen Nummern in Braze. Damit können Sie Telefonnummern erneut validieren, nachdem sie als ungültig markiert wurden."
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/sms/get_query_invalid_numbers/'>/sms/invalid_phone_numbers</a>"
    description: "Erstellen Sie eine Liste der Telefonnummern, die innerhalb eines bestimmten Zeitraums als \"ungültig\" eingestuft wurden."
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/export/purchases/get_list_product_id/'>/Einkäufe/Produkt_liste</a>"
    description: Gibt eine paginierte Liste von Produkt IDs zurück.
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_number_of_purchases/'>/Einkäufe/Menge_series</a>"
    description: Gibt die Gesamtzahl der Käufe in Ihrer App über einen bestimmten Zeitraum zurück.
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_revenue_series/'>/Einkäufe/Einnahmen_serien</a>"
    description: "Geben Sie den Gesamtbetrag zurück, der in Ihrer App über einen bestimmten Zeitraum ausgegeben wurde."
    tags:
      - Purchases    
  - name: "<a href='/docs/api/endpoints/preference_center/get_create_url_preference_center'>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</a>"
    description: Erstellen Sie eine URL für ein Einstellungscenter.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_list_preference_center/'>/präferenz_zentrum/v1/liste</a>"
    description: Liste der verfügbaren Präferenzzentren.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_view_details_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>"
    description: "Sehen Sie sich die Details zu Ihren Präferenzzentren an, einschließlich des Zeitpunkts, zu dem sie erstellt und aktualisiert wurden."
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/post_create_preference_center'>/präferenz_zentrum/v1</a>"
    description: "Erstellen Sie ein Einstellungscenter, mit dem Nutzer:innen ihre Benachrichtigungspräferenzen für E-Mail Kampagnen verwalten können."
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/put_update_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>"
    description: Aktualisieren Sie ein Einstellungszentrum.
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk'>/catalogs/{catalog_name}/artikel</a>"
    description: Löschen Sie mehrere Artikel in Ihrem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Einen Artikel und seine Details auflisten.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/'>/catalogs/{catalog_name}/artikel</a>"
    description: Bearbeiten Sie mehrere Artikel in Ihrem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/'>/catalogs/{catalog_name}/artikel</a>"
    description: Erstellen Sie mehrere Artikel in Ihrem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/'>/Kataloge/{Katalog_name}</a>"
    description: Löschen Sie einen Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/'>/Kataloge</a>"
    description: Erstellen Sie einen Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/'>/Kataloge</a>"
    description: Liste der Kataloge in einem Workspace.
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
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/'>/catalogs/{catalog_name}/artikel</a>"
    description: Gibt mehrere Artikel und deren Inhalt zurück.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Einen Artikel in einem Katalog löschen.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: Ersetzen Sie einen Artikel in einem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/'>/catalogs/{catalog_name}/artikel/</a>"
    description: Ersetzen Sie mehrere Artikel in einem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields/'>/kataloge/{Katalogname}/Felder/</a>"
    description: Erstellen Sie mehrere Felder in einem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field/'>/catalogs/{catalog_name}/felder/{feld_name}</a>"
    description: Löschen Sie ein Feld aus einem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections/'>/catalogs/{catalog_name}/auswahlen</a>"
    description: Erstellen Sie eine Auswahl in einem Katalog.
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection/'>/catalogs/{catalog_name}/auswahlen/{auswahl_name}</a>"
    description: Löschen Sie eine Katalogauswahl.
    tags:
      - Catalogs
  - name: "<a href='/docs/post_create_user_account/'>/scim/v2/Benutzer:innen</a>"
    description: "Erstellen Sie ein neues Nutzer:innen-Konto für das Dashboard, indem Sie E-Mail, Vor- und Nachnamen sowie Berechtigungen (für die Festlegung von Berechtigungen auf Unternehmens-, Workspace- und Teamebene) angeben."
    tags:
      - SCIM
  - name: "<a href='/docs/get_see_user_account_information/'>/scim/v2/Benutzer:innen/{id}</a>"
    description: "Suchen Sie ein bestehendes Dashboard-Nutzer:innen-Konto, indem Sie die ID der Ressource angeben."
    tags:
      - SCIM
  - name: "<a href='/docs/post_update_existing_user_account/'>/scim/v2/Benutzer:innen/{id}</a>"
    description: "Aktualisieren Sie ein bestehendes Nutzer:innen-Konto für das Dashboard, indem Sie E-Mail, Vor- und Nachnamen sowie Berechtigungen angeben (zum Festlegen von Berechtigungen auf Unternehmens-, Workspace- und Teamebene)."
    tags:
      - SCIM
  - name: "<a href='/docs/delete_existing_dashboard_user/'>/scim/v2/Benutzer:innen/{id}</a>"
    description: "Einen bestehenden Nutzer:innen des Dashboards dauerhaft löschen."
    tags:
      - SCIM
  - name: "<a href='/docs/get_search_existing_dashboard_user_email/'>/scim/v2/Benutzer:innen?filter={userName@example.com}</a>"
    description: "Suchen Sie ein bestehendes Dashboard Nutzer:innen-Konto, indem Sie dessen E-Mail angeben."
    tags:
      - SCIM
  - name: "<a href='/docs/api/endpoints/cdi/get_integration_list/'>/cdi/integrationen</a>"
    description: Gibt eine Liste der vorhandenen Integrationen zurück.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/post_job_sync/'>/cdi/integrationen/{integration_id}/sync</a>"
    description: Triggern Sie eine Synchronisierung für eine bestimmte Integration.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/get_job_sync_status/'>/cdi/integrationen/{integration_id}/job_sync_status</a>"
    description: Gibt eine Liste der Sync-Status zurück.
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/'>/app_group/sdk_authentication/create</a>"
    description: Erstellen Sie einen neuen SDK-Authentifizierungsschlüssel für Ihre App.
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/get_sdk_authentication_keys/'>/app_group/sdk_authentication/keys</a>"
    description: SDK-Authentifizierungsschlüssel für Ihre App auflisten.
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/'>/app_group/sdk_authentication/primär</a>"
    description: Legen Sie einen SDK-Authentifizierungsschlüssel als Primärschlüssel für Ihre App fest.
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key/'>/app_group/sdk_authentication/delete</a>"
    description: Löschen Sie einen SDK-Authentifizierungsschlüssel für Ihre App.
    tags:
      - SDK Authentication  
---