---
nav_title: Migration granularer Berechtigungen
article_title: Migration zu granularen Berechtigungen
page_order: 3
page_type: reference
alias: /granular_permissions_migration/
description: "Dieser Referenzartikel behandelt die Vorbereitung auf die Migration zu granularen Nutzerberechtigungen in Braze."
tool: Dashboard
---

# Migration zu granularen Berechtigungen

> Die Verwaltung der Zugriffsrechte auf Ihr Konto und die Ausführung bestimmter Aktionen ist sowohl für die Sicherheit als auch für die betriebliche Effizienz von entscheidender Bedeutung. Um Ihnen mehr Kontrolle zu geben, führt Braze granulare Berechtigungen ein – eine flexiblere und präzisere Methode zur Verwaltung des Nutzerzugriffs auf Ihr Konto.

Die Migration bietet folgende Vorteile:

- **Präzisere Steuerung:** Granulare Berechtigungen bieten mehr Kontrolle, höhere Sicherheit und eine übersichtlichere Übersicht. Nutzer:innen erhalten ausschließlich die Zugriffsrechte, die sie benötigen.
- **Automatische Abbildung:** Alle aktuellen Berechtigungen werden automatisch auf ihre [granularen Entsprechungen](#legacy-to-granular-permissions-mapping) abgebildet. Ihre Nutzer:innen behalten die gleiche Zugriffsebene, sofern Sie diese nicht ändern.

## Was Sie überprüfen sollten

Wenn für Ihr Unternehmen eine Migration geplant ist, erhalten Ihre Braze-Administratoren E-Mails und Banner im Dashboard, die sie über die Migration der granularen Berechtigungen informieren. Zur Vorbereitung auf die Migration empfehlen wir, dass ein Braze-Administrator die folgenden Schritte durchführt.

1. Identifizieren Sie Nutzer:innen, Rollen oder Berechtigungssätze, die möglicherweise aktualisiert werden müssen, um nach der Migration zum neuen Berechtigungsrahmen einen individuelleren Zugriff zu ermöglichen. 
2. Sollte Ihr Unternehmen die Nutzerbereitstellung mithilfe von SCIM oder Compliance-Tools automatisiert haben, die auf [Berechtigungs-Strings]({{site.baseurl}}/scim_api_appendix/) basieren, aktualisieren Sie diese entsprechend der neuen granularen Struktur. 
3. Informieren Sie Ihre Braze-Nutzer:innen über bevorstehende Änderungen, um Unklarheiten zu vermeiden.
4. Zum geplanten Migrationszeitpunkt wird Ihr Unternehmen automatisch auf granulare Berechtigungen umgestellt. Von den Unternehmensadministratoren sind keine weiteren Maßnahmen erforderlich.

{% alert important %}
Die Möglichkeit, Berechtigungen zu aktualisieren, wird 15 Minuten vor dem geplanten Migrationszeitpunkt gesperrt. Das bedeutet, dass Sie bis zum Abschluss der Migration keine Berechtigungen ändern können. Wir gehen davon aus, dass die Migration bis zu 15 Minuten dauern wird.
{% endalert %}

## Abbildung von Legacy- zu granularen Berechtigungen

Diese Tabelle zeigt, wie die einzelnen Legacy-Berechtigungen auf die granularen Berechtigungen abgebildet werden. Nutzen Sie diese Tabelle als Referenz, wenn Sie Ihre Berechtigungen aktualisieren. Um einem/einer Nutzer:in beispielsweise denselben Zugriff wie mit der Legacy-Berechtigung „E-Mail-Einstellungen verwalten" zu gewähren, muss diese/r Nutzer:in sowohl über die granulare Berechtigung „E-Mail-Einstellungen anzeigen" als auch über „E-Mail-Einstellungen bearbeiten" verfügen.

| | Legacy-Berechtigungen | Granulare Berechtigungen |
|---------------|---------------|---------------|
| **Ebene** | **Name** | **Name** |
| Admin | Admin | Admin |
| Workspace | Workspace-Administrator | Workspace-Administrator |
| Unternehmen | Workspaces erstellen und löschen | Workspaces erstellen und löschen |
| Unternehmen | Unternehmenseinstellungen verwalten | Unternehmenseinstellungen verwalten |
| Workspace | Zugriff auf Kampagnen, Canvase, Karten, Content-Blöcke, Feature-Flags, Segmente, Medienbibliothek, Standorte, Aktionscodes und Präferenzzentren | Kampagnen anzeigen<br>Kampagnen bearbeiten<br>Kampagnen archivieren<br>Canvase anzeigen<br>Canvase bearbeiten<br>Canvase archivieren<br>Frequency-Capping-Regeln anzeigen<br>Frequency-Capping-Regeln bearbeiten<br>Priorisierung von Nachrichten anzeigen<br>Priorisierung von Nachrichten bearbeiten<br>Content-Blöcke anzeigen<br>Feature-Flags anzeigen<br>Feature-Flags bearbeiten<br>Feature-Flags archivieren<br>Segmente anzeigen<br>Segmente bearbeiten<br>Globale Kontrollgruppe bearbeiten<br>IAM-Templates anzeigen<br>IAM-Templates bearbeiten<br>IAM-Templates archivieren<br>E-Mail-Templates anzeigen<br>E-Mail-Templates bearbeiten<br>E-Mail-Templates archivieren<br>Webhook-Templates anzeigen<br>Webhook-Templates bearbeiten<br>Webhook-Templates archivieren<br>E-Mail-Link-Templates anzeigen<br>E-Mail-Link-Templates bearbeiten<br>Mediathek-Assets anzeigen<br>Standorte anzeigen<br>Standorte bearbeiten<br>Standorte archivieren<br>Aktionscodes anzeigen<br>Aktionscodes bearbeiten<br>Aktionscodes exportieren<br>Präferenzzentren anzeigen<br>Präferenzzentren bearbeiten<br>Berichte bearbeiten<br>Banner-Templates anzeigen<br>Lokalisierungseinstellungen anzeigen<br>Operator verwenden<br>Entscheidungsstudio-Agenten anzeigen<br>Entscheidungsstudio-Konversions-Event anzeigen |
| Workspace | Dev-Konsole öffnen | API-Schlüssel anzeigen<br>API-Schlüssel bearbeiten<br>Interne Gruppen anzeigen<br>Interne Gruppen bearbeiten<br>Interne Gruppen löschen<br>Nachrichten-Aktivitätsprotokoll anzeigen<br>Event-Benutzerprotokoll anzeigen<br>API-Bezeichner anzeigen<br>Dashboard zur API-Nutzung anzeigen<br>API-Limits anzeigen<br>API-Nutzungsmeldungen anzeigen<br>API-Nutzungsmeldungen bearbeiten<br>SDK-Debugger anzeigen<br>SDK-Debugger bearbeiten |
| Workspace | Kampagnen genehmigen und ablehnen | Kampagnen genehmigen |
| Workspace | Canvase genehmigen und ablehnen | Canvase genehmigen |
| Workspace | Nutzerdaten exportieren | Nutzerdaten exportieren |
| Workspace | Nutzerdaten importieren und aktualisieren | Importierte Nutzer:innen anzeigen<br>Nutzer:innen importieren<br>Nutzerdaten bearbeiten |
| Workspace | Segmente bearbeiten | Segmente archivieren |
| Workspace | Content-Blöcke starten und verwalten | Content-Blöcke bearbeiten<br>Content-Blöcke archivieren<br>Content-Blöcke starten |
| Workspace | Medienbibliothek verwalten | Assets der Medienbibliothek bearbeiten<br>Assets der Medienbibliothek löschen |
| Workspace | Präferenzzentren starten | Präferenzzentren starten |
| Workspace | Apps verwalten | App-Einstellungen anzeigen<br>App-Einstellungen bearbeiten<br>Push-Einstellungen anzeigen<br>Push-Einstellungen bearbeiten<br>Banner-Templates bearbeiten<br>Banner-Templates archivieren |
| Workspace | Kataloge verwalten – Dashboard-Berechtigung | Kataloge anzeigen<br>Kataloge bearbeiten<br>Kataloge exportieren<br>Kataloge löschen |
| Workspace | Dashboard-Nutzer:innen verwalten | Dashboard-Nutzer:innen bearbeiten |
| Workspace | E-Mail-Einstellungen verwalten | E-Mail-Einstellungen anzeigen<br>E-Mail-Einstellungen bearbeiten |
| Workspace | Events, Attribute und Käufe verwalten | Angepasste Attribute anzeigen<br>Angepasste Attribute bearbeiten<br>Sperrliste für angepasste Attribute<br>Angepasste Attribute löschen<br>Angepasste Attribute exportieren<br>Angepasste Events anzeigen<br>Angepasste Events bearbeiten<br>Sperrliste für angepasste Events<br>Angepasste Events löschen<br>Angepasste Events exportieren<br>Segmentierung von angepassten Event-Eigenschaften bearbeiten<br>Produkte anzeigen<br>Produkte bearbeiten<br>Sperrliste für Produkte<br>Segmentierung von Kaufeigenschaften bearbeiten |
| Workspace | Externe Integrationen verwalten | Technologiepartner bearbeiten<br>Cloud-Datenaufnahme bearbeiten |
| Workspace | Einstellungen für mehrere Sprachen verwalten | Lokalisierungseinstellungen bearbeiten<br>Lokalisierungseinstellungen löschen |
| Workspace | Abo-Gruppen verwalten | Abos bearbeiten |
| Workspace | Tags verwalten | Tags anzeigen<br>Tags bearbeiten<br>Tags löschen |
| Workspace | Teams verwalten | Teams anzeigen<br>Teams bearbeiten<br>Teams archivieren |
| Workspace | Datentransformationen anzeigen | Datentransformation anzeigen |
| Workspace | Datentransformationen bearbeiten | Datentransformation bearbeiten |
| Workspace | Verschlüsselung der Nutzerdaten verwalten | Verschlüsselung auf Bezeichner-Feldebene bearbeiten |
| Workspace | Kampagnen und Canvase senden | Kampagnen starten<br>Canvase starten |
| Workspace | Rechnungsdetails anzeigen | Rechnungsdetails anzeigen |
| Workspace | Currents-Integrationen anzeigen | Currents-Integrationen anzeigen |
| Workspace | Currents-Integrationen bearbeiten | Currents-Integrationen bearbeiten |
| Workspace | Als PII gekennzeichnete angepasste Attribute anzeigen | Als PII gekennzeichnete angepasste Attribute anzeigen |
| Workspace | PII anzeigen | PII anzeigen |
| Workspace | Nutzerprofile PII-konform anzeigen | Nutzerprofile anzeigen (PII geschwärzt) |
| Workspace | Nutzungsdaten anzeigen | Nutzungsdaten anzeigen |
| Workspace | Doppelte Nutzer:innen zusammenführen | Doppelte Nutzer:innen zusammenführen |
| Workspace | Canvas-Templates erstellen und bearbeiten | Canvas-Templates bearbeiten |
| Workspace | Canvas-Templates anzeigen | Canvas-Templates anzeigen |
| Workspace | Canvas-Templates archivieren | Canvas-Templates archivieren |
| Workspace | Landing-Pages veröffentlichen | Landing-Pages veröffentlichen |
| Workspace | Entwürfe für Landing-Pages erstellen | Entwürfe für Landing-Pages bearbeiten |
| Workspace | Landing-Pages aufrufen | Landing-Pages anzeigen |
| Workspace | Landing-Page-Templates erstellen und bearbeiten | Landing-Page-Templates bearbeiten |
| Workspace | Landing-Page-Templates anzeigen | Landing-Page-Templates anzeigen |
| Workspace | Landing-Page-Templates archivieren | Landing-Page-Templates archivieren |
| Workspace | Angepasste KI-Agenten anzeigen | Angepasste KI-Agenten anzeigen |
| Workspace | Angepasste KI-Agenten bearbeiten | Angepasste KI-Agenten bearbeiten<br> Angepasste KI-Agenten archivieren |
| Workspace | Platzierungen anzeigen | Platzierungen anzeigen |
| Workspace | Platzierungen bearbeiten | Platzierungen bearbeiten |
| Workspace | Platzierungen archivieren | Platzierungen archivieren |
| Workspace | Neu | Zusammenführung von Nutzer:innen anzeigen |
| Workspace | Neu | Nutzerlöschungs-Datensätze anzeigen |
| Workspace | Neu | Banner-Templates anzeigen |
| Workspace | Neu | Banner-Templates bearbeiten |
| Workspace | Neu | Banner-Templates archivieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Häufig gestellte Fragen

### Ist es möglich, die Migration abzulehnen oder rückgängig zu machen?

Braze unterstützt keine Rückgängigmachung der Migration. Wir unterstützen Sie während der Migration und überwachen den Prozess genau, um etwaige Probleme umgehend zu beheben.

### Verlieren bestehende Nutzer:innen während der Migration den Zugriff auf Braze?

Nein, während der Migration wird es keine Ausfallzeit bei Braze geben. Allerdings werden Änderungen an Berechtigungen während der Migration gesperrt. Wir gehen davon aus, dass die Migration bis zu 15 Minuten dauern wird.