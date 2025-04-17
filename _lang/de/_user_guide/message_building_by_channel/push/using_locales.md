---
nav_title: Lokale in Nachrichten
article_title: Lokale in Nachrichten
page_order: 9
description: "In diesem Artikel erfahren Sie, wie Sie in Ihren Push-Benachrichtigungen Gebietsschemata verwenden können."
---

# Lokalisierungen in Nachrichten

> Nachdem Sie Ihrem Workspace Gebietsschemata hinzugefügt haben, können Sie Nutzer:innen in verschiedenen Sprachen in einer einzigen Push-Benachrichtigung zusammenstellen.

## Voraussetzungen

Um die [Mehrsprachenunterstützung]({{site.baseurl}}/multi_language_support/) konfigurieren zu können, benötigen Sie die Benutzerberechtigung "Mehrsprachigkeitseinstellungen konfigurieren". Um das Gebietsschema einer Nachricht einzustellen, benötigen Sie eine Berechtigung zur Bearbeitung von Kampagnen.

## Verwendung von Gebietsschemata

Um Lokalisierungen in Ihren Messaging-Nachrichten zu verwenden, erstellen Sie eine Push-Kampagne oder ein Canvas und führen dann die folgenden Schritte aus:

1. Fügen Sie die Übersetzungs-Tags {% raw %}`{% translation %}` und `{% endtranslation %}`{% endraw %} hinzu, um alle zu übersetzenden Texte, Bilder und Links einzufassen.<br><br>![Push-Benachrichtigung-Editor mit Übersetzungs-Tags für die Titel- und Nachrichtenfelder.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})<br><br>
2. Speichern Sie Ihre Nachricht als Entwurf.
3. Wählen Sie **Sprache verwalten** und fügen Sie über das Dropdown-Menü Ihre Lokalisierungen für die Nachricht hinzu.
4. Wählen Sie **Template herunterladen** aus und geben Sie die Übersetzungen in das CSV Template ein. <br><br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})<br><br>
5. Um die fertige CSV-Vorlage hochzuladen, wählen Sie **Übersetzungen hochladen**. <br><br>![Das Fenster "Mehrsprachige Nachrichten" mit zwei ausgewählten Lokalisierungen und Buttons zum Herunterladen eines Templates oder Hochladen von Übersetzungen.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

Um die Übersetzungen zu ändern, aktualisieren Sie die CSV und laden Sie die Datei erneut hoch. Änderungen an IDs oder Gebietsschemata in der CSV-Datei werden nicht automatisch in der Nachricht aktualisiert.

{% alert tip %}
Sehen Sie sich unsere [Translation API]({{site.baseurl}}/api/endpoints/translations) an, um Übersetzungen in Ihren Kampagnen und Canvase zu verwalten und zu aktualisieren.
{% endalert %}

## Vorschau auf Gebietsschemata

Wählen Sie im Dropdown-Menü **Vorschau der Nachricht als Nutzer:** in auf dem Tab **Test** die Option **Benutzer:innen** aus und geben Sie verschiedene Sprachen ein, um eine Vorschau der Nachricht anzuzeigen und zu prüfen, ob Ihre Nachricht wie erwartet übersetzt wird.

{% multi_lang_include locales.md section="Häufig gestellte Fragen" %}
