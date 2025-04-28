---
nav_title: Content-Qualitätssicherung mit KI
article_title: Content-Qualitätssicherung mit KI
page_order: 10
description: "In diesem Referenzartikel erfahren Sie, wie Sie mit KI direkt aus dem Nachrichten-Editor eine Qualitätssicherung für Ihre Nachrichteninhalte durchführen können."
---

# Content-Qualitätssicherung mit KI

> Erfahren Sie, wie Sie mit KI direkt aus dem Nachrichten-Editor heraus eine Qualitätssicherung für Ihre Nachrichteninhalte durchführen können.

Content-QA mit KI nutzt die Fähigkeiten von GPT und OpenAI, um den Inhalt Ihrer Nachrichten zu überprüfen und sicherzustellen, dass er den Qualitätsstandards entspricht, indem ineffektive Elemente wie Rechtschreibfehler, Grammatikprobleme, unangemessener Ton und beleidigende Sprache identifiziert werden. Sie können auf diese Funktion über die Registerkarte **Test** zugreifen, wenn Sie eine Push-, SMS- oder In-App-Nachricht in einer Kampagne oder einem Canvas verfassen.

## Wichtigste Features

Content-QA mit KI bietet die folgenden wichtigen Features zur Verbesserung der Qualität Ihrer Nachrichteninhalte:

- **Rechtschreib- und Grammatikprüfung:** Prüft automatisch auf Rechtschreib- und Grammatikfehler in Ihrer Nachricht. Es schlägt Korrekturen vor und gibt Empfehlungen zur Verbesserung der Gesamtgenauigkeit des Inhalts.
- **Ton-Analyse:** Bewertet den Ton der Nachricht, um mögliche Probleme zu erkennen. So können Sie sicherstellen, dass der beabsichtigte Ton mit dem gewünschten Kommunikationsstil übereinstimmt und Missverständnisse oder unbeabsichtigte Beleidigungen vermieden werden.
- **Erkennung anstößiger Sprache:** Scannt Ihre Nachricht auf potenziell beleidigende oder unangemessene Sprache. So können Sie Ihren Inhalt überarbeiten und eine respektvolle Kommunikation aufrechterhalten.
- **Versehentliche Inhaltskontrolle:** Erkennt alle Einfügungen von Code, Markup-Sprache oder Nachrichten, die möglicherweise unbeabsichtigt hinzugefügt wurden, einschließlich Liquid-Code, der für einen Testnutzer:in nicht gerendert wurde.

## Zugriff auf Content-QA mit KI

{% alert note %}
Content-QA mit KI ist zur Zeit nur für Push- und SMS-Kanäle verfügbar.
{% endalert %}

Um auf die Inhaltsprüfung zuzugreifen, gehen Sie folgendermaßen vor:

1. Nachdem Sie eine Push- oder SMS-Nachricht verfasst haben, navigieren Sie zur Registerkarte **Test**.
2. Suchen Sie den Abschnitt **Inhalts-Qualitätssicherung mit KI**.
3. Klicken Sie auf **Inhalt testen**.

![Content-QA mit KI auf dem Tab Test.][1]{: style="max-width:60%"}

### Unterstützung von Sprachen

GPT ist in der Lage, [mehrere Sprachen](https://openai.com/research/gpt-4#:~:text=GPT%2D4%203%2Dshot%20accuracy%20on%20MMLU%20across%20languages) zu verstehen, obwohl OpenAI diese offiziell nicht unterstützt. Braze gibt keine zusätzlichen Informationen über die Sprache oder das Gebietsschema Ihrer Kopie weiter, wenn der Inhalt der Nachricht an OpenAI gesendet wird, daher ist es Aufgabe von GPT, diese Entscheidung zu treffen.

Die Ergebnisse können je nach der Sprache, in der Sie schreiben, variieren.

## Tipps für eine effektive Nutzung

Beachten Sie die folgenden Tipps, um das Feature Content-QA mit KI optimal zu nutzen:

- **Lesen Sie Ihre Nachricht Korrektur:** Obwohl der Content Checker bei der Identifizierung von Fehlern helfen kann, ist es dennoch unerlässlich, Ihre Inhalte manuell zu korrigieren. Verlassen Sie sich auf die von der KI generierten Vorschläge als hilfreiche Orientierungshilfe, aber nutzen Sie Ihr Urteilsvermögen, um die Genauigkeit sicherzustellen.
- **Verstehen Sie die Tonanalyse:** Die Ergebnisse der Tonanalyse sind subjektiv und basieren auf dem Verständnis des KI-Modells. Sie können zwar nützliche Erkenntnisse liefern, aber Sie sollten Ihren beabsichtigten Tonfall und den Kontext des Gesprächs berücksichtigen, um entsprechende Anpassungen vorzunehmen.
- **Überprüfen Sie die markierte anstößige Sprache:** Die Erkennung beleidigender Sprache ist so konzipiert, dass sie robust ist, aber es kann gelegentlich zu falsch positiven Ergebnissen kommen. Überprüfen Sie die markierten Abschnitte sorgfältig und nehmen Sie bei Bedarf entsprechende Änderungen vor.

## Wie werden meine Daten verwendet und an OpenAI gesendet?

Um den Inhalt Ihrer Nachrichten zu überprüfen, sendet Braze diese an die API-Plattform von OpenAI. Alle Abfragen, die von Braze an OpenAI gesendet werden, sind anonymisiert. Das bedeutet, dass OpenAI nicht in der Lage ist, festzustellen, von wem die Abfrage gesendet wurde, es sei denn, Sie fügen eindeutig identifizierbare Informationen in den von Ihnen bereitgestellten Nachrichteninhalt ein. Wie in den [API Platform Commitments von OpenAI](https://openai.com/policies/api-data-usage-policies) beschrieben, werden Daten, die über Braze an die API von OpenAI gesendet werden, nicht zum Trainieren oder Verbessern ihrer Modelle verwendet und nach 30 Tagen gelöscht. Bitte stellen Sie sicher, dass Sie die für Sie relevanten Richtlinien von OpenAI einhalten, die unter anderem die [Nutzungsrichtlinie](https://openai.com/policies/usage-policies) und der [Richtlinie zur gemeinsamen Nutzung und Veröffentlichung](https://openai.com/policies/sharing-publication-policy) umfassen können. Braze übernimmt keinerlei Garantie in Bezug auf KI-generierte Inhalte.

[1]: {% image_buster /assets/img/content_qa_ai.png %}
