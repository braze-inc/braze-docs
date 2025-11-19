---
nav_title: Inhalt QA
article_title: Content-Qualitätssicherung mit KI
page_order: 4
description: "In diesem Referenzartikel erfahren Sie, wie Sie mit KI direkt aus dem Nachrichten-Editor eine Qualitätssicherung für Ihre Nachrichteninhalte durchführen können."
---

# Inhalts-Qualitätssicherung mit <sup>BrazeAITM</sup>

> Lernen Sie, wie Sie Ihre Inhalte mit <sup>BrazeAITM</sup> überprüfen können, damit Sie Rechtschreib- und Grammatikfehler, einen unangemessenen Tonfall oder eine beleidigende Sprache erkennen können, bevor Sie auf Senden drücken.

## Unterstützte Funktionen

Die folgenden Features werden unterstützt, um die Qualität Ihrer Inhalte zu verbessern:

| Feature                     | Beschreibung |
|----------------------------|-------------|
| Rechtschreib- und Grammatikprüfung | Prüft automatisch auf Rechtschreib- und Grammatikfehler in Ihrer Nachricht. Es schlägt Korrekturen vor und gibt Empfehlungen zur Verbesserung der Gesamtgenauigkeit des Inhalts. |
| Ton-Analyse              | Bewertet den Ton der Nachricht, um mögliche Probleme zu erkennen. So können Sie sicherstellen, dass der beabsichtigte Ton mit dem gewünschten Kommunikationsstil übereinstimmt und Missverständnisse oder unbeabsichtigte Beleidigungen vermieden werden. |
| Erkennung anstößiger Sprache | Scannt Ihre Nachricht auf potenziell beleidigende oder unangemessene Sprache. So können Sie Ihren Inhalt überarbeiten und eine respektvolle Kommunikation aufrechterhalten. |
| Versehentliche Inhaltskontrolle   | Erkennt alle Einfügungen von Code, Markup-Sprache oder Nachrichten, die möglicherweise unbeabsichtigt hinzugefügt wurden, einschließlich Liquid-Code, der für einen Testnutzer:in nicht gerendert wurde. |
| Unterstützung mehrerer Sprachen     | Obwohl nicht offiziell von OpenAI unterstützt, kann GPT [mehrere Sprachen](https://openai.com/research/gpt-4#:~:text=GPT%2D4%203%2Dshot%20accuracy%20on%20MMLU%20across%20languages) verstehen. Denken Sie daran, dass Braze keine Informationen über die Sprache oder das Gebietsschema Ihrer Kopie weitergibt, wenn diese an OpenAI gesendet wird. Daher können Ihre Ergebnisse je nach Sprache, in der Sie schreiben, variieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Verwendung von <sup>BrazeAITM</sup> zur Qualitätssicherung von Inhalten

{% alert note %}
Dieses Feature ist zur Zeit nur für SMS, Android Push, iOS Push und traditionelle In-App-Nachrichten verfügbar.
{% endalert %}

1. Nachdem Sie eine mobile Push-, SMS- oder herkömmliche In-App-Nachricht verfasst haben, navigieren Sie zum Tab **Test**.
2. Suchen Sie den Abschnitt **Inhalts-Qualitätssicherung mit KI**.
3. Klicken Sie auf **Inhalt testen**.

\![Content QA mit KI Abschnitt des Tabs Test.]({% image_buster /assets/img/content_qa_ai.png %})

## Bewährte Praktiken

Beachten Sie die folgenden Punkte, damit Sie das Beste aus Content QA mit KI machen können:

- **Lesen Sie Ihre Nachricht Korrektur:** Obwohl der Content Checker bei der Identifizierung von Fehlern helfen kann, ist es dennoch unerlässlich, Ihre Inhalte manuell zu korrigieren. Verlassen Sie sich auf die von der KI generierten Vorschläge als hilfreiche Orientierungshilfe, aber nutzen Sie Ihr Urteilsvermögen, um die Genauigkeit sicherzustellen.
- **Verstehen Sie die Tonanalyse:** Die Ergebnisse der Tonanalyse sind subjektiv und basieren auf dem Verständnis des KI-Modells. Sie können zwar nützliche Erkenntnisse liefern, aber Sie sollten Ihren beabsichtigten Tonfall und den Kontext des Gesprächs berücksichtigen, um entsprechende Anpassungen vorzunehmen.
- **Überprüfen Sie die markierte anstößige Sprache:** Die Erkennung beleidigender Sprache ist so konzipiert, dass sie robust ist, aber es kann gelegentlich zu falsch positiven Ergebnissen kommen. Überprüfen Sie die markierten Abschnitte sorgfältig und nehmen Sie bei Bedarf entsprechende Änderungen vor.

{% multi_lang_include brazeai/generative_ai/policy.md %}
