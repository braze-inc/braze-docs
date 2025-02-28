---
nav_title: "Wissen, bevor Sie senden"
article_title: "Wissen, bevor Sie senden"
description: "Nachdem Sie unseren Leitfaden für die Markteinführung durchgelesen haben, sollten Sie sich diese abschließende Checkliste für Content Cards, E-Mail, In-App-Nachrichten, Push und SMS ansehen."
alias: /know_before_send/

---

# Wissen, bevor Sie senden: Kanäle

Starten Sie Ihre Kampagnen und Canvases mit Zuversicht! Lesen Sie diese abschließende Liste mit Überprüfungen oder "Fallstricken" für Content Cards, E-Mail, In-App-Nachrichten, Push und SMS.

{% alert note %}
Wir bieten zwar eine umfangreiche Liste von Ressourcen, auf die Sie sich vor dem Versand beziehen können, aber jeder Kanal hat individuelle Nuancen, die mit der Weiterentwicklung unserer Produkte weiter wachsen. Die unten aufgeführten Kontrollen sind hilfreiche Vorschläge, und wir empfehlen, Ihre Kampagnen und großen Sendungen vor dem Versand gründlich zu testen.
{% endalert %}

## Allgemein

#### Zu überprüfende Dinge
- [**API-Grenzwerte**](https://braze.com/resources/articles/whats-rate-limiting): Überprüfen Sie die Braze [API-Ratenbeschränkungen]({{site.baseurl}}/api/api_limits/) für Ihre Arbeitsbereiche, um Fehler zu vermeiden. Wenn Sie Ihre Ratenlimits erhöhen möchten (und bereits Anfragen bündeln), wenden Sie sich an Ihren Customer Success Manager. Denken Sie daran, dass dieser Prozess Vorlaufzeit erfordert, planen Sie also entsprechend.
- [**Erforderliche Frequenzbegrenzung überschreibt**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping): Es gibt einige Kampagnen, wie z.B. Transaktionsnachrichten, die den Nutzer immer erreichen sollen, auch wenn Sie die Frequenzgrenze bereits erreicht haben (z.B. eine Lieferbenachrichtigung). Wenn Sie möchten, dass eine bestimmte Kampagne die Regeln für die Frequenzbegrenzung außer Kraft setzt, können Sie dies im Braze-Dashboard bei der Planung der Zustellung dieser Kampagne einrichten, indem Sie die Frequenzbegrenzung deaktivieren.

#### Was Sie wissen sollten
- [**Globale Kontrollgruppen**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group): Wenn Sie eine globale Kontrollgruppe verwenden, wird ein bestimmter Prozentsatz der Benutzer keine Kampagnen oder Leinwände erhalten. (Sie können Ausnahmen mit [Ausschlusseinstellungen]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings) erstellen). Um eine Liste dieser Benutzer zu sehen, exportieren Sie sie über CSV oder [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).
- [**Tarife für Leinwände**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting): In einem Canvas gilt das Ratenlimit für den gesamten Canvas, nicht für die einzelnen Schritte. Wenn Sie z.B. ein Ratenlimit von 10.000 Nachrichten pro Minute für eine Leinwand mit mehreren Stufen festlegen, bleibt diese auf 10.000 Nachrichten begrenzt, da das Limit bereits bei der ersten Stufe erreicht wurde.
- **Frequenzkappung**: 
  - Die Regeln für die Frequenzbegrenzung werden auf Push-Nachrichten, E-Mails, SMS und Webhooks angewendet, nicht aber auf In-App-Nachrichten und Content Cards.
  - Die globale Frequenzbegrenzung basiert auf der Zeitzone des Benutzers und wird nach Kalendertagen und nicht nach 24 Stunden berechnet. Wenn Sie beispielsweise eine Regel zur Begrenzung der Häufigkeit des Versendens von maximal einer Kampagne pro Tag einrichten, könnte ein Benutzer um 23 Uhr in seiner lokalen Zeitzone eine Nachricht erhalten und wäre eine Stunde später zum Empfang einer weiteren Nachricht berechtigt.

{% alert tip %}
Wenn Sie weitere Unterstützung bei der Fehlersuche für Canvas und Kampagnen benötigen, wenden Sie sich bitte innerhalb von 30 Tagen nach Auftreten des Problems an den Braze-Support, da uns nur die Diagnoseprotokolle der letzten 30 Tage vorliegen.
{% endalert %}

## E-Mail

#### Zu überprüfende Dinge
- **Zustimmung des Kunden**: Bevor Sie Ihre ersten E-Mails verschicken, sollten Sie zunächst die Erlaubnis Ihrer Kunden einholen. Weitere Informationen finden Sie unter [Einwilligung und Adresserfassung]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/) und in unserer [Braze Acceptable Use Policy](https://www.braze.com/company/legal/aup).
- **Erwartetes Volumen**: 2 Millionen E-Mails pro Tag für eine einzelne IP ist die allgemeine Empfehlung, solange dieses Volumen [ordentlich aufgewärmt]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming) wurde. 
  - Wenn Sie vorhaben, regelmäßig ein höheres Volumen zu versenden, um zu vermeiden, dass Provider den Empfang von E-Mails drosseln, was zu einer hohen Anzahl von Soft Bounces, einer niedrigeren Zustellbarkeitsrate und einer geringeren IP-Reputation führt, sollten Sie die Verwendung mehrerer IP-Adressen in Betracht ziehen, die in einem IP-Pool gebündelt sind. 
  - Wenn Sie nur innerhalb eines kürzeren Zeitraums versenden möchten, empfehlen wir Ihnen, sich zu informieren, wie schnell die verschiedenen Anbieter Mails annehmen, um die angemessene Anzahl von IPs zu ermitteln, von denen aus Sie versenden möchten. 

#### Was Sie wissen sollten
- **Faktoren für das Sendevolumen**: Einige Faktoren, die das mögliche Sendevolumen für eine IP bestimmen, sind:
  - Briefkästen: Große E-Mail-Anbieter können wahrscheinlich Millionen von E-Mails pro Tag von einer einzigen IP-Adresse aus bearbeiten, während ein kleinerer regionaler Mailbox-Anbieter oder ein Anbieter mit einer kleineren Infrastruktur möglicherweise nicht in der Lage ist, diese Menge zu bearbeiten.
  - Ruf des Absenders: Sie können möglicherweise ein größeres Volumen pro Tag von einer einzigen IP-Adresse aus versenden, wenn der Absender auf dieses Volumen eingestellt ist und wenn seine Absenderreputation bei jedem Postfach oder jeder Domain, an die er sendet, stark genug ist.
- **Bewährte Praktiken**: Informieren Sie sich über die [bewährten E-Mail-Verfahren]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) von Braze und wenden Sie sich an Ihr Braze Account Team, wenn Sie mehr über die Zustellbarkeitsservices erfahren möchten.

## Push

#### Zu überprüfende Dinge
- [**Angemeldet/abonniert und Push aktiviert**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/): Damit Benutzer eine Push-Nachricht von Braze erhalten, muss ihr Abonnementstatus entweder optiert (iOS) oder abonniert (Android) und `Push Enabled = True` sein. Beachten Sie, dass Android 13 eine wichtige Änderung bei der Verwaltung von Apps einführt, die Push-Benachrichtigungen senden. Die Braze [Android 13 SDK Upgrade-Anleitung]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_13/) wird laufend aktualisiert, sobald neue Android 13 Beta-Versionen veröffentlicht werden.

#### Was Sie wissen sollten
- **Web-Push**: Wenn Sie das Braze [Web SDK eingerichtet]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) haben, können Sie Web-Push nutzen, um Benutzer einzubinden. Web-Push funktioniert genauso wie die Push-Benachrichtigungen von Apps auf Ihrem Telefon. Weitere Informationen zum Verfassen einer Web-Push-Nachricht finden Sie unter [Erstellen einer Push-Benachrichtigung]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).
- **Eine einzelne App anvisieren**: Überprüfen Sie die [Unterschiede bei der Segmentierung]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#targeting-a-singular-app), um eine einzelne App und ihre Nutzer anzusprechen.

## SMS

#### Zu überprüfende Dinge
- **Zuteilungen und Durchsatz**: Informieren Sie sich darüber, welche SMS-Kontingente derzeit mit Ihrem Konto verknüpft sind (Kurzcode, Langcode und ähnliches) und [wie viel Durchsatz Sie dadurch erhalten]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/), um sicherzustellen, dass Sie genügend Durchsatz haben, um in der gewünschten Zeit zu senden.
- **Schätzen Sie das Segment aus der SMS-Kopie**: Testen Sie Ihren SMS-Text mit dem [SMS-Segmentrechner]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy). Denken Sie daran, dass die Anzahl der SMS-Segmente von Ihren Durchsatzmöglichkeiten abhängt. (Zielgruppe * SMS-Segmente = benötigter Durchsatz). Lesen Sie die SMS-FAQ zur [Vermeidung von Überschreitungen]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/#how-can-i-avoid-overages).
- **SMS-Gesetze und -Vorschriften**: [Überprüfen Sie die SMS-Gesetze, -Vorschriften und -Missbrauchsprävention]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/), um sicherzustellen, dass Sie die SMS-Dienste in Übereinstimmung mit allen geltenden Gesetzen nutzen. Vergewissern Sie sich, dass Sie vor dem Versenden den Rat Ihres Rechtsbeistandes einholen sollten.

#### Was Sie wissen sollten
- **SMS-Nachricht standardmäßig einstellen**: SMS-Nachrichten werden normalerweise standardmäßig von der Kurznummer im Absenderpool versendet.
- **Alphanumerische Absender-ID**: Zwei-Wege-Nachrichten funktionieren nicht mehr, wenn Sie eine alphanumerische Absender-ID verwenden; diese sind jetzt nur noch einseitig.
- **Aktualisierter Durchsatz in den USA**: Der Durchsatz hat sich in den USA mit der US [A2P 10DLC Registrierung](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) geändert. Bitte beachten Sie, dass wir uns vertraglich nicht zu einer bestimmten Sendegeschwindigkeit verpflichten, da zahlreiche Faktoren wie Verkehrsstaus und Probleme mit dem Transportunternehmen die tatsächlichen Zustellungsraten beeinflussen können.
- **Abonnement-Gruppe**: Um eine SMS-Kampagne über Braze zu starten, muss eine Abonnementgruppe ausgewählt werden. Um die internationalen [Telekommunikationsvorschriften und -richtlinien]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/) einzuhalten, sendet Braze außerdem niemals SMS an Benutzer, die [sich]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group) nicht [bei der ausgewählten Abonnementgruppe angemeldet]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group) haben.

## WhatsApp

#### Was Sie wissen sollten

- [**Beste Praktiken**]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/): Sehen Sie sich unsere empfohlenen WhatsApp-Best Practices an.

## Inhaltskarten

#### Zu überprüfende Dinge
- **Inhalt Kartengröße**: Die Größe der Nachrichtenfelder der Content Card ist vor der Komprimierung auf 2 KB begrenzt. Sie wird berechnet, indem die Byte-Länge der folgenden Felder addiert wird: Titel, Nachricht, Bild-URL, Linktext, Link-URLs und Schlüssel-Wert-Paare. Nachrichten, die diese Größe überschreiten, werden nicht gesendet. Beachten Sie, dass dies nicht die Größe des Bildes einschließt, sondern die Länge der Bild-URL.
- **Aktualisierung der Kopie nach dem Versand**: Nachdem eine Karte verschickt wurde, können Sie die Kopie auf derselben Karte nicht mehr aktualisieren. Lesen Sie den Abschnitt [Aktualisierung der gesendeten Karten]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-sent-cards), um zu verstehen, wie Sie dieses Szenario angehen können.

#### Was Sie wissen sollten
- **Limit für aktive Content Card-Kampagnen**: Sie können bis zu 500 aktive Content Card-Kampagnen haben. Diese Zahl umfasst Inhaltskarten, die mit einer der beiden [Kartenerstellungsoptionen]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) versendet wurden.  
- [**Bedingungen für die Berichterstattung**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/): Überprüfen Sie Begriffe wie Total Impressions, Unique Impressions und Unique Receivers, da die Definitionen manchmal für Verwirrung sorgen können.
- **Inhalt Karte aktualisieren**: Standardmäßig aktualisiert Braze die Inhaltskartenanfragen bei der Synchronisierung zu Beginn der Sitzung, beim Wischen nach unten (mobil) und beim Öffnen der Kartenansicht, wenn die letzte Aktualisierung länger als eine Minute zurückliegt.
- **Inhaltskarten zwischenspeichern**: Optionen für das Zwischenspeichern von Inhalten auf der Karte finden Sie in unseren [Android/FireOS-]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android) und [Web-Dokumenten](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards). 
- **Frequenzkappung**: Die Frequenzbegrenzung gilt nicht für Inhaltskarten.
- **Eindrücke**: Eindrücke werden in der Regel protokolliert, wenn eine Karte gesehen wird. Wenn Sie z.B. einen vollen Posteingang mit Inhaltskarten haben, wird ein Abdruck erst protokolliert, wenn der Benutzer zu einer bestimmten Inhaltskarte scrollt. Es gibt einige Unterschiede zwischen den Plattformen Web, Android und iOS.  

## In-App-Nachrichten

#### Was Sie wissen sollten
- **Auslösen von In-App-Nachrichten**: Beim Start der Sitzung fordert das SDK an, dass alle in Frage kommenden In-App-Nachrichten zusammen mit den Auslösern an das Gerät gesendet werden, damit es die In-App-Nachricht schnell und zuverlässig erhält, wenn es das Ereignis während der Sitzung ausführt. Aus diesem Grund können In-App-Nachrichten nicht durch benutzerdefinierte Ereignisse in Canvas ausgelöst werden.
- **Gesendet versus Eindrücke**: Bei In-App-Nachrichten unterscheidet sich das Konzept von "gesendet" von den anderen verfügbaren Kanälen. Um eine In-App-Nachricht zu sehen, muss ein Nutzer eine Sitzung starten, sich in der Zielgruppe befinden und den Auslöser betätigen. Aus diesem Grund verfolgen wir die "Impressionen", da sie eindeutiger sind.
- **Auslöser**: Standardmäßig werden In-App-Nachrichten durch vom SDK protokollierte Ereignisse ausgelöst. Wenn Sie In-App-Nachrichten durch vom Server gesendete Ereignisse auslösen möchten, können Sie dies auch mit diesen Anleitungen für [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/custom_triggering/) und [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization) erreichen.
- [**Canvas In-App Nachrichten**]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options): Diese Nachrichten erscheinen, wenn Ihr Benutzer die App zum ersten Mal öffnet (ausgelöst durch die Startsitzung), nachdem die geplante Nachricht in der Canvas-Komponente an ihn gesendet wurde.
