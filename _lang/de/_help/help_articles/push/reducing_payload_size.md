---
nav_title: Größe der Nutzlast von Push-Benachrichtigungen reduzieren
article_title: Größe der Nutzlast von Push-Benachrichtigungen reduzieren
page_type: solution
description: "In diesem Hilfeartikel finden Sie einige Tipps, wie Sie die Größe der Nutzlast Ihrer Push-Benachrichtigungen reduzieren können, wenn Sie eine Kampagne oder einen Canvas-Schritt aufgrund von Größenbeschränkungen der Push-Nutzlast nicht starten können."
channel: push
---

# Verkleinerung der Nutzlast von Push-Benachrichtigungen

Wenn Sie eine Push-Kampagne oder einen Canvas-Schritt nicht starten können, weil Ihre Push-Nutzlast zu groß ist, lesen Sie diese Tipps zur Reduzierung der Nutzlast Ihrer Push-Benachrichtigungen.

{% alert note %}
Unsere maximale Nutzdatengröße beträgt **3.807 Bytes**. Wenn Ihr Push diese Größe überschreitet, kann die Nachricht möglicherweise nicht gesendet werden. Am besten beschränken Sie Ihre Nutzdaten auf einige hundert Bytes.
{% endalert %}

## Was ist eine Push-Nutzlast?

Die Anbieter von Push-Diensten berechnen, ob Ihre Push-Benachrichtigung einem Benutzer angezeigt werden kann, indem sie die Bytegröße der gesamten Push-Nutzlast betrachten. Die Nutzlast ist bei den meisten Push-Diensten auf **4 KB (4.096 Byte** ) begrenzt, einschließlich:

- Apple Push-Benachrichtigungsdienst (APNs)
- Firebase Cloud Messaging (FCM) von Android
- Web-Push
- Huawei Druck

Diese Push-Dienste lehnen jede Benachrichtigung ab, die dieses Limit überschreitet.

Braze reserviert einen Teil der Push-Nutzlast für Integrations- und Analysezwecke. Die maximale Größe der Nutzdaten beträgt daher **3.807 Bytes**. Wenn Ihr Push diese Größe überschreitet, kann die Nachricht möglicherweise nicht gesendet werden. Am besten beschränken Sie Ihre Nutzdaten auf einige hundert Bytes.

Die folgenden Elemente in Ihrer Push-Nachricht bilden Ihre Push-Nutzlast:

- Texte, wie z.B. den Titel und den Nachrichtentext
- Endgültiges Rendering der Flüssigkeits-Personalisierung
- URLs für Bilder (aber nicht die Größe des Bildes selbst)
- URLs für Klickziele
- Tasten-Namen
- Schlüssel-Wert-Paare

## Tipps zur Reduzierung der Nutzlast

Um die Größe der Nutzlast zu reduzieren:

- Halten Sie Ihre Nachricht kurz. Ein guter allgemeiner Leitfaden ist, dass Sie weniger als 40 Zeichen verwenden sollten, um einen Nutzen zu erzielen.
- Lassen Sie Leerzeichen und Zeilenumbrüche in Ihrer Kopie weg.
- Überlegen Sie, wie Liquid beim Senden gerendert wird. Da die endgültige Darstellung einer Liquid-Personalisierung von Benutzer zu Benutzer unterschiedlich ist, kann Braze nicht feststellen, ob eine Push-Nutzlast die Größenbeschränkung überschreitet, wenn Liquid eingebunden wird. Wenn Ihr Liquid eine kürzere Nachricht wiedergibt, könnte das kein Problem sein. Wenn Ihr Liquid jedoch zu einer längeren Nachricht führt, kann es sein, dass Ihr Push die zulässige Größe der Nutzlast überschreitet. Testen Sie Ihre Push-Nachricht immer auf einem echten Gerät, bevor Sie sie an die Benutzer senden.
- Erwägen Sie die Verkürzung von URLs mit einem URL-Verkürzer.
