---
nav_title: Kataloge
article_title: Kataloge
page_order: 6
layout: dev_guide

guide_top_header: "Kataloge"
guide_top_text: "Kataloge greifen auf Daten aus importierten CSV-Dateien und API-Endpunkten zu, um Ihre Nachrichten anzureichern, ähnlich wie Sie über Liquid auf benutzerdefinierte Attribute oder benutzerdefinierte Ereigniseigenschaften zugreifen würden."

description: "Auf dieser Landing Page finden Sie Kataloge. Verwenden Sie Kataloge und gefilterte Sets, um Nicht-Nutzerdaten in Ihren Braze-Kampagnen zu nutzen und personalisierte Nachrichten zu versenden."

guide_featured_title: "Abschnittsartikel"
guide_featured_list:
- name: Einen Katalog erstellen
  link: /docs/user_guide/data/activation/catalogs/create/
  image: /assets/img/braze_icons/users-01.svg
- name: Kataloge verwenden
  link: /docs/user_guide/data/activation/catalogs/use/
  image: /assets/img/braze_icons/users-01.svg
- name: „Wieder verfügbar“-Benachrichtigungen
  link: /docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Benachrichtigungen über Preissenkungen
  link: /docs/price_drop_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Auswahlen
  link: /docs/user_guide/data/activation/catalogs/selections/
  image: /assets/img/braze_icons/list.svg

guide_menu_title: "Other articles"
guide_menu_list:
- name: Kataloge API Endpunkte
  link: /docs/api/endpoints/catalogs/
  image: /assets/img/braze_icons/server-01.svg
- name: Drag-and-Drop Produktblöcke
  link: /docs/dnd_product_blocks/
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## Katalog Anwendungsfälle

Sie können jede Art von Daten in einen Katalog einbringen. In der Regel handelt es sich bei den Daten um Metadaten über Angebote wie Produkte, Rabatte, Werbeaktionen, Events und ähnliches. In den folgenden Anwendungsfällen finden Sie einige Beispiele dafür, wie Sie diese Daten nutzen können, um Nutzern hochrelevante Nachrichten zukommen zu lassen.

### Einzelhandel und E-Commerce

- **Saisonale Aktionen:** Importieren Sie saisonale Produktkollektionen und personalisieren Sie Nachrichten, um aktuelle Trends widerzuspiegeln.
- **Lokalisierte Nachrichten:** Importieren Sie die Adressen, Öffnungszeiten und Dienstleistungen Ihres Standorts und personalisieren Sie dann die Benachrichtigungen auf der Grundlage der Nutzerstandorte.
- **„Wieder verfügbar“-Benachrichtigungen:** Importieren Sie Produktinformationen einschließlich der Bestandsmenge und verwenden Sie dann [Back-in-Stock-Benachrichtigungen]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/) und benutzerdefinierte Braze-Ereignisse, um eine Kampagne oder ein Canvas auszulösen, das Benutzern eine Benachrichtigung darüber sendet, dass ein Produkt jetzt auf Lager ist.
- **Benachrichtigungen über Preissenkungen:** Importieren Sie Produktinformationen, die Produktpreise enthalten, und verwenden Sie dann [Benachrichtigungen über Preisrückgänge]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/) und benutzerdefinierte Braze-Ereignisse, um ein Canvas auszulösen, das Benutzern eine Benachrichtigung über den Preisrückgang eines Produkts sendet.

### Unterhaltung

- **Abo-Pläne:** Importieren Sie Abo-Pläne und werben Sie bei Ihren Nutzer:innen für Add-Ons auf der Grundlage ihres Nutzungsverhaltens und der Content-Typen, die sie am häufigsten konsumieren.
- **Bevorstehende Events:** Importieren Sie Listen mit bevorstehenden Ereignissen, deren Orten und Altersgruppen und senden Sie dann personalisierte Benachrichtigungen an Nutzer, die sich in der Gegend aufhalten und der gewünschten Altersgruppe angehören.
- **Bevorzugte Medien:** Importieren Sie Informationen über Filme und Sendungen und empfehlen Sie Ihren Nutzern dann Inhalte auf der Grundlage ihrer bevorzugten Titel und meistgesehenen Genres.

### Reisen und Gastgewerbe

- **Ziele:** Importieren Sie Reiseziele und deren beliebteste Attraktionen, Restaurants und Aktivitäten, und personalisieren Sie dann die Empfehlungen für Ihre Benutzer auf der Grundlage ihrer früheren Reisen.
- **Unterkünfte:** Importieren Sie Hotelimmobilien und deren Ausstattung, Zimmertypen und Preise und senden Sie dann Werbeangebote an Ihre Nutzer auf der Grundlage ihrer ausgewählten Präferenzen.
- **Reisemethoden**: Importieren Sie Angebote und Aktionen für Reisearten (z.B. Flüge, Züge, Mietwagen und andere) und senden Sie diese dann an Ihre Nutzer auf der Grundlage ihres jüngsten Suchverlaufs.
- **Bevorzugte Mahlzeiten:** Importieren Sie Informationen über das Essensangebot und verwenden Sie die [Auswahl]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/), um personalisierte Nachrichten an Benutzer zu senden, die bestimmte Essensvorlieben haben, basierend auf ihrer zuletzt angesehenen Essenskategorie.

## Wie Kataloge und Liquid zusammenarbeiten

Kataloge sind eine Funktion zur Datenspeicherung. Sie enthalten große Mengen an Daten, auf die Sie in Ihren Nachrichten zur Personalisierung verweisen können. Um die Daten tatsächlich zu referenzieren, verwenden Sie [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) als Templating-Sprache. Mit anderen Worten: Kataloge sind der Speicher, in dem die Daten aufbewahrt werden, und Liquid ist die Sprache, die die relevanten Daten aus dem Speicher holt.

Beispiele dafür, wie Sie Liquid zum Abrufen von Kataloginformationen verwenden können, finden Sie in den zusätzlichen Anwendungsfällen unter [Erstellen eines Katalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#additional-use-cases/).

#### Einschränkungen bei der Speicherung von Daten

Der Datenspeicher für Kataloge ist aufgrund der Größe der Katalogartikel begrenzt, die sich von der Größe der hochgeladenen CSV-Dateien unterscheiden kann.

Bei der kostenlosen Version von Katalogen ist ein Speicherplatz von bis zu 100 MB zulässig. Sie können unbegrenzt Artikel haben, solange der Speicherplatz 100 MB nicht überschreitet.

Für Catalogs Pro sind die Optionen für die Speichergröße wie folgt: 5 GB, 10 GB, 15 GB oder 50 GB. Beachten Sie, dass der Speicherplatz der kostenlosen Version (100 MB) in jedem dieser Tarife enthalten ist.
