---
nav_title: Verbinden mehrerer Shops
article_title: Shopify Unterstützung mehrerer Shops
alias: /shopify_connecting_multiple_stores/
page_order: 5
description: "Dieser referenzierte Artikel beschreibt, wie Sie mehrere Shopify Shops mit einem einzigen Workspace verbinden und konfigurieren können."
---

# Mehrere Shopify Shops miteinander verbinden

> Verbinden Sie mehrere Shopify Domains mit einem einzigen Workspace, um einen ganzheitlichen Überblick über Ihre Kund:innen in allen Märkten zu erhalten. Erstellen und starten Sie Automatisierungsprogramme und Journeys in einem einzigen Workspace, ohne doppelte Arbeit in den regionalen Shops.  

{% alert important %}
Dieses Feature unterstützt nicht Shopify Markets oder Markets Pro. Wenn Sie Unterstützung für diese Produkte anfordern möchten, senden Sie uns eine [Anfrage zu einem Produkt]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

## Anforderungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Mehrere Shops aktivieren | Wenden Sie sich an Ihren Customer-Success-Manager:in, um die Unterstützung mehrerer Shopify-Shops zu aktivieren. |
| Einen Shopify Shop einrichten | Stellen Sie sicher, dass Sie bereits [mindestens einen Shopify Shop mit Braze]({{site.baseurl}}/shopify_overview/) eingerichtet haben. |
| Eindeutige Shopify Storefront Domains für jede Region | Die Unterstützung mehrerer Shops ist für die Verwendung eindeutiger Shopify Domains für verschiedene regionale Schaufenster gedacht. <br><br>Wenn Sie mehrere Untermarken mit Braze verbinden möchten, empfehlen wir, für jede Untermarke einen eigenen Workspace zu erstellen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Einen zusätzlichen Shop verbinden
Nachdem Sie die Braze App in Ihrem Shopify Shop installiert und Ihren ersten Shop eingerichtet haben, wählen Sie **\+ Neuen Shop verbinden**.

![Der Button "+ Neuen Shop verbinden" auf der Shopify Integrationsseite.]({% image_buster /assets/img/Shopify/begin_setup_button.png %}){: style="max-width:80%;"}

Für Ihren zusätzlichen regionalen Shopify Shop, wählen Sie **Einrichtung beginnen**.

![Der Bereich "Einstellungen für die Integration" mit einem Button zum "Einrichten".]({% image_buster /assets/img/Shopify/multiple_stores.png %}){: style="max-width:80%;"}

Wie bei Ihrer ersten Shopify Integration können Sie zwischen einer Standard- oder angepassten Einrichtung wählen.

!["Enablement der Braze SDKs" mit Optionen zur Implementierung des Braze Internet SDK mit der Standard- oder angepassten Einrichtung.]({% image_buster /assets/img/Shopify/standard_or_custom.png %}){: style="max-width:80%;"}

Wählen Sie die Option, die Ihren Bedürfnissen am besten entspricht:

{% multi_lang_include shopify.md section='Integration Tabs' %}

Um die einzelnen Shop-Integrationen anzuzeigen und fortschrittliche Einstellungen zu konfigurieren, wählen Sie einen Shop im Dropdown-Menü aus.

!["Integrationseinstellungen" mit einem Dropdown-Menü zum Auswählen eines Shopify Shops.]({% image_buster /assets/img/Shopify/store_dropdown_menu.png %})

## Synchronisierung von Nutzer:innen in verschiedenen Shops

### Shopify-Alias

Wenn Sie mehrere Shops verbinden, erhalten synchronisierte Nutzer:innen von Shopify, die sich angemeldet oder eine Bestellung aufgegeben haben, einen neuen Alias im Format: {% raw %}`shopify_customer_id_{{storename}}`{% endraw %}.

### Externe Braze-ID

Für Ihre externe ID von Braze können Sie aus den folgenden Optionen wählen:

|Option|Beschreibung|
|------|-----------|
|Shopify-Kunden-ID|Wenn Sie die Shopify ID als externe ID für Braze verwenden, generiert jeder Shop eine eindeutige Kund:in für jeden Nutzer:innen. Das bedeutet, dass Nutzer:innen, die mit mehreren Shops interagieren, separate Profile in Braze haben.|
|E-Mail, Hash-E-Mail oder angepasste externe ID|Wenn Sie die Typen E-Mail, Hash-E-Mail oder angepasste externe ID verwenden, werden die Profile von Nutzern:innen, die sich in mehreren Shops engagieren, in einem einzigen konsolidierten Profil zusammengefasst, wenn sie sich anmelden oder eine Bestellung aufgeben.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Zusammengeführte Felder

Wenn ein Nutzerprofil synchronisiert wird, werden die folgenden Felder zusammengeführt. Ausführliche Informationen zum Verhalten beim Zusammenführen finden Sie unter [Verhalten beim Zusammenführen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

- Informationen zum Gerät
- Gesamtzahl der Sitzungen (kombiniert aus beiden Profilen)
- Angepasste Event- und Kauf-Event-Daten
- Angepasste Event-Eigenschaften für die Segmentierung (z.B. "X Mal in Y Tagen", wobei X ≤ 50 und Y ≤ 30)
- Anzahl der Ereignisse (kombiniert aus beiden Profilen)
- Datum des ersten und des letzten Ereignisses (Braze wählt das früheste und das späteste Datum aus)
- Daten zur Interaktion mit der Kampagne (jüngste Datumsfelder)
- Workflow-Zusammenfassungen (jüngste Datumsfelder)
- Verlauf der Nachrichten und des Engagements
- Abo-Gruppen

### Sammeln von Abonnent:innen (optional)

Sie können wählen, ob Sie Abonnent:in direkt über Braze (in Ihren Shopify Konnektor-Einstellungen) oder über API- und SDK-Alternativen, die Daten von Shopify synchronisieren, sammeln möchten.

{% tabs local %}
{% tab Shopify Konnektor %}
Im Schritt **Nutzer:innen verwalten** Ihrer Shopify Konnektor-Einstellungen können Sie Braze verwenden, um Opt-ins von E-Mail- und SMS-Abonnenten zu sammeln und sie in einer speziellen Abo-Gruppe zu organisieren:

1. Erstellen Sie für jeden Shop, den Sie verbinden, eine eindeutige Abo-Gruppe. So erhalten Sie genaue Daten darüber, woher die Abonnent:innen kommen.
2. Aktivieren Sie die Erfassung von E-Mail- und SMS-Abonnenten.
{% endtab %}

{% tab Braze API oder SDKs %}
Alternativ können Sie die Opt-in-Informationen für E-Mail- und SMS-Marketing direkt von Shopify aus über die Braze API oder SDKs synchronisieren.

|Option|Ressourcen|
|------|---------|
|API |- [Abo-Gruppen Endpunkte]({{site.baseurl}}/api/endpoints/subscription_groups/), um direkt zu ersetzen, was von der Integration unterstützt wird<br>- [`Users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#set-subscription-groups) zum Festlegen der Daten der Abo-Gruppe oder des [globalen Status des E-Mail-Abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)<br>- [Braze Preference Center]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) für mehr angepasste Opt-in-Optionen für das Marketing|
|SDKs |- [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)<br>- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)<br>- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)<br>- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

## Shopify Daten 

### Synchronisierte Attribute

Wenn Sie mehr als einen Shop verbinden, werden die folgenden Attribute mit dem neuesten Stand des Shopify Profils synchronisiert:
- Vorname
- Nachname
- E-Mail
- Geschlecht
- Geburtsdatum
- Land
- Ort
- Letzte App-Nutzung
- Sprache
- Zeitzone
- shopify_tags
- Anzahl der Shopify-Bestellungen
- Gesamtausgaben in Shopify

### Unterstützte Ereignisse

#### E-Commerce empfohlene Veranstaltungen 

Wenn Sie mehrere Shops miteinander verbinden, enthalten eingehende empfohlene E-Commerce-Ereignisse eine Eigenschaft des Quell-Ereignisses. Diese Eigenschaft gibt an, von welcher Schaufenster-URL das Ereignis stammt, so dass Sie diese Information zur Segmentierung oder zum Triggern bestimmter Anwendungsfälle verwenden können.

![Ein aktionsbasiertes Canvas mit einem Trigger zur Erfassung von Nutzern:innen, die das angepasste Event `ecommerce.order_placed` ausführen.]({% image_buster /assets/img/Shopify/ecommerce_order_placed.png %}){: style="max-width:80%;"}

Die empfohlenen E-Commerce-Ereignisse innerhalb der Shopify Integration sind:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Shopify angepasste Events 

Eingehende angepasste Events von Shopify enthalten eine Eigenschaft namens `shopify_storefront`. Diese Eigenschaft zeigt an, von welcher Schaufenster-URL das Ereignis stammt, so dass Sie sie für die Segmentierung oder das Triggern von Anwendungsfällen nutzen können.

![Ein aktionsbasiertes Canvas mit einem Trigger zur Erfassung von Nutzern:innen, die das angepasste Event `shopify_paid_order` ausführen.]({% image_buster /assets/img/Shopify/shopify_paid_order.png %}){: style="max-width:80%;"}

Zu den unterstützten angepassten Events von Shopify gehören:

- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

Eine vollständige Übersicht über alle Ereignis-Payloads finden Sie unter [Shopify Daten Features]({{site.baseurl}}/shopify_data_features/).

### Shopify Produkte synchronisieren 

Wenn Sie jeden Shopify Shop in Braze verbinden und konfigurieren, können Sie optional die Synchronisierung der Shopify Produkte als Teil der Integration aktivieren.

Wenn Sie die Produktsynchronisierung für jeden Shop aktivieren, nimmt Braze den Namen Ihres Shopify Shops in den Katalognamen auf. So können Sie Produkte aus verschiedenen Shops unterscheiden.

![Shopify-Kataloge mit ihrem Shopify-Shop in ihrem Namen.]({% image_buster /assets/img/Shopify/catalog_store_name.png %})

