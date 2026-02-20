---
page_order: 2.0
nav_title: Rate-Limits
article_title: Braze SDK Rate-Limits
description: "Erfahren Sie mehr über das intelligente, Client-seitige Rate-Limiting des Braze SDK, das die Akkulaufzeit optimiert, die Bandbreitennutzung reduziert und eine zuverlässige Zustellung der Daten gewährleistet."
---

# Braze SDK Rate-Limits

> Erfahren Sie mehr über das intelligente, Client-seitige Rate-Limiting des Braze SDK, das die Akkulaufzeit optimiert, die Bandbreitennutzung reduziert und eine zuverlässige Zustellung der Daten gewährleistet.

## Verständnis der SDK Rate-Limits

Braze SDK Rate-Limiting nutzt die folgenden Features, um die Performance zu optimieren, den Akkuverbrauch zu minimieren, die Datennutzung zu reduzieren und eine zuverlässige Zustellung der Daten zu gewährleisten:

### Asynchrone Verarbeitung

Das Braze SDK verwendet einen Token Bucket-Algorithmus für Rate-Limiting. Dieser Ansatz ist zulässig, wenn die Aktivität sprunghaft ansteigt und gleichzeitig die langfristige Kontrolle der Rate beibehalten wird. Anstatt Anfragen in einer strengen Warteschlange zu verarbeiten, arbeitet der Token Bucket asynchron:

- **Token-Generierung**: Token werden in gleichmäßigem Rhythmus in den Bucket nachgefüllt.
- **Bearbeitung von Anfragen**: Jeder SDK-Aufruf, der eintrifft, wenn ein Token verfügbar ist, wird sofort ausgeführt, unabhängig davon, wann andere Aufrufe eintreffen.
- **Keine strenge Reihenfolge**: Anfragen warten nicht in der Schlange; mehrere Anfragen können um den nächsten verfügbaren Token konkurrieren.
- **Burst-Behandlung**: Kurze Ausbrüche von Aktivitäten sind zulässig, wenn zum Zeitpunkt der Anfragen genügend Token verfügbar sind.
- **Ratenkontrolle**: Der langfristige Durchsatz wird durch die konstante Token-Nachfüllrate begrenzt.

Dieser asynchrone Fluss hilft dem SDK, schnell auf die verfügbare Netzwerkkapazität zu reagieren und gleichzeitig ein vorhersehbares Gesamtverkehrsaufkommen beizubehalten.

### Adaptives Rate-Limiting

Das Braze SDK kann Rate-Limits in Realtime anpassen, um die Infrastruktur des Netzwerks zu schützen und eine optimale Performance zu gewährleisten. Dieser Ansatz:

- **Verhindert Überlastung**: Passt die Grenzen an, um eine Überlastung des Netzwerks zu vermeiden.
- **Optimiert die Performance**: Sorgt für einen reibungslosen SDK-Betrieb unter wechselnden Bedingungen.
- **Reagiert auf Bedingungen**: Passt sich basierend auf dem aktuellen Netzwerk und dem Nutzungsverhalten an.

{% alert note %}
Da sich die Limits in Echtzeit anpassen, werden keine genauen Bucket-Größen und statischen Werte angegeben. Sie können sich je nach Netzwerkbedingungen und Nutzung ändern.
{% endalert %}

### Optimierungen bei der Vernetzung

Das Braze SDK enthält mehrere integrierte Verhaltensweisen, um die Effizienz zu verbessern, den Akkuverbrauch zu reduzieren und mit unterschiedlichen Netzwerkbedingungen umzugehen:

- **Automatische Dosierung**: Stellt Ereignisse in eine Warteschlange und sendet sie in effizienten Stapeln.
- **Netzwerkfähiges Verhalten**: Passt die Spülrate an die Qualität der Verbindung an.
- **Akku-Optimierung**: Minimiert das Aufwachen des Radios und Netzanrufe.
- **Anmutige Degradierung**: Erhält die Funktionalität bei schlechten Netzwerkbedingungen aufrecht.
- **Hintergrund-/Vordergrundbewusstsein**: Optimiert das Verhalten, wenn sich der Lebenszyklus der App ändert.

## Bewährte Praktiken

Befolgen Sie diese bewährten Methoden, um Probleme mit Rate-Limits zu vermeiden:

| Tun Sie dies | Nicht das |
| --- | --- |
| Tracking sinnvoller Nutzer:innen-Aktionen und Meilensteine | Tracking jeder kleinen Interaktion oder jedes UI-Ereignisses |
| Inhalte nur bei Bedarf aktualisieren | Aktualisieren Sie den Inhalt bei jeder Nutzer:in-Aktion (z.B. Scroll-Ereignisse) |
| Lassen Sie das SDK das Batching automatisch erledigen | Erzwingen Sie die sofortige Übertragung von Daten (es sei denn, dies ist unbedingt erforderlich) |
| Konzentrieren Sie sich auf Ereignisse, die einen Mehrwert für Analytics bieten | SDK-Methoden in schneller Folge aufrufen, ohne die Häufigkeit zu berücksichtigen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Hilfe holen

Wenn Sie Probleme mit den Rate-Limits des SDK haben, sollten Sie die folgenden Netzwerkmethoden prüfen:

- `requestImmediateDataFlush()`
- `requestContentCardsRefresh()`
- `refreshFeatureFlags()`
- `logCustomEvent()`
- `logPurchase()`

Wenn Sie sich an [support@braze.com](mailto:support@braze.com) wenden, geben Sie bitte die folgenden Details für jede der von Ihnen verwendeten SDK-Methoden für Netzwerke an:

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
