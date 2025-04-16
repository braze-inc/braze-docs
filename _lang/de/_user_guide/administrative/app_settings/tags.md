---
nav_title: Tags
article_title: Tags
page_order: 12
page_type: reference
description: "Dieser Referenzartikel behandelt Tags im Braze-Dashboard, mit denen Sie Ihr Engagement weiter organisieren und sortieren können."

---
# Tags

> Braze verfolgt Autor-, Bearbeiter-, Datums- und Statusinformationen zu Segmenten, Kampagnen und Canvase und gibt Ihnen die Möglichkeit, Tags zu erstellen, um Ihr Engagement weiter zu organisieren und zu sortieren.

## Kampagnen-, Canvas- und Segment-Tags

Sie können bei der Erstellung oder Bearbeitung einer Kampagne, eines Canvas oder eines Segments Tags hinzufügen. Klicken Sie auf <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tags** unter dem Namen des Engagements und wählen Sie ein vorhandenes Tag aus, oder beginnen Sie mit der Eingabe, um ein neues Tag hinzuzufügen.

![Hinzufügen von Tags bei der Kampagnenerstellung][2]

Sie können auch Tags zu mehreren Kampagnen, Canvases oder Segmenten hinzufügen, indem Sie mehrere Engagements auswählen und auf <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag As** klicken.

![Hinzufügen von Tags zu mehreren Kampagnen zur gleichen Zeit][5]

Die für eine Kampagne, ein Canvas oder ein Segment festgelegten Tags sind auf der Detailseite neben dem Namen des Engagements sichtbar.

![Tags, die auf der Seite Kampagnendetails angezeigt werden][3]

Sie sind auch in der Liste der Kampagnen, Canvases oder Segmente sichtbar, zusammen mit zusätzlichen Tags für Statuskennzeichnungen wie **Archiviert** und **Entwurf**.

![Tags auf der Liste der Kampagnen][4]{: style ="max-width:70%;" }

Um nach einem Tag zu filtern, wählen Sie den Tagnamen aus der Liste der Tags aus oder suchen Sie den Tag im Suchbereich mit dem Selektor `tag:`. Um zum Beispiel nach dem Tag `Onboarding` zu suchen, geben Sie "tag:Onboarding" ein.

![Suche nach allen Kampagnen, die als Willkommens-E-Mail getaggt sind][6]

{% alert important %}
Sie können bis zu 175 Tags zu einer Kampagne, einem Canvas oder einem Segment hinzufügen.
{% endalert %}

## Angepasste Daten Tags

Bei der Verwaltung von benutzerdefinierten [Attributen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) und [Ereignissen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#managing-custom-events) können auch Tags zu benutzerdefinierten Daten hinzugefügt werden. 

{% alert important %}
Dieses Feature befindet sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Customer Success Manager, wenn Sie an einem Vorabzugang interessiert sind.
{% endalert %}

## Bewährte Praktiken {#tags-best-practices}

Tags können ein nützliches Organisations-Tool für das Tracking von Engagement-Taktiken sein. Sie können Segmente und Kampagnen mit Geschäftszielen, Funnel-Stufen und dergleichen verknüpfen.

Im Folgenden finden Sie ein Beispiel für Tags, die für eine E-Commerce App nützlich sein könnten:

<style>
table td {
    word-break: break-word;
}
</style>


<table>
<thead>
  <tr>
    <th>Funnel</th>
    <th>Geschäftsziele</th>
    <th>Regional</th>
    <th>Kampagnen</th>
    <th>Feiertage</th>
    <th>Transaktionen</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Onboarding<br>Erneute Interaktion<br>Loyal<br>PowerUser<br>Abwanderung<br>Verloren</td>
    <td>HighSpender<br>ActiveUser<br>NewUsers<br>FacebookAttribution<br>FirstAction</td>
    <td>UnitedStates<br>Nordost<br>Mittlerer Westen<br>Süd<br>West<br>LATAM<br>AP<br>West-Europa<br>Naher Osten</td>
    <td>Verkauf<br>Gutscheine<br>Events</td>
    <td>MLK<br>SuperBowl<br>PiDay<br>StPatricksDay<br>MarchMadness<br>Ostern<br>Pessach<br>Muttertag<br>MemorialDay<br>Vatertag<br>FourthJuly<br>LaborDay<br>VeteranenTag<br>ColumbusDay<br>PresidentsDay<br>Halloween<br>RoshHashanah<br>Erntedankfest<br>Weihnachten<br>Chanukka<br>NewYears</td>
    <td>Transaktion<br>Benachrichtigung<br>ConnectedActionTaken</td>
  </tr>
</tbody>
</table>

Sie können dieselben Tags für Kampagnen, Canvases und Segmente verwenden. Um Tags in Ihrem Dashboard effizient umzubenennen, zu entfernen oder hinzuzufügen, gehen Sie zu **Einstellungen** > **Tag Management**.

![Tab Tags auf der Seite Einstellungen verwalten][8]

Um Ihre Tags noch besser zu organisieren, verschachteln Sie Ihre Tags unter einem übergeordneten Tag. Sie können z.B. alle Feiertags-Tags unter einem übergeordneten Tag `Holidays` oder alle Tags, die sich auf eine Phase Ihres Marketing-Trichters beziehen, unter einem übergeordneten Tag `Funnel` unterbringen. 

Erstellen Sie dazu ein neues Tag, wählen Sie **Tag verschachteln unter** und wählen Sie aus, unter welchem bestehenden Tag Sie Ihr neues Tag verschachteln möchten. Sie können bestehende Tags auch auf der Seite **Tag Management** verschachteln. Bewegen Sie auf dieser Seite den Mauszeiger über eine Zeile mit Ihrem Tag und klicken Sie auf **<i class="fas fa-pencil-alt"></i>Bearbeiten**. Befolgen Sie dann die gleichen Schritte wie zuvor.

![Einen verschachtelten Tag erstellen][1]{: style ="max-width:70%;" }

## Anwendungsfälle

Suchen Sie nach Inspirationen, wie Sie Tags nutzen können, um Ihren Messaging-Lebenszyklus zu verwalten? Hier sind einige häufige Anwendungsfälle:

### Drosselung

Begrenzen Sie, wie oft Ihre Kunden Kampagnen eines bestimmten Typs erhalten. Sie könnten zum Beispiel die folgenden Filter setzen, um die Häufigkeit von Werbekampagnen zu begrenzen:

`Last received campaign` mit Tag `Promo` vor mehr als 5 Tagen
<br>`OR`<br>
`Has not received campaign` mit Tag `Promo`

### Berichterstattung

Richten Sie einen Engagement-Bericht ein, um das Volumen aller Kampagnen mit einem bestimmten Tag im Auge zu behalten. Wenn Sie beispielsweise alle Ihre Push-Kampagnen überwachen möchten, können Sie diesen Kampagnen ein Tag wie `Push Reporting` hinzufügen und dann einen [Engagement-Bericht]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#automatically-select-campaigns-or-canvases) einrichten, der Ihnen jeden Tag einen Bericht über diese getaggten Kampagnen sendet.



[1]: {% image_buster /assets/img_archive/tag_nested.png %}
[2]: {% image_buster /assets/img_archive/tags_add_tag.png %}
[3]: {% image_buster /assets/img_archive/tag_details_page.png %}
[4]: {% image_buster /assets/img_archive/tags_grid.png %}
[5]: {% image_buster /assets/img_archive/tags_apply_multiple.png %}
[6]: {% image_buster /assets/img_archive/tags_filtering.png %}
[7]: {% image_buster /assets/img_archive/Tags-Potential_Tags.png %}
[8]: {% image_buster /assets/img_archive/tags_view.png %}
