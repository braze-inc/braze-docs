---
nav_title: "API Bezeichner Typen"
article_title: API Bezeichner Typen
page_order: 2.2
toc_headers: h2
description: "Dieser Artikel referenziert die verschiedenen Arten von API-Bezeichnern, die im Braze-Dashboard vorhanden sind, wo Sie sie finden können und wofür sie verwendet werden." 
page_type: reference

---

# API Bezeichner Typen

> Dieser Leitfaden referenziert die verschiedenen Arten von API-Bezeichnern, die im Braze-Dashboard zu finden sind, ihren Zweck, wo sie zu finden sind und wie sie normalerweise verwendet werden. Informationen über REST API-Schlüssel oder Workspace API-Schlüssel finden Sie in der [Übersicht über die APIs]({{site.baseurl}}/api/api_key/).

Die folgenden Bezeichner können verwendet werden, um von der externen API von Braze aus auf Ihr Template, Ihr Canvas, Ihre Kampagne oder Ihr Segment zuzugreifen. Alle Nachrichten sollten in [UTF-8](https://en.wikipedia.org/wiki/UTF-8) kodiert sein.

## Bezeichner der App

Der App-Bezeichner oder `app_id` ist ein Parameter, der eine Aktivität mit einer bestimmten App in Ihrem Workspace verbindet. Es zeigt an, mit welcher App innerhalb des Arbeitsbereichs Sie interagieren. Sie werden zum Beispiel feststellen, dass Sie eine `app_id` für Ihre iOS App, eine `app_id` für Ihre Android App und eine `app_id` für Ihre Internet Integration haben werden. Bei Braze kann es vorkommen, dass Sie mehrere Apps für dieselbe Plattform auf den verschiedenen von Braze unterstützten Plattformtypen haben.

### Wo kann ich es finden?

Es gibt zwei Möglichkeiten, Ihren Standort `app_id` zu finden:

{% tabs local %}
{% tab App Bezeichner %}
Gehen Sie zu **Einstellungen** > **APIs und Bezeichner** > **App Bezeichner**. Ihr API-Schlüssel für jede App ist in der Spalte **Bezeichner** aufgeführt.
{% endtab %}

{% tab App Einstellungen %}
Gehen Sie zu **Einstellungen** > **App-Einstellungen**. Ihr API-Schlüssel ist neben dem Feld **API-Schlüssel** im Bereich Einstellungen aufgeführt.

{% endtab %}
{% endtabs %}

### Wofür kann es verwendet werden?

App-Bezeichner bei Braze werden bei der Integration des SDK verwendet und dienen auch dazu, eine bestimmte App in REST API-Aufrufen zu referenzieren. Mit `app_id` können Sie viele Dinge tun, wie z.B. Daten für ein angepasstes Event, das für eine bestimmte App aufgetreten ist, abrufen, Deinstallationsstatistiken, Statistiken über neue Nutzer:innen, DAU-Statistiken und Statistiken über den Sitzungsbeginn für eine bestimmte App.

{% alert tip %}
Manchmal kann es vorkommen, dass Sie zur Eingabe von `app_id` aufgefordert werden, Sie aber nicht mit einer App arbeiten, weil es sich um ein Legacy-Feld für eine bestimmte Plattform handelt. Sie können dieses Feld auslassen, indem Sie einen beliebigen String als Platzhalter für diesen erforderlichen Parameter einfügen.
{% endalert %}

### Mehrere Bezeichner für Apps

Bei der Einrichtung des SDK ist der häufigste Anwendungsfall für mehrere App-Bezeichner die Trennung dieser Bezeichner für Debug- und Release-Build-Varianten.

Um einfach zwischen mehreren App Bezeichnern in Ihren Builds zu wechseln, empfehlen wir Ihnen, für jede relevante [Variante des Builds](https://developer.android.com/studio/build/build-variants.html) eine eigene `braze.xml` Datei zu erstellen. Eine Build-Variante ist eine Kombination aus Build-Typ und Produkt-Flavor. Standardmäßig wird ein neues Android-Projekt mit den Build-Typen `debug` und `release` und ohne Produkt-Flavors konfiguriert.

Erstellen Sie für jede relevante Variante des Builds eine neue `braze.xml` in `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
Wenn die Build-Variante kompiliert wird, verwendet sie den neuen Bezeichner.

## Template Bezeichner

Ein [Template-Bezeichner]({{site.baseurl}}/api/endpoints/templates/) oder eine Template ID ist ein zufälliger Schlüssel, der von Braze für ein bestimmtes Template innerhalb des Dashboards generiert wird. Template IDs sind für jede Vorlage eindeutig und können verwendet werden, um Templates über die API zu referenzieren. 

Templates sind ideal, wenn Ihr Unternehmen Ihre HTML-Designs für Kampagnen in Auftrag gibt. Nach der Erstellung der Templates verfügen Sie nun über ein Template, das nicht speziell für eine Kampagne, sondern für eine Reihe von Kampagnen, z. B. einen Newsletter, verwendet werden kann.

### Wo kann ich es finden?

Sie können Ihre Template ID auf zwei Arten finden:

{% tabs local %}
{% tab Templates %}
Gehen Sie zu **Vorlagen**, wählen Sie eine Vorlagenseite aus und wählen Sie dann eine bereits vorhandene Vorlage. Wenn die gewünschte Vorlage noch nicht existiert, erstellen Sie eine und speichern Sie sie. Unten auf der Seite der einzelnen Templates finden Sie Ihren Bezeichner für das Template.
{% endtab %}

{% tab API-Schlüssel %}
Gehen Sie zu **Einstellungen** > **APIs und Bezeichner**. Hier bietet Braze eine Suche nach **zusätzlichen API Bezeichnern** an, mit der Sie bestimmte Bezeichner nachschlagen können.

{% endtab %}
{% endtabs %}

### Wofür kann es verwendet werden?

- Update von Templates über die API
- Informationen über eine bestimmte Vorlage abrufen

## Canvas Bezeichner

Ein [Canvas-Bezeichner]({{site.baseurl}}/user_guide/engagement_tools/canvas/) oder eine Canvas ID ist ein zufälliger Schlüssel, der von Braze für ein bestimmtes Canvas innerhalb des Dashboards generiert wird. Canvas IDs sind für jedes Canvas eindeutig und können verwendet werden, um Canvase über die API zu referenzieren. 

Denken Sie daran, dass es bei einem Canvas mit Varianten sowohl eine allgemeine Canvas-ID als auch individuelle Canvas-IDs für Varianten gibt, die unter dem Haupt-Canvas verschachtelt sind. 

### Wo kann ich es finden?

Ihre Canvas ID finden Sie auf dem Dashboard. Gehen Sie zu **Messaging** > **Canvas** und wählen Sie ein bereits vorhandenes Canvas aus. Wenn das gewünschte Canvas noch nicht existiert, erstellen Sie es und speichern es. Klicken Sie unten auf einer einzelnen Canvas-Seite auf **Varianten analysieren**. Es erscheint ein Fenster mit dem Canvas API Bezeichner am unteren Rand.

### Wofür kann es verwendet werden?

- Tracking von Analytics für eine bestimmte Nachricht
- Erfassen Sie aggregierte Statistiken zur Performance von Canvas auf höchster Ebene.
- Details zu einem bestimmten Canvas abrufen
- Mit Currents, um Nutzer:innen Daten für ein "größeres Bild" von Canvase einzubringen
- Mit API-getriggerter Zustellung zur Erfassung von Statistiken für transaktionale Nachrichten

## Bezeichner der Kampagne

Ein Bezeichner oder eine ID für eine [Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) ist ein zufälliger Schlüssel, der von Braze für eine bestimmte Kampagne innerhalb des Dashboards generiert wird. Kampagnen-IDs sind für jede Kampagne eindeutig und können verwendet werden, um Kampagnen über die API zu referenzieren. 

Denken Sie daran, dass es bei Kampagnen mit Varianten sowohl eine ID für die gesamte Kampagne als auch IDs für die einzelnen Varianten gibt, die unter der Hauptkampagne eingebettet sind. 

### Wo kann ich es finden?

Sie können Ihre ID für die Kampagne auf zwei Arten finden:

{% tabs local %}
{% tab Kampagnen %}
Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie eine bereits existierende Kampagne aus. Wenn die von Ihnen gewünschte Kampagne noch nicht existiert, erstellen Sie eine und speichern Sie sie. Unten auf der Seite der einzelnen Kampagnen finden Sie Ihren **API-Bezeichner für die Kampagne**.

{% endtab %}

{% tab API-Schlüssel %}
Gehen Sie zu **Einstellungen** > **APIs und Bezeichner**. Hier bietet Braze eine Suche nach **zusätzlichen API Bezeichnern** an, mit der Sie bestimmte Bezeichner nachschlagen können.

{% endtab %}
{% endtabs %}

### Wofür kann es verwendet werden?

- Tracking von Analytics für eine bestimmte Nachricht
- Erfassen Sie hochrangige Statistiken zur Performance von Kampagnen
- Details zu einer bestimmten Kampagne abrufen
- Mit Currents, um Daten auf Nutzer:innen-Ebene in Kampagnen einfließen zu lassen, die ein "größeres Bild" ergeben.
- Mit API-getriggerter Zustellung zur Erfassung von Statistiken für transaktionale Nachrichten
- Zum [Suchen nach einer bestimmten Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/#search-syntax) auf der Seite **Kampagnen** mithilfe des Filters `api_id:YOUR_API_ID`

## Bezeichner des Segments

Ein [Segmentbezeichner]({{site.baseurl}}/user_guide/engagement_tools/segments/) oder eine Segment ID ist ein zufälliger Schlüssel, der von Braze für ein bestimmtes Segment innerhalb des Dashboards generiert wird. Segment IDs sind für jedes Segment eindeutig und können verwendet werden, um Segmente über die API zu referenzieren. 

### Wo kann ich es finden?

Sie können Ihre Segment ID auf zwei Arten finden:

{% tabs local %}
{% tab Segmente %}
Gehen Sie zu **Zielgruppe** > **Segmente** und wählen Sie ein bereits bestehendes Segment aus. Wenn das gewünschte Segment noch nicht vorhanden ist, erstellen Sie es und speichern es. Unten auf der Seite der einzelnen Segmente finden Sie Ihren Bezeichner für die Segmente.

{% endtab %}

{% tab API-Schlüssel %}
Gehen Sie zu **Einstellungen** > **APIs und Bezeichner**. Hier bietet Braze eine Suche nach **zusätzlichen API Bezeichnern** an, mit der Sie bestimmte Bezeichner nachschlagen können.

{% endtab %}
{% endtabs %}

### Wofür kann es verwendet werden?

- Erhalten Sie Details zu einem bestimmten Segment
- Abrufen von Analytics eines bestimmten Segments
- Abrufen, wie oft ein angepasstes Event für ein bestimmtes Segment aufgezeichnet wurde
- Bestimmen und senden Sie eine Kampagne an Mitglieder eines Segments aus der API heraus

## Bezeichner senden

Ein Bezeichner oder eine ID ist ein Schlüssel, der entweder von Braze generiert oder von Ihnen für eine bestimmte gesendete Nachricht erstellt wurde und unter dem die Analytics verfolgt werden sollen. Der Bezeichner für den Versand ermöglicht es Ihnen, Analytics für eine bestimmte Instanz einer Kampagne abzurufen, die über den [Endpunkt `/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) gesendet wurde.

### Wo kann ich es finden?

API- und API-getriggerte Kampagnen, die als Broadcast gesendet werden, generieren automatisch einen Sendebezeichner, wenn kein Sendebezeichner angegeben wird. Wenn Sie einen eigenen Bezeichner für das Senden angeben möchten, müssen Sie diesen zunächst über den [Endpunkt `/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) erstellen. Der Bezeichner muss aus allen ASCII-Zeichen bestehen und darf höchstens 64 Zeichen lang sein. Sie können einen Bezeichner für mehrere Sendungen derselben Kampagne wiederverwenden, wenn Sie die Analytics für diese Sendungen zusammenfassen möchten.

### Wofür kann es verwendet werden?
Senden und verfolgen Sie die Performance von Nachrichten programmgesteuert, ohne dass für jeden Versand eine Kampagne erstellt werden muss.

## Bezeichner der Abo-Gruppe

Ein Bezeichner für Abo-Gruppen oder eine ID für Abo-Gruppen ist ein Schlüssel, der von Braze für eine bestimmte Abo-Gruppe generiert wird. IDs sind für jede Abo-Gruppe eindeutig und können verwendet werden, um Abo-Gruppen über die API zu referenzieren.

### Wo kann ich es finden?

Gehen Sie zu **Zielgruppe** > **Abonnements** und kopieren Sie die ID neben der jeweiligen Abo-Gruppe.

### Wofür kann es verwendet werden?

- Liste der Abo-Gruppen eines Nutzers:innen
- Erfassen Sie den Abo-Gruppenstatus eines Nutzers:innen
- Update des Abo-Gruppenstatus eines Nutzers:innen
