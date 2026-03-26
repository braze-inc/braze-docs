---
nav_title: Meta-Ressourcen
article_title: Meta-Ressourcen
page_order: 12
description: "In diesem Artikel finden Sie hilfreiche Meta-Dokumentation, Informationen und Ressourcen, die Ihnen helfen, die WhatsApp-Integration besser zu verstehen."
alias: /meta_resources/
page_type: reference
channel:
  - WhatsApp

---

# Meta-Ressourcen

## Meta-Dokumentation

In der folgenden Meta-Dokumentation finden Sie Anleitungen zu Anzeigenamen, Telefonnummern und mehr.

- [Anleitung zu Anzeigenamen](https://www.facebook.com/business/help/757569725593362)
- [Meta Insights aktivieren](https://www.facebook.com/business/help/218116047387456)
- [Anforderungen an die Telefonnummer](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)
- [Messaging-Limits](https://developers.facebook.com/docs/whatsapp/messaging-limits)
- [Qualitätsbewertung](https://www.facebook.com/business/help/896873687365001)

## WhatsApp-Produktupdates

### Juni 2026: Geschäftsbezogene Nutzer-IDs
*Letztes Update März 2026*

- Meta führt Nutzer-IDs ein, um die Weitergabe von Telefonnummern aus Datenschutzgründen zu ersetzen
- Braze arbeitet vor der Einführung an einer Lösung
- Geplante Einführung durch Meta im Juni 2026

### November 2025: [Marketing Messages API für WhatsApp](https://developers.facebook.com/documentation/business-messaging/whatsapp/marketing-messages/overview/) (ehemals Marketing Messages Lite API)
*Letztes Update März 2026*

- Ersetzt statische Cloud-API-Limits durch dynamische, Engagement-basierte Limits
- Nicht verfügbar in EMEA, Japan oder Südkorea für optimierte Zustellung
- Utility-/Authentifizierungsnachrichten werden automatisch über die Cloud API weitergeführt

### Oktober 2025: Genehmigungsprozess für Official Business Account (OBA) geändert
*Letztes Update März 2026*

- Zuvor für alle Kund:innen über den WhatsApp Manager zugänglich
- Jetzt beschränkt auf: Regierungen/große Meta-Werbetreibende, Direktwerbetreibende oder über einen BSP wie Braze (bis zu 5 pro Woche)
- Neue Voraussetzungen: Unternehmensverifizierung, Zwei-Faktor-Verifizierung, genehmigter Anzeigename, Bekanntheit
- Wenden Sie sich an Ihren Customer-Success-Manager für Unterstützung

### Oktober 2025: Regionale Preissenkungen
*Letztes Update März 2026*

- Niedrigere Utility-/Authentifizierungsraten in Argentinien, Ägypten, Mexiko, Nordamerika
- Niedrigere Marketingraten in Mexiko (gültig ab 1. Oktober 2025)

### Oktober 2025: Messaging-Limits ändern sich von pro Telefonnummer zu pro Unternehmensportfolio
*Letztes Update März 2026*

- Limits werden jetzt über alle Telefonnummern in einem Portfolio geteilt
- Portfolios übernehmen das höchste bestehende Limit
- Schnellerer Zugang zu höheren Limits (innerhalb von 6 Stunden)
- Risiko: Unternehmen ohne eine „unbegrenzte" Nummer können einen Rückgang der aggregierten Limits feststellen

### 1. Juli 2025: Preisumstellung
*Letztes Update März 2026*

- Pro-Nachricht-Abrechnung ersetzt Pro-Konversation-Abrechnung
- Utility-Nachrichten, die innerhalb eines 24-Stunden-Servicefensters gesendet werden, wurden kostenlos
- Aktualisierte Utility-/Authentifizierungsraten in mehreren Märkten mit neuen Volumenstufen
- Neue Regeln zur Fehlkategorisierung von Utility-Templates – Unternehmen können mit Template-Ablehnung und Einreichungsbeschränkungen rechnen

### April 2025: Pause für Marketing-Nachrichten an US-Telefonnummern
*Letztes Update August 2025*

Meta unterbricht die Zustellung aller Marketing-Template-Nachrichten an WhatsApp-Nutzer:innen mit einer US-Telefonnummer (eine Nummer, die sich aus der Vorwahl `+1` und einer US-Ortsvorwahl zusammensetzt). Es gibt derzeit keinen geplanten Termin, wann diese Pause aufgehoben wird.

Jeder Versuch, ein Template an eine:n WhatsApp-Nutzer:in mit einer US-Telefonnummer zu senden, führt zu dem Fehlercode `131049`.

### März 2025: Einschränkungen bei Fehlkategorisierung von Templates
*Letztes Update März 2026*

- Meta hat Durchsetzungsmaßnahmen für Unternehmen eingeführt, die die Utility-/Marketing-Kategorisierung missbrauchen
- Dies kann zu 7–30-tägigen Einschränkungen bei der Template-Erstellung und Kategorieüberprüfungen führen

### März 2025: Nutzerspezifische Marketing-Template-Nachrichtenlimits
*Letztes Update August 2025*

Meta begrenzt die Anzahl der Marketing-Template-Nachrichten, die ein:e Nutzer:in innerhalb eines bestimmten Zeitraums von allen Unternehmen erhalten kann, und beginnt mit Nachrichten, die mit geringerer Wahrscheinlichkeit gelesen werden.

Eine Ausnahme besteht, wenn eine Person auf eine Marketing-Nachricht antwortet – dadurch wird ein 24-Stunden-Kundenservice-Fenster geöffnet. Marketing-Nachrichten, die innerhalb dieses Zeitfensters gesendet werden, werden nicht auf das Limit der Person angerechnet.

Das spezifische Limit variiert je nach Nutzer:in und hängt von deren Engagement-Level ab. Erfahren Sie [hier](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits) mehr über die nutzerspezifischen Marketing-Template-Nachrichtenlimits von WhatsApp.

### Januar 2025: WhatsApp pausiert den Versand von Marketing-Nachrichten an US-Nutzer:innen ab dem 1. April
*Letztes Update Januar 2025*

WhatsApp stellt den Versand von Marketing-Nachrichten an US-Nutzer:innen (Personen mit US-Telefonnummern) ab dem 1. April 2025 ein. [Utility-, Service- und Authentifizierungsnachrichten](https://developers.facebook.com/docs/whatsapp/pricing/) sowie [Antwortnachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) sind in den USA weiterhin zulässig.

Der Versand von Marketing-Nachrichten (und allen anderen Nachrichtentypen) in andere Länder und Regionen ist weiterhin zulässig und wird nicht beeinträchtigt.

Meta hat uns mitgeteilt, dass dieses Update dem Schutz des WhatsApp-Ökosystems in den USA dient, wo WhatsApp zwar schnell wächst, sich aber noch in einem frühen Stadium befindet (so ist das Engagement bei Marketing-Nachrichten geringer als in anderen Regionen). Es soll weiter geprüft werden, wann der US-Markt wieder für Marketing-Nachrichten bereit ist.

Die Zustellung von Marketing-Nachrichten an Telefonnummern mit US-Vorwahl wird von WhatsApp abgelehnt und führt zu dem Fehlercode 131049.

### November 2024: Änderung der Opt-in-Richtlinie von WhatsApp
*Letztes Update Januar 2025*

Meta hat kürzlich seine [Opt-in-Richtlinie](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) aktualisiert. Anstatt eine kanalspezifische Zustimmung zu verlangen, können Unternehmen jetzt Nachrichten auf der Plattform senden, wenn:

1. Die Person ihre Telefonnummer angegeben hat.
2. Die Person eine allgemeine Einwilligung zum Nachrichtenempfang erteilt hat, nicht nur für WhatsApp.

Unternehmen müssen weiterhin alle lokalen Gesetze einhalten und bei der Einholung von Opt-ins die folgenden Anforderungen erfüllen:

- Unternehmen müssen deutlich darauf hinweisen, dass die Person dem Erhalt von Mitteilungen des Unternehmens zustimmt.
- Unternehmen müssen den Unternehmensnamen, von dem die Person Nachrichten erhalten wird, deutlich angeben.
- Unternehmen müssen sich an geltendes Recht halten.

Obwohl WhatsApp seine Richtlinie gelockert hat, empfiehlt Braze weiterhin, Opt-ins speziell für den WhatsApp-Kanal einzuholen, um das bestmögliche Kundenerlebnis und hohe Engagement-Raten zu fördern. Wie immer sollten Sie mit Ihrer Rechtsabteilung abklären, was für Ihre Marke sinnvoll ist.

### November 2024: Update des Limits für Marketing-Templates pro Nutzer:in in den USA vor der Weihnachtszeit
*Letztes Update Dezember 2024*

Seit der Einführung des nutzerspezifischen Marketing-Template-Limits hat Meta deutliche Verbesserungen bei Leseraten und Nutzerstimmung festgestellt.

Ab sofort, noch vor der Weihnachtszeit, werden Personen in den USA weniger neue Marketing-Konversationen erhalten. Meta geht davon aus, dass diese Änderung zu stärker engagierten Zielgruppen führt, was letztlich bessere Ergebnisse für Unternehmen bedeutet. Dies kann zu niedrigeren Zustellraten für Ihr Unternehmen führen, wenn Sie Marketing-Nachrichten an US-Telefonnummern senden. Sie können dies mit dem Fehlercode `131049` über Braze-Currents und das Nachrichtenaktivitätsprotokoll überwachen.

Unternehmen in den USA können nach wie vor Marketing-Nachrichten in andere Regionen senden, und es gibt keine Auswirkungen auf Utility-, Authentifizierungs- oder Servicenachrichten oder Marketing-Template-Nachrichten, die innerhalb eines von Nutzer:innen initiierten Konversationsfensters gesendet werden (z. B. eine Click-to-WhatsApp-Anzeige, ein Produktkarussell oder ein Gutschein-Template, das als Teil einer Konversation gesendet wird).

### November 2024: WhatsApp erweitert die qualitätsbasierten Kontodurchsetzungen um Leseraten
*Letztes Update Dezember 2024*

WhatsApp investiert kontinuierlich in neue Wege, um Unternehmen dabei zu helfen, hochwertige Erlebnisse für ihre Kund:innen zu schaffen, wie z. B. die Reduzierung von Spam-ähnlichem Verhalten auf der Plattform.

Am 22. November hat WhatsApp damit begonnen, die bestehenden Qualitätsmaßnahmen auf Kontoebene auf WhatsApp Business Accounts (WABAs) mit extrem niedrigen Leseraten auszuweiten. Diese Änderung wird weltweit eingeführt.

Wenn die Leserate eines Kontos signifikant sinkt (z. B. wenn die Mehrheit der vom Konto gesendeten Nachrichten ungelesen bleibt), werden für das Konto Nachrichtensperren verhängt. Die Schwere der Sperre nimmt zu, wenn die Leseraten bei hohem Volumen konstant niedrig bleiben.

Bei einer extrem niedrigen Leserate werden folgende Maßnahmen ergriffen:

- Das Konto wird für den Versand von geschäftlich initiierten Nachrichten gesperrt. Es können weiterhin Antworten auf kundenseitig initiierte Nachrichten gesendet werden. Diese anfängliche Sperre ist eine „weiche Sperre" und kann bestätigt werden, indem Sie im Bereich „Account Quality" auf die Schaltfläche „Bestätigen" klicken, um die Nachrichtenübermittlung wieder aufzunehmen.
- Wenn die Leserate weiter sinkt oder nach der weichen Sperre niedrig bleibt, müssen Unternehmen möglicherweise mit einer schrittweisen Verschärfung der Durchsetzungsmaßnahmen rechnen (z. B. einige Tage lang Einschränkungen bei der Nachrichtenübermittlung).
- Unternehmen müssen das erzwungene Limit abwarten, um wieder Nachrichten senden zu können. Wenn die Leserate auch nach wiederholten weichen Sperren niedrig bleibt, wird das Konto letztendlich abgeschaltet.

#### Wie Sie über diese Warnungen und Durchsetzungsmaßnahmen auf dem Laufenden bleiben

Ähnlich wie bei bestehenden Plattformdurchsetzungen werden Unternehmen über diese Maßnahmen benachrichtigt und können sie über die Seite „Account Quality" im WhatsApp Business Manager bestätigen. Vergewissern Sie sich, dass im WhatsApp Business Manager die korrekten Kontaktdaten für alle erforderlichen Administratoren hinterlegt sind, da die E-Mails zu Durchsetzungsmaßnahmen auf Grundlage dieser Informationen versendet werden.

Benachrichtigungen über schwere Spam-Verstöße werden:

- Im Benachrichtigungscenter des WhatsApp Business Managers angezeigt
- In einem Banner im WhatsApp Manager angezeigt
- Als E-Mail an alle im WhatsApp Business Manager festgelegten Administratoren gesendet

### Mai 2024: Cloud API geht in Türkiye live
*Letztes Update Mai 2024*

Meta bietet Cloud-API-Unternehmen jetzt Zugang zu Türkiye für geschäftliche Nachrichten. Zuvor war die WhatsApp Cloud API für Unternehmen in der Türkei verfügbar, aber WhatsApp-Nutzer:innen mit türkischen Nummern konnten keine Nachrichten über die Cloud API senden oder empfangen.

Meta weist Nutzer:innen stets darauf hin, wenn sie mit einem von Meta gehosteten Unternehmen chatten, und alle Nutzer:innen müssen die entsprechenden WhatsApp-Nutzungsbedingungen und die Datenschutzrichtlinie akzeptieren, um mit dem geschäftlichen Nachrichtenaustausch fortzufahren. Die Aktualisierung der Nutzungsbedingungen und der Datenschutzrichtlinie von 2021 in der Türkei war zunächst ausgesetzt worden, wird aber jetzt umgesetzt. Das ändert nichts an Metas Engagement für den Datenschutz – persönliche Gespräche werden weiterhin durch End-to-End-Verschlüsselung geschützt, sodass nur Sie und die vorgesehene Empfängerseite sie sehen können. Das Update ermöglicht türkischen Nutzer:innen den Zugriff auf optionale Geschäftsfunktionen, wenn sie sich dafür entscheiden, und bietet mehr Transparenz darüber, wie WhatsApp funktioniert.

Cloud-API-Unternehmen können jetzt Konversationen mit WhatsApp-Nutzer:innen mit türkischen Nummern einleiten. Anstelle des bisherigen Fehlercodes 131026 wird nun ein Webhook als „gesendete" Konversation zurückgegeben.

Damit eine geschäftliche Nachricht als „zugestellt" oder „gelesen" gilt, muss die Empfängerseite zunächst die WhatsApp-Bedingungen akzeptieren. Einem Unternehmen werden keine Kosten in Rechnung gestellt, solange die Nachricht nicht zugestellt wird.

Nutzer:innen, die eine Nachricht von einem Cloud-API-Unternehmen erhalten oder eine senden möchten, erhalten eine In-App-Benachrichtigung über die Aktualisierung der Bedingungen, die klarstellt, dass sie einem Cloud-API-Unternehmen erst dann Nachrichten senden können, wenn sie das WhatsApp-Update akzeptiert haben. Darüber hinaus werden Nutzer:innen, die die App auf ihrem Telefon registrieren oder neu registrieren, aufgefordert, das WhatsApp-Update zu akzeptieren.

Sobald ein:e Nutzer:in das Update akzeptiert hat, wird beim Chat mit einem Cloud-API-Unternehmen die bestehende Cloud-API-Systemnachricht angezeigt.

### Mai 2024: Nutzerspezifische Marketing-Template-Nachrichtenlimits
*Letztes Update Mai 2024*

Meta führt neue Ansätze ein, um ein hochwertiges Nutzererlebnis zu gewährleisten und das Engagement bei Marketing-Template-Nachrichten auf der WhatsApp-Plattform zu maximieren. Ab dem 23. Mai 2024 wird die Anzahl der Marketing-Template-Nachrichten begrenzt, die jede:r einzelne Nutzer:in von allen Unternehmen, mit denen sie interagieren, innerhalb eines bestimmten Zeitraums erhalten kann. Dabei wird mit einer kleinen Anzahl von Konversationen begonnen, die mit geringerer Wahrscheinlichkeit gelesen werden. Beachten Sie, dass das Limit auf der Anzahl der Marketing-Template-Nachrichten basiert, die diese Person bereits von anderen Unternehmen erhalten hat, und sich nicht speziell auf Ihre Marke bezieht. Dies kann jedoch die Zustellbarkeit Ihrer Marketing-Template-Nachrichten beeinträchtigen.

Das Limit gilt nur für Marketing-Template-Nachrichten, die normalerweise eine neue Marketing-Konversation eröffnen würden. Wenn bereits eine Marketing-Konversation zwischen Ihrer Marke und einer:m WhatsApp-Nutzer:in läuft, sind die an diese:n Nutzer:in gesendeten Marketing-Template-Nachrichten nicht betroffen.

Wird eine Marketing-Template-Nachricht aufgrund des Limits nicht an eine:n bestimmte:n Nutzer:in zugestellt, gibt die Cloud API den Fehlercode 131026 zurück. Beachten Sie jedoch, dass diese Fehlercodes eine breite Palette von Problemen abdecken, die dazu führen können, dass eine Nachricht nicht zugestellt wird. Aus Datenschutzgründen gibt Meta nicht bekannt, ob die Nachricht tatsächlich aufgrund des Limits nicht zugestellt wurde. Im [Dokument zur Fehlerbehebung](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) der Cloud API finden Sie Beschreibungen der Gründe für die Nichtzustellung und Hinweise, wie Sie die zugrunde liegende Ursache ermitteln können.

Wenn Sie einen dieser Fehlercodes erhalten und vermuten, dass er auf das Limit zurückzuführen ist, sollten Sie die Template-Nachricht nicht sofort erneut senden, da dies nur zu einer weiteren Fehlerantwort führen würde.

Weitere Informationen zu diesem Zustellbarkeits-Update, einschließlich Details zur Überwachung Ihrer Zustellbarkeit und weiterer Best Practices für Marketing-Nachrichten auf WhatsApp, finden Sie in unserem aktuellen [Blogbeitrag](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### April 2024: Template Pacing für Utility-Templates
*Letztes Update April 2024*

Letztes Jahr hat WhatsApp das Template Pacing für Marketing-Nachrichten eingeführt, um Unternehmen dabei zu helfen, das Engagement ihrer Templates zu verbessern und wertvolle Nutzererlebnisse zu schaffen. Ab dem 30. April wird das Template Pacing auf Utility-Nachrichten ausgeweitet. Wenn ein Utility-Template für ein Konto aufgrund von Nutzerfeedback pausiert wird, werden die neuen Utility-Templates, die in den nächsten sieben Tagen erstellt werden, ebenfalls dem Pacing unterzogen.

### April 2024: Leseraten beeinflussen die Qualitätsbewertung für Marketing-Templates
*Letztes Update März 2024*

WhatsApp testet neue Ansätze, beginnend mit Verbraucher:innen in Indien, um wertvollere Erlebnisse zu schaffen und das Engagement bei Marketing-Konversationen von Unternehmen zu maximieren. Dazu kann es gehören, die Anzahl der Marketing-Konversationen, die eine Person in einem bestimmten Zeitraum von einem Unternehmen erhält, zu begrenzen – angefangen mit einer kleinen Anzahl von Konversationen, die mit geringerer Wahrscheinlichkeit gelesen werden. Braze gibt einen Fehlercode aus, wenn eine Nachricht nicht zugestellt wird.

WhatsApp wird damit beginnen, die Leseraten als Teil der Qualitätsbewertung für Marketing-Templates zu berücksichtigen, neben traditionellen Metriken wie Blockierungen und Meldungen. WhatsApp kann Marketing-Kampagnen mit niedrigen Leseraten vorübergehend pausieren, um Unternehmen Zeit zu geben, die Templates mit dem geringsten Engagement zu überarbeiten, bevor das Volumen ab dem 1. April 2024 erhöht wird.

### Februar 2024: Experimente mit Marketing-Konversationen
*Letztes Update Februar 2024*

Ab dem 6. Februar 2024 testet WhatsApp neue Ansätze, beginnend mit Verbraucher:innen in Indien, um wertvollere Erlebnisse zu schaffen und das Kundenengagement mit den Marketing-Konversationen Ihrer Marke zu maximieren. Dazu kann es gehören, die Anzahl der Marketing-Konversationen zu begrenzen, die ein:e Nutzer:in in einem bestimmten Zeitraum von Ihrer Marke erhält – angefangen mit einer kleinen Anzahl von Konversationen, die mit geringerer Wahrscheinlichkeit gelesen werden.

### Oktober 2023: Template Pacing
*Letztes Update Oktober 2023*

Am 12. Oktober 2023 führt WhatsApp ein Konzept namens „Template Pacing" für Marketing-Nachrichten ein. Anstatt Ihre Nachricht gleichzeitig an die gesamte Zielgruppe Ihrer Kampagne zu senden, wird die Nachricht beim „Template Pacing" zunächst an eine kleinere Untergruppe von Nutzer:innen gesendet, um Echtzeit-Feedback von den Kampagnenempfänger:innen zu erhalten, bevor die restlichen Nachrichten versendet werden.

Die Obergrenze (der zuerst versendeten Nachrichten) ist dabei je nach Template unterschiedlich. Nach dem ersten Versand hält WhatsApp die verbleibenden Nachrichten für maximal 30 Minuten zurück. Während dieser Wartezeit wird die Qualität des Templates anhand des Kundenfeedbacks bewertet. Fällt das Feedback positiv aus, was auf ein hochwertiges Template hindeutet, werden die restlichen Nachrichten zugestellt. Fällt das Feedback negativ aus, werden die verbleibenden, nicht zugestellten Nachrichten verworfen. Dadurch wird weiteres negatives Feedback von einem größeren Teil Ihrer Kund:innen verhindert und Sie können potenzielle Probleme bei der Qualitätsdurchsetzung vermeiden (z. B. Auswirkungen auf die Qualitätsbewertung von Telefonnummern).

Beachten Sie, dass WhatsApp bei der Bewertung der Template-Qualität im Template Pacing dasselbe System verwendet wie bei der Template-Pausierung. Die Nachrichten, die beim Template Pacing aufgrund niedriger Qualität nicht zugestellt werden, sind also dieselben, die auch in größerem Umfang pausiert worden wären.

Letztendlich bietet Ihnen dieses Update eine schnellere Feedbackschleife (30 Minuten gegenüber Stunden oder Tagen bei der Template-Pausierung), sodass Sie Ihre Templates anpassen und ein besseres Kundenerlebnis bieten können.

**Wenn Sie weitere Fragen zu diesem Update haben, wenden Sie sich an die Vertretung Ihres Meta-Partners.**

### Juni 2023: Messaging-Experimente
*Letztes Update Juni 2023*

Ab dem 14. Juni 2023 führt Meta neue Experimentierverfahren auf der WhatsApp-Plattform ein, um herauszufinden, wie sich Marketing-Nachrichten auf das Kundenerlebnis und das Engagement auswirken. Dieses Experiment kann sich auf Ihre Marketing-Nachrichten auswirken, die über die WhatsApp Business API mit Braze versendet werden.

Meta beabsichtigt, solche Experimente auf der WhatsApp-Plattform fortzusetzen. Weitere Informationen finden Sie in [der Dokumentation von Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl).

**Die WhatsApp-Experimente betreffen nur Marketing-Nachrichten.** Dieses Experiment kann die Zustellung von Marketing-Template-Nachrichten beeinflussen. Utility- und Authentifizierungs-Templates werden weiterhin ohne Auswirkungen durch das Experiment zugestellt.

Für das Experiment wählt Meta zufällig etwa 1 % der WhatsApp-Nutzer:innen als Teilnehmende aus. Meta stellt diesen keine Marketing-Template-Nachrichten zu, es sei denn, eine der folgenden Bedingungen trifft zu:

- Die Person hat Ihnen in den letzten 24 Stunden geantwortet;
- Eine bestehende Marketing-Konversation ist offen; oder
- Die Person hat in den letzten 72 Stunden auf eine WhatsApp-Anzeige geklickt.

## Häufig gestellte Fragen {#faq}

### Woher weiß ich, ob meine Marketing-Nachricht von Metas Experiment betroffen war?

Wenn eine Nachricht aufgrund des Experiments nicht zugestellt werden kann, wird ein spezieller Fehlercode im Aktivitätsprotokoll und in Currents angezeigt. Die Nachricht wird auch als Fehlschlag gezählt und in Ihre WhatsApp-Fehlermetriken in allen Berichten im Braze-Dashboard aufgenommen. Diese Nachrichten sind für Sie nicht kostenpflichtig.

Der Fehlercode 130472 besagt: „Die Rufnummer ist Teil eines Experiments." Weitere Informationen zu den Fehlercodes der WhatsApp Cloud API finden Sie in der [Dokumentation von Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k).

### Kann ich mich von Metas Experiment abmelden?

Nein, Meta erlaubt keine Abmeldung von Experimenten. Alle Anbieter und Nutzer:innen der WhatsApp Business API unterliegen diesem Meta-Experiment.

### Kann ich versuchen, ein Template später erneut zu senden?

Es gibt keinen festen Zeitrahmen für dieses Experiment. Daher kann eine Person weiterhin dem Experiment unterliegen.

### Was kann ich tun, wenn meine Marketing-Nachrichten aufgrund von Metas Experiment nicht zugestellt werden?

Wir empfehlen Ihnen, andere Braze-Kanäle wie E-Mail, SMS, Push-Benachrichtigungen oder In-App-Nachrichten zu verwenden, um eine Nachricht mit ähnlichem Inhalt an Ihre Zielnutzer:innen zu senden.