---
nav_title: Benutzer und Segmente
article_title: "Erste Schritte: Benutzer und Segmente"
page_order: 2
page_type: reference
description: "Dieser Artikel gibt Ihnen einen Überblick über Nutzer und Segmente, ihre Bedeutung und wie Sie sie nutzen können, um Ihr Publikum anzusprechen."

---

# Erste Schritte: Benutzer und Segmente

Um personalisierte und gezielte Marketingkampagnen zu versenden, ist es wichtig, Ihre Nutzer zu verstehen und sie effektiv anzusprechen. Dieser Artikel gibt Ihnen einen Überblick über Nutzer und Segmente, ihre Bedeutung und wie Sie sie nutzen können, um Ihr Publikum anzusprechen.

## Nutzer:innen

In Braze werden die Informationen über Ihr Publikum in Nutzerprofilen gespeichert. Ein [Benutzerprofil]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) ist eine umfassende Sammlung von Informationen und Attributen, die einen einzelnen Verbraucher beschreiben. Es dient als zentraler Speicher für die Speicherung und Verwaltung von Daten über ihr Verhalten, ihre Vorlieben und ihre demografischen Daten.

### Teile eines Benutzerprofils

Wenn Sie die Nutzerprofile kennen, können Sie Insights über Ihre Zielgruppe gewinnen und sie gezielt und persönlich ansprechen. Nutzerprofile enthalten eine Vielzahl von Informationen. Dies sind die wichtigsten:

- **Nutzerkennung:** Jedes Benutzerprofil wird durch eine Benutzer-ID, `external_id` genannt, eindeutig identifiziert. Diese Kennung ermöglicht es Braze, Benutzerdaten über verschiedene Kanäle und Geräte hinweg zu verfolgen und zuzuordnen. So erhalten Sie einen einheitlichen Überblick über die Interaktionen der einzelnen Benutzer mit Ihrer Marke. [Anonyme Nutzerprofile]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) (Nutzer, die Ihre Website oder Anwendung besuchen, ohne sich anzumelden) haben kein `external_id`, können aber als alternativer Bezeichner mit [einem Nutzer-Aliasing]({{site.baseurl}}/user_guide/data/user_data_collection/anonymous_users/#assigning-user-aliases) versehen werden.
- [Attribute](#attributes)**:** Dabei handelt es sich um spezifische Informationen über den Benutzer, wie z.B. Name, Alter, Standort oder andere demografische Informationen. Sie können diese Attribute nutzen, um Ihre Zielgruppe zu unterteilen und Ihre Nachrichten zu personalisieren.
- [Ereignisse](#events)**:** Das sind Aktionen, die der Benutzer durchführt, z.B. einen Kauf tätigen, auf einen Link klicken oder eine App öffnen. Braze verfolgt diese Ereignisse, um Ihnen zu helfen, das Verhalten und das Engagement der Benutzer nachzuvollziehen. Ähnlich wie bei Attributen können Sie auch Ereignisse zur Segmentierung und Personalisierung verwenden.
- **Käufe:** In diesem Bereich wird die Kaufhistorie des Benutzers aufgezeichnet. Das ist wichtig, um die Kaufgewohnheiten und Vorlieben der Nutzer zu verstehen.
- **Geräte:** Dieser Abschnitt listet die Geräte auf, die der Nutzer verwendet hat, um mit Ihrer Marke zu interagieren. Dazu gehören mobile Geräte, Webbrowser und verbundene Geräte (wie Wearables und Smart TVs).
- **Engagement:** Dieser Bereich enthält Informationen über die Interaktionen des Benutzers mit den von Ihnen gesendeten Nachrichten, zu welchen Segmenten er gehört, den Abonnementstatus und mehr.
- **Nachrichtenverlauf:** Dies ist eine Aufzeichnung aller Nachrichten, die von dem jeweiligen Nachrichtenkanal (z.B. E-Mail oder Push) an den Benutzer gesendet wurden.

{% alert tip %}
Die SDKs von Braze erfassen automatisch 27 verschiedene Attribute und Ereignisse. Mithilfe dieser Standardereignisse und -attribute können Sie Segmente erstellen, sobald Sie das SDK integrieren.
{% endalert %}

### Attribute

Attribute sind spezifische Merkmale oder Eigenschaften, die mit einem Benutzer verbunden sind. Diese Attribute helfen Ihnen dabei, Nutzer auf der Grundlage ihrer einzigartigen Eigenschaften und Interessen zu segmentieren und anzusprechen. In Braze gibt es zwei Arten von Attributen: Standardattribute und benutzerdefinierte Attribute.

#### Standard-Attribute

Standardattribute sind vorgegebene Attribute, die Sie mit Braze verfolgen können, wenn Sie das SDK in Ihre App integriert haben. Es handelt sich dabei um allgemeine Benutzerinformationen, die für die meisten Apps nützlich sind, wie z. B. demografische Daten und Gerätedaten. Beispiele hierfür sind:

- Vorname
- Nachname
- E-Mail
- Geschlecht
- Geburtsdatum
- Land
- Ort
- Letzte App-Nutzung
- Sprache
- Zeitzone

#### Angepasste Attribute

[Benutzerdefinierte Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) sind Attribute, die Sie auf der Grundlage Ihrer spezifischen Geschäftsanforderungen definieren. Sie ermöglichen es Ihnen, Daten im Blick zu behalten, die Ihre App oder Ihr Unternehmen auszeichnen. 

Eine Musikstreaming-App kann zum Beispiel diese benutzerdefinierten Attribute verfolgen:

- Bevorzugtes Genre
- Anzahl der gespielten Titel
- Premium-Abonnent (Ja/Nein)
- Favorit Künstler

Eine Einzelhandels-App hingegen könnte benutzerdefinierte Attribute wie:

- Bevorzugte Kleidergröße
- Favorisierte Marke
- Anzahl der Käufe
- Mitglied im Treueprogramm (Ja/Nein)

Benutzerdefinierte Attribute geben Ihnen die Möglichkeit, die Daten zu sammeln und zu analysieren, die für Ihr Unternehmen am wichtigsten sind. Sie erfordern jedoch eine zusätzliche Einrichtung.

Sowohl Standard- als auch benutzerdefinierte Attribute können verwendet werden, um Ihre Zielgruppe zu segmentieren und Ihre Marketingbotschaften zu personalisieren. Sie könnten zum Beispiel ein spezielles Angebot an Benutzer in einer bestimmten Stadt (Standardattribut) senden, die mehr als 10 Einkäufe getätigt haben (benutzerdefiniertes Attribut).

### Events

Ereignisse stellen bestimmte Aktionen oder Verhaltensweisen dar, die von Benutzern innerhalb Ihrer App oder Website ausgeführt werden. Ereignisse sind z. B. das Starten von Apps, Käufe, das Aufrufen von Inhalten oder andere Aktionen. Wenn Sie diese Ereignisse verfolgen und analysieren, erhalten Sie Einblicke in Nutzerverhalten und Interaktionsmuster.

#### Standard-Ereignisse

[Standardereignisse]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/events#standard-events) sind vorgegebene Ereignisse, die Braze automatisch verfolgt, wenn das SDK in Ihre App oder Website integriert wurde. Einige Beispiele für Standardereignisse sind:

- **Sitzungsbeginn:** Dieses Ereignis wird ausgelöst, wenn ein Benutzer die App öffnet.
- **Sitzungsende:** Dieses Ereignis wird ausgelöst, wenn ein Benutzer die App schließt.
- **Kauf:** Dieses Ereignis wird ausgelöst, wenn ein Benutzer in der App einen Kauf tätigt.
- **Klick auf Push-Benachrichtigung:** Dieses Ereignis wird ausgelöst, wenn ein Benutzer auf eine Push-Benachrichtigung klickt.

#### Angepasste Events

[Benutzerdefinierte Ereignisse]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) sind Ereignisse, die Sie auf der Grundlage der spezifischen Aktionen definieren, die Sie innerhalb Ihrer App oder Website verfolgen möchten. Eine Musikstreaming-App kann zum Beispiel diese benutzerdefinierten Ereignisse verfolgen:

- Gespielter Song
- Wiedergabeliste erstellt
- Anzeige übersprungen

Eine Fitness-App hingegen könnte benutzerdefinierte Ereignisse wie:

- Workout gestartet
- Workout abgeschlossen
- Persönlicher Rekord aufgestellt

Benutzerdefinierte Ereignisse geben Ihnen die Flexibilität, Aktionen zu verfolgen, die für Ihre App und Ihr Unternehmen am wichtigsten sind. Wie benutzerdefinierte Attribute erfordern sie jedoch eine zusätzliche Einrichtung.

### Datenpunkte

Braze verwendet Datenpunkte, damit Sie die wichtigsten Informationen für Ihr Unternehmen bestimmen können. Datenpunkte sind ein wesentlicher Bestandteil der Funktionsweise von Braze und werden für die Abrechnung, Preisgestaltung und vor allem für die Personalisierung und Optimierung Ihrer Marketingkampagnen verwendet.

Datenpunkte werden verbraucht, wenn die Profildaten von Benutzern aktualisiert werden oder diese bestimmte Aktionen durchführen. Das kann der Beginn oder das Ende einer Sitzung, das Aufzeichnen eines benutzerdefinierten Ereignisses oder ein Kauf sein. Dabei sollte man wissen, dass nicht alle von Braze erfassten Daten als Datenpunkte zählen. So werden beispielsweise Daten und Ereignisse, die standardmäßig von den Braze Services erfasst werden, wie Push-Token, Geräteinformationen und alle Ereignisse zur Verfolgung von Kampagnen, wie das Öffnen von E-Mails und das Anklicken von Push-Benachrichtigungen, nicht als Datenpunkte gezählt.

Wenn Sie sich genau überlegen, was Sie als Datenpunkte verfolgen wollen, können Sie die Daten auswählen, die für Ihre Benutzer am wichtigsten sind. Ihr Braze Account Manager kann Ihnen geeignete Datenpraktiken für Ihre Bedürfnisse empfehlen.

In unseren Artikel zum Thema, erfahren Sie mehr über [Datenpunkte]({{site.baseurl}}/user_guide/data/data_points/).

## Segmente

[Die Segmentierung]({{site.baseurl}}/user_guide/engagement_tools/segments) ermöglicht es Ihnen, Benutzer auf der Grundlage ihrer demografischen, verhaltensbezogenen, sozialen oder technischen Merkmale und Aktionen (d.h. Attribute und Ereignisse) gezielt anzusprechen. Durch den kreativen und intelligenten Einsatz von Segmentierung und automatisierter Nachrichtenübermittlung können Sie Ihre Nutzer nahtlos durch ihren Kundenlebenszyklus führen.

Tipps für die Arbeit mit Segmenten:

- Segmente in Braze sind dynamisch: Benutzer fließen immer in und aus Segmenten, da sie nicht immer die Kriterien erfüllen. Nutzer, die zum Versandzeitpunkt die Kriterien eines Segments erfüllen, erhalten die Kampagne bzw. den Canvas.
    - Wenn Sie statische Segmente wünschen, können Sie die Segmenterweiterungen verwenden. Segmenterweiterungen ([ohne Regeneration]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#extension-regeneration)) bilden die Zielgruppe als Momentaufnahme ab.
- Sie können mehr als einen Filter verwenden. Erstellen Sie exakt abgegrenzte Segmente, indem Sie mehrere Filter übereinander legen.
- Sie können die Aktionen oder Nicht-Aktionen Ihrer Nutzer nutzen, um zu verstehen, wie Sie Ihre Nutzer dort erreichen können, wo sie mit Ihnen in Kontakt treten möchten. Bei diesen Aktionen kann es sich um benutzerdefinierte Ereignisse, die Beteiligung an einer bestehenden Kampagne oder einem Canvas oder sogar um eine bestimmte Nachricht innerhalb eines Canvas handeln.

### Anwendungsfall

Nehmen wir an, Sie betreiben ein Online-Kleidungsgeschäft und haben einen Nachrichtenfluss eingerichtet, um eine Reihe von E-Mails an Benutzer zu senden, die einen Artikel in ihren Einkaufswagen gelegt, den Kauf aber nicht abgeschlossen haben. Infrage kommen etwa eine erste Erinnerungs- oder Anknüpfungsmail mit einem Rabattangebot oder und eine abschließende Erinnerungsmail.

![]({% image_buster /assets/img/getting_started/segment_example.png %}){: style="max-width:70%" }

Sie könnten ein Segment von Benutzern erstellen, die das benutzerdefinierte Ereignis "Artikel in den Warenkorb gelegt" ausgelöst, aber nicht das benutzerdefinierte Ereignis "Kauf abgeschlossen" ausgelöst haben. Innerhalb dieses Segments können Sie dann die Nutzer bestimmen, die die erste Erinnerungsmail geöffnet aber keinen Kauf getätigt haben (Engagement mit einer bestimmten Nachricht).

![]({% image_buster /assets/img/getting_started/segment_example_breakdown.png %})

Dieses Segment könnte dann mit einer aggressiveren Kampagne angesprochen werden, um Käufe anzuregen. Sie könnten ihnen zum Beispiel ein Sonderangebot oder eine persönliche Empfehlung auf der Grundlage der Artikel in ihrem Warenkorb schicken.

Dies ist nur ein Beispiel dafür, wie Sie Benutzeraktionen und -inaktionen, benutzerdefinierte Ereignisse und Engagementdaten nutzen können, um Segmente zu erstellen und Ihre Marketingstrategien in Braze anzupassen.

