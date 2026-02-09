---
nav_title: "Feature für angepasste App-Symbole (iOS)"
article_title: Benutzerdefinierte App-Symbol-Funktion
page_order: 7
page_type: reference
description: "Dieser Referenzartikel behandelt das iOS 10.3-Update für anpassbare App-Symbole."
platform: iOS
channel:
  - push

---

# Funktion für benutzerdefinierte App-Symbole (iOS 10.3) 

> Mit iOS 10.3 führte Apple die Möglichkeit ein, das Symbol einer App auf dem Startbildschirm zu ändern, ohne die Anwendung im Apple App Store aktualisieren zu müssen. Der oder die Entwickler:in kann dem oder der Nutzer:in jetzt erlauben, das Startbildschirmsymbol innerhalb seiner oder ihrer App zu ändern. Apple verlangt, dass alle App-Symbole, die der Entwickler dem Benutzer zur Verfügung stellen möchte, in der Binärdatei enthalten sind, die bei der Veröffentlichung der App im Apple App Store an Apple zur Überprüfung übermittelt wird.

Um Ihre Benutzer über diese Funktion zu informieren, können Sie eine In-App-Nachricht oder eine Push-Benachrichtigung über Braze an den Benutzer senden, in der Sie diese Funktion erklären oder den Benutzer fragen, ob er sein Symbol ändern möchte. Der Entwickler müsste lediglich einen Deep Link in der Anwendung erstellen, über den die native iOS-Eingabeaufforderung angezeigt werden kann, um das Symbol zu ändern. Dies ähnelt den Anleitungen, die wir heute für die Einrichtung einer Einführung in Push-Benachrichtigungen für APNs bereitstellen.

Darüber hinaus kann diese Art der Nachrichtenübermittlung die Vorteile der Segmentierung voll ausschöpfen, um den Text der Nachricht für den Nutzer in hohem Maße kontextbezogen zu gestalten. Sie können auch A/B-Tests von Nachrichten durchführen, um zu sehen, welche Nachricht den größten Einfluss auf das gewünschte Ergebnis hat.
