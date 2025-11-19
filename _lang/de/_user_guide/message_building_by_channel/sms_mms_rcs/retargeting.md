---
nav_title: "Retargeting von Nutzer:innen"
article_title: "Retargeting von Nutzer:innen"
description: "Dieser referenzierte Artikel beschreibt, wie Nutzer:innen ihre Nachrichten über die SMS- und RCS-Interaktionen eines Nutzers retargeten können."
page_type: reference
page_order: 4
alias: /sms_mms_rcs_user_retargeting/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS

---

# Retargeting von Nutzer:innen

> Braze ändert nicht nur den Abonnementstatus des Benutzers und sendet automatische Antworten auf der Grundlage eingehender Schlüsselwörter, sondern zeichnet auch Interaktionen mit dem Benutzerprofil auf, um Nachrichten zu filtern und auszulösen.<br><br>Diese Filter und Trigger ermöglichen es Ihnen, Aktionen auf der Grundlage von Nutzern zu filtern, die SMS-, MMS- und RCS-Kampagnen gesendet oder darauf geantwortet haben, oder das Engagement von Nutzern:innen zu fördern, die auf Kurz-URLs geklickt haben.

{% alert tip %}
Wenn Sie mehr über benutzerdefinierte Schlüsselwörter erfahren möchten und darüber, wie Sie Zwei-Wege-Nachrichten einrichten, um diese Retargeting-Optionen zu nutzen, lesen Sie unseren Artikel über [benutzerdefinierte Schlüsselwörter]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/keyword_handling/).
{% endalert %}  

## Retargeting-Optionen

{% alert note %}
Beim Aufbau von Zielgruppen mit dem Retargeting von Nutzer:innen möchten Sie möglicherweise bestimmte Nutzer:innen auf der Grundlage ihrer Präferenzen ein- oder ausschließen, um Datenschutzgesetze einzuhalten, z. B. das Recht „Nicht verkaufen oder weitergeben“ gemäß dem CUP. Vermarkter sollten die entsprechenden Filter für die Eignung von Nutzern in ihre Canvas- und/oder Kampagneneingabekriterien implementieren.
{% endalert %}

### Nutzer:innen nach SMS, MMS und RCS filtern

Nutzer:innen können danach gefiltert werden, wann sie zuletzt eine SMS, MMS oder RCS erhalten haben oder ob sie eine SMS, MMS oder RCS von einer bestimmten Kampagne erhalten haben. Filter können im Schritt **Targeting Zielgruppen** des Kampagnen-Builders festgelegt werden. 

**Filter nach zuletzt empfangener SMS/MMS/RCS**<br>
Segmentierungsfilter Letzte empfangene SMS nach dem 8\. Dezember 2020.]({% image_buster /assets/img/sms/filter2.png %})

**Filter nach empfangenen Nachrichten aus SMS/MMS/RCS-Kampagnen**<br>
Filtert Nutzer:innen, die eine Nachricht aus einer bestimmten Kampagne erhalten haben. Mit diesem Filter haben Sie auch die Möglichkeit, diejenigen herauszufiltern, die keine Nachrichten aus einer Kampagne erhalten haben. <br>
![Segmentierungs-Filter Hat Nachricht von Kampagne "SMS Retargeting" erhalten.]({% image_buster /assets/img/sms/filter1.png %})

### Triggern Sie Nachrichten, wenn Nutzer:innen SMS, MMS oder RCS erhalten. {#trigger-messages}

Um Nachrichten auszulösen, wenn Nutzer:innen SMS-, MMS- oder RCS-Nachrichten aus einer bestimmten Kampagne erhalten, wählen Sie als Aktion triggern für eine aktionsbasierte Kampagne **Interaktion mit Kampagne** aus. Wählen Sie anschließend **SMS empfangen** und die gewünschte SMS-, MMS- oder RCS-Kampagne aus.

![]({% image_buster /assets/img/sms/trigger.png %})

### Nach Links für erweitertes Tracking filtern

Retargeting von Nutzern, die auf Kampagnen mit [erweiterten Tracking-Links]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) geklickt haben.
Nur Kampagnen, bei denen das erweiterte Tracking aktiviert ist, erscheinen in den folgenden Dropdown-Listen:

**Retargeting von Nutzer:innen, die auf eine bestimmte SMS-, MMS- oder RCS-Kampagne geklickt haben**
1. Erstellen Sie ein Segment mit dem Filter **Geklickte/geöffnete Kampagne**.
2. Wählen Sie **den angeklickten verkürzten SMS-Link** aus.
3. Wählen Sie die gewünschte Kampagne.

![]({% image_buster /assets/img/sms/retargeting5.png %})

**Retargeting von Nutzer:innen, die auf einen bestimmten Canvas-Schritt geklickt haben**
1. Erstellen Sie ein Segment mit dem Filter **Geklickter/geöffneter Schritt**.
2. Wählen Sie **den angeklickten verkürzten SMS-Link** aus.
3. Wählen Sie die gewünschte Leinwand und Leinwandstufe.

![]({% image_buster /assets/img/keyword_example1.jpg %})

## Keyword-spezifisches Retargeting

Zusätzlich zu den drei Standard-Keyword-Kategorien (Opt-in, Opt-out und Hilfe) können Sie bis zu 25 eigene Keyword-Kategorien erstellen, mit denen Sie beliebige Keywords und Antworten identifizieren können. Diese Kategorien können zum Filtern und Retargeting verwendet werden. Wenn Sie mehr über globale Schlüsselwortkategorien und deren Einrichtung erfahren möchten, lesen Sie [Schlüsselwortverarbeitung]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/). 

### Nach Aktualität filtern

Filtern Sie nach der Häufigkeit, mit der ein Nutzer:innen auf Ihre SMS, MMS oder RCS antwortet. Dieser Filter wertet das letzte Datum aus, an dem ein Nutzer:in eine eingehende Nachricht gesendet hat, die in eine der Schlüsselwortkategorien fällt. 

![Segmentierungsfilter Letzte gesendete SMS an Abo-Gruppe "Marketing SMS" mit dem Schlüsselwort "Opt-in" nach dem 11\. August 2020.]({% image_buster /assets/img/sms/retargeting1.png %})

### Nach Kampagne oder Canvas-Attribution filtern

Filter für Nutzer:innen, die auf eine bestimmte SMS-, MMS- oder RCS-Kampagne oder Canvas-Komponente, Schlüsselwortkategorie oder Tag geantwortet haben.

**Filter nach Antworten auf eine bestimmte Kampagne mit Stichwortkategorie**<br>
![Kampagne mit dem Filter "Hat auf SMS geantwortet" für Kampagne "SMS-283" "Aktion". Unter dem Filter wird die Funktion erwähnt: „Dieser Filter läuft 25 Monate nach dem Versand der letzten Nachricht von „Aktion“ ab, wenn er nicht in einer aktiven Kampagne verwendet wird.“]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

**Nach Beantwortung einer Kampagne oder eines Canvas mit einem bestimmten Tag filtern**
![Kampagne mit dem Filter "Hat auf SMS geantwortet" für Kampagne oder Canvas mit Tag "Curbside Messaging Service C".]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

**Nach der Antwort auf einen bestimmten Schritt filtern**
![Kampagne mit dem Filter "Hat auf SMS geantwortet" für Schritt "SMS Double Opt" "Schritt - Hilfe".]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### Nachrichten nach Keyword triggern

Nachrichten können ausgelöst werden, wenn Benutzer Nachrichten auf der Grundlage von Schlüsselwortkategorien (der Benutzer hat eines der Schlüsselwörter gesendet) oder anderen Schlüsselwörtern (der Benutzer hat ein Schlüsselwort gesendet, das nicht in eine der bestehenden Kategorien fällt) ankommen lassen. Diese Trigger werden im Schritt „Zustellung“ des Kampagnen-Builders festgelegt.

Bei der Auswertung, ob eine eingehende Nachricht ein definiertes Trigger-Event erfüllt, werden die führenden und nachfolgenden Leerzeichen entfernt, bevor die Auswertung beginnt.

{% alert tip %}
Wenn ein aktionsbasiertes Canvas durch eine eingehende SMS- oder MMS-Nachricht ausgelöst wird, können Sie in jedem Canvas-Schritt bis zum nächsten Aktions-Pfad auf [unterstützte SMS Liquid-Eigenschaften]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) referenzieren.
{% endalert %}

**Nach Kategorie der eingehenden Keywords triggern**<br>
![Aktionsbasierte SMS-Kampagne mit dem Segmentierungsfilter Gesendetes Schlüsselwort "Opt-in" an Abo-Gruppe "Marketing SMS".]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

**Nach beliebigen Keywords triggern**<br>
Beachten Sie, dass Sie beim Triggern einer Nachricht auf eine „Sonstige“-Keyword-Antwort die Möglichkeit haben, den Keyword-Text auf eine exakte Textübereinstimmung zu überprüfen. Für dieses Spiel gelten die gleichen Regeln wie oben beschrieben: Es wird nur die **exakte Ein-Wort-Nachricht** verarbeitet (Groß- und Kleinschreibung _wird nicht berücksichtigt_). Ein Keyword, das von `Hello Braze!` gesendet wird, würde die Kriterien im folgenden Beispiel nicht erfüllen.
![Aktionsbasierte SMS-Kampagne mit der Schlüsselwortkategorie "Sonstige", bei der die Nachricht genau "Hallo" oder "Hey" lautet.]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

**Template-Keywords**<br>
Wenn Sie eine Kampagne oder eine Canvas-Komponente bei einer eingehenden SMS oder MMS triggern, können Sie optional die Text- oder Medienanhänge, die Ihr:e Nutzer:in gesendet hat, in den Textkörper Ihrer Kampagne oder Ihres Canvas mit Liquid einfügen. Auf diese Weise können Sie auf die Antwort des Benutzers zugreifen, die Sie dann in Ihre Antwort einfügen, eine bedingte Logik darauf anwenden oder alles andere tun können, was Sie mit Liquid tun können. 

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

```liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}

[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}
