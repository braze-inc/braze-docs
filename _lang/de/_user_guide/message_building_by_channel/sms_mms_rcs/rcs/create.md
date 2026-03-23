---
nav_title: Erstellen Sie eine RCS-Nachricht
article_title: Erstellen Sie eine RCS-Nachricht
page_order: 2
alias: /create_rcs_message/
description: "Dieser Artikel beschreibt, wie Sie eine RCS-Nachricht erstellen."
page_type: reference
channel:
  - RCS
---

# Erstellen Sie eine RCS-Nachricht

> RCS-Kampagnen eignen sich hervorragend, um Ihre Kund:innen direkt zu erreichen und programmgesteuert mit ihnen zu kommunizieren. Sie können Liquid und andere dynamische Inhalte verwenden, um ein persönliches Erlebnis mit Ihren Nutzer:innen zu schaffen und eine Umgebung zu fördern, die ein unaufdringliches Nutzererlebnis mit Ihrer Marke unterstützt und verbessert.

## Erstellen einer RCS-Nachricht

### 1. Schritt: Wählen Sie, wo Sie Ihre Nachricht erstellen möchten

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Kampagne oder ein Canvas versendet werden soll? Kampagnen eignen sich besser für einzelne, zielgerichtete Messaging-Kampagnen, während Canvase besser für mehrstufige User Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}
1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie **SMS/MMS/RCS** oder, für Kampagnen mit Targeting für mehrere Kanäle, wählen Sie **Multichannel**.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu.
   * Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den [Berichts-Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.

{: start="5"} 
5. Fügen Sie so viele Varianten hinzu, wie Sie für Ihre Kampagne benötigen, und benennen Sie sie. Sie können für jede hinzugefügte Variante verschiedene Plattformen, Nachrichtentypen und Layouts auswählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- **Testen von SMS- und RCS-Varianten**: Braze erlaubt es Ihnen, sowohl SMS- als auch RCS-Varianten in eine einzige Kampagne einzubinden, sodass Sie die Performance der beiden Varianten vergleichen können. Sie können SMS- und RCS-Varianten während des ersten Schritts der Nachrichtenerstellung hinzufügen.

{: start="6"} 
6. Wählen Sie eine RCS-aktivierte [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups/) aus. Wenn Sie eine Abo-Gruppe auswählen, fügt Braze automatisch einen Filter zur Segmentierung hinzu, der sicherstellt, dass nur abonnierte Nutzer:innen die Kampagne erhalten. Nur Langcodes und Shortcodes, die zu dieser Abo-Gruppe gehören, werden für den Versand von SMS an die Zielnutzer:innen verwendet.
- **SMS-Fallback:** Braze empfiehlt dringend, dass jede Abo-Gruppe, die einen RCS-Sender enthält, auch mindestens einen SMS-Code für Fallback enthält. Dies ist wichtig für die Zustellbarkeit, falls RCS-Nachrichten nicht zugestellt werden können. Gründe dafür können unter anderem die Inkompatibilität der Nutzer:innen-Geräte und eine unvollständige Netzabdeckung in einem bestimmten Land oder einer bestimmten Region sein. Durch die Aktivierung von SMS-Fallback kann Ihre RCS-Nachricht weiterhin per SMS zugestellt werden, wenn RCS nicht möglich ist – so verpassen Sie keine Opportunity, mit Ihren Nutzer:innen in Kontakt zu treten.

{% alert note %}
MMS-Fallback wird nicht unterstützt.
{% endalert %}

{: start="7"}
7. Wählen Sie zwischen SMS und RCS. Bevor Sie RCS-Nachrichten verfassen, wählen Sie den Kanal, über den Sie senden. Wir empfehlen generell die Verwendung von RCS, wo immer dies möglich ist, da dies erhebliche Vorteile für das Engagement der Nutzer:innen gegenüber SMS mit sich bringt. Wir bieten jedoch immer die Möglichkeit, per SMS zu versenden, damit Sie maximale Flexibilität und Kontrolle haben. 

![Optionen zum Auswählen eines RCS- oder SMS/MMS-Nachrichtentyps.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sind oder den gleichen Inhalt haben, sollten Sie Ihre Nachricht verfassen, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann aus der Dropdown-Liste **Variante hinzufügen** die Option **Aus Variante kopieren** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit dem Canvas Composer.
2. Nachdem Sie Ihr Canvas eingerichtet haben, fügen Sie im Canvas Builder einen Schritt für **SMS/MMS/RCS**-Nachrichten hinzu. 
3. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
4. Wählen Sie eine RCS-aktivierte [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups/) aus. Wenn Sie eine Abo-Gruppe auswählen, fügt Braze automatisch einen Filter zur Segmentierung hinzu, der sicherstellt, dass nur abonnierte Nutzer:innen die Kampagne erhalten. Nur Langcodes und Shortcodes, die zu dieser Abo-Gruppe gehören, werden zum Targeting der Nutzer:innen verwendet.
- **SMS-Fallback**: Braze empfiehlt dringend, dass jede Abo-Gruppe, die einen RCS-Sender enthält, auch mindestens einen SMS-Code für Fallback enthält. Dies ist wichtig für die Zustellbarkeit, falls RCS-Nachrichten nicht zugestellt werden können. Gründe dafür können unter anderem die Inkompatibilität der Nutzer:innen-Geräte und eine unvollständige Netzabdeckung in einem bestimmten Land oder einer bestimmten Region sein. Durch die Aktivierung von SMS-Fallback wird Ihre Nachricht weiterhin Ihren Nutzer:innen zugestellt und Sie verpassen keine Opportunity, mit ihnen in Kontakt zu treten.

{: start="5"}
5. Wählen Sie zwischen SMS und RCS. Bevor Sie RCS-Nachrichten verfassen, wählen Sie den Kanal, über den Sie senden. Wir empfehlen generell die Verwendung von RCS, wo immer dies möglich ist, da dies erhebliche Vorteile für das Engagement der Nutzer:innen gegenüber SMS mit sich bringt. Wir bieten jedoch immer die Möglichkeit, per SMS zu versenden, damit Sie maximale Flexibilität und Kontrolle haben. 

![Optionen zum Auswählen eines RCS- oder SMS/MMS-Nachrichtentyps.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### 2. Schritt: Wählen Sie den Typ Ihrer RCS-Nachricht aus

Wählen Sie für Ihren RCS-Nachrichtentyp zwischen **Text** und **Medien**.

![Optionen zum Auswählen von Text- oder Mediennachrichten.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Text %}
Wie der Name schon sagt, liegt der Schwerpunkt von RCS-Textnachrichten auf Text als Medium. Wenn Sie bis zu 160 Zeichen eingeben, wird die RCS-Nachricht als reine Textnachricht (oder „Basic"-Nachricht) abgerechnet. Wenn Sie mehr als 160 Zeichen oder ein Rich-Element verwenden, wird die Nachricht als Rich-RCS-Nachricht (oder „Single"-Nachricht) abgerechnet (und das Zeichenlimit erhöht sich auf 3072 Zeichen). 

#### Features

- Textnachrichtentypen enthalten alle SMS-Features. Für das Tracking von URL-Klicks ist nur das erweiterte Tracking möglich, um Ihnen eine granulare Berichterstattung auf Nutzer:innen-Ebene zu ermöglichen. 
- Darüber hinaus haben Sie jetzt die Möglichkeit, ansprechende Buttons mit **Vorgeschlagenen Antworten** und **Vorgeschlagenen Aktionen** einzubinden, die Nutzer:innen zu Aktionen mit hohem Engagement anregen, z. B. zum Besuch einer Landing-Page oder zur Aufgabe einer Bestellung. 
    - **Vorgeschlagene Antworten** sind Buttons mit Antwortvorschlägen, auf die Nutzer:innen klicken können, um sie in ihre Texteingabe einzufügen. So müssen sie nicht mehr selbst an eine Antwort denken, sondern haben eine begrenzte Auswahl an Möglichkeiten. 
    - **Vorgeschlagene Aktionen** sind Buttons, die eine Aktion auf dem Gerät der Nutzer:innen auslösen. Sie bestehen in der Regel aus einem oder zwei beschreibenden Wörtern und einem visuellen Symbol, damit die Nutzer:innen verstehen, was der Button bewirkt. Braze unterstützt derzeit OpenURL Suggested Actions. Dies funktioniert ähnlich wie eine URL, bei der Nutzer:innen, die den Button auswählen, zu einer Webseite oder einem anderen URL-identifizierten Standort weitergeleitet werden. 

![Ein GIF mit drei vorgeschlagenen Aktionen für eine RCS-Nachricht, die für aktuelle Modetrends wirbt: „Fairytale royalty", „Edgy academia" und „Show me your other styles".]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Überlegungen

- Was die Zeichenbegrenzung für Text betrifft, können Sie bis zu 160 Zeichen für eine reine Text-RCS-Nachricht (Basic) oder bis zu 3072 Zeichen für eine Rich-RCS-Nachricht (Single) schreiben. 
- Für die Begrenzung der Buttons können Sie bis zu fünf Buttons pro Nachricht hinzufügen. Diese Buttons können entweder vorgeschlagene Aktionen oder vorgeschlagene Antworten sein.
- Längere Textblöcke und zu viele Buttons können Nutzer:innen frustrieren, daher empfehlen wir, wo immer möglich, auf Einfachheit zu setzen. 
- In manchen Fällen kann es kostengünstiger sein, längere reine Textnachrichten über RCS zu versenden als per SMS. Das liegt daran, dass längere SMS-Nachrichten in mehrere Segmente unterteilt werden, die jeweils abgerechnet werden, während RCS-Nachrichten pro Nachricht abgerechnet werden. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie weitere Einzelheiten und Hinweise benötigen. 
{% endtab %}

{% tab Media %}
RCS-Mediennachrichten erlauben Ihnen die Verwendung ansprechender Medienformate, die mit SMS nicht möglich sind. Dazu gehören Bild-, Video- und Dokumentdateien. Diese Medienoptionen helfen Ihnen, Ihre Zielgruppe noch stärker einzubinden und ermöglichen völlig neue Anwendungsfälle. Im Moment wird nur das Hochladen von Bildern über die [Medienbibliothek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) unterstützt. 

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Features

- Mediennachrichtentypen unterstützen alles, was in Textnachrichtentypen verfügbar ist, einschließlich Text, vorgeschlagene Antworten und vorgeschlagene Aktionen.
- Unterstützt Bilddateien, einschließlich der Dateiformate JPEG und PNG. Bilddateien sind durch Hochladen aus der Medienbibliothek verfügbar. 
- Unterstützt Videodateien, einschließlich MP4-, MPEG- und MV4-Dateiformate. Videodateien können per URL direkt im Nachrichten-Editor hinzugefügt werden. 
- Unterstützt Dokumentdateien im PDF-Format. Dokumentdateien können über die URL direkt im Nachrichten-Editor hinzugefügt werden. 

![RCS-Composer mit der Option, eine Mediendatei hochzuladen.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

#### Datei-Spezifikationen

| Dateityp | Spezifikationen |
| --- | --- |
| Alle | - Die Dateigröße ist auf 100 MB begrenzt. <br><br>- Die Datei-URL kann bis zu 2048 Zeichen lang sein. |
| Bilddateien | Unterstützte Dateiformate: JPG, JPEG und GIF |
| Videodateien | Unterstützte Dateiformate: H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Dokumentdateien | Unterstützte Dateiformate: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Überlegungen

Das Nutzererlebnis beim Empfang von RCS-Nachrichten kann aufgrund einer Reihe von Faktoren leicht variieren, z. B. der Netzabdeckung im Zielland, der Hardware des Mobilgeräts und des Betriebssystems des Mobilgeräts. 

Im Allgemeinen lässt sich RCS natürlicher in Android-Geräte integrieren (diese Methode wurde größtenteils von Google implementiert, und Peer-to-Peer-RCS-Messaging ist in der Android-Community weit verbreitet). Verschiedene Geräte können das Erlebnis in unterschiedlicher Geschwindigkeit und Qualität wiedergeben.  
{% endtab %}
{% endtabs %}

### 3. Schritt: Verfassen Sie Ihre RCS-Nachricht

Schreiben Sie Ihre Nachricht mit den gewünschten Sprachen und der gewünschten Personalisierung ([Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) und Emojis). Achten Sie darauf, unsere Obergrenzen für Nachrichtentexte einzuhalten, um das Risiko von Mehrkosten zu verringern.

{% alert important %}
Bevor Sie fortfahren, lesen Sie unsere [Richtlinien für die Begrenzung von RCS-Nachrichten](#step-2-select-your-rcs-message-type). RCS-Nachrichten werden [pro Nachricht abgerechnet]({{site.baseurl}}/sms_rcs_billing_calculators/). Es ist daher sinnvoll, die Feinheiten dessen zu verstehen, was in jeder Art von RCS-Nachricht enthalten sein kann.
{% endalert %}

### 4. Schritt: Vorschau und Test Ihrer Nachricht

Da die RCS-Darstellung vom Betriebssystem der Nutzer:innen, dem Gerätehersteller, dem Netzbetreiber und der Messaging-App (z. B. Google Messages vs. Apple Messages) gesteuert wird, kann das Erscheinungsbild der Nachrichten variieren. Daher kann es vorkommen, dass die in Braze angezeigte RCS-Vorschau nicht genau mit dem übereinstimmt, was die Endnutzer:innen letztendlich erhalten. Unterschiede können das Layout, die Mediengröße, Buttons, Branding-Elemente oder unterstützte Features umfassen. Braze empfiehlt immer, Ihre Nachricht vor dem Versand in der Vorschau zu prüfen und zu testen. Verwenden Sie den Tab **Test**, um einen Test-RCS an Content-Testgruppen oder einzelne Nutzer:innen zu senden und die Nachricht als Nutzer:in direkt in Braze in der Vorschau anzuzeigen. Die endgültige Darstellung sollte jedoch nach Möglichkeit immer auf realen Geräten überprüft werden, da Braze keine vollständige Übereinstimmung über alle Kombinationen von Betriebssystemen, Geräten und Netzbetreibern hinweg garantieren kann.


### 5. Schritt: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

Als Nächstes erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas. In den folgenden Abschnitten erfahren Sie, wie Sie unsere Tools zum Erstellen von RCS-Nachrichten am besten einsetzen.

#### Schritt 5.1: Wählen Sie einen Zeitplan für die Zustellung oder einen Trigger

RCS-Nachrichten können auf der Grundlage eines Zeitplans, einer Aktion oder eines API-Triggers zugestellt werden. Mehr dazu erfahren Sie unter [Planen Ihrer Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Für die aktionsbasierte Zustellung können Sie auch die Dauer der Kampagne und die Ruhezeiten festlegen.

Legen Sie Ihre Zustellungskontrollen fest, z. B. die Möglichkeit, Nutzer:innen wieder für den Empfang der Kampagne zuzulassen oder Frequency-Capping-Regeln zu aktivieren.

#### Schritt 5.2: Zielgruppe auswählen

Stellen Sie Ihre Zielgruppe zusammen, indem Sie Segmente oder Filter auswählen, um Ihre Zielgruppe einzugrenzen. Sie sollten bereits die Abo-Gruppe ausgewählt haben, die die Nutzer:innen nach der Ebene oder Kategorie der Kommunikation mit Ihnen eingrenzt.

{% multi_lang_include target_audiences.md %}

Anschließend wählen Sie die größere Zielgruppe aus Ihren Segmenten aus und grenzen dieses Segment mit optionalen [Filtern]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) weiter ein. Sie erhalten automatisch eine Vorschau, wie die ungefähre Segmentpopulation aussieht. Bitte beachten Sie, dass die genaue Segmentzugehörigkeit immer vor dem Versand der Nachricht berechnet wird.

{% alert tip %}
Möchten Sie RCS-Retargeting nutzen, um Nutzer:innen auf der Basis ihrer SMS- und RCS-Interaktionen zu targetieren? Lesen Sie dazu den Abschnitt [Retargeting]({{site.baseurl}}/sms_mms_rcs_user_retargeting/).
{% endalert %}

#### Schritt 5.3: Wählen Sie Konversions-Events aus

Mit Braze können Sie nachverfolgen, wie oft Nutzer:innen bestimmte Aktionen oder Konversions-Events durchführen, nachdem sie eine Kampagne erhalten haben. Sie können ein Zeitfenster von bis zu 30 Tagen zulassen, in dem eine Konversion gezählt wird, wenn die angegebene Aktion durchgeführt wird.

Konversions-Events helfen Ihnen, den Erfolg Ihrer Kampagne zu messen. Zum Beispiel:
- Wenn Sie Geotargeting verwenden, um eine RCS-Nachricht zu triggern, deren Ziel es ist, dass die Nutzer:innen einen Kauf tätigen, setzen Sie das Konversions-Event auf **Kauf**.
- Wenn Sie versuchen, die Nutzer:innen zu Ihrer App zu bringen, setzen Sie das Konversions-Event auf **Starts Session**.

Sie können auch benutzerdefinierte Konversions-Events für Ihren speziellen Anwendungsfall festlegen. Werden Sie kreativ bei der Frage, wie Sie den Erfolg Ihrer Kampagne wirklich messen möchten.

### 6. Schritt: Überprüfen und bereitstellen

Nachdem Sie Ihre Kampagne oder Ihr Canvas fertiggestellt haben, überprüfen Sie die Details, testen Sie sie und senden Sie sie dann ab!

Lesen Sie als Nächstes den Abschnitt [Reporting für SMS, MMS und RCS]({{site.baseurl}}/sms_mms_rcs_reporting/), um zu erfahren, wie Sie auf die Ergebnisse Ihrer RCS-Kampagnen zugreifen können.

## Tipps

### Verwendung von Liquid für die Personalisierung von Nachrichten

Wenn Sie Liquid verwenden möchten, stellen Sie sicher, dass Sie einen Standardwert für die von Ihnen gewählte Personalisierung angeben, damit Empfänger:innen mit einem unvollständigen Nutzerprofil nicht einen leeren Platzhalter `Hi, !` anstelle ihres Namens oder eines zusammenhängenden Satzes erhalten.

### KI-Texte generieren

Benötigen Sie Hilfe bei der Erstellung ansprechender Texte? Versuchen Sie es mit dem [KI-Textwerkstatt-Assistenten]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI generiert menschenähnliche Marketingtexte für Ihr Messaging.

![Nachrichten-Editor mit einem Symbol zur Öffnung des KI-Assistenten für das Verfassen von Texten.]({% image_buster /assets/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

### Konversationelle Nachrichten-Workflows erstellen

Konversationelle Nachrichten-Workflows ermöglichen es Ihnen, dynamisch auf Nutzer:innen zu reagieren und ein interaktives Messaging-Erlebnis zu schaffen. Um einen Workflow zu erstellen, erstellen Sie ein Canvas und kombinieren Sie dann vorgeschlagene Antworten mit [Aktionspfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), um Ihren Workflow basierend auf der ausgewählten Antwort der Nutzer:innen zu steuern.

1. Erstellen Sie im Canvas Builder einen RCS-Nachrichtenschritt mit mehreren vorgeschlagenen Antworten.

![RCS-Nachrichten-Editor mit vorgeschlagenen Antworten.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. Verbinden Sie diese Nachricht mit einem Aktionspfad, der für jede vorgeschlagene Antwort eine Aktionsgruppe enthält.
3. Für jede Aktionsgruppe:
  - Wählen Sie den Trigger **Eingehende SMS-Nachricht senden**.
  - Setzen Sie den Nachrichtentext auf denselben Text wie die entsprechende vorgeschlagene Antwort. 

![Aktionspfad-Schritt mit drei Aktionsgruppen, eine für jede vorgeschlagene Antwort.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. Verbinden Sie jede Aktionsgruppe mit einem RCS-Nachrichtenschritt und fügen Sie dann Inhalt basierend auf der zugehörigen vorgeschlagenen Antwort hinzu.
5. Setzen Sie den konversationellen Workflow fort, indem Sie vorgeschlagene Antworten zu allen Folgenachrichten hinzufügen.
6. Wiederholen Sie die Schritte 2–4, bis der Workflow vollständig ist.

![Canvas mit einem konversationellen Workflow mit zwei Aktionspfaden.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

## Häufig gestellte Fragen

### Kann ich mit RCS voraufgezeichnete Sprachnachrichten versenden?

Ja, Sie können Mediennachrichten verwenden, um Audio-Dateien zu unterstützen.