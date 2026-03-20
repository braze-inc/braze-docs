---
nav_title: Angepasste Attribute
article_title: Angepasste Attribute
page_order: 10
page_type: reference
description: "Diese Seite beschreibt angepasste Attribute und erläutert die verschiedenen Datentypen für angepasste Attribute."
search_rank: 1
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Angepasste Attribute

> Auf dieser Seite finden Sie Informationen zu angepassten Attributen, die eine Sammlung eindeutiger Eigenschaften Ihrer Nutzer:innen darstellen. Angepasste Attribute eignen sich am besten zum Speichern von Attributen über Ihre Nutzer:innen oder von Informationen über geringwertige Aktionen innerhalb Ihrer Anwendung. 

In Braze gespeicherte angepasste Attribute können zum Aufbau von Zielgruppen-Segmenten und zur Personalisierung von Nachrichten mit Liquid verwendet werden. Denken Sie daran, dass wir für angepasste Attribute keine Zeitreiheninformationen speichern, sodass Sie keine darauf basierenden Diagramme erhalten können, wie dies bei angepassten Events der Fall ist.

## Angepasste Attribute verwalten

Um angepasste Attribute im Dashboard zu erstellen und zu verwalten, gehen Sie zu **Dateneinstellungen** > **Angepasste Attribute**. 

![Vier angepasste Attribute, die Boolesche Werte sind.]({% image_buster /assets/img/export_custom_attributes.png %})

In der Spalte **Letztes Update** sehen Sie, wann das angepasste Attribut das letzte Mal bearbeitet wurde, z. B. wann es zuletzt auf Blockliste oder aktiv gesetzt wurde.

{% alert important %}
Für ein korrektes Targeting von Nachrichten sollten Sie darauf achten, dass der Datentyp Ihres angepassten Attributs mit dem tatsächlichen angepassten Attribut übereinstimmt. <br><br>Wenn beispielsweise `newsletter_subscribed` als String definiert ist, sollte Ihre Liquid-Syntax wie folgt aussehen: {% raw %}```{% if {{custom_attribute.${newsletter_subscribed}}} == 'true' %}```{% endraw %}. Wenn `newsletter_subscribed` als boolescher Wert definiert ist, sollte die Liquid-Syntax keine einfachen Anführungszeichen enthalten: {% raw %}```{% if {{custom_attribute.${newsletter_subscribed}}} == true %}```{% endraw %}.
{% endalert %}

Auf dieser Seite können Sie vorhandene angepasste Attribute anzeigen, verwalten, erstellen oder blockieren. Wählen Sie das Menü neben einem angepassten Attribut für die folgenden Aktionen aus:

### Auf Sperrliste setzen

Angepasste Attribute können einzeln im Aktionsmenü blockiert werden, oder es können bis zu 100 Attribute ausgewählt und in einer Massenaktion blockiert werden. Wenn Sie ein angepasstes Attribut sperren, werden keine Daten zu diesem Attribut erfasst, vorhandene Daten sind nicht verfügbar, es sei denn, sie werden reaktiviert, und blockierte Attribute werden nicht in Filtern oder Diagrammen angezeigt. Wenn das Attribut derzeit von Filtern oder Triggern in anderen Bereichen des Braze-Dashboards referenziert wird, erscheint außerdem ein Warnungs-Modal, in dem erklärt wird, dass alle Instanzen der Filter oder Trigger, die darauf verweisen, entfernt und archiviert werden.

### Kennzeichnung als persönlich identifizierbare Information (PII)

Administratoren können von dieser Seite aus auch angepasste Attribute erstellen und sie als PII markieren. Diese Attribute sind nur für Administratoren und Dashboard-Nutzer:innen mit der Berechtigung „Als PII markierte angepasste Attribute anzeigen" sichtbar.

### Hinzufügen von Beschreibungen

Sie können einem angepassten Attribut eine Beschreibung hinzufügen, nachdem es erstellt wurde, wenn Sie über die [Nutzer:innen-Berechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases` verfügen. Bearbeiten Sie das angepasste Attribut und geben Sie ein, was immer Sie möchten, z. B. eine Notiz für Ihr Team.

### Hinzufügen von Tags

Sie können Tags zu einem angepassten Attribut hinzufügen, nachdem es erstellt wurde, wenn Sie die [Nutzer:innen-Berechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) „Events, Attribute, Käufe verwalten" haben. Die Tags können dann zum Filtern der Liste der Attribute verwendet werden. 

### Angepasste Attribute entfernen

Es gibt zwei Möglichkeiten, wie Sie angepasste Attribute aus Nutzerprofilen entfernen können:

* Wählen Sie den Namen des angepassten Attributs aus, das in einem [Nutzer:innen-Update-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes) entfernt werden soll.
* Setzen Sie den Wert `null` in Ihrer API-Anfrage an den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

### Daten exportieren

Um die Liste der angepassten Attribute als CSV-Datei zu exportieren, wählen Sie oben auf der Seite **Alle exportieren**. Die CSV-Datei wird generiert, und ein Download-Link wird Ihnen per E-Mail zugesandt.

## Nutzungsberichte anzeigen

Der Nutzungsbericht listet alle Canvase, Kampagnen und Segmente auf, die ein bestimmtes angepasstes Attribut verwenden. Diese Liste enthält keine Verwendungen von Liquid. 

Sie können bis zu 100 Nutzungsberichte auf einmal anzeigen, indem Sie die Kontrollkästchen neben den jeweiligen angepassten Attributen aktivieren und dann **Nutzungsbericht anzeigen** wählen.

### Tab „Werte"

Wenn Sie einen Nutzungsbericht anzeigen, wählen Sie den Tab **Werte**, um die häufigsten Werte der ausgewählten angepassten Attribute basierend auf einer Stichprobe von etwa 250.000 Nutzer:innen anzuzeigen. Bitte beachten Sie, dass die Ergebnisse aus einer Teilmenge von Nutzer:innen stammen und daher nicht alle vorhandenen Werte enthalten. Dies bedeutet, dass der Tab **Werte** nicht zur Fehlerbehebung oder für Anwendungsfälle verwendet werden sollte, die die Einbeziehung von Daten aller Nutzer:innen erfordern.

![Nutzungsbericht für ausgewählte angepasste Attribute mit geöffnetem Tab „Werte", der ein Kreisdiagramm mit den Attributwerten für Länder wie „US" und „PR" anzeigt.]({% image_buster /assets/img/usage_report_values.png %}){: style="max-width:80%;"}

## Angepasste Attribute festlegen

Im Folgenden finden Sie eine Liste von Methoden für verschiedene Plattformen, mit denen Sie angepasste Attribute festlegen können.

{% details Expand for documentation by platform %}

- [Android und FireOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)
- [Internet]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=unity)
- [.NET MAUI (früher Xamarin)]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/)

{% enddetails %}

## Speicherung angepasster Attribute

Alle im **Nutzerprofil** gespeicherten Daten, einschließlich der Daten zu angepassten Attributen, werden auf unbestimmte Zeit gespeichert, solange das jeweilige Profil [aktiv]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users) ist.

## Datentypen für angepasste Attribute

Angepasste Attribute sind außerordentlich flexible Tools, die ein hervorragendes Targeting ermöglichen.

Die folgenden Datentypen können als angepasste Attribute gespeichert werden:

- [Boolesche Werte](#booleans)
- [Zahlen](#numbers)
- [Strings](#strings)
- [Arrays](#arrays)
- [Zeit](#time)
- [Objekte]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)
- [Arrays von Objekten]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/)

### Boolesche Werte (wahr/falsch) {#booleans}

Boolesche Attribute sind nützlich, um einfache binäre Daten über Ihre Nutzer:innen zu speichern, wie z. B. den Status von Abonnements. Sie können Nutzer:innen finden, bei denen eine Variable explizit auf den Wert „wahr" oder „falsch" gesetzt ist, sowie Nutzer:innen, bei denen dieses Attribut noch nicht aufgezeichnet wurde.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob der boolesche Wert entweder wahr, falsch, wahr oder nicht gesetzt, oder falsch oder nicht gesetzt **ist** | **IS**  | **TRUE**, **FALSE**, **TRUE OR NOT SET** oder **FALSE OR NOT SET** | Wenn dieser Filter `coffee_drinker` angibt, wird ein:e Nutzer:in in den folgenden Fällen diesem Filter entsprechen: <br> {::nomarkdown}<ul><li>Wenn dieser Filter <code>true</code> ist und der/die Nutzer:in den Wert <code>coffee_drinker</code> hat</li><li>Wenn dieser Filter <code>false</code> ist und der/die Nutzer:in nicht den Wert <code>coffee_drinker</code> hat</li><li>Wenn dieser Filter <code>true or not set</code> ist und der/die Nutzer:in den Wert <code>coffee_drinker</code> oder keinen Wert hat</li><li>Wenn dieser Filter <code>false or not set</code> ist und der/die Nutzer:in nicht <code>coffee_drinker</code> oder keinen Wert hat</li></ul>{:/} |
| Prüfen, ob der boolesche Wert im Profil eines Nutzers/einer Nutzerin **existiert** und nicht null ist | **IS NOT BLANK**  | **N/A** | Wenn dieser Filter `coffee_drinker` angibt und ein:e Nutzer:in einen Wert für das Attribut `coffee_drinker` hat, wird der/die Nutzer:in diesem Filter entsprechen. | 
| Prüfen, ob der boolesche Wert im Profil eines Nutzers/einer Nutzerin **nicht existiert** oder null ist | **IS BLANK**  | **N/A** | Wenn dieser Filter `coffee_drinker` angibt und ein:e Nutzer:in entweder nicht über das Attribut `coffee_drinker` verfügt oder der Wert für `coffee_drinker` null ist, wird der/die Nutzer:in diesem Filter entsprechen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Zahlen {#numbers}

Numerische Attribute umfassen [Ganzzahlen](https://en.wikipedia.org/wiki/Integer) und [Gleitkommazahlen](https://en.wikipedia.org/wiki/Floating-point_arithmetic) und haben eine Vielzahl von Anwendungsfällen. Inkrementierende angepasste Zahlenattribute sind nützlich, um zu speichern, wie oft eine bestimmte Aktion oder ein bestimmtes Event stattgefunden hat, ohne dass dies auf Ihr Datenlimit angerechnet wird. Standardzahlen haben alle möglichen Verwendungszwecke, wie z. B. die Aufzeichnung von:

- Schuhgröße
- Taillenumfang
- Anzahl der Male, die ein:e Nutzer:in ein bestimmtes Produkt-Feature oder eine Kategorie angesehen hat

{% alert tip %}
Ausgegebenes Geld sollte nicht auf diese Weise erfasst werden. Vielmehr sollte es über unsere [Kaufmethoden](#purchase-revenue-tracking) erfasst werden.
{% endalert %}

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das numerische Attribut **genau** einer **Zahl** entspricht| **EXACTLY** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Nutzerprofil den Wert `10` hat, wird der/die Nutzer:in diesem Filter entsprechen. |
| Prüfen, ob das numerische Attribut **nicht** einer **Zahl** entspricht| **DOES NOT EQUAL** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Nutzerprofil nicht den Wert `10` hat, wird der/die Nutzer:in diesem Filter entsprechen. |
| Prüfen, ob das numerische Attribut **mehr als** eine **Zahl** ist| **MORE THAN** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Nutzerprofil einen Wert größer als `10` hat, wird der/die Nutzer:in diesem Filter entsprechen. |
| Prüfen, ob das numerische Attribut **weniger als** eine **Zahl** ist| **LESS THAN** | **NUMBER** | Wenn dieser Filter `10` angibt und ein Nutzerprofil einen Wert kleiner als `10` hat, wird der/die Nutzer:in diesem Filter entsprechen. |
| Prüfen, ob das numerische Attribut im Profil eines Nutzers/einer Nutzerin **existiert** und nicht null ist | **IS NOT BLANK** | **N/A** | Wenn ein Nutzerprofil das angegebene numerische Attribut enthält, unabhängig vom Wert, wird der/die Nutzer:in diesem Filter entsprechen. |
| Prüfen, ob das numerische Attribut im Profil eines Nutzers/einer Nutzerin **nicht existiert** oder null ist | **IS BLANK** | **N/A** | Wenn ein Nutzerprofil das angegebene numerische Attribut nicht enthält oder der Wert des Attributs null ist, wird der/die Nutzer:in diesem Filter entsprechen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Details zu Zahlenattributen

- Die Filter „Genau 0" und „Weniger als" schließen Nutzer:innen mit NULL-Feldern ein.
  - Um Nutzer:innen ohne einen Wert für angepasste Attribute auszuschließen, müssen Sie den Filter **is not blank** einfügen.

### Strings (alphanumerische Zeichen) {#strings}

String-Attribute sind nützlich, um Nutzereingaben zu speichern, z. B. eine Lieblingsmarke, eine Telefonnummer oder einen letzten Suchstring in Ihrer Anwendung. String-Attribute können bis zu 255 Zeichen lang sein.

Beachten Sie, dass Braze bei der Eingabe von Werten, die Leerzeichen zwischen, vor oder nach Wörtern enthalten, auch auf diese Leerzeichen prüft.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das String-Attribut **teilweise mit** einem eingegebenen String **übereinstimmt** **ODER** einem regulären Ausdruck | **MATCHES REGEX** | **STRING** **ODER** **REGULAR EXPRESSION** <br>Groß-/Kleinschreibung wird nicht unterschieden; maximal 32.764 Zeichen | 
| Prüfen, ob das String-Attribut **nicht teilweise mit** einem eingegebenen String **übereinstimmt** **ODER** einem regulären Ausdruck | **DOES NOT MATCH REGEX** * | **STRING** **ODER** **REGULAR EXPRESSION**<br>Groß-/Kleinschreibung wird nicht unterschieden; maximal 32.764 Zeichen |
| Prüfen, ob das String-Attribut im Profil eines Nutzers/einer Nutzerin **existiert** und kein leerer String ist | **IS NOT BLANK** | **N/A** | Wenn dieser Filter `favorite_genre` angibt und ein Nutzerprofil das Attribut `favorite_genre` hat, wird der/die Nutzer:in unabhängig vom Attributwert diesem Filter entsprechen. Der/die Nutzer:in kann zum Beispiel `sci-fi`, `romance` oder einen anderen Wert haben.|
| Prüfen, ob das String-Attribut im Profil eines Nutzers/einer Nutzerin **nicht existiert** | **BLANK** | **N/A** | Wenn dieser Filter `favorite_genre` angibt und ein Nutzerprofil nicht über das Attribut `favorite_genre` verfügt, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob der String genau mit **einem der** eingegebenen Strings übereinstimmt | **IS ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings zulässig (maximal 256) | Wenn dieser Filter `book`, `bookmark` und `reading light` angibt und ein Nutzerprofil mindestens einen dieser Strings enthält, wird der/die Nutzer:in diesem Filter entsprechen. |
| Prüfen, ob das String-Attribut **nicht genau mit einem** der eingegebenen Strings übereinstimmt | **IS NONE OF** |**STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings zulässig (maximal 256) | Wenn dieser Filter `book`, `bookmark` und `reading light` angibt und ein Nutzerprofil keinen dieser Strings enthält, wird der/die Nutzer:in dem Filter entsprechen.|
| Prüfen, ob das String-Attribut **teilweise mit einem der** eingegebenen Strings **übereinstimmt** | **CONTAINS ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings zulässig (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil `gold` in einem beliebigen String enthält, wie z. B. `gold_tier` oder `former_gold_tier`, wird der/die Nutzer:in dem Filter entsprechen. |
| Prüfen, ob das String-Attribut **nicht teilweise mit einem der** eingegebenen Strings **übereinstimmt** | **DOESN'T CONTAIN ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings zulässig (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil in keinem String `gold` enthält, wird der/die Nutzer:in diesem Filter entsprechen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

{% alert important %}
Wenn Sie mit dem Filter **DOES NOT MATCH REGEX** segmentieren, müssen Sie bereits ein angepasstes Attribut mit einem zugewiesenen Wert in diesem Nutzerprofil haben. Braze empfiehlt, mit „OR"-Logik zu prüfen, ob ein angepasstes Attribut leer ist, um sicherzustellen, dass die Nutzer:innen richtig angesprochen werden.
{% endalert %}

### Arrays {#arrays}

Array-Attribute sind gut geeignet, um zusammenhängende Listen mit Informationen über Ihre Nutzer:innen zu speichern. Wenn Sie zum Beispiel die letzten 100 Inhalte, die ein:e Nutzer:in angesehen hat, in einem Array speichern, ist eine Segmentierung nach bestimmten Interessen möglich.

Arrays haben eine maximale Größe von 100&nbsp;KB. Die Standardlänge für ein Attribut beträgt bis zu 500 Einträge. Wenn Sie z. B. ein Attribut wie „Angesehene Filme" übermitteln und es auf 500 gesetzt ist, wird beim 501. Film der erste Film aus dem Array entfernt und der neueste Film hinzugefügt. 

Beachten Sie, dass Braze bei der Eingabe von Werten, die Leerzeichen zwischen, vor oder nach Wörtern enthalten, auch auf diese Leerzeichen prüft.

{% alert note %}
Die Option zum Erhöhen der maximalen Länge ist nicht verfügbar, wenn das Attribut so eingestellt ist, dass der Datentyp automatisch erkannt wird; der Datentyp muss auf Array eingestellt sein.
{% endalert %}

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das Array-Attribut **einen Wert enthält, der genau mit** einem eingegebenen Wert **übereinstimmt**| **INCLUDES VALUE** | **STRING** | Wenn dieser Filter `sci-fi` angibt und ein Nutzerprofil den Wert `sci-fi` hat, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob das Array-Attribut **keinen Wert enthält, der genau mit** einem eingegebenen Wert **übereinstimmt**| **DOESN'T INCLUDE VALUE** | **STRING** | Wenn dieser Filter `sci-fi` angibt und ein Nutzerprofil nicht den Wert `sci-fi` hat, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob das Array-Attribut **einen Wert enthält, der teilweise mit** einem eingegebenen Wert **übereinstimmt** **ODER** einem regulären Ausdruck | **MATCHES REGEX** | **STRING** **ODER** **REGULAR EXPRESSION**<br>Maximal 32.764 Zeichen | |
| Prüfen, ob das Array-Attribut **einen Wert hat** oder nicht leer ist | **HAS A VALUE** | **N/A** | Wenn dieser Filter `favorite_genres` angibt und ein Nutzerprofil `favorite_genres` mit einem beliebigen Wert enthält, wird der/die Nutzer:in diesem Filter entsprechen. |
| Prüfen, ob das Array-Attribut **leer ist** oder nicht existiert | **IS EMPTY** | **N/A** | Wenn dieser Filter `favorite_genres` angibt und ein Nutzerprofil `favorite_genres` nicht enthält oder `favorite_genres` enthält, aber keine Werte hat, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob das Array-Attribut **einen Wert enthält, der genau mit einem der** eingegebenen Werte **übereinstimmt** | **INCLUDES ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte zulässig (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil eine beliebige Kombination von `sci-fi`, `fantasy` oder `romance` enthält, einschließlich nur eines davon (z. B. nur `sci-fi`). Ein:e Nutzer:in kann `horror` oder einen anderen Wert in seinem/ihrem String haben, wenn er/sie auch einen der Werte `sci-fi`, `fantasy` und `romance` hat.|
| Prüfen, ob das Array-Attribut **keinen Wert enthält, der genau mit einem der** eingegebenen Werte **übereinstimmt** | **INCLUDES NONE OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte zulässig (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil keine Kombination von `sci-fi`, `fantasy` oder `romance` enthält, wird der/die Nutzer:in diesem Filter entsprechen. Der/die Nutzer:in kann `horror` oder einen anderen Wert haben, wenn er/sie keinen der Werte `sci-fi`, `fantasy` oder `romance` hat.|
| Prüfen, ob das Array-Attribut **einen Wert enthält, der teilweise mit einem der** eingegebenen Werte **übereinstimmt** | **VALUES CONTAIN ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte zulässig (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil-Array `gold` in mindestens einem String enthält, wird der/die Nutzer:in diesem Filter entsprechen. Dazu gehören String-Werte wie `gold_tier`, `former_gold_tier` und andere.|
| Prüfen, ob das Array-Attribut **keinen Wert enthält, der teilweise mit einem der** eingegebenen Werte **übereinstimmt** | **VALUES DON'T CONTAIN ANY OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte zulässig (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil-Array in keinem String `gold` enthält, wird der/die Nutzer:in diesem Filter entsprechen. Das bedeutet, dass Nutzer:innen mit String-Werten wie `gold_tier` und `former_gold_tier` diesem Filter nicht entsprechen.|
| Prüfen, ob das Array-Attribut **alle** eingegebenen Werte **enthält** | **IS ALL OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte zulässig (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil alle diese Werte aufweist, wird der/die Nutzer:in diesem Filter entsprechen. Der/die Nutzer:in kann auch `horror` oder andere Werte haben und diesem Filter entsprechen.|
| Prüfen, ob das Array-Attribut **nicht alle** eingegebenen Werte **enthält** | **ISN'T ALL OF** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte zulässig (maximal 256)|  Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil nicht alle diese Werte enthält, wird der/die Nutzer:in diesem Filter entsprechen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Wenn Sie mehr über die Verwendung regulärer Ausdrücke (Regex) erfahren möchten, lesen Sie diese Ressourcen:
- [Perl-kompatible reguläre Ausdrücke (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex mit Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Regex-Debugger und -Tester](https://www.regex101.com/)
- [Regex-Tutorial](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Zeit {#time}

Zeitattribute sind nützlich, um zu speichern, wann eine bestimmte Aktion das letzte Mal durchgeführt wurde, damit Sie Ihren Nutzer:innen inhaltsspezifische Nachrichten zur erneuten Interaktion anbieten können.

Zeitfilter mit relativen Daten (z. B. vor mehr als 1 Tag, vor weniger als 2 Tagen) messen 1 Tag als 24 Stunden. Jede Kampagne, die Sie mit diesen Filtern durchführen, schließt alle Nutzer:innen in 24-Stunden-Schritten ein. Zum Beispiel wird `last used app more than 1 day ago` alle Nutzer:innen erfassen, die „die App zuletzt vor mehr als 24 Stunden" ab dem genauen Zeitpunkt der Kampagnenausführung genutzt haben. Dasselbe gilt für Kampagnen mit längeren Datumsbereichen – fünf Tage nach der Aktivierung bedeuten also die letzten 120 Stunden.

Um beispielsweise ein Segment zu erstellen, das auf Nutzer:innen mit einem Zeitattribut zwischen 24 und 48 Stunden in der Zukunft abzielt, wenden Sie die Filter `in more than 1 day in the future` und `in less than 2 days in the future` an.

{% alert warning %}
Das letzte Datum, an dem ein angepasstes Event oder ein Kauf-Event stattgefunden hat, wird automatisch aufgezeichnet und sollte nicht erneut über ein angepasstes Zeitattribut aufgezeichnet werden.
{% endalert %}

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob das Zeitattribut **vor** einem **ausgewählten Datum** liegt| **BEFORE** | **CALENDAR DATE SELECTOR** | Wenn dieser Filter `2024-01-31` angibt und ein Nutzerprofil ein Datum vor `2024-1-31` hat, wird der/die Nutzer:in diesem Filter entsprechen. |
| Prüfen, ob das Zeitattribut **nach** einem **ausgewählten Datum** liegt| **AFTER** | **CALENDAR DATE SELECTOR** | Wenn dieser Filter `2024-01-31` angibt und ein Nutzerprofil ein Datum nach `2024-1-31` hat, wird der/die Nutzer:in diesem Filter entsprechen. |
| Prüfen, ob das Zeitattribut **mehr als X Tage** zurückliegt | **MORE THAN** | **NUMBER OF DAYS AGO** | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das mehr als sieben Tage zurückliegt, wird der/die Nutzer:in diesem Filter entsprechen. |
| Prüfen, ob das Zeitattribut **weniger als X Tage** zurückliegt| **LESS THAN** | **NUMBER OF DAYS AGO** | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das weniger als sieben Tage zurückliegt, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob das Zeitattribut **mehr als X Tage in der Zukunft** liegt | **IN MORE THAN** | **NUMBER OF DAYS IN FUTURE** | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das mehr als sieben Tage in der Zukunft liegt, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob das Zeitattribut **weniger als X Tage in der Zukunft** liegt | **IN LESS THAN** | **NUMBER OF DAYS IN FUTURE**  | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das weniger als sieben Tage in der Zukunft liegt, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob das Zeitattribut im Profil eines Nutzers/einer Nutzerin **existiert** und nicht null ist | **IS NOT BLANK** | **N/A** | Wenn dieser Filter ein Zeitattribut angibt, das sich in einem Nutzerprofil befindet, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob das Zeitattribut im Profil eines Nutzers/einer Nutzerin **nicht existiert** oder null ist | **IS BLANK** | **N/A** | Wenn dieser Filter ein Zeitattribut angibt, das sich nicht in einem Nutzerprofil befindet, wird der/die Nutzer:in diesem Filter entsprechen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Details zu Zeitattributen

- Tag des wiederkehrenden Events
  - Wenn Sie den Filter „Tag des wiederkehrenden Events" verwenden und dann aufgefordert werden, den „Kalendertag des wiederkehrenden Events" auszuwählen, wird bei Auswahl von `IS LESS THAN` oder `IS MORE THAN` das aktuelle Datum für diesen Segmentierungsfilter gezählt.
  - Wenn Sie zum Beispiel am 10. März 2020 das Datum des Attributs `LESS THAN ... March 10, 2020` ausgewählt haben, werden die Attribute für die Tage bis einschließlich 10. März 2020 berücksichtigt. 
- Vor weniger als X Tagen: Der Filter „Vor weniger als X Tagen" schließt Daten ein, die zwischen X Tagen in der Vergangenheit und dem aktuellen Datum/der aktuellen Uhrzeit liegen.
- Weniger als X Tage in der Zukunft: Enthält Daten zwischen dem aktuellen Datum/der aktuellen Uhrzeit und X Tagen in der Zukunft.

### Objekte

Sie können verschachtelte angepasste Attribute verwenden, um Objekte als Datentyp für angepasste Attribute zu senden. Weitere Informationen finden Sie unter [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/).

### Arrays von Objekten

Verwenden Sie ein Array von Objekten, um verwandte Attribute zu gruppieren. Weitere Einzelheiten finden Sie in unserem Artikel über [Array von Objekten]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/).

### Konsolidierte Operatoren

Wir haben die Liste der Operatoren konsolidiert, die in Attributfiltern, angepassten Attributfiltern und verschachtelten angepassten Attributfiltern verfügbar sind. Wenn Sie bereits Filter haben, die diese Operatoren verwenden, werden diese automatisch aktualisiert, um die neuen Operatoren zu verwenden.

| Datentyp | Alter Operator | Neuer Operator | Wert |
| --- | --- | --- | --- |
| String | ist gleich | ist eines von | Mindestens 1 Wert |
| String | ist nicht gleich | ist keines von | Mindestens 1 Wert |
| Array | enthält einen Wert | enthält eines von | Mindestens 1 Wert |
| Array | enthält keinen Wert | enthält keines von | Mindestens 1 Wert |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Tracking von Käufen und Umsatz {#purchase-revenue-tracking}

Mit unseren Kaufmethoden zur Erfassung von In-App-Käufen wird der Lifetime-Value (LTV) für jedes einzelne Nutzerprofil ermittelt. Diese Daten können Sie auf unserer Umsatzseite in Zeitreihen einsehen.

| Segmentierungsoptionen | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen, ob die Gesamtsumme der Ausgaben **größer als** eine **Zahl** ist| **GREATER THAN** | **NUMBER** | Wenn dieser Filter `500` angibt und ein Nutzerprofil einen Wert größer als `500` hat, wird der/die Nutzer:in diesem Filter entsprechen. |
| Prüfen, ob die Gesamtsumme der Ausgaben **weniger als** eine **Zahl** ist| **LESS THAN** | **NUMBER** | Wenn dieser Filter `500` angibt und ein Nutzerprofil einen Wert kleiner als `500` hat, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob die Gesamtsumme der Ausgaben **genau** einer **Zahl** entspricht| **EXACTLY** | **NUMBER** | Wenn dieser Filter `500` angibt und ein Nutzerprofil den Wert `500` hat, wird der/die Nutzer:in diesem Filter entsprechen. |
| Prüfen, ob der letzte Kauf **nach dem Datum X** stattgefunden hat | **AFTER** | **TIME** | Wenn dieser Filter `2024/31/1` angibt und der letzte Kauf eines Nutzers/einer Nutzerin nach `2024/31/1` stattfand, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob der letzte Kauf **vor dem Datum X** stattgefunden hat | **BEFORE** | **TIME** | Wenn dieser Filter `2024/31/1` angibt und der letzte Kauf eines Nutzers/einer Nutzerin vor `2024/31/1` lag, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob der letzte Kauf **mehr als X Tage zurückliegt** | **MORE THAN** | **TIME** | Wenn dieser Filter `7` angibt und der letzte Kauf eines Nutzers/einer Nutzerin mehr als sieben Tage zurückliegt, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob der letzte Kauf **weniger als X Tage zurückliegt** | **LESS THAN** | **TIME** |  Wenn dieser Filter `7` angibt und der letzte Kauf eines Nutzers/einer Nutzerin weniger als sieben Tage zurückliegt, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob der Kauf **mehr als X (Max = 50) Mal** stattgefunden hat | **MORE THAN** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |  Wenn dieser Filter `7` Mal und `21` Tage angibt und ein:e Nutzer:in in den letzten 21 Tagen mehr als sieben Käufe getätigt hat, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob der Kauf **weniger als X (Max = 50) Mal** stattgefunden hat | **LESS THAN** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** | Wenn dieser Filter `7` Mal und `21` Tage angibt und ein:e Nutzer:in in den letzten 21 Tagen weniger als sieben Käufe getätigt hat, wird der/die Nutzer:in diesem Filter entsprechen.|
| Prüfen, ob der Kauf **genau X (Max = 50) Mal** stattgefunden hat | **EXACTLY** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** | Wenn dieser Filter `7` Mal und `21` Tage angibt und ein:e Nutzer:in in den letzten 21 Tagen sieben Käufe getätigt hat, wird der/die Nutzer:in diesem Filter entsprechen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Wenn Sie nach der Häufigkeit eines bestimmten Kaufs segmentieren möchten, sollten Sie diesen Kauf auch einzeln als [inkrementelles angepasstes Attribut]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes) erfassen.
{% endalert %}

Sie können den Datentyp Ihres angepassten Attributs ändern, sollten sich aber über die Auswirkungen einer [Änderung des Datentyps]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) im Klaren sein.