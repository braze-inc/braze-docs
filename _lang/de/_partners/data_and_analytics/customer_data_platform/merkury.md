---
nav_title: Merkury
article_title: Merkury
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Merkury, einer Unternehmensidentitätsplattform für Ihre Apps, die es Ihnen erlaubt, die `MerkuryID` zu nutzen, um die Erkennungsrate von Website-Besuchern für Kund:in von Braze zu erhöhen."
page_type: partner
search_tag: Partner

---

# Merkury

> [Merkury](https://merkury.merkleinc.com/) ist die Identitätsplattform von Merkle für Unternehmen, die Marken dabei hilft, das Engagement, die Erfahrung und den Umsatz ihrer Verbraucher:in zu maximieren, indem sie die Identität der ersten Partei nutzt. Die `MerkuryID` vereinigt die bekannten und unbekannten Datensätze von Kunden und Interessenten einer Marke, Website-/App-Besuche und Verbraucher:in-Daten zu einer einzigen, persistenten ID.

_Diese Integration wird von Merkury gepflegt._

## Über die Integration

Die Integration von Braze und Merkury erlaubt es Ihnen, die `MerkuryID` zu nutzen, um die Erkennungsrate von Braze-Kunden zu erhöhen. Wenn Merkury erkennt, dass es sich bei den Besuchern um Abonnent:innen der Marke handelt, wird das Profil von Braze aktualisiert, um die E-Mail Adresse der Abonnent:innen aufzunehmen. Die verbesserten Erkennungsmöglichkeiten von `MerkuryID` verbessern das Engagement und die Chancen der Personalisierung und erhöhen sofort die Anzahl der gesendeten E-Mails und die damit verbundenen Einnahmen. 

## Voraussetzungen

| Anforderung | Beschreibung |
| --- | --- |
| Merkle Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Merkle Konto. |
| Merkle Client-ID | Erhalten Sie Ihre Client-ID von Ihrer Merkle Vertretung. |
| Merkur Tag | Platzieren Sie den Merkle Merkury Tag auf Ihrer Website. |
| Braze REST und SDK-Endpunkt | Ihre REST- oder SDK-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track, users.export.ids, users.export.segment, and segments.list` Berechtigungen. <br><br>Dieser kann über **Braze-Dashboard > Entwicklungskonsole > REST-API-Schlüssel > Neuen API-Schlüssel erstellen** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Die Anfragen des Merkury Konnektors an Braze bewegen sich im Rahmen der Braze API Rate-Limits. Kontaktieren Sie Braze oder Ihren Merkle Account Manager:in, wenn Sie Fragen haben.<br><br>Merkury sendet mindestens eine Anfrage am Ende einer qualifizierten Sitzung.
{% endalert %}

## Side-by-side-Integration von SDKs

Verwendet den Client-seitigen Merkury Tag von Merkle, um Braze Geräte zu erfassen und leitet sie zur Identifizierung an den Endpunkt des Merkury Identitätskonnektors weiter.

### Schritt 1: Braze Web SDK Tag einrichten

Sie müssen das [Braze Web SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#install-gtm) auf Ihrer Website installiert haben, um diese Integration nutzen zu können.

### Schritt 2: Merkle's Merkury Tag bereitstellen

Setzen Sie den Merkury Tag auf Ihrer Website ein. Dadurch wird der Merkury Konnektor auf Ihrer Website verfügbar. Ein detaillierter Leitfaden mit Anweisungen wird Ihnen von Ihrem Merkle Account Manager:in zur Verfügung gestellt.

### Schritt 3: Angepasste Attribute erstellen

Die folgenden Felder werden vom Merkury Identitätskonnektor ausgefüllt und müssen in Braze als [angepasste Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes#custom-attributes) erstellt werden.

| Attributname | Datentyp | Beschreibung |
| --- | --- | --- |
| `hmid` | String | Merkle's Merkury ID |
| `confidence_score` | Zahl | Wie sicher war Merkury in der Lage zu identifizieren (1-8, niedriger ist besser) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Schritt 4: Versorgen Sie Merkle mit Nutzer:innen-E-Mails

Merkle empfiehlt einen Segmentierungsexport Ihres zulässigen E-Mail Universums. Dies kann durch tägliche Exporte von aktiven zulässigen Nutzer:innen ergänzt werden.

Die folgenden Felder sind erforderlich:

- `braze_id`
- `external_id`
- E-Mail Adresse

Wenden Sie sich für weitere Informationen an Ihre Braze-Vertretung.

