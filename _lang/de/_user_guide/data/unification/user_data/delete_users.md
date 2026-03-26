---
nav_title: "Nutzer:innen löschen"
article_title: "Nutzer:innen löschen"
page_order: 4.2
toc_headers: h2
description: "Erfahren Sie, wie Sie einen einzelnen Nutzer oder ein Segment von Nutzern direkt über das Braze-Dashboard löschen können."
alias: /delete_users/
---

# Nutzer:innen löschen

> Erfahren Sie, wie Sie einen einzelnen Nutzer oder ein Segment von Nutzern direkt über das Braze-Dashboard löschen können.

{% alert important %}
Das Löschen von Nutzer:innen befindet sich derzeit im Early Access. Wenden Sie sich an Ihren Customer-Success-Manager, wenn Sie an einer Teilnahme interessiert sind.
{% endalert %}

## Voraussetzungen

Um Nutzer:innen zu löschen, müssen Sie Administrator sein oder über die Berechtigung **Nutzer:in löschen** verfügen.

## Über das Löschen von Nutzer:innen

Mit der Funktion zum Löschen von Nutzer:innen können Sie Ihre Datenbank verwalten, indem Sie Profile entfernen, die nicht mehr benötigt werden, versehentlich erstellt wurden oder aus Compliance-Gründen (z. B. DSGVO oder CCPA) gelöscht werden müssen.

| Aspekt | Details |
|---------------|---------|
| Maximale Größe | Beim Löschen eines Segments können Sie bis zu 100 Millionen Nutzerprofile entfernen. |
| Wartezeit | Für alle Löschungen von Segmenten gilt eine Wartezeit von 7 Tagen zuzüglich der Zeit, die für die Verarbeitung der Löschungen erforderlich ist. |
| Auftragsbeschränkungen | Es kann jeweils nur ein Segment gelöscht werden, einschließlich der 7-tägigen Wartezeit. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Nutzer:innen löschen

Sie können eine [einzelne Nutzer:in](#delete-individual) oder ein [Segment von Nutzer:innen](#delete-segment) über das Braze-Dashboard löschen:

### Eine einzelne Nutzer:in löschen {#delete-individual}

Um eine einzelne Nutzer:in aus Braze zu löschen, gehen Sie zu **Zielgruppe** > **Nutzersuche**, suchen Sie dann nach einer Nutzer:in und wählen Sie sie aus. Wenn Sie ein doppeltes Nutzerprofil löschen möchten, vergewissern Sie sich, dass Sie das richtige ausgewählt haben.

![Die Seite „Nutzersuche" in Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Löschungen einzelner Nutzer:innen sind dauerhaft – Profile können nach dem Löschen nicht wiederhergestellt werden.  
{% endalert %}

Wählen Sie auf der Profilseite <i class="fa-solid fa-ellipsis-vertical"></i> **Optionen anzeigen** > **Nutzer:in löschen**. Bitte beachten Sie, dass es einige Minuten dauern kann, bis die Nutzer:in vollständig aus Braze gelöscht ist.

![Eine Nutzer:in in Braze mit geöffnetem Drei-Punkte-Menü, das die Option zum Löschen der Nutzer:in anzeigt.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Ein Segment löschen {#delete-segment}

Falls noch nicht geschehen, [erstellen Sie ein Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment), das die zu löschenden Nutzerprofile enthält. Stellen Sie sicher, dass Sie alle Nutzerprofile einbeziehen, wenn Sie doppelte Nutzer:innen löschen.

Gehen Sie in Braze zu **Zielgruppe** > **Zielgruppe verwalten** und wählen Sie anschließend den Tab **Nutzer:innen löschen**.

![Der Tab „Nutzer:innen löschen" im Abschnitt „Zielgruppe verwalten" des Braze-Dashboards.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Wählen Sie **Nutzer:innen löschen**, wählen Sie das Segment aus, das Sie löschen möchten, und klicken Sie dann auf **Weiter**.

![Ein Popup-Fenster mit einem Segment, das zum Löschen ausgewählt wurde.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Geben Sie **DELETE** ein, um Ihre Anfrage zu bestätigen, und wählen Sie anschließend **Nutzer:innen löschen**.

![Die Bestätigungsseite mit dem Wort „DELETE" im Bestätigungsfeld.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Die Nutzer:innen in diesem Segment werden nicht sofort gelöscht. Stattdessen werden sie für die nächsten 7 Tage als zur Löschung vorgemerkt markiert. Nach Ablauf dieser Frist werden sie gelöscht, und wir informieren Sie per E-Mail darüber.

{% alert tip %}
Um sicherzustellen, dass genau diese Nutzer:innen unabhängig von Segmentänderungen gelöscht werden, wird automatisch ein Segmentfilter namens **Zur Löschung vorgemerkt** erstellt. [Mit diesem Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) können Sie den Status ausstehender Löschungen überprüfen.
{% endalert %}

## Löschen von Segmenten bestätigen

Braze versendet eine Bestätigungs-E-Mail mit der Anzahl der zur Löschung vorgemerkten Profile.

Um mit der Löschung fortzufahren, melden Sie sich bei Braze an und bestätigen Sie die Löschanfrage.

Sollten Sie nicht innerhalb des in der E-Mail angegebenen Zeitraums bestätigen, verfällt die Löschanfrage und wird nicht weiterbearbeitet.

## Löschen von Segmenten abbrechen {#cancel}

Sie haben 7 Tage Zeit, um ausstehende Löschungen von Segmenten abzubrechen. Gehen Sie dazu zu **Zielgruppe** > **Zielgruppe verwalten** und wählen Sie dann den Tab **Nutzer:innen löschen**.

![Der Tab „Nutzer:innen löschen" im Abschnitt „Zielgruppe verwalten" des Braze-Dashboards.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Wählen Sie neben einer ausstehenden Segmentlöschung <i class="fa-solid fa-eye"></i>, um die Details zum Löschvorgang zu öffnen.

![Eine ausstehende Segmentlöschung auf dem Tab „Nutzer:innen löschen".]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

Wählen Sie in den Details zum Löschvorgang **Löschen abbrechen**.

![Das Fenster „Details zum Löschvorgang" auf dem Tab „Nutzer:innen löschen".]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Wenn die Massenlöschung von Nutzer:innen in Bearbeitung ist, können Sie diese jederzeit abbrechen. Nutzer:innen, die bereits vor dem Abbruch gelöscht wurden, können jedoch nicht wiederhergestellt werden.
{% endalert %}

## Löschstatus überprüfen {#status}

Sie können den Status einer Löschung mithilfe von [Segmentfiltern](#segment-filters), der Seite [Zielgruppe verwalten](#manage-audience) oder [Sicherheitsereignisberichten](#security-event-report) überprüfen.

### Segmentfilter

Wenn Sie die Löschung eines Segments von Nutzer:innen beantragen, wird automatisch ein [Segmentfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) namens **Zur Löschung vorgemerkt** erstellt. Sie können ihn verwenden, um:

- Die genaue Gruppe von Nutzer:innen einzusehen, die mit einem bestimmten Löschungsdatum verknüpft sind.
- Diese Nutzer:innen von Kampagnen auszuschließen, damit sie vor der Entfernung keine Nachrichten erhalten.
- Die Liste zu exportieren, falls Sie diese für Compliance-Zwecke oder zur Dokumentation benötigen.

### Zielgruppe verwalten

{% alert note %}
Um eine Liste der genauen Nutzer:innen zu erhalten, die gelöscht werden, verwenden Sie stattdessen den [Segmentfilter „Zur Löschung vorgemerkt"](#segment-filters).
{% endalert %}

Gehen Sie zu **Zielgruppe** > **Zielgruppe verwalten** und wählen Sie anschließend den Tab **Nutzer:innen löschen**.

![Der Tab „Nutzer:innen löschen" im Abschnitt „Zielgruppe verwalten" des Braze-Dashboards.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Auf dieser Seite finden Sie die folgenden allgemeinen Informationen zu allen aktuellen und ausstehenden Löschungen:

| Feld | Beschreibung |
|-------|-------------|
| Anfragedatum | Das Datum, an dem die Anfrage ursprünglich gestellt wurde. Verwenden Sie es zusammen mit dem Filter **Zur Löschung vorgemerkt**, um eine Liste der zur Löschung vorgemerkten Profile zu erhalten. |
| Angefragt von | Die Nutzer:in, die die Löschanfrage initiiert hat. |
| Segmentname | Der Name des Segments, das zur Auswahl der zur Löschung vorgesehenen Nutzer:innen verwendet wurde. |
| Status | Zeigt an, ob die Löschanfrage aussteht, in Bearbeitung ist oder abgeschlossen wurde. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Für weitere Informationen zu einer bestimmten Anfrage wählen Sie <i class="fa-solid fa-eye"></i>, um die Details zum Löschvorgang anzuzeigen. Hier können Sie auch [ausstehende Löschungen von Segmenten abbrechen](#cancel).

![Eine ausstehende Segmentlöschung auf dem Tab „Nutzer:innen löschen".]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Sicherheitsereignisbericht

Sie können den Status früherer Löschungen auch überprüfen, indem Sie einen Sicherheitsereignisbericht herunterladen. Weitere Informationen finden Sie unter [Sicherheitseinstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report).

## Häufig gestellte Fragen {#faq}

### Kann ich Segmente mit mehr als 100 Millionen Nutzer:innen löschen?

Nein. Sie können keine Segmente mit mehr als 100 Millionen Nutzer:innen löschen. Sollten Sie Unterstützung beim Löschen eines Segments dieser Größe benötigen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administrative/access_braze/support).

### Es scheint, als könnte ich keine 100 Millionen Nutzer:innen löschen und bin auf 10 Millionen beschränkt. Handelt es sich hierbei um einen Fehler?

Nein, dies ist kein Fehler. Bestimmte Kund:innen unterliegen während des Early-Access-Programms (EA) einer Beschränkung hinsichtlich der Anzahl der Nutzer:innen, die sie löschen können.

Im Zuge der Weiterentwicklung des EA-Programms soll diese Kapazität erhöht werden, bis alle Kund:innen bis zu 100 Millionen Nutzer:innen löschen können.

Sollten Sie diese Kapazität erhöhen wollen, wenden Sie sich bitte an Ihren Braze-Account-Manager. Anfragen werden nach Ermessen des Produkt-Teams genehmigt.

### Hat die automatisierte Zusammenführung von Nutzer:innen Auswirkungen auf die Löschung von Nutzer:innen?

Wenn eine geplante Zusammenführung Nutzerprofile enthält, die zur Löschung vorgemerkt sind, überspringt Braze diese Profile und führt keine Zusammenführung durch. Um diese Profile zusammenzuführen, müssen Sie sie aus der Löschung entfernen.

### Was geschieht mit Daten, die an Nutzer:innen gesendet werden, deren Löschung aussteht?

Daten, die von externen Systemen oder SDKs gesendet werden, werden weiterhin akzeptiert, jedoch werden die Nutzer:innen unabhängig von ihrer Aktivität gemäß dem Zeitplan gelöscht.

### Werden Canvase und Kampagnen für Nutzer:innen ausgelöst, die zur Löschung vorgemerkt sind?

Ja. Sie können jedoch einen Segment-Einschlussfilter hinzufügen, um alle Nutzer:innen mit dem [Segmentfilter](#segment-filters) **Zur Löschung vorgemerkt** auszuschließen.

### Können gelöschte Nutzerprofile wiederhergestellt werden?

Das Löschen einzelner Nutzer:innen ist dauerhaft.

Sie können [Segmentlöschungen](#cancel) innerhalb der ersten 7 Tage abbrechen. Allerdings können Nutzer:innen, die bereits vor dem Abbruch gelöscht wurden, nicht wiederhergestellt werden.