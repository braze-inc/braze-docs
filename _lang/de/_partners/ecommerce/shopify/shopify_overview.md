---
nav_title: Shopify Übersicht
article_title: "Shopify Übersicht"
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Shopify, einem globalen Handelsunternehmen, die es Ihnen erlaubt, ihren Shopify-Shop nahtlos mit Braze zu verbinden, um ausgewählte Shopify-Webhooks an Braze weiterzugeben. Nutzen Sie die kanalübergreifenden Strategien von Braze und Canvas, um Kund:innen zum Abschluss ihrer Einkäufe zu bewegen oder Nutzer:innen auf der Grundlage ihrer früheren Einkäufe erneut zu retargeten."
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Shopify-Übersicht

> [Shopify](https://www.shopify.com/) ist ein weltweit führendes Handelsunternehmen, das zuverlässige Tools für die Gründung, das Wachstum, das Marketing und die Verwaltung von Unternehmen jeder Größe bereitstellt. Shopify macht den Handel für alle besser, mit einer Plattform und Diensten, die auf Zuverlässigkeit ausgelegt sind und Verbrauchern:in aller Welt ein besseres Einkaufserlebnis zustellen.

Die Integration von Braze in Shopify bietet eine leistungsstarke Lösung für E-Commerce-Unternehmen, die ihr Customer-Engagement verbessern und personalisiertes Marketing betreiben möchten. Diese Integration verbindet die robusten E-Commerce-Funktionen von Shopify nahtlos mit unserer fortschrittlichen Customer-Engagement-Plattform und ermöglicht es Ihnen, Ihren Nutzern gezielte, relevante und zeitnahe Nachrichten zuzustellen, die auf Echtzeit-Einkaufsverhalten und Transaktionsdaten basieren.

## Anforderungen

| Anforderung | Beschreibung |
| --- | --- |
| Shopify-Shop | Sie haben einen aktiven Shopify Shop. |
| Berechtigungen für Shopify Shop-Besitzer oder Mitarbeiter | {::nomarkdown}<ul><li>Zugang zu allen allgemeinen Einstellungen und den Einstellungen des Online Shops.</li><li> Zusätzliche Admin-Berechtigungen:</li><ul><li>Bestellungen: Anzeigen</li><li>Kund:in: LesenSchreiben</li><li>Kunden:in-Events anzeigen (Internet-Pixel)</li><li>Einstellungen verwalten</li><li>Apps ansehen, die von Mitarbeitern/Kollaborateuren entwickelt wurden</li><li>Verwalten/Installieren von Apps und Kanälen</li><li>Angepasste Bildpunkte verwalten/hinzufügen</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Wie man integriert 

Braze bietet zwei Integrationsoptionen für Shopify-Händler, die auf die unterschiedlichen Bedürfnisse von E-Commerce-Unternehmen zugeschnitten sind: **Standardintegration** und **angepasste Integration**.

{% multi_lang_include shopify.md section='Integration Tabs' %}

## So funktioniert die Integration

Wenn Sie in Ihren Konfigurationseinstellungen bereits den historischen Backfill eingerichtet und aktiviert haben, wird die erste Synchronisierung der Daten sofort beginnen. Braze importiert alle Kund:innen und bestellten Events aus den letzten 90 Tagen vor Ihrer Shopify Integration. Wenn Braze Ihre Shopify Kund:in importiert, weisen wir den `external_id` Typ zu, den Sie in Ihren Konfigurationseinstellungen gewählt haben.

Wenn Sie die Integration mit einer angepassten externen ID planen (entweder für die [Standardintegration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4-configure-how-you-manage-users) oder die [benutzerdefinierte Integration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6-configure-how-you-manage-users-optional)), müssen Sie Ihre angepasste externe ID als Shopify-Kunden-Metafeld zu allen bestehenden Shopify-Kundenprofilen hinzufügen und dann den [historischen Backfill]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) durchführen. 

Nach der anfänglichen Datensynchronisierung verfolgt Braze kontinuierlich neue Daten und Updates, direkt von Shopify und den Braze SDKs.

{% alert note %}
Wenn Sie bereits Kund:in von Braze sind und über aktive Kampagnen oder Canvase verfügen, finden Sie wichtige Informationen in der [Shopify Historie]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill). Um zu sehen, welche spezifischen Kundendaten abgefüllt werden, lesen Sie die [Shopify Features]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).
{% endalert %}

### Nutzer:innen und Daten synchronisieren

Nachdem die Integration in Betrieb genommen wurde, wird Braze über die Shopify-Integration Nutzerdaten aus zwei wichtigen Quellen sammeln:
- **Shopify Internet Pixel API und App-Einbettungen:** Das Braze Web SDK und das Javascript SDK unterstützen das Tracking vor Ort, das Identitätsmanagement, die Verhaltensdaten im E-Commerce und leistungsstarke Messaging-Kanäle wie In-App-Nachrichten.
- **Shopify Webhooks:** E-Commerce Verhaltensdaten, Produkt-Synchronisation und Abonnent: innen-Datenerfassung

Beim Onboarding der Integration müssen Sie auswählen, wann die Braze SDKs initialisiert und Ihre Shopify-Website geladen werden soll: 
- Beim Besuch vor Ort (z.B. bei Beginn der Sitzung)
    - **Was es tut:** Tracking anonymer Nutzer:innen - wie z.B. Gastkäufer - um mehr Daten für eine tiefere Personalisierung zu erhalten 
- Bei der Anmeldung eines Kontos (z.B. bei der Anmeldung eines Kontos) 
    - **Was es tut:** Verhindert das Tracking anonymer Nutzer:in für einen konservativeren, datenschutzorientierten Ansatz, so dass die Aktivitäten der Nutzer:in *nach der* Anmeldung in ihrem Konto verfolgt werden.

{% alert note %}
- Besuche auf der Website (Sitzungen) werden auf Ihre monatlichen aktiven Nutzer:in angerechnet.
- Die Versionen des Braze Web SDK und des JavaScript SDK werden automatisch auf v5.4.0 gesetzt.
{% endalert %}

Braze nutzt die Shopify Integration, um mehrere Bezeichner zu unterstützen, die das Tracking Ihrer Nutzer:innen von ihrem Gasteinkauf bis zu ihrer Identifizierung ermöglichen:

| Braze Bezeichner | Beschreibung |
| --- | --- |
| Braze `device_id` | Eine zufällig generierte ID, die im Browser gespeichert ist und die Aktivitäten anonymer Nutzer:in über Braze SDKs verfolgt. |
| Warenkorb Token Nutzer:in alias | Ein Alias, den Braze zum Tracking von Update-Ereignissen für den Warenkorb erstellt. Dieses Token wird mit dem Shopify Warenkorb-Token erstellt. |
| Token Nutzer:in für die Kasse | Ein Alias, den Braze erstellt, wenn der Nutzer:in den Checkout-Prozess einsteigt. Dieses Token wird mit Hilfe des Shopify Checkout Token erstellt. |
| Shopify ID alias | Die Shopify Kund:in ID wird als Alias zugewiesen, wenn die externe ID bei der Anmeldung des Kontos oder bei einer Bestellung zugewiesen wird. |
| Braze `external_id` | Ein eindeutiger Bezeichner, der das Tracking von Kund:in über verschiedene Geräte und Plattformen hinweg unterstützt. Dies sorgt für ein konsistentes App-Erlebnis und verbessert die Analytics, indem es verhindert, dass Nutzer:innen mehrere Profile anlegen, wenn sie das Gerät wechseln oder die App neu installieren.<br><br>Die Shopify Integration unterstützt die folgenden `external_id` Typen: <br><br>{::nomarkdown}<ul><li>Shopify Kund:in ID (Standard)</li><li>Angepasste externe ID</li><li>Gehashte E-Mail (SHA-256)</li><li>Gehashte E-Mail (SHA-1)</li><li>Gehashte E-Mail (MD5)</li><li>E-Mail</li></ul>{:/}Braze weist Ihren Nutzer:innen eine `external_id` zu, indem Sie die changeUser-Methode innerhalb des SDKs aufrufen, wenn: <br><br>{::nomarkdown}<ul><li>Ein Nutzer:in meldet sich an oder erstellt ein Konto</li><li>eine Bestellung wird aufgegeben</li></ul>{:/}<br> Weitere Informationen darüber, was passiert, wenn Sie einem anonymen Profil ein `external_id` zuweisen, finden Sie unter [Nutzerprofil-Lebenszyklus]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).<br><br>Braze wird auch die `external_id` nutzen, um nachgelagerte E-Commerce-Verhaltensdaten von Shopify Webhooks zu attributieren.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Für die Integration müssen die SDKs von Braze und die Serviceleistungen; Dienste von Shopify zusammenarbeiten, damit die Daten von Shopify in nahezu Echtzeit den richtigen Nutzer:innen zugeordnet und getrackt werden können. Weitere Einzelheiten zu den Daten, die durch die Integration getrackt werden, finden Sie unter [Shopify-Daten]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).

{% alert note %}
- Wenn Sie die Integration testen, raten wir Ihnen, den Inkognito-Modus zu verwenden oder Ihre Cookies zu löschen, um die Braze `device_id` zurückzusetzen und das Verhalten eines anonymen Nutzer:innen zu imitieren.
- Auch wenn eine Shopify Kunden-ID generiert wird, wenn eine E-Mail in die Shopify Newsletter-Fußzeile eingegeben wird oder während des Bestellvorgangs, bevor eine Bestellung aufgegeben wird, ist diese Kunden-ID nicht über Shopify Internet Pixels zugänglich. Aus diesem Grund kann Braze die Methode `changeUser` in diesen beiden Situationen nicht verwenden.
{% endalert %}

### Synchronisierung der Opt-ins für E-Mail- und SMS-Marketing von Shopify

Wenn Sie die Abo-Sammlung in Ihren Konfigurationseinstellungen aktivieren, müssen Sie für jeden Shop, den Sie mit Braze verbinden, eine Abo-Gruppe zuweisen. Das bedeutet, dass Ihre Kund:in der Abo-Gruppe Ihres Shops entweder als "abonniert" oder als "abgemeldet" kategorisiert werden.

Der Opt-in-Status des Shopify Marketings für E-Mail- und SMS-Marketing kann auf folgende Weise aktualisiert werden:
- **Manuelles Update:** Sie können den Opt-in-Status eines Nutzers:innen für E-Mail- oder SMS-Marketing manuell in Ihrem Shopify-Admin ändern.
- **Shopify Newsletter Fußzeile:** Wenn ein Nutzer:innen seine E-Mail in der Shopify Standard Newsletter-Fußzeile eingibt, wird sein Opt-in-Status aktualisiert.
- **Checkout-Prozess:** Wenn ein Nutzer:innen seinen Opt-in-Status während des Bestellvorgangs aktualisiert.

{% alert note %}
Der Opt-in-Status für E-Mail-Marketing von Shopify ändert nicht den [Status des globalen E-Mail-Abos]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) eines Nutzers:innen in Braze. Der Standardstatus des Abonnements bei der Erstellung eines Nutzerprofils ist "abonniert". Denken Sie daran, die Abo-Gruppe als Teil Ihrer Kampagnen- oder Canvas-Eingangskriterien zu verwenden.
{% endalert %}

Diese Tabelle zeigt, welche Opt-in-Status von Shopify Marketing mit den Status innerhalb Ihrer Abo-Gruppe von Braze korrelieren. 

| Shopify Marketing Opt-in Status | Braze Abo-Gruppe Status |
| --- | --- |
| E-Mail ist abonniert | Abonniert |
| E-Mail ist abbestellt | Abgemeldet |
| E-Mail ist noch nicht bestätigt | Abgemeldet |
| E-Mail ist ungültig | Abgemeldet |
| SMS abonniert | Abonniert |
| SMS abgemeldet | Abgemeldet |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Formulare für die Registrierung

#### Shopify Newsletter Fußzeile

Nutzer:innen, die ihre E-Mail in die Shopify Newsletter-Fußzeile eingeben, erleben einen dieser Workflows:

##### Nutzer:in, die sich nicht in ihr Konto eingeloggt haben

1. Braze empfängt einen eingehenden Shopify-Webhook, wenn ein Kunde:in erstellt oder aktualisiert wird.
2. Braze erstellt ein Nutzerprofil, das die E-Mail Adresse und den Shopify ID-Alias enthält, die mit diesem Nutzer:innen verbunden sind.
3. Das Braze SDK aktualisiert das anonyme Profil mit der E-Mail Adresse.

{% alert note %}
Dies kann zu einem doppelten Profil führen, bis der Nutzer:in sich selbst identifiziert, indem er sein Konto einrichtet, sich bei seinem Konto anmeldet oder eine Bestellung aufgibt. Braze bietet Tools für die Massenzusammenführung, mit denen Sie den Abgleich von doppelten Profilen automatisieren können. Weitere Informationen finden Sie unter [Nutzer:innen duplizieren]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/).
{% endalert %}

##### Nutzer:in, die sich bereits in ihrem Konto angemeldet haben

Braze erstellt ein Nutzerprofil mit der E-Mail Adresse und dem Shopify ID-Alias, die mit diesem Nutzer:innen verbunden sind. Braze aktualisiert die E-Mail Adresse des angemeldeten Nutzers:innen nicht, da wir davon ausgehen, dass Shopify diese Informationen bereits zur Verfügung gestellt hat.

#### Braze Formulare für die Registrierung

Braze bietet zwei Arten von Templates für Registrierungsformulare:
- **[Formulare für die Registrierung per E-Mail]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/email_capture/):** Erstellen Sie diese mit dem Drag-and-Drop-Editor.
- **[Traditionelles E-Mail-Erfassungsformular für Redakteure]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/):** Ein einfacheres Formular zur Erfassung von E-Mail-Adressen.

Wenn Sie diese Templates für Registrierungsformulare verwenden, aktualisiert Braze automatisch den Status des globalen E-Mail Abos im Nutzerprofil. Weitere Einzelheiten zum Umgang mit dem globalen Status des E-Mail-Abos, einschließlich Informationen zur Validierung von E-Mails, finden Sie in der Dokumentation für jeden Formularvorlagentyp.

{% alert note %}
- Stellen Sie sicher, dass Ihre Kampagne oder Ihr Canvas Eingangskriterien enthält, die sowohl den globalen E-Mail-Abonnementstatus als auch die Abo-Gruppe, die mit Ihrem Shopify-Shop verbunden ist, umfassen. So können Sie sicherstellen, dass Sie die richtige Zielgruppe ansprechen. 
- Braze sammelt über In-Browser-Nachrichten Informationen über Besucher, wie z.B. E-Mail-Adressen und Telefonnummern. Diese Informationen werden dann an Shopify gesendet. Diese Daten helfen Händlern, die Besucher ihres Shops zu erkennen und ein personalisiertes Einkaufserlebnis zu schaffen. Weitere Einzelheiten finden Sie unter [Besucher-API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

#### Formulare für die Registrierung durch Dritte 

Wenn Sie eine Plattform eines Drittanbieters oder ein Shopify-Plugin für Ihre Registrierungsformulare verwenden, müssen Sie mit Ihren Entwicklern:in zusammenarbeiten, um den Code für das Braze SDK zu integrieren, um die E-Mail Adresse und den globalen E-Mail Abo-Status aus den Formularübermittlungen zu erfassen. Um mehr zu erfahren, sehen Sie sich die [Einrichtung der Shopify Standard-Integration]({{site.baseurl}}/shopify_standard_integration/) und die [Einrichtung der angepassten Shopify-Integration]({{site.baseurl}}/shopify_custom_integration/) an.

### Produkte synchronisieren 

Braze unterstützt die Möglichkeit, die Produkte Ihres Shopify Shops mit einem Braze Katalog zu synchronisieren. Weitere Einzelheiten finden Sie unter [Shopify Produkt-Synchronisationen]({{site.baseurl}}/shopify_catalogs/).

## Anfragen zum Thema Daten

Im Rahmen der Shopify-Integration der Braze-Plattform empfängt Braze automatisch [die Webhooks von Shopify zur Einhaltung von Richtlinien](https://shopify.dev/docs/apps/build/privacy-law-compliance/). Da die Kunden jedoch die für die Daten ihrer Nutzer:innen verantwortlichen Personen sind, müssen sie alle Maßnahmen ergreifen, die erforderlich sind, um Anfragen bezüglich der Daten der Nutzer:innen in Braze (einschließlich der Daten der Nutzer:innen, die über die Shopify Integration erhalten wurden) zu beantworten. Weitere Einzelheiten finden Sie in unserer Dokumentation [zur technischen Unterstützung des Datenschutzes]({{site.baseurl}}/dp-technical-assistance).