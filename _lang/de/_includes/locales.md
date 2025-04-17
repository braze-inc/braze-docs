{% if include.section == "Frequently Asked Questions" %}

## Häufig gestellte Fragen

#### Kann ich eine Änderung an der übersetzten Kopie in einer meiner Lokalisationen vornehmen?
Ja Nehmen Sie zunächst die Bearbeitung in der CSV-Datei vor und laden Sie die Datei dann erneut hoch, um eine Änderung an der übersetzten Kopie vorzunehmen.

#### Lassen sich Übersetzungs-Tags verschachteln?
Nein.

#### Können Übersetzungs-Tags mit HTML-Designs versehen werden?
Ja, aber achten Sie darauf, dass das HTML-Styling nicht mit dem Inhalt übersetzt wird.

#### Welche Validierungen oder zusätzlichen Prüfungen führt Braze durch?

| Szenario                                                                                                                                                 | Validierung in Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| In einer Übersetzungsdatei fehlen die mit der jeweiligen Nachricht verbundenen Gebietsschemata.                                                                               | Diese Übersetzungsdatei wird nicht hochgeladen.                                                                       |
| In einer Übersetzungsdatei fehlen Textblöcke etwa aus Liquid-Übersetzungs-Tags aus der jeweiligen E-Mail.                                | Diese Übersetzungsdatei wird nicht hochgeladen.                                                                       |
| Die Übersetzungsdatei enthält den Standardtext, der nicht mit den Textblöcken der jeweiligen E-Mail übereinstimmt.                                          | Diese Übersetzungsdatei wird nicht hochgeladen. Korrigieren Sie den Fehler in der CSV-Datei, bevor Sie den Upload erneut versuchen.               |
| Die Übersetzungsdatei enthält Gebietsschemata, die in den **Mehrsprachigkeitseinstellungen** nicht vorkommen.                                                           | Diese Gebietsschemata werden nicht in Braze gespeichert.                                                                      |
| Die Übersetzungsdatei enthält Textblöcke, die in der aktuellen Nachricht nicht vorkommen (wie den Entwurfsstand beim Upload der Übersetzungen). | Textblöcke, die in der Nachricht fehlen, werden nicht aus der Übersetzungsdatei übernommen und in Braze gespeichert. |
| Ein Gebietsschema wird aus einer Nachricht entfernt, nachdem es als Teil der Übersetzungsdatei in die Nachricht übernommen worden ist.                           | Wenn Sie das Gebietsschema entfernen, werden alle damit verbundenen Übersetzungen in der Nachricht entfernt.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}