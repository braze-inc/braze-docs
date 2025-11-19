---
nav_title: "Erstellen einer RCS Nachricht"
article_title: Erstellen einer RCS Nachricht
page_order: 2
alias: /create_rcs_message/
description: "Dieser Artikel beschreibt, wie Sie eine RCS Nachricht erstellen."
page_type: reference
channel:
  - RCS
---

# Erstellen einer RCS Nachricht

> RCS Kampagnen eignen sich hervorragend, um Ihre Kund:in direkt zu erreichen und programmgesteuert mit ihnen zu kommunizieren. Sie können Liquid und andere dynamische Inhalte verwenden, um ein persönliches Erlebnis mit Ihren Nutzern zu schaffen und eine Umgebung zu schaffen, die ein unaufdringliches Nutzererlebnis mit Ihrer Marke fördert und verbessert.

## Erstellen einer RCS Nachricht

### Schritt 1: Wählen Sie, wo Sie Ihre Botschaft aufbauen möchten

Sie sind sich nicht sicher, ob Ihre Nachricht über eine Kampagne oder ein Canvas versendet werden soll? Kampagnen eignen sich eher für einzelne einfache Messaging-Kampagnen, während Canvases besser für mehrstufige User Journeys geeignet sind.

{% tabs %}
{% tab Campaign %}
1. Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie **Kampagne erstellen**.
2. Wählen Sie **SMS/MMS/RCS**, oder für Kampagnen, die auf mehrere Kanäle abzielen, wählen Sie **Multichannel**.
3. Geben Sie Ihrer Kampagne einen klaren und aussagekräftigen Namen.
4. Fügen Sie nach Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu.
   * Mithilfe von Tags lassen sich Ihre Kampagnen leichter finden und Berichte daraus erstellen. Wenn Sie zum Beispiel den [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) verwenden, können Sie nach bestimmten Tags filtern.

{: start="5"}
5\. Fügen Sie so viele Varianten hinzu, wie Sie für Ihre Kampagne benötigen, und benennen Sie sie. Sie können für jede hinzugefügte Variante verschiedene Plattformen, Nachrichtentypen und Layouts auswählen. Weitere Informationen zu diesem Thema finden Sie unter [Multivariate und A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- **Testen von SMS- und RCS-Varianten**: Braze erlaubt es Ihnen, sowohl SMS- als auch RCS-Varianten in eine einzige Kampagne einzubinden, so dass Sie die Performance der beiden Varianten vergleichen können. Sie können SMS- und RCS-Varianten während des ersten Schritts der Nachrichtenerstellung hinzufügen.

{: start="6"}
6\. Wählen Sie eine RCS-aktivierte [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups/) aus. Wenn Sie eine Abo-Gruppe auswählen, fügt Braze automatisch einen Filter zur Segmentierung hinzu, der sicherstellt, dass nur Nutzer:innen die Kampagne erhalten. Nur lange Codes und kurze Codes, die zu dieser Abonnementgruppe gehören, werden für den Versand von SMS an die Zielbenutzer verwendet.
- **SMS Fallback**: Braze empfiehlt dringend, dass jede Abo-Gruppe, die einen RCS-Sender enthält, auch mindestens einen SMS Code für Fallback enthält. Dies ist wichtig für die Zustellbarkeit, falls RCS-Nachrichten nicht zugestellt werden können. Dies kann unter anderem an der Inkompatibilität der Nutzer:innen-Geräte und der unvollständigen Netzabdeckung in einem bestimmten Land oder einer bestimmten Region liegen. Durch die Aktivierung von SMS Fallback wird Ihre Nachricht weiterhin Ihren Nutzer:innen zugestellt und Sie verpassen keine Opportunity, mit ihnen in Kontakt zu treten.   

{: start="7"}
7\. Wählen Sie zwischen SMS und RCS. Bevor Sie RCS-Nachrichten verfassen, wählen Sie den Kanal, über den Sie senden. Wir empfehlen generell die Verwendung von RCS, wo immer dies möglich ist, da dies erhebliche Vorteile für das Engagement der Nutzer:innen gegenüber SMS mit sich bringt. Wir bieten jedoch immer die Möglichkeit, per SMS zu versenden, damit Sie maximale Flexibilität und Kontrolle haben. 

Optionen zum Auswählen eines RCS- oder SMS/MMS-Nachrichtentyps.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Wenn alle Nachrichten in Ihrer Kampagne ähnlich sind oder den gleichen Inhalt haben, sollten Sie Ihre Nachricht verfassen, bevor Sie zusätzliche Varianten hinzufügen. Sie können dann aus der Dropdown-Liste **Variante hinzufügen** die Option **Aus Variante kopieren** wählen.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Erstellen Sie Ihr Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) mit dem Canvas Composer.
2. Nachdem Sie Ihr Canvas eingerichtet haben, fügen Sie einen **SMS/MMS/RCS** Nachricht-Schritt im Canvas-Builder hinzu. 
3. Geben Sie Ihrem Schritt einen klaren und aussagekräftigen Namen.
4. Wählen Sie eine RCS-aktivierte [Abo-Gruppe]({{site.baseurl}}/sms_rcs_subscription_groups/) aus. Wenn Sie eine Abo-Gruppe auswählen, fügt Braze automatisch einen Filter zur Segmentierung hinzu, der sicherstellt, dass nur Nutzer:innen die Kampagne erhalten. Nur Langcodes und Shortcodes, die zu dieser Abo-Gruppe gehören, werden zum Targeting der Nutzer:innen verwendet.
- **SMS Fallback**: Braze empfiehlt dringend, dass jede Abo-Gruppe, die einen RCS-Sender enthält, auch mindestens einen SMS Code für Fallback enthält. Dies ist wichtig für die Zustellbarkeit, falls RCS-Nachrichten nicht zugestellt werden können. Dies kann unter anderem an der Inkompatibilität der Nutzer:innen-Geräte und der unvollständigen Netzabdeckung in einem bestimmten Land oder einer bestimmten Region liegen. Durch die Aktivierung von SMS Fallback wird Ihre Nachricht weiterhin Ihren Nutzer:innen zugestellt und Sie verpassen keine Opportunity, mit ihnen in Kontakt zu treten.

{: start="5"}
5\. Wählen Sie zwischen SMS und RCS. Bevor Sie RCS-Nachrichten verfassen, wählen Sie den Kanal, über den Sie senden. Wir empfehlen generell die Verwendung von RCS, wo immer dies möglich ist, da dies erhebliche Vorteile für das Engagement der Nutzer:innen gegenüber SMS mit sich bringt. Wir bieten jedoch immer die Möglichkeit, per SMS zu versenden, damit Sie maximale Flexibilität und Kontrolle haben. 

Optionen zum Auswählen eines RCS- oder SMS/MMS-Nachrichtentyps.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Schritt 2: Wählen Sie den Typ Ihrer RCS Nachricht aus

Wählen Sie für Ihren RCS Nachrichtentyp zwischen **Text** und **Medien**.

![Optionen zum Auswählen eines Text- oder Medientyps für Nachrichten.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Text %}
Wie der Name schon sagt, liegt der Schwerpunkt von RCS Messaging auf Text als Medium. Wenn Sie bis zu 160 Zeichen eingeben, wird die RCS Nachricht als reine Textnachricht (oder "einfache" Nachricht) abgerechnet. Wenn Sie mehr als 160 Zeichen oder ein Rich-Element verwenden, wird die Nachricht als Rich (oder "Single") RCS-Nachricht abgerechnet (und das Zeichenlimit erhöht sich auf 3072 Zeichen). 

#### Features

- Die SMS-Nachrichten enthalten alle Features von SMS. Für das Tracking von URL-Klicks ist nur das erweiterte Tracking möglich, um Ihnen eine granulare Berichterstattung auf Nutzer:innen-Ebene zu ermöglichen. 
- Darüber hinaus haben Sie jetzt die Möglichkeit, ansprechende Buttons **mit Vorgeschlagenen Antworten** und **Vorgeschlagenen Aktionen** einzubinden, die Nutzer:innen zu Aktionen mit hohem Engagement anregen, z. B. zum Besuch einer Landing Page oder zur Aufgabe einer Bestellung. 
    - **Suggested Replies** sind Buttons mit Antwortvorschlägen, auf die Nutzer:innen klicken und die sie in ihre Texteingabe einfügen können. So müssen sie nicht mehr selbst an eine Antwort denken, sondern haben eine begrenzte Auswahl. 
    - **Vorgeschlagene Aktionen** sind Buttons, die eine Aktion auf dem Nutzer:innen Gerät auslösen. Sie bestehen in der Regel aus einem oder zwei beschreibenden Wörtern und einem visuellen Symbol, damit der Nutzer:in versteht, was der Button bewirkt. Braze unterstützt derzeit OpenURL Suggested Actions. Dies funktioniert ähnlich wie eine URL, bei der Nutzer:innen, die den Button auswählen, zu einer Webseite oder einem anderen URL-identifizierten Standort weitergeleitet werden. 

![Ein GIF mit drei vorgeschlagenen Aktionen für eine RCS Nachricht, die für aktuelle Modetrends wirbt: "Märchenhaftes Königtum", "Edgy Academia" und "Zeigen Sie mir Ihre anderen Stile".]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Überlegungen

- Was die Zeichenbegrenzung für Text betrifft, so können Sie bis zu 160 Zeichen für eine reine Text-RCS-Nachricht (Basic) oder bis zu 3072 Zeichen für eine Rich-RCS-Nachricht (Single) schreiben. 
- Für die Begrenzung der Buttons können Sie bis zu fünf Buttons pro Nachricht hinzufügen. Diese Buttons können entweder vorgeschlagene Aktionen oder vorgeschlagene Antworten sein.
- Längere Textblöcke und zu viele Buttons können Nutzer:innen frustrieren, daher empfehlen wir, wo immer möglich, auf Einfachheit zu setzen. 
- In manchen Fällen kann es kostengünstiger sein, längere reine Textnachrichten über RCS zu versenden als per SMS. Das liegt daran, dass längere SMS-Nachrichten in mehrere Segmente unterteilt sind, die jeweils abgerechnet werden, während RCS-Nachrichten pro Nachricht abgerechnet werden. Wenden Sie sich an Ihren Braze-Konto Manager:in, wenn Sie weitere Einzelheiten und Hinweise benötigen.
{% endtab %}

{% tab Media %}
RCS Nachrichten erlauben Ihnen die Verwendung von Medienformaten, die mit SMS nicht möglich sind. Dazu gehören Bild-, Video- und Dokumentationsdateien. Diese Medienoptionen helfen Ihnen, Ihre Zielgruppe noch stärker zu engagieren und ermöglichen völlig neue Anwendungsfälle. Im Moment wird nur das Hochladen von Bildern über die [Bibliothek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) unterstützt. 

#### Features

- Mediale Nachrichtentypen unterstützen alles, was in Textnachrichten verfügbar ist, d.h. Text, vorgeschlagene Antworten und vorgeschlagene Aktionen.
- Unterstützt Bilddateien, einschließlich der Dateiformate JPEG und PNG. Bilddateien sind durch Hochladen aus der Bibliothek verfügbar. 
- Unterstützt Videodateien, einschließlich MP4-, MPEG- und MV4-Dateiformate. Videodateien können per URL direkt im Nachrichten-Editor hinzugefügt werden. 
- Unterstützt Dokumentdateien im PDF-Format. Dokumentendateien können über die URL direkt im Nachrichten-Editor hinzugefügt werden. 

![RCS Composer mit einer Option zum Hochladen einer Mediendatei.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

#### Datei-Spezifikationen

| Dateityp | Spezifikationen |
| --- | --- |
| Alle | \- Die Dateigröße ist auf 100 MB begrenzt. <br><br>\- Die Datei-URL kann bis zu 2048 Zeichen lang sein. |
| Bilddateien | Unterstützte Dateiformate: JPG, JPEG und GIF
| Video Dateien | Unterstützte Dateiformate: H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| Dokumentationsdateien | Unterstützte Dateiformate: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Überlegungen

Das Nutzer:in-Erlebnis beim Empfang von RCS Nachrichten kann aufgrund einer Reihe von Faktoren leicht variieren, z.B. der Netzabdeckung im Zielland, der Hardware des mobilen Geräts und des Betriebssystems des mobilen Geräts. 

Im Allgemeinen lässt sich RCS natürlicher in Android Geräte integrieren (diese Methode wurde größtenteils von Google implementiert, und Peer-to-Peer RCS Messaging ist in der Android Community weit verbreitet). Verschiedene Geräte können das Erlebnis in unterschiedlicher Geschwindigkeit und Qualität wiedergeben.  
{% endtab %}
{% endtabs %}

### Schritt 3: Verfassen Sie Ihre RCS Nachricht

Schreiben Sie Ihre Nachricht in den Sprachen und mit der Personalisierung[(Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) und Emojis), die Sie benötigen. Achten Sie darauf, dass Sie unsere Obergrenzen für Nachrichtenkopien einhalten, um das Risiko von Mehrkosten zu verringern.

{% alert important %}
Bevor Sie fortfahren, lesen Sie unsere [Richtlinien für die Begrenzung von RCS Nachrichten](#step-2-select-your-rcs-message-type). RCS-Nachrichten werden [pro Nachricht abgerechnet]({{site.baseurl}}/sms_rcs_billing_calculators/). Es ist also eine gute Idee, die Feinheiten dessen zu verstehen, was in jeder Art von RCS-Nachricht enthalten sein kann.
{% endalert %}

### Schritt 4: Vorschau und Test Ihrer Nachricht

Braze empfiehlt immer, Ihre Nachricht vor dem Versand in der Vorschau zu prüfen. Gehen Sie auf den Tab **Test**, um eine Test-RCS an Inhaltstestgruppen oder einzelne Nutzer:innen zu senden, oder um eine Vorschau der Nachricht als Nutzer:innen direkt in Braze anzuzeigen.

### Schritt 5: Erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas

Als nächstes erstellen Sie den Rest Ihrer Kampagne oder Ihres Canvas. In den folgenden Abschnitten erfahren Sie, wie Sie unsere Tools zum Erstellen von RCS-Nachrichten am besten einsetzen.

#### Schritt 5.1: Wählen Sie einen Zeitplan für die Zustellung oder triggern Sie

RCS Nachrichten können auf der Grundlage eines Zeitplans, einer Aktion oder eines API-Triggers zugestellt werden. Mehr dazu erfahren Sie unter [Planen Ihrer Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Für die aktionsbasierte Zustellung können Sie auch die Dauer der Kampagne und die Ruhezeiten festlegen.

Legen Sie Ihre Zustellungskontrollen fest, z.B. die Möglichkeit, Nutzer:innen wieder für den Empfang der Kampagne zuzulassen oder Frequency-Capping-Regeln zu aktivieren.

#### Schritt 5.2: Zielgruppe auswählen

Stellen Sie Nutzer:innen durch die Auswahl von Segmenten oder Filtern gezielt zusammen, um Ihre Zielgruppe einzugrenzen. Sie sollten bereits die Abo-Gruppe ausgewählt haben, die die Nutzer:innen nach der Ebene oder Kategorie der Kommunikation mit Ihnen eingrenzt.

{% multi_lang_include target_audiences.md %}

Als nächstes wählen Sie die größere Zielgruppe aus Ihren Segmenten aus und grenzen dieses Segment mit optionalen [Filtern]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) weiter ein. Sie erhalten automatisch eine Vorschau darauf, wie die ungefähre Anzahl der Segmente im Moment aussieht. Denken Sie daran, dass die genaue Segmentzugehörigkeit immer erst kurz vor dem Versand der Nachricht berechnet wird.

{% alert tip %}
Möchten Sie RCS Retargeting nutzen, um Nutzer:innen auf der Basis ihrer SMS- und RCS-Interaktionen zu targetieren? Verweisen Sie auf [Retargeting]({{site.baseurl}}/sms_mms_rcs_user_retargeting/).
{% endalert %}

#### Schritt 5.3: Wählen Sie Konversions-Events aus

Mit Braze können Sie nachverfolgen, wie oft Nutzer:innen bestimmte Aktionen oder Konversions-Events durchführen, nachdem sie eine Kampagne erhalten haben. Sie können ein Zeitfenster von bis zu 30 Tagen zulassen, in dem eine Konversion gezählt wird, wenn die angegebene Aktion durchgeführt wird.

Konversions-Events helfen Ihnen, den Erfolg Ihrer Kampagnen zu messen. Zum Beispiel:
- Wenn Sie Geotargeting verwenden, um eine RCS Nachricht zu triggern, deren Ziel es ist, dass der Nutzer:innen einen Kauf tätigt, setzen Sie das Konversions-Event auf **Kauf**.
- Wenn Sie versuchen, den Nutzer:innen zu Ihrer App zu bringen, setzen Sie das Konversions-Event auf **Starts Session**.

Sie können auch benutzerdefinierte Konvertierungsereignisse für Ihren speziellen Anwendungsfall festlegen. Werden Sie kreativ bei der Frage, wie Sie den Erfolg Ihrer Kampagne wirklich messen wollen.

### Schritt 6: Überprüfen und einsetzen

Nachdem Sie Ihre Kampagne oder Ihr Canvas fertiggestellt haben, überprüfen Sie die Details, testen Sie sie und senden Sie sie dann ab!

Als nächstes referenzieren Sie auf [Reporting für SMS, MMS und RCS]({{site.baseurl}}/sms_mms_rcs_reporting/), um zu erfahren, wie Sie auf die Ergebnisse Ihrer RCS Kampagnen zugreifen können.

## Tipps

### Verwendung von Liquid für die Personalisierung von Nachrichten

Wenn Sie Liquid verwenden möchten, stellen Sie sicher, dass Sie einen Standardwert für die von Ihnen gewählte Personalisierung angeben, damit der Empfänger:in einem unvollständigen Nutzerprofil nicht einen leeren Platzhalter `Hi, !` anstelle seines Namens oder eines zusammenhängenden Satzes erhält.

### KI-Kopie generieren

Benötigen Sie Hilfe bei der Erstellung ansprechender Texte? Versuchen Sie es mit dem [KI-Textwerkstatt-Assistenten]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Geben Sie einen Produktnamen oder eine Beschreibung ein, und die KI generiert menschenähnliche Marketingtexte für Ihr Messaging.

![Nachrichten-Editor mit einem Symbol zum Öffnen des KI-Texter-Assistenten.]({% image_buster /assets/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Häufig gestellte Fragen

### Kann ich mit RCS voraufgezeichnete Sprachnachrichten versenden?

Ja, Sie können Nachrichten zur Unterstützung von Audio-Dateien verwenden.
