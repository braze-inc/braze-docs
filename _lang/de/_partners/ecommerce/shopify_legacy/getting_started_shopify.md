---
nav_title: Erste Schritte
article_title: "Erste Schritte mit Shopify"
description: "Dieser referenzierte Artikel beschreibt, wie Sie das Braze Web SDK auf Ihrer Shopify Website implementieren."
page_type: partner
search_tag: Partner
alias: /getting_started_shopify_legacy/
page_order: 1
---

# Erste Schritte mit Shopify

> In diesem Artikel erfahren Sie, wie Sie das Braze Web SDK auf Ihrer Shopify Website implementieren. Nach der Implementierung lesen Sie [Shopify einrichten]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview), um zu erfahren, wie Sie die Integration von Shopify mit Braze abschließen.

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Checkliste für die Einrichtung der Integration

1. [Implementieren Sie das Braze Web SDK](#implement-web-sdk)
2. [Shopify in Braze einrichten]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview)
3. Testen Sie die Shopify Integration

## Implementierung des Internet SDK auf Ihrer Shopify Website {#implement-web-sdk}

Das [Braze Web SDK]({{site.baseurl}}/user_guide/getting_started/web_sdk/) ist ein leistungsstarkes Tool, mit dem Sie das Tracking des Kundenverhaltens in Ihrem Shopify Shop durchführen können. Mit dem Web SDK können Sie Sitzungsdaten sammeln, Nutzer:innen identifizieren und Daten zum Nutzerverhalten von einem Web- oder Mobilbrowser aufzeichnen. Sie können auch native Messaging-Kanäle wie In-Browser-Nachrichten freischalten.

Obwohl die Shopify-Integration eine Reihe von Standard-Features bietet, sollten Sie bedenken, dass Sie das Internet SDK direkt auf Ihrer Shopify-Website implementieren müssen, wenn Sie Anwendungsfälle für das Tracking von [Ereignissen, die nicht von der Shopify-Integration unterstützt werden,]({{site.baseurl}}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/) oder Kanäle wie [Content-Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) hinzufügen möchten.

Bevor Sie mit dem Onboarding der Integration beginnen, besprechen Sie bitte mit Ihrem Team, welchen Weg Sie für die Implementierung des Internet SDK einschlagen möchten.

### Unterstützte Funktionen

|Symbol| Definition 
|-------------|-------------
|<i aria-hidden="true" class="fas fa-check" title="Unterstützt"></i><span class="sr-only">Unterstützt</span> | Unterstützt
|<i aria-hidden="true" class="fas fa-times" title="Nicht unterstützt"></i><span class="sr-only">Unterstützt</span> | Nicht unterstützt
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

| Features | Internet SDK über Shopify ScriptTag | Direkte Web SDK-Integration über theme.liquid | Direkte Web SDK-Integration über Shopify Hydrogen
|-------------|-------------|-------------|------------
| Standard Tracking vor Ort      | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i>          
| Erfassen des Abgleichs von Nutzer:innen (geringer technischer Aufwand erforderlich)   | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> 
| Abgleich der Nutzer:innen an der Kasse     | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-times" title="Nicht unterstützt"></i>   | <i class="fas fa-times" title="Nicht unterstützt"></i>                                        
| Angesehenes Produkt<br> Produkt geklickt<br> Warenkorb-Abbruch   | <i class="fas fa-check" title="Unterstützt"></i> |<i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> 
| Abgebrochene Kasse<br> Erstellter Auftrag<br> Braze Kaufen<br> Bestellung bezahlt<br> Teilweise erfüllte Bestellung<br> Erfüllte Bestellung<br> Stornierte Bestellung<br> Erstellt Erstattung<br> Kund:in erstellen & aktualisieren | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i>
| Historische Verfüllung | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-check" title="Unterstützt"></i>  
| Katalog synchronisieren  |<i class="fas fa-check" title="Unterstützt"></i> |<i class="fas fa-check" title="Unterstützt"></i>  |<i class="fas fa-check" title="Unterstützt"></i>
| E-Mail- und SMS-Abonnentenerfassung    | <i class="fas fa-check" title="Unterstützt"></i>| <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-check" title="Unterstützt"></i>     
| Standardmäßige Unterstützung von In-App-Nachrichten   | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-times" title="Nicht unterstützt"></i>     
| Standard Content-Cards Unterstützung   | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i>   
| Standard Web-Push Unterstützung     | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }    

{% tabs %}
{% tab Shopify ScriptTag %}

### Implementierung des Braze Web SDK über Shopify ScriptTag

[Shopify ScriptTag](https://shopify.dev/api/admin-rest/2021-10/resources/scripttag#top) ist ein dezentraler JavaScript Code, der in die Seiten Ihres Shops oder in die Bestellstatus-Seite der Kasse geladen wird. Wenn eine Shop-Seite geladen wird, prüft Shopify, ob Skript-Tags in die Site-Seite geladen werden müssen. 

Wenn Sie schnell mit Braze beginnen möchten, haben Sie die Möglichkeit, Braze zu erlauben, ein vordefiniertes Skript für das Braze Web SDK direkt auf Ihre Shopify-Website zu laden.

{% alert important %}
Das vordefinierte Skript für das Braze Web SDK für diese Integrationsmethode ist nicht anpassbar.
{% endalert %}

#### So funktioniert es mit der Shopify Integration

Wenn Ihre Shopify Website geladen wird, prüft Shopify, ob Skript-Tags in die Seite geladen werden müssen. Während des Prozesses werden die Skripte des Braze Web SDK auf die Seiten Ihres Shops oder auf die Bestellstatusseite der Kasse geladen. 

Wir fügen auch vordefinierte Skripte hinzu, wenn Sie die Ereignisse "Produkt angesehen", "Produkt angeklickt" und "Warenkorb-Abbruch" ausgewählt haben, die Shopify ScriptTag oder In-App-Nachrichten als Kanal erfordern.  

#### Wie Sie Enablement betreiben

Um die Braze Web SDK-Skripte automatisch als Teil Ihrer Integration zu aktivieren, wählen Sie die unterstützten Shopify ScriptTag-Ereignisse aus oder aktivieren Sie In-App-Nachricht als Kanal während der [Einrichtung Ihrer Shopify-Integration]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview). 

Im Shopify Setup Composer werden die mit einem Sternchen (\*) gekennzeichneten Ereignisse vom Internet SDK unterstützt. Wenn Sie diese Ereignisse auswählen oder In-Browser-Nachrichten einschließen, fügt Braze die Web SDK-Implementierung über Shopify ScriptTag als Teil Ihrer Einrichtung zu Ihrem Shopify Shop hinzu.

#### Shopify E-Mail-Erfassungsformulare und Nutzer:innen-Abstimmung 

Erfassungsformulare erhalten identifizierbare Kund:in-Daten zu einem frühen Zeitpunkt im Kundenlebenszyklus für nachgelagertes Messaging und Engagement. 

Das Internet SDK verfolgt das Verhalten von Shopify vor Ort und anonymen Nutzer:innen mit Hilfe des `device_id`. Die Braze Shopify ScriptTag Integration ordnet E-Mails aus Shopify E-Mail-Erfassungsformularen, wie z.B. einer Newsletter-Anmeldung, dem `device_id` des Nutzers:innen zu.

Typische Formulare zur Erfassung von E-Mails sind: 
- Formular zur Erfassung von E-Mails 
- Anmeldeformular für den Newsletter

Es gibt zwei Möglichkeiten, die E-Mail des Nutzers:innen und `device_id` abzugleichen: 
- Mit dem Skript zur automatisierten Erfassung von E-Mails von Braze 
- Aufrufen der Methoden `setEmail` oder `setPhoneNumber` 

##### Erfassen von E-Mail- oder Telefonanmeldungen

Mit Braze können Sie unsere Registrierungsformulare für [E-Mail]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign), [SMS und WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) nutzen, um das Web SDK und In-App-Nachrichten zu nutzen. 

Wenn Sie eine E-Mail- oder Telefonnummern-Erfassung von Shopify oder ein Erfassungsformular eines Drittanbieters verwenden, können Sie direkt auf den Nutzer:innen eingestellt werden, der vom Braze Web SDK getrackt wird. Wenn Sie z.B. die E-Mail Adresse der Kund:in erhalten, können Sie sie in deren Nutzerprofil wie folgt einstellen:

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

Einzelheiten zur Einstellung dieser Werte finden Sie in diesen Javascript-Ressourcen:

- Einstellen der [E-Mail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) des Nutzers
- Festlegen der [Telefonnummer](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber) des Nutzers:innen

Sie können auch den Abo-Status der Nutzer:innen festlegen, wenn Sie deren E-Mail oder Telefonnummer erfassen, etwa so:

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

Einzelheiten zur Einstellung dieser Werte finden Sie in diesen Javascript-Ressourcen:

- Einstellung des [Abo-Typs für die E-Mail-Benachrichtigung](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) des Nutzers:in
- Hinzufügen des Nutzers:innen zu einer [Abo-Gruppe](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)

**Beispiel für die Implementierung eines Formulars zur Erfassung durch Dritte**

1. Kopieren Sie in `theme.liquid` den folgenden Snippet in die `head tag`:

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2\. Wir rufen zunächst `setInterval` auf, damit das Skript zuerst geladen wird
3\. Ersetzen Sie `{FORM_ID}` durch die Element ID des Formulars, das Sie erfassen möchten
(wie z.B. "ContactFooter".)
4\. Ersetzen Sie `{INPUT_EMAIL_ID}` durch die ID des E-Mail-Eingabefelds innerhalb des Formulars.
5\. Wenn das Formular abgeschickt wird, ruft das Skript `setEmail` mit dem Eingabewert für die E-Mail auf
6\. Nachdem das Skript geladen wurde, rufen wir `clearInterval` auf, damit es nur einmal geladen wird

{% alert note %}
Zur Zeit wird mit dem E-Mail-Erfassungsformular von Braze keine Shopify Kund:in angelegt. So könnten Sie Braze Nutzerprofile ohne zugehörige Shopify Nutzerprofile haben, bis der Kunde zur Kasse geht oder ein Konto erstellt.
{% endalert %}

#### Was Sie nach der Implementierung erwartet

**Braze Web SDK Initialisierung**

Das Internet SDK wird beim Start der Sitzung initialisiert. Braze muss die `device_id` für das Tracking anonymer Nutzerdaten erfassen, da andere Bezeichner wie die Shopify ID, E-Mail oder Telefonnummer für Gastbesucher Ihres Shopify Shops möglicherweise nicht ohne weiteres verfügbar sind.

Die `device_id` wird auch verwendet, um Nutzerdaten mit dem anonymen Nutzerprofil abzugleichen, wenn ein Nutzer nach dem Bezahlvorgang weitere identifizierbare Daten (z.B. eine E-Mail Adresse oder Telefonnummer) angibt.

**Braze Web SDK Version**

Die aktuelle Version des Braze Web SDK über die Shopify ScriptTag Integration ist v4.2.

**Monatlich aktive Nutzer:innen (MAU)**

Das Internet SDK verfolgt die Sitzungen Ihrer Shopify Kund:innen und Gäste. Infolgedessen wird dies als MAU in Ihrem Braze-Dashboard-Bericht und für Ihre MAU-Zuteilungen angerechnet. Beachten Sie bitte, dass auch anonyme Nutzer:innen zu Ihrem MAU zählen. Bei mobilen Geräten sind anonyme Nutzer:innen geräteabhängig. Für Internet-Nutzer:innen sind anonyme Nutzer:innen vom Browser-Cache abhängig.

{% endtab %}

{% tab Thema Liquid %}

### Die Implementierung des Internet SDK direkt auf Ihrer Shopify Website theme.liquid

Braze bietet mehrere Möglichkeiten zur Implementierung des Internet SDK:
- Hinzufügen des Internet SDK direkt zu Ihrer Shopify `theme.liquid` Datei
- Google Tag Manager 

Wenn Sie das Internet SDK bereits in Ihrem Shopify Shop installiert haben, können Sie mit der Einrichtung des Shopify ScriptTag im Rahmen des Onboarding-Prozesses fortfahren. 

Während des Installationsprozesses prüft Braze, ob bereits Instanzen des Web SDK in Ihrem Shopify Shop verfügbar sind. Wenn es eine bestehende Implementierung gibt, lädt Braze die vordefinierten Skripte für das Enablement des Internet SDK nicht. Wir fügen dann die notwendigen Skripte hinzu, um sicherzustellen, dass Sie die ausgewählten Ereignisse tracken oder In-Browser-Nachrichten aktivieren können.

#### Wie Sie Enablement betreiben

Wie Sie das Internet SDK manuell implementieren können, erfahren Sie unter [Erste SDK-Einrichtung]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web). Um das Internet SDK über Google Tag Manager zu implementieren, sehen Sie sich [Google Tag Manager für das Internet]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager#google-tag-manager) an. 

Stellen Sie bei beiden Implementierungspfaden sicher, dass Ihre Internet SDK-Integration die folgenden Punkte enthält, sonst wird die Shopify-Integration nicht unterstützt: 
- Internet SDK Version von v4.0+
- Internet SDK initialisiert sich beim Start der Sitzung

#### Shopify E-Mail-Erfassungsformulare und Nutzer:innen-Abstimmung 

Erfassungsformulare erhalten identifizierbare Kund:in-Daten zu einem frühen Zeitpunkt im Kundenlebenszyklus für nachgelagertes Messaging und Engagement. 

Das Internet SDK verfolgt das Verhalten von Shopify vor Ort und anonymen Nutzer:innen mit Hilfe des `device_id`. Die Braze Shopify ScriptTag Integration ordnet E-Mails aus Shopify E-Mail-Erfassungsformularen, wie z.B. einer Newsletter-Anmeldung, dem `device_id` des Nutzers:innen zu.

Typische Formulare zur Erfassung von E-Mails sind: 
- Formular zur Erfassung von E-Mails 
- Anmeldeformular für den Newsletter

Es gibt zwei Möglichkeiten, die E-Mail des Nutzers:innen und `device_id` abzugleichen: 
- Mit dem Skript zur automatisierten Erfassung von E-Mails von Braze 
- Aufrufen der Methoden `setEmail` oder `setPhoneNumber` 

##### Erfassen von E-Mail- oder Telefonanmeldungen

Mit Braze können Sie unsere Registrierungsformulare für [E-Mail]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign), [SMS und WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) nutzen, um das Web SDK und In-App-Nachrichten zu nutzen. 

Wenn Sie eine E-Mail- oder Telefonnummern-Erfassung von Shopify oder ein Erfassungsformular eines Drittanbieters verwenden, können Sie direkt auf das Nutzer:innen-Objekt gesetzt werden, das vom Braze Web SDK getrackt wird. Wenn Sie z.B. die E-Mail Adresse der Kund:in erhalten, können Sie sie in deren Nutzerprofil wie folgt einstellen:

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

Einzelheiten zur Einstellung dieser Werte finden Sie in diesen Javascript-Ressourcen:

- Einstellen der [E-Mail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) des Nutzers
- Festlegen der [Telefonnummer](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber) des Nutzers:innen

Sie können auch den Status des Abos der Nutzer:innen festlegen, wenn Sie deren E-Mail oder Telefonnummer erfassen, z.B. so:

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

Einzelheiten zur Einstellung dieser Werte finden Sie in diesen Javascript-Ressourcen:

- Einstellung des [Abo-Typs für die E-Mail-Benachrichtigung](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) des Nutzers:in
- Hinzufügen des Nutzers:innen zu einer [Abo-Gruppe](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)

**Beispiel für die Implementierung eines Formulars zur Erfassung durch Dritte**

1. Kopieren Sie in `theme.liquid` den folgenden Snippet in die `head tag`:

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2\. Wir rufen zunächst `setInterval` auf, damit das Skript zuerst geladen wird
3\. Ersetzen Sie `{FORM_ID}` durch die Element ID des Formulars, das Sie erfassen möchten
(wie z.B. "ContactFooter".)
4\. Ersetzen Sie `{INPUT_EMAIL_ID}` durch die ID des E-Mail-Eingabefelds innerhalb des Formulars.
5\. Wenn das Formular abgeschickt wird, ruft das Skript `setEmail` mit dem Eingabewert für die E-Mail auf
6\. Nachdem das Skript geladen wurde, rufen wir `clearInterval` auf, damit es nur einmal geladen wird

{% alert note %}
Zur Zeit wird mit dem E-Mail-Erfassungsformular von Braze keine Shopify Kund:in angelegt. So könnten Sie Braze Nutzerprofile ohne zugehörige Shopify Nutzerprofile haben, bis der Kunde zur Kasse geht oder ein Konto erstellt.
{% endalert %}

#### Was Sie nach der Integration erwartet

**Braze Web SDK Initialisierung**

Das Internet SDK wird beim Start der Sitzung initialisiert. Braze muss die `device_id` für das Tracking anonymer Nutzerdaten erfassen, da andere Bezeichner wie die Shopify ID, E-Mail oder Telefonnummer für Gastbesucher Ihres Shopify Shops möglicherweise nicht ohne weiteres verfügbar sind.

Die `device_id` wird auch verwendet, um Nutzerdaten mit dem anonymen Nutzerprofil abzugleichen, wenn ein Nutzer:innen während und nach dem Bestellvorgang weitere identifizierbare Daten (wie seine E-Mail oder Telefonnummer) angibt.

**Braze Web SDK Version**

Die aktuelle Version des Braze Web SDK sollte v4.0+ sein.

**Monatlich aktive Nutzer:innen (MAU)**

Das Internet SDK verfolgt die Sitzungen Ihrer Shopify Kund:innen und Gäste. Infolgedessen wird dies als MAU in Ihrem Braze-Dashboard-Bericht und für Ihre MAU-Zuteilungen angerechnet. Beachten Sie bitte, dass auch anonyme Nutzer:innen zu Ihrem MAU zählen. Bei mobilen Geräten sind anonyme Nutzer:innen geräteabhängig. Für Internet-Nutzer:innen sind anonyme Nutzer:innen vom Browser-Cache abhängig.

{% endtab %}
{% tab Shopify-Website ohne Kopf %}

### Implementierung des Internet SDK direkt auf Ihrer Shopify-Website ohne Kopfhörer {#headless-site}

Die Braze Shopify ScriptTag Integration ist mit Shopify-Websites ohne Kopfzeile nicht kompatibel. Daher können Sie keine Standard-Unterstützung für die Ereignisse "Produkt angesehen", "Produkt angeklickt" oder "Warenkorb-Abbruch" erhalten und auch kein Enablement für In-App-Nachrichten über unsere vordefinierten Skripte. 

#### Wie Sie Enablement betreiben

Um das Web SDK direkt in Ihre Headless Shopify Website zu integrieren, lesen Sie bitte [Inital SDK Setup for Web]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web).

Stellen Sie sicher, dass Ihre Internet SDK-Integration Folgendes umfasst: 
- Internet SDK Version sollte v4.0+ sein
- Internet SDK initialisiert sich beim Start der Sitzung

#### Einrichten von Shopify-Formularen für den Abgleich mit Nutzer:innen

E-Commerce-Marken haben auf ihrer Shopify-Website wahrscheinlich Erfahrungen, um identifizierbare Informationen von Kunden vor der Kasse zu erfassen, z. B. Formulare zur Erfassung von E-Mails.

Das Internet SDK verfolgt das Verhalten von Shopify vor Ort und anonymen Nutzer:innen mit dem `device_id`. Um zu bestätigen, dass die E-Mail-Adressen dem Profil der anonymen Nutzer:in hinzugefügt werden, fügen Sie entweder in einem Newsletter oder in einem Formular zur Erfassung von E-Mails Folgendes hinzu: 
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) 
  - Für die Erfassung von E-Mails oder Newsletter-Anmeldungen
- [addAlias](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addalias) 
  - "alias_label": "shopify_email" 
  - "alias_name": "example@email.com"

Wenn sich Nutzer:innen registrieren oder bei ihrem Konto anmelden, möchten Sie [das Nutzerprofil identifizieren]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles), möglicherweise mit einer externen ID. Fügen Sie nach der Registrierung und Anmeldung des Nutzers die Methode [changeUser](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) hinzu, um eine externe ID zuzuweisen, wenn ein Nutzer:innen ein Konto erstellt oder sich anmeldet. 

{% alert note %}
Wenn Sie einen temporären Bezeichner für das Nutzerprofil festlegen, können Sie zu einem späteren Zeitpunkt eine Anfrage an den [Endpunkt users/merge]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) stellen, um den Nutzer:innen zu identifizieren.
{% endalert %}

#### Abgleich mit Nutzer:innen an der Kasse einrichten {#headless-checkout}

Wenn Sie das Ereignis "Abgebrochene Kasse" aktivieren, empfängt Braze den Shopify Webhook "Checkouts/Erstellen". Braze versucht, ein bestehendes Nutzerprofil entweder anhand der E-Mail Adresse, der Telefonnummer oder der Shopify Kund:innen-ID abzugleichen. Wenn es keine Übereinstimmung gibt, erstellt Braze ein Alias-Profil. 

Um sicherzustellen, dass das vor Ort getrackte Nutzerprofil mit dem von den Shopify Webhooks erstellten Nutzerprofil von Shopify-Alias übereinstimmt, können Sie den [Endpunkt`/users/merge` ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) verwenden, indem Sie die folgenden Schritte ausführen. 

{% alert tip %}
Sie können ein angepasstes Event über das SDK oder einen API-Aufruf in der Datei `theme.liquid` protokollieren, um ein Canvas zu triggern, das eine Anfrage an den `users/merge` Endpunkt enthält. Diese Methoden werden im Folgenden beschrieben.
{% endalert %}

Sobald ein Kunde Ihre Shopify-Website besucht, wird ein anonymer Nutzer:in angelegt. Diesem Nutzer:innen wird automatisch eine Braze `device_id` zugewiesen. 

1. Weisen Sie dem Besucher Ihrer Website bei einer neuen Sitzung nach dem Zufallsprinzip einen eindeutigen [Nutzer:in]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) zu.

2. Wenn Nutzer:innen auf Ihrer Website Aktionen durchführen, protokollieren Sie diese als [angepasste Events]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web) oder [erfassen die Attribute der Nutzer]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web):innen. Wenn der Nutzer:innen zur Kasse geht und seine E-Mail in ein Shopify-Formular eingibt, wird eine Shopify Kund:innen ID erstellt. Braze verarbeitet Shopify-Webhooks und erstellt ein neues Nutzerprofil, wenn die E-Mail, die Telefonnummer oder der Nutzer-Alias nicht mit einem bestehenden Nutzer übereinstimmen.

{% raw %}
```javascript
{
  "user_alias": {
    "alias_name": 1234,
    "alias_label": "temp_user_id"
  }
}
```
{% endraw %}

{% subtabs %}
{% subtab API approach %}

{: start="3"}
3\. Um doppelte Nutzerprofile zu vermeiden, müssen Sie das Nutzerprofil mit dem Braze `device_id` mit dem Nutzerprofil mit dem Shopify-Alias-Profil zusammenführen. Sie können ein API-getriggertes Canvas erstellen, das eine Verzögerung setzt, Ihren Nutzer:innen mit dem Attribut `do_not_merge` aktualisiert und eine Anfrage an den [Endpunkt`/users/merge` ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) stellt. Sie können auch ein angepasstes Event wie `merge_user` protokollieren, um Ihren Canvas zu triggern. 


{% endsubtab %}
{% subtab Non-API approach %}

{: start="3"}
3\. Wenn Nutzer:innen den Ablauf verlassen oder die Kasse abschließen, können Sie ein angepasstes Event, wie z.B. `merge_user`, protokollieren, um ein Canvas zu triggern, das eine Verzögerung festlegt, Ihre Nutzer:innen mit dem `do_not_merge` Attribut aktualisiert und eine Anfrage an den [`/users/merge` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) stellt.

{% endsubtab %}
{% endsubtabs %}

{: start="4"}
4\. Stellen Sie in Ihren Canvas-Eingangskriterien nur unidentifizierte Nutzerprofile zusammen, d.h. sie haben keine externe ID und `do_not_merge` ist nicht wahr. <br><br>![Der Schritt "Eingang Zielgruppe" im Canvas-Composer mit `do_not_merge` als Filter.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_entrycriteria.png %})

{: start="5"}
5\. Nachdem Sie Ihre Canvas Eingangskriterien konfiguriert haben, können Sie Ihren Canvas Flow erstellen. Machen Sie den ersten Schritt Ihres Canvas zu einem **Verzögerungsschritt**, um mögliche Race-Conditions während der Verarbeitung zu verhindern.<br><br>![Verzögerungsschritt im Canvas-Composer.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_delay.png %})

{: start="6"}
6\. Sie können einen Schritt **Benutzer Update** erstellen, um das angepasste Attribut `do_not_merge` auf "wahr" anzupassen, da diese Nutzer:innen im nächsten Schritt zusammengeführt werden. <br><br>![Nutzer:in-Update-Schritt im Canvas-Composer mit `do_not_merge` als Attribut ausgewählt.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_userupdate.png %})

{: start="7"}
7\. Als nächstes erstellen Sie einen Schritt **Nachricht** mit einem Webhook.<br><br>![Nachrichten-Schritt im Canvas-Composer mit einem Webhook Messaging-Kanal.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_webhook.png %}) 

{% raw %}
```javascript
{
  "merge_updates": [
    {
      "identifier_to_merge": {
           "user_alias": {
                "alias_label": "temp_user_id",
                "alias_name": "{{canvas_entry_properties.${temp_user_id}}}"
            }
      },
      "identifier_to_keep": {
           "user_alias": {
                "alias_label": "shopify_customer_id",
                "alias_name": "{{canvas_entry_properties.${shopify_customer_id}}}"
            }
      }
    }
  ]
}
```
{% endraw %}

{% alert tip %}
Informationen zum Verhalten von `merge_users` finden Sie unter [POST: Nutzer:innen zusammenführen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior).
{% endalert %}

{: start="8"}
8\. Wenn Nutzer:innen den Ablauf verlassen oder die Kasse abschließen, werden die nachfolgenden Webhooks von Shopify anhand der E-Mail Adresse oder Telefonnummer oder anhand des Shopify-Alias abgeglichen.

{% endtab %}
{% endtabs %}
