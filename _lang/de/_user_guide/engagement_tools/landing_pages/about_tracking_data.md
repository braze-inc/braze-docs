---
nav_title: Über Tracking Daten
article_title: Daten zum Tracking der Zielseite
description: "Erfahren Sie mehr über Tracking und anonymisierte Daten für Landing Pages in Braze."
page_order: 10
alias: /landing_pages/data_tracking/
---

# Daten zum Tracking der Zielseite

> Erfahren Sie mehr über Tracking und anonymisierte Daten für Landing Pages in Braze.

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

## Zusammenführen von doppelten Nutzerprofilen

Braze führt Nutzer:innen nicht automatisch auf der Grundlage von Attributen wie E-Mail oder Telefon zusammen, wenn ein Landing Page-Formular eingereicht wird. Wenn ein Formular mit einer E-Mail oder Telefonnummer eingereicht wird, die mit einem bestehenden Nutzerprofil übereinstimmt, erstellt Braze ein separates Nutzerprofil.

Um doppelte Nutzerprofile zusammenzuführen, können Sie:

- Triggern Sie den [Endpunkt`/users/merge` ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/), wenn ein Landing Page-Formular übermittelt wird, um das neue Profil mit einem bestehenden Profil zusammenzuführen.
- Planen Sie einen Zeitplan für die [Zusammenführung von]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging) doppelten Profilen auf der Grundlage übereinstimmender Bezeichner.

