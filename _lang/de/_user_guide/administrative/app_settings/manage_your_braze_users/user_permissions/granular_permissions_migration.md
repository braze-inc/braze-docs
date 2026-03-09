---
nav_title: Migration granularer Berechtigungen
article_title: Migration zu detaillierten Berechtigungen
page_order: 3
page_type: reference
alias: /granular_permissions_migration/
description: "Dieser Referenzartikel behandelt die Vorbereitung auf die Migration zu detaillierten Benutzerberechtigungen in Braze."
tool: Dashboard
---

# Migration zu detaillierten Berechtigungen

> Die Verwaltung der Zugriffsrechte auf Ihr Konto und die Ausführung bestimmter Aktionen ist sowohl für die Sicherheit als auch für die betriebliche Effizienz von entscheidender Bedeutung. Um Ihnen mehr Kontrolle zu ermöglichen, führt Braze detaillierte Berechtigungen ein, eine flexiblere und präzisere Methode zur Verwaltung des Benutzerzugriffs auf Ihr Konto.

Die Migration umfasst folgende Vorteile:

- **Präzisere Steuerung:** Detaillierte Berechtigungen bieten mehr Kontrolle, höhere Sicherheit und eine übersichtlichere Übersicht. Nutzer:innen erhalten ausschließlich die Zugriffsrechte, die sie benötigen.
- **Automatische Abbildung:** Alle aktuellen Berechtigungen werden automatisch ihren [granularen Entsprechungen](#legacy-to-granular-permissions-mapping) abgebildet. Ihre Nutzer:innen behalten die gleiche Zugriffsebene, sofern Sie diese nicht ändern.

## Zu überprüfen

Wenn für Ihr Unternehmen eine Migration geplant ist, erhalten Ihre Braze-Administratoren E-Mails und Banner im Dashboard, die sie über die Migration der detaillierten Berechtigungen informieren. Zur Vorbereitung der Migration empfehlen wir, dass ein Braze-Administrator die folgenden Schritte durchführt.

1. Identifizieren Sie Nutzer:innen, Rollen oder Berechtigungssätze, die möglicherweise aktualisiert werden müssen, um nach der Migration zum neuen Berechtigungsrahmen einen individuelleren Zugriff zu ermöglichen. 
2. Sollte Ihr Unternehmen die Benutzerbereitstellung mithilfe von SCIM oder Compliance-Tools automatisiert haben, die auf [Berechtigungs-Strings]({{site.baseurl}}/scim_api_appendix/) basieren, aktualisieren Sie diese bitte entsprechend der neuen granularen Struktur. 
3. Bitte informieren Sie Ihre Braze-Nutzer:innen über bevorstehende Änderungen, um Unklarheiten zu vermeiden.
4. Zum Zeitplan für die Migration und zur geplanten Migrationszeit wird Ihr Unternehmen automatisch auf granulare Berechtigungen umgestellt. Von den Unternehmensadministratoren sind keine weiteren Maßnahmen erforderlich.

{% alert important %}
Die Möglichkeit zum Update der Berechtigungen wird 15 Minuten vor dem Zeitplan für die Migration gesperrt. Dies bedeutet, dass Sie bis zum Abschluss der Migration, die voraussichtlich bis zu 15 Minuten dauern wird, keine Berechtigungen ändern können.
{% endalert %}

## Abbildung von Legacy- zu granularen Berechtigungen

Diese Tabelle zeigt die Abbildung der einzelnen alten Berechtigungen auf die detaillierten Berechtigungen. Bitte referenzieren Sie diese Tabelle, wenn Sie Ihre Berechtigungen Updateen. Um einem Nutzer:in beispielsweise denselben Zugriff wie die alte Berechtigung „E-Mail-Einstellungen verwalten” zu gewähren, muss dieser Nutzer:in sowohl über die detaillierte Berechtigung „E-Mail-Einstellungen anzeigen” als auch über die Berechtigung „E-Mail-Einstellungen bearbeiten” verfügen.

| | Bestehende Berechtigungen | Detaillierte Berechtigungen |
|---------------|---------------|---------------|
| **Ebene** | **Name** | **Name** |
| Admin | Admin | Admin |
| Workspace | Workspace-Administrator | Workspace-Administrator |
| Unternehmen | Workspaces erstellen und löschen | Workspaces erstellen und löschen |
| Unternehmen | Unternehmenseinstellungen verwalten | Unternehmenseinstellungen verwalten |
| Workspace | Greifen Sie auf Kampagnen, Leinwände, Karten, Inhaltsblöcke, Feature-Flags, Segmente, Medienbibliothek, Standorte, Promotion-Codes und Präferenzzentren zu. | Kampagnen anzeigen<br>Kampagnen bearbeiten<br>Kampagnen archivieren<br>Canvase anzeigen<br>Canvase bearbeiten<br>Canvase archivieren<br>Frequency-Capping-Regeln anzeigen<br>Frequency-Capping-Regeln bearbeiten<br>Priorisierung von Nachrichten anzeigen<br>Priorisierung von Nachrichten bearbeiten<br>Content-Blöcke anzeigen<br>Feature-Flags anzeigen<br>Feature-Flags bearbeiten<br>Feature-Flags archivieren<br>Segmente anzeigen<br>Segmente bearbeiten<br>Globale Kontrollgruppe bearbeiten<br>IAM-Templates anzeigen<br>IAM-Templates bearbeiten<br>IAM-Templates archivieren<br>E-Mail-Templates anzeigen<br>E-Mail-Templates bearbeiten<br>E-Mail Templates archivieren<br>Webhook-Templates anzeigen<br>Webhook-Templates bearbeiten<br>Webhook-Templates archivieren<br>Link-Templates anzeigen<br>Link-Templates bearbeiten<br>Mediathek Assets ansehen<br>Standorte anzeigen<br>Standorte bearbeiten<br>Standorte archivieren<br>Aktionscodes anzeigen<br>Aktionscodes bearbeiten<br>Exportförderungsaktionscodes<br>Präferenzzentren anzeigen<br>Präferenzzentren bearbeiten<br>Berichte bearbeiten<br>Banner-Templates anzeigen<br>Mehrsprachige Einstellungen anzeigen<br>Operator verwenden<br>Entscheidungsstudio-Agenten anzeigen<br>Entscheidungsstudio-Konversions-Event anzeigen |
| Workspace | Dev-Konsole öffnen | API-Schlüssel anzeigen<br>API-Schlüssel bearbeiten<br>Interne Gruppen anzeigen<br>Interne Gruppen bearbeiten<br>Interne Gruppen löschen<br>Nachrichten-Aktivitätsprotokoll anzeigen<br>Event-Nutzerprotokoll anzeigen<br>API-Bezeichner anzeigen<br>Dashboard zur API-Nutzung anzeigen<br>API-Limits anzeigen<br>API-Nutzungsmeldungen anzeigen<br>API-Nutzungsmeldungen bearbeiten<br>SDK Debugger anzeigen<br>SDK-Debugger bearbeiten |
| Workspace | Kampagnen genehmigen und ablehnen | Kampagnen genehmigen |
| Workspace | Canvase genehmigen und ablehnen | Canvase genehmigen |
| Workspace | Benutzerdaten exportieren | Benutzerdaten exportieren |
| Workspace | Benutzerdaten importieren und aktualisieren | Importierte Nutzer:innen anzeigen<br>Nutzer:innen importieren<br>Nutzerdaten bearbeiten |
| Workspace | Segmente bearbeiten | Segmente archivieren |
| Workspace | Content-Blöcke starten und verwalten | Content-Blöcke bearbeiten<br>Content-Blöcke archivieren<br>Content-Blöcke starten |
| Workspace | Medienbibliothek verwalten | Assets der Medienbibliothek bearbeiten<br>Assets der Medienbibliothek löschen |
| Workspace | Präferenzzentren starten | Präferenzzentren starten |
| Workspace | Apps verwalten | App-Einstellungen anzeigen<br>App-Einstellungen bearbeiten<br>Push-Einstellungen anzeigen<br>Push-Einstellungen bearbeiten<br>Banner-Templates bearbeiten<br>Banner-Templates archivieren |
| Workspace | Kataloge verwalten Dashboard Berechtigung | Kataloge anzeigen<br>Kataloge bearbeiten<br>Kataloge exportieren<br>Kataloge löschen |
| Workspace | Dashboard-Nutzer:innen verwalten | Dashboard-Nutzer:innen bearbeiten |
| Workspace | E-Mail-Einstellungen verwalten | E-Mail-Einstellungen anzeigen<br>E-Mail-Einstellungen bearbeiten |
| Workspace | Ereignisse, Attribute und Einkäufe verwalten | Angepasste Attribute anzeigen<br>Angepasste Attribute bearbeiten<br>Sperrliste für angepasste Attribute<br>Angepasste Attribute löschen<br>Angepasste Attribute exportieren<br>Angepasste Events anzeigen<br>Angepasste Events bearbeiten<br>Sperrliste für angepasste Events<br>Angepasste Events löschen<br>Angepasste Events exportieren<br>Segmentierung von angepassten Event-Eigenschaften bearbeiten<br>Produkte anzeigen<br>Produkte bearbeiten<br>Sperrliste für Produkte<br>Segmentierung von Kaufeigenschaften bearbeiten |
| Workspace | Externe Integrationen verwalten | Technologiepartner bearbeiten<br>Cloud-Datenaufnahme bearbeiten |
| Workspace | Einstellungen für mehrere Sprachen verwalten | Einstellungen für die Lokalisierung bearbeiten<br>Einstellungen für die Lokalisierung löschen |
| Workspace | Abonnementgruppen verwalten | Abos bearbeiten |
| Workspace | Tags verwalten | Tags anzeigen<br>Tags bearbeiten<br>Tags löschen |
| Workspace | Teams verwalten | Teams anzeigen<br>Teams bearbeiten<br>Teams archivieren |
| Workspace | Datentransformationen anzeigen | Datentransformation anzeigen |
| Workspace | Datentransformationen bearbeiten | Datentransformation bearbeiten |
| Workspace | Verwaltung der Verschlüsselung der Nutzerdaten | Verschlüsselung auf Bezeichner-Feldebene bearbeiten |
| Workspace | Kampagnen versenden, Leinwände | Kampagnen starten<br>Canvase starten |
| Workspace | Rechnungsdetails anzeigen | Rechnungsdetails anzeigen |
| Workspace | Currents-Integrationen anzeigen | Currents-Integrationen anzeigen |
| Workspace | Currents-Integrationen bearbeiten | Currents-Integrationen bearbeiten |
| Workspace | Als PII gekennzeichnete angepasste Attribute anzeigen | Als PII gekennzeichnete angepasste Attribute anzeigen |
| Workspace | PII anzeigen | PII anzeigen |
| Workspace | Nutzerprofile PII-konform anzeigen | Nutzerprofile PII-konform anzeigen |
| Workspace | Nutzungsdaten anzeigen | Nutzungsdaten anzeigen |
| Workspace | Doppelte Nutzer:innen zusammenführen | Doppelte Nutzer:innen zusammenführen |
| Workspace | Vorschau doppelter Nutzer:innen anzeigen | Vorschau doppelter Nutzer:innen anzeigen |
| Workspace | Canvas-Templates erstellen und bearbeiten | Canvas-Templates bearbeiten |
| Workspace | Canvas-Templates anzeigen | Canvas-Templates anzeigen |
| Workspace | Canvas-Templates archivieren | Canvas-Templates archivieren |
| Workspace | Startseiten veröffentlichen | Startseiten veröffentlichen |
| Workspace | Entwürfe für Startseite erstellen | Entwürfe für Landing-Pages bearbeiten |
| Workspace | Startseiten aufrufen | Landing-Pages anzeigen |
| Workspace | Landing-Page-Templates erstellen und bearbeiten | Landing-Page-Templates bearbeiten |
| Workspace | Landing-Page-Templates anzeigen | Landing-Page-Templates anzeigen |
| Workspace | Landing-Page-Templates archivieren | Landing-Page-Templates archivieren |
| Workspace | Angepasste KI-Agenten anzeigen | Angepasste KI-Agenten anzeigen |
| Workspace | Angepasste KI-Agenten bearbeiten | Angepasste KI-Agenten bearbeiten<br> Archiv Angepasste KI-Agenten |
| Workspace | Platzierungen ansehen | Platzierungen ansehen |
| Workspace | Platzierungen bearbeiten | Platzierungen bearbeiten |
| Workspace | Platzierungen archivieren | Platzierungen archivieren |
| Workspace | Neu | Nutzer:innen zusammenführen anzeigen |
| Workspace | Neu | Zu löschende Nutzer-Datensätze anzeigen |
| Workspace | Neu | Nutzer:innen aus Dashboard löschen |
| Workspace | Neu | Banner-Templates anzeigen |
| Workspace | Neu | Banner-Templates bearbeiten |
| Workspace | Neu | Banner-Templates archivieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Häufig gestellte Fragen

### Ist es möglich, die Migration abzulehnen oder rückgängig zu machen?

Braze unterstützt keine Rückgängigmachung der Migration. Wir werden Sie während der Migration unterstützen und diese genau überwachen, um etwaige Probleme umgehend zu beheben.

### Werden bestehende Nutzer:innen während der Migration den Zugriff auf Braze verlieren?

Nein, während der Migration wird es keine Ausfallzeiten für Braze geben. Während der Migration werden Updates der Berechtigungen jedoch gesperrt. Wir gehen davon aus, dass die Migration bis zu 15 Minuten dauern wird.