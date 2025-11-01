---
nav_title: Umgang mit unbekannten Telefonnummern
article_title: Umgang mit unbekannten Telefonnummern
page_order: 4
description: "Dieser referenzierte Artikel beschreibt, wie Braze unbekannte Telefonnummern von neuen Nutzer:innen verarbeitet."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
  
---

# Umgang mit unbekannten Rufnummern - neue Benutzer

> Nachdem Sie SMS, MMS und RCS mit Braze zum Laufen gebracht haben, werden Sie möglicherweise Nachrichten von unbekannten Nutzer:innen erhalten. Die folgenden Schritte beschreiben, wie ein:e nicht identifizierte:r Nutzer:in und eine Nummer verarbeitet werden.

## Opt-in/out und benutzerdefinierter Schlüsselwort-Workflow für unbekannte Nummern

Braze adressiert eine unbekannte Nummer automatisch auf eine von drei Arten:

1. Wenn ein Opt-in-Schlüsselwort eingegeben wird:
  * Braze erstellt ein anonymes Profil
  * Unser System legt das Telefon-Attribut fest
  * Abonniert die:den Nutzer:in die entsprechende Abo-Gruppe, je nachdem, welches Opt-in-Schlüsselwort von Braze empfangen wurde.<br><br>
2. Wenn ein Opt-out-Schlüsselwort eingegeben wird:
  * Braze erstellt ein anonymes Profil
  * Unser System legt das Telefon-Attribut fest
  * Meldet die:den Nutzer:in der entsprechenden Abo-Gruppe ab, je nachdem, welches Opt-out-Schlüsselwort von Braze empfangen wurde.<br><br>
3. Wenn ein anderes benutzerdefiniertes Schlüsselwort eingegeben wird:
  * Braze ignoriert die Textnachricht und tut nichts.

