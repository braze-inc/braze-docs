{% if include.section == "Prerequisites" %}
## Voraussetzungen

Um [die Mehrsprachenunterstützung]({{site.baseurl}}/multi_language_support/) zu bearbeiten und zu verwalten, benötigen Sie die folgenden [Nutzer:innen-Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) für Ihren Workspace:

- Lokalisierungseinstellungen anzeigen
- Lokalisierungseinstellungen bearbeiten
- Lokalisierungseinstellungen löschen

Um die Ländereinstellung zu einer Nachricht hinzuzufügen, benötigen Sie die Berechtigung „Kampagnen bearbeiten".

{% alert important %}
Die Mehrsprachenunterstützung befindet sich derzeit im Early Access. Kontaktieren Sie Ihren Braze Account Manager, wenn Sie an der Early-Access-Phase teilnehmen möchten.
{% endalert %}

{% endif %}

{% if include.section == "Preview" %}

## Vorschau Ihrer Lokalisierungen

Wählen Sie im Dropdown-Menü **Vorschau der Nachricht als Nutzer:in** auf dem Tab **Test** die Option **Angepasste:r Nutzer:in** aus und geben Sie verschiedene Sprachen ein, um eine Vorschau der Nachricht anzuzeigen und zu prüfen, ob Ihre Nachricht wie erwartet übersetzt wird.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Häufig gestellte Fragen

#### Kann ich eine Änderung am übersetzten Text in einer meiner Lokalisierungen vornehmen?
Ja. Nehmen Sie zunächst die Bearbeitung in der CSV-Datei vor und laden Sie die Datei dann erneut hoch, um eine Änderung am übersetzten Text vorzunehmen.

#### Lassen sich Übersetzungs-Tags verschachteln?
Nein.

#### Können Übersetzungs-Tags mit HTML-Styling versehen werden?
Ja, aber achten Sie darauf, dass das HTML-Styling nicht mit dem Inhalt übersetzt wird.

#### Welche Validierungen oder zusätzlichen Prüfungen führt Braze durch?

| Szenario                                                                                                                                                 | Validierung in Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| In einer Übersetzungsdatei fehlen die mit der jeweiligen Nachricht verbundenen Lokalisierungen.                                                                               | Diese Übersetzungsdatei wird nicht hochgeladen.                                                                       |
| In einer Übersetzungsdatei fehlen Textblöcke, etwa Text innerhalb von Liquid-Übersetzungs-Tags, aus der jeweiligen E-Mail-Nachricht.                                | Diese Übersetzungsdatei wird nicht hochgeladen.                                                                       |
| Die Übersetzungsdatei enthält den Standardtext, der nicht mit den Textblöcken der jeweiligen E-Mail-Nachricht übereinstimmt.                                          | Diese Übersetzungsdatei wird nicht hochgeladen. Korrigieren Sie den Fehler in der CSV-Datei, bevor Sie den Upload erneut versuchen.               |
| Die Übersetzungsdatei enthält Lokalisierungen, die in den Einstellungen unter **Multi-Language Support** nicht vorhanden sind.                                                           | Diese Lokalisierungen werden nicht in Braze gespeichert.                                                                      |
| Die Übersetzungsdatei enthält Textblöcke, die in der aktuellen Nachricht nicht vorhanden sind (z. B. im aktuellen Entwurf zum Zeitpunkt des Hochladens der Übersetzungen). | Textblöcke, die in der aktuellen Nachricht nicht vorhanden sind, werden nicht aus der Übersetzungsdatei in Braze übernommen. |
| Eine Lokalisierung wird aus einer Nachricht entfernt, nachdem sie als Teil der Übersetzungsdatei in die Nachricht hochgeladen wurde.                           | Wenn Sie die Lokalisierung entfernen, werden alle damit verbundenen Übersetzungen in der Nachricht gelöscht.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}