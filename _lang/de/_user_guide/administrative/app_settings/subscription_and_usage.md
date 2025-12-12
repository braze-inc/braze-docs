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

Die Registerkarte **Abonnements und Nutzung** enthält Nutzungsdiagramme und Ihre Vertragsdetails.

### Diagramme zur Nutzung

Hier finden Sie Nutzungsdiagramme, die sich auf Ihre Workspaces beziehen. Sie werden feststellen, dass Ihr eigenes Dashboard je nach den von Ihnen erworbenen Produkten unterschiedliche Nutzungskennzahlen anzeigt. 

![Nutzungsdiagramm mit monatlichen eindeutigen Besuchern]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

Diese Diagramme können monatlich aktive Nutzer:innen, eindeutige Besucher:innen und den Versand von E-Mails anzeigen. Nutzungsdiagramme wie diese sind besonders hilfreich, wenn Sie versuchen, die Nutzung zu budgetieren und ein tieferes Verständnis dafür zu gewinnen, welche Workspaces zur Gesamtnutzung beitragen.

### Vertragsdetails

Unter Vertragsdetails finden Sie das Anfangs- und Enddatum Ihres aktuellen Vertrags mit Braze.

## Meistgenutzte Events und Attribute nach App

Unter **Meistgenutzte Events und -Attribute nach App** können Sie die Treiber für die Nutzung Ihrer Attribute und angepassten Events-Datenpunkte überprüfen. 

![Meistgenutzte Events und Attribute nach App]({% image_buster /assets/img/most_used_events_attributes_time.png %})

Für jede App können Sie die Option **Aufschlüsselung anzeigen** wählen, um eine geschätzte Anzahl jedes spezifischen benutzerdefinierten Attributs, Profilattributs und benutzerdefinierten Ereignisses für den ausgewählten Zeitraum sowie den prozentualen Anteil der Attribut- und Ereignisaktualisierungen dieser App anzuzeigen, der auf dieses Attribut oder Ereignis zurückzuführen ist. 

![Meistgenutzte Events und Attribute nach App Aufschlüsselung Tab]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

Aufschlüsselungen wie diese können Ihnen helfen zu verstehen, welche Datenpunkte einen großen Teil Ihres Kontingents beanspruchen. Wir empfehlen Ihnen, diese Informationen von Zeit zu Zeit zu überprüfen, um sicherzustellen, dass Sie keine Datenpunkte auf unbeabsichtigte und unnötige Weise ausgeben. Ihr Kundenerfolgsmanager kann Sie dabei unterstützen, das Beste aus Ihrem aktuellen Plan herauszuholen, oder Ihnen Optionen für mehr Flexibilität anbieten. 

## Dashboard für Gesamtdatenpunkte

Der Tab **Datenpunkt-Nutzung insgesamt** bietet einen detaillierten Einblick in Ihre Datenpunkt-Nutzung. Sie können alle Daten in diesem Bereich entweder nach Wochen oder Monaten aggregiert anzeigen.

![Filtern der Datenpunkt-Nutzung nach Wochen]({% image_buster /assets/img/subscription_and_billing2.png %})

### Vertragsdetails

Hier finden Sie Informationen darüber, wann Ihr aktueller Braze-Vertrag beginnt und endet, sowie die zugeteilten Datenpunkte und eine Summe aller Datenpunkte, die bisher in Ihrem aktuellen Vertrag verwendet wurden.

Die Felder in diesem Abschnitt sind wie folgt definiert:

- **Art des Vertrags:** Struktur der Abrechnungsperiode, entweder jährlich oder mehrjährig.
- **Start- und Enddatum des Vertrags:** Anfangs- und Enddatum des gesamten Vertrags.
- **Datenpunkte-Kontingent:** Die Anzahl der Datenpunkte, die der Vertrag pro Abrechnungszeitraum vorsieht.
- **Datenpunktnutzung gemäß Vertrag:** Eine kumulative Summe aller Datenpunkte, die während der Lifetime des Vertrags protokolliert wurden und in der nächsten Abrechnungsperiode nicht zurückgesetzt werden.

![Abschnitt Vertragsdetails des Tabs Datenpunkt-Nutzung insgesamt]({% image_buster /assets/img/contract_details.png %})

### Rechnungsdaten des Unternehmens

#### Datenpunkt-Nutzung gesamt auf App-Ebene

Dieses Diagramm zeigt die Nutzung Ihrer Datenpunkte in verschiedenen Anwendungen.

![App Level Total Data Point Usage zeigt die für jede App verwendeten Datenpunkte an.]({% image_buster /assets/img/app_level_total.png %})

Wählen Sie eine der Summen aus, um die Tabelle **Datenpunktnutzung im Laufe der Zeit** anzuzeigen, in der die wöchentlichen Summen der Datenpunkte für jeden Arbeitsbereich aufgeführt sind.  Zeilen mit einer leeren Spalte **App-Name** stellen Datenpunkte dar, die keiner App zugeordnet sind (z. B. Datenpunkte, die in Anfragen verwendet werden, die keine `app_id` angeben).

![Datenpunkt-Nutzung im Zeitverlauf mit den gesamten wöchentlichen Datenpunkten für zwei Workspaces.]({% image_buster /assets/img/data_point_usage_time.png %})

#### Workspace Datenpunkt-Nutzung

Mit dieser Grafik können Sie die Gesamtnutzung der Datenpunkte eines Unternehmens nach Arbeitsbereich beurteilen. Anhand dieser Grafik können Sie beurteilen, wie jeder Workspace zur Datenpunkt-Nutzung des Unternehmens beiträgt.

![Workspace Datenpunkt-Nutzungsdiagramm für zwei Workspaces]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### Datenpunkt-Nutzung im Abrechnungszyklus nach Event-Quelle

Anhand dieses Diagramms können Sie sehen, wie sich die Nutzung von Datenpunkten auf verschiedene Ereignisquellen verteilt, z. B. auf verschiedene API-Attribute, benutzerdefinierte Ereignisse und Sitzungen.

Die Datenpunkt-Nutzung nach Ereignisquelle im Abrechnungszyklus zeigt die Zuordnung der Datenpunkte zu den verschiedenen Ereignisquellen an.]({% image_buster /assets/img/event_source_stats.png %})

#### Datenpunkt-Nutzung im Laufe der Zeit

Anhand dieses Diagramms können Sie schnell Ihre gesamte Datenpunkt-Nutzung im Vergleich zu der Ihnen zugeteilten Menge an Datenpunkten sehen.

![Datenpunkt-Nutzung im Zeitverlauf, wobei die für den aktuellen Abrechnungszyklus zugeteilten Datenpunkte mit der laufenden Gesamtsumme verglichen werden]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

