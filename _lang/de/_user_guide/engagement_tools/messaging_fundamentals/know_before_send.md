---
nav_title: "Wissen, bevor Sie senden"
article_title: Informationen vor dem Versand
description: "Nachdem Sie unseren Leitfaden für die Markteinführung gelesen haben, sollten Sie sich die folgende Liste mit den wichtigsten Tipps und Tricks für Content-Cards, E-Mail, In-App-Nachrichten, Push und SMS ansehen."
alias: /know_before_send/
page_order: 10.2
tool:
    - Campaigns
    - Canvas
---

# Informationen vor dem Versand: Kanäle

Starten Sie Ihre Kampagnen und Canvase mit Zuversicht! In dieser abschließenden Liste finden Sie einige Hinweise zu Content-Cards, E-Mail, In-App-Nachrichten, Push und SMS.

{% alert note %}
Wir stellen Ihnen zwar eine umfangreiche Liste von Ressourcen zur Verfügung, die Sie vor dem Versand referenzieren können, aber jeder Kanal hat seine eigenen Nuancen, die mit der Weiterentwicklung unserer Produkte weiter wachsen. Wir empfehlen Ihnen, Ihre Kampagnen und großen Sendungen vor dem Versand gründlich zu testen.
{% endalert %}

## Allgemein

#### Zu überprüfende Dinge
- [**API Rate-Limits**](https://braze.com/resources/articles/whats-rate-limiting): Überprüfen Sie die Braze API [Rate-Limits]({{site.baseurl}}/api/api_limits/) für Ihre Workspaces, um Fehler zu vermeiden. Wenn Sie Ihre Rate-Limits erhöhen möchten (und bereits Anfragen bündeln), wenden Sie sich an Ihren Customer-Success-Manager. Denken Sie daran, dass dieser Prozess Vorlaufzeit erfordert, planen Sie also entsprechend.
- [**Notwendiges Frequency-Capping wird außer Kraft gesetzt**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping): Es gibt Kampagnen, wie z.B. Transaktionsnachrichten, bei denen Sie die Nutzer:innen immer erreichen möchten, auch wenn Sie die Frequenzgrenze bereits erreicht haben (z.B. eine Zustellungsbenachrichtigung). Wenn Sie möchten, dass eine bestimmte Kampagne die Regeln für Frequency-Capping außer Kraft setzt, können Sie dies im Braze-Dashboard bei der Zeitplanung für die Zustellung dieser Kampagne einrichten, indem Sie Frequency-Capping ausschalten.

#### Was Sie wissen sollten
- [**Globale Kontrollgruppen**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group): Wenn Sie eine globale Kontrollgruppe verwenden, wird ein bestimmter Prozentsatz der Nutzer:innen keine Kampagnen oder Canvase erhalten. (Sie können Ausnahmen mit [Ausschlusseinstellungen]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings) erstellen). Um eine Liste dieser Nutzer:innen zu sehen, exportieren Sie sie per CSV oder [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).
- [**Canvas Rate-Limits**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting): In einem Canvas gilt das Rate-Limit für den gesamten Canvas, nicht für die einzelnen Schritte. Wenn Sie beispielsweise ein Rate-Limit von 10.000 Nachrichten pro Minute für ein Canvas mit mehreren Schritten festlegen, bleibt es auf 10.000 Nachrichten beschränkt, da das Limit bereits im ersten Schritt erreicht wurde.
- **Frequency-Capping**: 
  - Frequency-Capping-Regeln werden auf Push, E-Mail, SMS und Webhooks angewendet, aber nicht auf In-App-Nachrichten und Content-Cards.
  - Der Zeitplan für das globale Frequency-Capping basiert auf der Zeitzone des Nutzers:innen und wird nach Kalendertagen und nicht nach 24-Stunden-Perioden berechnet. Wenn Sie zum Beispiel eine Frequency-Capping-Regel einrichten, die vorsieht, dass nicht mehr als eine Kampagne pro Tag versendet wird, kann ein Nutzer:innen um 23 Uhr in seiner Ortszeit eine Nachricht erhalten und eine Stunde später eine weitere Nachricht bekommen.

{% alert tip %}
Wenn Sie weitere Unterstützung bei der Fehlerbehebung für Canvas und Kampagnen benötigen, wenden Sie sich bitte innerhalb von 30 Tagen nach dem Vorkommen des Problems an den Braze-Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage vorliegen.
{% endalert %}

## E-Mail

#### Zu überprüfende Dinge
- **Die Zustimmung der Kund**:in: Bevor Sie Ihre ersten E-Mails verschicken, sollten Sie zunächst die Erlaubnis Ihrer Kunden einholen. Weitere Informationen finden Sie unter [Zustimmung und Adresserfassung]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/) und in unserer [Braze Richtlinie zur akzeptablen Nutzung](https://www.braze.com/company/legal/aup).
- **Erwartetes Volumen**: 2 Millionen E-Mails pro Tag für eine einzelne IP ist die allgemeine Empfehlung, solange dieses Volumen [ordnungsgemäß erwärmt]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming) wurde. 
  - Wenn Sie vorhaben, regelmäßig ein höheres Volumen zu versenden, um zu vermeiden, dass Provider den Empfang von E-Mails drosseln, was zu einer hohen Anzahl von Soft Bounces, einer geringeren Zustellbarkeit und einer geringeren IP-Reputation führt, sollten Sie mehrere IP-Adressen in einem IP-Pool bündeln. 
  - Wenn Sie nur innerhalb eines kürzeren Zeitraums versenden möchten, empfehlen wir Ihnen, sich zu informieren, wie schnell die verschiedenen Anbieter Mails annehmen, um die angemessene Anzahl von IPs zu ermitteln, von denen aus Sie versenden möchten. 

#### Was Sie wissen sollten
- **Faktoren für das Sendevolumen**: Einige Faktoren, die das mögliche Sendevolumen für eine IP bestimmen, sind:
  - Briefkästen: Große E-Mail-Anbieter können wahrscheinlich Millionen von E-Mails pro Tag von einer einzigen IP-Adresse aus abwickeln, während ein kleinerer regionaler Mailbox-Anbieter oder einer mit einer kleineren Infrastruktur möglicherweise nicht in der Lage ist, diese Menge zu bewältigen.
  - Absender-Reputation: Sie können möglicherweise ein größeres Volumen pro Tag von einer einzigen IP-Adresse aus versenden, wenn der Sender auf dieses Volumen hochgefahren ist und wenn seine Absender-Reputation bei jedem Postfach oder jeder Domain, an die er sendet, stark genug ist.
- **Bewährte Praktiken**: Informieren Sie sich über die [Best Practices für E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) von Braze und wenden Sie sich an Ihr Braze-Konto Team, wenn Sie mehr über die Dienste zur Zustellbarkeit erfahren möchten.

## Push

#### Zu überprüfende Dinge
- [**Opt-in/abonniert und Push enabled**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/): Damit Nutzer:innen eine Push Nachricht von Braze erhalten können, müssen sie entweder Opt-in (iOS) oder Abonnent:in (Android) und `Push Enabled = True` sein. Beachten Sie, dass Android 13 die Verwaltung von Apps, die Push-Benachrichtigungen senden, für die Nutzer:innen grundlegend ändert. Die [Anleitung zum Upgrade des Android 13 SDK]({{site.baseurl}}/developer_guide/platforms/android/android_13/) von Braze wird laufend aktualisiert, sobald neue Android 13 Beta-Versionen veröffentlicht werden.

#### Was Sie wissen sollten
- **Web-Push**: Wenn Sie das Braze [Web SDK eingerichtet]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) haben, sollten Sie den Einsatz von Web-Push in Betracht ziehen, um Nutzer:innen zu engagieren. Web-Push funktioniert genauso wie die Push-Benachrichtigungen von Apps auf Ihrem Telefon. Weitere Informationen zum Verfassen einer Web-Push-Nachricht finden Sie unter [Erstellen einer Push-Benachrichtigung]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).
- **Targeting für eine singuläre App**: Überprüfen Sie die [Unterschiede bei der Segmentierung]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#targeting-a-singular-app), um eine singuläre App und ihre Nutzer:innen zu targetieren.

## SMS

#### Zu überprüfende Dinge
- **Zuteilungen und Durchsatz**: Verstehen Sie, welche SMS-Kontingente derzeit mit Ihrem Konto verknüpft sind (Shortcode, Langcode u.ä.) und [wie viel Durchsatz Ihnen dadurch zur Verfügung steht]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/), um sicherzustellen, dass Sie genügend Durchsatz haben, um in der gewünschten Zeit zu senden.
- **Schätzen Sie Segmente aus SMS-Kopien**: Testen Sie Ihre SMS-Kopie mit dem [SMS-Segment-Rechner]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy). Denken Sie daran, dass die Anzahl der SMS Segmente von Ihren Durchsatzmöglichkeiten abhängt. (Zielgruppe * SMS Segmente = benötigter Durchsatz). Siehe SMS FAQ zur [Vermeidung von Mehrkosten]({{site.baseurl}}/sms_faq/).
- **SMS-Gesetze und -Vorschriften**: [Überprüfen Sie die SMS Gesetze, Vorschriften und Missbrauchsverhinderung]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/), um sicherzustellen, dass Sie die Serviceleistungen; Dienste in Übereinstimmung mit allen geltenden Gesetzen nutzen. Vergewissern Sie sich, dass Sie vor dem Versenden den Rat Ihres Rechtsbeistandes einholen sollten.

#### Was Sie wissen sollten
- **SMS Nachrichten Standard**: SMS Nachrichten werden normalerweise standardmäßig über den Shortcode im Sender-Pool versendet.
- **Alphanumerische ID des Senders**: Zwei-Wege Messaging wird nicht mehr funktionieren, wenn Sie eine alphanumerische Sender ID verwenden; diese sind jetzt nur noch einseitig.
- **Update des Durchsatzes in den USA**: Der Durchsatz hat sich in den USA mit der US [A2P 10DLC Registrierung](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) geändert. Bitte beachten Sie, dass wir uns vertraglich nicht zu einer bestimmten Zustellungsgeschwindigkeit verpflichten, da zahlreiche Faktoren wie Verkehrsstaus und Probleme mit dem Transportunternehmen die tatsächlichen Zustellungsraten beeinflussen können.
- **Abo-Gruppe**: Um eine SMS-Kampagne über Braze einzuführen, muss eine Abo-Gruppe ausgewählt werden. Um die internationalen [Telekommunikationsrichtlinien]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) einzuhalten, sendet Braze außerdem niemals SMS an Nutzer:in, die nicht [die ausgewählte Abo-Gruppe abonniert]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group) haben.

## WhatsApp

#### Was Sie wissen sollten

- [**Beste Praktiken**]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/): Sehen Sie sich unsere empfohlenen WhatsApp-Best Practices an.

## Banner

#### Zu überprüfende Dinge
- **Abmessungen des Banners:** Erstellen Sie Ihre Banner mit einem Element fester Größe und testen Sie sie im Editor.
- **Vorrangig:** Wenn Sie mehrere Banner starten, können Sie die Priorität für die Anzeige jedes Banners manuell festlegen.

#### Was Sie wissen sollten
- **Liquid Personalisierung:** Die Liquid Personalisierung wird bei jeder Anfrage aktualisiert.
- **Platzierung und Banner-Verhältnis:** Jede Bannerplatzierung kann in bis zu 10 Kampagnen in einem Workspace verwendet werden.  
- **Klicks und Impressionen:** Klicks und Impressionen für Banner werden mit dem SDK automatisch getrackt.
- **Beschränkungen:**  Derzeit werden die folgenden Features nicht unterstützt: Canvas-Integration, API-getriggerte und aktionsbasierte Kampagnen, Connected-Content, Aktionscodes, benutzergesteuerte Kündigungen und `catalog_items` unter Verwendung des [Tags`:rerender` ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).
- **Testen:** Um den Testbanner anzuzeigen, muss das Gerät, das Sie verwenden, Push-Benachrichtigungen im Vordergrund empfangen können.
- **Angepasstes HTML:** Nutzen Sie die [JS-Bridge]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge), um Klicks zu protokollieren, wenn Sie angepasstes HTML verwenden, um Klick-Aktionen, wie Links und Buttons, zu definieren. Klick-Aktionen werden nur dann automatisch protokolliert, wenn Sie die vorgefertigten Komponenten im Drag-and-Drop-Editor verwenden.
- **Anfrage zur Platzierung:** Bis zu 10 Platzierungen können in einer einzigen Anfrage an das SDK zurückgegeben werden. Jede Platzierung enthält das Banner mit der höchsten Priorität, für das ein Nutzer:innen in Frage kommt.

## Content-Cards

#### Zu überprüfende Dinge
- **Content-Card Größe**: Die Größe der Content-Card-Nachrichtenfelder ist vor der Komprimierung auf 2 KB begrenzt. Sie wird durch Addition der Byte-Längen der folgenden Felder berechnet: Titel, Nachricht, Bild-URL, Linktext, Link-URLs und Schlüssel-Wert-Paare. Nachrichten, die diese Größe überschreiten, werden nicht gesendet. Beachten Sie, dass dies nicht die Größe des Bildes einschließt, sondern die Länge der Bild-URL.
- **Update der Kopie nach dem Versenden**: Nachdem eine Karte verschickt wurde, können Sie die Kopie auf derselben Karte nicht mehr aktualisieren. Lesen Sie den Abschnitt [Aktualisierung der gesendeten Karten]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-sent-cards), um zu verstehen, wie Sie dieses Szenario angehen können.

#### Was Sie wissen sollten
- **Aktive Content-Card-Kampagnen begrenzen**: Sie können bis zu 500 aktive Content-Card-Kampagnen haben. Diese Zahl umfasst Content-Cards, die mit einer der beiden [Kartenerstellungsoptionen]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) gesendet wurden.  
- [**Bedingungen für die Berichterstattung**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/): Überprüfen Sie Begriffe wie Gesamtzahl der Impressionen, eindeutige Impressionen und eindeutige Empfänger:innen, da die Definitionen manchmal für Verwirrung sorgen können.
- **Content-Card aktualisieren**: Standardmäßig aktualisiert Braze die Anfragen für Content-Cards bei der Synchronisierung zu Beginn der Sitzung, beim Wischen nach unten (mobil) und beim Öffnen der Kartenansicht, wenn die letzte Aktualisierung länger als eine Minute zurückliegt.
- **Content-Cards zwischenspeichern**: Content-Card-Zwischenspeicheroptionen finden Sie in unseren [Android/FireOS-]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android) und [Internet-Dokumenten](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards). 
- **Frequency-Capping**: Frequency-Capping gilt nicht für Content-Cards.
- **Impressionen**: Impressionen werden in der Regel protokolliert, wenn eine Karte gesehen wird. Wenn Sie z.B. einen vollen Posteingang mit Content-Cards haben, wird eine Impression erst protokolliert, wenn der Nutzer:innen zu einer bestimmten Content-Card scrollt. Es gibt einige Unterschiede zwischen den Plattformen Internet, Android und iOS.  

## In-App-Nachrichten

#### Was Sie wissen sollten
- **Triggern von In-App-Nachricht**: Zu Beginn der Sitzung fordert das SDK an, dass alle in Frage kommenden In-App-Nachrichten zusammen mit ihren Triggern an das Gerät gesendet werden, so dass es die In-App-Nachrichten schnell und zuverlässig empfangen kann, wenn es das Ereignis während der Sitzung ausführt.
- **Gesendet versus Impressionen**: Bei In-App-Nachrichten unterscheidet sich das Konzept von "gesendet" von den anderen verfügbaren Kanälen. Um eine In-App-Nachricht zu sehen, muss ein Nutzer:in eine Sitzung eintreten, sich in der berechtigten Zielgruppe befinden und den Trigger ausführen. Aus diesem Grund tracken wir "Impressionen", da dies eindeutiger ist.
- **Trigger**: Standardmäßig werden In-App-Nachrichten durch Events ausgelöst, die vom SDK protokolliert werden. Wenn Sie In-App-Nachrichten durch vom Server gesendete Ereignisse triggern möchten, können Sie dies auch mit diesen Anleitungen für [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift) und [Android]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android) erreichen.
- [In-App-Nachrichten von Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options): Diese Nachrichten erscheinen das erste Mal, wenn Ihr Nutzer:innen die App öffnet (ausgelöst durch die Startsitzung), nachdem die geplante Nachricht in der Canvas-Komponente an ihn gesendet wurde.
- **Connected-Content-Aufrufe**: Mit Connected-Content können Sie dynamische Inhalte in Nachrichten versenden. Wenn Sie Nachrichten über einen Kanal wie In-App-Nachrichten senden, können Sie mehr gleichzeitige Verbindungen zu den Geräten Ihrer Nutzer:innen herstellen (die Nachrichten werden einzeln und nicht in Stapeln gesendet). Daher empfehlen wir Ihnen, [die Rate-Limits]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting) für Ihre Nachrichten zu nutzen.
