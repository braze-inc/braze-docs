---
nav_title: Klonen von Canvase
article_title: Klonen von Canvase
page_order: 3
alias: "/cloning_canvases/"
description: "Dieser Referenzartikel beschreibt, wie Sie ein Canvas aus dem ursprünglichen Canvas-Editor in den Canvas Flow-Workflow klonen."
tool: Canvas
---

# Klonen von Canvase in Canvas Flow

{% alert important %}
Sie können Canvase nicht mehr mit dem ursprünglichen Canvas-Experiment erstellen oder duplizieren. Braze empfiehlt Kunden, die das ursprüngliche Canvas-Erlebnis nutzen, den Wechsel zu Canvas Flow, dem aktuellen Canvas-Erlebnis.
{% endalert %}

> Wenn Sie ein bestehendes Canvas aus dem ursprünglichen Editor haben, können Sie dieses Canvas klonen, um eine Kopie in Canvas Flow zu erstellen. Wenn Sie zum aktuellen Canvas-Workflow wechseln, erhalten Sie Zugriff auf leichtgewichtige [Canvas-Komponenten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), [persistente Eingangs-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) und die [Bearbeitung nach dem Start]({{site.baseurl}}/post-launch_edits). Ihr Original-Canvas wird nicht verändert oder gelöscht.

Um Ihr Canvas zu klonen, gehen Sie wie folgt vor:

1. Rufen Sie das Dashboard von Canvas auf. 
2. Identifizieren Sie das Canvas, von dem Sie eine Kopie erstellen möchten, im Canvas Flow-Workflow. Sie können Canvase mit den Status **Entwurf**, **Aktiv** oder **Angehalten** klonen. 
3. Klicken Sie auf <i class="fas fa-ellipsis-vertical"></i> **Weitere Aktionen** und wählen Sie **In Canvas Flow klonen**.

![]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4\. Geben Sie den Namen Ihres neuen Canvas ein und klicken Sie auf **In Canvas Flow klonen**. 

![]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

Jetzt haben Sie zwei Versionen Ihres Canvas: das ursprüngliche Canvas und die Canvas Flow-Version. Ihr ursprüngliches Canvas hat immer noch seinen ursprünglichen Status, und das geklonte Canvas hat den Status **Entwurf**. Sie können immer noch auf das ursprüngliche Canvas zugreifen, aber Braze empfiehlt, den Canvas-Flow-Workflow zu verwenden, um Ihre Canvases weiter aufzubauen.

Zuvor konnten einige Leinwände mit Verzweigungen nicht geklont werden. Jetzt können Sie Canvase mit Branches klonen. Beachten Sie, dass das Klonen von Canvase mit Branches zu unzusammenhängenden Schritten führen kann. Lösen Sie diese unzusammenhängenden Schritte auf (Schritte, die nicht mit einem vorangehenden Schritt verbunden sind), um sicherzustellen, dass Ihre Canvas-Reise korrekt abgebildet wird.

{% alert note %}
Wenn Sie ein aktives Canvas klonen, sendet Braze die Nutzer:innen weiterhin über das ursprüngliche Canvas. Wir empfehlen, ein Canvas vor dem Klonen zu stoppen, um zu vermeiden, dass doppelte Nachrichten an Nutzer:innen von beiden Canvas gesendet werden.
{% endalert %}

![Canvas Dashboard mit zwei Canvase aufgelistet: V2 Kopie von Canvas V1 und Canvas V1. Die V2-Kopie von Canvas V1 hat ein Symbol, das anzeigt, dass der Canvas Flow-Workflow verwendetk wird.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

Sie haben das Klonen Ihres Canvas in den Canvas Flow-Workflow abgeschlossen. Jetzt können Sie Ihre Canvase in dieser aktualisierten Umgebung weiter gestalten!

## Empfehlungen

Damit bestehende Nutzer:innen ihre Nutzer-Journey fortsetzen können, nachdem Sie Ihr ursprüngliches Canvas in Canvas Flow geklont haben, können Sie Filter zu Ihrem bestehenden Canvas hinzufügen, die verhindern, dass neue Nutzer:innen das neue Canvas aufrufen.

Wenn die erneute Nutzerqualifizierung deaktiviert ist, fügen Sie den Filter „Eingegebene Canvas-Variante“ hinzu. Wenn die erneute Nutzerqualifizierung aktiviert ist, sind dies die möglichen Methoden, die Sie in Betracht ziehen sollten, um sicherzustellen, dass Nutzer:innen nicht zweimal dasselbe Canvas eingeben:
- Aktualisieren Sie das vorhandene Canvas, um ein eindeutiges Tag einzufügen. Fügen Sie für das neue Canvas einen Filter „Letzte empfangene Nachricht von Kampagne oder Canvas mit Tag“ hinzu. Dies verhindert, dass Nutzer:innen den Canvas nach einem bestimmten Entry-Datum (Gesamtzahl der Tage nach dem Senden der letzten Nachricht aus dem ursprünglichen Canvas plus das Konversionsfenster) zweimal öffnen. 
- **Mit der folgenden Methode werden Datenpunkte aufgezeichnet.** Aktualisieren Sie das ursprüngliche Canvas, um einen Braze-to-Braze-Webhook einzubinden, der bei der Eingabe eines angepassten Attributs einen Zeitstempel für das Datum auslöst. Mit diesem Attribut können Sie verhindern, dass Nutzer:innen das neue Canvas nach dem angegebenen Datum aufrufen (Gesamtzahl der Tage nach dem Versand der letzten Nachricht aus dem ursprünglichen Canvas plus das Konversionsfenster).

Bei API-gesteuerten Canvases stimmen Sie sich mit Ihrem Entwicklungsteam ab, um sicherzustellen, dass diese Canvases die neue Canvas-ID verwenden, wenn die neuen Canvases zum Start bereit sind.

Weitere Informationen über die Unterschiede zwischen dem ursprünglichen Canvas-Editor und Canvas Flow finden Sie in den [Canvas-FAQ]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor).


