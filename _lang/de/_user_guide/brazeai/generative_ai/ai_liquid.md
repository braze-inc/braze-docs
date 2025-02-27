---
nav_title: BrazeAI Flüssiger Assistent
article_title: BrazeAI Flüssiger Assistent
description: "In diesem Artikel erfahren Sie, wie der AI Liquid Assistant funktioniert und wie Sie ihn nutzen können, um Liquid-Snippets für Ihre Nachrichten zu erstellen."
page_type: reference
page_order: 5
---

# <sup>BrazeAITM</sup> Flüssiger Assistent

> Der <sup>BrazeAITM</sup> Liquid Assistant ist ein von <sup>BrazeAITM</sup> betriebener Chat-Assistent, der Ihnen hilft, das Liquid zu erzeugen, das Sie für die Personalisierung von Nachrichteninhalten benötigen.

Mit dem <sup>BrazeAITM</sup> Liquid Assistant können Sie Liquid aus Vorlagen erstellen, personalisierte Liquid-Vorschläge erhalten und bestehendes Liquid mit Unterstützung von <sup>BrazeAITM</sup> optimieren. Der Assistent liefert auch Anmerkungen, die das verwendete Liquid erklären, damit Sie Ihr Verständnis von Liquid verbessern und lernen, Ihr eigenes zu schreiben.

## Unterstützte Kanäle

Sie können bei der Erstellung den BrazeAI<sup>TM</sup> Liquid Assistant verwenden: 
- SMS-Nachrichten
- Push-Benachrichtigungen
- HTML-E-Mail-Nachrichten
    - Der Assistent arbeitet mit E-Mail-Nachrichten und nicht mit Vorlagen und funktioniert am besten mit E-Mail-Nachrichten, die bereits erstellt sind.
- Canvase

## Funktionsweise

Der BrazeAI<sup>TM</sup> Liquid Assistant wurde entwickelt, um Ihnen beim Schreiben von effektivem Liquid-Code zu helfen, der auf Ihre Marketingbedürfnisse zugeschnitten ist. Unsere KI ist sowohl auf die Syntax von Liquid als auch auf die Art und Weise, wie Vermarkter Liquid in ihren Nachrichten verwenden, geschult und versteht die Feinheiten der Erstellung personalisierter Inhalte. Indem Sie dem <sup>BrazeAITM</sup> Liquid Assistant Ihre benutzerdefinierten Attributnamen (z. B. "Lieblingsfarbe") und Datentypen (z. B. boolesch und string) mitteilen, stellt unser <sup>BrazeAITM</sup> Liquid Assistant außerdem sicher, dass Ihre Nachrichten genau auf Ihre Ziele ausgerichtet sind. Wenn Sie außerdem Markenrichtlinien erstellen, kann der <sup>BrazeAITM</sup> Liquid Assistant die Markenrichtlinien verwenden, um die generierten Ausgaben besser zu personalisieren und den Inhalt an unsere eigene Markensprache anzupassen. Die von Ihnen erstellten Markenrichtlinien werden nur zur Personalisierung von Inhalten für Ihren eigenen Gebrauch verwendet. 

## Liquid-Code generieren

Um den BrazeAI<sup>TM</sup> Liquid Assistant zu starten, wählen Sie das KI-Assistenten-Symbol im Nachrichten-Editor.

![Nachrichtenersteller mit dem KI-Assistenten.][1]{: style="max-width:50%;"}

Sie können eine [vorgegebene Eingabeaufforderung](#provided-prompts) auswählen oder Ihre eigene in das Textfeld eingeben. Um Ihren Liquid-Code zu generieren, wählen Sie **Editor aktualisieren**.

![KI-Assistent-Fenster mit bereitgestellten Eingabeaufforderungen.][2]{: style="max-width:50%;"}
 
Sie können eine weitere Nachricht mit demselben Prompt erstellen, indem Sie auf **Neu generieren** gehen. Um die Nachricht zu entfernen und zur vorherigen Nachricht zurückzukehren, wählen Sie **Aktualisierung rückgängig machen**.

### Bereitgestellte Prompts

Wenn Sie den BrazeAI<sup>TM</sup> Liquid Assistant verwenden, sehen Sie u. U. Hinweise, die Ihnen den Einstieg in Liquid erleichtern. Einige der Eingabeaufforderungen sind unten aufgeführt.

#### App-Aktivität verwenden

Die Aufforderung zur **Verwendung der App-Aktivität** generiert einen Flüssigkeitscode, mit dem Sie verschiedene Nachrichten senden können, je nachdem, wann Ihre App zuletzt verwendet wurde. Möglicherweise werden Ihnen auch Anschlussfragen gestellt, damit der Assistent ein besseres Ergebnis ermitteln kann.

![Beispiel für die Ausgabe der Aufforderung "App-Aktivität verwenden".][3]{: style="max-width:45%;"}

#### Countdown hinzufügen

Dieser Prompt generiert Liquid-Code, der eine Nachricht mit der verbleibenden Zeitspanne bis zum Ereignis versendet. Sie werden aufgefordert, Angaben zu Datum und Uhrzeit des Ereignisses zu machen.

![Beispiel für die Ausgabe der Aufforderung "Countdown hinzufügen".][4]{: style="max-width:45%;"}

#### Etwas Inspiration, bitte.

Diese Eingabeaufforderung erscheint, wenn Ihr Nachrichtenfeld einen Inhalt enthält. Nun wird eine Liste mit Optionen generiert, mit denen Sie Ihre Nachricht mit Liquid personalisieren können. 

![Beispielausgabe für den Prompt "Inspiriere mich".][5]{: style="max-width:45%;"}

#### Liquid optimieren

Diese Eingabeaufforderung erscheint, wenn Ihr Nachrichten-Editor Inhalt enthält. Wählen Sie diese Option, wenn Sie möchten, dass der Assistent Ihren Code effizienter und leichter zu lesen macht.

![Beispielausgabe für den Prompt "Verbesser mein Liquid".][6]{: style="max-width:45%;"}

## Unterstützte Attribute in der Beta-Version

| Kriterium | Wissenstyp |
| - | - |
| Liquid (inkl. `for` Loops, `if` Anweisungen, Mathematik etc.) | Programmieren |
| Standard-Benutzerattribute | Attribute |
| Benutzerdefinierte Attribute, die einen dieser Datentypen haben: {::nomarkdown}<ul><li>Boolesche Werte</li><li>Zahlen</li><li>Strings</li><li>Arrays</li><li>Uhrzeit</li></ul>{:/} | Attribute |
| Connected-Content | Programmieren |
{: .reset-td-br-1 .reset-td-br-2 }

## Wie werden meine Daten verwendet und an OpenAI gesendet?

Um Nachrichteninhalte zu ändern oder zu erstellen, sendet Braze Prompts, Nachrichteninhalte und/oder Markenrichtlinien (sofern vorhanden), die Sie an den KI-Assistenten BrazeAI<sup>TM</sup> übermitteln, an die API-Plattform von OpenAI. Alle Abfragen, die von Braze an OpenAI gesendet werden, sind anonymisiert. Das bedeutet, dass OpenAI nicht in der Lage ist, festzustellen, von wem die Abfrage gesendet wurde, es sei denn, Sie enthalten eindeutig identifizierbare Informationen in den von Ihnen bereitgestellten Inhalten. Wie in der [Verpflichtungserklärung zur API-Plattform von OpenAI](https://openai.com/policies/api-data-usage-policies) dargelegt, werden Daten, die über Braze an die API von OpenAI gesendet werden, nicht für Training oder Verbesserung von dessen Modellen verwendet und nach 30 Tagen gelöscht. Bitte stellen Sie sicher, dass Sie die für Sie relevanten Richtlinien von OpenAI einhalten. Dazu gehören die [Nutzungsrichtlinien](https://openai.com/policies/usage-policies) und die [Richtlinien zur gemeinsamen Nutzung und Veröffentlichung](https://openai.com/policies/sharing-publication-policy). Braze übernimmt keinerlei Garantie in Bezug auf KI-generierte Inhalte.

[1]: {% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}
[2]: {% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}
[3]: {% image_buster /assets/img/ai_liquid/use_app_activity.png %}
[4]: {% image_buster /assets/img/ai_liquid/add_countdown.png %}
[5]: {% image_buster /assets/img/ai_liquid/inspire_me.png %}
[6]: {% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}
