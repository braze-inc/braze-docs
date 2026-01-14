---
nav_title: Segmente
article_title: Segmente
page_order: 1
layout: dev_guide
guide_top_header: "Segmente"
guide_top_text: "Zielgruppensegmentierung ist der Schlüssel zu strategischem Marketing - sie kann Sie davor bewahren, zu viele Zielgruppen anzusprechen, sie zu belästigen oder eine potenzielle Verbindung zu einem Kunden zu verpassen. Lesen Sie die folgenden Artikel, um zu erfahren, wie Sie Ihr Publikum segmentieren und filtern können - zu Ihrem (und dessen) größten Nutzen."
descriptions: "Zielgruppensegmentierung ist der Schlüssel zu strategischem Marketing - sie kann Sie davor bewahren, zu viele Zielgruppen anzusprechen, sie zu belästigen oder eine potenzielle Verbindung zu einem Kunden zu verpassen. Sehen Sie sich diese Landing-Page an, um zu erfahren, wie Sie Ihre Zielgruppe segmentieren und filtern können, um den größten Nutzen für Sie (und Ihre Zielgruppe) zu erzielen."
search_rank: 4
tool: Segments
page_type: landing
description: "Diese Landing Page enthält Artikel zum Thema Segmentierung in Dashboard-Kampagnen. Hier finden Sie Informationen darüber, wie Sie ein Segment, Filter, Funnels, Insights, Erweiterungen und mehr einrichten können."

guide_featured_title: "Beliebte Artikel"
guide_featured_list:
  - name: Ein Segment erstellen
    link: /docs/user_guide/engagement_tools/segments/creating_a_segment/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Segmente verwalten
    link: /docs/user_guide/engagement_tools/segments/managing_segments/
    image: /assets/img/braze_icons/edit-05.svg
  - name: Filter für die Segmentierung
    link: /docs/user_guide/engagement_tools/segments/segmentation_filters/
    image: /assets/img/braze_icons/flag-02.svg
  - name: Segmentdaten
    link: /docs/viewing_and_understanding_segment_data/
    image: /assets/img/braze_icons/pie-chart-01.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: Segment-Insights
    link: /docs/user_guide/engagement_tools/segments/segment_insights/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Segment Erweiterung
    link: /docs/user_guide/engagement_tools/segments/segment_extension/
    image: /assets/img/braze_icons/users-01.svg
  - name: SQL-Segmente
    link: /docs/sql_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: Katalog-Segmente
    link: /docs/catalog_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: Benutzerprofile
    link: /docs/user_guide/engagement_tools/segments/user_profiles/
    image: /assets/img/braze_icons/users-01.svg
  - name: Standort-Targeting
    link: /docs/user_guide/engagement_tools/segments/location_targeting/
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: Reguläre Ausdrücke
    link: /docs/user_guide/engagement_tools/segments/regex/
    image: /assets/img/braze_icons/search-sm.svg
  - name: Unterdrückungslisten
    link: /docs/user_guide/engagement_tools/segments/suppression_lists/
    image: /assets/img/braze_icons/list.svg 
  - name: Messung der Segmentgröße
    link: /docs/user_guide/engagement_tools/segments/measuring_segment_size/
    image: /assets/img/braze_icons/pie-chart-02.svg
  - name: Fehlersuche
    link: /docs/user_guide/engagement_tools/segments/troubleshooting/
    image: /assets/img/braze_icons/annotation-question.svg

guide_menu_title2: "Other"
guide_menu_list2:
  - name: Angepasste Attribute
    link: /docs/user_guide/data/custom_data/custom_attributes/
    image: /assets/img/braze_icons/table.svg

---

## Über Braze Segmente

In Braze sind Segmente dynamische Gruppen von Benutzern, die bestimmte von Ihnen definierte Kriterien erfüllen, wie Benutzerattribute, Benutzerverhalten und benutzerdefinierte Ereignisse. Sie können die Kriterien detailliert festlegen, indem Sie Segmente innerhalb anderer Segmente verschachteln und zusätzliche Funktionen anwenden. So können Sie die Reichweite Ihrer Zielgruppe eingrenzen und hochgradig personalisierte und ansprechende Inhalte an die richtigen Nutzer senden.

Sie können beliebig viele Segmente erstellen, um Zielgruppen zusammenstellen. Erforschen Sie verschiedene Kombinationen von Segmentfunktionen und Segmentierungsfiltern, um kreative Wege zur Nutzung Ihrer Benutzerdaten zu entdecken und neue Möglichkeiten zu erschließen, um relevante Nachrichten an Benutzer zu senden und das Engagement zu erhöhen.

Schauen Sie sich die folgenden Anwendungsfälle an, um einen kleinen Eindruck davon zu bekommen, wie Braze-Segmente Ihnen helfen können, Ihre Nutzer gezielt anzusprechen.

### Anwendungsfälle

- **Willkommensnachrichten:** Segmentieren Sie neue Nutzer:innen, damit Sie ihnen Onboarding-E-Mails oder In-App-Nachrichten schicken können, die sie mit Ihrer App bekannt machen.
- **Treue-Rewards:** Segmentieren Sie die Benutzer anhand ihrer Kaufhäufigkeit, ihres Mitgliedsjubiläums oder anderer Meilensteine und senden Sie exklusive Angebote oder Belohnungen an Ihre treuesten Benutzer.
- **Verhaltensbedingte Auslöser:** Segmentieren Sie Benutzer auf der Grundlage ihrer Aktionen, wie z.B. dem Verlassen eines Warenkorbs an der Kasse, um In-App-Nachrichten oder Push-Benachrichtigungen auszulösen.
- **Artikel-Empfehlungen:** Segmentieren Sie Nutzer, die bestimmte Produkte gekauft haben, und senden Sie ihnen Empfehlungen für ergänzende oder höherwertige Produkte.
- **A/B-Tests:** Segmentieren Sie Nutzer für A/B-Tests verschiedener Nachrichten, Betreffzeilen oder Inhalte, um festzustellen, was bei Nutzern bestimmten Alters, Geschlechts oder anderer Merkmale am besten ankommt.

#### Anwendungsfälle der Segmenterweiterung

Sie können Ihre Segmente weiter verfeinern, indem Sie [Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) verwenden, um Benutzer auf der Grundlage von benutzerdefinierten Ereignissen oder Kaufverhalten anzusprechen, die während der gesamten Lebensdauer ihres Benutzerprofils gespeichert werden.

- **Historische Käufe:** Segmentieren Sie Nutzer danach, ob sie in den letzten zwei Jahren mindestens zweimal eine bestimmte Farbe eines bestimmten Produkts gekauft haben.
- **Events und Nachrichten-Interaktionen:** Segmentieren Sie die Nutzer danach, ob sie in den letzten dreißig Tagen einen Kauf getätigt haben und außerdem mit einer bestimmten In-App-Nachricht interagiert haben.
- **Daten abfragen:** 
  - **Snowflake abfragen:** Segmentieren Sie Nutzer:innen mit kombinierten Daten aus Braze und externen Quellen, wie z. B. einem CRM oder einem Data Warehouse, indem Sie [SQL-Segmenterweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) zur Abfrage von Snowflake verwenden.
  - **Synchronisierung aus dem Data Warehouse:** Segmentieren Sie Nutzer:innen mit Daten, die direkt aus Ihrem Data Warehouse oder Dateispeichersystem mit Braze synchronisiert wurden, indem Sie [CDI Segment-Erweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/) verwenden.

