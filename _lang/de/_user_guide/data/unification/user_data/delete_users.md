---
nav_title: "Löschen von Nutzer:innen"
article_title: "Löschen von Nutzer:innen"
page_order: 4.2
toc_headers: h2
description: "Erfahren Sie, wie Sie einen einzelnen Nutzer:innen oder ein Segment von Nutzern:innen direkt über das Braze-Dashboard löschen können." 
---

# Löschen von Nutzer:innen

> Erfahren Sie, wie Sie einen einzelnen Nutzer:innen oder ein Segment von Nutzern:innen direkt über das Braze-Dashboard löschen können.

{% alert important %}
Dieses Feature befindet sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Customer-Success-Manager:in, wenn Sie an einer Teilnahme interessiert sind.
{% endalert %}

## Voraussetzungen

Um Nutzer:innen zu löschen, müssen Sie Administrator sein oder die Berechtigung zum **Löschen von Nutzern** haben.

## Über das Löschen von Nutzer:innen

Mit der Funktion zum Löschen von Nutzern:innen können Sie Ihre Datenbank verwalten, indem Sie Profile entfernen, die nicht mehr benötigt werden, irrtümlich erstellt wurden oder aus Compliance-Gründen (z.B. DSGVO oder CCPA) gelöscht werden müssen.

| Betrachtung | Details |
|---------------|---------|
| Maximale Größe | Sie können bis zu 100 Millionen Nutzerprofile löschen, wenn Sie ein Segment löschen. |
| Wartezeit | Für alle Segmente, die gelöscht werden, gilt eine Wartezeit von 7 Tagen zuzüglich der Zeit, die für die Bearbeitung von Löschungen benötigt wird. |
| Auftragsbeschränkungen | Es kann immer nur ein Segment auf einmal gelöscht werden, einschließlich der 7-tägigen Wartezeit. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Löschen von Nutzer:innen

Sie können einen [einzelnen Nutzer](#delete-individual):innen oder ein [Segment von Nutzern](#delete-segment):innen über das Braze-Dashboard löschen:

### Löschen einer Person {#delete-individual}

Um einen einzelnen Nutzer:innen aus Braze zu löschen, gehen Sie zu **Zielgruppe** > **Nutzer:innen suchen**, suchen Sie einen Nutzer:innen und wählen Sie ihn aus. Wenn Sie ein doppeltes Nutzerprofil löschen wollen, überprüfen Sie, ob Sie das richtige ausgewählt haben.

![Die Seite 'Nutzer:innen suchen' in Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
Die Löschung eines einzelnen Nutzers ist dauerhaft - Profile können nach der Löschung nicht wiederhergestellt werden.  
{% endalert %}

Wählen Sie auf der Seite ihres Profils <i class="fa-solid fa-ellipsis-vertical"></i> **Optionen anzeigen** > **Nutzer:innen löschen**. Denken Sie daran, dass es einige Minuten dauern kann, bis die Nutzer:innen in Braze vollständig gelöscht sind.

Ein Nutzer:innen in Braze mit geöffnetem Vertikal-Ellipsen-Menü, das die Option zum Löschen des Nutzers anzeigt.]({% image_buster /assets/img/audience_management/deleting_users/delete_user.png %}){: style="max-width:85%;"}

### Löschen eines Segments {#delete-segment}

Falls Sie dies noch nicht getan haben, [erstellen Sie ein Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) mit den Nutzerprofilen, die Sie löschen möchten. Achten Sie darauf, dass Sie alle Nutzerprofile einbeziehen, wenn Sie doppelte Nutzer:innen löschen.

Gehen Sie in Braze zu **Zielgruppe** > **Zielgruppe verwalten** und wählen Sie dann den Tab **Nutzer:innen löschen**.

![Der Tab 'Nutzer:innen löschen' im Abschnitt 'Zielgruppe verwalten' des Braze-Dashboards.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Wählen Sie **Nutzer:innen löschen**, wählen Sie das Segment, das Sie löschen möchten, und wählen Sie dann **Weiter**.

![Ein Popup-Fenster mit einem Segment, das zum Löschen ausgewählt wurde.]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

Geben Sie **DELETE** ein, um Ihre Anfrage zu bestätigen, und wählen Sie anschließend **Nutzer:innen löschen**.

![Die Bestätigungsseite mit der Eingabe von 'LÖSCHEN' im Bestätigungsfeld.]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

Die Nutzer:innen in diesem Segment werden nicht sofort gelöscht. Stattdessen werden sie für die nächsten 7 Tage als zur Löschung anstehend markiert. Nach Ablauf dieser Frist werden sie gelöscht und wir mailen Ihnen, um Sie darüber zu informieren.

{% alert tip %}
Um sicherzustellen, dass genau diese Nutzer:innen unabhängig von Segmentänderungen gelöscht werden, wird automatisch ein Filter mit dem Namen **Ausstehende Löschung** erstellt. Sie können [diesen Filter verwenden]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters), um den Status ausstehender Löschungen zu überprüfen.
{% endalert %}

## Löschen von Segmenten abbrechen {#cancel}

Sie haben 7 Tage Zeit, um anstehende Segmentierungen zu stornieren. Um den Vorgang abzubrechen, gehen Sie zu **Zielgruppe** > **Zielgruppe verwalten** und wählen Sie dann den Tab **Nutzer:innen löschen**.

![Der Tab 'Nutzer:innen löschen' im Abschnitt 'Zielgruppe verwalten' des Braze-Dashboards.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Wählen Sie neben einer anstehenden Segmentierung <i class="fa-solid fa-eye"></i> aus, um die Details des Löschungsdatensatzes zu öffnen.

![Eine anstehende Segmentierung auf dem Tab 'Nutzer:innen löschen'.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

Wählen Sie in den Details des Löschdatensatzes **Löschung abbrechen**.

![Das Fenster 'Details des Löschdatensatzes' auf dem Tab 'Nutzer:innen löschen'.]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
Wenn die Massenlöschung von Nutzer:innen im Gange ist, können Sie sie jederzeit abbrechen. Nutzer:innen, die bereits vor der Löschung gelöscht wurden, können jedoch nicht wiederhergestellt werden.
{% endalert %}

## Überprüfen des Löschungsstatus {#status}

Sie können den Status einer Löschung mit Hilfe von [Segment-Filtern](#segment-filters), der Seite [Zielgruppe verwalten](#manage-audience) oder [Sicherheitsereignisberichten](#security-event-report) überprüfen.

### Filter für Segmente

Wenn Sie eine Anfrage zur Löschung eines Segments von Nutzer:innen stellen, wird automatisch ein [Segment Filter]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#filters) mit dem Namen **Ausstehende Löschung** erstellt. Sie können es verwenden, um:

- Sehen Sie sich die genaue Menge der Nutzer:innen an, die mit einem bestimmten Löschungsdatum verbunden sind.
- Schließen Sie diese Nutzer:innen von Kampagnen aus, damit sie keine Nachrichten vor der Entfernung erhalten.
- Exportieren Sie die Liste, wenn Sie sie für die Einhaltung von Vorschriften oder zur Aufbewahrung von Unterlagen benötigen.

### Zielgruppe managen

{% alert note %}
Um die genaue Liste der Nutzer:innen zu erhalten, die gelöscht werden sollen, verwenden Sie stattdessen den [Filter Segmente für ausstehende Löschungen](#segment-filters).
{% endalert %}

Gehen Sie zu **Zielgruppe** > **Zielgruppe verwalten** und wählen Sie dann den Tab **Nutzer:innen löschen**.

![Der Tab 'Nutzer:innen löschen' im Abschnitt 'Zielgruppe verwalten' des Braze-Dashboards.]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

Auf dieser Seite finden Sie die folgenden allgemeinen Informationen zu allen laufenden und anstehenden Löschungen:

| Feld | Beschreibung |
|-------|-------------|
| Datum der Anfrage | Das Datum, an dem die Anfrage ursprünglich gestellt wurde. Verwenden Sie ihn zusammen mit dem Filter **Ausstehende Löschung**, um die Liste der Profile zu erhalten, die zur Löschung anstehen. |
| Angefragt von | Der Nutzer:innen, der die Anfrage zur Löschung initiiert hat. |
| Segmentname | Der Name des Segments, das zum Auswählen der Nutzer:innen verwendet wird, die zur Löschung anstehen. |
| Status | Zeigt an, ob die Anfrage zur Löschung ausstehend, in Bearbeitung oder abgeschlossen ist. |  
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Wenn Sie weitere Einzelheiten zu einer bestimmten Anfrage wünschen, wählen Sie <i class="fa-solid fa-eye"></i>, um die Details des Löschungsdatensatzes anzuzeigen. Hier können Sie auch [ausstehende Segmentierungen abbrechen](#cancel).

![Eine anstehende Segmentierung auf dem Tab 'Nutzer:innen löschen'.]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### Bericht über Sicherheitsereignisse

Sie können auch den Status früherer Löschungen überprüfen, indem Sie einen Bericht über Sicherheitsereignisse herunterladen. Weitere Informationen finden Sie unter [Sicherheitseinstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#security-event-report).

## Häufig gestellte Fragen {#faq}

### Kann ich Segmente mit mehr als 100 Millionen Nutzer:innen löschen?

Nein. Sie können keine Segmente mit mehr als 100 Millionen Nutzer:innen löschen. Wenn Sie Hilfe beim Löschen eines Segments dieser Größe benötigen, wenden Sie sich an [support@braze.com](mailto:support@braze.com).

### Hat die automatische Zusammenführung von Nutzer:innen Auswirkungen auf die Löschung von Nutzern?

Wenn ein Zeitplan für die Zusammenführung Nutzer:innen-Profile enthält, die zur Löschung anstehen, überspringt Braze diese Profile und führt sie nicht zusammen. Um diese Profile zusammenzuführen, müssen Sie sie vom Löschvorgang ausschließen.

### Was geschieht mit Daten, die an Nutzer:innen gesendet werden, die auf ihre Löschung warten?

Daten, die von externen Systemen oder SDKs gesendet werden, werden weiterhin akzeptiert, aber die Nutzer:innen werden unabhängig von ihrer Aktivität wie geplant gelöscht.

### Werden Canvase und Kampagnen für Nutzer:innen triggern, die zur Löschung anstehen?

Ja Sie können jedoch einen Segmenteinschlussfilter hinzufügen, um alle Nutzer:innen mit dem [Segmentfilter](#segment-filters) **Ausstehende Löschung** auszuschließen.

### Kann ich gelöschte Nutzerprofile wiederherstellen?

Die Löschung einzelner Nutzer:innen ist dauerhaft.

Sie können [Segmente](#cancel) innerhalb der ersten 7 Tage nach der Löschung [stornieren](#cancel). Nutzer:innen, die vor der Löschung gelöscht wurden, können jedoch nicht wiederhergestellt werden.
