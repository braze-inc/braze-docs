---
nav_title: Kontaktinformationen
article_title: Kontaktinformationen
page_order: 0
page_type: reference
description: "Dieser Referenzartikel enthält wichtige Informationen für Administratoren zur Verwaltung der Kontaktinformationen Ihres Unternehmens und der Zeitzone in Braze."

---

# Kontaktinformationen

> Als Administrator können Sie die Seite **„Kontaktinformationen“** verwenden, um die Kontaktinformationen und die Zeitzone Ihres Unternehmens in Braze zu verwalten.

Um auf diese Seite zuzugreifen, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Kontaktinformationen**. Bitte stellen Sie sicher, dass Sie **„Speichern“** auswählen, um alle Änderungen zu übernehmen, bevor Sie die Seite verlassen.

## Folgen der Umstellung Ihrer Zeitzone

{% alert warning %}
Das Wechseln von Zeitzonen kann zu Abweichungen in den Daten im Zeitraum führen, in dem die Zeitzone geändert wurde. Wenn Sie Ihre Zeitzone ändern, bemüht sich Braze nach bestem Wissen und Gewissen, die Konversion korrekt durchzuführen, kann jedoch keine perfekte Konversion garantieren. Möglicherweise stellen Sie eine Diskontinuität in Ihren Daten fest, bei der zwischen Zeitzonen gewechselt wird.
{% endalert %}

Wenn Sie sich entscheiden, Ihre Zeitzone zu wechseln, kann dies eine Reihe von Konsequenzen haben:

- Während Kampagnen, die für bestimmte Zeiten an bestimmten Orten geplant sind (z.B. 21 Uhr Ostküstenzeit), bis zur Bearbeitung ordnungsgemäß nach Plan laufen, sind sowohl die Kampagnenanalysen als auch zukünftige Kampagnenpläne von der Änderung betroffen.
- Jede Kartenplanung, die nicht der Ortszeit zugeordnet ist, kann davon betroffen sein, wobei aktive Karten möglicherweise als beendet angezeigt werden oder umgekehrt.
- Bei Filtern der Segmentierung der Form „Hat X vor/nach `Date`... durchgeführt“ wird die Zeit angepasst, da das ursprüngliche Datum nun in der Standard-Zeitzone Ihres Workspaces (z. B. Pacific Time) lokalisiert wird.
