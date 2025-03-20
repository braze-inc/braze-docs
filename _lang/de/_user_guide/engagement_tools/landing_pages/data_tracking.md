---
nav_title: Datenverfolgung
article_title: Datenverfolgung
description: "Dieser Artikel behandelt die Daten, die auf Landing Pages verfolgt werden."
page_order: 3
alias: /landing_pages/data_tracking/
---

# Datenverfolgung

> Braze-Startseiten verwenden eine Version des Braze Web SDK, um Benutzerdaten nur dann zu verfolgen, wenn ein Startseitenformular abgeschickt wird. Daten wie Seitenaufrufe und die Schaltflächenklicks, die nicht mit einem bestimmten Benutzer verknüpft sind, werden ohne das Web-SDK gesammelt.<br><br>Diese Seite erläutert Web-SDK- und anonymisierte Daten, die auf Startseiten verfolgt werden.

## Trackingmethoden

### Web SDK

Das Braze Web SDK wird nur initialisiert, wenn jemand ein Formular auf der Startseite abschickt. Vorher werden keine persönlichen Daten gesammelt und das SDK verfolgt die Benutzer nicht aktiv. Nach der Initialisierung speichert das SDK keine Daten im Browser (wie Cookies, lokale Speicherinhalte o. Ä.).

Wenn ein Formular abgeschickt wird, erfasst das SDK die folgenden Daten:

- Ereignis der Formularübermittlung (Ereignisname und Übermittlungszeitpunkt)
- Von Ihrem Team im Formular angegebene Daten (wie Name, E-Mail und Telefonnummer)
- Sitzungsbeginn
- Geräte-ID (eine eindeutige ID, die für das Gerät generiert, aber nicht gespeichert wird)
- Land bestimmt durch IP-Adresse

### Anonymisierte Daten

Bevor ein Benutzer ein Formular absendet, bestehen die auf einer Landing Page verfolgten Daten nur aus anonymisierten, nicht identifizierbaren Informationen. Es handelt sich dabei um standardmäßige aggregierte Website-Kennzahlen wie die Anzahl der Seitenaufrufe (Impressionen) und Klicks, die eine Landing Page erhält.

Da diese Daten nicht mit identifizierbaren Nutzern verknüpft sind, können sie nicht zum Retargeting oder zur Verfolgung des individuellen Nutzerverhaltens verwendet werden.

