---
nav_title: "RCS-Einrichtung"
article_title: RCS-Einrichtung
page_order: 1
alias: /rcs_setup/
description: "Dieser Artikel referenziert die Anforderungen, die Sie erfüllen müssen, um RCS zum Laufen zu bringen."
page_type: reference
channel:
  - RCS
---

# RCS einrichten

> In diesem Artikel erfahren Sie, welche Voraussetzungen Sie erfüllen müssen, um Ihren RCS-Kanal zum Laufen zu bringen.

Die Einrichtung von RCS ist so einfach wie die Einrichtung von SMS. Lesen Sie weiter, um zu erfahren, wie Sie umfangreiche und interaktive Nachrichten versenden können.

## Schritt 1: Erfüllen Sie die Zulassungskriterien

Um für den Versand von RCS mit Braze in Frage zu kommen, muss Ihr Unternehmen im Vorfeld drei Kriterien erfüllen:

1. Ihr aktueller Braze-Vertrag muss Nachrichten-Credits enthalten. 
2. Sie müssen Ihre RCS Nachrichten an eines der folgenden von Braze unterstützten Länder senden:
- Vereinigte Staaten
- Vereinigtes Königreich
- Deutschland
- Mexiko
- Schweden
- Spanien
- Singapur
- Brasilien
- Frankreich
- Italien
- Kolumbien
3. Sie müssen eine $0 RCS SKU(s) in Ihrem Vertrag beschaffen.

## Schritt 2: Registrieren Sie einen RCS-überprüften Absender

Bevor Sie RCS-Nachrichten versenden können, müssen Sie einen RCS-verifizierten Sender registrieren. Dies ist die Darstellung Ihrer Marke, die Nutzer:innen auf ihren mobilen Geräten sehen werden. Sie enthält den Namen Ihrer Marke, das Logo, ein Verifizierungs-Badge und optional einen Slogan. Der RCS-verifizierte Sender stärkt das Vertrauen der Kund:in und bestätigt, dass Ihre Nachrichten von einer authentifizierten Quelle stammen. 

![Ein Beispiel für einen RCS-überprüften Sender in einer RCS Nachricht namens "Cat Failz Cafe".]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

Nachdem Sie die RCS SKU(s) zu Ihrem Bestellformular hinzugefügt haben, wird Braze benachrichtigt und setzt sich mit Ihnen in Verbindung, um Ihnen Informationen zur Registrierung von RCS-Sendern zu geben. Das Format dieser Nachrichten hängt von den Ländern ab, an die Sie RCS Nachrichten senden möchten. 

Wenn Sie Ihre ausgefüllten Formulare an Braze geschickt haben, werden wir den Registrierungsprozess in Ihrem Namen abschließen. 

### Schritt 2.1: SMS Fallbacks für RCS Abo-Gruppen einrichten

Da die Netzabdeckung von Land zu Land unterschiedlich ist und die Hardware- und Softwareunterstützung der Nutzer:innen von Person zu Person variiert, ist SMS Fallback heute eine Schlüsselkomponente für ein erfolgreiches RCS-Programm. Wir empfehlen, ein SMS Fallback einzurichten. Wenn ein Anbieter RCS nicht unterstützt oder das Gerät eines Nutzers keine RCS-Nachrichten empfangen kann, sendet SMS Fallback Ihre Nachricht trotzdem, damit Sie keinen wichtigen Moment mit Ihren Nutzer:innen verpassen.

Wir empfehlen Ihnen dringend, Ihre aktuellen SMS Opt-in-Erfahrungen, Abo-Gruppen und Zielgruppen-Segmentierungen zu überprüfen, bevor Sie Ihre erste RCS Kampagne starten. Bei Bedarf steht Ihnen Ihr Customer-Success-Manager:in mit Rat und Tat zur Seite und hilft Ihnen bei der Einrichtung.

### Zeitplan für die Genehmigung durch das Luftfahrtunternehmen

Die Zeitspanne für die Zulassung eines Luftfahrtunternehmens ist von Land zu Land unterschiedlich und kann auch innerhalb eines Landes variieren. Denken Sie daran, dass der RCS-Markt noch in den Kinderschuhen steckt und dass sich die Prozesse der Anbieter und Aggregatoren schnell weiterentwickeln. In den Vereinigten Staaten schätzt Braze, dass die Genehmigungszeit für einen RCS-überprüften Sender in der Regel zwischen 4 und 6 Wochen liegt, wobei ein Testsender in der Regel innerhalb einer Woche genehmigt wird.

Wenn Ihr RCS-verifizierter Sender genehmigt ist, wird unser Team Ihre Abo-Gruppen nach Bedarf aktualisieren, um zu überprüfen, ob der RCS-Sender darin enthalten ist. 

## Schritt 3: Abo-Gruppen einrichten

RCS wird in der Regel auf zwei Arten verwendet: 
- So upgraden Sie den bestehenden SMS-Verkehr 
- Enablement von neuen Anwendungsfällen, die nur mit den erweiterten Funktionen von RCS möglich sind

Abhängig von Ihrer Integration kann Braze RCS-überprüfte Absender zu Ihren bestehenden SMS-Abo-Gruppen hinzufügen oder neue Abo-Gruppen für Sie einrichten. In jedem Fall wird Ihr Braze Team Sie durch ein nahtloses und gesetzeskonformes Upgraden des SMS-Verkehrs begleiten. Weitere Informationen finden Sie unter [Abo-Gruppen für SMS und RCS]({{site.baseurl}}/sms_rcs_subscription_groups/).

Für neue Anwendungsfälle, die mit SMS nicht möglich sind, sollten Sie die Einrichtung spezieller RCS Abo-Gruppen in Erwägung ziehen, die auf Ihre Programmziele abgestimmt sind.