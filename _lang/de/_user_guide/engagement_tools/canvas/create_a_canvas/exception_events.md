---
nav_title: Ausnahme-Events 
article_title: Ausnahme-Events
page_order: 4
page_type: reference
description: "Dieser Referenzartikel beschreibt Ausnahmeereignisse und wie sie sich auf Ihre Canvas-Komponenten auswirken."
tool: Canvas

---

# Canvas-Ausnahmeereignisse

{% alert important %}
Ab dem 28\. Februar 2023 können Sie keine Canvase mehr mit dem Original-Editor erstellen oder duplizieren. Diesen Artikel können Sie referenzieren, wenn Sie Ausnahme-Events für den ursprünglichen Canvas-Workflow einrichten. <br><br> Braze empfiehlt Kund:innen, die die ursprüngliche Canvas-Umgebung nutzen, den Wechsel zu Canvas Flow. Es handelt sich um eine verbesserte Bearbeitungsfunktion, mit der Sie Canvases besser erstellen und verwalten können. Erfahren Sie mehr über das [Klonen Ihrer Canvases in Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

> Wenn Sie mit dem Original-Canvas-Editor einen Zeitplan für eine Komponente für ein Canvas erstellen, haben Sie die Möglichkeit, ein Ausnahme-Event einzurichten. Sie können ein Ausnahme-Event zu einer Komponente hinzufügen, solange die Zielgruppe nicht sofort vorangebracht wird. Nutzer:innen, die das Ausnahme-Event durchführen, werden nicht [durch den Schritt][2] vorangebracht und scheiden aus Ihrer Canvas-Zielgruppe aus.

Ausnahme-Events triggern nur, während ein:e Nutzer:in auf die zugehörige Canvas-Komponente wartet. Wenn ein:e Nutzer:in die gleiche Aktion in einem früheren Canvas-Schritt durchführt, wird das Ausnahme-Event nicht getriggert.

{% alert important %}
Für Canvas Flow werden Ausnahmeereignisse nur über [Aktionspfade]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) konfiguriert. Sie können zum Beispiel einen Aktionspfad definieren und den Pfad Jeder Andere als Ausnahme verwenden.
{% endalert %}

Ausnahme-Events für einen aktionsbasierten Schritt funktionieren während der Schrittverzögerung oder des Fensters. Geplante Schritte haben kein Zeitfenster, und daher funktioniert das Ausnahme-Event nur, wenn es während der Verzögerung eintritt.

Wenn Sie beispielsweise ein Ausnahme-Event für "Warenkorb-Abbruch" im dritten Schritt Ihres Canvas haben, ein:e Nutzer:in aber seinen Warenkorb abbricht, während er sich im zweiten Schritt befindet, wird das Ausnahme-Event nicht getriggert. In diesem Beispiel wird das Ausnahmeereignis nur dann ausgelöst, wenn der Benutzer seinen Warenkorb im dritten Schritt Ihres Canvas verlässt. 

![][1]


[1]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/
