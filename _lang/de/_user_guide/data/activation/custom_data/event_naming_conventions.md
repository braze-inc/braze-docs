---
nav_title: Konventionen zur Benennung von Ereignissen
article_title: Event-Benennungskonventionen
page_order: 10
page_type: reference
description: "Dieser Artikel referenziert die korrekten Konventionen für die Benennung von Ereignissen und die besten Praktiken."

---

# Konventionen zur Benennung von Ereignissen

> Diese Seite behandelt die korrekte Benennung von Ereignissen und bewährte Verfahren. Wenn Sie die Konsistenz Ihrer Ereignis- und Attribut-Taxonomie wahren, bleiben Ihre Daten sauber und für neue und bestehende Nutzer:innen der Braze-Plattform nutzbar. Dies hilft, spätere Probleme zu vermeiden, z.B. das Triggern einer Kampagne an die falsche Zielgruppe oder die Generierung falscher Ergebnisse nach Verwendung des falschen Ereignisses.

## Bewährte Praktiken

- Halten Sie Ihre Namenskonvention klar.
- Verwenden Sie eine einheitliche Schreibweise und Formatierung von Ereignisnamen.
- Vermeiden Sie es, Veranstaltungen ähnliche Namen zu geben.
- Vermeiden Sie lange Strings für die Attribute von Ereignissen, die im Braze-Dashboard abgeschnitten oder gekürzt werden.

## Konventionen zur Namensgebung

### Ereignisgruppen verwenden

Verwenden Sie Gruppen zur Unterscheidung von Teilen Ihres Produkts, um Ereignisse zu benennen. Indem Sie Ihr Produkt in Gruppen einteilen, kann jeder Nutzer:innen klar verstehen, worauf sich das Ereignis bezieht und was es bewirkt.

### Struktur der Ereignisbenennung

Die häufigste Namensstruktur ist `group_noun_action`. Ereignisse sollten alle klein geschrieben werden, um Fehler bei der Instrumentierung und der Identifizierung von Eigenschaften zu vermeiden.

### Eigenschaften

Markieren Sie ein Ereignis und identifizieren Sie dann Unterschiede anhand von Eigenschaften. Dies ist hilfreich bei Ereignissen, die an sich gleich sind, aber kleine Unterschiede aufweisen, wie z. B. Kanäle für eine Kampagne. Wir können auch leicht sehen, wie Nutzer:innen durch die Ereignisse fließen. Im [Objekt Event-Eigenschaften]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) finden Sie ein Beispiel und zusätzlichen Kontext.

## Beispiele

Nehmen wir an, Sie sind Teil eines E-Commerce-Unternehmens und daran interessiert, zu tracken, wann sich Kunden für Ihre App angemeldet und wann sie Ihren Newsletter abonniert haben. Hier finden Sie Beispiele für wirkungsvolle Veranstaltungsnamen:

- `user_signup`
- `newsletter_subscribed`

Diese beiden Ereignisnamen zeigen deutlich, welches Ereignis sie tracken. Wenn Sie weitere angepasste Events erstellen, sollten Sie darauf achten, dass Ihre Namenskonventionen verständlich sind. Vermeiden Sie beispielsweise die Verwendung von Ereignisnamen wie `signup_event_1`, da dies im Vergleich zu `user_signup` unklar ist und nicht vermittelt, worum es bei dem Ereignis geht.
