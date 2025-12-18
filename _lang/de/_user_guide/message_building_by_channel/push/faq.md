---
nav_title: FAQs
article_title: Push-FAQs
page_order: 80
description: "Dieser Artikel behandelt einige der am häufigsten gestellten Fragen, die bei der Einrichtung von Push Kampagnen auftreten."
page_type: FAQ
channel:
  - Push
---

# Häufig gestellte Fragen

> In diesem Artikel finden Sie Antworten auf einige häufig gestellte Fragen zum Push-Kanal.

### Was passiert, wenn sich mehrere Nutzer:innen an einem Gerät anmelden?

Wenn sich ein Nutzer:in von einem Gerät oder einer Website abmeldet, bleibt er per Push erreichbar, bis sich ein anderer Nutzer:in anmeldet. Zu diesem Zeitpunkt wird der Push-Token dem neuen Nutzer:innen neu zugewiesen. Das liegt daran, dass jedes Gerät nur ein aktives Push-Abonnement pro App oder Website haben kann.

Wenn ein Push-Token neu zugewiesen wird, wird die Änderung im **Push-Changelog** des Nutzerprofils angezeigt. Sie finden dies unter dem Tab **Engagement** im Nutzerprofil.

\![Der "Push Changelog" im Abschnitt "Kontakteinstellungen".]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

### Warum hat ein Opt-in Nutzer:innen kein Push-Token?

Dies kann passieren, wenn der Push-Token des Nutzers:innen an eine andere Person weitergegeben wurde, die dasselbe Gerät verwendet.

1. Gehen Sie zum **Push Changelog** im Tab **Engagement** des Profils des betroffenen Nutzers:innen.
2. Suchen Sie nach einer Nachricht, die besagt, dass das Push-Token auf einen anderen Nutzer:innen übertragen wurde.
3. Kopieren Sie den Push-Token und fügen Sie ihn in die Leiste für die Nutzersuche ein. 
4. Wenn das Push-Token noch existiert, werden Sie zu dem Nutzer:in weitergeleitet, der sich zuletzt auf dem Gerät angemeldet hat.

Wenn Sie möchten, dass das Push-Token dem ursprünglichen Nutzer:innen wieder zugewiesen wird:

1. Lassen Sie den ursprünglichen Nutzer:innen sich bei dem Profil mit dem fehlenden Push-Token anmelden.
2. Triggern Sie einen neuen Push-Versand. Dadurch wird das Token zurück auf das Konto übertragen, wenn Push auf dem Gerät noch aktiviert ist.

