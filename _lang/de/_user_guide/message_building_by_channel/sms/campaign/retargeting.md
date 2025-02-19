---
nav_title: "Retargeting von Nutzer:innen"
article_title: "Retargeting von SMS-Nutzer:innen"
description: "In diesem Referenzartikel erfahren Sie, wie Sie Ihre Nachrichten nach den SMS-Interaktionen der Nutzer:innen neu ausrichten können."
page_type: reference
tool:
  - Campaigns
channel:
  - SMS

---

# Retargeting von Nutzer:innen

> Braze ändert nicht nur den Abonnementstatus des Benutzers und sendet automatische Antworten auf der Grundlage eingehender Schlüsselwörter, sondern zeichnet auch Interaktionen mit dem Benutzerprofil auf, um Nachrichten zu filtern und auszulösen.<br><br>Mit diesen Filtern und Auslösern können Sie Benutzer filtern, die SMS-Nachrichten erhalten haben, SMS-Nachrichten aus einer bestimmten SMS-Kampagne erhalten haben und Nachrichten auslösen, wenn Benutzer SMS-Nachrichten aus einer bestimmten SMS-Kampagne erhalten. 

{% alert tip %}
Wenn Sie mehr über benutzerdefinierte Schlüsselwörter erfahren möchten und darüber, wie Sie Zwei-Wege-Nachrichten einrichten, um diese Retargeting-Optionen zu nutzen, lesen Sie unseren Artikel über [benutzerdefinierte Schlüsselwörter]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/).
{% endalert %}  

## Retargeting-Optionen

{% alert note %}
Beim Aufbau von Zielgruppen mit dem Retargeting von Nutzer:innen möchten Sie möglicherweise bestimmte Nutzer:innen auf der Grundlage ihrer Präferenzen ein- oder ausschließen, um Datenschutzgesetze einzuhalten, z. B. das Recht „Nicht verkaufen oder weitergeben“ gemäß dem CUP. Vermarkter sollten die entsprechenden Filter für die Eignung von Nutzern in ihre Canvas- und/oder Kampagneneingabekriterien implementieren.
{% endalert %}

### Benutzer nach SMS filtern

Benutzer können danach gefiltert werden, wann sie zuletzt eine SMS erhalten haben oder ob sie eine SMS aus einer bestimmten SMS-Kampagne erhalten haben. Filter können im Schritt Zielbenutzer des Kampagnenerstellers festgelegt werden. 

**Filtern nach zuletzt empfangenen SMS**<br>
![Segmentierungsfilter Letzte erhaltene SMS nach dem 8\. Dezember 2020.][2]

**Nach empfangenen Nachrichten aus SMS-Kampagnen filtern**<br>
Filtert Benutzer, die eine Nachricht von einer bestimmten SMS-Kampagne erhalten haben. Mit diesem Filter haben Sie auch die Möglichkeit, diejenigen herauszufiltern, die keine Nachrichten aus einer SMS-Kampagne erhalten haben. <br>
![Segmentierungsfilter Hat Nachricht von Kampagne "SMS Retargeting" erhalten.][1]

### Nachrichten triggern, wenn Nutzer:innen SMS erhalten {#trigger-messages}

Um Nachrichten auszulösen, wenn Benutzer SMS-Nachrichten von einer bestimmten Kampagne erhalten, wählen Sie **Interaktion mit Kampagne** als Auslöseaktion für eine aktionsbasierte Kampagne. Wählen Sie anschließend **SMS empfangen** und die gewünschte SMS-Kampagne.

![][3]

### Nach Links für erweitertes Tracking filtern

Retargeting von Nutzern, die auf Kampagnen mit [erweiterten Tracking-Links]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/) geklickt haben.
Nur Kampagnen, bei denen das erweiterte Tracking aktiviert ist, erscheinen in den folgenden Dropdown-Listen:

**Retargeting von Nutzer:innen, die auf eine bestimmte SMS-Kampagne geklickt haben**
1. Erstellen Sie ein Segment mit dem Filter **Geklickte/geöffnete Kampagne**.
2. Wählen Sie **angeklickte sms**.
3. Wählen Sie die gewünschte Kampagne.

![][15]

**Retargeting von Nutzer:innen, die auf einen bestimmten Canvas-Schritt geklickt haben**
1. Erstellen Sie ein Segment mit dem Filter **Geklickter/geöffneter Schritt**.
2. Wählen Sie **angeklickte sms**.
3. Wählen Sie die gewünschte Leinwand und Leinwandstufe.

![][16]

## Keyword-spezifisches Retargeting

Zusätzlich zu den drei Standard-Keyword-Kategorien (Opt-in, Opt-out und Hilfe) können Sie bis zu 25 eigene Keyword-Kategorien erstellen, mit denen Sie beliebige Keywords und Antworten identifizieren können. Diese Kategorien können zum Filtern und Retargeting verwendet werden. Wenn Sie mehr über SMS-Schlüsselwortkategorien und deren Einrichtung erfahren möchten, lesen Sie bitte [SMS Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/). 

### Nach Aktualität filtern

Nach der Aktualität filtern, mit der ein:e Nutzer:in auf Ihr SMS-Programm antwortet. Dieser Filter wertet das letzte Datum aus, an dem ein Benutzer eine eingehende SMS gesendet hat, die in eine der Schlüsselwortkategorien fällt. 

![Segmentierungsfilter Letzte gesendete SMS an die Abonnentengruppe "Marketing SMS" mit dem Schlüsselwort "Opt-in" nach dem 11\. August 2020.][6]

### Nach Kampagne oder Canvas-Attribution filtern

Filtern Sie nach Benutzern, die auf eine bestimmte SMS-Kampagne oder Canvas-Komponente, Stichwortkategorie oder Tag geantwortet haben.

**Nach Antworten auf eine bestimmte Kampagnenkategorie filtern**<br>
![Kampagne mit dem Filter "Hat auf SMS geantwortet" für die Kampagne "SMS-283" "Werbung". Unter dem Filter wird die Funktion erwähnt: „Dieser Filter läuft 25 Monate nach dem Versand der letzten Nachricht von „Aktion“ ab, wenn er nicht in einer aktiven Kampagne verwendet wird.“][12]

**Nach Beantwortung einer Kampagne oder eines Canvas mit einem bestimmten Tag filtern**
![Kampagne mit dem Filter „Hat auf SMS geantwortet“ für Kampagne oder Canvas mit Tag „Curbside Messaging Service C“.][13]

**Nach der Antwort auf einen bestimmten Schritt filtern**
![Kampagne mit dem Filter „Hat auf SMS geantwortet“ für Schritt „Doppeltes Opt-In für SMS“ „Schritt – Hilfe“.][11]

### Nachrichten nach Keyword triggern

Nachrichten können ausgelöst werden, wenn Benutzer Nachrichten auf der Grundlage von Schlüsselwortkategorien (der Benutzer hat eines der Schlüsselwörter gesendet) oder anderen Schlüsselwörtern (der Benutzer hat ein Schlüsselwort gesendet, das nicht in eine der bestehenden Kategorien fällt) ankommen lassen. Diese Trigger werden im Schritt „Zustellung“ des Kampagnen-Builders festgelegt.

Bei der Auswertung, ob eine eingehende Nachricht ein definiertes Trigger-Event erfüllt, werden die führenden und nachfolgenden Leerzeichen entfernt, bevor die Auswertung beginnt.

{% alert tip %}
Wenn ein aktionsbasiertes Canvas durch eine eingehende SMS-Nachricht getriggert wird, können Sie in jedem Canvas-Schritt bis zum nächsten Aktionspfad auf SMS-Eigenschaften verweisen.
{% endalert %}

**Nach Kategorie der eingehenden Keywords triggern**<br>
![Aktionsbasierte SMS-Kampagne mit dem Segmentierungsfilter Schlüsselwort "Opt-in" an die Abonnementgruppe "Marketing-SMS" gesendet.][7]{: style="margin-top:10px;"}

**Nach beliebigen Keywords triggern**<br>
Beachten Sie, dass Sie beim Triggern einer Nachricht auf eine „Sonstige“-Keyword-Antwort die Möglichkeit haben, den Keyword-Text auf eine exakte Textübereinstimmung zu überprüfen. Für dieses Spiel gelten die gleichen Regeln wie oben beschrieben: Es wird nur die **exakte Ein-Wort-Nachricht** verarbeitet (Groß- und Kleinschreibung _wird nicht berücksichtigt_). Ein Keyword, das von `Hello Braze!` gesendet wird, würde die Kriterien im folgenden Beispiel nicht erfüllen.
![Aktionsbasierte SMS-Kampagne mit der Keyword-Kategorie „Sonstige“, bei der der Nachrichtentext genau „Hallo“ oder „Hey“ lautet.][8]{: style="margin-top:10px;"}

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

[1]: {% image_buster /assets/img/sms/filter1.png %}
[2]: {% image_buster /assets/img/sms/filter2.png %}
[3]: {% image_buster /assets/img/sms/trigger.png %}
[6]: {% image_buster /assets/img/sms/retargeting1.png %}
[7]: {% image_buster /assets/img/sms/retargeting2.png %}
[8]: {% image_buster /assets/img/sms/retargeting3.png %}
[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[17]: {% image_buster /assets/img/keyword_example2.jpg %}
[11]: {% image_buster /assets/img/sms/clicked_opened_step.png %}
[12]: {% image_buster /assets/img/sms/clicked_opened_campaign.png %}
[13]: {% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %}
[15]: {% image_buster /assets/img/sms/retargeting5.png %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}
