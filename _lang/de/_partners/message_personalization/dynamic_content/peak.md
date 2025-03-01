---
nav_title: Peak
article_title: Peak
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Peak, einer Plattform für Entscheidungsintelligenz, die es Ihnen ermöglicht, die prognostizierte Abwanderungswahrscheinlichkeit und Attribute auf der Grundlage des Kundenverhaltens und der Interaktionen in Braze zu importieren, um sie für die Kundensegmentierung und das Targeting zu verwenden."
alias: /partners/Peak/
page_type: partner
search_tag: Partner

---

# Peak

> [Peak](https://platform.peak.ai/), eine Plattform für Entscheidungsintelligenz, ist ein End-to-Outcome-System, bei dem Entscheidungsintelligenz die kommerzielle Anwendung von KI ist, um die Entscheidungsfindung in Unternehmen zu verbessern und den Umsatz und Gewinn zu steigern.

Die Partnerschaft zwischen Braze und Peak ermöglicht es Ihnen, die prognostizierte Abwanderungswahrscheinlichkeit und Attribute auf der Grundlage von Kundenverhalten und -interaktionen in Braze zu importieren, um sie für die Kundensegmentierung und das Targeting zu verwenden. 

## Voraussetzungen

Als Ausgangspunkt muss ein Peak-Mieter die Integration zwischen Peak und Braze hosten. Dieser wird traditionell während des Onboardings von Peak-Kunden erstellt. Außerdem ist zunächst eine Lösung für Entscheidungsintelligenz erforderlich, da diese die KI-gesteuerten Ausgaben generiert, die später in Braze integriert werden.

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Spitzenmieter | Eine Instanz der Peak-Plattform, ein sogenannter Tenant, ist erforderlich, um die Integration zu hosten und zu steuern. |
| Decision Intelligence Lösung | Die Integration zwischen Peak und Braze basiert auf KI-gesteuerten Ausgaben und erfordert daher eine von Peak oder einem Kunden bereitgestellte Lösung in Ihrem Tenant. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |

## Integration

Die Peak-Lösung Customer Intelligence nutzt ein Modell zur Vorhersage einer Reihe zukunftsorientierter Attribute auf der Grundlage des Kundenverhaltens und der Kundeninteraktionen. Diese Attribute werden in Peak gespeichert und können verwendet werden, um eine prädiktive Segmentierung zu erstellen, einschließlich der Wahrscheinlichkeit, dass ein Kunde abwandert. Die Aktualisierung dieser prädiktiven Attribute erfolgt in einem konfigurierbaren Rhythmus (täglich oder wöchentlich).

### Schritt 1: Modell ausführen und Kunden extrahieren

Die Integration wird durch die Ausführung des KI-Modells und die Neuberechnung der prädiktiven Kundenattribute ausgelöst. Diese AI-Ausgaben werden in Peak gespeichert, auch wenn ein Attribut mit einem neuen Status oder Wert aktualisiert wird.

Je nachdem, wann die Attribute aktualisiert wurden, wird eine Auswahl durchgeführt, um alle Kunden mit aktualisierten prädiktiven Attributen seit der letzten Synchronisierung zwischen Peak und Braze zu erfassen.

### Schritt 2: Update Braze

Mit den aktualisierten Kunden und den zugehörigen Attributen POSTet Peak diese über den [Endpunkt`/user/track` ][1] unter Verwendung des [Bulk-Headers]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#making-bulk-updates) an Braze.

Beim Empfang erfolgreicher Statuscodes von der API wird Peak die erfolgreiche Synchronisierung zwischen Peak und Braze aufzeichnen.

### Schritt 3: Mit dieser Integration

Sobald die Synchronisierung zwischen Peak und Braze erfolgreich war, enthalten die aktualisierten Benutzer nun die neuen Attribute. Verwenden Sie diese Attribute in Kampagnen und Canvases, um Nutzer anzusprechen und Nachrichten zu personalisieren.

[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/