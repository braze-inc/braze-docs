---
nav_title: Kontext 
article_title: Kontext 
alias: /context/
page_order: 1.5
page_type: reference
description: "Dieser referenzierte Artikel beschreibt, wie Sie Kontext-Schritte in Ihrem Canvas erstellen und verwenden."
tool: Canvas

---

# Kontext

> Verwenden Sie Kontext-Schritte, um eine Reihe von Variablen zu erstellen oder zu aktualisieren, die den Kontext eines Nutzers:innen (oder Insights über das Verhalten dieses Nutzers) darstellen, während er sich durch ein Canvas bewegt. Jede Kontextvariable enthält einen Namen, einen Datentyp und einen Wert, der Liquid enthalten kann. Indem Sie den Kontext als Teil Ihrer User Journey festlegen, können Sie z.B. Nachrichten verzögern oder Nutzer:innen anhand von Kontextvariablen filtern.

{% alert important %}
Context Steps befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Konto Manager:in, wenn Sie an der Teilnahme an diesem frühen Zugang interessiert sind.
{% endalert %}

## Funktionsweise

Jeder Canvas-Schritt besteht aus einem Variablennamen und einem zugehörigen Datentyp, den sogenannten Context-Variablen (früher als Canvas-Eingangs-Eigenschaften bezeichnet). Diese Variablen folgen einem Nutzer:innen durch ein Canvas und können über das Liquid `context` aufgerufen werden.

![Ein Context-Schritt als erster Schritt eines Canvas.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Es gibt zwei Möglichkeiten, Kontextvariablen zu setzen:

- **Am Eingang von Canvas:** Variablen von Ereignissen oder API-Aufrufen, die den Eingang eines Nutzers:innen in ein Canvas triggern, werden als Kontextvariable gespeichert.
- **Einen Kontext-Schritt verwenden:** Sie können Kontextvariablen im Schritt-Editor erstellen oder aktualisieren.

Beachten Sie, dass alle Variablen, die in der Kontextvariable enthalten sind, nicht automatisch im Nutzerprofil gespeichert werden.

## Erstellen eines Kontextschritts

Um einen Context-Schritt zu erstellen, fügen Sie Ihrem Canvas einen Schritt hinzu. Ziehen Sie dann die Komponente per Drag-and-Drop aus der Seitenleiste oder wählen Sie den <i class="fas fa-plus-circle"></i> plus Button am unteren Rand eines Schritts und wählen Sie **Kontext**.

### Definieren von Kontextvariablen

1. Geben Sie Ihrer Context-Variable einen Namen.
2. Wählen Sie einen Datentyp aus.
3. Geben Sie einen Liquid-Ausdruck ein oder wählen Sie den Button **Personalisierung hinzufügen**. Dies erzeugt ein Liquid Snippet zur Verwendung in Ihrem Liquid-Ausdruck.
4. Wählen Sie **Vorschau**, um die Kontextvariable anzuzeigen.
5. Wählen Sie **Fertig**, um den Schritt zu speichern.

Sie können Kontextvariablen überall dort verwenden, wo Sie Liquid einsetzen können, z.B. in den Schritten Nachrichten und Nutzer:innen Update, mit dem Button **Personalisierung hinzufügen**.

## Typen von Kontextvariablen

Canvas-Kontextvariablen, die in dem Schritt erstellt oder aktualisiert werden, können Typen zugewiesen werden. Beachten Sie, dass die Kontextvariable nicht aktualisiert wird, wenn der Liquid-Ausdruck zur Laufzeit einen Wert liefert, der nicht dem Typ entspricht.

Wenn zum Beispiel der Datentyp der Kontextvariablen auf **Datum** eingestellt ist, der Wert aber kein Datum ist, wird die Variable nicht aktualisiert. Dies bedeutet, dass Folgendes geschieht:

- Der Nutzer:innen bringt entweder den nächsten Schritt voran oder verlässt den Canvas, wenn es der letzte Schritt im Canvas ist.
- In den Analytics Ihres Canvas-Schritts wird dies als *Nicht aktualisiert* gezählt.

Braze beendet einen Nutzer:innen bei diesem Schritt, wenn:

- Die Kontextvariable gibt keinen Wert zurück.
- Ein Aufruf eines eingebetteten Connected-Content schlägt fehl.
- Die Typen der Kontextvariablen stimmen nicht überein.

### JSON-Typen und Connected-Content-Antworten

Braze wertet Kontextvariablen, von denen erwartet wird, dass sie vom Typ JSON (oder Object) sind, aus Connected-Content-Antworten in Strings aus. Um zu verhindern, dass Kontextvariablen als Strings ausgewertet werden, geben Sie diese Ergebnisse in diesen Liquid-Filter ein: `as_json_string`. Ein Beispiel ist:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Verwendung von Kontextvariablen mit Verzögerungsschritten

Sie können [personalisierte Verzögerungsoptionen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) mit den Informationen aus dem Schritt Kontext hinzufügen, d.h. Sie können die Variable auswählen, die Nutzer:innen verzögert.

[1]: {% image_buster /assets/img/context_step3.png %}
