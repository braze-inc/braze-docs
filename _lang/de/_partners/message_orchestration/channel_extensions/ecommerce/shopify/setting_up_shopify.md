---
nav_title: Shopify einrichten
article_title: "Shopify einrichten"
description: "Dieser Referenzartikel beschreibt, wie Sie Shopify nach der Integration in Ihr Braze Web SDK einrichten."
page_type: partner
search_tag: Partner
alias: "/shopify_subscription_states/"
alias: "/setting_up_shopify/"
page_order: 2
---

# Einrichten von Shopify in Braze

> Dieser Artikel beschreibt, wie Sie die Shopify-Integration mit Braze fertigstellen. Folgen Sie diesen Anweisungen, nachdem Sie [das Braze Web SDK]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk) auf Ihrer Shopify-Website [implementiert]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk) haben.

## Einrichtung der Shopify-Integration in Braze

### Schritt 1: Verbinden Sie Ihren Shopify-Shop

Gehen Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und suchen Sie dann nach "Shopify".

{% alert note %}
Wenn Sie die ältere Navigation verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Wählen Sie auf der Shopify-Partnerseite die Option **Zum Shopify App Store gehen**, um den Integrationsprozess zu starten.

![]({% image_buster /assets/img/Shopify/shop_setup_1.png %}){: style="max-width:70%"}

Sie werden dann zum Shopify App Store weitergeleitet, um die Braze-App zu installieren.

{% alert note %}
Wenn Ihr Shopify-Konto mit mehr als einem Shop verbunden ist, können Sie den Shop, bei dem Sie angemeldet sind, wechseln, indem Sie auf das Shop-Symbol oben rechts auf der Seite klicken und " **Shop wechseln"** wählen.
{% endalert %}

![]({% image_buster /assets/img/Shopify/switch_stores.png %}){: style="max-width:30%"}

Nachdem Sie den gewünschten Shop ausgewählt haben, wählen Sie auf der Seite der Braze-App die Option **Installieren**. 

![]({% image_buster /assets/img/Shopify/braze_install.png %}){: style="max-width:70%"}

Nachdem Sie die Braze-App installiert haben, werden Sie zu Braze weitergeleitet, um den Arbeitsbereich zu bestätigen, den Sie mit Shopify verbinden möchten. 

![]({% image_buster /assets/img/Shopify/confirm_workspace.png %}){: style="max-width:50%"}

Nachdem Sie sich vergewissert haben, dass Sie sich im richtigen Arbeitsbereich befinden, können Sie die Konfiguration Ihrer Shopify-Integration abschließen, indem Sie **Einrichtung beginnen** wählen.

![]({% image_buster /assets/img/Shopify/begin_setup.png %}){: style="max-width:70%"}

{% alert note %}
Sie können zur Zeit nur einen Shop pro Arbeitsbereich verbinden. Wenn Sie mehrere Shopify-Shops haben, die Sie mit Ihrem Arbeitsbereich verbinden möchten, wenden Sie sich an Ihren Kundenerfolgsmanager, um Einzelheiten über die Shopify-Beta für mehrere Shops zu erfahren.
{% endalert %}

### Schritt 2: Wählen Sie Ereignisse und historische Hintergrundinformationen

Nachdem Sie Ihren Shopify-Shop verbunden haben, fahren Sie mit Schritt 2 fort und wählen die Ereignisse aus, die Sie in Ihre Integration aufnehmen möchten. Sie müssen mindestens ein Ereignis auswählen.

![]({% image_buster /assets/img/Shopify/shopify_step_2_events.png %}){: style="max-width:70%"}

Wenn Sie die Ereignisse **Product Viewed**, **Product Clicked** oder **Abandoned Cart** auswählen, benötigen Sie das Braze Web SDK für die Nachverfolgung. Wenn Sie das Braze Web SDK entweder über [Shopify ScriptTag]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=shopify%20scripttag#supported-features) oder direkt auf Ihrer Shopify-Website implementieren [`theme.liquid`]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=theme.liquid#supported-features)implementieren, generiert Braze automatisch die Tracking-Skripte und lädt sie auf Ihre Website. Wenn Sie das Web SDK auf Ihrer [Shopify-Website]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk) implementieren, müssen Sie das Tracking für diese Ereignisse manuell einschalten. 

#### Historische Daten verfüllen (optional)

Sie können optional einen Backfill der Käufe der letzten 90 Tage vor Ihrer Installation aktivieren. Durch die automatische Synchronisierung früherer Kunden- und Kaufdaten können Sie sofort damit beginnen, Ihre Kunden gezielt anzusprechen und mit ihnen in Kontakt zu treten. Wenn Sie mehr darüber erfahren möchten, lesen Sie Shopify historical backfill.

![]({% image_buster /assets/img/Shopify/shop_setup_4.png %}){: style="max-width:70%"}

{% alert warning %}
Damit der Backfill die Ereignisse "Order Created" und "Braze Purchase" importieren kann, müssen Sie " **Order Created"** und **"Braze Purchase"** als Teil Ihrer Integration ausgewählt haben.
{% endalert %}

### Schritt 3: Abonnenten sammeln (optional)

Mit der Shopify-Integration können Sie E-Mail- und SMS-Abonnenten aus Ihrem Shopify-Shop in Braze sammeln. Weitere Informationen finden Sie unter [Synchronisierung von Shopify-Abonnenten]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/#syncing-shopify-subscribers).

![]({% image_buster /assets/img/Shopify/shopify_step_3_email.png %}){: style="max-width:70%"}

### Schritt 4: Einrichten von Shopify-Produktsynchronisationen (optional)

Optional können Sie Ihre Produkte nahezu in Echtzeit aus Ihrem Shopify-Shop in einen Braze-Katalog synchronisieren und so den Prozess zur Einbringung von Produktdaten für eine bessere Personalisierung Ihrer Nachrichten automatisieren. Weitere Informationen finden Sie unter [Shopify-Produktsynchronisationen]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_catalogs/).

![]({% image_buster /assets/img/Shopify/shopify_step_4_catalog.png %}){: style="max-width:70%"}

### Schritt 5: Aktivieren Sie In-Browser-Nachrichten 

Sie können optional einen zusätzlichen Kanal in Ihrem Shopify-Shop für In-Browser-Nachrichten verwenden, indem Sie diese Funktion aktivieren. Damit können Sie unsere grundlegenden Nachrichtentypen wie Slide-up, Modal, Vollbild, einfache Umfragen und benutzerdefiniertes HTML verwenden.

![]({% image_buster /assets/img/Shopify/shopify_step_5_channels.png %}){: style="max-width:70%"}

Wenn Sie In-Browser-Meldungen aktivieren, muss das Braze Web SDK für das Tracking implementiert werden. Wenn Sie das Braze Web SDK entweder über [Shopify ScriptTag]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=shopify%20scripttag#supported-features) oder direkt auf Ihrer Shopify-Website implementieren [`theme.liquid`]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=theme.liquid#supported-features)implementieren, generiert Braze automatisch das grundlegende Skript für die Implementierung von Nachrichten im Browser auf Ihrer Website. Wenn Sie das Web SDK auf Ihrer [Shopify-Website]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk) implementieren oder Anpassungen an In-Browser-Nachrichten vornehmen möchten, müssen Sie In-Browser-Nachrichten manuell mit Hilfe unseres [Entwicklerhandbuchs](/developer_guide/platform_integration_guides/web/in-app_messaging/integration/) zu Ihrer Website hinzufügen. 

### Schritt 6: Einrichtung beenden

Nachdem Sie Ihre Einrichtung konfiguriert haben, wählen Sie **Einrichtung beenden**.

![]({% image_buster /assets/img/Shopify/finish_setup.png %}){: style="max-width:70%"}

Das war's! Der Status "Verbindung ausstehend" wird auf "Verbunden" aktualisiert und zeigt den Zeitstempel an, zu dem die Verbindung hergestellt wurde. Sie sehen auch, ob die einzelnen Shopify-Funktionen auf der Seite erfolgreich aktiviert wurden. 

![]({% image_buster /assets/img/Shopify/shopify_connected_store.png %}){: style="max-width:70%"}

### Erweiterte Einstellungen (optional) 

#### Aktualisieren Sie Verzögerungen bei abgebrochenen Warenkörben und abgebrochenen Transaktionen

Standardmäßig setzt Braze die Verzögerung für die Auslösung der Ereignisse `shopify_abandoned_checkout` und `shopify_abandoned_cart` automatisch auf eine Stunde Inaktivität. Sie können die **Verzögerung für abgebrochene Warenkörbe** und **abgebrochene Bestellungen** für jedes Ereignis von 5 Minuten bis zu 24 Stunden einstellen, indem Sie das Dropdown-Menü auswählen und dann auf der Shopify-Partnerseite **Verzögerung einstellen** wählen.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_abandonment.png %}){: style="max-width:30%"}

#### Legen Sie Ihren bevorzugten Produktidentifikator fest

Wenn Sie Braze-Einkaufsereignisse in Ihre Shopify-Integrationseinrichtung aufgenommen haben, legt Braze standardmäßig die Shopify-Produkt-ID als `product_id` fest, die innerhalb des Braze-Einkaufsereignisses verwendet wird. Dies wird verwendet, wenn Sie nach Produkten filtern, die in Y Tagen gekauft wurden, oder den Inhalt Ihrer Nachricht mit Liquid personalisieren.

Sie können auch wählen, ob Sie anstelle der Shopify-Produkt-ID die SKU oder den Produkttitel aus Shopify angeben möchten.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_productid.png %}){: style="max-width:30%"}

## Fehlersuche

{% details Warum ist die Installation meiner Shopify-App noch nicht abgeschlossen? %}
Ihre Installation kann aus einem der folgenden Gründe noch nicht abgeschlossen sein:
 - Wenn Braze Ihre Shopify-Webhooks einrichtet
 - Wenn Braze mit Shopify kommuniziert


Wenn Ihre App-Installation 1 Stunde lang aussteht, schlägt Braze die Installation fehl und Sie werden aufgefordert, die Installation zu wiederholen.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Warum ist die Installation meiner Shopify-App fehlgeschlagen? %}
Ihre Installation kann aus einem der folgenden Gründe fehlgeschlagen sein:
 - Braze konnte Shopify nicht erreichen
 - Braze konnte die Anfrage nicht bearbeiten
 - Ihr Shopify-Zugangs-Token ist ungültig
 - Die Braze Shopify-App wurde von Ihrer Shopify-Verwaltungsseite gelöscht


In diesem Fall können Sie die Option **Installation wiederholen** wählen und den Installationsvorgang erneut starten.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details Wie deinstalliere ich die Braze-Anwendung aus meinem Shopify-Shop? %}

Es gibt zwei Möglichkeiten, Braze aus Ihrem Shopify-Shop zu deinstallieren:

1. Wählen Sie auf der Shopify-Partnerseite **Trennen**.<br><br> ![Der Abschnitt "Integration trennen" mit einem Link zum Trennen der Verbindung.]({% image_buster /assets/img/Shopify/disconnect_integration.png %}){: style="max-width:70%;"}

2. Gehen Sie zu Ihrer Shopify-Verwaltungsseite, die Sie unter **Apps** finden. Sie sehen dann eine Option zum Löschen der Braze-Anwendung.<br><br> ![Ein Modal mit der Bitte um Bestätigung, dass Sie die Braze-App löschen möchten.]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:70%;"}
{% enddetails %}

{% details Ich kämpfe damit, meine Benutzer unter einen Hut zu bringen. Was könnte der Grund dafür sein? %}

Die Art der Unterstützung, die Sie für den Benutzerabgleich benötigen, hängt davon ab, wie Sie das Web SDK implementiert haben. Weitere Informationen finden Sie unter [Erste Schritte mit Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/). 

- Wenn Sie eine Shopify-Website ohne Kopfzeile verwenden, überprüfen Sie die [Headless-Implementierung]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=headless%20shopify%20site#supported-features), um sicherzugehen, dass Sie den Abgleich mit den Benutzern an der Kasse aktiviert haben.
- Wenn Sie auf doppelte Benutzerprofile mit derselben E-Mail oder Telefonnummer stoßen, können Sie die folgenden Braze-Tools verwenden, um die Duplikate in einem Profil zusammenzuführen: 
    - [`users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) Endpunkt
    - [Massenhafte Zusammenführung]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)
- Wenn Sie die ScriptTag-Integration verwenden und Ihr Shopify-Shop eine "Jetzt kaufen"-Option anbietet, bei der der Warenkorb übersprungen wird, hat Braze möglicherweise Schwierigkeiten, die Benutzer abzugleichen, da Shopify es nicht zulässt, dass ScriptTags eine `device_id` abrufen, um die Ereignisse einem Benutzer zuzuordnen, der den Warenkorb überspringt.

{% enddetails %}