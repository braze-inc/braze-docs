---
nav_title: Event-Benennungskonventionen
article_title: Event-Benennungskonventionen
page_order: 10
page_type: reference
description: "Dieser Referenzartikel behandelt die korrekten Konventionen für die Benennung von Events und die besten Praktiken."

---

# Event-Benennungskonventionen

> Wenn Sie bei der Integration von Braze die Konsistenz Ihrer Event- und Attribut-Taxonomie sicherstellen, bleiben Ihre Daten sauber und für neue und bestehende Nutzer:innen der Braze-Plattform nutzbar. So vermeiden Sie spätere Probleme, die eine Kampagne an die falsche Zielgruppe triggern oder zu Diskrepanzen bei den Ergebnissen führen können, weil Sie das falsche Event verwenden.

## Bewährte Praktiken

- Halten Sie Ihre Namenskonvention klar.
- Verwenden Sie eine einheitliche Schreibweise und Formatierung von Event-Namen.
- Vermeiden Sie es, Events ähnliche Namen zu geben.
- Vermeiden Sie lange Strings für die Attribute von Events, die im Braze-Dashboard abgeschnitten oder gekürzt werden.

## Konventionen zur Namensgebung

### Event-Gruppen verwenden

Verwenden Sie Gruppen zur Unterscheidung von Teilen Ihres Produkts, um Events zu benennen. Indem Sie Ihr Produkt in Gruppen einteilen, kann jeder Nutzer:innen klar verstehen, worauf sich das Ereignis bezieht und was es bewirkt.

### Struktur der Event-Benennung

Die häufigste Namensstruktur ist `group_noun_action`. Events sollten alle klein geschrieben werden, um Fehler bei der Instrumentierung und der Identifizierung von Eigenschaften zu vermeiden.

### Eigenschaften

Markieren Sie ein Event und identifizieren Sie dann Unterschiede anhand von Eigenschaften. Dies ist hilfreich bei Events, die an sich gleich sind, aber kleine Unterschiede aufweisen, wie z. B. Kanäle für eine Kampagne. Wir können auch leicht sehen, wie Nutzer:innen durch die Events fließen. Im [Objekt Event-Eigenschaften]({{site.baseurl}}/api/objects_filters/event_object/#event-properties-object) finden Sie ein Beispiel und zusätzlichen Kontext.
