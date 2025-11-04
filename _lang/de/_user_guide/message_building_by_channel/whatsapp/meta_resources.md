---
nav_title: Meta-Ressourcen
article_title: Meta-Ressourcen
page_order: 11
description: "In diesem Artikel finden Sie hilfreiche Informationen von Meta zur WhatsApp-Integration."
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

### April 2025: Pause für Marketing Nachrichten an US-Telefonnummern
*Letztes Update August 2025*

Meta unterbricht die Zustellung aller Marketing Template Nachrichten an Nutzer:innen von WhatsApp, die eine Telefonnummer in den USA haben (eine Nummer, die sich aus einer `+1` Vorwahl und einer US-Vorwahl zusammensetzt). Es gibt keinen aktuellen Zeitplan, wann diese Pause aufgehoben werden soll. 

Jeder Versuch, ein Template an einen Nutzer:innen von WhatsApp mit einer US-Telefonnummer zu senden, führt zu der Fehlermeldung `131049`.

### März 2025: Nutzerspezifische Werbetemplate-Nachrichtenlimits
*Letztes Update August 2025*

Meta begrenzt die Anzahl der Marketing Template Nachrichten, die ein Nutzer:innen innerhalb eines bestimmten Zeitraums in allen Unternehmen erhalten kann, und beginnt mit Nachrichten, die mit geringerer Wahrscheinlichkeit gelesen werden. 

Eine Ausnahme ist, dass eine Person, die auf eine Nachricht des Marketings antwortet, ein 24-Stunden-Fenster für den Kund:in-Dienst öffnet. Marketing Nachrichten, die innerhalb dieses Zeitfensters gesendet werden, werden nicht auf das Limit einer Person angerechnet.

Das spezifische Limit variiert je nach Nutzer:innen, abhängig von ihrem Engagement. Erfahren Sie [hier](https://developers.facebook.com/docs/whatsapp/cloud-api/guides/send-message-templates#per-user-marketing-template-message-limits) mehr über die Beschränkungen von WhatsApps Marketing Template Nachrichten pro Nutzer:innen. 

### Januar 2025: WhatsApp pausiert den Versand von Werbenachrichten an Nutzer:innen in den USA ab dem 1\. April
*Letzte Änderung: Januar 2025*

WhatsApp stellt den Versand von Werbenachrichten an US-Telefonnummern ab dem 1\. April 2025 ein. Nachrichten über [Dienste, Service und Authentifizierung](https://developers.facebook.com/docs/whatsapp/pricing/) sowie [Antwortnachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) sind in den USA weiterhin zulässig. 

Der Versand von Werbenachrichten (und allen anderen Nachrichtentypen) in andere Länder und Regionen ist weiterhin zulässig und wird nicht beeinträchtigt.

Meta hat uns mitgeteilt, dass mit dem Update das WhatsApp-Ökosystem in den USA geschützt werden soll, wo WhatsApp zwar schnell wächst, sich aber noch in einem frühen Stadium befindet (so ist das Engagement bei Werbenachrichten geringer als in anderen Regionen). Es soll aber weiter geprüft werden, wann der US-Markt wieder für Werbenachrichten bereit ist.

Die Zustellung von Werbenachrichten an Telefonnummern mit US-Vorwahl wird von WhatsApp unterbunden und führt zu dem Fehlercode 131049. 

### November 2024: Änderung der Einwilligungsrichtlinie von WhatsApp
*Letzte Änderung: Januar 2025*

Meta hat kürzlich seine [Einwilligungsrichtlinie](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) geändert. Auch ohne kanalspezifische Zustimmungen können Unternehmen ab sofort Nachrichten auf der Plattform senden, wenn:

1. Der Betroffene seine Rufnummer angegeben hat
2. Der Betroffene allgemeinen Benachrichtigungen zugestimmt hat, nicht nur solchen von WhatsApp. 

Unternehmen müssen auch künftig die lokalen Gesetze einhalten und bei der Einholung von Opt-ins die folgenden Anforderungen erfüllen:

- Unternehmen müssen deutlich darauf hinweisen, dass sich die Einwilligung auf den Erhalt von Mitteilungen des Unternehmens bezieht.
- Unternehmen müssen den Firmennamen, auf den sich die Einwilligung bezieht, deutlich angeben.
- Unternehmen müssen sich an geltendes Recht halten.

Obwohl WhatsApp seine Richtlinien gelockert hat, empfiehlt Braze auch weiterhin, Opt-ins speziell für den WhatsApp-Kanal einzuholen, um Kundenerlebnis und Engagement zu fördern. Wie immer sollten Sie mit Ihrer Rechtsabteilung abklären, was für Ihr Unternehmen sinnvoll ist.

### November 2024: Update des Limits für Marketing-Templates pro Nutzer:innen in den USA, noch vor der Weihnachtszeit
*Zuletzt aktualisiert im Dezember 2024*

Seit der Einführung des nutzerspezifischen Werbetemplate-Limits hat Meta deutliche Verbesserungen an Leserate und Stimmung festgestellt.
 
Ab jetzt, noch vor der Urlaubssaison, werden die Menschen in den USA weniger neue Marketinggespräche erhalten. Meta geht davon aus, dass diese Veränderung zu einem stärkeren Engagement der Zielgruppen führt, was letztlich zu besseren Ergebnissen für Unternehmen führt. Dies kann zu niedrigeren Zustellungsraten für Ihr Unternehmen führen, wenn Sie Marketingnachrichten an US-Telefonnummern senden. Dies kann mit dem Fehlercode `131049` über Braze Currents und das Nachrichtenaktivitätsprotokoll überwacht werden.

Unternehmen in den USA können nach wie vor Marketingnachrichten in anderen Regionen verschicken, und es gibt keine Auswirkungen auf Dienstleistungs-, Authentifizierungs- oder Servicenachrichten oder Marketingvorlagen, die innerhalb eines vom Benutzer initiierten Konversationsfensters verschickt werden (z. B. eine Click-to-WhatsApp-Anzeige oder ein Produktkarussell oder eine Gutscheinvorlage, die als Teil einer Konversation verschickt wird). 

### November 2024: WhatsApp erweitert die qualitätsbasierten Kontoerzwingungen um die Leseraten
*Zuletzt aktualisiert im Dezember 2024*

WhatsApp investiert kontinuierlich in neue Wege, um Unternehmen dabei zu helfen, hochwertige Erlebnisse für ihre Kunden zu schaffen, wie z.B. die Reduzierung von Spam-ähnlichem Verhalten auf ihrer Plattform. 

Am 22\. November hat WhatsApp damit begonnen, die bestehenden Qualitätsmaßnahmen auf Account-Ebene auf WhatsApp Business Accounts (WABAs) mit extrem niedrigen Leseraten auszuweiten. Diese Änderung wird weltweit eingeführt.

Wenn die Leserate eines Kontos signifikant sinkt (z. B. wenn die Mehrheit der von dem Konto gesendeten Nachrichten ungelesen bleibt), werden für das Konto Nachrichtensperren verhängt. Die Sperre wird noch verschärft, wenn die Leserate gemessen an der Größe konstant niedrig ist. 

Bei einer extrem niedrigen Leserate werden folgende Maßnahmen ergriffen:

- Das Konto wird für den Versand von geschäftlich veranlassten Nachrichten gesperrt. Sie können weiterhin auf Kundennachrichten reagieren. Diese anfängliche Sperre ist eine "weiche Sperre" und kann bestätigt werden, indem Sie auf die Schaltfläche Bestätigen in der Kontoqualität klicken, um die Nachrichtenübermittlung wieder aufzunehmen.
- Wenn die Leserate weiter sinkt oder nach dem Soft Lock niedrig bleibt, müssen Unternehmen möglicherweise mit einer schrittweisen Verschärfung der Durchsetzungsmaßnahmen rechnen (z. B. einige Tage lang Beschränkungen bei der Nachrichtenübermittlung).
- Unternehmen müssen das erzwungene Limit abwarten, um mit dem Messaging fortzufahren. Wenn die Leserate auch nach wiederholten Soft Locks niedrig bleibt, wird das Konto abgeschaltet.

#### Wie Sie über diese Warnungen und Durchsetzungsmaßnahmen auf dem Laufenden bleiben

Ähnlich wie bei der bestehenden Durchsetzung der Plattform werden Unternehmen über diese Aktionen benachrichtigt und können sie über die Seite Account Quality im WhatsApp Business Manager bestätigen. Vergewissern Sie sich, dass Sie im WhatsApp Business Manager die korrekten Kontaktdaten für alle erforderlichen Administratoren angegeben haben, da die Benachrichtigungs-E-Mails zur Durchsetzung der Bestimmungen auf der Grundlage dieser Informationen gesendet werden.

Benachrichtigungen über schwere Spam-Verstöße:

- Aufgetaucht im WhatsApp Business Manager Benachrichtigungscenter
- Wird in einem Banner im WhatsApp Manager angezeigt
- Wird als E-Mail an alle im WhatsApp Business Manager festgelegten Administratoren gesendet

### Mai 2024: Cloud API geht in Türkiye live
*Zuletzt aktualisiert im Mai 2024*

Meta bietet jetzt Cloud API-Unternehmen Zugang zu Türkiye für Geschäftsnachrichten. Zuvor war die WhatsApp Cloud API für Unternehmen in der Türkei verfügbar, aber WhatsApp-Nutzer mit türkischen Nummern konnten keine Nachrichten über die Cloud API senden oder empfangen. 

Meta weist die Nutzer stets darauf hin, wenn sie mit einem von Meta gehosteten Unternehmen chatten, und alle Nutzer müssen die entsprechenden WhatsApp-Nutzungsbedingungen und Datenschutzrichtlinien akzeptieren, um mit dem geschäftlichen Nachrichtenaustausch fortzufahren. Die Aktualisierung der Nutzungsbedingungen und der Datenschutzrichtlinien in der Türkei im Jahr 2021 war zunächst ausgesetzt worden, wird aber jetzt durchgeführt. Das ändert nichts an Metas Datenschutzversprechen: Persönliche Gespräche werden weiterhin per Ende-zu-Ende-Verschlüsselung geschützt, sodass nur Sie und der Empfänger sie sehen können. Das Update ermöglicht türkischen Nutzern den Zugriff auf optionale Geschäftsfunktionen, wenn sie sich dafür entscheiden, und bietet mehr Transparenz darüber, wie WhatsApp funktioniert.  
 
Unternehmen, die eine Cloud API nutzen, können jetzt Konversationen mit Nutzer:innen von WhatsApp mit türkischen Nummern einleiten. Anstelle des heutigen Fehlercodes 131026 wird nun ein Webhook als "gesendete" Konversation zurückgegeben.

Damit eine geschäftliche Nachricht zugestellt und gelesen werden kann, muss die Empfängerseite zunächst die WhatsApp-Bedingungen akzeptieren. Einem Unternehmen werden keine Kosten in Rechnung gestellt, wenn die Nachricht nicht zugestellt wird.

Benutzer, die eine Nachricht an ein Cloud-API-Unternehmen erhalten oder zu senden versuchen, erhalten eine In-App-Benachrichtigung über die Aktualisierung der Bedingungen, die klarstellt, dass sie einem Cloud-API-Unternehmen erst dann eine Nachricht senden können, wenn sie das WhatsApp-Update akzeptiert haben. Darüber hinaus werden Benutzer, die die App auf ihrem Telefon registrieren oder neu registrieren, aufgefordert, das WhatsApp-Update zu akzeptieren.

Wenn das Update angenommen wird, wird bei Chats mit Cloud-API-Unternehmen eine Nachricht des bestehenden Cloud-API-Systems angezeigt.

### Mai 2024: Nutzerspezifische Werbetemplate-Nachrichtenlimits
*Zuletzt aktualisiert im Mai 2024*

Meta führt derzeit ein neues Verfahren ein, um das Nutzererlebnis zu schützen und das Engagement bei Werbetemplate-Nachrichten bei WhatsApp zu maximieren. Ab dem 23\. Mai 2024 werden sie die Anzahl der Marketingvorlagen begrenzen, die jeder einzelne Nutzer von allen Unternehmen, mit denen er innerhalb eines bestimmten Zeitraums interagiert, erhalten kann. Beachten Sie, dass das Limit auf der Anzahl der Marketingvorlagen basiert, die diese Person bereits von anderen Unternehmen erhalten hat, und sich nicht speziell auf Ihre Marke bezieht. Dies kann jedoch die Zustellbarkeit Ihrer Werbetemplate-Nachrichten beeinträchtigen.

Das Limit gilt nur für Nachrichten, wie sie zur Eröffnung von Werbegesprächen üblich sind. Wenn bereits eine Marketing-Konversation zwischen Ihrer Marke und einem WhatsApp-Nutzer läuft, sind die an den Nutzer gesendeten Marketing-Vorlagen nicht betroffen.

Wird eine Werbetemplate-Nachricht aufgrund des Limits nicht zugestellt, gibt die Cloud-API den Fehlercode 131026 zurück. Beachten Sie jedoch, dass diese Fehlercodes eine breite Palette von Problemen abdecken, die dazu führen können, dass eine Nachricht nicht zugestellt werden kann. Aus Gründen des Datenschutzes gibt Meta nicht bekannt, ob die Nachricht aufgrund des Limits tatsächlich nicht zugestellt wurde. Im [Dokument zur Fehlerbehebung](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting) von Cloud API finden Sie Beschreibungen der Gründe für die Nichtzustellung und was Sie tun können, um die zugrunde liegende Ursache zu ermitteln.

Wenn Sie einen dieser Fehlercodes erhalten und vermuten, dass er auf das Limit zurückzuführen ist, sollten Sie die Vorlage nicht sofort erneut senden, da dies nur zu einer weiteren Fehlerantwort führen würde. 

Weitere Informationen zu der Änderung und zur Zustellbarkeitskontrolle sowie Tipps zu Werbenachrichten auf WhatsApp finden Sie in unserem neuesten [Blogbeitrag](https://www.braze.com/resources/articles/meta-introduces-deliverability-updates-for-whatsapp?utm_campaign=fy25-q2-global-customer-customer-meta-deliverability-updates-for-whatsapp&utm_medium=email-cdb&utm_source=braze&utm_content=blog-meta-deliverability-updates-for-wa-blog).

### April 2024: Template-Begrenzung bei Utility-Vorlagen
*Zuletzt aktualisiert im April 2024*

Letztes Jahr hat WhatsApp das Template Pacing für Marketing-Nachrichten eingeführt, um Unternehmen dabei zu helfen, das Engagement ihrer Templates zu verbessern und wertvolle Nutzererlebnisse zu schaffen. Ab dem 30\. April werden die Vorlagen auf Nachrichten von Versorgungsunternehmen ausgeweitet. Wenn eine Dienstprogrammvorlage für ein Konto aufgrund von Benutzerfeedback pausiert wird, werden die neuen Dienstprogrammvorlagen, die für die nächsten sieben Tage erstellt werden, beschleunigt.

### April 2024: Die Leseraten beeinflussen die Qualitätsbewertung für Marketingvorlagen 
*Zuletzt aktualisiert im März 2024*

WhatsApp testet neue Ansätze, beginnend mit Verbrauchern in Indien, um wertvollere Erfahrungen zu schaffen und die Einbindung in Marketingkonversationen von Unternehmen zu maximieren. Dazu kann es gehören, die Anzahl der Marketinggespräche, die eine Person in einem bestimmten Zeitraum von einem Unternehmen erhält, zu begrenzen und mit einer kleinen Anzahl von Gesprächen zu beginnen, die weniger wahrscheinlich gelesen werden. Braze gibt einen Fehlercode aus, wenn eine Nachricht nicht zugestellt wird.

WhatsApp wird damit beginnen, die Leseraten als Teil unserer Qualitätsbewertung für Marketingvorlagen zu berücksichtigen, neben traditionellen Metriken wie Blöcken und Berichten. WhatsApp kann Werbekampagnen mit geringem Engagement unterbrechen, um dem jeweiligen Unternehmen Zeit zu geben, die entsprechenden Templates zu überarbeiten, bevor das Volumen ab dem 1\. April 2024 erhöht wird. 

### Februar 2024: Werbenachrichten
*Zuletzt aktualisiert im Februar 2024*

Ab dem 6\. Februar 2024 testet WhatsApp neue Ansätze, beginnend mit Verbrauchern in Indien, um wertvollere Erlebnisse zu schaffen und das Kundenengagement mit den Marketingkonversationen Ihrer Marke zu maximieren. Dazu kann es gehören, die Anzahl der Marketingkonversationen zu begrenzen, die ein Nutzer in einem bestimmten Zeitraum von Ihrer Marke erhält, und mit einer kleinen Anzahl von Konversationen zu beginnen, die mit geringerer Wahrscheinlichkeit gelesen werden.

### Oktober 2023: Template-Begrenzung 
*Zuletzt aktualisiert im Oktober 2023*

Am 12\. Oktober 2023 führt WhatsApp die Template-Begrenzung (<i>template pacing</i>) für Werbenachrichten ein. Anstatt Ihre Nachricht gleichzeitig an die gesamte Zielgruppe Ihrer Kampagne zu senden, wird die Nachricht zunächst an eine kleinere Untergruppe von Nutzern gesendet, um Echtzeit-Feedback von den Empfängern der Kampagne zu erhalten, bevor die restlichen Nachrichten gesendet werden. 

Die Obergrenze (der zuerst versendeten Nachrichten) ist dabei je nach Template unterschiedlich. Nach dem ersten Versand hält WhatsApp die verbleibenden Nachrichten für maximal 30 Minuten zurück. Während dieser Wartezeit bewerten sie die Qualität der Vorlage anhand des Kundenfeedbacks. Wenn das Feedback positiv ausfällt, was auf ein hochwertiges Template hindeutet, werden die restlichen Nachrichten zugestellt. Wenn das Feedback negativ ausfällt, werden die verbleibenden, nicht zugestellten Nachrichten gelöscht. Dadurch wird weiteres negatives Feedback von einem größeren Teil Ihrer Kunden verhindert und Sie können potenzielle Probleme bei der Durchsetzung der Qualität vermeiden (z. B. Auswirkungen auf die Qualitätsbewertung von Telefonnummern). 

Beachten Sie, dass WhatsApp bei der Bewertung der Template-Qualität dasselbe System verwendet wie bei der Template-Unterbrechung. Die Nachrichten, die aufgrund der Template-Begrenzung  (wegen ihrer schlechten Qualität) nicht zugestellt werden, sind also dieselben, die auch ansonsten pausiert würden. 

Letztendlich bietet Ihnen dieses Update eine schnellere Feedbackschleife (30 Minuten gegenüber Stunden oder Tagen mit Vorlagenpausen), so dass Sie Ihre Vorlagen anpassen und ein besseres Kundenerlebnis bieten können.

**Falls Sie Fragen zu dem Update haben, wenden Sie sich bitte an Ihren Meta-Partner.**

### Juni 2023: Versuchsphase 
*Zuletzt aktualisiert im Juni 2023*

Ab dem 14\. Juni 2023 führt Meta neue Versuchsverfahren bei WhatsApp ein, um zu herauszufinden, wie sich Werbenachrichten auf Kundenerlebnis und Engagement auswirken. Dies kann sich auf Ihre Werbenachrichten auswirken, die in Braze über die WhatsApp Business API versendet werden.

Meta beabsichtigt, solche Experimente auf der WhatsApp-Plattform fortzusetzen. Weitere Informationen finden Sie in [der Dokumentation von Meta](https://developers.facebook.com/docs/whatsapp/on-premises/guides/experiments?content_id=86oue5PtwEgcBJl).

**Die WhatsApp-Experimente betreffen nur Marketing-Nachrichten.** Der Versuch kann auch die Zustellung von Werbetemplate-Nachrichten beeinflussen. Utility- und Authentifizierungs-Templates werden auch weiterhin wie gewohnt zugestellt.

Für seinen Versuch wählt Meta zufällig etwa 1% der WhatsApp-Nutzerbasis aus. Meta stellt diesen keine Werbetemplate-Nachrichten zu, wenn nicht mindestens eine der folgenden Aussagen zutrifft:

- Wenn Ihnen ein Verbraucher in den letzten 24 Stunden geantwortet hat;
- Wenn ein bestehendes Marketinggespräch offen ist; oder
- Wenn der Verbraucher in den letzten 72 Stunden auf eine WhatsApp-Anzeige geklickt hat.

## Häufig gestellte Fragen {#faq}

### Woher weiß ich, ob meine Marketingbotschaft von Metas Experiment beeinflusst wurde?

Wenn eine Nachricht aufgrund des Experiments nicht zugestellt werden kann, wird ein spezieller Fehlercode im Aktivitätsprotokoll und in Currents angezeigt. Die Nachricht wird auch als Fehlschlag gezählt und in Ihre Metriken für WhatsApp-Fehlschläge in allen Berichten im Braze-Dashboard aufgenommen. Diese Nachrichten sind für Sie nicht kostenpflichtig.

Der Fehlercode 130472 besagt: "Die Rufnummer ist Teil eines Versuchs." Weitere Informationen zu den Fehlercodes der WhatsApp Cloud API finden Sie in der [Dokumentation von Meta](https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes?content_id=8SJRLBEjYGvXO9k).

### Kann ich mich von Metas Experiment abmelden?

Nein, Meta erlaubt keine Ablehnung von Experimenten. Dieses Meta-Experiment gilt für alle Anbieter und Nutzer der WhatsApp Business API.

### Kann ich versuchen, eine Vorlage später erneut zu senden?

Es gibt keine feste Zeit für dieses Experiment. Als solcher kann ein Verbraucher weiterhin dem Experiment unterliegen.

### Was kann ich tun, wenn meine Marketingnachrichten aufgrund von Metas Experiment nicht zugestellt werden?

Wir empfehlen Ihnen, andere Braze-Kanäle wie E-Mail, SMS, Push-Benachrichtigungen oder In-App-Nachrichten zu verwenden, um eine Nachricht mit ähnlichem Inhalt an Ihre Zielbenutzer zu senden.
