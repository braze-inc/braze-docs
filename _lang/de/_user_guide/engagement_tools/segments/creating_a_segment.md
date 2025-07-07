---
nav_title: Ein Segment erstellen
article_title: Ein Segment erstellen
page_order: 1
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie mit Braze ein Segment einrichten und erstellen."
tool: Segments
search_rank: 3
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"}Erstellen eines Segments

> Die Segmentierung ermöglicht es Ihnen, Benutzer auf der Grundlage ihrer demografischen, verhaltensbezogenen oder technischen Merkmale und Aktionen anzusprechen. Durch den kreativen und intelligenten Einsatz von Segmentierung und Nachrichtenautomatisierung können Sie Ihre Nutzer nahtlos vom Erstkontakt zum langfristigen Kunden machen. Segmente werden in Echtzeit aktualisiert, wenn sich Daten ändern. Sie können so viele Segmente erstellen, wie Sie für Ihre Targeting- und Messaging-Zwecke benötigen.

## Schritt 1: Zum Abschnitt „Segmente“ navigieren

Gehen Sie zu **Zielgruppe** > **Segmente**.

## Schritt 2: Benennen Sie Ihr Segment

Wählen Sie **Segment erstellen**, um mit der Erstellung Ihres Segments zu beginnen. Benennen Sie Ihr Segment, indem Sie den Nutzertyp beschreiben, nach dem Sie filtern möchten. Dies hilft Ihnen, das Segment zu identifizieren, wenn Sie es für Ihre Kampagnen oder Canvase auswählen möchten. Ungenaue Segmenttitel können verwirrend sein.

Optional können Sie auch Folgendes tun:
- Fügen Sie dem Segment eine Beschreibung hinzu, um mehr Details über die Absicht dieses Publikums zu liefern, und hinterlassen Sie Notizen, auf die andere Teammitglieder zurückgreifen können.
- Fügen Sie ein [Team]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) zu Ihrem Segment hinzu.
- Fügen Sie Ihrem Segment zur weiteren Organisation [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu.

![Erstellen Sie ein Segment-Modal, in dem das Segment „Passive Nutzer:innen“ heißt und die Segmentbeschreibung „Dies ist unser Hauptsegment für passive Nutzer:innen, um inaktive Nutzer:innen innerhalb der letzten vierzehn Tage anzusprechen“ lautet. Fügen Sie zwei Buttons hinzu: „Abbrechen“ und „Segment erstellen“.][2]{: style="max-width:70%;"}

## Schritt 3: Wählen Sie Ihre App oder Plattform

Wählen Sie, welche Apps oder Plattformen Sie anvisieren möchten, indem Sie **Benutzer aus allen Apps** (Standard) oder **Benutzer aus bestimmten Apps** auswählen. Wenn Sie **Benutzer aus allen Apps** wählen, umfasst das Segment alle Benutzer, unabhängig von Sitzungs- oder App-Daten. Wenn Sie **Nutzer aus bestimmten Apps** wählen, können Sie anschließend auswählen, welche Apps oder Plattformen Sie in Ihr Segment aufnehmen möchten.

Wenn Sie zum Beispiel eine In-App-Nachricht nur an iOS-Geräte senden möchten, wählen Sie Ihre iOS-App aus. So wird sichergestellt, dass Benutzer, die sowohl ein iOS- als auch ein Android-Gerät verwenden, die Nachricht nur auf ihrem iOS-Gerät erhalten. In der Liste der spezifischen Apps können Sie mit der Option **Benutzer aus keinen Apps** Benutzer ohne Sitzungen und ohne App-Daten (die in der Regel über den Benutzerimport oder die REST-API erstellt wurden) aufnehmen.

![Segmentdetails mit der Option „Nutzer:innen aus allen Apps“ im Abschnitt „Verwendete Apps“.][5]{: style="max-width:70%;"}

## Schritt 4: Filter zu Ihrem Segment hinzufügen

Fügen Sie mindestens einen Filter zu Ihrem Segment hinzu. Sie können so viele Filter kombinieren, wie Sie möchten, um Ihre Segmentierung zu präzisieren.

{% alert note %}
Braze erstellt erst dann Profile für Benutzer, wenn diese die App zum ersten Mal verwendet haben. Sie können also keine Benutzer ansprechen, die Ihre App noch nicht geöffnet haben.
{% endalert %}

#### Gruppen filtern

Filter sind in Filtergruppen organisiert. Jeder Filter muss Teil einer Filtergruppe sein, die aus mindestens einem Filter besteht. Ein Segment kann mehrere Filtergruppen haben. Um eine hinzuzufügen, wählen Sie **Filtergruppe hinzufügen**. Bearbeiten Sie den Namen der Filtergruppe, indem Sie auf das Symbol klicken, das erscheint, wenn Sie den Mauszeiger daneben halten.

![Filtergruppe mit einem Bearbeitungssymbol neben ihrem Namen.][14]{: style="max-width:70%;"}

Wählen Sie die Symbole neben den einzelnen Filtern, um den Filter-Editor zu schließen, den Filter zu duplizieren oder den Filter zu entfernen. Nachdem Sie einen Filter dupliziert haben, können Sie seine Werte in jedem Dropdown-Menü anpassen.

Sie können auch das Symbol innerhalb jeder Filtergruppe verwenden, um diese Filtergruppe und die darin enthaltenen Filter zu duplizieren oder diese Filtergruppe aus Ihrem Segment zu löschen.

#### Segmentierungslogik mit AND und OR

Innerhalb einer Filtergruppe können Filter entweder mit "UND" oder "ODER" verknüpft werden. Zwischen Filtergruppen können Gruppen entweder durch "UND" oder "ODER" verbunden werden. Wenn Sie Filtergruppen verwenden, können Sie eine Segmentierungslogik erstellen. Beispiel:
- (A UND B UND C) ODER (C UND E UND F)
- (A ODER B ODER C) UND (C ODER D ODER F)

Wenn Sie "ODER" für Ihre Filter auswählen, bedeutet dies, dass Ihr Segment Nutzer enthält, die eine beliebige Kombination aus einem, einigen oder allen dieser Filter erfüllen. Wenn Sie „UND“ auswählen, werden Nutzer:innen, die diesen Filter nicht bestehen, nicht in Ihr Segment aufgenommen.

{% alert tip %}
Wenn Sie „ODER“ für Filter auswählen, die einen negativen Filter enthalten (z. B. „ist nicht“ in einer Abonnementgruppe), denken Sie daran, dass Nutzer:innen nur einen der „ODER“-Filter erfüllen müssen, um in das Segment aufgenommen zu werden. Um den Negativfilter unabhängig von den anderen Filtern anzuwenden, verwenden Sie eine [Ausschlussgruppe](#exclusion).
{% endalert %}

#### Filteroperatoren

Je nach dem von Ihnen gewählten Filter stehen Ihnen verschiedene Operatoren zur Identifizierung von Filterwerten zur Verfügung. Wenn Sie mehr über die Operatoren erfahren möchten, die für die verschiedenen Arten von benutzerdefinierten Attributen verfügbar sind, lesen Sie den Abschnitt [Speicherung von benutzerdefinierten Attributen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes). Beachten Sie, dass Sie bei Verwendung des Operators „ist irgendein von“ maximal 256 Elemente in dieses Feld aufnehmen können.

{% alert note %}
Braze erstellt erst dann Profile für Benutzer, wenn diese die App zum ersten Mal verwendet haben. Sie können also keine Benutzer ansprechen, die Ihre App noch nicht geöffnet haben.
{% endalert %}

![Segmenter-Filtergruppen mit dem Operator AND.][9]{: style="max-width:70%;"}

{% alert important %}
Segmente, die bereits den Filter **Segmentzugehörigkeit** verwenden, können nicht weiter einbezogen oder in andere Segmente verschachtelt werden. Dadurch wird ein Zyklus verhindert, bei dem Segment A Segment B einschließt, das dann wiederum versucht, Segment A einzuschließen. In diesem Fall würde das Segment immer wieder auf sich selbst verweisen, so dass es unmöglich wäre, zu berechnen, wer tatsächlich dazugehört.

Außerdem wird die Verschachtelung von Segmenten auf diese Weise komplizierter und kann die Arbeit verlangsamen. Erstellen Sie stattdessen das Segment, das Sie einbeziehen möchten, mit denselben Filtern neu.
{% endalert %}

#### Ausschlussgruppen (optional) {#exclusion}

Wenn Sie ein Segment erstellen, können Sie eine oder mehrere Ausschlussgruppen anwenden. Ausschlussgruppen enthalten Kriterien, die Benutzer identifizieren, die von Ihrem Segment ausgeschlossen werden sollen, und werden immer mit einem "AND NOT"-Operator mit Ihren Filtergruppen verbunden.

Ausschlussgruppen haben Vorrang vor Segmentkriterien. Wenn ein Benutzer unter die Kriterien Ihrer Ausschlussgruppen fällt, gehört er nicht zu Ihrem Segment, selbst wenn er die Kriterien Ihrer Filtergruppen erfüllt.

Erstellen Sie eine Ausschlussgruppe, indem Sie Filter hinzufügen, wie Sie es bei Filtergruppen tun würden. Die Statistik _Geschätzte erreichbare Nutzer_ in einer Ausschlussgruppe zeigt die geschätzte Anzahl der Nutzer, die nach Anwendung der Ausschlusskriterien in Ihrem Segment verbleiben.

Ausgeschlossene Benutzer werden nicht als Teil der Statistik der _insgesamt erreichbaren Benutzer_ Ihres Segments gezählt.

![Eine Ausschlussgruppe mit zwei Filtern.][12]{: style="max-width:70%;"}

#### Segmente testen

Nachdem Sie Ihrem Segment Apps und Filter hinzugefügt haben, können Sie testen, ob Ihr Segment wie erwartet eingerichtet ist, indem Sie nach einem Benutzer suchen, um zu überprüfen, ob er den Segmentkriterien entspricht. Suchen Sie dazu in der **Benutzersuche** nach dem Namen eines Benutzers `external_id` oder `braze_id`.

![Abschnitt „Nutzersuche“ mit einem Suchfeld.][6]{: style="max-width:80%;"}

Die Benutzersuche ist verfügbar, wenn:
- Ein Segment erstellen
- Einrichten einer Kampagne oder einer Canvas-Zielgruppe
- Einrichten eines Audience Paths-Schrittes

Wenn ein:e Nutzer:in den Segment-, Filter- und App-Kriterien entspricht, wird dies in einer Benachrichtigung angezeigt.

![Die Suche nach dem Benutzer "user007" löst eine Warnung aus, die besagt: "user007 passt zu allen Segmenten, Filtern und Anwendungen.][7]{: style=" max-width:80%;"}

Wenn ein Benutzer die Segment-, Filter- oder App-Kriterien ganz oder teilweise nicht erfüllt, werden die fehlenden Kriterien zur Fehlerbehebung aufgelistet.

![Eine Benutzersuche nach "user1234" löst eine Warnung aus, die besagt: "user1234 entspricht nicht den folgenden Zielkriterien:" und zeigt zwei fehlende Kriterien an: eine Betriebszugehörigkeit von mehr als einem Jahr und dass heute ein Jahrestag ist.][8]{: style=" max-width:80%;"}

#### Segmente für Einzelbenutzer

Sie können einzelne Benutzersegmente (oder Segmente einer Handvoll von Benutzern) erstellen, indem Sie eindeutige Attribute zur Identifizierung von Benutzern verwenden, wie z.B. einen Benutzernamen oder eine Benutzer-ID.

In der Segmentierungsstatistik oder der Vorschau wird dieser einzelne Benutzer jedoch möglicherweise nicht angezeigt, da die Segmentierungsstatistiken auf der Grundlage einer Zufallsstichprobe mit einem Konfidenzintervall von 95 % berechnet werden, wobei das Ergebnis innerhalb von +/- 1 % liegt. Je größer Ihre Nutzerbasis ist, desto wahrscheinlicher ist es, dass die Größe Ihres Segments nur eine grobe Schätzung ist. Um sicherzustellen, dass Ihr Segment den einzelnen Nutzer enthält, auf den Sie abzielen, wählen Sie **Exakte Statistik berechnen**. Dadurch wird die genaue Anzahl der Nutzer:innen in Ihrem Segment mit einer Genauigkeit von mehr als 99,999 % berechnet.

Braze verfügt über Testfilter, um bestimmte Nutzer:innen nach Nutzer-ID oder E-Mail-Adresse anzusprechen.

## Schritt 5: Segment speichern

Wählen Sie **Speichern**. Jetzt können Sie Nachrichten an Ihre Benutzer senden!

## Messung der Größe eines Segments

Wenn Sie wissen möchten, wie Sie die Mitgliedschaft und Größe Ihres Segments überwachen können, lesen Sie den Abschnitt [Messung der Segmentierung]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/).

## Segmente archivieren

Wenn Sie ein bestimmtes Segment nicht mehr benötigen oder nicht mehr verwenden möchten, können Sie es archivieren, indem Sie auf die Seite **Segmente** gehen und aus dem Menü in der Zeile des Segments die Option **Archivieren** wählen.

{% alert warning %}
Wenn Sie ein Segment archivieren, werden alle Kampagnen oder Canvases, die dieses Segment verwenden, ebenfalls archiviert (selbst wenn das Segment nur in einer einzigen Canvas-Komponente verwendet wird). Dies gilt auch für verschachtelte Segmente, bei denen beide Segmente und alle Kampagnen oder Canvases, die sie verwenden, ebenfalls archiviert werden.
<br><br>
Sie erhalten eine Warnung, die auflistet, welche Kampagnen und Canvases demnächst archiviert werden, indem Sie das zugehörige Segment archivieren.
{% endalert %}

Sie können die Archivierung des Segments aufheben, indem Sie auf der Seite **Segmente** zu dem Segment navigieren und dann **Archivierung aufheben** wählen.

## Zielgerichtetes Verhalten bei Benutzern mit mehreren Geräten

Nutzer:innen haben mehr als ein Gerät, wenn sie sich mit demselben Konto auf mehreren Geräten anmelden. Sie können im Abschnitt **Letzte Geräte** eines [Benutzerprofils]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) nach mehreren Geräten suchen.

Wenn Sie mit geräteabhängigen Filtern segmentieren (Gerätemodell, Betriebssystem und App-Version), enthält Ihr Segment alle Nutzer, die Ihren Filterkriterien entsprechen. Diese Nutzer:innen erhalten eine Nachricht auf allen ihren Geräten, auch auf denen, die nicht Ihren Filterkriterien entsprechen. Nehmen wir zum Beispiel an, Nutzer:in A hat zwei Geräte: Gerät 1 hat OS 13.0, und Gerät 2 hat OS 10.0. Wenn sich ein Segment an Nutzer:innen mit OS 10.0 richtet, gehört diese:r Nutzer:in zu diesem Segment und erhält Nachrichten auf beiden Geräten.

### Push-Benachrichtigungen

Sie können festlegen, dass an jede:n Nutzer:in nur eine Push-Benachrichtigung gesendet wird. Wenn [Sie Ihre Nachricht verfassen]({{ssite.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#step-4-compose-your-push-message), wählen Sie unter **Weitere Einstellungen** die Option **Nur an das zuletzt verwendete Gerät des Benutzers senden**.

![][13]{: style="max-width:60%;"}

### Überlegungen

- **Gesendete Nachrichten können die Größe der Zielgruppe übersteigen.** Wenn einige Nutzer:innen mehr als ein Gerät haben, kann jedes Gerät eine Nachricht erhalten. Dies führt zu einer höheren Anzahl von gesendeten Nachrichten als die Nutzer in Ihrem Segment.
- **Die Segmentzugehörigkeit eines Nutzers oder einer Nutzer:in sieht vielleicht nicht so aus, wie Sie es erwarten würden.**
    - Ein Benutzer kann auf seinem aktuellen Gerät anhand von Attributen angesprochen werden, die mit einem anderen Gerät verbunden sind. Wenn Sie nicht erwartet haben, dass ein:e Nutzer:in eine Nachricht erhält, überprüfen Sie das entsprechende Nutzerprofil auf mehrere Geräte.
    - Es kann sein, dass ein Nutzer zum Zeitpunkt des Versands zu Ihrem Zielsegment gehörte, aber aufgrund des Verhaltens, das mit einem seiner Geräte verbunden ist, danach nicht mehr zu diesem Segment gehört. Dies kann dazu führen, dass ein Benutzer eine Kampagne oder ein Canvas erhält, obwohl er die Filterkriterien derzeit nicht erfüllt. <br><br>Zum Beispiel könnte ein:e Nutzer:in eine Nachricht erhalten, die sich an Nutzer:innen mit einer aktuellen App-Version von OS 10.0 richtet, obwohl er oder sie derzeit OS 13.0 hat. In diesem Fall hatte der oder die Nutzer:in OS 10.0, als die Nachricht gesendet wurde, und aktualisierte danach auf OS 13.0.<br><br> Wenn ein Benutzer zu einem späteren Zeitpunkt ein Gerät mit einer anderen App-Version verwendet, wird sein Benutzerprofil mit der neuen, neuesten App-Version aktualisiert. Dies könnte den Anschein erwecken, dass der oder die Nutzer:in sich nicht für die Nachricht qualifiziert haben sollte, obwohl er oder sie sich qualifiziert hat, als die Nachricht gesendet wurde.


[1]: {% image_buster /assets/img_archive/Segment1.png %}
[2]: {% image_buster /assets/img_archive/Segment2.png %}
[3]: {% image_buster /assets/img_archive/segment_step4.png %}
[5]: {% image_buster /assets/img_archive/segment_app_selection.png %}
[6]: {% image_buster /assets/img_archive/user_lookup.png %}
[7]: {% image_buster /assets/img_archive/user_lookup_match.png %}
[8]: {% image_buster /assets/img_archive/user_lookup_nomatch.png %}
[9]: {% image_buster /assets/img_archive/segmenter_filter_groups.png %}
[11]: {% image_buster /assets/img_archive/segmenter_and_or.png %}
[12]: {% image_buster /assets/img_archive/segmenter_exclusion_groups.png %}
[13]: {% image_buster /assets/img_archive/send_to_last_device.png %}
[14]: {% image_buster /assets/img_archive/edit_filter_group_name.png %}