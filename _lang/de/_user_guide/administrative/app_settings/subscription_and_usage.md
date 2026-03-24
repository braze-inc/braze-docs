---
nav_title: Abrechnung
article_title: Abrechnung
alias: /subscription_and_usage/
page_order: 25
page_type: reference
description: "Dieser Referenzartikel behandelt die Seite Abrechnung, auf der Sie Ihren Datenverbrauch überwachen und überprüfen können."
tool: Dashboard
search_rank: 5
---

# Abrechnung

> Erfahren Sie, wie Sie die **Abrechnungsseite** verwenden, um Ihren Datenverbrauch über Arbeitsbereiche, Anwendungen und Ereignisquellen hinweg zu überwachen und zu überprüfen. Dieser Artikel befasst sich mit den verschiedenen Abschnitten der Seite und den Informationen, die Sie dort finden können.

Um zur Seite **Abrechnung** zu navigieren, gehen Sie zu **Einstellungen** > **Abrechnung**.

Die Seite **Abrechnung** enthält die folgenden Registerkarten:

- [Abos und Nutzung](#subscriptions-and-usage)
- [Meistgenutzte Events und Attribute nach App](#most-used-events-and-attributes-by-app)
- [Datenpunkt-Nutzung gesamt](#total-data-points-dashboard)

## Abos und Nutzung

Die Registerkarte **Abonnements und Nutzung** enthält Nutzungsdiagramme und Ihre Vertragsdetails. Die Daten auf dieser Seite werden täglich um 22:00 Uhr Eastern Time (ET) aktualisiert. Es spiegelt keine Realtime-Aktivitäten wider.

### Diagramme zur Nutzung

Hier finden Sie Nutzungsdiagramme, die für Ihre Workspaces relevant sind. Sie werden feststellen, dass Ihr eigenes Dashboard je nach den von Ihnen erworbenen Produkten unterschiedliche Nutzungskennzahlen anzeigt. 

![Nutzungsdiagramm mit monatlichen eindeutigen Besuchern]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

Diese Diagramme können monatlich aktive Nutzer:innen, eindeutige Besucher:innen und den Versand von E-Mails anzeigen. Nutzungsdiagramme wie diese sind besonders hilfreich, wenn Sie versuchen, die Nutzung zu budgetieren und ein tieferes Verständnis dafür zu gewinnen, welche Workspaces zur Gesamtnutzung beitragen.

### Vertragsdetails

Unter Vertragsdetails finden Sie das Anfangs- und Enddatum Ihres aktuellen Vertrags mit Braze.

#### Überlegungen

Wenn Ihr Vertrag monatliche Unique Visitors (MUV) verwendet und Sie zu einem Vertrag wechseln, der nur monatlich aktive:r Nutzer:in (MAU) verwendet, werden Ihre historischen Daten weiterhin im MUV-Diagramm angezeigt, während Ihre neuen Daten nur im MAU-Diagramm erscheinen. Wenn Ihr Vertrag beispielsweise im Oktober endet, zeigt das MUV-Diagramm die Daten bis Ende September an.

## Meistgenutzte Events und Attribute nach App

Unter **„meistgenutzte Events und Attribute nach App**“ können Sie die Treiber Ihrer Attribut- und angepassten Event-Datenpunkt-Nutzung überprüfen. 

![Meistgenutzte Events und Attribute nach App]({% image_buster /assets/img/most_used_events_attributes_time.png %})

Für jede App können Sie die Option **Aufschlüsselung anzeigen** wählen, um eine geschätzte Anzahl jedes spezifischen benutzerdefinierten Attributs, Profilattributs und benutzerdefinierten Ereignisses für den ausgewählten Zeitraum sowie den prozentualen Anteil der Attribut- und Ereignisaktualisierungen dieser App anzuzeigen, der auf dieses Attribut oder Ereignis zurückzuführen ist. 

![Die meistgenutzten Events und Attribute nach App-Aufschlüsselung]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

Aufschlüsselungen wie diese können Ihnen helfen zu verstehen, welche Datenpunkte einen großen Teil Ihres Kontingents beanspruchen. Wir empfehlen Ihnen, diese Informationen von Zeit zu Zeit zu überprüfen, um sicherzustellen, dass Sie keine Datenpunkte auf unbeabsichtigte und unnötige Weise ausgeben. Ihr Kundenerfolgsmanager kann Sie dabei unterstützen, das Beste aus Ihrem aktuellen Plan herauszuholen, oder Ihnen Optionen für mehr Flexibilität anbieten. 

## Dashboard für Gesamtdatenpunkte

Die Tab-Seite **„Gesamt-Datenpunkt-Nutzung“** bietet einen detaillierten Überblick über Ihre Datenpunkt-Nutzung. Sie können alle Daten in diesem Bereich entweder nach Wochen oder Monaten aggregiert anzeigen.

{% alert note %}
Die Datenpunkte werden alle 24 Stunden zwischengespeichert.
{% endalert %}

![Filtern der Datenpunktverwendung nach Wochen]({% image_buster /assets/img/subscription_and_billing2.png %})

### Vertragsdetails

Hier finden Sie Informationen zum Beginn und Ende Ihres aktuellen Braze-Vertrags sowie zu den zugewiesenen Datenpunkten und der Summe aller Datenpunkte, die bisher im Rahmen Ihres aktuellen Vertrags verwendet wurden.

Die Felder in diesem Abschnitt sind wie folgt definiert:

- **Art des Vertrags:** Struktur der Abrechnungsperiode, entweder jährlich oder mehrjährig.
- **Start- und Enddatum des Vertrags:** Anfangs- und Enddatum des gesamten Vertrags.
- **Datenpunkte-Kontingent:** Die Anzahl der Datenpunkte, die der Vertrag pro Abrechnungszeitraum vorsieht.
- **Datenpunktnutzung gemäß Vertrag:** Die kumulierte Summe aller Datenpunkte, die während der Vertragslaufzeit protokolliert wurden, und die in der nächsten Abrechnungsperiode nicht zurückgesetzt wird.

![Abschnitt "Vertragsdetails" auf dem Tab "Datenpunkt-Nutzung insgesamt"]({% image_buster /assets/img/contract_details.png %})

### Rechnungsdaten des Unternehmens

#### Datenpunkt-Nutzung gesamt auf App-Ebene

Dieses Diagramm zeigt die Nutzung Ihrer Datenpunkte in verschiedenen Anwendungen.

!["Datenpunkt-Nutzung gesamt auf App-Ebene" zeigt die für jede App verwendeten Datenpunkte an.]({% image_buster /assets/img/app_level_total.png %})

Wählen Sie eine der Summen aus, um die Tabelle **Datenpunktnutzung im Laufe der Zeit** anzuzeigen, in der die wöchentlichen Summen der Datenpunkte für jeden Arbeitsbereich aufgeführt sind.  Zeilen mit einer leeren Spalte **App-Name** stellen Datenpunkte dar, die keiner App zugeordnet sind (z. B. Datenpunkte, die in Anfragen verwendet werden, die keine `app_id` angeben).

![Datenpunkt-Nutzung im Laufe der Zeit mit den gesamten wöchentlichen Datenpunkten für zwei Workspaces.]({% image_buster /assets/img/data_point_usage_time.png %})

#### Workspace Datenpunkt-Nutzung

Mit dieser Grafik können Sie die Gesamtnutzung der Datenpunkte eines Unternehmens nach Arbeitsbereich beurteilen. Anhand dieser Grafik können Sie beurteilen, wie jeder Workspace zur Datenpunkt-Nutzung des Unternehmens beiträgt.

![Workspace Datenpunkt-Nutzungsdiagramm für zwei Workspaces]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### Datenpunkt-Nutzung im Abrechnungszyklus nach Event-Quelle

Anhand dieses Diagramms können Sie sehen, wie sich die Nutzung von Datenpunkten auf verschiedene Ereignisquellen verteilt, z. B. auf verschiedene API-Attribute, benutzerdefinierte Ereignisse und Sitzungen.

![Datenpunkt-Nutzung im Abrechnungszyklus nach Event-Quelle, wobei die Zuordnung der Datenpunkte zu den verschiedenen Event-Quellen angezeigt wird.]({% image_buster /assets/img/event_source_stats.png %})

#### Datenpunkt-Nutzung im Laufe der Zeit

Anhand dieses Diagramms können Sie schnell Ihre gesamte Datenpunkt-Nutzung im Vergleich zu der Ihnen zugeteilten Menge an Datenpunkten sehen.

![Datenpunktnutzung im Zeitverlauf, wobei die für den aktuellen Abrechnungszyklus zugewiesenen Datenpunkte der laufenden Gesamtzahl gegenübergestellt werden]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

