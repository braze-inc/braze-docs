---
nav_title: Liquid Code
article_title: Generierung von Liquid Code mit BrazeAI
description: "In diesem Artikel erfahren Sie, wie der AI Liquid Assistant funktioniert und wie Sie ihn nutzen können, um Liquid-Snippets für Ihre Nachrichten zu erstellen."
page_type: reference
page_order: 0.0
---

# Generierung von Liquid Code mit <sup>BrazeAITM</sup>

> Der <sup>BrazeAITM</sup> Liquid Assistant ist ein von <sup>BrazeAITM</sup> betriebener Chat-Assistent, der Ihnen hilft, das Liquid zu erzeugen, das Sie für die Personalisierung von Nachrichteninhalten benötigen.

## Über den <sup>BrazeAITM</sup> Liquid-Assistenten

Der BrazeAI<sup>TM</sup> Liquid Assistant wurde entwickelt, um Ihnen beim Schreiben von effektivem Liquid-Code zu helfen, der auf Ihre Marketingbedürfnisse zugeschnitten ist. Unsere KI ist sowohl auf die Syntax von Liquid als auch auf die Art und Weise, wie Vermarkter Liquid in ihren Nachrichten verwenden, geschult und versteht die Feinheiten der Erstellung personalisierter Inhalte.

Indem Sie dem <sup>BrazeAITM</sup> Liquid Assistant Ihre angepassten Attribute (z.B. “favourite_color”) ) und Datentypen (z.B. Boolean und String) zur Verfügung stellen, stellt unser <sup>BrazeAITM</sup> Liquid Assistant außerdem sicher, dass Ihre Nachrichten genau auf Ihre Ziele ausgerichtet sind und Targeting betreiben. Wenn Sie außerdem Markenrichtlinien erstellen, kann der <sup>BrazeAITM</sup> Liquid Assistant die Markenrichtlinien verwenden, um die generierten Ausgaben besser zu personalisieren und den Inhalt an unsere eigene Markensprache anzupassen. Die von Ihnen erstellten Markenrichtlinien werden nur zur Personalisierung von Inhalten für Ihren eigenen Gebrauch verwendet.

## Unterstützte Kanäle

Sie können bei der Erstellung den BrazeAI<sup>TM</sup> Liquid Assistant verwenden: 
- SMS-Nachrichten
- Push-Benachrichtigungen
- HTML-E-Mail-Nachrichten
- Canvase

{% alert note %}
Der Assistent arbeitet mit E-Mail Nachrichten und nicht mit Templates. Es funktioniert am besten mit Nachrichten, die bereits erstellt sind.
{% endalert %}

## Liquid-Code generieren

Um den BrazeAI<sup>TM</sup> Liquid Assistant zu starten, wählen Sie das KI-Assistenten-Symbol im Nachrichten-Editor.

![Nachrichten-Editor mit dem KI-Assistenten.]({% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}){: style="max-width:50%;"}

Sie können einen der mitgelieferten Prompts auswählen oder Ihre eigenen in das Textfeld eingeben.

{% tabs local %}
{% tab use app activity %}
Die Aufforderung zur **Verwendung der App-Aktivität** generiert einen Flüssigkeitscode, mit dem Sie verschiedene Nachrichten senden können, je nachdem, wann Ihre App zuletzt verwendet wurde. Möglicherweise werden Ihnen auch Anschlussfragen gestellt, damit der Assistent ein besseres Ergebnis ermitteln kann.

![Beispiel für die Ausgabe der Aufforderung "App-Aktivität verwenden".]({% image_buster /assets/img/ai_liquid/use_app_activity.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab add countdown %}
Dieser Prompt generiert Liquid-Code, der eine Nachricht mit der verbleibenden Zeitspanne bis zum Ereignis versendet. Sie werden aufgefordert, Angaben zu Datum und Uhrzeit des Ereignisses zu machen.

![Beispiel für die Ausgabe der Aufforderung "Countdown hinzufügen".]({% image_buster /assets/img/ai_liquid/add_countdown.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab inspire me %}
Diese Eingabeaufforderung erscheint, wenn Ihr Nachrichtenfeld einen Inhalt enthält. Nun wird eine Liste mit Optionen generiert, mit denen Sie Ihre Nachricht mit Liquid personalisieren können. 

![Beispiel für die Ausgabe der Eingabeaufforderung "Inspire me".]({% image_buster /assets/img/ai_liquid/inspire_me.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab improve my liquid %}
Diese Eingabeaufforderung erscheint, wenn Ihr Nachrichten-Editor Inhalt enthält. Wählen Sie diese Option, wenn Sie möchten, dass der Assistent Ihren Code effizienter und leichter zu lesen macht.

![Beispiel für die Ausgabe der Aufforderung "Verbessern Sie mein Liquid".]({% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}){: style="max-width:45%;"}
{% endtab %}
{% endtabs %}

Um Ihren Liquid-Code zu generieren, wählen Sie **Editor aktualisieren**.

![KI-Assistenten-Fenster mit bereitgestellten Eingabeaufforderungen.]({% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}){: style="max-width:50%;"}
 
Sie können eine weitere Nachricht mit demselben Prompt erstellen, indem Sie auf **Neu generieren** gehen. Um die Nachricht zu entfernen und zur vorherigen Nachricht zurückzukehren, wählen Sie **Aktualisierung rückgängig machen**.

## Liquid Attribute {#supported-attributes}

Die folgenden Attribute befinden sich derzeit im Beta-Stadium für den <sup>BrazeAITM</sup> Liquid Assistant:

| Kriterium | Wissenstyp |
| - | - |
| Liquid (inkl. `for` Loops, `if` Anweisungen, Mathematik etc.) | Programmieren |
| Standard-Benutzerattribute | Attribute |
| Benutzerdefinierte Attribute, die einen dieser Datentypen haben: {::nomarkdown}<ul><li>Boolesche Werte</li><li>Zahlen</li><li>Strings</li><li>Arrays</li><li>Uhrzeit</li></ul>{:/} | Attribute |
| Connected-Content | Programmieren |
{: .reset-td-br-1 .reset-td-br-2 }

## Bewährte Praktiken

Wenn Sie Hilfe beim Schreiben effektiver Prompts für den <sup>BrazeAITM</sup> Liquid Assistant benötigen, lesen Sie unsere Best Practices:

### Natürliche Sprache verwenden

Der <sup>BrazeAITM</sup> Liquid Assistant ist darauf trainiert, natürliche Sprache zu verstehen. Sprechen Sie mit ihm wie mit einem Kollegen, wenn Sie um Hilfe bitten. Das macht es dem Assistenten leichter, Ihre Bedürfnisse zu verstehen und präzise Hilfe zu leisten.

### Kontext geben

Die Bereitstellung von Kontext hilft dem BrazeAI<sup>TM</sup> Liquid Assistant, das Gesamtbild Ihres Projekts zu verstehen. Es ist hilfreich, den Kontext mit einzubeziehen, z. B:

- Ihr Firmenname und Ihre Branche
- Eine Kampagne, an der Sie gerade arbeiten, wie z.B. der Schwarze Freitag oder der Weihnachtsverkauf
- Ihr Ziel, z. B. die Erhöhung Ihrer Click-through-Rate
- Spezifische benutzerdefinierte Attribute, die Sie in Ihre Nachricht aufnehmen möchten

Wenn Sie den Kontext in Ihre Eingabeaufforderung aufnehmen, kann der Assistent seine Antworten besser auf Ihre Bedürfnisse abstimmen. Sie können auch Details aus Ihrer Kampagne, Ihrem Nachrichtenbrief oder Ihrem Brainstorming-Dokument einfügen, um den Assistenten auf den neuesten Stand zu bringen.

### Konkret sein

Der <sup>BrazeAITM</sup> Liquid Assistant kann Folgefragen stellen, aber die Angabe von Details im Vorfeld kann schneller zu präziseren Ergebnissen führen. Erwägen Sie Details wie z. B.:

- Alle bekannten Präferenzen oder Anforderungen an die Nachricht
- Anweisungen für den Umgang mit Situationen, wie z. B. fehlende Antworten der Empfängerin oder des Empfängers der Nachricht oder Fallback-Nachrichtenoptionen
- Wenn Sie nach Liquid fragen, das Connected-Content verwendet, erhalten Sie eine Dokumentation für den API-Endpunkt, eine Beispiel-API-Antwort oder beides

### Kreativ werden

Denken Sie bei Ihren Prompts über den Tellerrand hinaus und sehen Sie, wie der BrazeAI<sup>TM</sup> Liquid Assistant Ihr Messaging verbessern kann. Experimentieren Sie mit verschiedenen Aufforderungen und Ideen, denn Kreativität kann zu engagierteren Ergebnissen führen.

## Beispiel-Eingabeaufforderungen

Hier finden Sie einige Beispiele, die Ihnen den Einstieg erleichtern:

{% tabs local %}
{% tab gaining knowledge %}
- Was ist Liquid und wie kann es mir helfen, die Personalisierung meiner Marketingkampagnen in Braze zu verbessern?
- Welche Arten von Daten kann ich in Liquid verwenden, um meine Nachrichten im Marketing zu personalisieren, z. B. demografische Informationen oder frühere Einkäufe?
{% endtab %}

{% tab personalizing dynamic content %}
- Erstellen Sie eine Nachricht, die je nach Treuestatus meines Kunden unterschiedliche Inhalte anzeigt. Wenn wir nichts über ihren Treuestatus wissen, senden Sie eine Fallback-Nachricht.
- Schreiben Sie eine dynamische Nachricht, die das Lieblingsprodukt eines Benutzers und das Datum seines letzten Kaufs enthält. Wenn es keinen letzten Kauf gibt, brechen Sie die Nachricht ab.
- Schreiben Sie mir Liquid, um jemanden zu ermutigen, auf meine Nachricht zu klicken, die einen Countdown enthält, der angibt, wie viel Zeit noch bleibt. Wenn das Angebot abgelaufen ist, brechen Sie die Nachricht ab.
- Helfen Sie mir, eine Nachricht zu verfassen, die Benutzer ermutigt, zur Kasse zu gehen, wenn sie noch Artikel in ihrem Warenkorb haben.
- Schreiben Sie Liquid, um eine Nachricht auf der Grundlage des Landes einer Kundin oder eines Kunden zu personalisieren. Ich möchte die Nachricht mit dem Namen des Landes ausfüllen. Wenn wir keinen von beiden haben, schlagen Sie ihnen vor, auf einen Link zu klicken, um ihr Profil zu aktualisieren.
- Wie kann ich eine Begrüßungsnachricht mit dem Vornamen eines Benutzers personalisieren und je nach Geschlecht des Benutzers unterschiedliche Texte verfassen?
- Schreiben Sie Liquid, um verschiedene Nachrichten basierend auf einem angepassten Attribut, “CUSTOM_ATTRIBUTE_NAME“ und dessen Wert anzuzeigen. Es gibt sechs verschiedene Optionen, die ich senden könnte. Wenn es keinen Wert für das angepasste Attribut gibt, möchte ich eine Nachricht mit einem Platzhalter senden.
{% endtab %}

{% tab handling outliers %}
- Können Sie mir einige Beispiele dafür nennen, wie Liquid in Marketingkampagnen eingesetzt wird, um das Engagement und die Konversionsraten zu erhöhen?
- Welche Anwendungsfälle gibt es für Liquid in SMS-Nachrichten für den Sommerschlussverkauf, z. B. Erinnerungen an einen Warenkorb-Abbruch oder personalisierte Aktionen?
{% endtab %}
{% endtabs %}

{% alert tip %}
Lassen Sie uns wissen, ob Sie interessante Anregungen oder Erfahrungen gemacht haben, indem Sie eine [Feedback-Sitzung](https://research.rallyuxr.com/braze/schedule/clxxhw8em0d071ak4b279553s?channel=share) mit uns buchen.
{% endalert %}

{% multi_lang_include brazeai/generative_ai/policy.md %}
