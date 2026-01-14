---
nav_title: Ein Segment erstellen
article_title: Ein Segment erstellen
page_order: 0
page_type: tutorial
description: "In diesem Artikel erfahren Sie, wie Sie mit Braze ein Segment einrichten und erstellen."
tool: Segments
search_rank: 3
---

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/segmentation-course){: style="float:right;width:120px;border:0;" class="noimgborder"} Segmentierung erstellen

> Die Segmentierung ermöglicht es Ihnen, Benutzer auf der Grundlage ihrer demografischen, verhaltensbezogenen oder technischen Merkmale und Aktionen anzusprechen. Durch den kreativen und intelligenten Einsatz von Segmentierung und Nachrichtenautomatisierung können Sie Ihre Nutzer nahtlos vom Erstkontakt zum langfristigen Kunden machen. Segmente werden in Echtzeit aktualisiert, wenn sich Daten ändern. Sie können so viele Segmente erstellen, wie Sie für Ihre Targeting- und Messaging-Zwecke benötigen.

## Schritt 1: Zum Abschnitt „Segmente“ navigieren

Gehen Sie zu **Zielgruppe** > **Segmente**.

## Schritt 2: Benennen Sie Ihr Segment

Wählen Sie **Segment erstellen**, um mit der Erstellung Ihres Segments zu beginnen. Benennen Sie Ihr Segment, indem Sie den Nutzertyp beschreiben, nach dem Sie filtern möchten. Dies hilft Ihnen, das Segment zu identifizieren, wenn Sie es für Ihre Kampagnen oder Canvase auswählen möchten. Ungenaue Segmenttitel können verwirrend sein.

Optional können Sie auch Folgendes tun:
- Fügen Sie dem Segment eine Beschreibung hinzu, um mehr Details über die Absicht dieses Publikums zu liefern, und hinterlassen Sie Notizen, auf die andere Teammitglieder zurückgreifen können.
- Fügen Sie ein [Team]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) zu Ihrem Segment hinzu.
- Fügen Sie Ihrem Segment zur weiteren Organisation [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu.

![Modal zum Erstellen von Segmenten, in dem das Segment den Namen "Verfallene Nutzer:innen" trägt, mit der Segmentbeschreibung "Dies ist unser Hauptsegment für verfallene Nutzer:innen, um Nicht-Aktive innerhalb der letzten vierzehn Tage zu targetieren." und zwei Buttons: „Abbrechen“ und „Segment erstellen“.]({% image_buster /assets/img_archive/segment_app_selection.png %}){: style="max-width:80%;"}

## Schritt 3: Wählen Sie Ihre App oder Plattform

Wählen Sie, welche Apps oder Plattformen Sie anvisieren möchten, indem Sie **Benutzer aus allen Apps** (Standard) oder **Benutzer aus bestimmten Apps** auswählen. **Benutzer aus bestimmten Apps** stellt Nutzer:innen mit mindestens einer Sitzung in den angegebenen Apps zusammen.

Wenn Sie zum Beispiel eine In-App-Nachricht nur an iOS-Geräte senden möchten, wählen Sie Ihre iOS-App aus. So wird sichergestellt, dass Benutzer, die sowohl ein iOS- als auch ein Android-Gerät verwenden, die Nachricht nur auf ihrem iOS-Gerät erhalten. In der Liste der spezifischen Apps können Sie mit der Option **Nutzer:innen ohne** Sitzungen und ohne App-Daten (die in der Regel durch Nutzerimport oder REST API erstellt wurden) aufnehmen.

![Segment Details Panel mit der ausgewählten Option "Nutzer:innen aus allen Apps" im Abschnitt Verwendete Apps.]({% image_buster /assets/img_archive/Segment2.png %}){: style="max-width:80%;"}

## Schritt 4: Filter zu Ihrem Segment hinzufügen

Fügen Sie mindestens einen Filter zu Ihrem Segment hinzu. Sie können so viele Filter kombinieren, wie Sie möchten, um Ihre Segmentierung zu präzisieren. 

{% alert note %}
Braze erstellt erst dann Profile für Benutzer, wenn diese die App zum ersten Mal verwendet haben. Sie können also keine Benutzer ansprechen, die Ihre App noch nicht geöffnet haben.
{% endalert %}

#### Gruppen filtern

Filter sind in Filtergruppen organisiert. Jeder Filter muss Teil einer Filtergruppe sein, die aus mindestens einem Filter besteht. Ein Segment kann mehrere Filtergruppen haben. Um eine hinzuzufügen, wählen Sie **Filtergruppe hinzufügen**. Bearbeiten Sie den Namen der Filtergruppe, indem Sie auf das Symbol klicken, das erscheint, wenn Sie den Mauszeiger daneben halten.

![Filtergruppe mit einem Bearbeitungssymbol neben ihrem Namen.]({% image_buster /assets/img_archive/edit_filter_group_name.png %})

Wählen Sie die Symbole neben den einzelnen Filtern aus, um den Filter-Editor auszublenden oder einzelne Filter zu duplizieren. Nachdem Sie einen Filter dupliziert haben, können Sie seine Werte in jedem Dropdown-Menü anpassen.

#### Segmentierungslogik mit AND und OR

Innerhalb einer Filtergruppe können Filter entweder mit "UND" oder "ODER" verknüpft werden. Zwischen Filtergruppen können Gruppen entweder durch "UND" oder "ODER" verbunden werden. Wenn Sie Filtergruppen verwenden, können Sie eine Segmentierungslogik erstellen. Beispiel:
- (A UND B UND C) ODER (C UND E UND F)
- (A ODER B ODER C) UND (C ODER D ODER F)

Wenn Sie "ODER" für Ihre Filter auswählen, bedeutet dies, dass Ihr Segment Nutzer enthält, die eine beliebige Kombination aus einem, einigen oder allen dieser Filter erfüllen. Wenn Sie „UND“ auswählen, werden Nutzer:innen, die diesen Filter nicht bestehen, nicht in Ihr Segment aufgenommen.

{% alert tip %}
Wenn Sie „ODER“ für Filter auswählen, die einen negativen Filter enthalten (z. B. „ist nicht“ in einer Abonnementgruppe), denken Sie daran, dass Nutzer:innen nur einen der „ODER“-Filter erfüllen müssen, um in das Segment aufgenommen zu werden. Um den Negativfilter unabhängig von den anderen Filtern anzuwenden, verwenden Sie eine [Ausschlussgruppe](#exclusion).
{% endalert %}

{% details When to avoid the OR operator %}

Es kann Situationen des Nutzer:in Targeting geben, in denen die Verwendung des Operators `OR` vermieden werden sollte. Der `OR` Operator erstellt eine Aussage, die als wahr ausgewertet wird, wenn ein Nutzer:innen die Kriterien für einen oder mehrere der Filter in einer Aussage erfüllt. Wenn Sie zum Beispiel ein Segment von Nutzern:in erstellen möchten, die zu den "Foodies" gehören, aber weder zu den "Non-Foodies" noch zu den "Candy-lovers", dann können Sie den `OR` Operator verwenden.

![Filtergruppe für Nutzer:innen im Segment "Feinschmecker" und nicht in den Segmenten "Nicht-Feinschmecker" oder "Süßigkeiten-Liebhaber".]({% image_buster /assets/img_archive/or_operator_segment.png %})

Wenn Sie jedoch Nutzer:in segmentieren möchten, die zum Segment "Feinschmecker" gehören und nicht zu den Segmenten "Nicht-Feinschmecker" und "Süßigkeiten-Liebhaber" gehören, dann verwenden Sie den Operator `AND`. Auf diese Weise befinden sich Nutzer:innen, die die Kampagne oder das Canvas erhalten, in dem beabsichtigten Segment ("Foodies") und nicht gleichzeitig in den anderen Segmenten ("Nicht-Foodies" und "Candy-lovers"). 

Die folgenden negativen Targeting-Kriterien sollten nicht mit dem Operator `OR` verwendet werden, wenn zwei oder mehr Filter auf dasselbe Attribut verweisen:

- `not included`
- `is not`
- `does not equal`
- `does not match regex`

Wenn `not included`, `is not`, `does not equal` oder `does not match regex` zusammen mit dem Operator `OR` zwei- oder mehrmals in einer Anweisung verwendet werden, werden Nutzer:innen mit allen Werten für das entsprechende Attribut gezielt angesprochen.

{% enddetails %}

#### Filteroperatoren

Je nach dem von Ihnen gewählten Filter stehen Ihnen verschiedene Operatoren zur Identifizierung von Filterwerten zur Verfügung. Wenn Sie mehr über die Operatoren erfahren möchten, die für die verschiedenen Arten von benutzerdefinierten Attributen verfügbar sind, lesen Sie den Abschnitt [Speicherung von benutzerdefinierten Attributen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#setting-custom-attributes). Beachten Sie, dass Sie bei Verwendung des Operators „ist irgendein von“ maximal 256 Elemente in dieses Feld aufnehmen können.

{% alert note %}
Braze erstellt erst dann Profile für Benutzer, wenn diese die App zum ersten Mal verwendet haben. Sie können also keine Benutzer ansprechen, die Ihre App noch nicht geöffnet haben.
{% endalert %}

![Segmente filtern Gruppen mit dem Operator AND.]({% image_buster /assets/img_archive/segmenter_filter_groups.png %})

{% alert important %}
Segmente, die bereits den Filter **Segmentzugehörigkeit** verwenden, können nicht weiter einbezogen oder in andere Segmente verschachtelt werden. Dadurch wird ein Zyklus verhindert, bei dem Segment A Segment B einschließt, das dann wiederum versucht, Segment A einzuschließen. In diesem Fall würde das Segment immer wieder auf sich selbst verweisen, so dass es unmöglich wäre, zu berechnen, wer tatsächlich dazugehört.

Außerdem wird die Verschachtelung von Segmenten auf diese Weise komplizierter und kann die Arbeit verlangsamen. Erstellen Sie stattdessen das Segment, das Sie einbeziehen möchten, mit denselben Filtern neu.
{% endalert %}

#### Ausschlussgruppen (optional) {#exclusion}

Wenn Sie ein Segment erstellen, können Sie eine oder mehrere Ausschlussgruppen anwenden. Ausschlussgruppen enthalten Kriterien, die Benutzer identifizieren, die von Ihrem Segment ausgeschlossen werden sollen, und werden immer mit einem "AND NOT"-Operator mit Ihren Filtergruppen verbunden.

Ausschlussgruppen haben Vorrang vor Segmentkriterien. Wenn ein Benutzer unter die Kriterien Ihrer Ausschlussgruppen fällt, gehört er nicht zu Ihrem Segment, selbst wenn er die Kriterien Ihrer Filtergruppen erfüllt.

Erstellen Sie eine Ausschlussgruppe, indem Sie Filter hinzufügen, wie Sie es bei Filtergruppen tun würden. Die Statistik _Geschätzte erreichbare Nutzer_ in einer Ausschlussgruppe zeigt die geschätzte Anzahl der Nutzer, die nach Anwendung der Ausschlusskriterien in Ihrem Segment verbleiben.

Ausgeschlossene Benutzer werden nicht als Teil der Statistik der _insgesamt erreichbaren Benutzer_ Ihres Segments gezählt.

![Eine Ausschlussgruppe mit zwei Filtern.]({% image_buster /assets/img_archive/segmenter_exclusion_groups.png %})

#### Anzeigen der Funnel-Statistiken

Wählen Sie **Trichterstatistiken anzeigen** aus, um die Statistiken für diese Filtergruppe anzuzeigen und zu sehen, wie sich jeder hinzugefügte Filter auf Ihre Segmentierungsstatistiken auswirkt. Sie sehen die geschätzte Anzahl und den Prozentsatz der Nutzer:innen, die bis zu diesem Zeitpunkt von allen Filtern targetiert wurden. Sobald die Statistiken für eine Filtergruppe angezeigt werden, werden sie automatisch aktualisiert, sobald Sie die Filter ändern. Diese Statistiken sind geschätzt und es kann einen Moment dauern, bis sie erstellt sind.

Beachten Sie, dass die Funnel-Statistiken sinken, wenn Sie AND zwischen Ihren Filtern verwenden. Wenn Sie OR zwischen Ihren Filtern verwenden, steigen die Funnel-Statistiken.

![Zwei Filter mit Segment Funnel Statistiken.]({% image_buster /assets/img_archive/segment_funnel_statistics.png %})

Durch das Hinzufügen von Filtern, die Ihren Nutzerfluss dokumentieren, können Sie die Punkte erkennen, an denen Nutzer:innen abspringen. Wenn Sie zum Beispiel eine App für soziale Netzwerke betreiben und sehen möchten, wo Sie während des Onboarding-Prozesses Nutzer:innen verlieren, können Sie angepasste Datenfilter für die Registrierung, das Hinzufügen von Freunden und das Senden der ersten Nachricht hinzufügen. Wenn Sie feststellen, dass 85 % der Nutzer:innen sich registrieren und Freunde hinzufügen, aber nur 45 % die erste Nachricht gesendet haben, dann wissen Sie, dass Sie sich darauf konzentrieren sollten, mehr Nachrichten während Ihrer Onboarding- und Marketing-Kampagnen zu senden.

#### Segmente testen

Nachdem Sie Ihrem Segment Apps und Filter hinzugefügt haben, können Sie testen, ob Ihr Segment wie erwartet eingerichtet ist, indem Sie nach einem Benutzer suchen, um zu überprüfen, ob er den Segmentkriterien entspricht. Suchen Sie dazu in der **Benutzersuche** nach dem Namen eines Benutzers `external_id` oder `braze_id`. Beachten Sie, dass Sie in der **Benutzer:innen-Suche** nicht nach E-Mail-Adressen suchen können.

![Abschnitt Nutzer:in mit einem Suchfeld.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%;"}

Die Benutzersuche ist verfügbar, wenn:
- Ein Segment erstellen
- Einrichten einer Kampagne oder einer Canvas-Zielgruppe
- Einrichten eines Audience Paths-Schrittes

Wenn ein:e Nutzer:in den Segment-, Filter- und App-Kriterien entspricht, wird dies in einer Benachrichtigung angezeigt.

![Eine Nutzer:in-Suche nach "testuser" triggert einen Alarm mit der Meldung "testuser stimmt mit allen Segmenten, Filtern und Apps überein.]({% image_buster /assets/img_archive/user_lookup_match.png %})

Wenn ein Benutzer die Segment-, Filter- oder App-Kriterien ganz oder teilweise nicht erfüllt, werden die fehlenden Kriterien zur Fehlerbehebung aufgelistet.

![Eine Nutzer:innen-Suche mit der Meldung "test1 stimmt nicht mit den folgenden Targeting-Kriterien überein:" und zeigt fehlende Kriterien an.]({% image_buster /assets/img_archive/user_lookup_nomatch.png %})

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

!["Zusätzliche Einstellungen" mit einem Kontrollkästchen, um nur an das zuletzt benutzte Gerät des Nutzer:innen zu senden.]({% image_buster /assets/img_archive/send_to_last_device.png %}){: style="max-width:60%;"}

### Überlegungen

- **Gesendete Nachrichten können die Größe der Zielgruppe übersteigen.** Wenn einige Nutzer:innen mehr als ein Gerät haben, kann jedes Gerät eine Nachricht erhalten. Dies führt zu einer höheren Anzahl von gesendeten Nachrichten als die Nutzer in Ihrem Segment.
- **Die Segmentzugehörigkeit eines Nutzers oder einer Nutzer:in sieht vielleicht nicht so aus, wie Sie es erwarten würden.**
    - Ein Benutzer kann auf seinem aktuellen Gerät anhand von Attributen angesprochen werden, die mit einem anderen Gerät verbunden sind. Wenn Sie nicht erwartet haben, dass ein:e Nutzer:in eine Nachricht erhält, überprüfen Sie das entsprechende Nutzerprofil auf mehrere Geräte.
    - Es kann sein, dass ein Nutzer zum Zeitpunkt des Versands zu Ihrem Zielsegment gehörte, aber aufgrund des Verhaltens, das mit einem seiner Geräte verbunden ist, danach nicht mehr zu diesem Segment gehört. Dies kann dazu führen, dass ein Benutzer eine Kampagne oder ein Canvas erhält, obwohl er die Filterkriterien derzeit nicht erfüllt. <br><br>Zum Beispiel könnte ein:e Nutzer:in eine Nachricht erhalten, die sich an Nutzer:innen mit einer aktuellen App-Version von OS 10.0 richtet, obwohl er oder sie derzeit OS 13.0 hat. In diesem Fall hatte der oder die Nutzer:in OS 10.0, als die Nachricht gesendet wurde, und aktualisierte danach auf OS 13.0.<br><br> Wenn ein Benutzer zu einem späteren Zeitpunkt ein Gerät mit einer anderen App-Version verwendet, wird sein Benutzerprofil mit der neuen, neuesten App-Version aktualisiert. Dies könnte den Anschein erwecken, dass der oder die Nutzer:in sich nicht für die Nachricht qualifiziert haben sollte, obwohl er oder sie sich qualifiziert hat, als die Nachricht gesendet wurde.


