---
nav_title: Übertragung zwischen Workspaces
article_title: Übertragen Sie Rufnummern und Abo-Gruppen zwischen Workspaces
page_order: 4
description: "In diesem referenzierten Artikel erfahren Sie, wie Sie Ihre WhatsApp-Telefonnummer und Abo-Gruppen zwischen Workspaces übertragen können."
page_type: reference
channel:
  - WhatsApp
---

# Übertragung von WhatsApp-Telefonnummern und Abo-Gruppen zwischen Workspaces

> Auf dieser Seite erfahren Sie, wie Sie eine WhatsApp Business Account (WABA)-Telefonnummer und die zugehörige Abo-Gruppe innerhalb von Braze von einem Workspace in einen anderen verschieben können. Dieser Prozess vereinfacht die Nutzung von WhatsApp mit Braze und reduziert den Bedarf an technischer Hilfe.

## Voraussetzungen

- Stellen Sie sicher, dass Sie sowohl im ursprünglichen als auch im neuen Workspace über die [Nutzer:in-Berechtigung]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) "Abo-Gruppen verwalten" verfügen.
- Die WABA kann nicht mehrere [Braze-Cluster]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) durchqueren. Das ist unwahrscheinlich, wenn Sie in einem einzigen Unternehmen arbeiten. 

## Übertragen einer Telefonnummer und Abo-Gruppe

### Schritt 1: Archivieren Sie die Abo-Gruppe

Um eine WhatsApp Abo-Gruppe zu archivieren, gehen Sie folgendermaßen vor:

1. Gehen Sie zu dem Workspace, in dem die Abo-Gruppe derzeit existiert.
2. Gehen Sie zu **Zielgruppe** > **Abo-Gruppen-Verwaltung** und suchen Sie die Abo-Gruppe, die mit der WhatsApp-Telefonnummer verbunden ist, die Sie verschieben möchten.
3. Bewegen Sie den Mauszeiger über den Status der Abo-Gruppe und wählen Sie <i class="fa-solid fa-box-archive"></i> **Archiv**. Dadurch wird die Abo-Gruppe als inaktiv markiert, aber nicht gelöscht.

!["Archiv"-Button, der erscheint, wenn Sie den Mauszeiger über den Status "Aktiv" einer Abo-Gruppe bewegen.]({% image_buster /assets/img/whatsapp/archive_subscription_group.png %}){: style="max-width:70%;"}

### Schritt 2: Integrieren Sie die WhatsApp-Telefonnummer in den neuen Workspace

1. Gehen Sie zu dem Workspace, in den Sie die WhatsApp-Telefonnummer verschieben möchten.
2. Gehen Sie zu **Partnerintegrationen** > **Technologiepartner** > **WhatsApp**, und blättern Sie dann zum Abschnitt **WhatsApp Messaging Integration**. 
3. Wählen Sie die Option **Neue Abo-Gruppe und Rufnummer erstellen**
4. Starten Sie den Integrationsprozess, bei dem Sie die Rufnummer aus der archivierten Abo-Gruppe auswählen können.

### Schritt 3: Überprüfen Sie die Integration

1. Bestätigen Sie nach Abschluss der Integration, dass die WhatsApp-Telefonnummer jetzt mit der Abo-Gruppe im neuen Workspace verknüpft ist.
2. Testen Sie, ob Nachrichten über diese WhatsApp-Telefonnummer gesendet und empfangen werden können.

## Überlegungen

- Wenn Sie die WhatsApp-Telefonnummer zurück in den ursprünglichen Workspace übertragen müssen, wiederholen Sie die Schritte. Archivieren Sie die Abo-Gruppe im Workspace des Ziels und integrieren Sie sie dann in den ursprünglichen Workspace.
- Sie müssen die WhatsApp-Telefonnummer während der Übertragung nicht aus Ihrem Meta Business Manager:in entfernen.