---
nav_title: Bereinigung
article_title: Bereinigung
page_order: 4
description: "Dieser Artikel definiert die Bereinigung und ihren Zweck für E-Mail-Nachrichten in Braze."
channel:
  - email

---

# Informationen zur Bereinigung

> Sanitization ist ein Prozess, der stattfindet, wenn Braze eine bestimmte Art von JavaScript in Ihrer E-Mail-Nachricht erkennt.

## Warum führen wir eine Bereinigung durch?

Der Hauptzweck der Bereinigung besteht darin, zu verhindern, dass böswillige Akteure auf die Sitzungsdaten anderer Braze Dashboard-Nutzer:innen zugreifen. Ohne Bereinigung kann ein böser Akteur mit einfachem Lesezugriff eine E-Mail mit dem CKEditor mit JavaScript erstellen, die die aktuelle Browsersitzung über eine Netzwerkanfrage an einen beliebigen Ort sendet, den der böse Akteur wünscht.

Wenn ein:e anderer Dashboard-Nutzer:in dieses E-Mail-Template öffnet, wird das JavaScript ausgeführt und sendet die Sitzungsdaten des aktuellen Nutzers oder der aktuellen Nutzerin an den oder die böswillige:n Akteur:in.

Die meisten Anbieter von E-Mail-Postfächern verarbeiten übrigens kein JavaScript, so dass diese Maßnahme auch dazu dient, E-Mails von unnötigem Ballast zu befreien und ihre Größe zu verringern. 

## Wie bereinigt Braze Ihre Nachrichten?

Wenn Braze JavaScript erkennt, das ein Sicherheitsrisiko darstellt, werden Sie, bevor Sie auf die Registerkarte **Vorschau und Test** oder den HTML-Editor gehen, um die E-Mail-Nachricht zu betrachten, aufgefordert zu bestätigen, dass Braze das JavaScript aus Ihrer Nachricht entfernen kann, bevor Sie fortfahren.

![]({% image_buster /assets/img/email_sanitization.png %})

## Wann werden Bereinigungen fortgesetzt?

Sowohl im Drag-and-Drop-Editor als auch im HTML-Editor werden die bereinigten Ergebnisse in den folgenden Szenarien zwar bereinigt, aber nicht beibehalten:

* Die E-Mail wird in den folgenden Bereichen wiedergegeben:
    * Abschnitt **Inbox Vision** und Registerkarte **Spam-Test** 
    * Abschnitt **Vorschau & Heatmap** im Bereich **E-Mail-Leistung** 
* Die E-Mail wird in einem Testversand gesendet

Für den Drag-and-Drop-Editor führen wir eine Bereinigung durch und behalten die Bereinigung in der Nachricht bei, wenn der
Der Editor wird geschlossen und die Kampagne wird gespeichert. Für den HTML-Editor führen wir eine Bereinigung durch und behalten die Bereinigung in der Nachricht bei, wenn ein:e Nutzer:in zwischen den Editor-Typen wechselt und die Kampagne gespeichert wird.

In all diesen Fällen wird eine Meldung angezeigt, wenn die Bereinigung den HTML-Code verändert hat. Der oder die Nutzer:in muss dies akzeptieren, bevor die Bereinigung abgeschlossen ist.