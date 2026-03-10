---
nav_title: Aktionen prüfen
article_title: Aktionen von BrazeAI Operator<sup>TM</sup> prüfen
page_order: 2
description: "Erfahren Sie, wie Sie Aktionen prüfen und genehmigen, wenn BrazeAI Operator Änderungen im Dashboard vorschlägt."
---

# Aktionen von BrazeAI Operator prüfen

> Erfahren Sie, wie Sie Aktionen prüfen und genehmigen, wenn BrazeAI Operator<sup>TM</sup> Änderungen im Dashboard vorschlägt.

![Operator zeigt vorgeschlagene Aktionskarten zur Prüfung an.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## So funktionieren Aktionskarten

Wenn Operator Änderungen im Dashboard vorschlägt (z. B. Formularfelder ausfüllen, Einstellungen anpassen oder Bilder erzeugen), wird jede Änderung als Aktionskarte zur Prüfung angezeigt.

1. **Operator fasst den Plan zusammen:** Operator erläutert vor den Aktionskarten, was er tun wird.
2. **Einzelne Aktionskarten erscheinen:** Jede vorgeschlagene Änderung wird auf einer eigenen Karte gezeigt. Bei Änderungen an bestehenden Werten werden alter und neuer Wert nebeneinander angezeigt.
3. **Prüfen und genehmigen:** Prüfen Sie jede Karte und genehmigen oder lehnen Sie sie ab.
4. **Aktion wird ausgeführt:** Genehmigte Aktionen werden in Braze ausgeführt. Abgelehnte Aktionen werden nicht übernommen.

Schlägt eine Aktion nach der Genehmigung fehl, informiert Operator mit Details zum Fehler.

### Verfügbarkeit

Aktionskarten werden in folgenden Editoren unterstützt:

- In-App-Nachrichten (nur klassischer Editor)
- Content Cards
- E-Mail (nur HTML-Editor)
- Push-Benachrichtigungen
- SMS/MMS/RCS
- Webhooks

Auf anderen Seiten liefert Operator eine Liste von Schritten zur Ausführung in der UI statt selbst Aktionen auszuführen. Die Operator-Funktionalität wird laufend erweitert; eine breitere Abdeckung der Erstellungs-Tools ist geplant.

## Einen Plan anpassen

Um den Plan von Operator zu ändern, genehmigen oder lehnen Sie zuerst die ausstehenden Aktionen ab. Beschreiben Sie die gewünschte Änderung dann in einer neuen Chat-Nachricht.

Genehmigte Aktionen können nicht über Operator rückgängig gemacht werden. Beschreiben Sie Operator die neue Änderung oder nehmen Sie die Änderungen manuell im Dashboard vor.

## Aktionen automatisch genehmigen

Der Schalter **Aktionen automatisch genehmigen** befindet sich im Operator-Chat-Panel.

- **Ein:** Die von Operator vorgeschlagenen Aktionen werden sofort ausgeführt, ohne manuelle Freigabe. Aus Sicherheitsgründen erfordern einige Aktionen weiterhin eine ausdrückliche Freigabe, z. B. das Erzeugen von Bildern oder Änderungen auf Workspace-Ebene.
- **Aus (Standard):** Alle vorgeschlagenen Aktionen durchlaufen den beschriebenen manuellen Prüfprozess.

![Der Schalter für automatische Genehmigung und der Bestätigungsdialog im Operator-Chat-Panel.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

Die automatische Genehmigung wird zurückgesetzt, wenn Sie die Seite aktualisieren, einen neuen Tab öffnen oder sich ab- und wieder anmelden. Das Wechseln zwischen Seiten im Dashboard setzt sie nicht zurück. Sie können die automatische Genehmigung jederzeit ausschalten.
