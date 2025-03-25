---
nav_title: Angepasste Attribute
article_title: Angepasste Attribute
page_order: 10
page_type: reference
description: "Dieser Referenzartikel beschreibt benutzerdefinierte Attribute und erläutert die verschiedenen Datentypen für benutzerdefinierte Attribute."
search_rank: 1
---

# [![Braze Learning Kurs]](https://learning.braze.com/custom-events-and-attributes) ( [{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}Benutzerdefinierte Attribute

> Benutzerdefinierte Attribute sind eine Sammlung der einzigartigen Eigenschaften Ihrer Benutzer. Benutzerdefinierte Attribute eignen sich am besten zum Speichern von Attributen über Ihre Benutzer oder von Informationen über geringwertige Aktionen innerhalb Ihrer Anwendung. 

Wenn diese Merkmale in Braze gespeichert sind, können sie dazu verwendet werden, Segmente für die Zielgruppe zu erstellen und Nachrichten mit Liquid zu personalisieren. Sie sollten bedenken, dass wir für angepasste Attribute keine Zeitreiheninformationen speichern, sodass Sie keine darauf basierenden Diagramme wie für angepasste Events erhalten können.

## Benutzerdefinierte Attribute verwalten

Um angepasste Attribute im Dashboard zu erstellen und zu verwalten, gehen Sie zu **Dateneinstellungen** > Angepasste Attribute. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Benutzerdefinierte Attribute** unter **Einstellungen verwalten**.
{% endalert %}

![Vier angepasste Attribute, die boolesch sind.]({% image_buster /assets/img/export_custom_attributes.png %})

Die Spalte **Letzte Aktualisierung** listet das letzte Mal auf, als das benutzerdefinierte Attribut bearbeitet wurde, z.B. als es zuletzt auf Blockliste oder aktiv gesetzt wurde. 

Auf dieser Seite können Sie vorhandene benutzerdefinierte Attribute anzeigen, verwalten, erstellen oder blockieren. Wählen Sie das Menü neben einem angepassten Attribut für die folgenden Aktionen aus:

### Wird auf Sperrliste gesetzt ...

Angepasste Attribute können einzeln über das Aktionsmenü gesperrt werden, oder es können bis zu 10 Attribute ausgewählt und in einer Liste gesperrt werden. Wenn Sie ein benutzerdefiniertes Attribut blockieren, werden keine Daten zu diesem Attribut gesammelt, vorhandene Daten sind nicht verfügbar, es sei denn, sie werden wieder aktiviert, und blockierte Attribute werden nicht in Filtern oder Diagrammen angezeigt. Wenn das Attribut derzeit von Filtern oder Auslösern in anderen Bereichen des Braze Dashboards referenziert wird, erscheint außerdem ein Warnmodal, in dem erklärt wird, dass alle Instanzen der Filter oder Auslöser, die darauf verweisen, entfernt und archiviert werden.

### Markierung als PII

Administratoren können auf dieser Seite auch benutzerdefinierte Attribute erstellen und sie als PII markieren. Diese Attribute sind nur für Administratoren und Dashboard-Benutzer mit der Berechtigung "Als PII markierte benutzerdefinierte Attribute anzeigen" sichtbar.

### Hinzufügen von Beschreibungen

Sie können einem angepassten Attribut eine Beschreibung hinzufügen, nachdem es erstellt wurde, wenn Sie über die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) `Manage Events, Attributes, Purchases` verfügen. Bearbeiten Sie das angepasste Attribut und geben Sie ein, was immer Sie möchten, z.B. eine Notiz für Ihr Team.

### Hinzufügen von Tags

Sie können Tags zu einem angepassten Attribut hinzufügen, nachdem es erstellt wurde, wenn Sie über die [Nutzerberechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) „Events, Attribute, Einkäufe verwalten“ verfügen. Die Tags können dann zum Filtern der Liste der Attribute verwendet werden. 

{% alert important %}
Dieses Feature befindet sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Customer Success Manager, wenn Sie an einem Vorabzugang interessiert sind.
{% endalert %}

### Entfernen von benutzerdefinierten Attributen

Es gibt zwei Möglichkeiten, wie Sie angepasste Attribute aus Nutzerprofilen entfernen können:

* Wählen Sie den Namen des angepassten Attributs aus, das in einem [Update-Schritt für Nutzer:innen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#removing-custom-attributes) entfernt werden soll.
* Setzen Sie den Wert `null` in Ihrer API-Anfrage auf den `/users/track`-[Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track#user-track).

### Nutzungsberichte anzeigen

Der Nutzungsbericht listet alle Canvases, Kampagnen und Segmente auf, die ein bestimmtes benutzerdefiniertes Attribut verwenden. Diese Liste enthält nicht die Verwendung von Liquid. 

Sie können bis zu 10 Nutzungsberichte auf einmal anzeigen, indem Sie die Kontrollkästchen neben den jeweiligen benutzerdefinierten Attributen aktivieren und dann **Nutzungsbericht anzeigen** wählen.

### Exportieren von Daten

Um die Liste der angepassten Attribute als CSV-Datei zu exportieren, wählen Sie oben auf der Seite **Alle exportieren**. Die CSV-Datei wird generiert, und ein Download-Link wird Ihnen per E-Mail zugesandt.

## Anpassen der Attribute

Im Folgenden finden Sie eine Liste von Methoden für verschiedene Plattformen, mit denen Sie angepasste Attribute festlegen können.

{% details Erweitern, um die Dokumentation für einzelne Plattformen anzuzeigen %}

- [Android und FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/)
- [Internet]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-custom-attributes)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/setting_custom_attributes/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#setting-custom-attributes)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_custom_attributes/)

{% enddetails %}

## Angepasste Attribute speichern

Alle im **Nutzerprofil** gespeicherten Daten, einschließlich der Daten zu angepassten Attributen, werden auf unbestimmte Zeit gespeichert, solange das jeweilige Profil [aktiv]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#active-users) ist.

## Angepasste Attribut-Datenarten

Angepasste Attribute sind außerordentlich flexible Tools, die ein hervorragendes Targeting ermöglichen.

Die folgenden Datenarten können als angepasste Attribute gespeichert werden:

- [Boolesche Werte](#booleans)
- [Zahlen](#numbers)
- [Strings](#strings)
- [Arrays](#arrays)
- [Uhrzeit](#time)
- [Objekte]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/)
- [Arrays von Objekten]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/)

### Boolesche Werte (wahr/falsch) {#booleans}

Boolesche Attribute sind nützlich, um einfache binäre Daten über Ihre Nutzer:innen zu speichern, wie z.B. den Status von Abonnements. Sie können Nutzer:innen finden, bei denen eine Variable explizit auf den Wert "wahr" oder "falsch" gesetzt ist, sowie Nutzer:innen, bei denen dieses Attribut noch nicht aufgezeichnet wurde.

| Möglichkeiten der Segmentierung | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen Sie, ob der boolesche Wert entweder wahr, falsch, wahr oder nicht gesetzt oder falsch oder nicht gesetzt **ist**. | **IST**  | **TRUE**, **FALSE**, **TRUE OR NOT SET**, oder **FALSE OR NOT SET** | Wenn dieser Filter `coffee_drinker` angibt, wird ein:e Nutzer:in den folgenden Fällen mit diesem Filter übereinstimmen: <br> {::nomarkdown}<ul><li>Wenn dieser Filter <code>true</code> und der Nutzer:innen hat den Wert <code>coffee_drinker</code></li><li>Wenn dieser Filter <code>false</code> und der Nutzer:in hat nicht den Wert <code>coffee_drinker</code></li><li>Wenn dieser Filter <code>true or not set</code> und der Nutzer:innen hat den Wert <code>coffee_drinker</code> oder kein Wert</li><li>Wenn dieser Filter <code>false or not set</code> und der Nutzer:in hat nicht <code>coffee_drinker</code> oder einen beliebigen Wert</li></ul>{:/} |
| Prüfen Sie, ob der boolesche Wert im Profil eines Nutzers oder einer Nutzerin **existiert** und nicht null ist. | **IST NICHT LEER**  | **--** | Wenn dieser Filter `coffee_drinker` angibt und ein Nutzer:innen einen Wert für das Attribut `coffee_drinker` hat, wird der Nutzer:innen diesem Filter entsprechen. | 
| Prüfen Sie, ob der boolesche Wert im Profil eines Nutzers oder einer Nutzerin **nicht existiert** oder null ist. | **IST LEER**  | **--** | Wenn dieser Filter `coffee_drinker`angibt und ein Nutzer:innen entweder nicht über das Attribut `coffee_drinker` verfügt oder der Wert für `coffee_drinker` null ist, wird der Nutzer:innen diesem Filter entsprechen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Zahlen {#numbers}

Numerische Attribute umfassen [Ganzzahlen](https://en.wikipedia.org/wiki/Integer) und [Gleitkommazahlen](https://en.wikipedia.org/wiki/Floating-point_arithmetic) und haben eine Vielzahl von Anwendungsfällen. Angepasste Attribute mit inkrementeller Anzahl sind nützlich, um zu speichern, wie oft eine bestimmte Aktion oder ein bestimmtes Event stattgefunden hat, ohne dass dies auf Ihre Daten angerechnet wird. Standardnummern haben alle möglichen Verwendungszwecke, wie z.B. die Aufzeichnung:

- Schuhgröße
- Taillenumfang
- Anzahl der Nutzer:innen, die ein bestimmtes Produkt Feature oder eine Kategorie angesehen haben

{% alert tip %}
Das ausgegebene Geld sollte nicht auf diese Weise erfasst werden. Vielmehr sollte es über unsere [Kaufmethoden](#purchase-revenue-tracking) erfasst werden.
{% endalert %}

| Möglichkeiten der Segmentierung | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen Sie, ob das numerische Attribut **exakt** eine **Zahl** ist| **EXAKT** | **ZAHL** | Wenn dieser Filter `10` angibt und ein Nutzerprofil den Wert `10` hat, wird der oder die Nutzer:in diesem Filter berücksichtigt. |
| Prüfen Sie, ob das numerische Attribut **nicht exakt** einer **Zahl** entspricht.| **IST NICHT GLEICHBEDEUTEND MIT** | **ZAHL** | Wenn dieser Filter `10` angibt und ein Nutzerprofil nicht den Wert `10` hat, wird der Nutzer:innen diesem Filter entsprechen. |
| Prüfen Sie, ob das numerische Attribut **mehr als** eine **Zahl** ist.| **MEHR ALS** | **ZAHL** | Wenn dieser Filter `10` angibt und ein Nutzerprofil einen Wert hat, der größer als `10` ist, wird der Nutzer:innen diesem Filter entsprechen. |
| Prüfen Sie, ob das numerische Attribut **weniger als** eine **Zahl** ist.| **WENIGER ALS** | **ZAHL** | Wenn dieser Filter `10` angibt und ein Nutzerprofil einen Wert kleiner als `10` hat, wird der Nutzer:innen diesem Filter entsprechen. |
| Prüfen Sie, ob das numerische Attribut im Profil eines Nutzers oder einer Nutzerin **existiert** und nicht null ist. | **IST NICHT LEER** | **--** | Wenn ein Nutzerprofil das angegebene numerische Attribut enthält, unabhängig vom Wert, wird der Nutzer:innen diesem Filter entsprechen. |
| Prüfen Sie, ob das numerische Attribut im Profil eines Nutzers oder einer Nutzerin **nicht existiert** oder null ist. | **IST LEER** | **--** | Wenn ein Nutzerprofil das angegebene numerische Attribut nicht enthält oder der Wert des Attributs Null ist, entspricht der Nutzer:innen diesem Filter.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Nummer Attribut Details

- Die Filter "Genau 0" und "Kleiner als" schließen Nutzer:innen mit NULL-Feldern ein.
  - Um Nutzer:innen ohne einen Wert für angepasste Attribute auszuschließen, müssen Sie den Filter **is not blank** einfügen.

### Strings (alphanumerische Zeichen) {#strings}

String-Attribute sind nützlich, um Nutzereingaben zu speichern, z. B. eine Lieblingsmarke, eine Telefonnummer oder einen letzten Suchstring in Ihrer Anwendung. String Attribute können bis zu 255 Zeichen lang sein.

Beachten Sie, dass Braze bei der Eingabe von Werten, die Leerzeichen zwischen, vor oder nach Wörtern enthalten, auch auf diese Leerzeichen prüft.

| Möglichkeiten der Segmentierung | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen Sie, ob das String-Attribut mit einem eingegebenen String **exakt übereinstimmt**.| **IST GLEICH** | **STRING**<br>Groß-/Kleinschreibung beachten | Wenn dieser Filter `book` angibt und ein Nutzerprofil ein String-Attribut für `last_item_purchased` hat, das `book` enthält, wird der Nutzer:in diesem Filter berücksichtigt. |
| Prüfen Sie, ob das String-Attribut mit einem eingegebenen String **ODER** einem regulären Ausdruck **teilweise übereinstimmt**. | **STIMMT MIT REGEX ÜBEREIN** | **STRING** **ODER** **REGEX** <br>Groß- und Kleinschreibung wird nicht unterschieden; maximal 32.764 Zeichen | 
| Prüfen Sie, ob das String-Attribut mit einem eingegebenen String **ODER** regulären Ausdruck **nicht teilweise übereinstimmt**. | **STIMMT NICHT MIT REGEX** ÜBEREIN \* | **STRING** **ODER** **REGEX**<br>Groß- und Kleinschreibung wird nicht unterschieden; maximal 32.764 Zeichen |
| Prüfen Sie, ob das String-Attribut mit einem eingegebenen String **nicht übereinstimmt**.| **IST NICHT GLEICHBEDEUTEND MIT** | **STRING**<br>Keine Unterscheidung zwischen Groß- und Kleinschreibung  | Wenn dieser Filter `book` angibt und ein Nutzerprofil ein String-Attribut für `last_item_purchased` hat, das nicht `book` enthält, wird der Nutzer:in diesem Filter berücksichtigt.|
| Prüfen Sie, ob das String-Attribut im Profil eines Nutzers oder einer Nutzerin **existiert** und kein leerer String ist. | **IST NICHT LEER** | **--** | Wenn dieser Filter `favorite_genre` angibt und ein Nutzerprofil das Attribut `favorite_genre` hat, wird der Nutzer:innen unabhängig von seinem Attributwert diesem Filter entsprechen. Der oder die Nutzer:in kann zum Beispiel `sci-fi`, `romance` oder einen anderen Wert haben.|
| Prüfen Sie, ob das String-Attribut im Profil eines Nutzers oder einer Nutzerin **nicht existiert**. | **LEER** | **--** | Wenn dieser Filter `favorite_genre` angibt und ein Nutzerprofil nicht über das Attribut `favorite_genre` verfügt, wird der Nutzer:innen diesem Filter entsprechen.|
| Prüfen Sie, ob der String genau mit **einem der** eingegebenen Strings übereinstimmt. | **IST EINES VON** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings zulässig (maximal 256) | Wenn dieser Filter `book`, `bookmark` und `reading light` angibt und ein Nutzerprofil mindestens einen dieser Strings enthält, wird der Nutzer:innen diesem Filter entsprechen. |
| Prüfen Sie, ob das String-Attribut **nicht exakt mit einem** der eingegebenen Strings übereinstimmt. | **IST KEINES VON** |**STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings zulässig (maximal 256) | Wenn dieser Filter `book`, `bookmark` und `reading light` angibt und ein Nutzerprofil keinen dieser Strings enthält, wird der Nutzer:innen dem Filter entsprechen.|
| Prüfen Sie, ob das String-Attribut **teilweise mit einem der** eingegebenen Strings übereinstimmt. | **ENTHÄLT EINE DER** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings zulässig (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil `gold` in einem beliebigen String enthält, wie z.B. `gold_tier` oder `former_gold_tier`, wird der Nutzer:innen dem Filter entsprechen. |
| Prüfen Sie, ob das String-Attribut **nicht teilweise mit einem** der eingegebenen Strings übereinstimmt. | **ENTHÄLT KEINE DER** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Strings zulässig (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil in keinem String `gold` enthält, wird der Nutzer:in diesem Filter berücksichtigt.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Ein Datums-String wie "12-1-2021" oder "12/1/2021" wird in ein Datetime-Objekt umgewandelt und als [Attribut für die Zeit]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#time) behandelt.
{% endalert %}

{% alert important %}
Wenn Sie mit dem Filter **DOES NOT MATCH REGEX** segmentieren, müssen Sie bereits ein angepasstes Attribut mit einem Wert in diesem Nutzerprofil zugewiesen haben. Braze schlägt vor, mit "OR"-Logik zu prüfen, ob ein angepasstes Attribut leer ist, um sicherzustellen, dass die Nutzer:innen richtig targetiert werden.
{% endalert %}

### Arrays {#arrays}

Array-Attribute sind gut geeignet, um zusammenhängende Listen mit Informationen über Ihre Nutzer:innen zu speichern. Wenn Sie zum Beispiel die letzten 100 Inhalte, die ein Nutzer:innen gesehen hat, in einem Array speichern, ist eine Segmentierung nach Interessen zulässig.

Standardmäßig ist die maximale Länge eines Arrays für ein Attribut auf 25 festgelegt und kann für ein individuelles Array auf 100 erhöht werden. Wenn Sie z.B. ein Attribut wie "Movies Watched" übermitteln und es auf 100 gesetzt ist, wird, wenn ein Nutzer:innen den 101\. Film ansieht, der erste Film aus dem Array entfernt und der neueste Film hinzugefügt.

Wenn Sie dieses Maximum erhöhen möchten, wenden Sie sich an Ihren Customer-Success-Manager:in. Ihr Dashboard-Administrator kann dann auf der Registerkarte **Benutzerdefinierte Attribute** auf der Seite **Einstellungen verwalten** die maximale Länge für einzelne Arrays auf über 100 erhöhen.

Beachten Sie, dass Braze bei der Eingabe von Werten, die Leerzeichen zwischen, vor oder nach Wörtern enthalten, auch auf diese Leerzeichen prüft.

{% alert note %}
Die Option zum Erhöhen der maximalen Länge ist nicht verfügbar, wenn das Attribut so eingestellt ist, dass der Datentyp automatisch erkannt wird; der Datentyp muss auf Array eingestellt sein.
{% endalert %}

| Möglichkeiten der Segmentierung | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen Sie, ob das Array-Attribut einen Wert enthält, der mit einem eingegebenen Wert **exakt übereinstimmt**.| **ENTHÄLT EINEN WERT** | **STRING** | Wenn dieser Filter `sci-fi` angibt und ein Nutzerprofil den Wert `sci-fi` hat, wird der oder die Nutzer:in diesem Filter berücksichtigt.|
| Prüfen Sie, ob das Array-Attribut einen Wert enthält, der mit einem eingegebenen Wert **nicht exakt übereinstimmt**.| **ENTHÄLT KEINEN WERT** | **STRING** | Wenn dieser Filter `sci-fi` angibt und ein Nutzerprofil nicht den Wert `sci-fi` hat, wird der Nutzer:innen diesem Filter entsprechen.|
| Prüfen Sie, ob das Array-Attribut einen Wert enthält, der mit einem eingegebenen Wert **ODER** regulären Ausdruck **teilweise übereinstimmt**. | **STIMMT MIT REGEX ÜBEREIN** | **STRING** **ODER** **REGEX**<br>Maximal 32.764 Zeichen | |
| Prüfen Sie, ob das Array-Attribut **einen Wert hat** oder nicht leer ist | **HAT EINEN WERT** | **--** | Wenn dieser Filter `favorite_genres` angibt und ein Nutzerprofil `favorite_genres` mit einem beliebigen Wert enthält, entspricht der Nutzer:innen diesem Filter. |
| Prüfen Sie, ob das Array-Attribut **leer ist** oder nicht existiert | **IST LEER** | **--** | Wenn dieser Filter `favorite_genres` angibt und ein Nutzerprofil `favorite_genres` nicht enthält oder `favorite_genres` enthält, aber keine Werte enthält, wird der Nutzer:innen diesem Filter entsprechen.|
| Prüfen Sie, ob das Array-Attribut **einen Wert enthält, der exakt mit einem der** eingegebenen Werte übereinstimmt. | **UMFASST EINE DER** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte zulässig (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil eine beliebige Kombination von `sci-fi`, `fantasy` oder `romance` enthält, einschließlich nur einer dieser Kombinationen (z.B. nur `sci-fi`). Ein:e Nutzer:in kann `horror` oder einen anderen Wert in seinem oder ihrem String haben, wenn er oder sie auch einen der Werte `sci-fi`, `fantasy` und `romance` hat.|
| Prüfen Sie, ob das Array-Attribut **einen Wert enthält, der nicht exakt mit einem** der eingegebenen Werte übereinstimmt. | **ENTHÄLT KEINE DER** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte zulässig (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil keine Kombination von `sci-fi`, `fantasy` oder `romance` enthält, entspricht der Nutzer:innen diesem Filter. Der Nutzer:innen kann `horror` oder einen anderen Wert haben, wenn er keinen der Werte `sci-fi`, `fantasy` oder `romance` hat.|
| Prüfen Sie, ob das Array-Attribut **einen Wert enthält, der teilweise mit einem der** eingegebenen Werte übereinstimmt | **WERTE ENTHALTEN EINE DER** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte zulässig (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil-Array `gold` in mindestens einem String enthält, wird der Nutzer:in diesem Filter berücksichtigt. Dazu gehören String-Werte wie `gold_tier`, `former_gold_tier`, und andere.|
| Prüfen Sie, ob das Array-Attribut **keinen Wert enthält, der teilweise mit einem** der eingegebenen Werte übereinstimmt. | **WERTE ENTHALTEN KEINE DER** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte zulässig (maximal 256) | Wenn dieser Filter `gold` angibt und ein Nutzerprofil-Array in keinem String `gold` enthält, wird der Nutzer:in diesem Filter berücksichtigt. Das bedeutet, dass Nutzer:innen mit String-Werten wie `gold_tier` und `former_gold_tier` nicht auf diesen Filter zutreffen.|
| Prüfen Sie, ob das Array-Attribut **alle** eingegebenen Werte enthält | **IST ALLES VON** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte zulässig (maximal 256) | Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil alle diese Werte aufweist, entspricht der Nutzer:innen diesem Filter. Der Nutzer:innen kann auch `horror` oder andere Werte haben und diesem Filter entsprechen.|
| Prüfen Sie, ob das Array-Attribut **nicht alle** eingegebenen Werte enthält | **IST NICHT ALLES VON** | **STRING**<br>Groß-/Kleinschreibung beachten; mehrere Werte zulässig (maximal 256)|  Wenn dieser Filter `sci-fi, fantasy, romance` angibt und ein Nutzerprofil nicht alle diese Werte enthält, wird der Nutzer:innen diesem Filter entsprechen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Wenn Sie mehr über die Verwendung regulärer Ausdrücke (Regex) erfahren möchten, lesen Sie diese Ressourcen:
- [Perl-kompatible reguläre Ausdrücke (PCRE)](https://www.regextester.com/pregsyntax.html)
- [Regex mit Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Regex Debugger und Tester](https://www.regex101.com/)
- [Regex-Tutorial](https://www.medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

### Zeit {#time}

Zeitattribute sind nützlich, um zu speichern, wann eine bestimmte Aktion das letzte Mal durchgeführt wurde, damit Sie Ihren Nutzer:innen inhaltsspezifische Nachrichten zur erneuten Interaktion anbieten können.

Zeitfilter, die relative Datumsangaben verwenden (z. B. vor mehr als einem Tag, vor weniger als zwei Tagen), messen einen Tag als 24 Stunden. Jede Kampagne, die Sie mit diesen Filtern durchführen, schließt alle Nutzer:innen in 24-Stunden-Schritten ein. Zum Beispiel wird `last used app more than 1 day ago` alle Nutzer:innen erfassen, die "die App zuletzt mehr als 24 Stunden" ab dem genauen Zeitpunkt der Kampagne genutzt haben. Dasselbe gilt für Kampagnen mit längeren Datumsbereichen - fünf Tage nach der Aktivierung sind also die letzten 120 Stunden.

Um beispielsweise ein Segment zu erstellen, das auf Nutzer:innen mit einem zeitlichen Attribut zwischen 24 und 48 Stunden in der Zukunft abzielt, wenden Sie die Filter `in more than 1 day in the future` und `in less than 2 days in the future` an.

{% alert warning %}
Das letzte Datum, an dem ein angepasstes Event oder ein Kauf-Event stattgefunden hat, wird automatisch aufgezeichnet und sollte nicht erneut über ein angepasstes Zeitattribut aufgezeichnet werden.
{% endalert %}

| Möglichkeiten der Segmentierung | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen Sie, ob das Zeit-Attribut **vor** einem **ausgewählten Datum** liegt.| **BEVOR** | **KALENDERAUSWAHL** | Wenn dieser Filter `2024-01-31` angibt und ein Nutzerprofil ein Datum vor `2024-1-31` hat, wird der Nutzer:in diesem Filter berücksichtigt. |
| Prüfen Sie, ob das Zeit-Attribut **nach** einem **ausgewählten Datum** liegt.| **NACH** | **KALENDERAUSWAHL** | Wenn dieser Filter `2024-01-31` angibt und ein Nutzerprofil ein Datum nach `2024-1-31` hat, wird der Nutzer:in diesem Filter berücksichtigt. |
| Prüfen Sie, ob das Zeit-Attribut **mehr als** **X Tage zurückliegt**. | **MEHR ALS** | **ANZAHL DER TAGE IN DER VERGANGENHEIT** | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das mehr als sieben Tage zurückliegt, wird der Nutzer:in diesem Filter berücksichtigt. |
| Prüfen Sie, ob das Zeit-Attribut **weniger als** **X Tage zurückliegt**.| **WENIGER ALS** | **ANZAHL DER TAGE IN DER VERGANGENHEIT** | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das weniger als sieben Tage zurückliegt, wird der Nutzer:in diesem Filter berücksichtigt.|
| Prüfen Sie, ob das Zeit-Attribut **mehr als** **X Tage in der Zukunft liegt**. | **IN MEHR ALS** | **ANZAHL DER TAGE IN DER ZUKUNFT** | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das mehr als sieben Tage in der Zukunft liegt, wird der Nutzer:in diesem Filter berücksichtigt.|
| Prüfen Sie, ob das Zeit-Attribut **weniger als** **X Tage in der Zukunft liegt**. | **IN WENIGER ALS** | **ANZAHL DER TAGE IN DER ZUKUNFT**  | Wenn dieser Filter `7` angibt und ein Nutzerprofil ein Datum hat, das weniger als sieben Tage in der Zukunft liegt, wird der Nutzer:in diesem Filter berücksichtigt.|
| Prüfen Sie, ob das Zeit-Attribut im Profil eines Nutzers oder einer Nutzerin **existiert** und nicht null ist. | **IST NICHT LEER** | **--** | Wenn dieser Filter ein Zeitattribut angibt, das sich in einem Nutzerprofil befindet, wird der Nutzer:innen diesem Filter entsprechen.|
| Prüfen Sie, ob das Zeit-Attribut im Profil eines Nutzers oder einerr Nutzerin **nicht existiert** oder null ist | **IST LEER** | **--** | Wenn dieser Filter ein Zeitattribut angibt, das sich nicht in einem Nutzerprofil befindet, wird der Nutzer:innen diesem Filter entsprechen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

#### Details zum Zeitattribut

- Tag des wiederkehrenden Events
  - Wenn Sie den Filter „Tag des wiederkehrenden Events“ verwenden und dann aufgefordert werden, den „Kalendertag des wiederkehrenden Events“ auszuwählen, wird bei Auswahl von `IS LESS THAN` oder `IS MORE THAN` das aktuelle Datum für diesen Segmentierungsfilter gezählt.
  - Wenn Sie zum Beispiel am 10\. März 2020 das Datum des Attributs `LESS THAN ... March 10, 2020` ausgewählt haben, werden die Attribute für die Tage bis einschließlich 10. März 2020 berücksichtigt. 
- Vor weniger als X Tagen: Der Filter "Vor weniger als X Tagen" schließt Daten ein, die zwischen X Tagen vor und dem aktuellen Datum/Uhrzeit liegen.
- Weniger als X Tage in der Zukunft: Enthält Daten zwischen dem aktuellen Datum/Uhrzeit und X Tagen in der Zukunft.

### Objekte

Sie können verschachtelte angepasste Attribute verwenden, um Objekte als Datentyp für angepasste Attribute zu senden. Weitere Informationen finden Sie unter [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/).

### Arrays von Objekten

Verwenden Sie ein Array von Objekten, um verwandte Attribute zu gruppieren. Weitere Einzelheiten finden Sie in unserem Artikel über [Array von Objekten]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects/).

### Konsolidierte Operatoren

Wir haben die Operatoren für Attributfilter, angepasste Attributfilter und verschachtelte angepasste Attributfilter in einer Liste zusammengefasst. Wenn Sie bereits Filter haben, die diese Operatoren verwenden, werden diese automatisch aktualisiert, um die neuen Operatoren zu verwenden.

| Datentyp | Alter Operator | Neuer Operator | Wert |
| --- | --- | --- | --- |
| String | ist gleich | ist eines von | Mindestens 1 Wert |
| String | ist nicht gleich | ist keines von | Mindestens 1 Wert |
| Array | enthält einen Wert | enthält eines von | Mindestens 1 Wert |
| Array | enthält keinen Wert | enthält keines von | Mindestens 1 Wert |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Tracking von Käufen und Einnahmen {#purchase-revenue-tracking}

Mit unseren Kaufmethoden zur Erfassung von In-App-Käufen wird der Lifetime-Value (LTV) für jedes einzelne Nutzerprofil ermittelt. Diese Daten können Sie auf unserer Umsatzseite in Zeitserien einsehen.

| Möglichkeiten der Segmentierung | Dropdown-Filter | Eingabeoptionen | Beispiele |
| ---------------------| --------------- | ------------- | -------- |
| Prüfen Sie, ob die Gesamtzahl der ausgegebenen Summe **größer als** eine **Zahl** ist| **GRÖSSER ALS** | **ZAHL** | Wenn dieser Filter `500` angibt und ein Nutzerprofil einen Wert hat, der größer als `500` ist, wird der Nutzer:innen diesem Filter entsprechen. |
| Prüfen Sie, ob die Gesamtzahl der ausgegebenen Summe **weniger als** eine **Zahl** ist| **WENIGER ALS** | **ZAHL** | Wenn dieser Filter `500` angibt und ein Nutzerprofil einen Wert kleiner als `500` hat, wird der Nutzer:innen diesem Filter entsprechen.|
| Prüfen Sie, ob die Gesamtzahl der ausgegebenen Dollar **genau** eine **Zahl** **ist** | **EXAKT** | **ZAHL** | Wenn dieser Filter `500` angibt und ein Nutzerprofil den Wert `500` hat, wird der oder die Nutzer:in diesem Filter berücksichtigt. |
| Prüfen Sie, ob der letzte Kauf **nach dem Datum X** stattgefunden hat | **NACH** | **TIME** | Wenn dieser Filter `2024/31/1` angibt und der letzte Kauf eines Nutzers nach `2024/31/1` stattfand, passt der Nutzer:innen auf diesen Filter.|
| Prüfen Sie, ob der letzte Kauf **vor dem Datum X** stattgefunden hat | **BEVOR** | **TIME** | Wenn dieser Filter `2024/31/1` angibt und der letzte Kauf eines Nutzers vor `2024/31/1` lag, entspricht der Nutzer:innen diesem Filter.|
| Prüfen Sie, ob der letzte Kauf **mehr als X Tage zurückliegt** | **MEHR ALS** | **TIME** | Wenn dieser Filter `7` angibt und der letzte Kauf eines Nutzers:innen mehr als sieben Tage zurückliegt, wird der Nutzer:innen diesem Filter entsprechen.|
| Prüfen Sie, ob der letzte Kauf **weniger als X Tage zurückliegt** | **WENIGER ALS** | **TIME** |  Wenn dieser Filter `7` angibt und der letzte Kauf eines Nutzers:innen weniger als sieben Tage zurückliegt, wird der Nutzer:innen diesem Filter entsprechen.|
| Prüfen Sie, ob der Kauf **mehr als X (Max = 50) Mal** stattgefunden hat | **MEHR ALS** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |  Wenn dieser Filter `7` Zeiten und `21` Tage angibt und ein Nutzer:innen in den letzten 21 Tagen mehr als sieben Einkäufe getätigt hat, wird der Nutzer:innen diesem Filter entsprechen.|
| Prüfen Sie, ob der Kauf **weniger als X (Max = 50) Mal** stattgefunden hat | **WENIGER ALS** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** | Wenn dieser Filter `7` Zeiten und `21` Tage angibt und ein Nutzer:innen in den letzten 21 Tagen weniger als sieben Einkäufe getätigt hat, wird der Nutzer:innen diesem Filter entsprechen.|
| Prüfen Sie, ob der Kauf **exakt X (Max = 50) Mal** stattgefunden hat | **EXAKT** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** | Wenn dieser Filter `7` Zeiten und `21` Tage angibt und ein Nutzer:innen in den letzten 21 Tagen sieben Einkäufe getätigt hat, wird der Nutzer:innen diesem Filter entsprechen.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert tip %}
Wenn Sie nach der Häufigkeit eines bestimmten Kaufs segmentieren möchten, sollten Sie diesen Kauf auch einzeln als [inkrementelles angepasstes Attribut]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/#incrementingdecrementing-custom-attributes) erfassen.
{% endalert %}

Sie können den Datentyp Ihres angepassten Attributs ändern, sollten sich aber über die Auswirkungen einer [Änderung des Datentyps]({{site.baseurl}}/help/help_articles/data/change_custom_data_type/) im Klaren sein.

