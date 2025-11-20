---
nav_title: Integration
article_title: Onboarding-Überblick
page_order: 8
page_type: reference
description: "Dieser Artikel beschreibt die erforderlichen Integrationsschritte für Ihre Entwicklerabteilung."

---

# Integration

> Die Integration mit Braze ist ein lohnender Prozess. Aber Sie sind klug. Sie sind **hier**. Offensichtlich wissen Sie das bereits. Was Sie aber wahrscheinlich noch nicht wissen: Sie und Ihr Entwicklerteam brauchen technisches Fachwissen, strategische Planung und eine einheitliche Kommunikation, die Ihnen die Koordinierung erleichtert.

{% alert note %}
Beachten Sie, dass der Inhalt dieses Artikels nicht für E-Mails gilt. Sehen Sie sich das im Abschnitt [E-Mail-Einrichtung]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/) an.
{% endalert %}

## Die technische Seite des Integrationsprozesses

Vielleicht denken Sie jetzt: "Meine Entwickler sind echte Zauberkünstler! Sie können alles, also lasse ich sie meistens einfach gewähren!" Und sie sind es wahrscheinlich und können es wahrscheinlich auch! Aber es gibt keinen Grund, warum Sie nicht wissen sollten, was sie hinter den Kulissen tun. In der Tat wäre es für den gesamten Prozess hilfreich, wenn Sie wüssten, wann Sie mit Informationen einspringen und worauf Sie achten müssen, wenn man Sie fragt: "Können Sie mir den API-Schlüssel und den API-Endpunkt schicken?"

Was tun sie also, wenn sie Braze in Ihre App oder Website integrieren? Eine gute Frage!

### Schritt 1: Sie implementieren das Braze SDK

Wir verwenden das Braze-SDK (Software-Development-Kit), um Informationen mit Ihrer App oder Website auszutauschen. Ihre Ingenieure verbinden unsere Anwendungen im Wesentlichen miteinander. Dazu benötigen sie einige wichtige Informationen:

* Ihre [API-Schlüssel]({{site.baseurl}}/api/api_key/)
* Ihr [SDK-Endpunkt]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)
  * Braze stellt keine benutzerdefinierten Endpunkte mehr zur Verfügung. Verwenden Sie daher die vordefinierten SDK-Endpunkte. Wenn Sie einen bereits existierenden benutzerdefinierten Endpunkt erhalten haben, finden Sie hier die Einrichtungsschritte für die [Android-]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-5-optional-custom-endpoint-setup), [iOS-]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) und [Web-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#initializing-the-sdk).

Sie können diese Informationen entweder direkt weitergeben oder Sie können ihnen Zugang zu Braze geben, indem Sie ein Konto für sie erstellen. 

{% alert warning %}
Stellen Sie sicher, dass Sie und Ihr Entwicklerteam in Braze nicht versehentlich die Zugangsdaten Ihre Unternehmens ändern. Denn das kann zu Problemen bei der Implementierung und sogar zur Kontensperrung führen.
{% endalert %}

### Schritt 2: Sie implementieren die von Ihnen gewünschten Nachrichtenkanäle

Braze bietet viele Optionen, um mit Ihren Benutzern in Kontakt zu treten, und jede erfordert eine eigene Einrichtung oder Anpassung, damit sie so funktioniert, wie Sie es wünschen. An dieser Stelle wird die Kommunikation mit Ihren Ingenieuren entscheidend.

Teilen Sie Ihren Entwicklern mit, welche Kanäle Sie verwenden möchten, um sicherzustellen, dass die Implementierung effizient und in der richtigen Reihenfolge erfolgt.

| Kanal | Details |
|---|---|
| In-App-Nachrichten | Erfordert die SDK-Implementierung sowie diese kanalspezifischen Schritte. |
| Push | Erfordert eine SDK-Implementierung für die korrekte Handhabung von Messaging-Zugangsdaten und Push-Token. |
| E-Mail | Dies ist ein völlig anderer Prozess. Weitere Einzelheiten zur Integration finden Sie im Abschnitt [E-Mail-Einrichtung]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/). |
| Content-Cards | Um mit [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) zu beginnen, wenden Sie sich an Ihren Braze Customer Success Manager. |
| SMS & MMS | Weitere Einzelheiten zur Integration finden Sie im Abschnitt [SMS-Einrichtung]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/sms_setup/sms_sending/). |
| Webhooks | Erfordert eine SDK-Implementierung sowie kanalspezifische Schritte. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Mit Braze können Sie für jeden Kanal barrierefreie Messaging-Kampagnen erstellen. Stellen Sie gemeinsam mit Ihren Entwicklern sicher, dass Sie bei der Implementierung die Standards der Barrierefreiheit einhalten.
{% endalert %}

### Schritt 3: Daten einrichten

Braze ist kein One-Trick-Pony. Hier geht es nicht nur um das Versenden von E-Mails oder Push-Nachrichten. Es geht darum, individuelle Customer Journeys auf Nutzer- und Kundenebene zu erstellen. Diese basieren auf Kundenaktionen in Ihrer App oder auf Ihrer Website. Welche das sind, können Sie selbst bestimmen. Die nächste Aufgabe Ihrer Entwickler besteht darin, dafür zu sorgen, dass die in Ihrer App oder Website durchgeführten Aktionen von Braze erfasst werden.

Was müssen Sie also tun, um ihnen diese Informationen zu geben?

1. Arbeiten Sie mit Ihrem Marketingteam zusammen, um Kampagnen, Ziele, Attribute und Ereignisse festzulegen, die Sie verfolgen wollen. Definieren Sie diese Anwendungsfälle und teilen Sie sie mit Ihren Teams.
2. Definieren Sie Ihre benutzerdefinierten Datenanforderungen[(benutzerdefinierte Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/), [benutzerdefinierte Ereignisse]({{site.baseurl}}/user_guide/data/custom_data/custom_events/), usw.).
3. Diskutieren Sie dann, wie diese Daten getrackt werden sollen (getriggert durch das SDK usw.).
4. Legen Sie fest, wie viele [Arbeitsbereiche]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/) Sie benötigen. Ihre Techniker müssen wissen, wie sie diese Arbeitsbereiche [testen und konfigurieren]({{site.baseurl}}/user_guide/getting_started/workspaces/) können.

Wenn Sie alles geklärt haben, informieren Sie Ihr Engineering. Sie nehmen diese Informationen auf und implementieren Ihre [individuellen Daten]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/). Vielleicht müssen Sie sogar [einige Benutzer importieren]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/). Sie sollten auch die [Benennungskonventionen für Ereignisse]({{site.baseurl}}/user_guide/data/custom_data/event_naming_conventions/) kennen.

### Schritt 4: Sie passen sich Ihren Wünschen an

Wenn Sie Dinge wie API-getriggerte Starts und Connected-Content beabsichtigen, besprechen Sie das mit Ihrem Braze-Ansprechpartner und Ihrem Entwicklerteam, damit Sie auch Daten von außerhalb Ihrer App und Braze in Ihren Nachrichten verwenden können.

### Schritt 5: Sie beide führen eine QA für Ihre Implementierung durch

Arbeiten Sie mit Ihrem Engineering zusammen, um sicherzustellen, dass alles funktioniert. Versenden Sie [Testnachrichten]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/), nutzen Sie unsere [Test-Apps für Android]({{site.baseurl}}/developer_guide/references/?tab=android) und [Test-Apps für iOS]({{site.baseurl}}/developer_guide/references/?tab=swift) und gehen Sie auf Nummer sicher, bevor Sie mit dem Versand beginnen.

Wir haben sogar spezielle Anweisungen zum [Testen Ihrer Android- oder FireOS-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/test_your_basic_integration/#test-your-basic-integration) und zum Testen von [Push für iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/testing/).

## Nach der Implementierung

Denken Sie daran, dass eine abgeschlossene Implementierung nicht automatisch bedeutet, dass Sie Millionen von Nachrichten auf einmal versenden können. Das Versenden von einer Million Push-Nachrichten könnte Ihre App zerstören, wenn jeder Kunde gleichzeitig auf denselben Link klickt. Wir empfehlen Ihnen, die Kapazität Ihrer internen Einrichtung für die Bearbeitung von Anfragen von Braze zu besprechen, bevor Sie auf die Schaltfläche **Senden** klicken. Auf dieser Grundlage können Sie dann Ihre [Ratenbegrenzung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting) festlegen.

\![]({% image_buster/assets/img/torchie/firebrands.png %}){: style="max-width:15%;float:right;margin-left:15px;border:none;"}

Wenn Sie sich mit Braze vertraut gemacht haben, können Sie bei Braze Firebrands mitmachen. Braze Firebrands ist unsere Kundencommunity. Wir wollen Vordenker und Pioniere zusammenbringen, die Braze nutzen, um ihr Kundenerlebnis und ihr Marketing zu modernisieren. Möchten Sie mehr erfahren? [Jetzt mitmachen](https://brazefirebrands.splashthat.com/).
