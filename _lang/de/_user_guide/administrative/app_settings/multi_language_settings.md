---
nav_title: Mehrsprachige Einstellungen
article_title: Mehrsprachige Einstellungen
alias: "/multi_language_support/"
page_order: 5.5
description: "Dieser Artikel bietet eine Übersicht über die mehrsprachigen Einstellungen im Braze-Dashboard und darüber, wie Sie Lokalisierungen in Ihrem Messaging verwenden können."
---

# Mehrsprachige Einstellungen

> Wenn Sie die Einstellungen für die Mehrsprachigkeit anpassen, können Sie Nutzer in verschiedenen Sprachen und an verschiedenen Orten mit unterschiedlichen Nachrichten in einer einzigen E-Mail-Nachricht ansprechen.

## Voraussetzungen

Um die Unterstützung für mehrere Sprachen zu bearbeiten und zu verwalten, benötigen Sie die Nutzerberechtigung „Einstellungen für mehrere Sprachen verwalten verwalten“. Um das Gebietsschema einer Nachricht einzustellen, benötigen Sie eine Berechtigung zur Bearbeitung von Kampagnen.

{% alert important %}
Die Unterstützung mehrerer Sprachen befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Early-Access-Phase teilnehmen möchten.
{% endalert %}

## Gebietsschema hinzufügen

1. Gehen Sie zu **Einstellungen** > **Mehrsprachige Unterstützung** unter **Arbeitsbereichseinstellungen**.
2. Wählen Sie **Gebietsschema hinzufügen** und wählen Sie dann **Standardgebietsschema** oder **Benutzerdefinierte Attribute**.<br><br>![Das Dropdown-Menü "Gebietsschema hinzufügen" mit Optionen zur Auswahl des Standardgebietsschemas oder angepasster Attribute.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}
3. Geben Sie einen Namen für das Gebietsschema ein.
4. Wählen Sie die entsprechenden Nutzerattribute für die von Ihnen gewählte Gebietsschema-Option aus.

{% tabs %}
{% tab Default locale %}

Verwenden Sie für **Standard-Gebietsschema** die Dropdown-Listen, um die hinzuzufügende Sprache und optional das Land, das mit der Sprache verknüpft werden soll, auszuwählen.<br><br>![Ein Fenster mit der Bezeichnung "Gebietsschema hinzufügen - Standardsprache und Land", um die Sprache und das Land anzugeben.]({% image_buster /assets/img/multi-language_support/default_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Custom attributes %}

Für **benutzerdefinierte Attribute** wählen Sie aus der Dropdown-Liste das entsprechende benutzerdefinierte Attribut aus und geben in das Textfeld den Wert ein.<br><br>![Ein Fenster namens "Gebietsschema hinzufügen - Angepasste Attribute", um das angepasste Attribut und den Wert festzulegen.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{: start="5"}
5\. Wählen Sie **Gebietsschema hinzufügen** aus. 

Wie Sie diese Gebietsschemata in Ihren E-Mail-Kampagnen und Canvas verwenden können, erfahren Sie unter [Verwendung von Gebietsschemata]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/).

## Überlegungen

- Beim Einrichten eines Gebietsschemas können Sie entweder Sprachen aus den Standardattributen den angepassten Attributen für Nutzer:innen auswählen. Sie können nicht aus beiden wählen.
- Sie können bis zu zwei angepasste Attribute in einem einzigen Gebietsschema oder bis zu zwei Standard-Nutzerattribute in einer Sprache auswählen. In beiden Fällen ist das zweite Attribut optional.
- Wenn Sie Änderungen an den übersetzten Werten in der CSV-Datei vornehmen, vermeiden Sie es, die Standardwerte in der Datei zu ändern.
- Der Lokalisierungsschlüssel in Ihrer hochgeladenen Datei muss mit dem Schlüssel in Ihren Mehrspracheneinstellungen übereinstimmen.

### Unterstützung und Prioritätensetzung

- Benutzer, die mit einem benutzerdefinierten Attribut locale übereinstimmen, werden vor Benutzern bevorzugt, die mit einem Standardbenutzerattribut übereinstimmen.
- Die Unterstützung für benutzerdefinierte Attribute ist auf String-Typen und den Vergleichsschlüssel `equals` beschränkt.
- Wenn ein angepasstes Attribut gelöscht oder sein Typ geändert wird, kann der Nutzer:innen nicht mehr in diese Lokalisierung fallen und wird entweder in der Prioritätsliste der Lokalisierungen nach unten rutschen oder Standardübersetzungen für das Marketing erhalten.
- Wenn ein Gebietsschema ungültig ist (das benutzerdefinierte Attribut hat sich geändert oder wurde gelöscht), wird der Fehler auf der Seite **Mehrsprachiger Support** angezeigt.

## Häufig gestellte Fragen

#### Wie viele Gebietsschemata kann ich hinzufügen?

Sie können bis zu 200 Gebietsschemata hinzufügen.

#### Wo werden die Übersetzungsdateien in Braze gespeichert?

Die Übersetzungsdateien werden auf Kampagnen-Ebene gespeichert, d. h. für jede Variante der Nachricht müssen Übersetzungen hochgeladen werden.

#### Muss der Name des Gebietsschemas einem bestimmten Muster oder Format folgen?

Nein. Sie können Ihre bevorzugte Benennungskonvention verwenden. Der Name des Gebietsschemas wird bei der Auswahl des Gebietsschemas im Editor verwendet und erscheint in den Überschriften der Datei, die Sie mit den Übersetzungs-IDs herunterladen.

