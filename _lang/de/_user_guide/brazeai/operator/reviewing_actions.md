---
nav_title: Überprüfen Sie die Maßnahmen
article_title: Überprüfung der Aktionen von BrazeAI Operator<sup>TM</sup>
page_order: 2
description: "Erfahren Sie, wie Sie Aktionen überprüfen und genehmigen können, wenn BrazeAI Operator Änderungen im Dashboard vorschlägt."
---

# Überprüfung der Aktionen des BrazeAI-Operators

> Erfahren Sie, wie Sie Aktionen überprüfen und genehmigen können, wenn BrazeAI Operator<sup>TM</sup> Änderungen im Dashboard vorschlägt.

![Der Operator präsentiert vorgeschlagene Aktionskarten zur Überprüfung.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Wie Aktionskarten funktionieren

Wenn der Operator Änderungen im Dashboard vorschlägt (z. B. das Ausfüllen von Formularfeldern, das Erstellen von Updates oder das Generieren von Bildern), wird jede Änderung als Aktionskarte zur Überprüfung angezeigt.

1. **Der Operator fasst den Plan zusammen:** Der Operator erläutert seine Absichten, bevor er die Aktionskarten vorzeigt.
2. **Einzelne Aktionskarten werden angezeigt:** Jede vorgeschlagene Änderung wird als separate Karte dargestellt, die anzeigt, was der Operator im Dashboard ändern oder ausführen möchte. Bei Änderungen bestehender Werte werden der vorherige Wert und der vorgeschlagene Wert zum Vergleich nebeneinander angezeigt.
3. **Bitte überprüfen und genehmigen Sie:** Bitte überprüfen Sie jede Karte und genehmigen oder lehnen Sie sie ab.
4. **Die Aktion wird ausgeführt:** Genehmigte Maßnahmen werden in Braze ausgeführt. Abgelehnte Aktionen werden nicht angewendet.

Sollte eine Aktion nach der Genehmigung fehlschlagen, wird der Operator Sie mit detaillierten Informationen über den Fehler benachrichtigen.

### Verfügbarkeit

Aktionskarten werden in den folgenden Editoren unterstützt:

- In-App-Nachrichten (nur traditioneller Editor)
- Content-Cards
- E-Mail (nur HTML-Editor)
- Push-Benachrichtigungen
- SMS/MMS/RCS
- Webhooks

Auf anderen Seiten stellt Operator eine Liste von Schritten zur Verfügung, die in der UI ausgeführt werden müssen, anstatt selbst Maßnahmen zu ergreifen. Die Funktionalität des Operators wird regelmäßig verbessert, und es wird eine erweiterte Abdeckung für Erstellungswerkzeuge erwartet.

## Einen Plan ändern

Um den Plan des Operators zu ändern, genehmigen oder lehnen Sie bitte zunächst die ausstehenden Aktionen ab. Bitte beschreiben Sie die gewünschte Änderung in einer neuen Chat-Nachricht.

Genehmigte Aktionen können nicht über Operator rückgängig gemacht werden. Bitte beschreiben Sie die neuen Änderungen dem Operator oder nehmen Sie die Änderungen manuell im Dashboard vor.

## Aktionen automatisch genehmigen

Die Option **„Aktionen automatisch genehmigen“** befindet sich im Chat-Panel des Operators.

- **Ein:** Die vom Operator vorgeschlagenen Maßnahmen werden sofort ausgeführt, ohne dass eine manuelle Genehmigung erforderlich ist. Einige Aktionen erfordern weiterhin eine ausdrückliche Genehmigung aus Sicherheitsgründen, beispielsweise das Erstellen von Bildern oder das Vornehmen von Änderungen an den Einstellungen auf Workspace-Ebene.
- **Aus (Standard):** Alle vorgeschlagenen Maßnahmen werden dem beschriebenen manuellen Überprüfungsprozess unterzogen.

![Die Schaltfläche zum Umschalten auf die automatische Genehmigung und das BestätigungsModal im Operator-Chat-Panel.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

Die automatische Genehmigung wird zurückgesetzt, wenn Sie die Seite aktualisieren, einen neuen Tab öffnen oder sich ab- und wieder anmelden. Das Wechseln zwischen den Seiten im Dashboard führt nicht zu dessen Zurücksetzen. Die automatische Genehmigung kann jederzeit deaktiviert werden.
