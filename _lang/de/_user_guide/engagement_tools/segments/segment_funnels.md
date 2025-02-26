---
nav_title: Segmente Funnels
article_title: Segmente Funnels
page_order: 3

page_type: reference
tool: Segments
description: "Dieser Referenzartikel erläutert die Verwendung von Braze Segment Funnels, ihre bewährten Praktiken und Anwendungsfälle."
search_rank: 1
---

# Segmente Funnels

> Segmenttrichter eignen sich hervorragend, um Ihre Zielgruppe für einen bestimmten Kampagnenanwendungsfall einzugrenzen, etwas über diese Zielgruppe und ihre Interaktionen zu erfahren und dieses Wissen zu nutzen, um effektive Kampagnen zu planen und zu entwickeln.

Anhand von Segmenttrichtern können Sie sehen, wie sich jeder hinzugefügte Filter auf Ihre Segmentstatistiken auswirkt. Wenn Sie ein Segment erstellen, wird unter jedem Filter eine Zeile mit Daten angezeigt. Diese Daten liefern die folgenden Informationen für Nutzer:innen, die von allen Filtern bis zu diesem Punkt gezielt angesprochen werden:

- Gesamtzahl der angesprochenen Nutzer und der Prozentsatz Ihrer Zielgruppe
- LTV und LTV für zahlende Nutzer  
- Anzahl der Nutzer:innen, die per E-Mail erreichbar sind
- Anzahl der Benutzer, die sich für E-Mail entschieden haben
- Anzahl der Nutzer:innen, die Push aktiviert haben  
- Anzahl der Nutzer, die sich für Push entschieden haben

![][1]

## Bewährte Praktiken

- Durch das Hinzufügen von Filtern, die Ihren Nutzerfluss dokumentieren, können Sie die Punkte erkennen, an denen Nutzer:innen abspringen. Wenn Sie beispielsweise eine App für soziale Netzwerke betreiben und sehen möchten, wo Sie während des Einführungsprozesses Nutzer verlieren, können Sie benutzerdefinierte Datenfilter für die Anmeldung, das Hinzufügen von Freunden und das Senden der ersten Nachricht hinzufügen. Wenn Sie feststellen, dass 85 % der Nutzer:innen sich registrieren und Freunde hinzufügen, aber nur 45 % die erste Nachricht gesendet haben, dann wissen Sie, dass Sie sich darauf konzentrieren sollten, mehr Nachrichten während Ihrer Onboarding- und Marketing-Kampagnen zu senden.

- Mit Segmenttrichtern können Sie den Prozentsatz der Nutzer vergleichen, die verschiedene Aktionen durchführen. Neigen beispielsweise aktive Nutzer oder solche mit hohem LTV [eher dazu, mit Push oder E-Mail zu interagieren][4]? Um das herauszufinden, erstellen Sie ein Segment aktiver Nutzer:innen mit einem oder mehreren Filtern und sehen Sie dann, wie sich die Statistiken ändern, wenn Sie einen Filter für das Opt-in bei Push und einen Filter für das Opt-in bei E-Mail hinzufügen.

- Analysieren Sie, wie sich der LTV ändert, wenn Sie Filter hinzufügen. Haben bei aktiven Nutzer:innen diejenigen, die sich mit Facebook verbinden, oder diejenigen, die sich mit X (früher Twitter) verbinden, einen höheren LTV? Oder ist der LTV deutlich höher für diejenigen, die mit beiden verbunden sind? Wenn Sie beispielsweise feststellen, dass eine Verbindung zu X (früher Twitter) nur einen geringen Einfluss auf den LTV hat, eine Verbindung zu Facebook jedoch einen großen Einfluss, sollten Sie Ihre Marketingkampagnen auf Anreize für Facebook-Verbindungen konzentrieren.

## Anwendungsfälle

### Auswirkungen einer bestimmten Benutzeraktion auf Konversionen {#push-email}

Durch die Analyse der Auswirkungen einer bestimmten Benutzeraktion (z. B. Hinzufügen von Artikeln zu einer Wunschliste) auf eine Konversion (z. B. Einkäufe) können Sie die folgenden Fragen beantworten:

- Fällt die Benutzeraktion mit mehr Käufen zusammen?
- Wie weit verbreitet ist die Benutzeraktion? Sollten Sie Marketingkampagnen erstellen, die zu mehr dieser Aktionen anregen?

Nehmen wir zum Beispiel an, Sie haben eine Gruppe, in der alle Benutzer, die Artikel zu einer Wunschliste hinzugefügt haben, auch einen Kauf getätigt haben. Da nur ein kleiner Prozentsatz der Nutzer Artikel zu einer Wunschliste hinzufügte, könnte diese App dieses Verhalten durch Marketingkampagnen stärker fördern.

![Beispiel eines Segmenttrichters mit den folgenden Filtern: "Diese Apps wurden zuletzt vor weniger als 30 Tagen genutzt", "Artikel wurde zuletzt vor weniger als 30 Tagen auf die Warteliste gesetzt" und "Der letzte Kauf liegt weniger als 30 Tage zurück", um 4.302 Nutzer:innen zu erreichen.][3]

### Messaging-Kanäle vergleichen

Erstellen Sie ein Segment von aktiven Nutzern (oder Nutzern mit gewünschten Eigenschaften) und vergleichen Sie deren Interaktionen mit verschiedenen Interaktionskanälen, wie E-Mail und Push-Benachrichtigungen. Wenn zum Beispiel mehr treue Nutzer:innen Push abonniert haben, sollten Sie mehr Zeit darauf verwenden, aktive Nutzerkampagnen über Push zu versenden. Wenn Sie jedoch feststellen, dass der LTV bei denjenigen, die E-Mails abonniert haben, höher ist, sollten Sie mehr aktive Nutzer dazu auffordern, E-Mails zu abonnieren.

![Segmenttrichter für E-Mail-Beispiel mit den folgenden Filtern: "Letzter Kauf vor weniger als 30 Tagen", "Letzte Nutzung dieser Apps vor weniger als 30 Tagen", "Push aktiviert ist wahr" und "E-Mail-Abo-Status ist Opt-in", um 2.799 Nutzer:innen zu erreichen.][5]

### Push-Opt-ins für iOS oder Android

Dieser Anwendungsfall nutzt den Filter "Push für App aktiviert", um iOS- oder Android-Nutzer anzusprechen, die sich für Push entschieden haben.

![][11]

![][12]

### Vollständig Push-fähige Zielgruppe

Dieser Anwendungsfall nutzt den Filter "Push aktiviert", um Nutzer anzusprechen, die sich für Push entschieden haben.

![][10]

### Globale Kontrollgruppe der Push-aktivierten Zielgruppe

Dieser Anwendungsfall nutzt die Filter "Push aktiviert" und "Zufällige Bucket-Nummer", um Nutzer anzusprechen, die Teil der globalen Kontrollgruppe sind und sich für Push entschieden haben.

![][9]

### Kürzlich gekaufte Produkte

Dieser Anwendungsfall nutzt den Filter "Letzter Kauf", um Nutzer anzusprechen, die vor weniger als 7 Tagen zuletzt einen Kauf getätigt haben.

![][8]

### Push-Engagement

Dieser Anwendungsfall nutzt den Filter "Letztes angepasstes Event", bei dem das angepasste Event "öffnete jedes Push" lautet, um Nutzer:innen anzusprechen, die in den letzten 21 Tagen ein Push-Engagement gezeigt haben.

![][7]

### In der App ausgegebenes Geld

In diesem Anwendungsfall wird der Filter "Ausgegebenes Geld" genutzt, um Nutzer anzusprechen, die mindestens 1000 Dollar ausgegeben haben.

![][6]


[1]: {% image_buster /assets/img_archive/segment_funnel_example.png %}
[3]: {% image_buster /assets/img_archive/Wish_List_2.png %}
[11]: {% image_buster /assets/img/seg_filter_examples/ios.png %}
[12]: {% image_buster /assets/img/seg_filter_examples/android.png %}
[6]: {% image_buster /assets/img/seg_filter_examples/moneyspent.png %}
[7]: {% image_buster /assets/img/seg_filter_examples/push_engagement.png %}
[8]: {% image_buster /assets/img/seg_filter_examples/recent_purchase.png %}
[9]: {% image_buster /assets/img/seg_filter_examples/global_control.png %}
[10]: {% image_buster /assets/img/seg_filter_examples/both.png %}
[4]: \#push-email
[5]: {% image_buster /assets/img_archive/Wish_List_Email.png %}
