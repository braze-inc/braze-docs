---
nav_title: Shopify einrichten
article_title: "Shopify einrichten"
description: "Dieser referenzierte Artikel beschreibt, wie Sie Shopify nach der Integration in Ihr Braze Web SDK einrichten."
page_type: partner
search_tag: Partner
alias: "/shopify_subscription_states/"
alias: "/setting_up_shopify_legacy/"
page_order: 2
---

# Einrichten von Shopify in Braze

> In diesem Artikel erfahren Sie, wie Sie die Integration von Shopify mit Braze abschließen. Folgen Sie diesen Anweisungen, nachdem Sie auf Ihrer Shopify Website [das Braze Web SDK implementiert]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk) haben.

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Shopify Integration in Braze einrichten

### Schritt 1: Verbinden Sie Ihren Shopify Shop

Gehen Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und suchen Sie dann nach "Shopify".

{% alert note %}
Wenn Sie die ältere Navigation verwenden, finden Sie **Technologie Partner** unter **Integrationen**.
{% endalert %}

Wählen Sie auf der Shopify Partnerseite **Gehe zum Shopify App Store**, um die Integration zu starten.

![]({% image_buster /assets/img/Shopify/shop_setup_1.png %}){: style="max-width:70%"}

Sie werden dann zum Shopify App Store weitergeleitet, um die Braze App zu installieren.

{% alert note %}
Wenn Ihr Shopify-Konto mit mehr als einem Shop verknüpft ist, können Sie den Shop, bei dem Sie angemeldet sind, wechseln, indem Sie das Shop-Symbol oben rechts auf der Seite auswählen und " **Shop wechseln"** wählen.
{% endalert %}

![]({% image_buster /assets/img/Shopify/switch_stores.png %}){: style="max-width:30%"}

Nachdem Sie den Shop Ihrer Wahl ausgewählt haben, wählen Sie auf der Seite der Braze App **Installieren**. 

![]({% image_buster /assets/img/Shopify/braze_install.png %}){: style="max-width:70%"}

Nachdem Sie die Braze App installiert haben, werden Sie zu Braze weitergeleitet, um den Workspace zu bestätigen, den Sie mit Shopify verbinden möchten. 

![]({% image_buster /assets/img/Shopify/confirm_workspace.png %}){: style="max-width:50%"}

Nachdem Sie bestätigt haben, dass Sie sich im richtigen Workspace befinden, können Sie die Konfiguration Ihrer Shopify Integration abschließen, indem Sie **Einrichtung beginnen** auswählen.

![]({% image_buster /assets/img/Shopify/begin_setup.png %}){: style="max-width:70%"}

{% alert note %}
Sie können zur Zeit nur einen Shop pro Workspace verbinden. Wenn Sie mehrere Shopify Shops haben, die Sie mit Ihrem Workspace verbinden möchten, wenden Sie sich an Ihren Customer-Success-Manager:in, um mehr über die Shopify Beta für mehrere Shops zu erfahren.
{% endalert %}

### Schritt 2: Ereignisse auswählen und historisches Backfill

Nachdem Sie Ihren Shopify Shop verbunden haben, fahren Sie mit Schritt 2 fort und wählen Sie die Ereignisse aus, die Sie in Ihre Integration einbeziehen möchten. Sie müssen mindestens ein Ereignis auswählen.

![]({% image_buster /assets/img/Shopify/shopify_step_2_events.png %}){: style="max-width:70%"}

Wenn Sie die Ereignisse **"Produkt angesehen"**, **"Produkt angeklickt"** oder **"Warenkorb-Abbruch"** auswählen, benötigen Sie das Braze Web SDK für das Tracking. Wenn Sie das Braze Internet SDK entweder über [Shopify ScriptTag]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=shopify%20scripttag#supported-features) oder direkt auf Ihrer Shopify-Website implementieren [`theme.liquid`]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=theme.liquid#supported-features)implementieren, generiert Braze automatisch die Tracking-Skripte und lädt sie auf Ihre Website. Wenn Sie das Internet SDK auf Ihrer [Shopify-Website]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk) implementieren, müssen Sie das Tracking für diese Ereignisse manuell einschalten. 

#### Historische Daten nachfüllen (optional)

Sie können optional ein Backfill der Käufe der letzten 90 Tage vor Ihrer Installation aktivieren. Durch die automatische Synchronisierung früherer Kunden- und Kaufdaten können Sie sofort mit dem Targeting und Engagement Ihrer Kund:innen beginnen. Wenn Sie mehr darüber erfahren möchten, schauen Sie sich die Shopify Historische Auffüllung an.

![]({% image_buster /assets/img/Shopify/shop_setup_4.png %}){: style="max-width:70%"}

{% alert warning %}
Damit der Backfill die Ereignisse "Order Created" und "Braze Purchase Event" importieren kann, müssen Sie " **Order Created"** und **"Braze Purchase Event"** als Teil Ihrer Integration ausgewählt haben.
{% endalert %}

### Schritt 3: Abonnent:innen sammeln (optional)

Mit der Shopify Integration können Sie E-Mails und SMS Abonnent:innen aus Ihrem Shopify Shop an Braze weiterleiten. Weitere Informationen finden Sie unter [Synchronisierung von Shopify Abonnent:innen]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/#syncing-shopify-subscribers).

![]({% image_buster /assets/img/Shopify/shopify_step_3_email.png %}){: style="max-width:70%"}

### Schritt 4: Einrichten von Shopify-Produktsynchronisationen (optional)

Optional können Sie Ihre Produkte nahezu in Realtime aus Ihrem Shopify Shop in einen Braze Katalog synchronisieren und so den Prozess zur Einbringung von Produktdaten für eine tiefere Personalisierung Ihrer Nachrichten automatisieren. Weitere Informationen finden Sie unter [Shopify Produkt-Synchronisationen]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/).

![]({% image_buster /assets/img/Shopify/shopify_step_4_catalog.png %}){: style="max-width:70%"}

### Schritt 5: Enablement von In-Browser-Nachrichten 

Sie können optional einen zusätzlichen Kanal in Ihrem Shopify Shop für In-Browser-Nachrichten verwenden, indem Sie dieses Feature aktivieren. Dies erlaubt Ihnen, unsere grundlegenden Messaging-Typen wie Slide-up, Modal, Vollbild, einfache Umfragen und angepasstes HTML zu verwenden.

![]({% image_buster /assets/img/Shopify/shopify_step_5_channels.png %}){: style="max-width:70%"}

Wenn Sie In-Browser-Nachrichten aktivieren, muss das Braze Web SDK für das Tracking implementiert werden. Wenn Sie das Braze Internet SDK entweder über [Shopify ScriptTag]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=shopify%20scripttag#supported-features) oder direkt in Ihre Shopify-Website implementieren [`theme.liquid`]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=theme.liquid#supported-features)implementieren, generiert Braze automatisch das grundlegende Skript zur Implementierung von In-Browser-Nachrichten auf Ihrer Website. Wenn Sie das Web SDK auf Ihrer [Shopify-Website]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk) implementieren oder In-Browser-Nachrichten anpassen möchten, müssen Sie In-Browser-Nachrichten mit Hilfe unseres [Entwickler:]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=web)in manuell auf Ihrer Website hinzufügen. 

### Schritt 6: Einrichtung abschließen

Nachdem Sie Ihre Einrichtung konfiguriert haben, wählen Sie **Einrichtung beenden**.

![]({% image_buster /assets/img/Shopify/finish_setup.png %}){: style="max-width:70%"}

Das war's! Der Status "Verbindung ausstehend" wird auf "Verbunden" aktualisiert und zeigt den Zeitstempel an, zu dem die Verbindung hergestellt wurde. Sie sehen auch, ob jedes Shopify Feature auf der Seite erfolgreich aktiviert wurde. 

![]({% image_buster /assets/img/Shopify/shopify_connected_store.png %}){: style="max-width:70%"}

### Erweiterte Einstellungen (optional) 

#### Update der Verzögerungen bei Warenkorb-Abbruch und abgebrochenem Checkout

Standardmäßig setzt Braze die Verzögerung zum Triggern der Ereignisse `shopify_abandoned_checkout` und `shopify_abandoned_cart` automatisch auf eine Stunde Inaktivität. Sie können die **Verzögerung für den Warenkorb-Abbruch** und die **Verzögerung für den Checkout-Abbruch** für jedes Ereignis von 5 Minuten bis zu 24 Stunden einstellen, indem Sie das Dropdown-Menü auswählen und dann auf der Shopify Partnerseite **Verzögerung einstellen** auswählen.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_abandonment.png %}){: style="max-width:30%"}

#### Legen Sie Ihren bevorzugten Bezeichner für das Produkt fest

Wenn Sie die Kauf-Events von Braze in Ihre Shopify Integration integriert haben, setzt Braze standardmäßig die Shopify Produkt ID als `product_id` für das Kauf-Event von Braze ein. Dies wird verwendet, wenn Sie nach Produkten filtern, die in den letzten Y Tagen gekauft wurden, oder wenn Sie den Inhalt Ihrer Nachricht mit Liquid personalisieren.

Sie können auch wählen, ob Sie anstelle der Shopify Product ID die SKU oder den Titel des Produkts aus Shopify angeben möchten.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_productid.png %}){: style="max-width:30%"}

## Fehlersuche

{% details Warum ist die Installation meiner Shopify App noch nicht abgeschlossen? %}
Ihre Installation kann aus einem der folgenden Gründe noch nicht abgeschlossen sein:
 - Wenn Braze Ihre Shopify-Webhooks einrichtet
 - Wenn Braze mit Shopify kommuniziert


Wenn die Installation Ihrer App 1 Stunde lang aussteht, schlägt Braze die Installation fehl und Sie werden aufgefordert, die Installation zu wiederholen.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Warum ist die Installation meiner Shopify App fehlgeschlagen? %}
Ihre Installation kann aus einem der folgenden Gründe fehlgeschlagen sein:
 - Braze konnte Shopify nicht erreichen
 - Braze konnte die Anfrage nicht bearbeiten
 - Ihr Shopify Zugangstoken ist ungültig
 - Die Braze Shopify App wurde von Ihrer Shopify Admin-Seite gelöscht


Sollte dies der Fall sein, können Sie **Setup erneut** auswählen und den Installationsvorgang erneut starten.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Wie deinstalliere ich die Braze Anwendung aus meinem Shopify Shop? %}

Es gibt zwei Möglichkeiten, Braze aus Ihrem Shopify Shop zu deinstallieren:

1. Wählen Sie auf der Shopify Partnerseite **Trennen** aus.<br><br> ![Der Abschnitt "Integration trennen" mit einem Link zum Trennen der Verbindung.]({% image_buster /assets/img/Shopify/disconnect_integration.png %}){: style="max-width:70%;"}

2. Gehen Sie zu Ihrer Shopify-Verwaltungsseite, die sich unter **Apps** befindet. Sie sehen dann eine Option zum Löschen der Braze-Anwendung.<br><br> ![Ein Modal mit der Bitte um Bestätigung, dass Sie die Braze App löschen möchten.]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:70%;"}
{% enddetails %}

{% details Ich habe Schwierigkeiten, meine Nutzer:innen in Einklang zu bringen. Was könnte der Grund dafür sein? %}

Die Art der Unterstützung, die Sie für den Abgleich mit den Nutzer:innen benötigen, hängt davon ab, wie Sie das Internet SDK implementiert haben. Weitere Informationen finden Sie unter [Erste Schritte mit Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/). 

- Wenn Sie eine Shopify-Website ohne Kopfzeile verwenden, lesen Sie bitte den Abschnitt [Implementierung ohne Kopfzeile]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=headless%20shopify%20site#supported-features), um sicherzustellen, dass Sie den Abgleich zwischen Nutzern:innen und Kassen aktiviert haben.
- Wenn Sie auf doppelte Nutzerprofile mit derselben E-Mail oder Telefonnummer stoßen, können Sie die folgenden Braze Tools verwenden, um die doppelten Profile zu einem einzigen Profil zusammenzuführen: 
    - [`users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) Endpunkt
    - [Massenhafte Zusammenführung]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)
- Wenn Sie die ScriptTag Integration verwenden und Ihr Shopify Shop eine "Jetzt kaufen"-Option anbietet, die den Warenkorb überspringt, hat Braze möglicherweise Probleme, Nutzer:innen abzugleichen, da Shopify es nicht zulässt, dass ScriptTags eine `device_id` abrufen, um die Ereignisse einem Nutzer:in zuzuordnen, der den Warenkorb überspringt.

{% enddetails %}
