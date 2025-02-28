---
nav_title: Erste Schritte
article_title: "Erste Schritte mit Shopify"
description: "Dieser Referenzartikel beschreibt, wie Sie das Braze Web SDK auf Ihrer Shopify-Website implementieren."
page_type: partner
search_tag: Partner
alias: /getting_started_shopify/
page_order: 1
---

# Erste Schritte mit Shopify

> Dieser Artikel beschreibt, wie Sie das Braze Web SDK auf Ihrer Shopify-Website implementieren. Nach der Implementierung lesen Sie [Shopify einrichten]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify), um zu erfahren, wie Sie die Shopify-Integration mit Braze fertigstellen.

## Checkliste für die Integration

1. [Implementierung des Braze Web SDK](#implement-web-sdk)
2. [Shopify in Braze einrichten]({{site.baseurl}}//partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify)
3. Testen Sie die Shopify-Integration

## Implementierung des Web SDK auf Ihrer Shopify-Website {#implement-web-sdk}

Das [Braze Web SDK]({{site.baseurl}}/user_guide/onboarding_with_braze/web_sdk/) ist ein leistungsstarkes Tool, mit dem Sie das Verhalten Ihrer Shopify-Kunden verfolgen können. Mit dem Web SDK können Sie Sitzungsdaten sammeln, Benutzer identifizieren und Daten zum Benutzerverhalten von einem Web- oder Mobilbrowser aufzeichnen. Sie können auch native Messaging-Kanäle wie In-Browser-Nachrichten freischalten.

Obwohl die Shopify-Integration eine Reihe von Standardfunktionen bietet, sollten Sie bedenken, dass Sie das Web SDK direkt auf Ihrer Shopify-Website implementieren müssen, wenn Sie Anwendungsfälle haben, bei denen Sie das Tracking vor Ort für [Ereignisse]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_in_braze/) hinzufügen möchten [, die von der Shopify-Integration nicht unterstützt werden]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_in_braze/), oder Kanäle wie [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) hinzufügen möchten.

Bevor Sie mit dem Onboarding der Integration beginnen, besprechen Sie bitte mit Ihrem Team, welchen Weg Sie für die Implementierung des Web SDK einschlagen möchten.

### Unterstützte Funktionen

|Symbol| Definition 
|-------------|-------------
|<i aria-hidden="true" class="fas fa-check" title="Unterstützt"></i><span class="sr-only">Unterstützt</span> | Unterstützt
|<i aria-hidden="true" class="fas fa-times" title="Nicht unterstützt"></i><span class="sr-only">Unterstützt</span> | Nicht unterstützt
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

| Eigenschaften | Web SDK über Shopify ScriptTag | Direkte Web-SDK-Integration über theme.liquid | Direkte Web-SDK-Integration über Shopify Hydrogen
|-------------|-------------|-------------|------------
| Standardmäßige Vor-Ort-Verfolgung      | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i>          
| Erfassen von Formularen zur Abstimmung mit dem Benutzer (geringer technischer Aufwand erforderlich)   | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> 
| Checkout Benutzerabgleich     | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-times" title="Nicht unterstützt"></i>   | <i class="fas fa-times" title="Nicht unterstützt"></i>                                        
| Produkt angesehen<br> Produkt geklickt<br> Verlassener Wagen   | <i class="fas fa-check" title="Unterstützt"></i> |<i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> 
| Abgebrochene Kasse<br> Erstellter Auftrag<br> Braze Kauf<br> Bestellung bezahlt<br> Teilweise erfüllte Bestellung<br> Erfüllte Bestellung<br> Stornierte Bestellung<br> Erstellt Erstattung<br> Kunden erstellen & aktualisieren | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i> | <i class="fas fa-check" title="Unterstützt"></i>
| Historische Verfüllung | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-check" title="Unterstützt"></i>  
| Katalog synchronisieren  |<i class="fas fa-check" title="Unterstützt"></i> |<i class="fas fa-check" title="Unterstützt"></i>  |<i class="fas fa-check" title="Unterstützt"></i>
| Sammlung von E-Mail- und SMS-Abonnenten    | <i class="fas fa-check" title="Unterstützt"></i>| <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-check" title="Unterstützt"></i>     
| Standardmäßige Unterstützung für In-App-Nachrichten   | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-check" title="Unterstützt"></i>  | <i class="fas fa-times" title="Nicht unterstützt"></i>     
| Unterstützung von Standard-Inhaltskarten   | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i>   
| Standardmäßige Web-Push-Unterstützung     | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i> | <i class="fas fa-times" title="Nicht unterstützt"></i>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }    

{% tabs %}
{% tab Shopify ScriptTag %}

### Implementierung des Braze Web SDK über Shopify ScriptTag

[Shopify ScriptTag](https://shopify.dev/api/admin-rest/2021-10/resources/scripttag#top) ist ein Remote-JavaScript-Code, der in die Seiten Ihres Shops oder die Bestellstatusseite der Kasse geladen wird. Wenn eine Shopseite geladen wird, prüft Shopify, ob Skript-Tags in die Seite geladen werden müssen. 

Wenn Sie schnell mit Braze beginnen möchten, haben Sie die Möglichkeit, Braze zu erlauben, ein vordefiniertes Skript für das Braze Web SDK direkt auf Ihre Shopify-Website zu laden.

{% alert important %}
Das vordefinierte Skript für das Braze Web SDK für diese Integrationsmethode ist nicht anpassbar.
{% endalert %}

#### So funktioniert es mit der Shopify-Integration

Wenn Ihre Shopify-Website geladen wird, prüft Shopify, ob Skript-Tags in die Seite geladen werden müssen. Während des Prozesses werden die Skripte des Braze Web SDK auf die Seiten Ihres Shops oder die Bestellstatusseite der Kasse geladen. 

Wir fügen auch vordefinierte Skripte hinzu, wenn Sie die Ereignisse "Produkt angesehen", "Produkt angeklickt" und "Abgebrochener Warenkorb" ausgewählt haben, die Shopify ScriptTag oder In-App-Nachrichten als Kanal erfordern.  

#### Wie Sie aktivieren

Um die Braze Web SDK-Skripte automatisch als Teil Ihrer Integration zu aktivieren, wählen Sie während der [Einrichtung der Shopify-Integration]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/) die unterstützten Shopify ScriptTag-Ereignisse aus oder aktivieren Sie In-App-Messaging als Kanal. 

Im Shopify Setup Composer werden die mit einem Sternchen (\*) gekennzeichneten Ereignisse vom Web SDK unterstützt. Wenn Sie diese Ereignisse auswählen oder In-Browser-Messaging einschließen, fügt Braze die Web SDK-Implementierung über Shopify ScriptTag als Teil Ihrer Einrichtung zu Ihrem Shopify-Shop hinzu.

#### Shopify E-Mail-Erfassungsformulare und Benutzerabgleich 

Erfassungsformulare erhalten identifizierbare Kundeninformationen zu einem frühen Zeitpunkt im Lebenszyklus des Kunden, um spätere Nachrichten und Interaktionen zu ermöglichen. 

Das Web SDK verfolgt das Verhalten von Shopify vor Ort und anonymen Nutzern mit Hilfe der `device_id`. Die Braze Shopify ScriptTag-Integration ordnet E-Mails aus Shopify-E-Mail-Erfassungsformularen, wie z. B. einer Newsletter-Anmeldung, dem `device_id` des Benutzers zu.

Typische E-Mail-Erfassungsformulare sind: 
- Formular zur E-Mail-Erfassung 
- Anmeldeformular für den Newsletter

Es gibt zwei Möglichkeiten, die E-Mail des Benutzers und `device_id` abzugleichen: 
- Verwendung des Skripts zur automatischen E-Mail-Erfassung von Braze 
- Aufrufen der Methoden `setEmail` oder `setPhoneNumber` 

##### Erfassen von E-Mail- oder Telefonanmeldungen

Mit Braze können Sie unsere [E-Mail-]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign), [SMS- und WhatsApp-Anmeldeformulare]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) verwenden, um das Web-SDK und In-App-Nachrichten zu nutzen. 

Wenn Sie eine Shopify E-Mail- oder Telefonnummern-Erfassung oder ein Erfassungsformular eines Drittanbieters verwenden, können Sie direkt auf den Benutzer eingestellt werden, der vom Braze Web SDK verfolgt wird. Wenn Sie z.B. die E-Mail-Adresse des Kunden erhalten, können Sie sie wie folgt in dessen Benutzerprofil eingeben:

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

Einzelheiten zur Einstellung dieser Werte finden Sie in diesen Javascript-Ressourcen:

- Einstellen der [E-Mail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) des Benutzers
- Einstellen der [Telefonnummer](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber) des Benutzers

Sie können auch den Abonnementstatus des Benutzers festlegen, wenn Sie seine E-Mail oder Telefonnummer erfassen, z.B. so:

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

Einzelheiten zur Einstellung dieser Werte finden Sie in diesen Javascript-Ressourcen:

- Einstellung des [Abonnementtyps für die E-Mail-Benachrichtigung](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) des Benutzers
- Hinzufügen des Benutzers zu einer [Abonnementgruppe](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)

**Beispiel für die Implementierung eines Formulars zur Erfassung durch Dritte**

1. Kopieren Sie in `theme.liquid` den folgenden Ausschnitt in die `head tag`:

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
3\. Ersetzen Sie `{FORM_ID}` durch die Element-ID des Formulars, das Sie erfassen möchten.
(wie z.B. "ContactFooter".)
4\. Ersetzen Sie `{INPUT_EMAIL_ID}` durch die Element-ID des E-Mail-Eingabefelds innerhalb des Formulars
5\. Wenn das Formular abgeschickt wird, ruft das Skript `setEmail` mit dem E-Mail-Eingabewert auf.
6\. Nachdem das Skript geladen wurde, rufen wir `clearInterval` auf, damit es nur einmal geladen wird

{% alert note %}
Derzeit wird mit dem Braze E-Mail-Erfassungsformular kein Shopify-Kunde angelegt. Infolgedessen können Sie Braze-Benutzerprofile ohne zugehörige Shopify-Benutzerprofile haben, bis der Kunde zur Kasse geht oder ein Konto erstellt.
{% endalert %}

#### Was Sie nach der Implementierung erwartet

**Initialisierung des Braze Web SDK**

Das Web SDK wird beim Start der Sitzung initialisiert. Braze muss die `device_id` für die Nachverfolgung anonymer Benutzerdaten erfassen, da andere Identifikatoren wie die Shopify-Kunden-ID, E-Mail oder Telefonnummer für Gastbesucher Ihres Shopify-Shops möglicherweise nicht ohne weiteres verfügbar sind.

Die `device_id` wird auch verwendet, um Benutzerdaten mit dem anonymen Benutzerprofil abzugleichen, wenn ein Kunde nach dem Bezahlvorgang weitere identifizierbare Informationen (wie eine E-Mail-Adresse oder Telefonnummer) angibt.

**Braze Web SDK Version**

Die aktuelle Version des Braze Web SDK über Shopify ScriptTag Integration ist v4.2.

**Monatlich aktive Benutzer (MAU)**

Das Web SDK verfolgt die Sitzungen Ihrer Shopify-Kunden und Gäste. Folglich wird dies als MAU in Ihren Braze Dashboard-Berichten und bei Ihren MAU-Zuteilungen berücksichtigt. Es ist wichtig zu wissen, dass auch anonyme Nutzer zu Ihren MAUs zählen. Bei mobilen Geräten sind anonyme Benutzer geräteabhängig. Bei Internetnutzern sind anonyme Nutzer vom Browser-Cache abhängig.

{% endtab %}

{% tab Thema Flüssigkeit %}

### Die Implementierung des Web SDK direkt auf Ihrer Shopify-Website theme.liquid

Braze bietet mehrere Möglichkeiten zur Implementierung des Web-SDKs:
- Hinzufügen des Web SDK direkt zu Ihrer Shopify `theme.liquid` Datei
- Google Tag Manager 

Wenn Sie das Web SDK bereits in Ihrem Shopify-Shop installiert haben, können Sie mit der Einrichtung des Shopify ScriptTag im Rahmen des Onboarding-Prozesses fortfahren. 

Während des Installationsvorgangs prüft Braze, ob Instanzen des Web SDK bereits in Ihrem Shopify-Shop verfügbar sind. Wenn es eine bestehende Implementierung gibt, lädt Braze die vordefinierten Skripte zur Aktivierung des Web SDK nicht. Anschließend fügen wir die erforderlichen Skripte hinzu, um sicherzustellen, dass Sie die ausgewählten Ereignisse verfolgen oder In-Browser-Messaging aktivieren können.

#### Wie Sie aktivieren

Um das Web SDK manuell zu implementieren, sehen Sie sich die [erste SDK-Einrichtung]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/) an. Um das Web SDK über Google Tag Manager zu implementieren, sehen Sie sich [Google Tag Manager für Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager#google-tag-manager) an. 

Stellen Sie bei beiden Implementierungspfaden sicher, dass Ihre Web SDK-Integration Folgendes umfasst, sonst wird die Shopify-Integration nicht unterstützt: 
- Web SDK Version von v4.0+
- Web SDK initialisiert beim Start der Sitzung

#### Shopify E-Mail-Erfassungsformulare und Benutzerabgleich 

Erfassungsformulare erhalten identifizierbare Kundeninformationen zu einem frühen Zeitpunkt im Lebenszyklus des Kunden, um spätere Nachrichten und Interaktionen zu ermöglichen. 

Das Web SDK verfolgt das Verhalten von Shopify vor Ort und anonymen Nutzern mit Hilfe der `device_id`. Die Braze Shopify ScriptTag-Integration ordnet E-Mails aus Shopify-E-Mail-Erfassungsformularen, wie z. B. einer Newsletter-Anmeldung, dem `device_id` des Benutzers zu.

Typische E-Mail-Erfassungsformulare sind: 
- Formular zur E-Mail-Erfassung 
- Anmeldeformular für den Newsletter

Es gibt zwei Möglichkeiten, die E-Mail des Benutzers und `device_id` abzugleichen: 
- Verwendung des Skripts zur automatischen E-Mail-Erfassung von Braze 
- Aufrufen der Methoden `setEmail` oder `setPhoneNumber` 

##### Erfassen von E-Mail- oder Telefonanmeldungen

Mit Braze können Sie unsere [E-Mail-]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign), [SMS- und WhatsApp-Anmeldeformulare]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) verwenden, um das Web-SDK und In-App-Nachrichten zu nutzen. 

Wenn Sie eine E-Mail- oder Telefonnummern-Erfassung von Shopify oder ein Erfassungsformular eines Drittanbieters verwenden, können Sie direkt auf das Benutzerobjekt gesetzt werden, das vom Braze Web SDK verfolgt wird. Wenn Sie z.B. die E-Mail-Adresse des Kunden erhalten, können Sie sie wie folgt in dessen Benutzerprofil eingeben:

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

Einzelheiten zur Einstellung dieser Werte finden Sie in diesen Javascript-Ressourcen:

- Einstellen der [E-Mail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) des Benutzers
- Einstellen der [Telefonnummer](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber) des Benutzers

Sie können auch den Abonnementstatus des Benutzers festlegen, während Sie seine E-Mail oder Telefonnummer erfassen, wie hier:

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

Einzelheiten zur Einstellung dieser Werte finden Sie in diesen Javascript-Ressourcen:

- Einstellung des [Abonnementtyps für die E-Mail-Benachrichtigung](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) des Benutzers
- Hinzufügen des Benutzers zu einer [Abonnementgruppe](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)

**Beispiel für die Implementierung eines Formulars zur Erfassung durch Dritte**

1. Kopieren Sie in `theme.liquid` den folgenden Ausschnitt in die `head tag`:

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
3\. Ersetzen Sie `{FORM_ID}` durch die Element-ID des Formulars, das Sie erfassen möchten.
(wie z.B. "ContactFooter".)
4\. Ersetzen Sie `{INPUT_EMAIL_ID}` durch die Element-ID des E-Mail-Eingabefelds innerhalb des Formulars
5\. Wenn das Formular abgeschickt wird, ruft das Skript `setEmail` mit dem E-Mail-Eingabewert auf.
6\. Nachdem das Skript geladen wurde, rufen wir `clearInterval` auf, damit es nur einmal geladen wird

{% alert note %}
Derzeit wird mit dem Braze E-Mail-Erfassungsformular kein Shopify-Kunde angelegt. Infolgedessen können Sie Braze-Benutzerprofile ohne zugehörige Shopify-Benutzerprofile haben, bis der Kunde zur Kasse geht oder ein Konto erstellt.
{% endalert %}

#### Was Sie nach der Integration erwartet

**Initialisierung des Braze Web SDK**

Das Web SDK wird beim Start der Sitzung initialisiert. Braze muss die `device_id` für die Nachverfolgung anonymer Benutzerdaten erfassen, da andere Identifikatoren wie die Shopify-Kunden-ID, E-Mail oder Telefonnummer für Gastbesucher Ihres Shopify-Shops möglicherweise nicht ohne weiteres verfügbar sind.

Die `device_id` wird auch verwendet, um Benutzerdaten mit dem anonymen Benutzerprofil abzugleichen, wenn ein Kunde während und nach dem Bezahlvorgang weitere identifizierbare Informationen (z. B. seine E-Mail-Adresse oder Telefonnummer) angibt.

**Braze Web SDK Version**

Die aktuelle Version des Braze Web SDK sollte v4.0+ sein.

**Monatlich aktive Benutzer (MAU)**

Das Web SDK verfolgt die Sitzungen Ihrer Shopify-Kunden und Gäste. Folglich wird dies als MAU in Ihren Braze Dashboard-Berichten und bei Ihren MAU-Zuteilungen berücksichtigt. Es ist wichtig zu wissen, dass auch anonyme Nutzer zu Ihren MAUs zählen. Bei mobilen Geräten sind anonyme Benutzer geräteabhängig. Bei Internetnutzern sind anonyme Nutzer vom Browser-Cache abhängig.

{% endtab %}
{% tab Kopflose Shopify-Website %}

### Implementierung des Web SDK direkt auf Ihrer Shopify-Website ohne Kopfhörer {#headless-site}

Die Braze Shopify ScriptTag-Integration ist nicht mit Shopify-Websites ohne Kopfzeile kompatibel. Infolgedessen können Sie keine Standardunterstützung für die Ereignisse "Produkt angesehen", "Produkt angeklickt" oder "Abgebrochener Warenkorb" erhalten und auch keine In-App-Nachrichten über unsere vordefinierten Skripte aktivieren. 

#### Wie Sie aktivieren

Um das Web-SDK direkt in Ihre Shopify-Website zu integrieren, lesen Sie bitte [Inital SDK Setup for Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/).

Stellen Sie sicher, dass Ihre Web SDK-Integration Folgendes umfasst: 
- Web SDK Version sollte v4.0+ sein
- Web SDK initialisiert beim Start der Sitzung

#### Einrichten von Shopify-Formularen für den Benutzerabgleich

E-Commerce-Marken haben auf ihrer Shopify-Website wahrscheinlich Erfahrungen, um identifizierbare Informationen von Kunden vor der Kasse zu erfassen, wie z.B. E-Mail-Erfassungsformulare.

Das Web SDK verfolgt das Verhalten von Shopify vor Ort und anonymen Nutzern mit dem `device_id`. Um zu bestätigen, dass E-Mail-Adressen zum anonymen Benutzerprofil hinzugefügt werden, fügen Sie entweder in einem Newsletter oder einem E-Mail-Erfassungsformular Folgendes hinzu: 
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) 
  - Für E-Mail-Erfassung oder Newsletter-Anmeldungen
- [addAlias](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addalias) 
  - "alias_label": "shopify_email" 
  - "alias_name": "example@email.com"

Wenn sich Benutzer registrieren oder bei ihrem Konto anmelden, möchten Sie [das Benutzerprofil]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) möglicherweise mit einer externen ID [identifizieren]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles). Nachdem sich der Benutzer registriert und angemeldet hat, fügen Sie die Methode [changeUser](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) hinzu, um eine externe ID zuzuweisen, wenn ein Benutzer ein Konto erstellt oder sich anmeldet. 

{% alert note %}
Wenn Sie im Benutzerprofil einen temporären Alias festlegen, können Sie zu einem späteren Zeitpunkt eine Anfrage an den [Endpunkt users/merge]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) stellen, um den Benutzer zu identifizieren.
{% endalert %}

#### Einrichten des Checkout-Benutzerabgleichs {#headless-checkout}

Wenn Sie das Ereignis "Abgebrochene Kasse" aktivieren, empfängt Braze den Shopify-Webhook "Checkouts/Erstellen". Braze wird versuchen, ein bestehendes Benutzerprofil entweder anhand der E-Mail-Adresse, der Telefonnummer oder der Shopify-Kunden-ID zu finden. Wenn es keine Übereinstimmung gibt, erstellt Braze ein Alias-Profil. 

Um sicherzustellen, dass das vor Ort verfolgte Benutzerprofil mit dem von den Shopify-Webhooks erstellten Shopify-Alias-Benutzerprofil übereinstimmt, können Sie den [Endpunkt`/users/merge` ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) verwenden, indem Sie die folgenden Schritte ausführen. 

{% alert tip %}
Sie können ein benutzerdefiniertes Ereignis über das SDK oder einen API-Aufruf in der Datei `theme.liquid` protokollieren, um ein Canvas auszulösen, das eine Anfrage an den Endpunkt `users/merge` enthält. Diese Methoden werden im Folgenden beschrieben.
{% endalert %}

Sobald ein Kunde Ihre Shopify-Website besucht, wird ein anonymer Benutzer erstellt. Diesem Benutzer wird automatisch ein Braze `device_id` zugewiesen. 

1. Weisen Sie dem Besucher Ihrer Website bei einer neuen Sitzung nach dem Zufallsprinzip einen eindeutigen [Benutzer-Alias]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) zu.

2. Wenn Benutzer Aktionen auf Ihrer Website durchführen, protokollieren Sie diese als [benutzerdefinierte Ereignisse]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events) oder [erfassen Benutzerattribute]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/). Wenn der Benutzer zur Kasse geht und seine E-Mail in ein Shopify-Formular eingibt, wird eine Shopify-Kunden-ID erstellt. Braze verarbeitet Shopify-Webhooks und erstellt ein neues Benutzerprofil, wenn die E-Mail, die Telefonnummer oder der Shopify-Alias nicht mit einem bestehenden Benutzer übereinstimmen.

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
3\. Um doppelte Benutzerprofile zu vermeiden, müssen Sie das Benutzerprofil, das das Braze `device_id` enthält, mit dem Benutzerprofil zusammenführen, das das Shopify-Aliasprofil enthält. Sie können ein API-ausgelöstes Canvas erstellen, das eine Verzögerung festlegt, Ihren Benutzer mit dem Attribut `do_not_merge` aktualisiert und eine Anfrage an den [Endpunkt`/users/merge` ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) stellt. Sie können auch ein benutzerdefiniertes Ereignis wie `merge_user` protokollieren, um Ihr Canvas auszulösen. 


{% endsubtab %}
{% subtab Non-API approach %}

{: start="3"}
3\. Wenn Benutzer den Ablauf verlassen oder den Checkout abschließen, können Sie ein benutzerdefiniertes Ereignis wie `merge_user` protokollieren, um ein Canvas auszulösen, das eine Verzögerung festlegt, Ihren Benutzer mit dem Attribut `do_not_merge` aktualisiert und eine Anfrage an den [Endpunkt`/users/merge` ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) stellt.

{% endsubtab %}
{% endsubtabs %}

{: start="4"}
4\. In Ihren Canvas-Eingabekriterien zielen Sie nur auf nicht identifizierte Benutzerprofile ab, d.h. sie haben keine externe ID und `do_not_merge` ist nicht wahr. <br><br>![Der Schritt "Eintritt Publikum" im Canvas Composer mit `do_not_merge` als Filter.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_entrycriteria.png %})

{: start="5"}
5\. Nachdem Sie Ihre Canvas-Eingabekriterien konfiguriert haben, können Sie Ihren Canvas Flow erstellen. Machen Sie den ersten Schritt Ihres Canvas zu einem **Verzögerungsschritt**, um mögliche Race Conditions während der Verarbeitung zu verhindern.<br><br>![Verzögerungsschritt im Canvas Composer.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_delay.png %})

{: start="6"}
6\. Sie können einen Schritt **zur Benutzeraktualisierung** erstellen, um das benutzerdefinierte Attribut `do_not_merge` auf "true" zu aktualisieren, da diese Benutzer im nächsten Schritt zusammengeführt werden sollen. <br><br>![Benutzeraktualisierungsschritt im Canvas Composer mit `do_not_merge` als Attribut ausgewählt.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_userupdate.png %})

{: start="7"}
7\. Als nächstes erstellen Sie einen **Nachrichtenschritt** mit einem Webhook.<br><br>![Nachrichtenschritt im Canvas Composer mit einem Webhook-Nachrichtenkanal.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_webhook.png %}) 

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
Informationen zum Verhalten von `merge_users` finden Sie unter [POST: Benutzer zusammenführen]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior).
{% endalert %}

{: start="8"}
8\. Wenn der Benutzer den Ablauf verlässt oder die Kasse abschließt, werden die nachfolgenden Shopify-Webhooks anhand der E-Mail-Adresse oder Telefonnummer oder anhand des Shopify-Alias abgeglichen.

{% endtab %}
{% endtabs %}
