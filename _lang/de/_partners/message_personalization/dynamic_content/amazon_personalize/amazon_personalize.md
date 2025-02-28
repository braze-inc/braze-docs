---
nav_title: Amazon Personalisieren
article_title: Amazon Personalisieren
alias: /partners/amazon_personalize/
description: "Dieser Referenzartikel beschreibt eine Referenzarchitektur für und die Integration von Braze und Amazon Personalize. Dieser Referenzartikel hilft Ihnen, die Anwendungsfälle zu verstehen, die Amazon Personalize bietet, die Daten, mit denen es arbeitet, die Konfiguration des Dienstes und die Integration mit Braze."
page_type: partner
search_tag: Partner
---

# Amazon Personalisieren
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
> Amazon Personalize ist wie Ihr eigenes maschinelles Empfehlungssystem von Amazon, das den ganzen Tag über arbeitet. Amazon Personalize basiert auf mehr als 20 Jahren Erfahrung mit Empfehlungen und ermöglicht es Ihnen, die Kundenbindung zu verbessern, indem es personalisierte Produkt- und Inhaltsempfehlungen in Echtzeit und gezielte Marketingaktionen ermöglicht.

Mithilfe von maschinellem Lernen und einem von Ihnen mitdefinierten Algorithmus kann Amazon Personalize Ihnen helfen, ein Modell zu trainieren, das hochwertige Empfehlungen für Ihre Websites und Anwendungen ausgibt. Mit diesen Modellen können Sie Empfehlungslisten erstellen, die auf dem früheren Verhalten der Nutzer basieren, Artikel nach Relevanz sortieren und andere Artikel auf der Grundlage von Ähnlichkeiten empfehlen. Die von der Amazon Personalize API erhaltenen Listen können dann in Braze Connected Content verwendet werden, um personalisierte Braze Empfehlungskampagnen durchzuführen. Durch die Integration mit Amazon Personalize haben Kunden die Freiheit, die Parameter zu kontrollieren, die zum Trainieren der Modelle verwendet werden, und optionale Geschäftsziele zu definieren, die den Output des Algorithmus optimieren. 

Dieser Referenzartikel hilft Ihnen, die Anwendungsfälle zu verstehen, die Amazon Personalize bietet, die Daten, mit denen es arbeitet, die Konfiguration des Dienstes und die Integration mit Braze.

## Voraussetzungen

| Anforderung| Beschreibung|
| ---| ---| 
| Amazon Web Service-Konto | Ein AWS-Konto ist erforderlich, um die Vorteile dieser Partnerschaft zu nutzen. Nachdem Sie ein AWS-Konto haben, können Sie über die Amazon Personalize-Konsole, die AWS-Befehlszeilenschnittstelle (AWS CLI) oder die AWS SDKs auf Amazon Personalize zugreifen. |
| Definierte Anwendungsfälle | Bevor Sie ein Modell erstellen, müssen Sie Ihren Anwendungsfall für diese Integration festlegen. In der folgenden Liste finden Sie häufige Anwendungsfälle. |
| Datensätze | Amazon Personalize Empfehlungsmodelle benötigen drei verschiedene Arten von Datensätzen: Interaktionen, Benutzer und Artikel. Lesen Sie die folgenden Details, um die Anforderungen für jeden Datensatz zu sehen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% tabs %}
{% tab Anwendungsfälle %}

**Anwendungsfälle**

Bevor Sie ein Modell erstellen, müssen Sie Ihren Anwendungsfall für diese Integration festlegen. Einige häufige Anwendungsfälle sind:
- Empfehlen Sie Nutzern Artikel auf der Grundlage ihrer früheren Interaktionen und schaffen Sie so ein wirklich personalisiertes Erlebnis für Ihre Nutzer.
- Bieten Sie eine Liste von Artikeln oder Suchergebnissen an, die auf jeden Benutzer zugeschnitten sind, und erhöhen Sie das Engagement, indem Sie Artikel nach Relevanz für den Benutzer anzeigen.
- Finden Sie Empfehlungen für ähnliche Artikel und helfen Sie den Nutzern, neue Dinge zu entdecken.

In der folgenden Anleitung werden wir uns auf das Rezept für benutzerdefinierte Empfehlungen konzentrieren.

{% endtab %}
{% tab Datensätze %}

**Datensätze**

Um mit den Amazon Personalize Empfehlungsmodellen zu beginnen, benötigen Sie drei Arten von Datensätzen:

- Wechselwirkungen
  - Speichert historische Interaktionen zwischen Benutzern und Objekten
  - Erfordert die Werte `USER_ID`, `ITEM_ID`, `EVENT_TYPE` und `TIMESTAMP` und akzeptiert optional Metadaten über das Ereignis
- Nutzer:innen
  - Speichert Metadaten über die Benutzer
  - Erfordert einen `USER_ID` Wert und mindestens ein Metadatenfeld (String oder numerisch) wie Geschlecht, Alter, Treue-Mitgliedschaft
- Artikel
  - Speichert Metadaten über Objekte
  - Erfordert eine `ITEM_ID` und mindestens ein Metadatenfeld (textuell, kategorisch oder numerisch), das den Artikel beschreibt.

Für ein Rezept für Benutzerempfehlungen müssen Sie einen Interaktionsdatensatz bereitstellen, der mindestens 1000 Interaktionspunkte von mindestens 25 einzelnen Benutzern mit jeweils mindestens zwei Interaktionen enthält. Diese Datensätze können in großen Mengen mit Hilfe von in S3 gespeicherten CSV-Dateien oder inkrementell über die API hochgeladen werden.

{% endtab %}
{% endtabs %}

## Modelle erstellen

### Schritt 1: Ausbildung

Sobald die Datensätze importiert sind, können Sie eine Lösung erstellen. Eine Lösung verwendet eines der Amazon [Personalize-Rezepte](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html) (Algorithmen), um ein Modell zu trainieren. In unserem Fall werden wir das Rezept `USER_PERSONALIZATION` verwenden. Durch das Trainieren der Lösung wird eine Lösungsversion (trainiertes Modell) erstellt, die Sie anhand der Leistungsmetriken des Modells bewerten können.

Mit Amazon Personalize können Sie die Hyperparameter anpassen, die das Modell für das Training verwendet. Zum Beispiel:
- Mit dem Parameter "Perzentil der Benutzerhistorie", den Sie in der Amazon Personalize-Konsole finden, können Sie das Perzentil der Benutzerhistorie einstellen, das in das Training einbezogen werden soll:<br><br>![Min-Max Benutzerprofileinstellung][3]
  - `min_user_history_length_percentile`: schließt einen Prozentsatz von Nutzern mit sehr kurzen Verläufen aus, was hilfreich sein kann, um beliebte Artikel zu eliminieren und Empfehlungen zu erstellen, die auf tiefer liegenden Mustern basieren.
  - `max_user_history_length_percentile`: Passen Sie den Prozentsatz der Benutzer an, der beim Training mit sehr langen Historien berücksichtigt werden soll.

Die Anzahl der versteckten Dimensionen hilft dabei, kompliziertere Muster für komplexe Datensätze zu erkennen, während die Back-Propagation-Through-Time-Technik (BPTT) die Belohnungen für ein frühes Ereignis anpasst, nachdem eine Kette von Ereignissen stattgefunden hat, die zu einer wertvollen Aktion geführt haben.

Außerdem bietet Amazon Personalize eine automatische Abstimmung der Hyperparameter, indem mehrere Versionen der Lösung mit unterschiedlichen Werten gleichzeitig ausgeführt werden. Um die Abstimmung zu verwenden, aktivieren Sie **HPO durchführen**, wenn Sie eine Lösung erstellen.

### Schritt 2: Auswerten und vergleichen

Sobald eine Lösung die Schulung abgeschlossen hat, können Sie sie bewerten und verschiedene Versionen vergleichen. Jede Lösungsversion zeigt berechnete Metriken an. Einige der verfügbaren Metriken sind:

- **Normalisieren des diskontierten kumulativen Gewinns:** vergleicht die empfohlene Reihenfolge der Artikel mit der tatsächlichen Liste der Artikel und gibt jedem Artikel ein Gewicht, das seiner Position in der Liste entspricht
- **Präzision @k:** die Anzahl der richtig empfohlenen Artikel geteilt durch die Anzahl aller empfohlenen Artikel, wobei `k` die Anzahl der Artikel ist
- **Mittlerer reziproker Rang:** konzentriert sich auf die erste, höchstrangige Empfehlung und berechnet, wie viele empfohlene Artikel gesehen werden, bevor die erste übereinstimmende Empfehlung erscheint
- **Abdeckungsgrad:** der Anteil der eindeutigen empfohlenen Artikel an der Gesamtzahl der eindeutigen Artikel im Datensatz

## Empfehlungen erhalten

Sobald Sie eine Lösungsversion erstellt haben, mit der Sie zufrieden sind, ist es an der Zeit, die Empfehlungen in die Tat umzusetzen. Es gibt zwei Möglichkeiten, auf die Empfehlungen zuzugreifen:

1. Kampagne in Echtzeit<br>Eine Kampagne ist eine eingesetzte Lösungsversion mit einem bestimmten Mindesttransaktionsdurchsatz. Eine Transaktion ist ein einzelner API-Aufruf zum Abrufen der Empfehlungsausgabe. Sie ist als TPS (Transaktionen pro Sekunde) mit einem Mindestwert von eins definiert. Die Kampagne skaliert die Ressourcen im Falle einer erhöhten Belastung, fällt aber nicht unter den von Ihnen festgelegten Mindestwert. Sie können die Empfehlungen in der Konsole, AWS CLI oder über AWS SDKs in Ihrem Code abfragen.<br><br>
2. Stapelverarbeitungsauftrag<br>Ein Batch-Auftrag exportiert die Empfehlungen in einen S3-Bucket. Der Auftrag nimmt als Eingabe eine JSON-Datei mit einer Liste von Benutzer-IDs entgegen, für die Sie die Empfehlungen exportieren möchten. Nachdem Sie die richtigen Berechtigungen und das Ausgabeziel angegeben haben, können Sie den Auftrag ausführen. Die Laufzeit hängt von der Größe Ihrer Datensätze und der Länge der Empfehlungsliste ab.

### Filter

Mit den Filtern können Sie die Ausgabe der Empfehlungen anpassen, indem Sie Artikel auf der Grundlage der Artikel-ID, des Ereignistyps oder der Metadaten ausschließen. Sie können Benutzer auch nach ihren Metadaten filtern, z. B. nach Alter oder Status der Treue-Mitgliedschaft. Filter können sich als nützlich erweisen, um zu verhindern, dass Artikel empfohlen werden, mit denen der Benutzer bereits interagiert hat.

## Integration der Ergebnisse mit Braze

Mit dem erstellten Modell und der Empfehlungskampagne sind Sie bereit, eine Braze-Kampagne für Ihre Benutzer mit Content Cards und Connected Content durchzuführen.
Bevor Sie eine Braze-Kampagne starten, müssen Sie einen Service erstellen, der diese Empfehlungen über eine API bereitstellen kann. Sie können [Schritt 3 im Workshop-Artikel][1] befolgen, um den Service mit AWS-Services bereitzustellen. Sie können auch Ihren eigenen, unabhängigen Backend-Dienst einsetzen, der die Empfehlungen liefert.

### Anwendungsfall der Content Card Kampagne

Lassen Sie uns eine Content Card-Kampagne mit dem ersten empfohlenen Artikel aus der Liste starten.<br><br>
In den folgenden Beispielen werden wir folgende Abfragen durchführen
`GET http://<service-endpoint.com>/recommendations?user_id=user123` Endpunkt mit einem `user_id` Parameter, der eine Liste der empfohlenen Artikel zurückgibt:

```json
[
  {
    "id": "abc123",
    "url": "http://productpage.com/product/abc123",
    "name": "First Item",
    "price": 39.99,
    "image": "http://pp.cdn.com/abvh3321pjb1j"
  },
  {
    "id": "xyz987",
    "url": "http://productpage.com/product/xyz987",
    "name": "Great Item",
    "price": 19.99,
    "image": "http://pp.cdn.com/234bjl1gioj1b2b"
  },
  ...
]
```

Erstellen Sie im Braze Dashboard eine neue [Content Card Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/). Erstellen Sie im Feld Nachrichtentext einen Connected Content Liquid-Block, um die API abzufragen und die Antwort in der Variablen `recommendations` zu speichern:

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

Sie können dann auf das erste Element im resultierenden Array verweisen und den Inhalt für den Benutzer anzeigen:

```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

Einschließlich des Titels, des Bildes und der Verlinkung der URL würde die vollständige Content Card so aussehen:

![Ein Bild einer Kampagne mit Connected Content, das dem Nachrichtentext und dem Feld "Bild hinzufügen" hinzugefügt wurde. Dieses Bild zeigt auch die Logik von Connected Content, die dem Feld "Redirect to Web URL" hinzugefügt wurde und die Benutzer mit einer Empfehlungs-URL verbindet.][2]

[1]: {{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/workshop/#step-3-send-personalized-emails-from-braze
[2]: {% image_buster /assets/img/amazon_personalize/content-card-campaign.png %}
[3]: {% image_buster /assets/img/amazon_personalize/min_and_max_user_percentile.png %}