---
nav_title: "Shopify Historisches Backfill"
article_title: "Shopify Historisches Backfill"
alias: "/shopify_historical_backfill/"
description: "In diesem Referenzartikel erfahren Sie, wie Sie Shopify historische Backfills einrichten, einschließlich Risiken und unterstützter Daten."
page_type: partner
search_tag: Partner
page_order: 1
---

# Shopify Historisches Backfill 

> Die Shopify-Funktion Historical Backfill ermöglicht es Marken, Kunden- und Kaufdaten auf automatisierte und nahtlose Weise zu synchronisieren, damit Sie sofort mit einem Ihrer wertvollsten Segmente - den Käufern - in Kontakt treten können. 

Im Rahmen dieses Backfill importiert Braze alle Kunden, Bestellungen und Kaufereignisse der letzten 90 Tage vor Ihrer Shopify-Integrationsverbindung. Beachten Sie, dass diese Funktion angesichts der im nächsten Abschnitt erläuterten Auswirkungen ideal für neuere Kunden ist, die noch keine aktiven Nachrichten laufen haben. Diese Funktion wird auch auf Ihren Datenpunktverbrauch angerechnet.

## Risiken

Diese Funktion importiert historische Daten und Ereignisse, die zu unbeabsichtigten Konsequenzen führen könnten, wie z.B. dass Benutzer irrelevante und unzeitgemäße Nachrichten für betroffene Kampagnen oder Canvases erhalten. Kampagnen und Canvases, die die folgenden Trigger-Ereignisse verwenden, könnten davon betroffen sein, wenn sie Shopify-Daten verwenden, die mit dieser Funktion synchronisiert werden:
- Wert des Kundenattributs ändern
- Konversions-Event ausführen
- Ausnahmeereignis für Kampagne durchführen
- Abo-Status aktualisieren
- Status der Abonnementgruppe aktualisieren
- Eine E-Mail-Adresse hinzufügen
- Kauf tätigen*
- Benutzerdefiniertes Ereignis durchführen*

{% alert important %}
Wir empfehlen Ihnen, Ihre aktuellen aktiven Kampagnen und Canvases auf Nachrichten zu überprüfen, die die oben genannten Ereignisse auslösen könnten, indem Sie Daten aus unserem Shopify Historical Backfill verwenden. 

- Für "Kauf tätigen" und "Benutzerdefiniertes Ereignis durchführen" können Sie die [Startzeitdauer]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/?redirected=true#step-4-assign-duration) auf ein beliebiges Datum und eine beliebige Uhrzeit aktualisieren, nachdem Ihr Shopify-Shop in Braze verbunden wurde. Alle vergangenen Ereignisse vor dieser neuen Startzeit lösen keine Nachrichten aus. 
- Bei allen anderen oben genannten Ereignissen können Sie diese [vorübergehend stoppen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign), bevor Sie den Backfill aktivieren, um sicherzustellen, dass keine Nachrichten gesendet werden.
{% endalert %}

## Einrichten von Shopify Historical Backfill

### Voraussetzungen

Die folgenden Ereignisse müssen aktiviert werden, bevor Sie das Backfill aktivieren, sonst werden ihre Daten nicht importiert:

- `shopify_created_order`
- Braze Purchase Event 

Die oben genannten Ereignisse können bei der Einrichtung von Shopify während der [Ereignisauswahl]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#event-selection) aktiviert werden.

{% alert important %}
Sie können die Backfill-Funktion nur einmal in Ihrer Integration aktivieren.
{% endalert %}

### Schritt 1: Starten Sie den Shopify Backfill-Prozess

Wählen Sie auf der Shopify-Partnerseite die Option **Start Data Backfill**. Für bestehende Shopify-Kunden müssen Sie den Zugang für Braze neu autorisieren, um alle vergangenen Bestellungsereignisse zu sammeln, bevor Sie mit dem Daten-Backfill beginnen können.

![][3]{: style="max-width:75%;"}

### Schritt 2: Umschalten auf das Backfill von Shopify-Daten

Als Nächstes wird der Setup Composer angezeigt, und Sie können optional das Backfill von historischen Shopify-Daten aktivieren. Als Teil dieses Backfills synchronisiert Braze standardmäßig nur die folgenden Shopify-Daten für die letzten 90 Tage vor Ihrer Shopify-Integration:
- Bestellung Erstellt Ereignis
- Braze Purchase Event
- Kundendaten

Um zu sehen, welche spezifischen Kundendaten rückgefüllt werden, können Sie den Abschnitt [Unterstützte Shopify-Kundendaten](#supported-shopify-customer-data) besuchen.

{% alert note %}
Diese Funktion synchronisiert nur den E-Mail- und SMS-Abonnementstatus für neue Benutzer, die während des Backfill angelegt wurden. Dadurch wird der Abonnementstatus für bestehende Benutzer in Braze nicht synchronisiert, um zu vermeiden, dass der aktuelle Status Ihrer Benutzer überschrieben wird.<br><br>Wenn Sie Feedback zum aktuellen Verhalten haben, übermitteln Sie es über das Produktportal, das im **Dashboard** unter **Ressourcen** als **Produkt-Roadmap** aufgeführt ist (Wenn Sie unsere [aktualisierte Navigation]({{site.baseurl}}/navigation) verwenden, wählen Sie **Community** > **Produkt-Roadmap**).
{% endalert %}

Sobald Sie auf **Weiter** klicken, wird der Backfill aktiviert und beginnt mit der Synchronisierung der vergangenen Daten. Beachten Sie, dass der Historische Backfill nur **einmal** abgeschlossen werden kann. Sie können diesen Import also nicht erneut durchführen, nachdem die Daten synchronisiert wurden.

![][1]{: style="max-width:75%;"}

### Schritt 3: Aufschüttung im Gange

Sie erhalten eine Benachrichtigung auf dem Dashboard, und Ihr Status wird als "In Bearbeitung" angezeigt, um anzuzeigen, dass die Auffüllung begonnen hat. Beachten Sie, dass die Zeit, die für das Backfill benötigt wird, davon abhängt, wie viele Kunden und Bestellungen Braze von Shopify synchronisieren muss. Während dieser Zeit können Sie diese Seite verlassen und auf eine Dashboard-Benachrichtigung oder eine E-Mail warten, die Sie darüber informiert, wann die Auffüllung abgeschlossen ist.

![][2]{: style="max-width:75%;"}

### Schritt 4: Aufschüttung abgeschlossen
Sie erhalten eine Dashboard-Benachrichtigung und eine E-Mail, nachdem der Shopify-Backfill abgeschlossen ist. Auf der Shopify-Partnerseite wird außerdem der Status unter Historisches Backfill auf "Vollständig" aktualisiert.

## Unterstützte Shopify-Kundendaten

### Shopify benutzerdefinierte Attribute

| Attributname | Beschreibung |
| --- | --- |
| `shopify_order_count` | Dieses benutzerdefinierte Attribut entspricht der Gesamtzahl der Bestellungen, die dieser Kunde in Shopify abgeschlossen hat. Diese Funktion ist nur für Benutzer verfügbar, die im Rahmen dieses Prozesses neu angelegt wurden. |
| `shopify_total_spent` | Dieses benutzerdefinierte Attribut entspricht dem Gesamtbetrag, den dieser Kunde in Shopify ausgegeben hat. Diese Funktion ist nur für Benutzer verfügbar, die im Rahmen dieses Prozesses neu angelegt wurden. |
| `shopify_tags` | Dieses Attribut entspricht den von Shopify-Administratoren festgelegten [Kunden-Tags](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

### Shopify Standard-Attribute
- E-Mail
- Vorname
- Nachname
- Tel.
- Ort
- Land

[1]: {% image_buster /assets/img/Shopify/backfill1.jpg %}
[2]: {% image_buster /assets/img/Shopify/backfill2.png %}
[3]: {% image_buster /assets/img/Shopify/backfill3.png %} 
