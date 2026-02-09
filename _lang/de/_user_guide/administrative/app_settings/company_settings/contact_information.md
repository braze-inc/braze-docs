---
nav_title: Kontaktinformationen
article_title: Kontaktinformationen
page_order: 0
page_type: reference
description: "Dieser Referenzartikel enthält wichtige Informationen für Administratoren zur Verwaltung der Kontaktinformationen Ihres Unternehmens und der Zeitzone in Braze."

---

# Kontaktinformationen

<style>
.fa-crown {
  color: gold;
}
</style>

> Diese Seite enthält wichtige Informationen für Administratoren zur Verwaltung der Kontaktinformationen und der Zeitzone Ihres Unternehmens in Braze.

Um auf diese Seite zuzugreifen, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Kontaktinformationen**.

Auf dieser Seite können Sie die Kontaktinformationen und die Zeitzone Ihres Unternehmens verwalten. Stellen Sie sicher, dass Sie **Speichern** auswählen, bevor Sie die Seite verlassen!

## Folgen der Umstellung Ihrer Zeitzone

{% alert warning %}

Der Wechsel der Zeitzone kann zu Unstimmigkeiten bei den Daten rund um den Zeitpunkt des Wechsels der Zeitzone führen. Wenn jemand seine Zeitzone wechselt, bemühen wir uns nach bestem Wissen und Gewissen um eine genaue Umrechnung, aber es ist nicht immer eine perfekte Umrechnung. Möglicherweise stellen Sie eine Diskontinuität in Ihren Daten fest, bei der zwischen Zeitzonen gewechselt wird.

{% endalert %}

Wenn Sie sich entscheiden, Ihre Zeitzone zu wechseln, kann dies eine Reihe von Konsequenzen haben:

- Während Kampagnen, die für bestimmte Zeiten an bestimmten Orten geplant sind (z.B. 21 Uhr Ostküstenzeit), bis zur Bearbeitung ordnungsgemäß nach Plan laufen, sind sowohl die Kampagnenanalysen als auch zukünftige Kampagnenpläne von der Änderung betroffen.
- Jede Kartenplanung, die nicht der Ortszeit zugeordnet ist, kann davon betroffen sein, wobei aktive Karten möglicherweise als beendet angezeigt werden oder umgekehrt.
- Bei Segmentierungsfiltern der Form "Hat X vor/nach `Date` getan" wird die Zeit angepasst, da das Anfangsdatum nun in Pazifischer Zeit lokalisiert wird.