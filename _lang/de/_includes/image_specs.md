{% if include.variable_name == "image behavior" %}


| Layout | Verhalten |
| --- | --- |
| Bild und Text | Hohe oder schmale Bilder werden verkleinert und horizontal zentriert. Breite Bilder werden am linken und rechten Rand abgeschnitten. |
| Nur Bild | Die Nachricht passt sich an die meisten Bildformate an. |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "payload size" %}

Wir empfehlen die folgenden Nutzlastgrößen:

| Nachrichtensystem | Empfohlene Nutzlast |
| --- | --- |
| iOS (vor iOS 8) | 0.256 KB |
| iOS (post-iOS 8) | 2 KB |
| Android (FCM) | 4 KB |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "in-app messages" %}

Modale In-App-Nachrichten sind so konzipiert, dass sie sich bestmöglich und mit dem höchsten Füllgrad an das Gerät anpassen, während sie gleichzeitig die Größe und das Verhältnis des von Ihnen ausgewählten Bildes oder Textes für Ihre Nachricht beibehalten.

Es gibt zwar keine Beschränkungen für die Anzahl der Textzeichen, die Sie in einer In-App-Nachricht (sowie in Buttons, in der Überschrift, im Hauptteil und in anderen Teilen) verwenden können, aber wir begrenzen die Anzahl der Textzeichen, die Sie verwenden. Zu viel Text führt dazu, dass die Nutzer die Nachricht erweitern und scrollen müssen.

Alle In-App-Nachrichten haben eine empfohlene Bildgröße von 500 KB, eine maximale Bildgröße von 5 MB und unterstützen die Dateitypen PNG, JPEG und GIF.

{% tabs %}
{% tab Porträt %}

| Typ | Seitenverhältnis | Bildqualität | Anmerkungen |
| --- | --- | --- | --- |
| Hochformat Vollbild mit Text | 6:5 | Hohe Auflösung 1200 x 1000 px <br>Mindestauflösung 600 x 500 px | Der Beschnitt kann an allen Seiten erfolgen, aber das Bild füllt immer die oberen 50 % des Ansichtsfensters aus. |
| Hochformat-Vollbild (nur Bild, mit oder ohne Schaltflächen) | 3:5 | Hohe Auflösung 1200 x 2000 px <br> Mindestauflösung 600 x 1000 px | Bei größeren Geräten kann es am linken und rechten Rand zu Beschneidungen kommen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Landschaft %}

| Typ | Seitenverhältnis | Bildqualität | Anmerkungen |
| --- | --- | --- | --- |
| Vollbild im Querformat mit Text | 10:3 | Hohe Auflösung 2000 x 600 px <br>Mindestauflösung 1000 x 300 px | Der Beschnitt kann an allen Seiten erfolgen, aber das Bild füllt immer die oberen 50 % des Ansichtsfensters aus. |
| Vollbild im Querformat (nur Bild, mit oder ohne Schaltflächen) | 5:3 | Hohe Auflösung 2000 x 600 px <br> Mindestauflösung 1000 x 600 px | Bei größeren Geräten kann es am linken und rechten Rand zu Beschneidungen kommen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Slideup %}

| Typ | Seitenverhältnis | Bildqualität | Anmerkungen |
| --- | --- | --- | --- |
| Slideup | 1:1 | Hohe Auflösung 150 x 150 px <br> Mindestauflösung 50 x 50 px | Bilder mit unterschiedlichen Seitenverhältnissen passen in einen quadratischen Bildcontainer, ohne dass sie beschnitten werden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Modal %}

| Typ | Seitenverhältnis | Bildqualität | Anmerkungen |
| --- | --- | --- | --- |
| Modal (nur Bild) | 1:1 | Hohe Auflösung 1200 x 2000 px <br> Mindestauflösung 600 x 600 px | Die Nachricht passt sich an die meisten Bildformate an. |
| Modal mit Text | 29:10 | Hohe Auflösung 1450 x 500 px <br> Mindestauflösung 600 x 205 px | Große Bilder werden verkleinert und horizontal zentriert. Breite Bilder werden am linken und rechten Rand abgeschnitten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% endtabs %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| Nachrichtentyp | Maximale Nachrichtenlänge | Maximale Titellänge |
| --- | --- | --- |
| iOS Sperrbildschirm | 175 Zeichen | 43 Zeichen |
| iOS-Benachrichtigung | 175 Zeichen | 43 Zeichen |
| iOS-Banneralarm | 85 Zeichen | 43 Zeichen |
| Android Sperrbildschirm | 49 Zeichen | 43 Zeichen |
| Android Benachrichtigungsschublade | 597 Zeichen | 43 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Die empfohlene Bildgröße für alle Push-Bilder beträgt 500 KB.

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Bildtyp</th>
      <th>Seitenverhältnis</th>
      <th>Maximale Pixel</th>
      <th>Maximale Bildgröße</th>
      <th>Dateitypen</th>
      <th>Anmerkungen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS</td>
      <td>2:1 (empfohlen)</td>
      <td>1038 x 1038</td>
      <td>5 MB</td>
      <td>PNG, JPEG, GIF</td>
      <td>Ab Januar 2020 können iOS Rich-Push-Benachrichtigungen Bilder mit einer Größe von 1038 x 1038 px verarbeiten, solange sie unter 10 MB liegen. Wir empfehlen jedoch, eine möglichst kleine Dateigröße zu verwenden. In der Praxis kann das Versenden großer Dateien sowohl unnötigen Stress für das Netzwerk verursachen als auch dazu führen, dass es häufiger zu Timeouts beim Herunterladen kommt.<br><br>Weitere Informationen finden Sie unter <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">iOS Rich Notifications</a>.</td>
    </tr>
    <tr>
      <td>Android Push-Symbol</td>
      <td>1:1</td>
      <td>--</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td></td>
    </tr>
    <tr>
      <td>Android erweitertes Benachrichtigungsbild</td>
      <td>2:1</td>
      <td><b>Klein:</b><br>512 x 256<br><br><b>Medium:</b><br>1024 x 512<br><br><b>Groß:</b><br>2048 x 1024</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td>Wird in <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">Android Rich Notifications</a> verwendet.</td>
    </tr>
    <tr>
      <td>Android Neigungsbild</td>
      <td>3:2</td>
      <td>--</td>
      <td>--</td>
      <td>PNG, JPEG</td>
      <td>Weitere Einzelheiten finden Sie unter <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">Android-Inline-Image-Push</a>.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4  .reset-td-br-5 .reset-td-br-6 role="presentation"}

{% endif %}

{% if include.variable_name == "email" %}

| E-Mail-Typ | Empfohlene maximale Eigenschaften |
| --- | --- | 
| Nur Text | 25 KB |
| Text mit Bildern | 60 KB |
| E-Mail Breite | 600 px |
{: .reset-td-br-1 .reset-td-br-2}

| Bild-Spezifikationen | Empfohlene maximale Eigenschaften |
| --- | --- | 
| Größe | 5 MB |
| Breite | Überschrift: 600 px<br>Text: 480 px |
| Dateitypen | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2}

| Text Spezifikationen | Empfohlene maximale Eigenschaften |
| --- | --- | 
| Länge der Betreffzeile | 35 Zeichen<br>6 bis 10 Wörter |
| `"From: Name"` Länge | 25 Zeichen |
| Länge der Vorkopfzeile | 85 Zeichen |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "content cards" %}

| Kartentyp | Seitenverhältnis     | Bildqualität       |
| --------- | ---------------- | ------------------- |
| Klassisch   | Seitenverhältnis 1:1 | 60 x 60 px        |
| Untertitel | Seitenverhältnis 4:3 | 600 px Mindestbreite |
| Banner    | Jedes Seitenverhältnis | 600 px Mindestbreite |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Weitere Informationen finden Sie unter [Kreative Details der Inhaltskarte]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/).

{% endif %}