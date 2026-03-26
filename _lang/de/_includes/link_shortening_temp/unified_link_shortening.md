Link-Shortening ermöglicht es Ihnen, URLs in SMS- oder RCS-Nachrichten automatisch zu kürzen und Klickraten-Analytics zu erfassen. So erhalten Sie zusätzliche Engagement-Metriken, die Ihnen helfen zu verstehen, wie Nutzer:innen mit Ihren Kampagnen interagieren.

Link-Shortening kann auf [Nachrichtenvarianten-Ebene]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) sowohl in Kampagnen als auch in Canvases aktiviert werden. Wenn Link-Shortening aktiviert ist, werden Klicks als [SMS-Klick-Event]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) generiert und über Currents gesendet.

Links werden über unsere gemeinsame Short-Domain (`brz.ai`) oder Ihre benutzerdefinierte Link-Shortening-Domain gekürzt und sind ab dem Erstellungsdatum 9 Wochen lang gültig. Eine Beispiel-URL könnte etwa so aussehen: `https://brz.ai/8jshX2dj`.

## Link-Shortening verwenden

Um Link-Shortening zu verwenden, stellen Sie sicher, dass das Kontrollkästchen für Link-Shortening im Nachrichten-Editor aktiviert ist.

{% tabs %}
{% tab SMS composer %}

![SMS-Nachrichten-Editor mit aktiviertem Kontrollkästchen für Link-Shortening.]({% image_buster /assets/img/link_shortening/shortening1.png %})

{% endtab %}
{% tab RCS composer %}

![RCS-Nachrichten-Editor mit aktiviertem Kontrollkästchen für Link-Shortening.]({% image_buster /assets/img/link_shortening/shortening1_rcs.png %})

{% endtab %}
{% endtabs %}

Braze erkennt nur URLs, die mit `http://` oder `https://` beginnen. Wenn eine URL erkannt wird, aktualisiert sich der **Vorschau**-Abschnitt mit einer Platzhalter-URL. Braze schätzt die Nachrichtenlänge nach dem Kürzen, aber eine Warnung fordert Sie auf, eine:n Testnutzer:in auszuwählen und die Nachricht als Entwurf zu speichern, um eine genauere Schätzung zu erhalten.

![Nachrichten-Editor mit einer langen URL im Feld „Nachricht" und einem generierten gekürzten Link in der Vorschau.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### UTM-Parameter hinzufügen

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Liquid-Personalisierung in URLs

Sie können Ihre URL direkt im Braze-Editor dynamisch erstellen, sodass Sie dynamische UTM-Parameter zu Ihren URLs hinzufügen oder Nutzer:innen eindeutige Links senden können (z. B. um Nutzer:innen zu ihrem Warenkorb-Abbruch oder zu einem bestimmten Produkt weiterzuleiten, das wieder auf Lager ist).

### Eine URL mit unterstützten Liquid-Personalisierungs-Tags erstellen

URLs können dynamisch mithilfe beliebiger [unterstützter Liquid-Personalisierungs-Tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) generiert werden.

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Wir unterstützen auch das Kürzen von benutzerdefinierten Liquid-Variablen. Nachfolgend finden Sie einige Beispiele:

### Eine URL mit Liquid-Variablen erstellen

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Von Liquid-Variablen gerenderte URLs kürzen

Wir kürzen URLs, die von Liquid gerendert werden, auch solche, die in API-Trigger-Eigenschaften enthalten sind. Wenn beispielsweise {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} eine gültige URL darstellt, kürzen und tracken wir diese URL, bevor die Nachricht gesendet wird.

### URLs im `/messages/send`-Endpunkt kürzen

Link-Shortening ist auch für reine API-Nachrichten über den [`/messages/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) aktiviert. Eine vollständige Liste der Anfrage-Parameter finden Sie unter [Anfrage-Parameter]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Ja | Boolescher Wert | Setzen Sie `link_shortening_enabled` auf `true`, um Link-Shortening zu aktivieren. Für die Nutzung von Tracking müssen eine `campaign_id` und eine `message_variation_id` vorhanden sein.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Testen

Bevor Sie Ihre Kampagne oder Ihr Canvas starten, empfiehlt es sich, Ihre Nachricht zunächst in der Vorschau anzuzeigen und zu testen. Gehen Sie dazu zum Tab **Test**, um eine SMS- oder RCS-Nachricht an [Inhalts-Testgruppen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) oder eine:n einzelne:n Nutzer:in in der Vorschau anzuzeigen und zu senden.

Diese Vorschau wird mit der relevanten Personalisierung und der gekürzten URL aktualisiert. Die Zeichenanzahl und die [abrechenbaren Segmente]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) werden ebenfalls aktualisiert, um die gerenderte Personalisierung und die gekürzte URL widerzuspiegeln.

Stellen Sie sicher, dass Sie die Kampagne oder das Canvas speichern, bevor Sie eine Testnachricht senden, um eine Darstellung der gekürzten URL zu erhalten, die in Ihrer Nachricht versendet wird. Wenn die Kampagne oder das Canvas vor dem Testversand nicht gespeichert wird, enthält der Testversand eine Platzhalter-URL.

{% alert important %}
Wenn ein Entwurf innerhalb eines aktiven Canvas erstellt wird, wird keine gekürzte URL generiert. Die tatsächliche gekürzte URL wird erst generiert, wenn der Canvas-Entwurf aktiviert wird.
{% endalert %}

![Tab „Test" der Nachricht mit Feldern zur Auswahl von Testempfänger:innen.]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
Liquid-Personalisierung und gekürzte URLs werden im Tab **Test** erst nach Auswahl einer/eines Nutzer:in gerendert. Stellen Sie sicher, dass ein:e Nutzer:in ausgewählt ist, um eine genaue Zeichenanzahl zu erhalten.
{% endalert %}

## Klick-Tracking

Wenn Link-Shortening aktiviert ist, enthält die Tabelle **SMS/MMS/RCS Performance** eine Spalte mit dem Titel **Klicks gesamt**, die eine Anzahl der Klick-Events pro Variante und eine zugehörige Klickrate anzeigt. Weitere Details zu Metriken finden Sie unter [Nachrichten-Performance]({{site.baseurl}}/sms_mms_rcs_reporting/).

![Tabelle mit SMS- und MMS-Performance-Metriken.]({% image_buster /assets/img/link_shortening/shortening4.png %})

Die Tabellen **Historische Performance** und **SMS/MMS/RCS Performance** bieten auch eine Option für **Klicks gesamt** und zeigen eine tägliche Zeitreihe der Klick-Events an. Klicks werden bei der Weiterleitung gezählt (z. B. wenn ein:e Nutzer:in einen Link besucht) und können pro Nutzer:in mehrfach gezählt werden.

## Retargeting von Nutzer:innen

Hinweise zum Retargeting finden Sie unter [Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Kann ich sehen, welche einzelnen Nutzer:innen auf eine URL klicken?

Ja. Sie können Nutzer:innen, die auf URLs geklickt haben, mithilfe der [SMS-Retargeting-Filter]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) oder der SMS-Klick-Events (`users.messages.sms.ShortLinkClick`) retargeten, die über Currents gesendet werden.

### Funktioniert Link-Shortening mit Deeplinks oder Universal Links?

Link-Shortening funktioniert nicht mit Deeplinks. Alternativ können Sie Universal Links von Drittanbietern wie Branch oder Appsflyer kürzen, allerdings kann es bei Nutzer:innen zu einer kurzen Weiterleitung oder einem „Flicker"-Effekt kommen. Dies geschieht, weil der gekürzte Link zunächst über das Internet geleitet wird, bevor er zum Universal Link aufgelöst wird, der das Öffnen der App unterstützt. Darüber hinaus kann Braze keine Probleme beheben, die beim Kürzen von Universal Links auftreten können, wie z. B. das Unterbrechen der Attribution oder unerwartete Weiterleitungen.

{% alert note %}
Testen Sie die Nutzererfahrung, bevor Sie Link-Shortening mit Universal Links implementieren, um sicherzustellen, dass es Ihren Erwartungen entspricht.
{% endalert %}

### Sind `send_ids` mit SMS-Klick-Events verknüpft?

Nein. Sie können `send_ids` jedoch in der Regel mit Klick-Events verknüpfen, indem Sie den [Query Builder]({{site.baseurl}}/query_builder/) verwenden, um Currents-Daten mit dieser Abfrage abzufragen:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```