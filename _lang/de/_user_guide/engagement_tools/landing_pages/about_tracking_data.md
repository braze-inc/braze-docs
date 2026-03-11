---
nav_title: Über das Tracking von Daten
article_title: Daten zum Tracking der Zielseite
description: "Erfahren Sie mehr über Tracking und anonymisierte Daten für Landing Pages in Braze."
page_order: 10
alias: /landing_pages/data_tracking/
---

# Daten zum Tracking der Zielseite

> Erfahren Sie mehr über Tracking und anonymisierte Daten für Landing Pages in Braze.

## Trackingmethoden

### Web SDK

Das Braze-Internet-SDK wird initialisiert, wenn eine Nutzer:in ein Formular auf einer Landing Page absendet. Vorher werden keine persönlichen Daten gesammelt und das SDK verfolgt die Benutzer nicht aktiv. Nach der Initialisierung speichert das SDK keine Daten im Browser (wie Cookies, lokale Speicherinhalte o. Ä.). 

Das Braze-Web-SDK wird sofort initialisiert, wenn ein Nutzer:in über einen Link, der durch ein{% raw %}`{% landing_page_url %}`{% endraw %}Liquid-Tag in einer Braze-Nachricht generiert wurde, zur Landing Page navigiert.

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

Braze führt keine automatische Zusammenführung von Nutzer:innen anhand von Attributen wie E-Mail-Adresse oder Telefonnummer durch, wenn ein Formular auf einer Landing Page übermittelt wird. Wenn ein Formular mit einer E-Mail-Adresse oder Telefonnummer eingereicht wird, die mit einem bestehenden Nutzerprofil übereinstimmt, erstellt Braze ein separates Nutzerprofil.

Um doppelte Nutzerprofile zusammenzuführen, haben Sie folgende Möglichkeiten:

- Triggern Sie den[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)[Endpunkt,]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) wenn ein Formular auf der Landing Page übermittelt wird, um das neue Profil mit einem bestehenden Profil zusammenzuführen.
- Erstellen Sie einen Zeitplan für[ eine Massenzusammenführung,]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging) um doppelte Profile regelmäßig anhand übereinstimmender Bezeichner zusammenzuführen.

