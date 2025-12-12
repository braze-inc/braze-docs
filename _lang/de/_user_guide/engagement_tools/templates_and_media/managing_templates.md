---
nav_title: Vorlagen verwalten
article_title: Vorlagen verwalten
page_order: 3

page_type: reference
description: "Dieser Referenzartikel beschreibt, wie Sie Templates im Bereich \"Templates und Medien\" des Braze-Dashboards duplizieren und archivieren können."
tool:
  - Templates
  - Media

---

# Vorlagen verwalten

> Das Archivieren oder Duplizieren von Templates kann helfen, diese besser zu organisieren und zu verwalten. Dieser Referenzartikel beschreibt, wie Sie Vorlagen im Bereich **Vorlagen** des Braze-Dashboards archivieren und duplizieren können.

## Duplizieren von Templates

### Individuelle Vorlage

![Dropdown-Menü mit duplizierter Option.]({% image_buster /assets/img/template_duplicate_cog.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Um eine einzelne Vorlage zu duplizieren, klicken Sie auf das Zahnradsymbol <i class="fas fa-cog"></i> für die einzelne Vorlage und wählen Sie aus dem Dropdown-Menü **Duplizieren**.
<br><br>

{% alert note %}
Für [Inhaltsblockvorlagen]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) wird eine Entwurfskopie erstellt. Für alle anderen Vorlagen wird automatisch ein neues Duplikat erstellt.
{% endalert %}

### Mehrere Vorlagen

{% raw %}

Sie können mehrere Templates duplizieren, indem Sie das Kontrollkästchen neben dem Namen des Templates auswählen. Wählen Sie zunächst die Templates aus und wählen Sie dann **Duplizieren**.

Doppelte Vorlagen können Sie finden, indem Sie die Spalte **Letzte Bearbeitung** sortieren. Neue Vorlagen erhalten standardmäßig den Namen `Copy of ORIGINAL_TEMPLATE_NAME`.

{% endraw %}

![Drei Templates, sortiert nach dem Zeitpunkt, an dem die Templates zuletzt bearbeitet wurden, wobei eine kopierte Template ganz oben in der Liste steht.]({% image_buster /assets/img/duplicate_multiple_template.gif %})

## Vorlagen archivieren

![Erweitertes Einstellungs-Dropdown-Menü, das drei Optionen anzeigt: "Archivieren", "Duplizieren" und "In Workspace kopieren", wobei die Option "Archivieren" hervorgehoben ist.]({% image_buster /assets/img/template_archive_cog.png %}){: style="float:right;max-width:20%;margin-left:15px;"}

Um eine einzelne Vorlage zu archivieren, klicken Sie auf das Einstellungssymbol im Vorlagengitter und wählen Sie **Archivieren**. Wenn eine Template archiviert wird, beachten Sie die folgenden unterschiedlichen Szenarien:

- Aktive Kampagnen verwenden die archivierte Vorlage ohne Unterbrechung weiter.
- Kampagnenentwürfe behalten den Inhalt der archivierten Vorlage bei und können bearbeitet und gestartet werden.
- Um eine archivierte Template zu bearbeiten, müssen Sie sie zunächst entarchivieren. Wenn Sie eine archivierte Template für eine Kampagne verwenden möchten, müssen Sie die Template zunächst entarchivieren.

Um mehrere Vorlagen zu archivieren, aktivieren Sie das Kontrollkästchen neben jeder Vorlage, die Sie archivieren möchten. Nachdem Sie mehrere Templates ausgewählt haben, wählen Sie **Archiv**. Sie finden Ihre archivierten Vorlagen, indem Sie in der Vorlagentabelle unter **Anzeigen** die Option **Archiviert** wählen.

![Saved Drop & Drop E-Mail Templates Abschnitt, der zwei ausgewählte Templates und die Symbolleiste mit der Option zum Archivieren anzeigt.]({% image_buster /assets/img/archive_multiple_template.png %}){: style="max-width:60%;"}

{% alert important %}
Die Archivierung ist derzeit für [Linkvorlagen]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates) nicht verfügbar.
{% endalert %}

