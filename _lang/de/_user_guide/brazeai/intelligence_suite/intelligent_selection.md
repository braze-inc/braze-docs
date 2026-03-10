---
nav_title: Intelligente Auswahl
article_title: Intelligente Auswahl
page_order: 1.0
description: "Dieser Artikel beschreibt die Intelligente Auswahl – eine Funktion, die die Performance einer wiederkehrenden Kampagne oder eines Canvas zweimal täglich analysiert und den Prozentsatz der Nutzer, die jede Nachrichtenvariante erhalten, automatisch anpasst."
search_rank: 10
toc_headers: h2
---

# Intelligente Auswahl {#intelligent-selection}

> Die Intelligente Auswahl ist eine Funktion, die die Performance einer wiederkehrenden Kampagne oder eines Canvas zweimal täglich analysiert und den Prozentsatz der Nutzer, die jede Nachrichtenvariante erhalten, automatisch anpasst.

## Über die Intelligente Auswahl

Eine Variante, die besser abzuschneiden scheint, wird an mehr Nutzer gesendet; schwächere Varianten werden an weniger Nutzer gerichtet. Jede Anpassung erfolgt über einen [statistischen Algorithmus](https://en.wikipedia.org/wiki/Multi-armed_bandit), der sicherstellt, dass Braze auf echte Performance-Unterschiede und nicht nur Zufall reagiert.

![A/B-Testing-Bereich einer Kampagne mit aktivierter Intelligenter Auswahl.]({% image_buster /assets/img/intelligent_selection1.png %})

Die Intelligente Auswahl wird:
- wiederholt Performancedaten auswerten und den Kampagnen-Datenverkehr schrittweise in Richtung der Gewinner-Varianten verlagern,
- sicherstellen, dass mehr Nutzer Ihre beste Variante erhalten, ohne die statistische Aussagekraft zu beeinträchtigen,
- schwächere Varianten schneller ausschließen und starke Varianten schneller identifizieren als ein [klassischer A/B-Test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/),
- häufiger testen und mit größerer Sicherheit, dass Ihre Nutzer Ihre beste Nachricht sehen.

Die Intelligente Auswahl eignet sich am besten für Kampagnen, die mehr als einmal senden. Für Einmalsendungen empfehlen wir einen klassischen [A/B-Test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

## Voraussetzungen

Stellen Sie vor dem Hinzufügen der Intelligenten Auswahl zu Ihrer Kampagne Folgendes sicher:

- Die Kampagne wird nach wiederkehrendem Zeitplan gesendet (Einmalsendungen werden nicht unterstützt).
- Es gibt mindestens zwei Nachrichtenvarianten.
- Ein Konversionsereignis zur Messung der Performance über Varianten ist definiert.
- Das Fenster für die erneute Berechtigung beträgt 24 Stunden oder mehr (kürzere Fenster werden nicht unterstützt, da sie die Integrität der Kontrollvariante beeinträchtigen).

Bei einem Canvas: Der Nachrichten-Schritt enthält mindestens zwei Varianten und mindestens ein Konversionsereignis.

Ausführliche Schritte zum Hinzufügen zu Kampagnen und Canvases, Laufzeit, Variantenverteilung und FAQ finden Sie in der vollständigen Version dieses Artikels im linken Inhaltsverzeichnis oder in der Braze-Dashboard-Hilfe.
