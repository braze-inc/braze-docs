---
nav_title: Klick-Tracking
article_title: Klick-Tracking
page_order: 3
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie das Tracking von Klicks in Ihren WhatsApp Nachrichten aktivieren, verkürzte Links testen, Ihre angepasste Domain in verfolgten Links verwenden und vieles mehr."
page_type: reference
alias: "/whatsapp_click_tracking/"
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Klick-Tracking

> Auf dieser Seite erfahren Sie, wie Sie das Tracking von Klicks in Ihren WhatsApp Nachrichten aktivieren, verkürzte Links testen, Ihre angepasste Domain in verfolgten Links verwenden und vieles mehr.

Mit dem Tracking von Klicks können Sie messen, wann jemand auf einen Link in Ihrer WhatsApp Nachricht tippt. So erhalten Sie einen klaren Überblick darüber, welche Inhalte das Engagement fördern. Braze verkürzt Ihre URLs, fügt im Hintergrund Tracking hinzu und protokolliert Klicks, sobald sie stattfinden.

Sie können das Tracking von Klicks sowohl in Nachrichten als auch in Templates einschalten. Es funktioniert mit Links in Buttons und Bodytext und unterstützt personalisierte URLs und angepasste Domains. Nach der Aktivierung sehen Sie die Daten der Klicks in Ihren WhatsApp Performance-Berichten und können die Nutzer:innen anhand der Klicks segmentieren.

{% alert note %}
Click Tracking funktioniert nicht mit Deeplinks. Sie können universelle Links von Anbietern wie Branch oder Appsflyer kürzen, aber Braze ist nicht in der Lage, Probleme zu beheben, die dabei auftreten können (z. B. die Unterbrechung der Attribution oder eine Umleitung).
{% endalert %}

## Funktionsweise

### Responsive Nachrichten 

So richten Sie Click Tracking für responsive Nachrichten ein:
1. Erstellen Sie eine Nachricht, die einen Call-to-Action (CTA) Button mit einer Website URL enthält.
2. Aktivieren Sie das Tracking von Klicks, indem Sie auf den entsprechenden Button auf der Schnittstelle klicken.

Der Link wird auf die Braze Domain oder die für die Abo-Gruppe angegebene angepasste Domain verkürzt und für den Nutzer:innen personalisiert.

Alle statischen URLs, die mit `http://` oder `https://` beginnen, werden gekürzt. Verkürzte URLs, die eine Liquid Personalisierung enthalten (z.B. Tracking Targeting auf Nutzerebene), sind zwei Monate lang gültig.

![WhatsApp Nachrichten-Editor mit Inhalt und einem Button.]({% image_buster /assets/img/whatsapp/click_tracking/message_composer.png %})

### Template-Nachrichten 

Bei Nachrichten mit Template muss die Basis-URL bei der Erstellung des Templates korrekt angegeben werden, um das Tracking von Klicks zu aktivieren.

#### Schritt 1: Erstellen Sie ein Template für das Tracking von Klicks in WhatsApp

1. Erstellen Sie in Ihrem WhatsApp Manager:in eine Basis-URL, die entweder Ihre angepasste Domain oder `brz.ai` ist.
2. Stellen Sie sicher, dass die in der Vorlage enthaltenen Links mit Klick Tracking kompatibel sind.
3. Ändern Sie die Variablen des Templates nicht mehr, nachdem Sie es als Kampagne in Braze eingerichtet haben; nachgelagerte Änderungen können nicht mehr übernommen werden.
4. Für CTA-Buttons wählen Sie **Dynamisch** und geben dann die Basis-URL an (`brz.ai` oder Ihre angepasste Domain).<br><br>![Abschnitt, um einen Aufruf zum Handeln zu erstellen.]({% image_buster /assets/img/whatsapp/click_tracking/create_cta.png %})<br><br>
5. Für Links im Textkörper entfernen Sie beim Schreiben des Templates in Ihrem WhatsApp Manager:in alle eingefügten Leerzeichen für Links, die im Textkörper enthalten sind und die Sie tracken möchten.<br><br>![Textfeld zur Eingabe des Inhaltskörpers für den Aufruf zur Aktion.]({% image_buster /assets/img/whatsapp/click_tracking/cta_textbox.png %})

#### Schritt 2: Vervollständigen Sie Ihr Template in Braze

Bei der Erstellung erkennt Braze automatisch, welche Templates unterstützbare URL Domains haben, sowohl im Fließtext als auch für CTA Buttons. Der Status wird am unteren Rand des Templates angezeigt. 

!["Link Status" Abschnitt zeigt einen aktiven Status für das Klick Tracking.]({% image_buster /assets/img/whatsapp/click_tracking/link_status.png %}){: style="max-width:70%;"}

- **Unterstützte Links:** Für Links, die mit der passenden Basis-URL übermittelt werden, ist das Klick Tracking aktiviert.
- **Teilweise unterstützte Links:** Wenn einige Links in einem Template als vollständige URLs übermittelt werden, wird das Click Tracking **nicht** auf diese Links angewendet.
- **Nicht unterstützte Links:** Links ohne eine genehmigte Basis-URL verfügen **nicht** über die Möglichkeit des Klick Trackings.

Die Ziel-URL muss für jeden Link mit einer Basis-URL angegeben werden, die entweder `brz.ai` oder Ihrer angepassten Domain entspricht. 

!["Buttons"-Abschnitt mit Feldern für den Button-Namen, die Website-URL und die Klick-Tracking-URL.]({% image_buster /assets/img/whatsapp/click_tracking/buttons.png %}){: style="max-width:70%;"}

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

## Flüssige Personalisierung in URLs

Sie können Ihre URL direkt im Braze Composer dynamisch aufbauen, so dass Sie dynamische UTM-Parameter zu Ihren URLs hinzufügen oder Benutzern einzigartige Links senden können (z. B. die Weiterleitung zu einem abgebrochenen Warenkorb oder zu einem bestimmten Produkt, das wieder auf Lager ist).
URLs können durch die Verwendung beliebiger unterstützter Tags zur Personalisierung in Liquid dynamisch generiert werden.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Wir unterstützen auch die Verkürzung von angepassten Liquid-Variablen, wie in diesen Beispielen:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Kürzen Sie URLs, die von Liquid-Variablen gerendert werden

Braze verkürzt URLs, die von Liquid gerendert werden, auch solche, die in API-triggernden Eigenschaften enthalten sind. Wenn zum Beispiel {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} eine gültige URL darstellt, werden wir diese URL vor dem Versand der WhatsApp Nachricht kürzen und tracken.

## Testen

Bevor Sie Ihre Kampagne oder Ihr Canvas einführen, sollten Sie Ihre Nachricht zunächst in einer Vorschau testen. Gehen Sie dazu auf den Tab **Test**, um eine Vorschau zu sehen und eine WhatsApp an Inhaltstestgruppen oder einen einzelnen Nutzer:innen zu senden.

Diese Vorschau wird mit der entsprechenden Personalisierung und der verkürzten URL aktualisiert. 

{% alert important %}
Wenn ein Entwurf innerhalb eines aktiven Canvas erstellt wird, wird keine verkürzte URL generiert. Die eigentliche verkürzte URL wird generiert, wenn der Canvas-Entwurf aktiviert wird.
{% endalert %}

## Berichterstattung

Wenn das Tracking von Klicks aktiviert ist oder mit unterstützten Templates verwendet wird, enthält die WhatsApp Performance-Tabelle die Spalte **Gesamtklicks**, in der die Anzahl der Klick-Ereignisse pro Variante und die zugehörige Klickrate angezeigt werden. Weitere Einzelheiten zu den Metriken von WhatsApp finden Sie unter [WhatsApp Nachrichten Performance]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics).

![WhatsApp Nachricht Canvas-Schritt.]({% image_buster /assets/img/whatsapp/click_tracking/canvas_step.png %}){: style="max-width:30%;"}

Die Daten der Klicks werden automatisch im Analytics Dashboard angezeigt.

![WhatsApp Nachrichten Performance Tabelle.]({% image_buster /assets/img/whatsapp/click_tracking/message_performance.png %})

## Nutzer-Retargeting 

Sie können den Filter `Clicked/Opened Step` und die Interaktion `clicked tracked WhatsApp link` verwenden, um Nutzer:innen auf der Grundlage ihrer Interaktionen mit den Links zu segmentieren.

![Filtergruppe mit einem Filter für "geklickten Tracking WhatsApp Link".]({% image_buster /assets/img/whatsapp/click_tracking/filter_group.png %})

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Kann ich wissen, welche einzelnen Benutzer auf eine URL klicken?

Ja Wenn das Tracking von Klicks eingeschaltet ist (oder je nach Template-Konfiguration aktiviert ist), können Sie Nutzer:innen, die auf URLs geklickt haben, erneut ansprechen, indem Sie die Retargeting-Filter von WhatsApp oder die von Currents gesendeten WhatsApp-Klickereignisse (`users.messages.whatsapp.Click`) nutzen.

### Zählen Vorschauen auf dem WhatsApp Gerät als Klicks? 

Nein, sie tragen nicht zur Klickrate für WhatsApp Nachrichten bei. 

