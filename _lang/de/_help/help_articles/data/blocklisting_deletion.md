---
nav_title: Unterschied zwischen Blocklisting und Löschung
article_title: Unterschied zwischen Blocklisting und Löschung
page_order: 2

page_type: solution
description: "In diesem Hilfeartikel erfahren Sie mehr über den Unterschied zwischen der Sperrung von Attributen und der Löschung."
---

# Unterschied zwischen Blocklisting und Löschen

Um den Unterschied zwischen dem Blockieren und dem Löschen von Attributen in Braze zu verstehen, lassen Sie uns die Ergebnisse der beiden Aktionen betrachten:

- **Blocklisting:** Wenn benutzerdefinierte Attribute, Ereignisse oder Käufe auf der Blockliste stehen, bleiben sie im Benutzerprofil, aber es werden keine neuen Anfragen für das Attribut bearbeitet.
- **Löschung:** Wenn benutzerdefinierte Attribute, Ereignisse oder Käufe gelöscht werden, werden auch die Daten entfernt. Braze wird jedoch weiterhin neue eingehende Anfragen für dieses Attribut akzeptieren, wenn es noch über das SDK verfolgt oder über API oder CSV hochgeladen wird.

## Was soll ich tun?

Um die Blocklistung zu erreichen, muss Braze die Informationen zur Blocklistung an jedes Gerät des Benutzers senden. Das ist ein datenintensiver Vorgang, den wir idealerweise vermeiden möchten. Wenn die Liste zu umfangreich ist (mehr als 100 Attribute, Ereignisse oder Käufe), kann Ihre App außerdem langsamer werden. 

Wenn Sie nicht mehr vorhaben, Attribute an Braze zu senden, ist der Weg des Löschens der empfohlene Weg.

Unabhängig von Ihrer Route werden die benutzerdefinierten Attribute, Ereignisse und Käufe, die Sie entfernen möchten, nicht mehr auf der Seite **Arbeitsbereich verwalten** angezeigt, wodurch sie als Segmentfilter entfernt werden. Die Daten auf Benutzerebene bleiben in den Profilen erhalten. 