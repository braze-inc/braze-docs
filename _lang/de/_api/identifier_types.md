---
nav_title: "API-Bezeichner-Typen"
article_title: API-Bezeichner-Typen
page_order: 2.2
toc_headers: h2
description: "Dieser Referenzartikel behandelt die verschiedenen Arten von API-Kennungen, die im Braze Dashboard vorhanden sind, wo Sie sie finden können und wofür sie verwendet werden." 
page_type: reference

---

# API-Kennungstypen

> Dieser Leitfaden beschreibt die verschiedenen Arten von API-Kennungen, die im Braze Dashboard zu finden sind, ihren Zweck, wo Sie sie finden können und wie sie normalerweise verwendet werden. Informationen über REST-API-Schlüssel oder Arbeitsbereich-API-Schlüssel finden Sie in der [API-Übersicht]({{site.baseurl}}/api/api_key/).

Die folgenden Identifikatoren können verwendet werden, um von der externen API von Braze aus auf Ihre Vorlage, Ihr Canvas, Ihre Kampagne, Ihr Segment, Ihren Versand oder Ihre Karte zuzugreifen. Alle Nachrichten sollten in [UTF-8](https://en.wikipedia.org/wiki/UTF-8) kodiert sein.

## App Kennung

Die App-Kennung oder `app_id` ist ein Parameter, der eine Aktivität mit einer bestimmten App in Ihrem Arbeitsbereich verbindet. Es zeigt an, mit welcher App innerhalb des Arbeitsbereichs Sie interagieren. Sie werden zum Beispiel feststellen, dass Sie eine `app_id` für Ihre iOS-App, eine `app_id` für Ihre Android-App und eine `app_id` für Ihre Web-Integration haben werden. Bei Braze kann es vorkommen, dass Sie mehrere Apps für dieselbe Plattform haben, und zwar für die verschiedenen Plattformtypen, die Braze unterstützt.

### Wo kann ich es finden?

Es gibt zwei Möglichkeiten, Ihr `app_id` zu finden:

{% tabs lokal %}
{% tab App-Identifikatoren %}
Gehen Sie zu **Einstellungen** > **APIs und Identifikatoren** > **App-Identifikatoren**. Ihr API-Schlüssel für jede App ist in der Spalte **Kennung** aufgeführt.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **die App-Kennungen** unter **Entwicklerkonsole** > **API-Einstellungen**.
{% endalert %}
{% endtab %}

{% tab App-Einstellungen %}
Gehen Sie zu **Einstellungen** > **App-Einstellungen**. Ihr API-Schlüssel ist neben dem Feld **API-Schlüssel** im Bereich Einstellungen aufgeführt.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **die App-Einstellungen** unter **Einstellungen verwalten** > **Einstellungen**.
{% endalert %}
{% endtab %}
{% endtabs %}

### Wofür kann es verwendet werden?

App-Identifikatoren bei Braze werden bei der Integration des SDK verwendet und dienen auch dazu, eine bestimmte App in REST-API-Aufrufen zu referenzieren. Mit `app_id` können Sie viele Dinge tun, wie z.B. Daten für ein benutzerdefiniertes Ereignis, das für eine bestimmte App aufgetreten ist, abrufen, Deinstallationsstatistiken, Statistiken über neue Benutzer, DAU-Statistiken und Statistiken über den Sitzungsbeginn für eine bestimmte App.

{% alert tip %}
Manchmal kann es vorkommen, dass Sie zur Eingabe von `app_id` aufgefordert werden, aber nicht mit einer App arbeiten. Da es sich um ein Legacy-Feld handelt, das für eine bestimmte Plattform spezifisch ist, können Sie dieses Feld auslassen, indem Sie eine beliebige Zeichenfolge als Platzhalter für diesen erforderlichen Parameter einfügen.
{% endalert %}

### Mehrere App-Identifikatoren

Während der SDK-Einrichtung ist der häufigste Anwendungsfall für mehrere App-Identifikatoren die Trennung dieser Identifikatoren für Debug- und Release-Build-Varianten.

Um in Ihren Builds einfach zwischen mehreren App-Identifikatoren wechseln zu können, empfehlen wir, für jede relevante [Build-Variante](https://developer.android.com/studio/build/build-variants.html) eine eigene `braze.xml` Datei zu erstellen. Eine Build-Variante ist eine Kombination aus Build-Typ und Produktvariante. Standardmäßig wird ein neues Android-Projekt mit den Build-Typen `debug` und `release` und ohne Product Flavors konfiguriert.

Erstellen Sie für jede relevante Build-Variante eine neue `braze.xml` in `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
Wenn die Build-Variante kompiliert wird, wird sie den neuen Bezeichner verwenden.

## Identifikator der Vorlage

Ein [Vorlagenbezeichner]({{site.baseurl}}/api/endpoints/templates/) oder eine Vorlagen-ID ist ein zufälliger Schlüssel, der von Braze für eine bestimmte Vorlage im Dashboard generiert wird. Vorlagen-IDs sind für jede Vorlage eindeutig und können verwendet werden, um Vorlagen über die API zu referenzieren. 

Vorlagen sind ideal, wenn Ihr Unternehmen Ihre HTML-Designs für Kampagnen in Auftrag gibt. Nachdem Sie die Vorlagen erstellt haben, verfügen Sie nun über eine Vorlage, die sich nicht auf eine bestimmte Kampagne bezieht, sondern auf eine Reihe von Kampagnen wie einen Newsletter angewendet werden kann.

### Wo kann ich es finden?

Sie können Ihre Vorlagen-ID auf zwei Arten finden:

{% tabs lokal %}
{% tab Vorlagen %}
Gehen Sie zu **Vorlagen**, wählen Sie eine Vorlagenseite und dann eine bereits vorhandene Vorlage aus. Wenn die von Ihnen gewünschte Vorlage noch nicht existiert, erstellen Sie eine und speichern Sie sie. Unten auf der Seite der einzelnen Vorlagen finden Sie die Kennung Ihrer Vorlage.
{% endtab %}

{% tab API-Schlüssel %}
Gehen Sie zu **Einstellungen** > **APIs und Identifikatoren**. Hier bietet Braze eine Suche nach **zusätzlichen API-Identifikatoren** an, mit der Sie bestimmte Identifikatoren nachschlagen können.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie die API-Kennungen unter **Entwicklerkonsole** > **API-Einstellungen**.
{% endalert %}
{% endtab %}
{% endtabs %}

### Wofür kann es verwendet werden?

- Vorlagen über API aktualisieren
- Informationen über eine bestimmte Vorlage abrufen

## Kennung der Leinwand

Eine [Canvas-Kennung]({{site.baseurl}}/user_guide/engagement_tools/canvas/) oder Canvas-ID ist ein zufälliger Schlüssel, der von Braze für ein bestimmtes Canvas im Dashboard generiert wird. Canvas-IDs sind für jedes Canvas eindeutig und können verwendet werden, um über die API auf Canvas zu verweisen. 

Denken Sie daran: Wenn Sie eine Leinwand mit Varianten haben, gibt es sowohl eine allgemeine Leinwand-ID als auch individuelle Leinwand-IDs, die unter der Hauptleinwand verschachtelt sind. 

### Wo kann ich es finden?

Sie können Ihre Canvas-ID im Dashboard finden. Gehen Sie zu **Nachrichten** > **Canvas** und wählen Sie ein bereits vorhandenes Canvas. Wenn das gewünschte Canvas noch nicht existiert, erstellen Sie es und speichern es. Klicken Sie unten auf einer einzelnen Canvas-Seite auf **Varianten analysieren**. Es erscheint ein Fenster mit der Canvas-API-Kennung am unteren Rand.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, befindet sich **Canvas** unter **Engagement**.
{% endalert %}

### Wofür kann es verwendet werden?

- Verfolgen Sie die Analysen zu einer bestimmten Nachricht
- Erfassen Sie hochrangige aggregierte Statistiken zur Canvas-Leistung
- Details zu einem bestimmten Canvas abrufen
- Mit Currents, um Daten auf Benutzerebene für ein "größeres Bild" in Canvases einzubringen
- Mit API-Trigger-Zustellung, um Statistiken für Transaktionsnachrichten zu sammeln

## Kennung der Kampagne

Ein [Kampagnenbezeichner]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) oder eine Kampagnen-ID ist ein zufälliger Schlüssel, der von Braze für eine bestimmte Kampagne im Dashboard generiert wird. Kampagnen-IDs sind für jede Kampagne eindeutig und können verwendet werden, um Kampagnen über die API zu referenzieren. 

Denken Sie daran: Wenn Sie eine Kampagne mit Varianten haben, gibt es sowohl eine allgemeine Kampagnen-ID als auch individuelle Kampagnen-IDs für die Varianten, die unter der Hauptkampagne eingebettet sind. 

### Wo kann ich es finden?

Sie können Ihre Kampagnen-ID auf zwei Arten finden:

{% tabs lokal %}
{% tab Kampagnen %}
Gehen Sie zu **Messaging** > **Kampagnen** und wählen Sie eine bereits bestehende Kampagne aus. Wenn die von Ihnen gewünschte Kampagne noch nicht existiert, erstellen Sie eine und speichern Sie sie. Unten auf der Seite der einzelnen Kampagnen finden Sie Ihre **Kampagnen-API-Kennung**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Kampagnen** unter **Engagement**.
{% endalert %}
{% endtab %}

{% tab API-Schlüssel %}
Gehen Sie zu **Einstellungen** > **APIs und Identifikatoren**. Hier bietet Braze eine Suche nach **zusätzlichen API-Identifikatoren** an, mit der Sie bestimmte Identifikatoren nachschlagen können.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie die **API-Schlüssel** unter **Entwicklerkonsole** > **API-Einstellungen**.
{% endalert %}
{% endtab %}
{% endtabs %}

### Wofür kann es verwendet werden?

- Verfolgen Sie die Analysen zu einer bestimmten Nachricht
- Erfassen Sie aggregierte Statistiken zur Kampagnenleistung auf höchster Ebene
- Details zu einer bestimmten Kampagne abrufen
- Mit Currents, um Daten auf Benutzerebene für einen "ganzheitlichen" Ansatz für Kampagnen einzubringen
- Mit API-gesteuerter Zustellung, um Statistiken für Transaktionsnachrichten zu sammeln
- So [suchen Sie]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/#search-syntax) auf der Seite **Kampagnen** mithilfe des Filters [nach einer bestimmten Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/#search-syntax)  `api_id:YOUR_API_ID`

## Segment-Bezeichner

Ein [Segmentbezeichner]({{site.baseurl}}/user_guide/engagement_tools/segments/) oder eine Segment-ID ist ein zufälliger Schlüssel, der von Braze für ein bestimmtes Segment innerhalb des Dashboards generiert wird. Segment-IDs sind für jedes Segment eindeutig und können verwendet werden, um Segmente über die API zu referenzieren. 

### Wo kann ich es finden?

Sie können Ihre Segment-ID auf zwei Arten finden:

{% tabs lokal %}
{% tab Segmente %}
Gehen Sie zu **Zielgruppe** > **Segmente** und wählen Sie ein bereits vorhandenes Segment aus. Wenn das von Ihnen gewünschte Segment noch nicht existiert, erstellen Sie es und speichern es. Unten auf der Seite mit den einzelnen Segmenten finden Sie die Kennung Ihres Segments.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie die **Segmente** unter **Engagement**.
{% endalert %}
{% endtab %}

{% tab API-Schlüssel %}
Gehen Sie zu **Einstellungen** > \*\*APIs**und Bezeichner**. Hier bietet Braze eine Suche nach **zusätzlichen API-Identifikatoren** an, mit der Sie bestimmte Identifikatoren nachschlagen können.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie die **API-Schlüssel** unter **Entwicklerkonsole** > **API-Einstellungen**.
{% endalert %}
{% endtab %}
{% endtabs %}

### Wofür kann es verwendet werden?
- Details zu einem bestimmten Segment abrufen
- Abrufen von Analysen eines bestimmten Segments
- Ziehen Sie ab, wie oft ein benutzerdefiniertes Ereignis für ein bestimmtes Segment aufgezeichnet wurde
- Legen Sie eine Kampagne fest und senden Sie sie von der API aus an die Mitglieder eines Segments.

## Kennung der Karte

Ein Kartenidentifikator oder eine Karten-ID ist ein zufälliger Schlüssel, der von Braze für eine bestimmte News Feed-Karte im Dashboard generiert wird. Die Karten-IDs sind für jede [News Feed-Karte]({{site.baseurl}}/user_guide/engagement_tools/news_feed/) eindeutig und können verwendet werden, um über die API auf Karten zu verweisen. 

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

### Wo kann ich es finden?

Sie können Ihre Karten-ID auf zwei Arten finden:

{% tabs lokal %}
{% tab News Feed %}
Gehen Sie zu **Nachrichten** > **News Feed** und wählen Sie einen bereits vorhandenen News Feed aus. Wenn der von Ihnen gewünschte News Feed noch nicht existiert, erstellen Sie ihn und speichern ihn. Unten auf der jeweiligen News-Feed-Seite finden Sie Ihre eindeutige Kartenkennung.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **News Feed** unter **Engagement**.
{% endalert %}
{% endtab %}

{% tab API-Schlüssel %}
Gehen Sie zu **Einstellungen** > **APIs und Identifikatoren**. Hier bietet Braze eine Suche nach **zusätzlichen API-Identifikatoren** an, mit der Sie bestimmte Identifikatoren nachschlagen können.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie die **API-Schlüssel** unter **Entwicklerkonsole** > **API-Einstellungen**.
{% endalert %}
{% endtab %}
{% endtabs %}

### Wofür kann es verwendet werden?

- Abrufen von relevanten Informationen auf einer Karte
- Verfolgen Sie Ereignisse im Zusammenhang mit Content Cards und Engagement

## Kennung senden

Eine Sendekennung oder Sende-ID ist ein Schlüssel, der entweder von Braze generiert oder von Ihnen für eine bestimmte gesendete Nachricht erstellt wurde und unter dem die Analysen nachverfolgt werden sollen. Die Sendekennung ermöglicht es Ihnen, Analysen für eine bestimmte Instanz einer über den [Endpunkt`/sends/data_series` ]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/) gesendeten Kampagne abzurufen.

### Wo kann ich es finden?

API- und API-ausgelöste Kampagnen, die als Broadcast gesendet werden, erzeugen automatisch eine Sendekennung, wenn keine Sendekennung angegeben wird. Wenn Sie Ihre eigene Sendekennung angeben möchten, müssen Sie diese zunächst über den [Endpunkt`/sends/id/create` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/) erstellen. Der Bezeichner muss aus allen ASCII-Zeichen bestehen und darf höchstens 64 Zeichen lang sein. Sie können eine Sendekennung für mehrere Sendungen derselben Kampagne wiederverwenden, wenn Sie die Analysen dieser Sendungen zusammenfassen möchten.

### Wofür kann es verwendet werden?
Versenden und verfolgen Sie die Leistung Ihrer Nachrichten programmatisch, ohne dass Sie für jeden Versand eine Kampagne erstellen müssen.

## Kennung der Abonnementgruppe

Eine Abonnementgruppen-Kennung oder Abonnementgruppen-ID ist ein Schlüssel, der von Braze für eine bestimmte Abonnementgruppe generiert wird. Die IDs sind für jede Abonnementgruppe eindeutig und können verwendet werden, um Abonnementgruppen über die API zu referenzieren.

### Wo kann ich es finden?

Gehen Sie zu **Audience** > **Abonnements** und kopieren Sie die ID neben der jeweiligen Abonnementgruppe.

### Wofür kann es verwendet werden?

- Liste der Abonnementgruppen eines Benutzers
- Den Status der Abonnementgruppe eines Benutzers abrufen
- Den Status der Abonnementgruppe eines Benutzers aktualisieren
