---
nav_title: Amazon Personalize
article_title: Amazon Personalize
alias: "/partners/amazon_personalize_overview/"
description: "Dieser referenzierte Artikel beschreibt eine Referenzarchitektur für und die Integration von Braze und Amazon Personalize. In diesem referenzierten Artikel erfahren Sie, welche Anwendungsfälle Amazon Personalize bietet, mit welchen Daten es arbeitet, wie Sie den Dienst konfigurieren und wie Sie ihn in Braze integrieren können."
page_type: partner
search_tag: Partner
---

# Amazon Personalize
<!--
{% multi_lang_include video.html id="xFZ3HMleYYE" align="right" %}
-->
> Amazon Personalize ist so, als hätten Sie Ihr eigenes Empfehlungssystem für maschinelles Lernen, das den ganzen Tag läuft. Basierend auf mehr als 20 Jahren Erfahrung mit Empfehlungen ermöglicht Ihnen Amazon Personalize, das Customer-Engagement zu verbessern, indem es personalisierte Produkt- und Inhaltsempfehlungen in Echtzeit sowie gezielte Marketing-Aktionen ermöglicht.

_Diese Integration wird von Amazon Personalize gepflegt._

## Über die Integration

Mithilfe von maschinellem Lernen und einem Algorithmus, den Sie mit definieren, kann Amazon Personalize Ihnen helfen, ein Modell zu trainieren, das hochwertige Empfehlungen für Ihre Websites und Anwendungen ausgibt. Mit diesen Modellen ist es zulässig, Empfehlungslisten auf der Grundlage des bisherigen Verhaltens der Nutzer:innen zu erstellen, Artikel nach Relevanz zu sortieren und andere Artikel auf der Grundlage von Ähnlichkeiten zu empfehlen. Die von der Amazon Personalize API erhaltenen Listen können dann in Braze Connected-Content verwendet werden, um personalisierte Braze Empfehlungskampagnen durchzuführen. Durch die Integration mit Amazon Personalize haben Kund:in die Freiheit, die Parameter zu kontrollieren, die zum Trainieren der Modelle verwendet werden, und optionale Geschäftsziele zu definieren, die den Output des Algorithmus optimieren. 

In diesem referenzierten Artikel erfahren Sie, welche Anwendungsfälle Amazon Personalize bietet, mit welchen Daten es arbeitet, wie Sie den Dienst konfigurieren und wie Sie ihn in Braze integrieren können.

## Voraussetzungen

| Anforderung| Beschreibung|
| ---| ---| 
| Amazon Internet Service Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein AWS-Konto. Nachdem Sie über ein AWS-Konto verfügen, können Sie über die Amazon Personalize-Konsole, die AWS Command Line Interface (AWS CLI) oder die AWS SDKs auf Amazon Personalize zugreifen. |
| Definierte Anwendungsfälle | Bevor Sie ein Modell erstellen, müssen Sie Ihren Anwendungsfall für diese Integration festlegen. Referenzieren Sie die folgende Liste für gängige Anwendungsfälle. |
| Datensätze | Amazon Personalize Empfehlungsmodelle benötigen drei verschiedene Arten von Datensätzen: Interaktionen, Nutzer:innen und Artikel. Referenzieren Sie die folgenden Details, um die Anforderungen für jeden Datensatz zu sehen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% tabs %}
{% tab Anwendungsfälle %}

**Anwendungsfälle**

Bevor Sie ein Modell erstellen, müssen Sie Ihren Anwendungsfall für diese Integration festlegen. Einige häufige Anwendungsfälle sind:
- Empfehlen Sie Nutzern:innen Artikel auf der Grundlage ihrer bisherigen Interaktionen und schaffen Sie so ein wirklich personalisiertes Erlebnis.
- Stellen Sie eine Liste von Artikeln oder Suchergebnissen bereit, die auf jeden Nutzer zugeschnitten sind, und erhöhen Sie das Engagement, indem Sie Artikel nach Relevanz für den Nutzer:innen anzeigen.
- Finden Sie Empfehlungen für ähnliche Artikel und helfen Sie den Nutzer:innen, neue Dinge zu entdecken.

In der folgenden Anleitung konzentrieren wir uns auf das Rezept der Nutzer:innen für personalisierte Empfehlungen.

{% endtab %}
{% tab Datensätze %}

**Datensätze**

Um mit den Empfehlungsmodellen von Amazon Personalize zu beginnen, benötigen Sie drei Arten von Datensätzen:

- Wechselwirkungen
  - Speichert historische Interaktionen zwischen Nutzer:innen und Artikeln
  - Erfordert die Werte `USER_ID`, `ITEM_ID`, `EVENT_TYPE` und `TIMESTAMP` und akzeptiert optional Metadaten über das Ereignis
- Nutzer:innen
  - Speichert Metadaten über die Nutzer:innen
  - Erfordert einen `USER_ID` Wert und mindestens ein Metadatenfeld (String oder numerisch) wie Geschlecht, Alter, Loyalitätsmitgliedschaft
- Artikel
  - Speichert Metadaten über Artikel
  - Erfordert eine `ITEM_ID` und mindestens ein Metadatenfeld (textuell, kategorisch oder numerisch), das den Artikel beschreibt.

Für ein Rezept für Benutzerempfehlungen müssen Sie einen Interaktionsdatensatz mit mindestens 1000 Datenpunkten von mindestens 25 eindeutigen Nutzer:innen mit jeweils mindestens zwei Interaktionen bereitstellen. Diese Datensätze können in großen Mengen über in S3 gespeicherte CSV-Dateien oder inkrementell über die API hochgeladen werden.

{% endtab %}
{% endtabs %}

## Modelle erstellen

### Schritt 1: Training

Sobald die Datensätze importiert sind, können Sie eine Lösung erstellen. Eine Lösung verwendet eines der Amazon [Personalize-Rezepte](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html) (Algorithmen), um ein Modell zu trainieren. In unserem Fall werden wir das Rezept `USER_PERSONALIZATION` verwenden. Durch das Trainieren der Lösung wird eine Lösungsversion (trainiertes Modell) erstellt, die Sie anhand der Performance-Metriken des Modells bewerten können.

Mit Amazon Personalize können Sie die Hyperparameter anpassen, die das Modell beim Training verwendet. Zum Beispiel:
- Mit dem Parameter "Perzentil der Länge des Nutzer:innen-Verlaufs" in der Amazon Personalize-Konsole können Sie das Perzentil des Nutzer:innen-Verlaufs anpassen, das beim Training berücksichtigt werden soll:<br><br>![Minimal-/Maximaleinstellung des Nutzerprofils]({% image_buster /assets/img/amazon_personalize/min_and_max_user_percentile.png %})
  - `min_user_history_length_percentile`: schließt einen Prozentsatz der Nutzer:innen mit sehr kurzen Verläufen aus, was hilfreich sein kann, um beliebte Artikel zu eliminieren und Empfehlungen zu erstellen, die auf tiefer liegenden Mustern basieren.
  - `max_user_history_length_percentile`Adjustieren Sie den Prozentsatz der Nutzer:innen, der beim Training mit sehr langen Verläufen berücksichtigt werden soll.

Die Anzahl der ausgeblendeten Dimensionen hilft, kompliziertere Muster für komplexe Datensätze zu erkennen, während die Back-Propagation-Through-Time-Technik (BPTT) die Rewards für ein frühes Ereignis anpasst, nachdem eine Kette von Ereignissen stattgefunden hat, die zu einer hochwertigen Aktion geführt haben.

Zusätzlich bietet Amazon Personalize eine automatische Abstimmung der Hyperparameter, indem mehrere Versionen der Lösung mit unterschiedlichen Werten gleichzeitig ausgeführt werden. Um die Abstimmung zu nutzen, aktivieren Sie **HPO durchführen**, wenn Sie eine Lösung erstellen.

### Schritt 2: Auswerten und vergleichen

Sobald Sie eine Lösung trainiert haben, können Sie sie bewerten und verschiedene Versionen vergleichen. Jede Version der Lösung zeigt die berechneten Metriken an. Einige der verfügbaren Metriken sind:

- **Normalisieren des diskontierten kumulativen Gewinns:** vergleicht die empfohlene Reihenfolge der Artikel mit der tatsächlichen Liste der Artikel und gibt jedem Artikel ein Gewicht, das seiner Position in der Liste entspricht
- **Präzision @k:** die Anzahl der richtig empfohlenen Artikel geteilt durch die Anzahl aller empfohlenen Artikel, wobei `k` die Anzahl der Artikel ist
- **Mittlerer reziproker Rang:** konzentriert sich auf die erste, höchstrangige Empfehlung und berechnet, wie viele empfohlene Artikel gesehen werden, bevor die erste übereinstimmende Empfehlung erscheint
- **Abdeckungsgrad:** der Anteil der eindeutig empfohlenen Artikel an der Gesamtzahl der eindeutigen Artikel im Datensatz

## Empfehlungen erhalten

Sobald Sie eine Version der Lösung erstellt haben, mit der Sie zufrieden sind, ist es an der Zeit, die Empfehlungen in die Tat umzusetzen. Es gibt zwei Möglichkeiten, auf die Empfehlungen zuzugreifen:

1. Kampagne in Echtzeit<br>Eine Kampagne ist eine eingesetzte Version der Lösung mit einem definierten Mindestdurchsatz an Transaktionen. Eine Transaktion ist ein einzelner API-Aufruf, um die Ausgabe einer Empfehlung zu erhalten. Sie ist definiert als TPS oder Transaktionen pro Sekunde mit einem Mindestwert von eins. Die Kampagne skaliert die Ressourcen im Falle einer erhöhten Belastung, fällt aber nicht unter Ihren Mindestwert. Sie können die Empfehlungen in der Konsole, AWS CLI oder über AWS SDKs in Ihrem Code abfragen.<br><br>
2. Stapelverarbeitungsauftrag<br>Ein Batch-Auftrag exportiert die Empfehlungen in ein S3-Bucket. Der Auftrag nimmt als Input eine JSON-Datei mit einer Liste von Nutzer:innen, für die Sie die Empfehlungen exportieren möchten. Nachdem Sie die richtigen Berechtigungen und das Ausgabeziel angegeben haben, können Sie den Auftrag ausführen. Die Laufzeit hängt von der Größe Ihrer Datensätze und der Länge der Empfehlungsliste ab.

### Filter

Mit den Filtern können Sie die Ausgabe der Empfehlungen anpassen, indem Sie Artikel auf der Grundlage der ID des Artikels, des Ereignistyps oder der Metadaten ausschließen. Sie können Nutzer:innen auch anhand ihrer Metadaten filtern, z.B. Alter oder Status der Treue-Mitgliedschaft. Filter können nützlich sein, um zu verhindern, dass Artikel empfohlen werden, mit denen der Nutzer:innen bereits interagiert hat.

## Integration der Ergebnisse in Braze

Mit dem erstellten Modell und der Empfehlungskampagne sind Sie bereit, eine Braze-Kampagne für Ihre Nutzer:innen mit Content-Cards und Connected-Content durchzuführen.
Bevor Sie eine Kampagne von Braze starten, müssen Sie einen Dienst erstellen, der diese Empfehlungen über eine API bereitstellen kann. Sie können [Schritt 3 des Workshop-Artikels]({{site.baseurl}}/partners/amazon_personalize_workshop/#step-3-send-personalized-emails-from-braze) befolgen, um den Dienst mit Hilfe der AWS Dienste bereitzustellen. Sie können auch Ihren eigenen unabhängigen Backend-Dienst einsetzen, der die Empfehlungen bereitstellt.

### Content-Card-Kampagne Anwendungsfall

Lassen Sie uns eine Content-Card-Kampagne mit dem ersten empfohlenen Artikel aus der Liste durchführen.<br><br>
In den folgenden Beispielen werden wir Folgendes abfragen
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

Erstellen Sie im Braze-Dashboard eine neue [Content-Card-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/). Erstellen Sie im Feld für den Nachrichtentext einen Connected-Content Liquid-Block, um die API abzufragen und die Antwort in der Variablen `recommendations` zu speichern:

{% raw %}

```liquid
{% connected_content https:/<service-endpoint.com>/recommendations?user_id={{${user_id}}} :save recommendations %}
```

Sie können dann den ersten Artikel im resultierenden Array referenzieren und dem Nutzer:innen den Inhalt anzeigen:

```liquid
This seems like a great fit for you:
{% recommendations[0].name %}
{% recommendations[0].price %}
```

{% endraw %}

Einschließlich des Titels, des Bildes und der Verlinkung der URL würde die komplette Content-Card so aussehen:

![Ein Bild einer Kampagne mit Connected-Content, das dem Nachrichtentext und dem Feld "Bild hinzufügen" hinzugefügt wurde. Dieses Bild zeigt auch die Connected-Content-Logik, die dem Feld "Redirect to Internet URL" hinzugefügt wurde und die Nutzer:innen mit einer Empfehlungs-URL verbindet.]({% image_buster /assets/img/amazon_personalize/content-card-campaign.png %})


