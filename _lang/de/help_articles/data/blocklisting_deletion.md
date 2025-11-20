---
nav_title: Unterschied zwischen Blocklisting und Löschung
article_title: Unterschied zwischen Blocklisting und Löschung
page_order: 2

page_type: solution
description: "Dieser Hilfe-Artikel erklärt Ihnen den Unterschied zwischen der Sperrung von Attributen und der Löschung."
---

# Unterschied zwischen Blocklisting und Löschen

Um den Unterschied zwischen dem Blockieren und dem Löschen von Attributen in Braze zu verstehen, lassen Sie uns die Ergebnisse der beiden Aktionen betrachten:

- Wird auf Sperrliste gesetzt ... Wenn angepasste Attribute, Events oder Käufe auf der Blockliste stehen, verbleiben sie im Nutzerprofil, aber es werden keine neuen Anfragen für das Attribut bearbeitet.
- **Löschung:** Wenn angepasste Attribute, Events oder Käufe gelöscht werden, werden auch die Daten entfernt. Braze akzeptiert jedoch weiterhin neue eingehende Anfragen für dieses Attribut, wenn es noch über das SDK getrackt oder über API oder CSV hochgeladen wird.

## Was soll ich tun?

Um die Blocklistung zu erreichen, muss Braze die Informationen zur Blocklistung an die Geräte der Nutzer:innen senden. Dies ist ein datenintensiver Vorgang, den wir idealerweise vermeiden möchten. Wenn die Liste zu umfangreich ist (> 100 Attribute, Ereignisse oder Käufe), kann Ihre App außerdem langsamer werden. 

Wenn Sie nicht mehr vorhaben, Attribute an Braze zu senden, empfiehlt sich der Weg der Löschung.

Unabhängig von Ihrer Route werden die angepassten Attribute, Events und Käufe, die Sie entfernen möchten, nicht mehr auf der Seite **Workspace verwalten** angezeigt, wodurch sie als Filter für Segmente entfernt werden. Die Daten auf Nutzerebene bleiben auf den Profilen erhalten. 