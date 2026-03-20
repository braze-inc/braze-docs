---
page_order: 2.0
nav_title: Rate-Limits
article_title: Braze SDK-Rate-Limits
description: "Erfahren Sie mehr über das intelligente, clientseitige Rate-Limiting des Braze SDK, das die Akkulaufzeit optimiert, die Bandbreitennutzung reduziert und eine zuverlässige Zustellung der Daten gewährleistet."
---

# Braze SDK-Rate-Limits

> Erfahren Sie mehr über das intelligente, clientseitige Rate-Limiting des Braze SDK, das die Akkulaufzeit optimiert, die Bandbreitennutzung reduziert und eine zuverlässige Zustellung der Daten gewährleistet.

## SDK-Rate-Limits verstehen

Das Rate-Limiting des Braze SDK nutzt die folgenden Features, um die Performance zu optimieren, den Batterieverbrauch zu minimieren, die Datennutzung zu reduzieren und eine zuverlässige Zustellung der Daten zu gewährleisten:

### Asynchrone Verarbeitung

Das Braze SDK verwendet einen Token-Bucket-Algorithmus für Rate-Limiting. Dieser Ansatz ermöglicht Aktivitätsschübe bei gleichzeitiger Aufrechterhaltung einer langfristigen Ratenkontrolle. Anstatt Anfragen in einer strengen Warteschlange zu verarbeiten, arbeitet der Token-Bucket asynchron:

- **Token-Generierung**: Die Token werden kontinuierlich in den Bucket nachgefüllt.
- **Bearbeitung von Anfragen**: Jeder SDK-Aufruf, der eingeht, wenn ein Token verfügbar ist, wird sofort ausgeführt, unabhängig davon, wann andere Aufrufe eingegangen sind.
- **Keine strenge Reihenfolge**: Anfragen warten nicht in einer Warteschlange; mehrere Aufrufe können um das nächste verfügbare Token konkurrieren.
- **Burst-Verarbeitung**: Kurze Aktivitätsausbrüche sind zulässig, sofern zum Zeitpunkt der Anfragen ausreichend Token verfügbar sind.
- **Ratenkontrolle**: Der langfristige Durchsatz wird durch die konstante Nachfüllrate der Token begrenzt.

Dieser asynchrone Ablauf unterstützt das SDK dabei, schnell auf die verfügbare Netzwerkkapazität zu reagieren und gleichzeitig ein vorhersehbares Gesamtverkehrsaufkommen aufrechtzuerhalten.

### Adaptives Rate-Limiting

Das Braze SDK kann Rate-Limits in Echtzeit anpassen, um die Netzwerk-Infrastruktur zu schützen und eine optimale Performance aufrechtzuerhalten. Dieser Ansatz:

- **Verhindert Überlastung**: Passt die Limits an, um Netzwerküberlastungen zu vermeiden.
- **Optimiert die Performance**: Gewährleistet einen reibungslosen Betrieb des SDK unter unterschiedlichen Bedingungen.
- **Reagiert auf Bedingungen**: Passt sich an das aktuelle Netzwerk und die Nutzungsmuster an.

{% alert note %}
Da sich die Limits in Echtzeit anpassen, werden keine genauen Bucket-Größen und statischen Werte angegeben. Diese können sich je nach Netzwerkbedingungen und Nutzung ändern.
{% endalert %}

### Netzwerkoptimierungen

Das Braze SDK enthält mehrere integrierte Funktionen zur Verbesserung der Effizienz, zur Reduzierung des Batterieverbrauchs und zur Bewältigung unterschiedlicher Netzwerkbedingungen:

- **Automatische Bündelung**: Stellt Ereignisse in eine Warteschlange und sendet sie in effizienten Stapeln.
- **Netzwerkbewusstes Verhalten**: Passt die Flush-Raten basierend auf der Verbindungsqualität an.
- **Batterieoptimierung**: Minimiert Funkaktivierungen und Netzwerkaufrufe.
- **Graceful Degradation**: Gewährleistet die Funktionalität auch bei schlechten Netzwerkbedingungen.
- **Hintergrund-/Vordergrund-Erkennung**: Optimiert das Verhalten, wenn sich der Lebenszyklus der App ändert.

## Best Practices

Befolgen Sie diese Best Practices, um Probleme mit Rate-Limits zu vermeiden:

| Empfohlen | Nicht empfohlen |
| --- | --- |
| Verfolgen Sie relevante Nutzeraktionen und Meilensteine | Verfolgen Sie jede kleine Interaktion oder jedes UI-Ereignis |
| Aktualisieren Sie Inhalte nur bei Bedarf | Aktualisieren Sie Inhalte bei jeder Nutzeraktion (z. B. bei Scroll-Ereignissen) |
| Lassen Sie das SDK die Stapelverarbeitung automatisch durchführen | Erzwingen Sie eine sofortige Übertragung der Daten (sofern nicht unbedingt erforderlich) |
| Konzentrieren Sie sich auf Ereignisse, die einen Mehrwert für Analytics bieten | Rufen Sie SDK-Methoden in schneller Folge auf, ohne die Häufigkeit zu berücksichtigen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Hilfe erhalten

Sollten Sie Probleme mit den SDK-Rate-Limits haben, überprüfen Sie bitte die folgenden Netzwerkmethoden:

- `requestImmediateDataFlush()`
- `requestContentCardsRefresh()`
- `refreshFeatureFlags()`
- `logCustomEvent()`
- `logPurchase()`

Wenn Sie den [Braze Support]({{site.baseurl}}/user_guide/administrative/access_braze/support) kontaktieren, geben Sie bitte die folgenden Details für jede der von Ihnen verwendeten Netzwerk-SDK-Methoden an:

```plaintext
Method name:

Frequency:
[Describe how often this is called, e.g., at every app launch, once per session]

Trigger/context:
[Describe what causes it to be called, e.g., button click, scroll event]

Code snippet:  
[Paste the exact code where this method is called, one snippet for each time it is called]

Patterns in user flow that may cause bursts or excessive calls:
[Describe here]
```
