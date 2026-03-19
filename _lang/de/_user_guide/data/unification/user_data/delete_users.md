---
nav_title: "Nutzer:innen löschen"
article_title: "Nutzer:innen löschen"
page_order: 4.2
toc_headers: h2
description: "Erfahren Sie, wie Sie einen einzelnen Nutzer oder ein Segment von Nutzern direkt über das Braze-Dashboard löschen können."
alias: /delete_users/
hidden: true
---

# Nutzer:innen löschen

> Erfahren Sie, wie Sie einen einzelnen Nutzer oder ein Segment von Nutzern direkt über das Braze-Dashboard löschen können.

{% alert important %}
Der vorzeitige Zugriff auf dieses Feature ist vorübergehend nicht verfügbar. Bitte wenden Sie sich für weitere Informationen an Ihren Customer-Success-Manager.
{% endalert %}

## Voraussetzungen

Sie müssen Administrator sein, um Nutzer:innen löschen zu können.

## Über das Löschen von Nutzer:innen

Mit der Funktion zum Löschen von Nutzern können Sie Ihre Datenbank verwalten, indem Sie Profile entfernen, die nicht mehr benötigt werden, versehentlich erstellt wurden oder aus Compliance-Gründen (z. B. DSGVO oder CCPA) gelöscht werden müssen.

| Betrachtung | Details |
|---------------|---------|
| Maximale Größe | Beim Löschen eines Segments können Sie bis zu 100 Millionen Nutzerprofile entfernen. |
| Wartezeit | Für alle Löschungen von Segmenten gilt eine Wartezeit von sieben Tagen zuzüglich der Zeit, die für die Bearbeitung der Löschungen erforderlich ist. |
| Beschäftigungsbeschränkungen | Es kann jeweils nur ein Segment gelöscht werden, einschließlich der 7-tägigen Wartezeit. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Nutzer:innen löschen

Sie können einen [einzelnen Nutzer:in](#delete-individual) oder eine [Gruppe von Nutzern:innen](#delete-segment) über das Braze-Dashboard löschen:

### Eine Person löschen {#delete-individual}

Um einen einzelnen Nutzer aus Braze zu löschen, gehen Sie zu **„Zielgruppe“** > **„Nutzersuche“**, suchen Sie dann nach einem Nutzer und wählen Sie ihn aus. Wenn Sie ein doppeltes Nutzerprofil löschen möchten, überprüfen Sie bitte, dass Sie das richtige ausgewählt haben.

![Die Seite „Nutzersuche“ in Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Löschungen durch einzelne Nutzer:innen sind dauerhaft – Profile können nach dem Löschen nicht wiederhergestellt werden.  
{% endalert %}

Auswählen Sie auf der <i class="fa-solid fa-ellipsis-vertical"></i>Profilseite **„Optionen anzeigen**“ > **„Benutzer löschen**“. Bitte beachten Sie, dass es einige Minuten dauern kann, bis der Nutzer:in vollständig aus Braze gelöscht ist.

![Eine Nutzer:in in Braze mit geöffnetem Menü mit den vertikalen Ellipsen, das die Option zum Löschen der Nutzer:in anzeigt.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Löschen eines Segments {#delete-segment}

Falls noch nicht geschehen, [erstellen]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) Sie [bitte ein Segment,]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) das die zu löschenden Nutzerprofile enthält. Bitte stellen Sie sicher, dass Sie alle Nutzerprofile einbeziehen, wenn Sie doppelte Nutzer:innen löschen.

Bitte gehen Sie in Braze zu **„Zielgruppe** > **Zielgruppe verwalten**“ und wählen Sie anschließend die Registerkarte **„Nutzer:innen löschen**“.

![Die Registerkarte „Nutzer:innen löschen“ im Abschnitt „Zielgruppen verwalten“ des Braze-Dashboards.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Auswählen Sie **„Nutzer:innen löschen“**, wählen Sie das Segment aus, das Sie löschen möchten, und klicken Sie dann auf **„Weiter**“.

![Ein Popup-Fenster mit einem Segment, das zum Löschen ausgewählt wurde.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Geben Sie **DELETE** ein, um Ihre Anfrage zu bestätigen, und wählen Sie anschließend **Nutzer:innen löschen**.

![Die Bestätigungsseite mit dem Wort „DELETE“ im Bestätigungsfeld.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Die Nutzer:innen in diesem Segment werden nicht sofort gelöscht. Stattdessen werden sie für die nächsten 7 Tage als zur Löschung vorgesehen markiert. Nach Ablauf dieser Frist werden sie gelöscht, und wir werden Sie per E-Mail darüber informieren.

{% alert tip %}
Um sicherzustellen, dass genau diese Nutzer:innen unabhängig von Segmentänderungen gelöscht werden, wird automatisch ein Filter namens **„Zur Löschung anstehend“** erstellt. [Mit diesem Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) können Sie den Status ausstehender Löschungen überprüfen.
{% endalert %}

## Löschen von Segmenten bestätigen

Braze versendet eine Bestätigungs-E-Mail mit der Anzahl der zur Löschung anstehenden Profile.

Um mit der Löschung fortzufahren, melden Sie sich bitte bei Braze an und bestätigen Sie die Löschanfrage.

Sollten Sie nicht innerhalb des in der E-Mail angegebenen Zeitraums bestätigen, verfällt die Löschanfrage und wird nicht weiterbearbeitet.

## Löschen von Segmenten rückgängig machen {#cancel}

Sie haben 7 Tage Zeit, um ausstehende Löschungen von Segmenten zu widerrufen. Um zu löschen, gehen Sie zu **„Zielgruppe“** > **„Zielgruppe verwalten**“ und wählen Sie dann die Registerkarte **„Nutzer:innen löschen**“.

![Die Registerkarte „Nutzer:innen löschen“ im Abschnitt „Zielgruppen verwalten“ des Braze-Dashboards.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Wählen Sie neben einem ausstehenden <i class="fa-solid fa-eye"></i>Segmentlöschvorgang die Option, um die Details zum Löschvorgang auszuwählen.

![Eine ausstehende Segmentlöschung auf dem Tab „Nutzer:innen löschen“.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

Wählen Sie in den Details zum Löschvorgang **die Option „Löschen abbrechen“** aus.

![Das Fenster „Löschdatensatzdetails“ auf dem Tab „Nutzer:innen löschen“.]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Wenn die Massenlöschung von Nutzern:innen durchgeführt wird, können Sie diese jederzeit abbrechen. Nutzer:innen, die bereits vor der Kündigung gelöscht wurden, können jedoch nicht wiederhergestellt werden.
{% endalert %}

## Überprüfung des Löschstatus {#status}

Sie können den Status einer Löschung mithilfe von [Segmentfiltern](#segment-filters), der Seite [„Zielgruppen verwalten](#manage-audience)“ oder [Sicherheitsereignisberichten](#security-event-report) überprüfen.

### Segmentfilter

Wenn Sie die Löschung eines Segments von Nutzer:innen beantragen, wird automatisch ein [Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) namens **„Zur Löschung anstehend“** erstellt. Sie können es verwenden, um:

- Bitte beachten Sie die genaue Gruppe von Nutzern:innen, die mit einem bestimmten Löschungsdatum verknüpft sind.
- Bitte schließen Sie diese Nutzer:innen von Kampagnen aus, damit sie vor der Entfernung keine Nachrichten erhalten.
- Bitte exportieren Sie die Liste, falls Sie diese für Compliance-Zwecke oder zur Dokumentation benötigen.

### Zielgruppe verwalten

{% alert note %}
Um eine Liste der genauen Nutzer:innen zu erhalten, die gelöscht werden, verwenden Sie bitte den [Filter „Zur Löschung anstehende Elemente](#segment-filters)“.
{% endalert %}

Bitte gehen Sie zu **„Zielgruppe“** > **„Zielgruppe verwalten**“ und wählen Sie anschließend die Tab-Seite **„Nutzer:innen löschen**“.

![Die Registerkarte „Nutzer:innen löschen“ im Abschnitt „Zielgruppen verwalten“ des Braze-Dashboards.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Auf dieser Seite finden Sie die folgenden allgemeinen Informationen zu allen aktuellen und ausstehenden Löschungen:

| Feld | Beschreibung |
|-------|-------------|
| Anfrage-Datum | Das Datum, an dem die Anfrage ursprünglich gestellt wurde. Verwenden Sie diese Option zusammen mit dem Filter **„Zur Löschung vorgemerkt“,** um eine Liste der zur Löschung vorgemerkten Profile zu erhalten. |
| Angefragt von | Die Nutzer:in, die die Löschanfrage initiiert hat. |
| Segmentname | Der Name des Segments, das zur Auswahl der zur Löschung vorgesehenen Nutzer:innen verwendet wird. |
| Status | Zeigt an, ob die Löschanfrage aussteht, in Bearbeitung ist oder abgeschlossen wurde. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Für weitere Informationen zu einer bestimmten Anfrage wählen Sie <i class="fa-solid fa-eye"></i>bitte  aus, um die Details zum Löschvorgang anzuzeigen. Hier können Sie auch [ausstehende Löschungen von Segmenten abbrechen](#cancel).

![Eine ausstehende Segmentlöschung auf dem Tab „Nutzer:innen löschen“.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Bericht über Sicherheitsereignisse

Sie können den Status früherer Löschungen auch überprüfen, indem Sie einen Sicherheitsereignisbericht herunterladen. Weitere Informationen finden Sie unter [Sicherheitseinstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report).

## Häufig gestellte Fragen {#faq}

### Ist es möglich, Segmente mit mehr als 100 Millionen Nutzer:innen zu löschen?

Nein. Sie können keine Segmente mit mehr als 100 Millionen Nutzer:innen löschen. Sollten Sie Unterstützung beim Löschen eines Segments dieser Größe benötigen, wenden Sie sich bitte an [support@braze.com](mailto:support@braze.com).

### Es scheint, als sei es mir nicht möglich, 100 Millionen Nutzer:innen zu löschen, sondern nur 10 Millionen. Handelt es sich hierbei um einen Fehler?

Nein, dies ist kein Fehler. Bestimmte Kund:innen unterliegen während des Early-Access-Programms (EA) einer Beschränkung hinsichtlich der Anzahl der Nutzer:innen, die sie löschen können.

Im Zuge der Weiterentwicklung des EA-Programms soll diese Kapazität erhöht werden, bis alle Kund:innen bis zu 100 Millionen Nutzer:innen löschen können.

Sollten Sie diese Kapazität erhöhen wollen, wenden Sie sich bitte an Ihren Braze-Account Manager. Anfragen werden nach Ermessen des Produkt-Teams genehmigt.

### Hat die Automatisierung der Zusammenführung von Nutzern Auswirkungen auf die Löschung von Nutzern:innen?

Wenn ein Zeitplan Benutzerprofile enthält, die zur Löschung vorgesehen sind, ignoriert Braze diese Profile und führt keine Zusammenführung durch. Um diese Profile zusammenzuführen, müssen Sie sie aus der Löschliste entfernen.

### Was geschieht mit Daten, die an Nutzer:innen gesendet wurden und deren Löschung aussteht?

Daten, die von externen Systemen oder SDKs gesendet werden, werden weiterhin akzeptiert, jedoch werden die Nutzer:innen unabhängig von ihrer Aktivität gemäß dem Zeitplan gelöscht.

### Werden Canvases und Kampagnen für Nutzer:innen ausgelöst, die zur Löschung anstehen?

Ja Sie können jedoch einen Segment-Einschlussfilter hinzufügen, um alle Nutzer:innen mit dem [Segment-Filter](#segment-filters) **„Zur Löschung vorgemerkt“** auszuschließen.

### Ist es möglich, gelöschte Nutzerprofile wiederherzustellen?

Das Löschen einzelner Nutzer:innen ist dauerhaft.

Sie können [Segmentlöschungen](#cancel) innerhalb der ersten 7 Tage nach [der Löschung widerrufen](#cancel). Allerdings können Nutzer:innen, die bereits vor der Kündigung gelöscht wurden, nicht wiederhergestellt werden.
