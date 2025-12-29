---
nav_title: Erstellen eines Webhooks
article_title: Einen Webhook erstellen
page_order: 1
channel:
  - webhooks
description: "In diesem Referenzartikel erfahren Sie, wie Sie eine Webhook-Kampagne erstellen und konfigurieren."
search_rank: 2
---

# Erstellen einer Webhook-Kampagne

> Wenn Sie eine Webhook-Kampagne erstellen oder einen Webhook in eine Multichannel-Kampagne einbinden, ist es zulässig, Nicht-App-Aktionen zu triggern, indem Sie anderen Systemen und Anwendungen Informationen in Echtzeit zur Verfügung stellen. 

Sie können Webhooks verwenden, um Informationen an Systeme wie Salesforce oder Marketo oder an Ihre Backend-Systeme zu senden. Zum Beispiel könnten Sie Ihren Kunden eine Werbeaktion gutschreiben, nachdem sie ein benutzerdefiniertes Ereignis eine bestimmte Anzahl von Malen durchgeführt haben.

{% alert tip %}
Wenn Sie mehr darüber erfahren möchten, was Webhooks sind und wie Sie sie in Braze verwenden können, lesen Sie [Über Webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/), bevor Sie fortfahren.
{% endalert %}

## Schritt 1: Wählen Sie, wo Sie Ihre Botschaft aufbauen möchten

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Kampagne oder ein Canvas versendet werden soll? Kampagnen eignen sich eher für einzelne einfache Messaging-Kampagnen, während Canvases besser für mehrstufige User Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}

**Schritte:**

1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie **Webhook** aus. Wählen Sie für Kampagnen, die auf mehrere Kanäle abzielen, **Multichannel** aus.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. (Optional) Fügen Sie eine Beschreibung hinzu, um zu beschreiben, wie diese Kampagne verwendet werden soll.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu.
   * Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.
5. Fügen Sie so viele Varianten hinzu, wie Sie für Ihre Kampagne benötigen, und benennen Sie sie. Sie können für jede Ihrer hinzugefügten Varianten unterschiedliche Webhook-Vorlagen wählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sind oder den gleichen Inhalt haben, sollten Sie Ihre Nachricht verfassen, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann aus der Dropdown-Liste **Variante hinzufügen** die Option **Aus Variante kopieren** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Schritte:**

1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit dem Canvas Composer.
2. Wenn Sie den Canvas eingerichtet haben, fügen Sie im Canvas Builder einen Schritt hinzu. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
3. Wählen Sie einen [Zeitplan für den Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) und geben Sie bei Bedarf eine Verzögerung an.
4. Filtern Sie Ihre Zielgruppe für diesen Schritt nach Bedarf. Sie können den Empfängerkreis mit Segmenten und zusätzlichen Filtern weiter eingrenzen. Die Zielgruppenoptionen werden mit einer gewissen Verzögerung zum Versandzeitpunkt überprüft.
5. Legen Sie das [Fortschrittsverhalten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) fest.
6. Wählen Sie weitere Messaging-Kanäle für Ihre Nachricht aus.

{% endtab %}
{% endtabs %}

## Schritt 2: Erstellen Sie Ihren Webhook

Sie können einen Webhook von Grund auf neu erstellen, eine vorhandene Vorlage verwenden oder eine unserer vorhandenen Vorlagen nutzen. Erstellen Sie dann Ihren Webhook auf der Registerkarte **Verfassen** des Editors.

Die Registerkarte **Verfassen** besteht aus den folgenden Feldern:

- Sprache
- Webhook-URL
- HTTP-Methode
- Anfragetext

![Der Tab "Verfassen" mit einem Beispiel für ein Webhook Template.]({% image_buster /assets/img_archive/webhook_compose.png %})

#### Sprache {#internationalization}

Die [Internationalisierung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) wird in der URL und im Anfragetext unterstützt. Um Ihre Nachricht zu internationalisieren, wählen Sie **Sprachen hinzufügen** aus und füllen Sie die erforderlichen Felder aus. 

Wählen Sie die Sprachen am besten aus, bevor Sie den Content verfassen, damit Sie den Text dort einfügen können, wo er im Liquid hingehört. Eine vollständige Liste der Sprachen, die Sie verwenden können, finden Sie unter [Unterstützte Sprachen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

Wenn Sie Texte in einer Sprache hinzufügen, die von rechts nach links geschrieben ist, beachten Sie, dass das endgültige Aussehen von Nachrichten von rechts nach links weitgehend davon abhängt, wie die Dienste sie darstellen. Bewährte Methoden zur Erstellung von Nachrichten, die so genau wie möglich angezeigt werden, finden Sie unter [Erstellen von Nachrichten von]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) rechts nach links.

#### Webhook-URL

Die Webhook-URL (oder HTTP-URL) gibt Ihren Endpunkt an. Der Endpunkt ist der Ort, an den Sie die Informationen senden, die Sie im Webhook erfassen. 

Wenn Sie Informationen an einen Anbieter senden möchten, sollte der Anbieter diese URL in seiner API-Dokumentation angeben. Wenn Sie Informationen an Ihre eigenen Systeme senden, fragen Sie Ihr Entwicklerteam, ob Sie die richtige URL verwenden. 

Braze lässt nur URLs zu, die über die Standardports `80` (HTTP) und `443` (HTTPS) kommunizieren.

##### Liquid verwenden

Sie können Ihre Webhook-URLs mit [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) personalisieren. Bei bestimmten Endpunkten kann es vorkommen, dass Sie einen Nutzer:innen identifizieren oder benutzerspezifische Informationen als Teil Ihrer URL angeben müssen. Wenn Sie Liquid verwenden, stellen Sie sicher, dass Sie für jede nutzerspezifische Information, die Sie in Ihrer URL verwenden, einen [Standardwert]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) angeben.

#### HTTP-Methode

Die [HTTP-Methode]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#methods), die Sie verwenden sollten, hängt von dem Endpunkt ab, an den Sie Informationen senden. In den meisten Fällen werden Sie POST verwenden.

#### Anfragetext

Der Anfragetext ist die Information, die an die von Ihnen angegebene URL gesendet wird. Sie können den Text Ihrer Webhook-Anfrage mit JSON Schlüssel-Wert-Paaren oder Rohtext erstellen.

##### JSON-Schlüssel-Wert-Paare

Mit JSON-Schlüssel-Wert-Paaren können Sie ganz einfach eine Anfrage für einen Endpunkt schreiben, der ein JSON-Format erwartet. Sie können dies nur mit einem Endpunkt verwenden, der eine JSON-Anfrage erwartet. Wenn Ihr Schlüssel zum Beispiel `message_body` lautet, könnte der entsprechende Wert `Your order just arrived!` sein. Nachdem Sie Ihr Schlüssel-Wert-Paar eingegeben haben, konfiguriert der Editor Ihre Anfrage in JSON-Syntax, und eine Vorschau Ihrer JSON-Anfrage wird automatisch eingeblendet.

![Body der Anfrage auf JSON Schlüssel-Wert-Paare eingestellt.]({% image_buster /assets/img/webhook_json_1.png %})

Sie können Ihre Schlüssel-Wert-Paare mit Liquid personalisieren, z.B. indem Sie ein beliebiges Benutzerattribut, ein [benutzerdefiniertes Attribut]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#additional-notes-and-best-practices) oder eine [Ereigniseigenschaft]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) in Ihre Anfrage aufnehmen. Sie können zum Beispiel den Vornamen und die E-Mail-Adresse eines Kunden in Ihre Anfrage aufnehmen. Achten Sie darauf, dass Sie für jedes Attribut einen [Standardwert]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) angeben.

##### Rohtext

Die Option „Rohtext“ bietet Ihnen die Flexibilität, eine Anfrage für einen Endpunkt zu schreiben, der einen Textkörper in einem beliebigen Format erwartet. Sie können dies beispielsweise verwenden, um eine Anfrage für einen Endpunkt zu schreiben, der Ihre Anfrage im XML-Format erwartet. 

Sowohl die [Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) als auch die [Internationalisierung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) mit Liquid wird im Rohtext unterstützt.

![Ein Beispiel für eine Anfrage mit Rohtext in Liquid.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

Wenn Sie den [Anfrage-Header](#request-headers-optional) `Content-Type` auf `application/x-www-form-url-encoded` setzen, muss der Anfragetext als URL-kodierter String formatiert werden. Zum Beispiel:

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![Body der Anfrage mit URL-kodiertem String.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## Schritt 3: Konfigurieren Sie zusätzliche Einstellungen

#### Kopfzeilen der Anfrage (optional)

Bestimmte Endpunkte erfordern möglicherweise, dass Sie Header in Ihre Anfrage aufnehmen. Im Abschnitt **Verfassen** des Composers können Sie so viele Kopfzeilen wie nötig hinzufügen.

![Beispiele für Anfrage-Header für die Schlüssel "Autorisierung" und "Content-Typ".]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

Gängige Anfrage-Header sind `Content-Type`-Spezifikationen (die beschreiben, welche Art von Daten im Text zu erwarten ist, z. B. XML oder JSON) und Autorisierungs-Header, die Ihre Zugangsdaten bei Ihrem Anbieter oder System enthalten. 

Content-Typ-Spezifikationen müssen den Schlüssel `Content-Type` verwenden. Übliche Werte sind `application/json` oder `application/x-www-form-urlencoded`.

Autorisierungs-Header müssen den Schlüssel `Authorization` verwenden. Übliche Werte sind {% raw %} `Bearer {{YOUR_TOKEN}}` oder `Basic {{YOUR_TOKEN}}` {% endraw %}, wobei `YOUR_TOKEN` die von Ihrem Anbieter oder System bereitgestellten Zugangsdaten sind.

## Schritt 4: Nachricht als Test senden

Braze empfiehlt Ihnen, den Webhook zu testen, bevor Sie Ihre Kampagne live schalten, um sicherzustellen, dass die Anfrage richtig formatiert ist.

Wechseln Sie dazu auf die Registerkarte **Test** und senden Sie einen Test-Webhook. Sie können den Webhook als zufälligen Benutzer, einen bestimmten Benutzer (durch Eingabe der E-Mail-Adresse oder der externen Benutzer-ID) oder einen benutzerdefinierten Benutzer mit von Ihnen gewählten Attributen testen.  

Nach dem Senden des Test-Webhooks wird ein Dialogfeld mit der Antwortnachricht angezeigt. Wenn die Webhook-Anfrage nicht erfolgreich war, lesen Sie die Fehlermeldung, um Hilfe bei der Fehlerbehebung Ihres Webhooks zu erhalten. Das folgende Beispiel zeigt die Antwort auf einen Webhook mit einer ungültigen Webhook-URL.

```json
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

## Schritt 5: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

{% tabs %}
{% tab Campaign %}

Als Nächstes erstellen Sie den Rest Ihrer Kampagne. In den folgenden Abschnitten erfahren Sie mehr darüber, wie Sie unsere Tools zur Erstellung von Webhooks am besten einsetzen.

#### Wählen Sie einen Zeitplan für die Zustellung oder triggern Sie

Webhooks können auf der Grundlage eines Zeitplans, einer Aktion oder eines API-Triggers zugestellt werden. Mehr dazu erfahren Sie unter [Planen Ihrer Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Für die aktionsbasierte Zustellung können Sie auch die Dauer der Kampagne und die [Ruhezeiten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) festlegen.

In diesem Schritt können Sie auch Zustellungskontrollen festlegen, z. B. dass Nutzer:innen wieder für den Empfang der Kampagne [zugelassen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) werden oder [Frequency-Capping-Regeln]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) aktiviert werden.

#### Wählen Sie Benutzer als Zielgruppe aus

Als Nächstes müssen Sie mithilfe von Segmenten oder Filtern eine [Zielgruppe erstellen]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/). In diesem Schritt wählen Sie die größere Zielgruppe aus Ihren Segmenten aus und grenzen dieses Segment mit unseren Filtern weiter ein, wenn Sie möchten. Sie erhalten automatisch eine Vorschau darauf, wie die ungefähre Anzahl der Segmente im Moment aussieht. Denken Sie daran, dass die genaue Segmentzugehörigkeit immer erst kurz vor dem Versand der Nachricht berechnet wird.

{% multi_lang_include target_audiences.md %}

#### Wählen Sie Konversionsereignisse aus

Mit Braze können Sie nachverfolgen, wie oft Benutzer nach Erhalt einer Kampagne bestimmte Aktionen, d.h. [Conversion Events]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), durchführen. Sie haben die Möglichkeit, ein Zeitfenster von bis zu 30 Tagen zuzulassen, in dem eine Konversion gezählt wird, wenn der Nutzer:innen die angegebene Aktion durchführt.

{% endtab %}

{% tab Canvas %}

Falls Sie dies noch nicht getan haben, vervollständigen Sie die restlichen Abschnitte Ihres Canvas-Schrittes. Weitere Einzelheiten zum Aufbau des restlichen Canvas, zur Implementierung von multivariaten Tests und intelligenter Auswahl und mehr finden Sie im Schritt [Aufbau Ihres Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) in unserer Canvas-Dokumentation.

{% endtab %}
{% endtabs %}

## Schritt 6: Überprüfen und einsetzen

Nachdem Sie den letzten Teil Ihrer Kampagne oder Ihres Canvas erstellt haben, überprüfen Sie die Details, testen Sie sie und senden Sie sie ab!

## Was Sie wissen sollten

### Fehler, Wiederholungslogik und Zeitüberschreitungen

Webhooks basieren auf Braze-Servern, die Anfragen an einen externen Endpunkt stellen, und dabei können gelegentlich Fehler auftreten. Zu den häufigsten Fehlern gehören Syntaxfehler, abgelaufene API-Schlüssel, Rate-Limits und unerwartete serverseitige Probleme. Bevor Sie eine Webhook Kampagne senden:

- Testen Sie Ihren Webhook auf Syntaxfehler
- Stellen Sie sicher, dass personalisierte Variablen Standardwerte haben

Wenn Ihr Webhook nicht gesendet werden kann, wird eine Fehlernachricht im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) protokolliert, die Details wie den Zeitstempel des Fehlers, den Namen der App und Details zum Fehler enthält.

![Webhook-Fehler mit der Nachricht "Es muss ein aktives Token verwendet werden, um Informationen über den aktuellen Nutzer:in abzufragen".]({% image_buster /assets/img_archive/webhook-error.png %})

Wenn die Nachricht über die Fehlerquelle nicht eindeutig genug ist, sollten Sie die Dokumentation des von Ihnen verwendeten API Endpunkts überprüfen. Darin finden Sie in der Regel eine Erläuterung der Fehlercodes, die der Endpunkt verwendet, sowie die typischen Ursachen für diese Fehler.

#### Antwort-Codes und Logik für Wiederholungsversuche

Wenn die Webhook-Anfrage gesendet wird, gibt der empfangende Server einen Antwort-Code zurück, der angibt, was mit der Anfrage geschehen ist. Die folgende Tabelle fasst die verschiedenen Antworten zusammen, die der Server senden kann, wie sie sich auf die Kampagnenanalyse auswirken und ob Braze im Falle von Fehlern versuchen wird, die Kampagne erneut zuzustellen:

| Antwortcode | Als erhalten markiert? | Wiederholungsversuche? |
|---------------|-----------|----------|
| `20x` (Erfolg)  | Ja |   --  |
| `30x` (Weiterleitung)  | Kein:e | Kein:e |
| `408` (Zeitüberschreitung der Anfrage)  | Kein:e | Ja |
| `429` (Rate-Limit aktiv)  | Kein:e | Ja |
| `Other 4XX` (Client-Fehler)  | Kein:e | Kein:e |
| `5XX` (Serverfehler)   | Kein:e | Ja |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Braze wiederholt die oben genannten Status Codes bis zu fünf Mal innerhalb von 30 Minuten mit exponentiellem Backoff. Wenn wir Ihren Endpunkt nicht erreichen können, werden die Wiederholungsversuche möglicherweise über einen Zeitraum von 24 Stunden verteilt.<br><br>Für jeden Webhook sind 90 Sekunden zulässig, bevor er abläuft.
{% endalert %}

#### Fehlerbehebung und zusätzliche Fehlerdetails

Ausführliche Erklärungen, Schritte zur Fehlerbehebung und Hinweise zur Behebung bestimmter Webhook-Fehler finden Sie unter [Fehlerbehebung bei Webhook- und Connected-Content-Anfragen]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/). Außerdem finden Sie in Braze-Currents weitere Erklärungen dazu, wie unser System zur Erkennung ungesunder Hosts funktioniert und wie Braze Fehlerbenachrichtigungen durch automatisierte E-Mails und zusätzliche Protokollierung bereitstellt.

### IP-Allowlisting {#ip-allowlisting}

Wenn ein Webhook von Braze gesendet wird, stellen die Braze-Server Netzwerkanfragen an unsere Kund:innen oder an Server von Drittanbietern. Mit IP-Allowlisting können Sie überprüfen, ob die Webhook-Anfragen von Braze stammen, was eine zusätzliche Sicherheitsebene darstellt.

Braze sendet Webhooks von den folgenden IPs. Die aufgelisteten IPs werden automatisch und dynamisch zu allen API-Schlüsseln hinzugefügt, für die ein Opt-in für Allowlisting erteilt wurde.

{% alert important %}
Wenn Sie einen Braze-to-Braze-Webhook erstellen und Allowlisting verwenden, sollten Sie alle folgenden IPs zulassen, einschließlich `127.0.0.1`.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='ips' %}

### Verwendung von Webhooks mit Braze-Partnern {#utilizing-webhooks}

Es gibt viele Möglichkeiten, Webhooks zu nutzen, und mit unseren Technologiepartnern (Alloys) können Sie Webhooks nutzen, um Ihre Kommunikation direkt mit Ihren Kunden und Benutzern zu verbessern.

Weitere Informationen:
* [Messenger]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/remerge/)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/)
* Und viele weitere unserer [Technologiepartner]({{site.baseurl}}/partners/home/)!


