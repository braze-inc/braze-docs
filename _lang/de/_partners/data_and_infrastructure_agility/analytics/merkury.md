---
nav_title: Merkury
article_title: Merkury
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Merkury, einer Unternehmensidentitätsplattform für Ihre Anwendungen, die es Ihnen ermöglicht, die `MerkuryID` zu nutzen, um die Erkennungsraten der Website-Besucher für Braze-Kunden zu erhöhen."
page_type: partner
search_tag: Partner

---

# Merkury

> [Merkury](https://merkury.merkleinc.com/) ist die Unternehmensidentitätsplattform von Merkle, die Marken dabei hilft, die Kundenbindung, das Kundenerlebnis und den Umsatz durch kochunabhängige Identitätsfunktionen zu maximieren. Die `MerkuryID` vereinigt die bekannten und unbekannten Kunden- und Interessentendatensätze, Website-/App-Besuche und Verbraucherdaten einer Marke zu einer einzigen, dauerhaften Personen-ID.

Die Integration von Braze und Merkury ermöglicht es Ihnen, die `MerkuryID` zu nutzen, um die Erkennungsrate von Braze-Kunden zu erhöhen. Wenn Merkury erkennt, dass es sich bei den Besuchern um E-Mail-Abonnenten der Marke handelt, wird das Braze-Profil mit der E-Mail-Adresse des Abonnenten aktualisiert. Die verbesserten Erkennungsmöglichkeiten von `MerkuryID` verbessern die Möglichkeiten zur Einbindung und Personalisierung und erhöhen sofort die Anzahl der gesendeten Abbruch-E-Mails und die damit verbundenen Einnahmen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Merkle-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Merkle-Konto. |
| Merkle Kunden-ID | Erhalten Sie Ihre Kunden-ID von Ihrem Merkle-Vertreter. |
| Merkury-Tag | Platzieren Sie den Merkle Merkury Tag auf Ihrer Website. |
| Braze REST und SDK Endpunkt | Ihre REST- oder SDK-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track, users.export.ids, users.export.segment, and segments.list` Berechtigungen. <br><br>Dieser kann über **Braze Dashboard > Developer Console > REST API Key > Create New API Key** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Die Anfragen der Merkury-Identitätskonnektoren an Braze bewegen sich innerhalb der Spezifikationen für die Braze-API-Rate. Kontaktieren Sie Braze oder Ihren Merkle-Kundenbetreuer, wenn Sie Fragen haben.<br><br>Merkury sendet mindestens eine Anfrage am Ende einer qualifizierten Sitzung.
{% endalert %}

## Nebeneinander liegende SDK-Integration

Verwendet das client-seitige Merkury-Tag von Merkle zur Erfassung von Braze-Geräten und leitet sie zur Identifizierung an den Merkury-Identitätskonnektor-Endpunkt weiter.

### Schritt 1: Braze web SDK Tag einrichten

Sie müssen das [Braze Web SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm) auf Ihrer Website implementiert haben, um diese Integration zu nutzen.

### Schritt 2: Setzen Sie den Merkury-Tag von Merkle ein

Setzen Sie den Merkury-Tag auf Ihrer Website ein. Dadurch wird der Merkury-Identitätskonnektor auf Ihrer Website verfügbar. Ein detaillierter Leitfaden mit Anweisungen wird Ihnen von Ihrem Merkle-Kundenbetreuer zur Verfügung gestellt.

### Schritt 3: Benutzerdefinierte Attribute erstellen

Die folgenden Felder werden vom Merkury Identitätskonnektor ausgefüllt und müssen in Braze als [benutzerdefinierte Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attributes) erstellt werden.

| Attributname | Datentyp | Beschreibung |
| --- | --- | --- |
| `hmid` | String | Merkle's Merkury ID |
| `confidence_score` | Nummer | Wie sicher war Merkury bei der Identifizierung (1-8, niedriger ist besser) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Schritt 4: Stellen Sie Merkle das E-Mail-Universum der Benutzer zur Verfügung

Merkle empfiehlt einen Segmentierungsexport Ihres zulässigen E-Mail-Universums. Dies kann mit täglichen Exporten aktiver zulässiger Benutzer weiterverfolgt werden.

Die folgenden Felder sind erforderlich:

- `braze_id`
- `external_id`
- E-Mail Adresse

Wenden Sie sich für weitere Informationen an Ihren Braze-Vertreter.