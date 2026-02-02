---
nav_title: StackAdapt
article_title: StackAdapt
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und StackAdapt."
alias: /partners/stackadapt/
page_type: partner
search_tag: Partner
---

# StackAdapt

> [StackAdapt](https://www.stackadapt.com/) ist die führende KI-gestützte Marketing-Plattform, die von digitalen Marketern genutzt wird, um zielgerichtete Performance-gesteuerte Werbung zu liefern.

_Diese Integration wird von StackAdapt gepflegt._

Die Integration von Braze und StackAdapt erlaubt es Ihnen, Nutzerprofil-Daten aus Braze mit dem StackAdapt Data Hub zu synchronisieren. Durch die Verbindung der beiden Plattformen können Sie eine einheitliche Sicht auf Ihre Kund:innen schaffen und First-Party-Daten aktivieren, um die Performance von Anzeigen zu verbessern.

## Anwendungsfälle

- **Erneutes Engagement für passive Nutzer:innen:** Identifizieren Sie Nutzer:innen, die sich von E-Mail-Marketing-Listen in Braze abgemeldet haben, und stellen Sie sie mit programmatischen Anzeigen auf StackAdapt zusammen, um sie über einen anderen Kanal wieder zu engagieren.
- **Schaffen Sie Erlebnisse auf mehreren Kanälen:** Erweitern Sie die Reise eines Nutzers:innen über E-Mails hinaus. Wenn ein Nutzer:innen zum Beispiel auf eine E-Mail Kampagne in Braze klickt, können Sie ihm mit StackAdapt eine ergänzende programmatische Anzeige zeigen, die die Nachricht verstärkt und zu weiteren Aktionen anregt.
- **Personalisieren Sie in großem Umfang:** Nutzen Sie granulare Datenpunkte von Braze, wie "Heimatort" oder "Sprache", um hochrelevante, lokalisierte und sprachspezifische Anzeigen und E-Mails zu schalten.
- **Vertiefen Sie das Verständnis für Ihre Zielgruppe:** Durch die Synchronisierung von Profil-Attributen können Sie in StackAdapt umfangreichere Segmente für Zielgruppen erstellen, die ein präziseres Targeting und personalisierte Werbeerlebnisse ermöglichen.

## Voraussetzungen

| Anforderung | Beschreibung         |
| ----------- | ------------------- |
| **StackAdapt-Konto**  | Sie benötigen ein aktives StackAdapt-Konto mit Berechtigungen, um Data Hub-Integrationen zu verwalten. |
| **Braze REST API-Schlüssel**  | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen: <br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden **.** |
| **Braze REST Endpunkt** | [Ihre URL für den REST-Endpunkt](https://www.braze.com/docs/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Funktionsweise

Der StackAdapt Data Hub stellt eine direkte Verbindung zu Ihrem Braze-Konto her, um die Attribute des Nutzerprofils abzurufen. Dies erlaubt es Ihnen, Ihre Braze Kundendaten direkt in StackAdapt für eine fortschrittliche Segmentierung und Aktivierung der Zielgruppe zu nutzen.

### Datenfluss

1. StackAdapt initiiert eine sichere Verbindung zu Ihrer Braze-Instanz unter Verwendung der angegebenen API Zugangsdaten.
2. StackAdapt ruft Nutzerprofildaten und speziell die Eigenschaften ab, die Sie ausgewählt und abgebildet haben.
3. Die Daten werden normalisiert und in Ihren StackAdapt Data Hub aufgenommen und stehen dann für die Segmentierung und die Verwendung in Ihren Kampagnen zur Verfügung.
4. Die Integration lässt einen Zeitplan für die Synchronisierung von Daten zu (z.B. täglich), damit Ihre Zielgruppen von StackAdapt immer mit den neuesten Profildaten von Braze versorgt sind.

## Felder synchronisiert

StackAdapt kann eine Vielzahl von Feldern des Braze-Profils synchronisieren, einschließlich, aber nicht beschränkt auf:

{% tabs local %}
{% tab Standard attributes %}
- E-Mail
- Geburtsdatum
- Vorname
- Nachname
- Telefon
- Heimatstadt
- Land
- Geschlecht
- Zeitzone
- Erstellt am
- Externe ID
- Sprache 

{% endtab %}
{% tab Custom attributes %}
Attribute, die für Ihre App oder Ihr Unternehmen spezifisch sind und auf der Grundlage Ihrer spezifischen Geschäftsanforderungen definiert werden.

{% endtab %}
{% tab Attribution data %}
- Attributierte Anzeige
- Attributierte Anzeigengruppe
- Attribution-Kampagne
- Attributierte Quelle

{% endtab %}
{% tab Subscription status %}
- E-Mail-Abostatus
- Push-Abostatus 

Es ist wichtig, die Felder in Braze, die die Zustimmung der Nutzer:innen für Marketing-Kommunikation widerspiegeln (z.B. den Status des E-Mail-Abos), genau abzubilden, damit Ihre Werbemaßnahmen mit den Nutzer:innen-Einstellungen und den Datenschutzbestimmungen konform gehen.

{% endtab %}
{% endtabs %}

## Einrichten der Integration

Folgen Sie diesen Schritten, um Ihre Nutzer:innen-Profile zu importieren:

1. Melden Sie sich bei Ihrem StackAdapt-Konto an.
2. Wählen Sie im Navigationsmenü **Data Hub** aus.
3. Wählen Sie **Profile importieren** und wählen Sie dann **Braze** aus der Liste der verfügbaren Integrationen aus.
4. Geben Sie Ihre Braze API-Zugangsdaten ein, wenn Sie dazu aufgefordert werden.
- **Braze REST API-Schlüssel:** Den Standort finden Sie in Braze unter **Einstellungen** > **API-Schlüssel**. Als bewährte Sicherheitspraxis empfehlen wir Ihnen, einen eigenen API-Schlüssel für Ihre StackAdapt-Integration zu erstellen.
- **Braze App Key:** Den Standort finden Sie in Braze unter **Einstellungen** > **API-Schlüssel** oder **Apps verwalten**.
- **Braze REST Endpunkt URL:** Die Basis-URL für Ihre Braze-Instanz (z. B. ```https://rest.iad-01.braze.com```).
5. Wählen Sie **Verbinden**, um die Zugangsdaten zu überprüfen.

![Braze-Verbindung in StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_braze_connection_settings.png %})

{: start="6"}
6\. Wählen Sie Ihre Verbindung und wählen Sie Ihren StackAdapt-Anbieter aus.
7\. Konfigurieren Sie Ihre **Eigenschaften-Abbildungen**. Überprüfen und bestätigen Sie die von StackAdapt vorgeschlagenen Standard-Abbildungen und vorausgewählten Eigenschaften.
8\. (Optional) Wenn Sie weitere Eigenschaften importieren möchten, wählen Sie diese aus, indem Sie die entsprechenden Kontrollkästchen aktivieren und angeben, ob sie PII enthalten und welchen Datentyp sie haben.

![Braze-Verbindung in StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_mappings.png %})

{: start="9"}
9\. Fügen Sie Ihre Profile zu einer **Liste** hinzu oder erstellen Sie eine neue, damit Sie Ihre Profile gruppieren und segmentieren können.
10\. Wählen Sie **Integration aktivieren**, um die erste Daten-Synchronisation zu starten.

## Überlegungen

- **Importieren von angepassten Events und Eigenschaften:** Dieses Feature wird noch nicht unterstützt.
- **Daten-Latenzzeit:** Es kann bis zu 24 Stunden dauern, alle Nutzer:innen-Daten zu importieren.
- **Verwaltung der Zustimmungen:** Vergewissern Sie sich, dass Ihre Datenerfassung in Braze mit den Datenschutzbestimmungen übereinstimmt und dass Sie die erforderliche Zustimmung zur Verwendung von Kundendaten für Werbezwecke haben. StackAdapt verlässt sich auf den Zustimmungsstatus, der von Ihren Quellsystemen übermittelt wird.
- **Konsistenz der Attribute:** Um die Effektivität Ihrer Daten zu maximieren, sollten Sie die Benennung und Befüllung der Attribute in Braze konsistent halten, bevor Sie sie mit StackAdapt synchronisieren.
