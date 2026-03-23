---
nav_title: Aktionen überprüfen
article_title: Aktionen von BrazeAI Operator<sup>TM</sup> überprüfen
page_order: 2
description: "Erfahren Sie, wie Sie Aktionen überprüfen und genehmigen können, wenn BrazeAI Operator Änderungen im Dashboard vorschlägt."
---

# Aktionen von BrazeAI Operator überprüfen

> Erfahren Sie, wie Sie Aktionen überprüfen und genehmigen können, wenn BrazeAI Operator<sup>TM</sup> Änderungen im Dashboard vorschlägt.

![Operator präsentiert vorgeschlagene Aktionskarten zur Überprüfung.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Wie Aktionskarten funktionieren

Wenn Operator Änderungen im Dashboard vorschlägt (z. B. das Ausfüllen von Formularfeldern, das Aktualisieren von Einstellungen oder das Generieren von Bildern), wird jede Änderung als Aktionskarte zur Überprüfung angezeigt.

1. **Operator fasst den Plan zusammen:** Operator erläutert seine Absichten, bevor die Aktionskarten angezeigt werden.
2. **Einzelne Aktionskarten werden angezeigt:** Jede vorgeschlagene Änderung wird als separate Karte dargestellt, die anzeigt, was Operator im Dashboard ändern oder ausführen möchte. Bei Änderungen bestehender Werte werden der vorherige Wert und der vorgeschlagene Wert zum Vergleich nebeneinander angezeigt.
3. **Überprüfen und genehmigen:** Überprüfen Sie jede Karte und genehmigen oder lehnen Sie sie ab.
4. **Die Aktion wird ausgeführt:** Genehmigte Aktionen werden in Braze ausgeführt. Abgelehnte Aktionen werden nicht angewendet.

Sollte eine Aktion nach der Genehmigung fehlschlagen, benachrichtigt Operator Sie mit Details zum aufgetretenen Fehler.

### Verfügbarkeit

Aktionskarten werden in den folgenden Editoren und auf den folgenden Seiten unterstützt.

- **Nachrichten-Editoren:**
    - In-App-Nachrichten (nur traditioneller Editor)
    - Content Cards
    - E-Mail (nur HTML-Editor)
    - Push-Benachrichtigungen
    - SMS/MMS/RCS
    - Webhooks
- Seite [Angepassten Agenten erstellen]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
 
Auf anderen Seiten stellt Operator eine Liste von Schritten zur Verfügung, die in der UI ausgeführt werden müssen, anstatt selbst Aktionen auszuführen. Die Funktionalität von Operator wird regelmäßig verbessert, und eine erweiterte Abdeckung für Erstellungswerkzeuge ist geplant.

## Einen Plan ändern

Um den Plan von Operator zu ändern, genehmigen oder lehnen Sie zunächst die ausstehenden Aktionen ab. Beschreiben Sie dann die gewünschte Änderung in einer neuen Chat-Nachricht.

Genehmigte Aktionen können nicht über Operator rückgängig gemacht werden. Beschreiben Sie die neue Änderung gegenüber Operator oder nehmen Sie die Änderungen manuell im Dashboard vor.

## Aktionen automatisch genehmigen

Der Schalter **Aktionen automatisch genehmigen** befindet sich im Chat-Panel von Operator.

- **Ein:** Die von Operator vorgeschlagenen Aktionen werden sofort ausgeführt, ohne dass eine manuelle Genehmigung erforderlich ist. Einige Aktionen erfordern aus Sicherheitsgründen weiterhin eine ausdrückliche Genehmigung, beispielsweise das Generieren von Bildern oder das Vornehmen von Änderungen an Einstellungen auf Workspace-Ebene.
- **Aus (Standard):** Alle vorgeschlagenen Aktionen durchlaufen den beschriebenen manuellen Überprüfungsprozess.

![Der Schalter für die automatische Genehmigung und das Bestätigungs-Modal im Chat-Panel von Operator.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

Die automatische Genehmigung wird zurückgesetzt, wenn Sie die Seite aktualisieren, einen neuen Tab öffnen oder sich ab- und wieder anmelden. Das Wechseln zwischen Seiten im Dashboard setzt sie nicht zurück. Die automatische Genehmigung kann jederzeit deaktiviert werden.