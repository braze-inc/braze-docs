---
nav_title: Feature-Flags
article_title: Feature-Flags
page_order: 8
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Feature-Flags in Canvas verwendet werden können."
tool: Canvas
local_redirect:
  create-a-feature-flag: '/docs/user_guide/engagement_tools/canvas/canvas_components/feature_flags/#creating-a-feature-flag'
---

# Feature-Flags

> Mit Feature-Flags können Sie experimentieren und Ihre Hypothesen zu neuen Funktionen bestätigen. Marketingexperten können Feature-Flags verwenden, um Ihr Publikum in [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) zu segmentieren und die Auswirkungen der Einführung von Features auf die Konversionen zu verfolgen. Darüber hinaus können Sie mit den [Experimentierpfaden]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) diese Konversionen optimieren, indem Sie verschiedene Botschaften oder Pfade gegeneinander testen und ermitteln, welche am effektivsten ist. Nutzen Sie den Winning Path, wenn Sie Ihr Feature nach und nach einer breiteren Zielgruppe zugänglich machen.

Suchen Sie nach weiteren Informationen über Feature-Flags und wie sie in Braze verwendet werden können? Werfen Sie einen Blick auf unsere Artikel zu [den Feature Flags]({{site.baseurl}}/developer_guide/feature_flags/).

## Erstellen eines Feature-Flags

![Ein Beispiel für einen Feature-Flag-Schritt für das Feature Live Chat Button.]({% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Um eine Feature-Flag Komponente zu erstellen, fügen Sie zunächst einen Schritt zu Ihrem Canvas hinzu. Ziehen Sie die Komponente per Drag & Drop aus der Seitenleiste oder klicken Sie auf die Plus-Schaltfläche <i class="fas fa-plus-circle"></i> am unteren Rand eines Schritts und wählen Sie **Feature Flag**. Als Nächstes wählen Sie das Feature-Flag aus der Dropdown-Liste aus, die alle Feature-Flags enthält, die nicht archiviert sind.

## So funktioniert dieser Schritt

Wenn ein Canvas gestoppt, archiviert oder ein Schritt entfernt wird, erhalten alle Benutzer, die diesen Schritt durchlaufen haben, nicht mehr das Feature-Flag des Schritts und seine Eigenschaften. Für den Benutzer gelten weiterhin der Standardprozentsatz für die Verbreitung und die Zielgruppensegmentierung für dieses Feature-Flag und alle anderen Canvases, die noch aktiv sein könnten.

Eigenschaften in einem Canvas-Schritt können nach dem Start geändert werden, und sogar nachdem ein:e Nutzer:in den Schritt durchlaufen hat. Nutzer:innen erhalten immer eine dynamische Realtime-Version des Feature-Flags anstelle der älteren, zuvor gespeicherten Version.

## Überschreiben von Eigenschaften

Bei der Erstellung eines Feature-Flags legen Sie Standard-Eigenschaften fest. Beim Einrichten eines Funktionskennzeichen-Leinwandschritts können Sie entweder die Standardwerte beibehalten oder die Werte für Benutzer, die diesen Schritt eingeben, überschreiben.

![Ein Feature-Flag "Preference Center" mit "String" als Eigenschaft, "url" als Schlüssel der Eigenschaft und einem Wert.]({% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %}){: style="max-width:90%"}

Gehen Sie zu **Messaging** > **Feature Flags**, um zusätzliche Eigenschaften zu bearbeiten, hinzuzufügen oder zu entfernen.

## Unterschiede zwischen Canvas und Rollout

Canvas und ein Feature-Flag-Rollout (Ziehen des Schiebereglers) können unabhängig voneinander funktionieren. Ein wichtiger Vorbehalt ist, dass der Entry zu einem Canvas-Schritt jede Standard-Rollout-Konfiguration überschreibt. Das heißt, wenn ein:e Nutzer:in nicht für ein Feature-Flag qualifiziert ist, kann ein Canvas-Schritt das Feature für diese:n Nutzer:in aktivieren.

Ähnlich verhält es sich, wenn sich ein Benutzer mit bestimmten Eigenschaften für ein Feature-Flag-Rollout qualifiziert und gleichzeitig den Canvas-Schritt betritt, erhält er alle überschriebenen Werte aus diesem Canvas-Schritt.

