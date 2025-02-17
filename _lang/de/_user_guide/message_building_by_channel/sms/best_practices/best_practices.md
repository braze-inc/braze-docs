---
nav_title: "Bewährte SMS/MMS-Praktiken"
article_title: Bewährte SMS/MMS-Praktiken
page_order: 1
description: "Dieser Referenzartikel behandelt bewährte Verfahren für SMS/MMS."
page_type: reference
channel:
  - SMS
  
---

# Bewährte SMS/MMS-Verfahren

> Erfahren Sie mehr über die besten Praktiken für SMS/MMS mit Braze, einschließlich unserer Empfehlungen für die Opt-out-Überwachung und das Pumpen des Datenverkehrs.

## Empfehlungen zur Opt-out-Überwachung

Es ist gesetzlich vorgeschrieben, dass wir den Anfragen von Empfängern nachkommen, die eine Abmeldung von Mitteilungen wünschen. Die Nichteinhaltung von Aufforderungen von SMS-Empfängern, den Kanal abzubestellen, kann Strafen nach sich ziehen, einschließlich Geldstrafen, und kann zu Gerichtsverfahren führen. Braze verfügt über Features, die ein robustes Opt-in und Opt-out von SMS/MMS ermöglichen, sowie über Mechanismen, die sicherstellen, dass Anfragen korrekt bearbeitet werden.

Im Rahmen ihrer Abonnementverträge mit uns sind unsere Kunden allein dafür verantwortlich, dass sie bei der Nutzung unserer Dienste die geltenden Gesetze einhalten. Dementsprechend empfehlen wir unseren Kunden dringend, auf die korrekte Konfiguration ihrer SMS-Einstellungen zu achten, diese gründlich zu testen, Maßnahmen zur Überwachung der Einhaltung der Opt-Out-Bestimmungen zu ergreifen und sofort zu handeln, wenn sie Fälle von Nichteinhaltung der Opt-Out-Anforderungen feststellen.

Wenn Sie SMS/MMS in Braze einrichten, um Opt-ins und Opt-outs zu verwalten, konsultieren Sie die folgende Liste von Ressourcen:
* [SMS-Abonnementgruppen]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/): Abonnementgruppen und Opt-in/out-Methoden und -Status.
* [Abonnementgruppen-REST-APIs]({{site.baseurl}}/api/endpoints/subscription_groups): Wie Sie Opt-Ins und Opt-Outs verarbeiten, die sie aus einer anderen Quelle als einer direkten Antwort auf eine Nachricht erhalten.
* [Schlüsselwortverarbeitung]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords): Erklärungen dazu, wie Braze die Schlüsselwortverarbeitung und -verwaltung angeht.
* [SMS Double Opt-in]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/sms_double_opt_in/): Nutzer:innen müssen ihre Opt-in Absicht ausdrücklich bestätigen, bevor sie Nachrichten per SMS erhalten können. SMS Double Opt-in ist in einigen Ländern vorgeschrieben, daher empfiehlt Braze, dies zu konfigurieren.
* [SMS Nachrichten versenden]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/sms_sending/): Grundlagen des SMS-Versands bei Braze, einschließlich der Bedeutung von Abo-Gruppen, Anforderungen für SMS-Segmente und Nachrichten-Teile und mehr.

### Überlegungen

Wenn SMS/MMS über mehrere Instanzen hinweg eingerichtet wurden und aufgrund einer Fehlkonfiguration eine Kampagne oder Canvas-Opt-outs an den falschen Arbeitsbereich gesendet werden.

* Braze hat eine Überwachung eingerichtet, um solche Fälle zu identifizieren. Wenn dieses Verhalten erkannt wird, leitet Braze Opt-outs an die richtige Instanz weiter und füllt alle Opt-outs, die in diesem Zeitraum aufgetreten sind, wieder auf.
* Wir empfehlen Kund:innen dringend, Opt-outs für jede Abo-Gruppe zu testen, die sie in Braze haben. Es ist besser, dieses Problem vor dem Start einer Nachricht zu erkennen, als es zu beheben, nachdem es bereits erkannt wurde.

Braze verwaltet SMS/MMS-Abonnements sowohl auf der Ebene des Benutzerprofils (`user_id`) als auch auf der Ebene der Rufnummer (`channel_id`). Wenn eine Telefonnummer ein- oder ausgeschaltet wird, gilt die Aktualisierung für alle Profile, die diese Nummer nutzen. Wenn sich ein Endbenutzer mit einer bestimmten Telefonnummer angemeldet hat, dann aber seine Telefonnummer ändert, erbt die neue Telefonnummer den Status der Abonnementgruppe des Benutzers. Wenn ein Endbenutzer sich abgemeldet hat, dann aber die App oder Website mit einer neuen Telefonnummer erneut aufruft, wird er keine unerwünschten Nachrichten erhalten.

## Empfehlungen für Verkehrspumpen

### Was ist eine Verkehrspumpe?

Traffic-Pumping ist eine Form des Betrugs, die auftritt, wenn ein böser Akteur ein Online-Formular verwendet, um den Versand von SMS-Nachrichten in großem Umfang auszulösen (z. B. Opt-in-Nachrichten oder einmalige Passwörter). Der Betrüger richtet eine Mehrwertnummer ein, an die diese Nachrichten gesendet werden, und fordert eine Umsatzbeteiligung von dem Mobilfunkbetreiber, bei dem die Mehrwertnummer eingerichtet wurde.

### Wie man Verkehrspumpen erkennt

* Mehrwertdienstnummern, die diese Art von Betrug unterstützen, werden oft, aber nicht immer, in Ländern eingerichtet, die nicht zu Ihrem normalen Sendegebiet gehören.
* Ungewöhnliche Spitzen bei der Versendung von Nachrichten aus Online-Formularen können auf ein Ansteigen des Datenverkehrs hinweisen.
    * Wir empfehlen, [Kampagnenwarnungen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_alerts/) einzurichten, um die Anzahl der gesendeten Nachrichten zu begrenzen und Sie zu benachrichtigen, wenn eine unplausibel hohe Anzahl von Nachrichten gesendet wird.
* Unvollständig ausgefüllte Online-Formulare können auf eine programmatische Ausfüllung hinweisen.
* Wenn Sie Online-Formulare erstellen, empfehlen wir Ihnen, Regeln aufzustellen, um sicherzustellen, dass die Formulare vollständig sind, und Tools wie CAPTCHA zu verwenden, um das Risiko zu minimieren.

### Auswirkungen der Verkehrspumpe

Die Kunden sind für die Überwachung des von ihnen versendeten Datenverkehrs verantwortlich und erhalten eine Rechnung für alle über ihr Konto versendeten SMS. Zwischen Braze und Kund:in ist die:der Kund:in die Partei, die besser in der Lage ist, Traffic-Pumping zu erkennen und zu verhindern.

