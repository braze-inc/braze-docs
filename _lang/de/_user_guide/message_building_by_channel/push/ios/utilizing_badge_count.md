---
nav_title: Badge-Zählung verwenden
article_title: Badge-Zählung verwenden
page_order: 8

page_type: reference
description: "Dieser Artikel behandelt die Verwendung der iOS-Badge-Zählung, um Benutzer, die eine Push-Benachrichtigung nicht bemerkt haben oder die Push-Benachrichtigungen im Vordergrund deaktiviert haben, wieder zu aktivieren."
platform: iOS
channel: 
- push
- in-app messages

---

# Badge-Zählung verwenden

> Die iOS-Badge-Anzeige zeigt die Anzahl der ungelesenen Benachrichtigungen innerhalb Ihrer Anwendung in Form eines roten Kreises in der oberen rechten Ecke des App-Symbols an. In den letzten Jahren hat sich Badge als effektives Mittel zur erneuten Interaktion mit Nutzer:innen von Apps erwiesen.

Die Anzahl der Abzeichen kann verwendet werden, um Ihre Nutzer, die eine Push-Benachrichtigung nicht bemerkt haben oder die Push-Benachrichtigungen im Vordergrund deaktiviert haben, wieder einzubinden. Ebenso können Sie Ihre Nutzer über ungesehene Nachrichten wie In-App-Updates benachrichtigen.

## Abzeichen zählen mit Braze

Sie können die gewünschte Anzahl der Badges angeben, wenn Sie eine Push-Benachrichtigung über das Braze-Dashboard verfassen. Dies kann auf ein Attribut der Nutzerin oder des Nutzers mit personalisiertem Messaging gesetzt werden, was eine endlos anpassbare Logik erlaubt. Wenn Sie eine stille Push-Mitteilung senden möchten, die die Anzahl der Ausweise aktualisiert, ohne den Benutzer zu stören, fügen Sie die Markierung "Content-Available" zu Ihrer Push-Mitteilung hinzu und lassen Sie den Inhalt der Nachricht leer.

{% alert note %}
Sie fragen sich, wie Sie die Anzahl der Badges für Android festlegen können? Android verarbeitet das App-Badging für Push automatisch, daher gibt es in Braze keine angepassten Einstellungen für das Badging.
{% endalert %}

### Entfernen der Badge-Zählung

Setzen Sie die Anzahl der Abzeichen auf 0 oder "", um die Anzahl der Abzeichen aus dem Symbol der App zu entfernen. Braze löscht das Badge auch automatisch, wenn eine Push-Benachrichtigung empfangen wird, während die App im Vordergrund ist.

## Bewährte Praktiken

Um die leistungsstarke erneute Interaktion durch Badging Badges zu optimieren, ist es wichtig, dass Sie Ihre Badge-Einstellungen so konfigurieren, dass sie für die Nutzer:innen möglichst einfach sind.

### Halten Sie die Anzahl der Abzeichen niedrig
Untersuchungen haben ergeben, dass die Benutzer nach einer zweistelligen Anzahl von Badges das Interesse an den Updates verlieren und die App oft ganz aufgeben.

> Je nach Art Ihrer App kann es Ausnahmen von dieser Regel geben (z. B. E-Mail- und Gruppennachrichten-Apps).

### Begrenzen Sie die Anzahl der Dinge, die eine Badge-Zählung repräsentieren kann
Wenn Sie Badging verwenden, sollten Sie die Benachrichtigungen so klar und direkt wie möglich gestalten. Indem Sie die Anzahl der Dinge begrenzen, die eine Badge-Benachrichtigung darstellen kann, können Sie Ihren Benutzern ein Gefühl der Vertrautheit mit den Funktionen und Updates Ihrer App vermitteln.

