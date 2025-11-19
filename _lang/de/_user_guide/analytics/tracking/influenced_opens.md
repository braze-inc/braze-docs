---
nav_title: Beeinflusst öffnet
article_title: Beeinflusste Öffnungen
page_order: 7
page_type: reference
description: "Dieser referenzierte Artikel erklärt, wie Sie Öffnungen beeinflussen und tracken können, um Ihre Push-Kampagnen mit mehr Details zu versehen."
channel: push

---

# Beeinflusst öffnet

> Wenn ein Nutzer:innen eine Push-Benachrichtigung auswählt und zu Ihrer App geschickt wird, protokolliert Braze dies als direkte Öffnung. Wenn Nutzer:innen die Push-Benachrichtigung nicht auswählen, aber dennoch von ihr beeinflusst werden können, protokolliert Braze dies als eine beeinflusste Öffnung. Dadurch erhalten Sie einen detaillierteren Einblick in die Wirkung Ihrer Push-Kampagnen.

## Funktionsweise

Beeinflusste Öffnungen messen die Anzahl der Nutzer:innen, die die App nach dem Erhalt einer Benachrichtigung öffnen, ohne die Benachrichtigung auszuwählen. Da es keine direkte Aktion gibt, die die Benachrichtigung mit der Öffnung der App verbindet, wird eine beeinflusste Öffnung protokolliert, wenn der Nutzer:innen die App weniger als dreißig Minuten nach Erhalt der Push-Benachrichtigung oder weniger als die Hälfte der durchschnittlichen Zeit seit der letzten Sitzung dieses Nutzers öffnet.

Nehmen wir an, Sie senden eine Push-Benachrichtigung an die Nutzer:innen Ihrer App. Wenn ein Nutzer:innen, der die App normalerweise 30 Mal am Tag öffnet, Ihre App sechs Stunden nach Erhalt des Push öffnet, hat der Push wenig bis gar keinen Einfluss auf die Öffnung. Wenn jedoch ein Nutzer:innen, der die App normalerweise einmal im Monat nutzt, die App sechs Stunden nach Erhalt des Push öffnet, ist die Chance, dass die Öffnung als beeinflusstes Öffnen gezählt wird, wesentlich größer. 

Dies unterscheidet sich von der Einstellung der Öffnung einer App als Konversions-Event für eine Push-Kampagne. Bei Konversionen werden alle Öffnungen innerhalb des Konversionsfensters der Kampagne zugeschrieben. Beeinflusste Öffnungen legen ein Zeitfenster und eine Attribution-Gutschrift auf der Grundlage des Verhaltens eines einzelnen Nutzers:innen fest.

## Das Anzeigen der Einflüsse einer Kampagne öffnet

Beeinflusste Öffnungen werden zu den direkten Öffnungen einer Kampagne addiert, um die Gesamtzahl der Öffnungen zu ermitteln. Dies wird auf der Seite **Campaign Analytics** einer Push-Kampagne angezeigt. Die Gesamtzahl der Öffnungen und die direkten Öffnungen werden in den Abschnitten Performance der Nachrichten und **Historische Performance** angezeigt. Beeinflusste Öffnungen sind der Unterschied zwischen den beiden Maßnahmen.

![Beeinflusst öffnet die Statistiken auf der Seite Kampagnendetails für eine Kampagne]({% image_buster /assets/img_archive/Influenced_Opens2.png %})

Weitere Informationen zum Tracking von Öffnungen finden Sie im Abschnitt über das Konversions-Tracking in unseren [Best Practices für Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

