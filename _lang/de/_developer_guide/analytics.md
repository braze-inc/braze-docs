---
nav_title: Analytics
article_title: Über Analytics für das Braze SDK
page_order: 2.6
description: "Erfahren Sie mehr über die Analytics des Braze SDK, damit Sie besser verstehen, welche Daten Braze sammelt, was der Unterschied zwischen angepassten Events und angepassten Attributen ist und wie Sie Analytics am besten verwalten."
platform: 
  - Android
  - Swift
  - Web
  - Cordova
  - FireOS
  - Flutter
  - React Native
  - Roku
  - Unity
  - Unreal Engine
  - Xamarin
---

# Analytics

> Erfahren Sie mehr über die Analytics des Braze SDK, damit Sie besser verstehen, welche Daten Braze sammelt, was der Unterschied zwischen angepassten Events und angepassten Attributen ist und wie Sie Analytics am besten verwalten.

{% alert tip %}
Besprechen Sie während der Implementierung von Braze unbedingt die Marketingziele mit Ihrem Team, damit Sie am besten entscheiden können, welche Daten Sie tracken möchten und wie Sie sie mit Braze tracken wollen. Ein Beispiel finden Sie in unserer Fallstudie [zur Taxi/Ride-Sharing App](#example-case) am Ende dieses Leitfadens.
{% endalert %}

## Automatisch erfasste Daten

Bestimmte Nutzerdaten werden von unserem SDK automatisch erfasst, z. B. die zuerst verwendete App, die zuletzt verwendete App, die Gesamtzahl der Sitzungen, das Betriebssystem des Geräts usw. Wenn Sie unseren Integrationsleitfäden folgen, um unsere SDKs zu implementieren, können Sie die Vorteile dieser [Standard Datenerfassung]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/) nutzen. Wenn Sie diese Liste überprüfen, können Sie vermeiden, die gleichen Informationen über Nutzer mehrfach zu speichern. Mit Ausnahme von Sitzungsbeginn und -ende werden alle anderen automatisch getrackten Daten nicht auf Ihr Datenpunkt-Kontingent angerechnet.

In unserem Artikel über [SDK Primer]({{site.baseurl}}/developer_guide/getting_started/sdk_overview/) können Sie Prozesse auflisten, die die standardmäßige Datenerfassung bestimmter Artikel blockieren.

## Angepasste Events

Angepasste Events sind Aktionen, die von Ihren Nutzer:innen ausgeführt werden. Sie eignen sich am besten für das Tracking hochwertiger Nutzer:innen-Interaktionen mit Ihrer Anwendung. Die Protokollierung eines angepassten Events kann eine beliebige Anzahl von Folgekampagnen mit konfigurierbaren Verzögerungen triggern und ermöglicht die folgenden Filter zur Segmentierung in Bezug auf die Häufigkeit dieses Events:

| Segmentierung Optionen | Dropdown-Filter | Eingabeoptionen |
| ---------------------| --------------- | ------------- |
| Prüfen, ob das angepasste Event **mehr als X-mal** aufgetreten ist | **MEHR ALS** | **ZAHL** |
| Prüfen, ob das angepasste Event **weniger als X-mal** aufgetreten ist | **WENIGER ALS** | **ZAHL** |
| Prüfen, ob das angepasste Event **genau X-mal** aufgetreten ist | **EXAKT** | **ZAHL** |
| Prüfen Sie, ob das angepasste Event zuletzt **nach dem Datum X** aufgetreten ist | **NACH** | **TIME** |
| Prüfen, ob das angepasste Event zuletzt **vor dem Datum X** aufgetreten ist | **BEVOR** | **TIME** |
| Prüfen, ob das angepasste Event zuletzt **vor mehr als X Tagen** stattgefunden hat | **MEHR ALS** | **ANZAHL DER TAGE VORHER** (positive) Zahl) |
| Prüfen Sie, ob das angepasste Event zuletzt **vor weniger als X Tagen** stattgefunden hat | **WENIGER ALS** | **ANZAHL DER TAGE VORHER** (positive) Zahl) |
| Prüfen Sie, ob das angepasste Event **mehr als X (Max = 50) Mal aufgetreten ist** | **MEHR ALS** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen, ob das angepasste Event **weniger als X Mal (max. 50)** aufgetreten ist **.** | **WENIGER ALS** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen, ob das angepasste Event **genau X Mal (max. 50)** aufgetreten ist **.** | **EXAKT** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze merkt sich für die Segmentierung, wie oft diese Events aufgetreten sind und wann sie von den einzelnen Nutzern zuletzt ausgeführt wurden. Auf der Seite Analytics für **angepasste Events** können Sie sich ansehen, wie oft die einzelnen angepassten Events insgesamt auftreten, und für eine detailliertere Analyse auch nach Segmenten im Zeitverlauf. Dies ist besonders nützlich, um zu sehen, wie sich Ihre Kampagnen auf die Aktivität angepasster Events ausgewirkt haben. Dazu sehen Sie sich die grauen Linien an, die Braze über die Zeitreihe legt, um anzuzeigen, wann zuletzt eine Kampagne gesendet wurde.

![Ein angepasstes Event Analytics Diagramm, das Statistiken über Nutzer:innen anzeigt, die eine Kreditkarte hinzugefügt und eine Suche über einen Zeitraum von dreißig Tagen durchgeführt haben.]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

{% alert note %}
[Das Inkrementieren angepasster Attribute]({{site.baseurl}}/api/endpoints/messaging/) kann verwendet werden, um einen Zähler für eine Nutzer:in-Aktion zu führen, ähnlich wie bei einem angepassten Event. Sie können jedoch keine angepassten Attribut-Daten in einer Zeitserie anzeigen. Nutzer:innen-Aktionen, die nicht in Zeitreihen analysiert werden müssen, sollten mit dieser Methode erfasst werden.
{% endalert %}

### Angepasste Events speichern

Alle Nutzerprofildaten (angepasste Events, angepasste Attribute, angepasste Daten) werden gespeichert, solange diese Profile aktiv sind.

### Angepasste Event-Eigenschaften

Mit angepassten Event-Eigenschaften ermöglicht Braze Ihnen, Eigenschaften für angepasste Events und Käufe festzulegen. Diese Eigenschaften können dann zur weiteren Qualifizierung von Trigger-Bedingungen, zur stärkeren Personalisierung des Messagings und zur Erstellung ausgefeilterer Analytics durch den Export von Rohdaten verwendet werden. Eigenschaften können Strings, Zahlen, boolesche Werte oder Zeitobjekte sein. Eigenschaftswerte können jedoch keine Array-Objekte sein.

Wenn eine E-Commerce-Anwendung beispielsweise eine Nachricht an einen Benutzer senden möchte, wenn dieser seinen Warenkorb abbricht, könnte sie zusätzlich ihre Zielgruppe verbessern und eine stärkere Personalisierung der Kampagne zulassen, indem sie eine angepasste Event-Eigenschaft der `cart_value` der Warenkörbe der Benutzer hinzufügt.

![Ein Beispiel für ein angepasstes Event, das eine Kampagne an einen Nutzer:in sendet, der seinen Warenkorb-Abbruch verursacht hat und den Warenkorbwert bei mehr als 100 und weniger als 200 belassen hat.]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png")

Angepasste Event-Eigenschaften können auch zur Personalisierung im Messaging Template verwendet werden. Jede Kampagne, die [aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) mit einem triggernden Event verwendet, kann angepasste Event-Eigenschaften aus diesem Event für die Personalisierung von Nachrichten nutzen. Wenn eine Spielanwendung eine Nachricht an Nutzer:innen senden möchte, die ein Level abgeschlossen haben, kann sie die Nachricht mit einer Eigenschaft für die Zeit personalisieren, die Nutzer:innen für den Abschluss dieses Levels benötigt haben. In diesem Beispiel wird die Nachricht mithilfe [bedingter Logik]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/) für drei verschiedene Segmente personalisiert. Die angepasste Event-Eigenschaft namens ``time_spent`` kann durch den Aufruf von ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}`` in die Nachricht aufgenommen werden.

{% raw %}
```liquid
{% if {{event_properties.${time_spent}}} < 600 %}
Congratulations on beating that level so fast! Check out our online portal where you can play against top players fromm around the world!
{% elsif {{event_properties.${time_spent}}} < 1800 %}
Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Talk to villagers for essential tips on how to beat levels!
{% endif %}
```
{% endraw %}

Angepasste Event-Eigenschaften helfen Ihnen dabei, Ihr Messaging anzupassen oder granulare aktionsbasierte Zustellungskampagnen zu erstellen. Wenn Sie Segmente auf der Grundlage der Häufigkeit und der Eigenschaften von Events erstellen möchten, wenden Sie sich an Ihren Customer-Success-Manager oder an unser Support-Team.

## Angepasste Attribute

Angepasste Attribute sind außerordentlich flexible Werkzeuge, mit denen Sie Nutzer:innen noch gezielter als mit Standardattributen zusammenstellen können. Angepasste Attribute eignen sich hervorragend, um markenspezifische Informationen über Ihre Nutzer zu speichern. Sie sollten bedenken, dass wir für angepasste Attribute keine Zeitreiheninformationen speichern. Sie erhalten also keine darauf basierenden Diagramme wie im vorangegangenen Beispiel für angepasste Events.

### Angepasste Attribute speichern

Alle Nutzerprofildaten (angepasste Events, angepasste Attribute, angepasste Daten) werden gespeichert, solange diese Profile aktiv sind.

### Angepasste Attribut-Datenarten

Die folgenden Datenarten können als angepasste Attribute gespeichert werden:

#### Strings (alphanumerische Zeichen)

String Attribute sind nützlich, um Nutzereingaben zu speichern, z. B. eine Lieblingsmarke, eine Telefonnummer oder einen letzten Suchstring in Ihrer Anwendung. String Attribute können bis zu 255 Zeichen lang sein.

Die folgende Tabelle beschreibt die verfügbaren Segmentierungsoptionen für String-Attribute.

| Segmentierung Optionen | Dropdown-Filter | Eingabe-Optionen |
| ---------------------| --------------- | ------------- |
| Prüfen Sie, ob das String-Attribut mit einem eingegebenen String **exakt übereinstimmt**.| **IST GLEICH** | **STRING** |
| Prüfen Sie, ob das String-Attribut mit einem eingegebenen String **ODER** einem regulären Ausdruck **teilweise übereinstimmt**. | **STIMMT MIT REGEX ÜBEREIN** | **STRING** **ODER** **REGEX** |
| Prüfen Sie, ob das String-Attribut mit einem eingegebenen String **ODER** regulären Ausdruck **nicht teilweise übereinstimmt**. | **STIMMT NICHT MIT REGEX ÜBEREIN** | **STRING** **ODER** **REGEX** |
| Prüfen Sie, ob das String-Attribut mit einem eingegebenen String **nicht übereinstimmt**.| **IST NICHT GLEICHBEDEUTEND MIT** | **STRING** |
| Prüfen Sie, ob das String-Attribut n einem Nutzerprofil **vorhanden ist**. | **IS BLANK** | **--** |
| Prüfen Sie, ob das String-Attribut in einem Nutzerprofil **nicht vorhanden ist**. | **IST NICHT LEER** | **--** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
Bei der Segmentierung mit dem Filter **DOES NOT MATCH REGEX** ist es erforderlich, dass bereits ein angepasstes Attribut mit einem Wert in diesem Nutzerprofil existiert. Wir empfehlen, mit ODER-Logik zu prüfen, ob ein angepasstes Attribut leer ist, um die Zielgruppe richtig zusammenzustellen.
{% endalert %}

{% alert tip %}
Wenn Sie mehr über die Verwendung unseres Filters für reguläre Ausdrücke erfahren möchten, lesen Sie diese Dokumentation über [Perl-kompatible reguläre Ausdrücke (PCRE)](http://www.regextester.com/pregsyntax.html).
<br>
Weitere Ressourcen zu Regex:
- [Regex mit Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/)
- [Regex Debugger und Tester](https://regex101.com/)
- [Regex-Tutorial](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285)
{% endalert %}

#### Arrays

Array-Attribute sind gut geeignet, um zusammenhängende Listen mit Informationen über Ihre Nutzer zu speichern. Wenn Sie zum Beispiel die letzten 100 Inhalte, die ein Nutzer gesehen hat, in einem Array speichern, ist eine Segmentierung nach Interessen zulässig.

Angepasste Attribut-Arrays sind eindimensionale Sets; mehrdimensionale Arrays werden nicht unterstützt. **Wenn Sie ein Element zu einem angepassten Attribut-Array hinzufügen, wird das Element an das Ende des Arrays angehängt, es sei denn, es ist bereits vorhanden. In diesem Fall wird es von seiner aktuellen Position an das Ende des Arrays verschoben.** Wenn zum Beispiel das Array `['hotdog','hotdog','hotdog','pizza']` importiert wurde, wird es im Array-Attribut als `['hotdog', 'pizza']` angezeigt, da nur eindeutige Werte unterstützt werden.

Wenn das Array seine Höchstzahl an Elementen enthält, wird das erste Element verworfen und das neue Element am Ende hinzugefügt. Im Folgenden finden Sie einige Beispiele für Code, der das Array-Verhalten im Web SDK zeigt:

```js
var abUser = appboy.getUser();
// initialize array for this user, assuming max length of favorite_foods is set to 4.
abUser.setCustomUserAttribute('favorite_foods', ['pizza', 'wings', 'pasta']); // => ['pizza', 'wings', 'pasta']
abUser.addToCustomAttributeArray('favorite_foods', 'fries'); // => ['pizza', 'wings', 'pasta', 'fries']
abUser.addToCustomAttributeArray('favorite_foods', 'pizza'); // => ['wings', 'pasta', 'fries', 'pizza']
abUser.addToCustomAttributeArray('favorite_foods', 'ice cream'); // => ['pasta', 'fries', 'pizza', 'ice cream']
```

Die maximale Anzahl von Elementen in benutzerdefinierten Attribut-Arrays ist standardmäßig auf 25 festgelegt. Das Maximum für einzelne Arrays kann im Braze-Dashboard unter **Dateneinstellungen** > Angepasste Attribute auf bis zu 100 erhöht werden. Wenn Sie möchten, dass dieser Höchstbetrag erhöht wird, wenden Sie sich an Ihren Kundenbetreuer. Arrays, die die maximale Anzahl von Elementen überschreiten, werden so abgeschnitten, dass sie die maximale Anzahl von Elementen enthalten.

Die folgende Tabelle beschreibt die verfügbaren Segmentierungsoptionen für Array-Attribute.

| Segmentierung Optionen | Dropdown-Filter | Eingabe-Optionen |
| ---------------------| --------------- | ------------- |
| Prüfen Sie, ob das Array-Attribut einen Wert enthält, der mit einem eingegebenen Wert **exakt übereinstimmt**.| **ENTHÄLT EINEN WERT** | **STRING** |
| Prüfen Sie, ob das Array-Attribut einen Wert enthält, der mit einem eingegebenen Wert **nicht exakt übereinstimmt**.| **ENTHÄLT KEINEN WERT** | **STRING** |
| Prüfen Sie, ob das Array-Attribut einen Wert enthält, der mit einem eingegebenen Wert **ODER** regulären Ausdruck **teilweise übereinstimmt**. | **STIMMT MIT REGEX ÜBEREIN** | **STRING** **ODER** **REGEX** |
| Prüfen Sie, ob das Attribut array **einen Wert hat** | **HAT EINEN WERT** | **--** |
| Prüfen Sie, ob das Attribut array **leer ist** | **IST LEER** | **--** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Wir verwenden [Perl-kompatible reguläre Ausdrücke (PCRE](http://www.regextester.com/pregsyntax.html)).
{% endalert %}

#### Daten

Zeitattribute sind nützlich, um zu speichern, wann eine bestimmte Aktion das letzte Mal durchgeführt wurde, damit Sie Ihren Nutzer:innen inhaltsspezifische Nachrichten zur erneuten Interaktion anbieten können.

{% alert note %}
Das letzte Datum, an dem ein angepasstes Event oder Kauf-Event stattgefunden hat, wird automatisch aufgezeichnet und darf nicht über ein angepasstes Zeitattribut doppelt erfasst werden.
{% endalert %}

Datumsfilter mit relativen Daten (z.B. vor mehr als 1 Tag, vor weniger als 2 Tagen) messen 1 Tag als 24 Stunden. Jede Kampagne, die Sie mit diesen Filtern durchführen, schließt alle Nutzer in einem 24-Stunden-Inkrement ein. Ein Beispiel: "Letzte Nutzung der App vor mehr als 1 Tag" erfasst alle Nutzer:innen, die "die App zuletzt vor mehr als 24 Stunden genutzt haben", genau ab dem Zeitpunkt, an dem die Kampagne läuft. Dasselbe gilt für Kampagnen mit längeren Datumsbereichen - fünf Tage nach der Aktivierung sind also die 120 Stunden davor.

Die folgende Tabelle beschreibt die verfügbaren Segmentierungsoptionen für Zeitattribute.

| Segmentierung Optionen | Dropdown-Filter | Eingabe-Optionen |
| ---------------------| --------------- | ------------- |
| Prüfen Sie, ob das Zeit-Attribut **vor** einem **ausgewählten Datum** liegt.| **BEVOR** | **KALENDERAUSWAHL** |
| Prüfen Sie, ob das Zeit-Attribut **nach** einem **ausgewählten Datum** liegt.| **NACH** | **KALENDERAUSWAHL** |
| Prüfen Sie, ob das Zeit-Attribut **mehr als** **X Tage zurückliegt**. | **MEHR ALS** | **ANZAHL DER TAGE IN DER VERGANGENHEIT** |
| Prüfen Sie, ob das Zeit-Attribut **weniger als** **X Tage zurückliegt**.| **WENIGER ALS** | **ANZAHL DER TAGE IN DER VERGANGENHEIT** |
| Prüfen Sie, ob das Zeit-Attribut **mehr als** **X Tage in der Zukunft liegt**. | **IN MEHR ALS** | **ANZAHL DER TAGE IN DER ZUKUNFT** |
| Prüfen Sie, ob das Zeit-Attribut **weniger als** **X Tage in der Zukunft liegt**. | **IN WENIGER ALS** | **ANZAHL DER TAGE IN DER ZUKUNFT**  |
| Prüfen Sie, ob das Zeit-Attribut n einem Nutzerprofil **vorhanden ist**. | **IST LEER** | **--** |
| Prüfen Sie, ob das Zeit-Attribut in einem Nutzerprofil **nicht vorhanden ist**. | **IST NICHT LEER** | **--** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Zahlen {#integers}

Für numerische Attribute gibt es eine Vielzahl von Anwendungsfällen. Angepasste Attribute mit inkrementeller Anzahl sind nützlich, um zu speichern, wie oft eine bestimmte Aktion oder ein bestimmtes Event stattgefunden hat. Standardnummern haben alle möglichen Verwendungszwecke, wie z.B. die Erfassung der Schuhgröße, des Taillenumfangs oder der Anzahl, wie oft ein Nutzer:innen ein bestimmtes Produkt Feature oder eine Kategorie angesehen hat.

{% alert note %}
Das ausgegebene Geld sollte nicht auf diese Weise erfasst werden. Vielmehr sollte es über unsere [Kaufmethoden]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#purchase-events--revenue-tracking) erfasst werden.
{% endalert %}

Die folgende Tabelle beschreibt die verfügbaren Segmentierungsoptionen für numerische Attribute.

| Segmentierung Optionen | Dropdown-Filter | Eingabe-Optionen |
| ---------------------| --------------- | ------------- |
| Prüfen Sie, ob das numerische Attribut **mehr als** eine **Zahl** beträgt.| **MEHR ALS** | **ZAHL** |
| Prüfen Sie, ob das numerische Attribut **weniger als** eine **Zahl** beträgt.| **WENIGER ALS** | **ZAHL** |
| Prüfen Sie, ob das numerische Attribut **exakt** einer **Zahl** entspricht.| **EXAKT** | **ZAHL** |
| Prüfen Sie, ob das numerische Attribut **nicht exakt** einer **Zahl** entspricht.| **IST NICHT GLEICHBEDEUTEND MIT** | **ZAHL** |
| Prüfen Sie, ob das numerische Attribut n einem Nutzerprofil **vorhanden ist**. | **EXISTS** | **--** |
| Prüfen Sie, ob das numerische Attribut in einem Nutzerprofil **nicht vorhanden ist**. | **EXISTIERT NICHT** | **--** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Boolesche Werte (wahr/falsch)

Boolesche Attribute sind nützlich, um den Status von Abos und andere einfache binäre Daten über Ihre Nutzer zu speichern. Die Eingabeoptionen, die wir Ihnen zur Verfügung stellen, erlauben es Ihnen, sowohl Nutzer:innen zu finden, bei denen eine Variable explizit auf einen Booleschen Wert gesetzt wurde, als auch Nutzer:innen, bei denen dieses Attribut noch nicht aufgezeichnet wurde.

Die folgende Tabelle beschreibt die verfügbaren Segmentierungsoptionen für boolesche Attribute.

| Segmentierung Optionen | Dropdown-Filter | Eingabe-Optionen |
| ---------------------| --------------- | ------------- |
| Prüfen Sie, ob der boolesche Wert **ist** | **IST**  | **TRUE**, **FALSE**, **TRUE OR NOT SET**, oder **FALSE OR NOT SET** |
| Prüfen Sie, ob der boolesche Wert im Nutzerprofil **vorhanden ist**. | **EXISTS**  | **--** |
| Prüfen Sie, ob der boolesche Wert in einem Nutzerprofil **nicht vorhanden ist**. | **EXISTIERT NICHT**  | **--** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Kauf-Events und Umsatz Tracking

Durch die Verwendung unserer Kaufmethoden zur Erfassung von In-App-Käufen wird der Life-time Value (LTV) für jedes einzelne Nutzerprofil ermittelt. Diese Daten können Sie auf unserer Umsatzseite in Zeitseriendiagrammen einsehen.

Die folgende Tabelle beschreibt die verfügbaren Segmentierungsoptionen für Kauf-Events.

| Segmentierung Optionen | Dropdown-Filter | Eingabe-Optionen |
| ---------------------| --------------- | ------------- |
| Prüfen Sie, ob die Gesamtzahl der ausgegebenen Summe **größer als** eine **Zahl** ist| **GRÖSSER ALS** | **ZAHL** |
| Prüfen Sie, ob die Gesamtzahl der ausgegebenen Summe **weniger als** eine **Zahl** ist| **WENIGER ALS** | **ZAHL** |
| Prüfen Sie, ob die Gesamtzahl der ausgegebenen Dollar **exakt** einer **Zahl** entspricht| **EXAKT** | **ZAHL** |
| Prüfen Sie, ob der letzte Kauf **nach dem Datum X** stattgefunden hat | **NACH** | **TIME** |
| Prüfen Sie, ob der letzte Kauf **vor dem Datum X** stattgefunden hat | **BEVOR** | **TIME** |
| Prüfen Sie, ob der letzte Kauf **mehr als X Tage zurückliegt** | **MEHR ALS** | **TIME** |
| Prüfen Sie, ob der letzte Kauf **weniger als X Tage zurückliegt** | **WENIGER ALS** | **TIME** |
| Prüfen Sie, ob der Kauf **mehr als X (Max = 50) Mal** stattgefunden hat | **MEHR ALS** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen Sie, ob der Kauf **weniger als X (Max = 50) Mal** stattgefunden hat | **WENIGER ALS** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
| Prüfen Sie, ob der Kauf **exakt X (Max = 50) Mal** stattgefunden hat | **EXAKT** | in den letzten **Y Tagen (Y = 1,3,7,14,21,30)** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Wenn Sie nach der Häufigkeit eines bestimmten Kaufs segmentieren möchten, sollten Sie diesen Kauf auch einzeln als [inkrementelles angepasstes Attribut](#integers) erfassen.
{% endalert %}

## Anwendungsfall Taxi-/Mitfahr-App {#example-case}

Nehmen wir als Beispiel eine Mitfahr-App, die entscheiden möchte, welche Nutzer:innen-Daten sie sammeln möchte. Die folgenden Fragen und der Brainstorming-Prozess sind ein hervorragendes Modell für Marketing- und Entwickler-Teams. Am Ende dieser Übung sollten beide Teams ein solides Verständnis davon haben, welche angepassten Events und -Attribute sinnvollerweise gesammelt werden sollten, um ihr Ziel zu erreichen.

**Fallfrage 1: Was ist das Ziel?**

Ihr Ziel ist ganz einfach: Sie wollen, dass Nutzer:innen über ihre App Taxifahrten anfordern.

**Fallfrage 2: Was sind die Zwischenschritte auf dem Weg von der App-Installation zu diesem Ziel?**

1. Sie benötigen Nutzer, um den Registrierungsprozess zu beginnen und ihre persönlichen Daten auszufüllen.
2. Die Nutzer:innen müssen den Registrierungsprozess abschließen und überprüfen, indem sie einen Code in die App eingeben, den sie per SMS erhalten.
3. Sie müssen versuchen, ein Taxi zu rufen.
4. Um ein Taxi anzufordern, müssen Sie verfügbar sein, wenn sie gesucht werden.

Diese Aktionen könnten dann als die folgenden angepassten Events getaggt werden:

- Beginn der Registrierung
- Abgeschlossene Registrierung
- Erfolgreiche Taxifahrten
- Erfolglose Taxi-Anrufe

Nachdem Sie die Events implementiert haben, können Sie nun die folgenden Kampagnen durchführen:

1. Nachrichten an Nutzer:innen, die mit der Registrierung begonnen, aber das Ereignis "Registrierung abgeschlossen" nicht innerhalb eines bestimmten Zeitrahmens ausgelöst haben.
2. Senden Sie Nachrichten an Nutzer:innen, die die Registrierung abgeschlossen haben.
3. Senden Sie Nutzern:innen, die erfolglos ein Taxi gerufen haben und auf die nicht innerhalb einer bestimmten Zeitspanne ein erfolgreiches Taxi gerufen wurde, eine Entschuldigung und eine Gutschrift für eine Aktion.
4. Senden Sie Aktionen an leistungsstarke Nutzer:innen mit vielen erfolgreichen Taxifahrten, um ihnen für ihre Treue zu danken.

Und viele mehr!

**Fallfrage 3: Welche anderen Informationen sollten wir über unsere Nutzer:innen wissen, um unser Messaging zu verbessern?**

- Ob sie über Aktionskredite verfügen oder nicht?
- Die durchschnittliche Bewertung, die sie für ihre Fahrer vergeben?
- Eindeutige Promo-Codes für Nutzer?

Diese Merkmale könnten dann als die folgenden angepassten Attribute getaggt werden:

- Aktionsguthaben (Dezimaltyp)
- Durchschnittliche Fahrerbewertung (Zahlentyp)
- Eindeutiger Promo Code (String Typ)

Wenn Sie diese Attribute hinzufügen, haben Sie die Möglichkeit, Kampagnen an Nutzer zu senden, z. B:

1. Erinnern Sie Nutzer:innen, die sich seit sieben Tagen nicht mehr eingeloggt haben, aber über ein Aktionsguthaben verfügen, daran, dass ihr Guthaben existiert und dass sie die App erneut besuchen sollten, um es zu nutzen!
2. Schreiben Sie Nutzern, die niedrige Fahrerbewertungen abgeben, eine Nachricht, um direktes Kundenfeedback zu erhalten und zu erfahren, warum ihnen die Fahrt nicht gefallen hat.
3. Nutzen Sie unsere [Features zur Template-Erstellung und Personalisierung von Nachrichten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/), um das eindeutige Attribut des Aktionscodes in das Messaging für die Nutzer:innen zu ziehen.

## Bewährte Praktiken

### Allgemeine bewährte Praktiken

#### Event-Eigenschaften verwenden

- Nennen Sie ein angepasstes Event – etwas, das eine Aktion beschreibt, die Nutzer durchführen.
- Machen Sie großzügigen Gebrauch von angepassten Event-Eigenschaften, um wichtige Daten zu einem Event darzustellen.
- Anstatt z.B. für jeden von 50 verschiedenen Filmen ein eigenes angepasstes Event zu erfassen, wäre es effektiver, einfach das Ansehen eines Films als Event zu erfassen und eine Event-Eigenschaft zu haben, die den Namen des Films enthält.

### Bewährte Praktiken für die Entwicklung

#### Benutzer:innen IDs für alle Nutzer:innen festlegen

Für jeden Ihrer Benutzer sollten Benutzer-IDs festgelegt werden. Diese sollten unveränderlich und zugänglich sein, wenn ein Benutzer die App öffnet. Wir **empfehlen dringend,** diesen Bezeichner anzugeben, da Sie damit folgende Möglichkeit haben:

- Verfolgen Sie Ihre Nutzer geräte- und plattformübergreifend und verbessern Sie so die Qualität Ihrer verhaltensbezogenen und demografischen Daten.
- Importieren Sie Daten über Ihre Benutzer mit unserer [Benutzerdaten-API]({{site.baseurl}}/api/endpoints/user_data/).
- Richten Sie sich mit unserer [Messaging-API]({{site.baseurl}}/api/endpoints/messaging/) für allgemeine und transaktionsbezogene Nachrichten an bestimmte Nutzer.

Nutzer:innen IDs müssen weniger als 512 Zeichen lang sein und sollten privat und nicht leicht erhältlich sein (z.B. keine einfache E-Mail Adresse oder Benutzername). Wenn eine solche Kennung nicht verfügbar ist, weist Braze Ihren Benutzern eine eindeutige Kennung zu, aber Ihnen fehlen dann die für Benutzer-IDs aufgeführten Möglichkeiten. Sie sollten es vermeiden, Benutzer-IDs für Benutzer festzulegen, für die Sie keinen eindeutigen Bezeichner haben, die mit ihnen als Individuum verbunden ist. Die Übergabe eines Gerätebezeichners bietet keinen Vorteil gegenüber der automatischen anonymen Benutzerverfolgung, die Braze standardmäßig anbietet. Im Folgenden finden Sie einige Beispiele für geeignete und ungeeignete Nutzer:innen IDs.

Gute Optionen für Nutzer-IDs:

- Gehashte E-Mail Adresse oder eindeutiger Benutzername
- Eindeutiger Bezeichner der Datenbank

Diese sollten nicht als Nutzer:innen IDs verwendet werden:

- Geräte-ID
- Zufallszahl oder Sitzungs-ID
- Jede nicht eindeutige ID
- E-Mail-Adresse
- Die Nutzer:in eines anderen Drittanbieters ID

{% multi_lang_include sdk_auth_alert.md %}

#### Geben Sie angepassten Events und -Attributen lesbare Namen

Stellen Sie sich vor, Sie sind ein Marketer, der Braze erst ein oder zwei Jahre nach der Implementierung einsetzt. Eine Dropdown-Liste voller Namen wie "usr_no_acct" ohne weiteren Kontext zu lesen, kann einschüchternd wirken. Wenn Sie Ihren Events und Attributen identifizierbare und lesbare Namen geben, wird es für alle Nutzer Ihrer Plattform einfacher. Beachten Sie die folgenden Best-Practice-Beispiele:

- Beginnen Sie ein angepasstes Event nicht mit einem numerischen Zeichen. Die Dropdown-Liste ist alphabetisch sortiert und beginnt mit einem numerischen Zeichen, was die Segmentierung nach dem ausgewählten Filter erschwert.
- Versuchen Sie, möglichst keine obskuren Abkürzungen oder Fachausdrücke zu verwenden.
  - Beispiel: `usr_ctry` mag als Variablenname für das Land eines Nutzers innerhalb eines Codes in Ordnung sein, aber das angepasste Attribut sollte als `user_country` an Braze gesendet werden, um einem Marketer, der das Dashboard später verwendet, etwas Klarheit zu verschaffen.

#### Nur Attribute protokollieren, wenn sie sich ändern

Wir zählen jedes an Braze übergebene Attribut als Datenpunkt, auch wenn das übergebene Attribut denselben Wert enthält wie zuvor gespeichert. Wenn Sie Daten nur dann protokollieren, wenn sie sich ändern, vermeiden Sie die redundante Verwendung von Datenpunkten und sorgen durch die Vermeidung unnötiger API-Aufrufe für eine reibungslosere Nutzung.

#### Vermeiden Sie die programmatische Erzeugung von Event-Namen

Wenn Sie ständig neue Event-Namen erstellen, wird es unmöglich sein, Ihre Nutzer sinnvoll zu segmentieren. Sie sollten in der Regel allgemeine Ereignisse erfassen ("Video angesehen" oder "Artikel gelesen") und keine hochspezifischen Ereignisse wie ("Gangnam Style angesehen" oder "Artikel gelesen"): Die 10 besten Orte zum Mittagessen in Midtown Manhattan"). Die spezifischen Daten zum Event sollten als Eigenschaft des Events und nicht als Teil des Event-Namens enthalten sein.

### Technische Beschränkungen und Bedingungen

Beachten Sie bei der Implementierung angepasster Events die folgenden Beschränkungen und Bedingungen:

#### Längenbeschränkungen

Angepasste Events, Namen von angepassten Attributen (Schlüsseln) und String-Werte für angepasste Events, die 255 Zeichen oder länger sind, werden abgeschnitten. Idealerweise sollten diese so kurz wie möglich sein, um die Netzwerk- und Akku-Performance Ihrer App zu verbessern. Beschränken Sie sie nach Möglichkeit auf 50 Zeichen.

#### Inhaltliche Beschränkungen
Die folgenden Inhalte werden programmgesteuert aus Ihren Attributen und Ereignissen herausgefiltert. Achten Sie darauf, Folgendes nicht zu verwenden:

- Führende und nachgestellte Leerzeichen
- Zeilenumbrüche
- Zeichen, die keine Ziffern sind, in Telefonnummern
  - Beispiel: "(732) 178-1038" wird zu "7321781038" verkürzt.
- Zeichen ohne Leerzeichen müssen in Leerzeichen umgewandelt werden
- $ sollte nicht als Präfix für angepasste Events verwendet werden
- Alle ungültigen UTF-8-Kodierungswerte
  -  "Mein \\x80 Feld" würde zu "Mein Feld" verkürzt werden.

#### Reservierte Tasten

Die folgenden Schlüssel sind reserviert und können nicht als benutzerdefinierte Ereigniseigenschaften verwendet werden:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

#### Wert-Definitionen

- Ganzzahlige Werte sind 64 Bit
- Dezimalzahlen haben standardmäßig 15 Dezimalstellen

### Parsen eines generischen Namensfeldes

Wenn für Nutzer nur ein einziges generisches Namensfeld existiert (z.B. 'JohnDoe'), können Sie diesen gesamten Titel dem Vornamen-Attribut zuordnen. Sie können auch versuchen, sowohl den Vor- als auch den Nachnamen mit Hilfe von Leerzeichen zu parsen, aber diese Methode birgt das Risiko, dass Nutzer falsch benannt werden.
