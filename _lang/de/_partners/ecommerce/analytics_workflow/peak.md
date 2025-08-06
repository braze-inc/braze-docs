---
nav_title: Peak
article_title: Peak
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Peak, einer Plattform für Entscheidungsintelligenz, die es Ihnen erlaubt, voraussichtliche Abwanderungswahrscheinlichkeiten und Attribute, die auf Kundenverhalten und -interaktionen basieren, in Braze zu importieren, um sie für die Segmentierung und das Targeting von Kunden zu verwenden."
alias: /partners/Peak/
page_type: partner
search_tag: Partner

---

# Peak

> [Peak](https://platform.peak.ai/), eine Plattform für Entscheidungsintelligenz, ist ein End-to-Outcome-System, bei dem Entscheidungsintelligenz die kommerzielle Anwendung von KI ist, um die Entscheidungsfindung in Unternehmen zu verbessern und Umsätze und Gewinne zu steigern.

_Diese Integration wird von Peak gepflegt._

## Über die Integration

Die Partnerschaft zwischen Braze und Peak erlaubt es Ihnen, voraussichtliche Abwanderungswahrscheinlichkeiten und Attribute, die auf Kundenverhalten und -interaktionen basieren, in Braze zu importieren, um sie für die Segmentierung und das Targeting von Kunden zu verwenden. 

## Voraussetzungen

Als Ausgangspunkt muss ein Peak-Mieter die Integration zwischen Peak und Braze hosten. Diese wird traditionell während des Onboarding von Peak Kund:in erstellt. Darüber hinaus ist zunächst eine Lösung für Entscheidungsintelligenz erforderlich, da diese die KI-gesteuerten Ausgaben generiert, die später in Braze integriert werden sollen.

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Spitzenmieter | Für das Hosting und die Orchestrierung der Integration ist eine Instanz der Peak-Plattform, ein sogenannter Tenant, erforderlich. |
| Decision Intelligence Lösung | Die Integration zwischen Peak und Braze basiert auf KI-gesteuerten Ausgaben und erfordert daher eine von Peak oder Kund:in bereitgestellte Lösung innerhalb Ihres Tenants. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |

## Integration

Die Peak Lösung Customer Intelligence nutzt ein Modell zur Prognose einer Reihe zukunftsorientierter Attribute auf der Grundlage des Kundenverhaltens und der Interaktionen mit den Kunden. Diese Attribute werden in Peak gespeichert und können für eine vorausschauende Segmentierung verwendet werden, einschließlich der Wahrscheinlichkeit, dass ein Kunde abwandert. Die Aktualisierung dieser prognostischen Attribute erfolgt in einem konfigurierbaren Rhythmus (täglich oder wöchentlich).

### Schritt 1: Modell ausführen und Kunden:in extrahieren

Die Integration wird durch den Lauf des KI-Modells und die Neuberechnung der prognostizierten Attribute der Kund:in ausgelöst. Diese KI-Ausgaben werden in Peak gespeichert, auch wenn ein Attribut mit einem neuen Status oder Wert aktualisiert wird.

Basierend darauf, wann Attribute aktualisiert wurden, wird eine Auswahl getroffen, um alle Kund:innen mit angepassten prognostischen Attributen seit der letzten Synchronisierung zwischen Peak und Braze zu sammeln.

### Schritt 2: Update Braze

Mit den aktualisierten Kund:in und den dazugehörigen Attributen wird Peak diese über den [Endpunkt`/user/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) unter Verwendung des [Bulk-Headers]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#making-bulk-updates) an Braze posten.

Bei Erhalt erfolgreicher Statuscodes von der API wird Peak die erfolgreiche Synchronisierung zwischen Peak und Braze aufzeichnen.

### Schritt 3: Verwendung dieser Integration

Sobald die Synchronisierung zwischen Peak und Braze erfolgreich war, enthalten die aktualisierten Nutzer:innen nun die neuen Attribute. Verwenden Sie diese Attribute in Kampagnen und Canvase, um Nutzer:innen anzusprechen und Nachrichten zu personalisieren.


