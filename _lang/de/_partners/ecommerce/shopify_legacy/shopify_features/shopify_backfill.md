---
nav_title: "Shopify Historisches Backfill"
article_title: "Shopify Historisches Backfill"
alias: "/shopify_historical_backfill_legacy/"
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Shopify Historische Backfills einrichten, einschließlich Risiken und unterstützter Daten."
page_type: partner
search_tag: Partner
page_order: 1
---

# Shopify Historisches Backfill 

> Das Shopify Historical Backfill Feature erlaubt es Marken, Kunden- und Kaufdaten automatisiert und nahtlos zu synchronisieren, so dass Sie sofort mit dem Engagement mit einem Ihrer wertvollsten Segmente beginnen können - den Käufern. 

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

Im Rahmen dieses Backfill importiert Braze alle Kund:innen, Bestellungen und Kauf-Events der letzten 90 Tage vor Ihrer Shopify Integration. Beachten Sie, dass dieses Feature ideal für neuere Kund:innen ist, die noch keine aktiven Nachrichten laufen haben, da die Auswirkungen im nächsten Abschnitt erläutert werden. Dieses Feature wird auch auf Ihre Datenpunkt-Nutzung angerechnet.

## Risiken

Mit diesem Feature werden historische Daten und Ereignisse importiert, die zu unbeabsichtigten Konsequenzen führen könnten, wie z.B. dass Nutzer:innen irrelevante und unzeitgemäße Nachrichten für betroffene Kampagnen oder Canvase erhalten. Kampagnen und Canvase, die die folgenden Trigger-Ereignisse verwenden, könnten davon betroffen sein, wenn sie Daten von Shopify verwenden, die mit diesem Feature synchronisiert werden:
- Wert des angepassten Attributs ändern
- Konversions-Event ausführen
- Ausnahme-Event für Kampagne durchführen
- Abo-Status aktualisieren
- Abo-Gruppenstatus aktualisieren
- E-Mail-Adresse hinzufügen
- Kauf tätigen*
- Angepasstes Event* durchführen

{% alert important %}
Wir empfehlen Ihnen, Ihre aktuellen aktiven Kampagnen und Canvase anhand der Daten aus unserem Shopify Historical Backfill auf Nachrichten zu überprüfen, die die oben genannten Ereignisse triggern könnten. 

- Für "Kauf tätigen" und "Angepasstes Event durchführen" können Sie die [Startzeitdauer]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-4-assign-duration) auf ein beliebiges Datum und eine beliebige Uhrzeit aktualisieren, nachdem Ihr Shopify Shop in Braze verbunden wurde. Alle vergangenen Ereignisse vor diesem neuen Startzeitpunkt werden keine Nachrichten triggern. 
- Bei allen anderen oben genannten Ereignissen können Sie diese [vorübergehend stoppen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#stopping-your-campaign), bevor Sie den Backfill aktivieren, um sicherzustellen, dass keine Nachrichten gesendet werden.
{% endalert %}

## Einrichten von Shopify Historical Backfill

### Voraussetzungen

Die folgenden Ereignisse müssen vor dem Einschalten des Backfill aktiviert werden, da ihre Daten sonst nicht importiert werden können:

- `shopify_created_order`
- Braze-Kauf-Event 

Die oben genannten Ereignisse können bei der Einrichtung von Shopify während der [Ereignisauswahl]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#event-selection) aktiviert werden.

{% alert important %}
Sie können das Feature Backfill nur einmal in Ihrer Integration aktivieren.
{% endalert %}

### Schritt 1: Starten Sie den Shopify Backfill-Prozess

Wählen Sie auf der Shopify Partnerseite **Start Data Backfill**. Für bestehende Shopify-Kunden müssen Sie den Zugriff auf Braze neu autorisieren, um alle vergangenen Bestellungsereignisse zu erfassen, bevor Sie mit dem Backfill der Daten beginnen können.

![]({% image_buster /assets/img/Shopify/backfill3.png %}){: style="max-width:75%;"}

### Schritt 2: Umschalten auf das Backfill von Shopify Daten

Als nächstes wird der Setup Composer angezeigt, und Sie können optional das Backfill historischer Shopify Daten aktivieren. Im Rahmen dieses Backfills synchronisiert Braze standardmäßig nur die folgenden Shopify Daten der letzten 90 Tage vor Ihrer Shopify Integration:
- Event „Bestellung erstellt“
- Braze-Kauf-Event
- Kundendaten

Um zu sehen, welche spezifischen Kundendaten rückgefüllt werden, können Sie den Bereich [Unterstützte Shopify Kundendaten](#supported-shopify-customer-data) besuchen.

{% alert note %}
Mit diesem Feature werden nur E-Mail- und SMS-Abos für neue Nutzer:innen synchronisiert, die während des Backfill angelegt wurden. Dadurch werden die Abo-Stati bestehender Nutzer:innen in Braze nicht synchronisiert, um zu vermeiden, dass der aktuelle Status Ihrer Nutzer:innen überschrieben wird.<br><br>Wenn Sie Feedback zum aktuellen Verhalten haben, übermitteln Sie es über das Produktportal, das im **Dashboard** unter **Ressourcen** als **Produkt-Roadmap** aufgeführt ist (Wenn Sie unsere [aktualisierte Navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/) verwenden, wählen Sie **Community** > **Produkt-Roadmap**).
{% endalert %}

Sobald Sie auf **Weiter** klicken, wird der Backfill aktiviert und beginnt mit der Synchronisierung der vergangenen Daten. Beachten Sie, dass der Historische Backfill nur **einmal** abgeschlossen werden kann. Sie können diesen Import also nicht erneut durchführen, nachdem die Daten synchronisiert wurden.

![]({% image_buster /assets/img/Shopify/backfill1.jpg %}){: style="max-width:75%;"}

### Schritt 3: Aufschüttung im Gange

Sie erhalten eine Dashboard-Benachrichtigung, und Ihr Status wird als "In Bearbeitung" angezeigt, um anzuzeigen, dass die Auffüllung begonnen hat. Beachten Sie, dass die Dauer des Backfill-Vorgangs davon abhängt, wie viele Kunden und Bestellungen Braze von Shopify synchronisieren muss. Während dieser Zeit können Sie diese Seite verlassen und auf eine Dashboard-Benachrichtigung oder eine E-Mail warten, die Sie darüber informiert, wann die Aufstockung abgeschlossen ist.

![]({% image_buster /assets/img/Shopify/backfill2.png %}){: style="max-width:75%;"}

### Schritt 4: Aufschüttung abgeschlossen
Sie erhalten eine Dashboard-Benachrichtigung und eine E-Mail, nachdem das Shopify Backfill abgeschlossen ist. Auf der Shopify Partnerseite wird auch der Status unter Historischer Backfill auf "Vollständig" aktualisiert.

## Unterstützte Shopify Kundendaten

### Angepasste Shopify-Attribute

| Attributname | Beschreibung |
| --- | --- |
| `shopify_order_count` | Dieses angepasste Attribut entspricht der Gesamtzahl der Bestellungen, die dieser Kund:in in Shopify getätigt hat. Diese Funktion ist nur für Nutzer:innen verfügbar, die im Rahmen dieses Prozesses wieder aufgefüllt wurden. |
| `shopify_total_spent` | Dieses angepasste Attribut entspricht dem Gesamtbetrag, den dieser Kunde in Shopify ausgegeben hat. Diese Funktion ist nur für Nutzer:innen verfügbar, die im Rahmen dieses Prozesses wieder aufgefüllt wurden. |
| `shopify_tags` | Dieses Attribut entspricht den [Tags der Kund:in](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/using-tags#tag-types), die von Shopify-Administratoren festgelegt wurden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

### Shopify Standard Attribute
- E-Mail
- Vorname
- Nachname
- Telefon
- Ort
- Land

