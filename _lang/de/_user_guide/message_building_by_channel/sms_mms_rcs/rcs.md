---
nav_title: "RCS"
article_title: Über Rich Communication Serviceleistungen; Dienste (RCS)
alias: /about_rcs/
page_type: reference
page_order: 14
description: "Dieser referenzierte Artikel behandelt allgemeine Anwendungsfälle des RCS-Kanals und die Anforderungen, die Sie erfüllen müssen, um Ihren RCS-Kanal einsatzbereit zu machen."
---

# Über Rich Communication Serviceleistungen; Dienste (RCS)

> Rich Communication Serviceleistungen; Dienste (RCS) verbessern die traditionelle SMS, indem sie Marken in die Lage versetzen, Nachrichten zuzustellen, die nicht nur informativ sind, sondern auch ein weitaus größeres Engagement bieten. RCS wird jetzt sowohl von Android als auch von iOS unterstützt und bringt Features wie hochwertige Medien, interaktive Buttons und gebrandete Absenderprofile direkt in die vorinstallierten Messaging-Apps der Nutzer:innen, so dass der Download einer separaten App entfällt.

Im Gegensatz zu Messaging-Anwendungen von Drittanbietern nutzt RCS die native Messaging-Umgebung (Apple Messages und Google Messages), so dass Sie die Nutzer:innen dort erreichen, wo sie bereits die meiste Zeit verbringen, und über die traditionellen SMS- und MMS-Erlebnisse hinausgehen, indem Sie eine reichhaltigere, interaktivere Kommunikation mit den Kund:innen ermöglichen. 

## Vorteile der Verwendung von RCS

- **Bessere Kundenerlebnisse:** Bieten Sie Ihren Nutzern durch die nahtlose Integration von Text, Bildmaterial und interaktiven Elementen ein besseres Erlebnis, steigern Sie das Engagement und ebnen Sie den Weg für personalisierte, datengestützte Kampagnen.
- **Vertrauenswürdige, markengeschützte Interaktionen:** Erzielen Sie vertrauenswürdige, markenbezogene Interaktionen durch eine überprüfte Sender ID, die nicht nur die Vorzüge Ihrer Marke hervorhebt, sondern auch die höchsten Datenschutzstandards der Branche erfüllt und so das Vertrauen und die Loyalität Ihrer Kund:innen stärkt.
- **Flexible Zustellung von Messaging:** Erleichtern Sie die flexible, zuverlässige Zustellung von Nachrichten mit einer nahtlosen SMS-Zustellung, die jedes Segmente der Zielgruppe erreicht, unabhängig von den Möglichkeiten des Geräts, und dabei ein einheitliches Nutzer:innen-Erlebnis gewährleistet.
- **Umsetzbare Insights:** Schalten Sie umsetzbare Insights mit fortschrittlichen Berichten frei, die kritische KPIs tracken und Sie in die Lage versetzen, Kampagnen in Realtime zu optimieren und messbare Erfolge zu erzielen.
- **Omnichannel-Synergie:** Integrieren Sie RCS nahtlos in Ihre umfassende Marketing Strategie, um konsistente, kanalübergreifende Kundenerlebnisse zu liefern und die Effektivität Ihrer Kampagnen und den ROI insgesamt zu steigern.

## Anwendungsfälle

| Anwendungsfall | Beschreibung |
| --- | --- |
| Interaktive Aktionen für Produkte | Erwecken Sie Aktionen zum Leben, indem Sie ansprechende Bilder oder kurze Videos mit detaillierten Produktdokumentationen kombinieren. Nutzen Sie die vorgeschlagenen Antworten (z.B. "In den Warenkorb" oder "Lernangebote") und openURL-Aktionen, um die sofortige Erkundung von Produkten und die Konversion zu fördern - und das alles in einem reichhaltigen In-Messaging-Erlebnis. |
| Personalisierte Updates für Treue und Rewards | Versenden Sie personalisierte Nachrichten, die mit hochwertigen Bildern und Details zu den Prämien angereichert sind. Verwenden Sie vorgeschlagene Antworten (wie "Jetzt einlösen" oder "Angebote ansehen") und openURL-Aktionen, um eine interaktive Customer Journey zu erstellen, die jedes Update visuell ansprechend und maßgeschneidert gestaltet, um sofortiges Engagement und eine stärkere Bindung zu fördern. |
| Sichere Transaktionen und Kontowarnungen | Liefern Sie sichere Kontowarnungen und Transaktionsbenachrichtigungen, indem Sie Bilder von PDF-Quittungen oder Dokumenten einfügen. Vorgeschlagene Aktionen (wie z.B. "Jetzt prüfen" oder "Support kontaktieren") und openURL-Links ermöglichen es Kund:innen, schnell auf weitere Details zuzugreifen oder Sicherheitsschritte einzuleiten, was sowohl die Zuverlässigkeit als auch das Vertrauen bei jeder Interaktion stärkt. |
| Reiseroute & Verbesserungen bei der Buchung | Verbessern Sie das Reiseerlebnis, indem Sie visuell ansprechende Reiserouten, Reiseführer oder Bordkarten versenden. Mit openURL-Aktionen können Kund:innen schnell auf Buchungsänderungen oder Realtime Updates (wie z.B. Zeitplanänderungen) zugreifen, ohne das Messaging-Fenster zu verlassen, und so eine reibungslose und ansprechende Reise von Anfang bis Ende ermöglichen. |
| Kundenmeinungen und interaktive Umfragen | Erfassen Sie verwertbares Feedback durch interaktive Umfragen, die eine Mischung aus Rich-Media-Inhalten und Text verwenden. Integrieren Sie Antwortvorschläge für schnelle Antworten und openURL-Aktionen, um auf umfassendere Umfrageformulare zuzugreifen. So können Kunden ganz einfach ihre Meinung mitteilen und Marketer können ihre Strategien auf der Grundlage von Echtzeit-Feedback aus allen Branchen verfeinern. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anforderungen

| Anforderung | Beschreibung |
| --- | --- |
| Credits für Nachrichten | Wenden Sie sich an Ihren Braze-Konto Manager:in, um zu bestätigen, dass Sie Nachrichten-Credits in Ihrem Vertrag erworben haben. Message Credits ist ein flexibler Artikel, mit dem Sie Messaging-Volumen über verschiedene Kanäle wie SMS, MMS, RCS und WhatsApp kaufen und zuweisen können. |
| Förderfähiges Land | Stellen Sie sicher, dass Sie RCS an Nutzer:innen in einem der von Braze unterstützten Länder senden: Vereinigte Staaten, Vereinigtes Königreich, Deutschland, Mexiko, Schweden, Spanien, Singapur, Brasilien, Frankreich, Italien, Kolumbien |
| RCS überprüfter Sender | Der Sender, den der Empfänger auf seinem Gerät sieht, um zu erkennen, woher die Nachricht kommt. Ein RCS-verifizierter Sender besteht aus einem Firmennamen, einem visuellen Branding und einem überprüften Badge. <br><br> Braze hilft Ihnen bei der Beantragung und Registrierung eines RCS-verifizierten Senders in den in Frage kommenden Regionen. Sie müssen Ihrer Vertretung von Braze einige grundlegende Informationen zur Verfügung stellen. |
| Liste der Benutzer mit Telefonnummern | Bevor Sie mit dem Versenden von Nachrichten beginnen können, müssen Sie Benutzer zu Ihrem Konto hinzufügen. Außerdem müssen Sie die ungefähre Größe Ihrer Zielgruppe kennen. Nutzer:innen und Telefonnummern können auf verschiedene Weise zu Braze hinzugefügt werden. Telefonnummern müssen als 10-stellige Nummer formatiert sein und eine Landesvorwahl enthalten. Weitere Informationen finden Sie unter [Nutzer:innen Telefonnummern]({{site.baseurl}}/user_phone_numbers/). |
| Schlüsselwörter und Antworten | Allen Basis-Schlüsselwörtern müssen Antworten attributiert werden, bevor Sie mit dem Messaging beginnen können. Braze verarbeitet Opt-in, Opt-out und Hilfe-Schlüsselwörter automatisch. Anpassungsmöglichkeiten und zusätzliche Keyword-Response-Konfigurationen sind verfügbar. Weitere Informationen finden Sie unter [Opt-in und Opt-out Schlüsselwörter]({{site.baseurl}}/optin_optout/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Begriffe, die Sie kennen sollten

| Begriff | Definition |
|----|----|
| Abo-Gruppe | Eine Gruppe von Nutzer:innen, die einen bestimmten Messaging-Anwendungsfall abonniert haben. Jede Abo-Gruppe ist an einen oder mehrere Marken-"Absender" gebunden, die RCS-überprüfte Absender, SMS-Codes oder beides sein können. Wenn Sie beispielsweise planen, sowohl transaktionale als auch werbliche RCS-Nachrichten zu versenden, könnten Sie in Ihrem Braze-Dashboard zwei Abo-Gruppen mit separaten RCS-verifizierten Sendern einrichten. |
| RCS-verifizierter Sender | Der Absender einer RCS Nachricht oder das, was der Empfänger:in der Nachricht auf seinem Gerät sieht, um zu erkennen, woher die Nachricht kommt. RCS-überprüfte Absender enthalten einen Firmennamen, eine Beschriftung, ein visuelles Branding und ein überprüftes Badge. Nachdem Sie Braze die erforderlichen Informationen zur Registrierung von RCS-Sendern zur Verfügung gestellt haben, kümmern wir uns um die Registrierung und die Einrichtung der Abo-Gruppe. |
| SMS Fallback | Wenn eine Nachricht nicht mit RCS zugestellt werden kann (z. B. mangelnde Unterstützung durch den Netzbetreiber in der Region), versucht Braze dennoch, die Nachricht per SMS zuzustellen, wenn ein SMS-Code in der Abo-Gruppe vorhanden ist. |
| Basic RCS | Reine Textnachrichten mit bis zu 160 Zeichen. Abgerechnet als einzelne Nachricht. <br><br> Diese Kategorie wird nur im globalen Modell verwendet. |
| Einzelne RCS | Reine Textnachrichten, die mehr als 160 Zeichen umfassen **oder** Rich-Elemente wie Buttons oder Medien enthalten. <br><br>Diese Kategorie wird nur im globalen Modell verwendet. |
| Reich | Reine Textnachrichten, mit oder ohne eingeschränkte Vorschläge oder Buttons. Abrechnung pro Segment (160 UTF-8 Bytes). Eine Nachricht mit 161 Zeichen Klartext besteht zum Beispiel aus zwei Segmenten. <br><br> Diese Kategorie wird nur im Modell für die Vereinigten Staaten verwendet. |
| Reiche Medien | Nachrichten, die eine Mediendatei (Bild, Video) oder eine Rich Card enthalten. Wird als einzelne Nachricht abgerechnet, unabhängig von der Länge der Nachricht. <br><br> Diese Kategorie wird nur im Modell für die Vereinigten Staaten verwendet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
