---
nav_title: Navigations-Deeplinks
article_title: Navigations-Deeplinks in Braze Pilot
page_order: 4
page_type: reference
description: "Dieser Artikel beschreibt die erforderlichen Integrationsschritte für Ihre Entwicklerabteilung."
---

# Navigations-Deeplinks in Braze Pilot

> Braze Pilot unterstützt Deeplinking von Braze-Nachrichten zu bestimmten Bereichen der Pilot-App. Dies ermöglicht es Ihnen, Anwendungsfälle für das Engagement zu erstellen und die Nutzer:innen zu verschiedenen Teilen der Pilot-Anwendung zu leiten. Sie können auch optionale Deeplink-Parameter verwenden, um den Inhalt bestimmter Seiten in der App für die Nutzer:innen anzupassen. Weitere Informationen zum Deeplinking finden Sie unter [Deeplinking zu In-App-Inhalten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

## Allgemein

Dies sind die Deeplinks für die Hauptnavigationsseiten in der Pilot-App. 

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Projekte | `braze-pilot://navigation/projects` |
| Protokoll-Daten | `braze-pilot://navigation/logdata` |
| Einrichtung | `braze-pilot://navigation/setup` |
| Sprache ändern | `braze-pilot://navigation/selectlanguage` |
| Kamera | `braze-pilot://navigation/camera` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Steppington

Dies sind die Deeplinks für die App der fiktiven Marke Steppington in Pilot.

### Beispiel für einen Deeplink

`braze-pilot://navigation/steppington/workout?title=Running&icon=HEART_DETAILS&image=https://picsum.photos/400&info=This%20workout%20is%20awesome%21&workout=5k%20Run&calories=600&length=25&workout_info_left_text=Road%20Run&workout_info_left_icon=RUNNING_HOME&workout_info_center_text=120%20BPM&workout_info_center_icon=HEART_DETAILS&workout_info_right_text=25%3A00&workout_info_right_icon=TIMER_DETAILS`

### Deeplinks ohne Parameter

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Begrüßungsbildschirm | `braze-pilot://navigation/steppington/splash` |
| Home | `braze-pilot://navigation/steppington/home` |
| Steppington+-Seite | `braze-pilot://navigation/steppington/plus` |
| Zielbildschirm | `braze-pilot://navigation/steppington/goals` |
| Zielbildschirm ändern | `braze-pilot://navigation/steppington/changegoals` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Deeplinks mit Parametern

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Training | `braze-pilot://navigation/steppington/workout` |
| Aktives Training | `braze-pilot://navigation/steppington/activeworkout` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Akzeptierte Parameter

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 22%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Beschreibung</th>
            <th>Erforderlich</th>
            <th>Standard (sofern nicht anders angegeben)</th>
            <th>Typ</th>
            <th>Beispiel</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>title</code></td>
            <td>Der Titel, der oben auf dem Bildschirm angezeigt werden soll.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>Läuft …</td>
        </tr>
        <tr>
            <td><code>icon</code></td>
            <td>Eine String-Zeichenfolge, die angibt, welches Symbol verwendet werden soll.</td>
            <td>Kein:e</td>
            <td><code>RUNNING_HOME</code></td>
            <td>String</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>Die URL des Bildes des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>info</code></td>
            <td>Informationen zum Training, die über dem Button für das Training platziert werden sollen.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>Dieses Training ist hervorragend.</td>
        </tr>
        <tr>
            <td><code>workout</code></td>
            <td>Der Name des Trainingsprogramms. Gesendet am <code>st_completed_class</code> Veranstaltung.</td>
            <td>Ja</td>
            <td></td>
            <td>Zahl</td>
            <td>5k-Lauf</td>
        </tr>
        <tr>
            <td><code>calories</code></td>
            <td>Die Anzahl der Kalorien, die auf dem aktiven Trainingsbildschirm angezeigt werden sollen. Gesendet am <code>st_completed_class</code> Veranstaltung.</td>
            <td>Kein:e</td>
            <td>Zufallszahl zwischen 500 und 1.250</td>
            <td>Zahl</td>
            <td>sechshundert</td>
        </tr>
        <tr>
            <td><code>length</code></td>
            <td>Die Dauer des Trainings. Gesendet am <code>st_completed_class</code> Veranstaltung.</td>
            <td>Kein:e</td>
            <td></td>
            <td>Zahl</td>
            <td>25</td>
        </tr>
        <tr>
            <td><code>workout_info_left_text</code></td>
            <td>Der Text, der auf der linken Karte auf dem aktiven Trainingsbildschirm verwendet werden soll.</td>
            <td>Kein:e</td>
            <td></td>
            <td>String</td>
            <td>Straßenlauf</td>
        </tr>
        <tr>
            <td><code>workout_info_left_icon</code></td>
            <td>Das Symbol, das auf der linken Karte auf dem aktiven Trainingsbildschirm verwendet werden soll.</td>
            <td>Kein:e</td>
            <td></td>
            <td>String</td>
            <td>RUNNING_HOME</td>
        </tr>
        <tr>
            <td><code>workout_info_center_text</code></td>
            <td>Der Text, der in der mittleren Karte auf dem aktiven Trainingsbildschirm verwendet werden soll.</td>
            <td>Kein:e</td>
            <td></td>
            <td>String</td>
            <td>120 % BPM</td>
        </tr>
        <tr>
            <td><code>workout_info_center_icon</code></td>
            <td>Das Symbol, das in der mittleren Karte auf dem aktiven Trainingsbildschirm verwendet werden soll.</td>
            <td>Kein:e</td>
            <td></td>
            <td>String</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>workout_info_right_text</code></td>
            <td>Der Text, der auf der rechten Karte auf dem aktiven Trainingsbildschirm verwendet werden soll.</td>
            <td>Kein:e</td>
            <td></td>
            <td>String</td>
            <td>25 %:00</td>
        </tr>
        <tr>
            <td><code>workout_info_right_icon</code></td>
            <td>Das Symbol, das in der rechten Karte auf dem aktiven Trainingsbildschirm verwendet werden soll.</td>
            <td>Kein:e</td>
            <td></td>
            <td>String</td>
            <td>TIMER_DETAILS</td>
        </tr>
    </tbody>
</table>

##### Symboloptionen

| Symbol | Bild |
| --- | --- |
| `RUNNING_HOME` | ![Eine Ikone unter den Laufschuhen.]({% image_buster /assets/img/braze_pilot/running_home_icon.png %}){:style="max-width:30%"} |
| `HEART_DETAILS` | ![Ein Herz-Symbol.]({% image_buster /assets/img/braze_pilot/heart_details_icon.png %}){:style="max-width:30%"} |
| `TIMER_DETAILS` | ![Ein Stoppuhr-Symbol.]({% image_buster /assets/img/braze_pilot/timer_details_icon.png %}){:style="max-width:30%"} |
| `YOGA_HOME` | ![Ein Symbol für eine Person in einer Yoga-Pose.]({% image_buster /assets/img/braze_pilot/yoga_home_icon.png %}){:style="max-width:30%"} |
| `BICYCLE_HOME` | ![Eine Ikone des Radsports.]({% image_buster /assets/img/braze_pilot/bicycle_home_icon.png %}){:style="max-width:30%"} |
| `DUMBBELL_HOME` | ![Ein Hantel-Symbol.]({% image_buster /assets/img/braze_pilot/dumbbell_home_icon.png %}){:style="max-width:30%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Hosenlabyrinth

Dies sind die Deeplinks für die fiktive Marken-App „PantsLabyrinth“ in Pilot.

### Beispiel für einen Deeplink

`braze-pilot://navigation/pantslabyrinth/itemdetails?name=Jeans&price=85&image=https://picsum.photos/400&description=This%20item%20is%20awesome%21&quantity=2&size=Large&colors=%230000FF,%23FF0000&color_strings=White,Blue&selected_color=1`

### Deeplinks ohne Parameter

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Begrüßungsbildschirm | `braze-pilot://navigation/pantslabyrinth/splash` |
| Begrüßungsbildschirm | `braze-pilot://navigation/pantslabyrinth/welcome` |
| Anzeige-Bildschirm | `braze-pilot://navigation/pantslabyrinth/listing` |
| Warenkorbseite | `braze-pilot://navigation/pantslabyrinth/cart` |
| Wunschliste | `braze-pilot://navigation/pantslabyrinth/wishlist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Deeplinks mit Parametern

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Artikeldetailseite | `braze-pilot://navigation/pantslabyrinth/itemdetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Akzeptierte Parameter

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 20%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Beschreibung</th>
            <th>Erforderlich</th>
            <th>Standard (sofern nicht anders angegeben)</th>
            <th>Typ</th>
            <th>Beispiel</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>name</code></td>
            <td>Der Name des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>Jeans</td>
        </tr>
        <tr>
            <td><code>price</code></td>
            <td>Der Preis des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>85</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>Die URL des Bildes des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>description</code></td>
            <td>Die Beschreibung des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>Dieser Artikel ist hervorragend.</td>
        </tr>
        <tr>
            <td><code>quantity</code></td>
            <td>Die Menge des Artikels.</td>
            <td>Kein:e</td>
            <td>(1 %)</td>
            <td>Zahl</td>
            <td>(2 %)</td>
        </tr>
        <tr>
            <td><code>size</code></td>
            <td>Eine String-Zeichenfolge, die die Größe des Artikels angibt.</td>
            <td>Kein:e</td>
            <td>M</td>
            <td>String</td>
            <td>Groß</td>
        </tr>
        <tr>
            <td><code>colors</code></td>
            <td>Eine durch Kommas getrennte Liste von Hex-Farben. Dies sind die für diesen Artikel verfügbaren Farben.</td>
            <td>Kein:e</td>
            <td>#23000000</td>
            <td>String</td>
            <td>#000000,#FF0000</td>
        </tr>
        <tr>
            <td><code>color_strings</code></td>
            <td>Eine Liste der durch Kommas getrennten Strings. Stellt die Farben im Text dar.</td>
            <td>Kein:e</td>
            <td>Schwarz</td>
            <td>String</td>
            <td>Blau, Rot</td>
        </tr>
        <tr>
            <td><code>selected_color</code></td>
            <td>Der ausgewählte Index der Farbe, die im SELEKTOR ausgewählt werden soll, wenn der Nutzer:in den Bildschirm aufruft. Wenn kein Wert angegeben wird, wird die erste Farbe, die ausgewählt wurde, verwendet.</td>
            <td>Kein:e</td>
            <td>0</td>
            <td>Zahl</td>
            <td>(1 %)</td>
        </tr>
    </tbody>
</table>

## Filmkanon

Dies sind die Deeplinks für die App der fiktiven Marke Steppington in Pilot.

### Beispiel für einen Deeplink

`braze-pilot://navigation/moviecannon/moviedetails?id=1&title=Jaws&thumbnail=https://picsum.photos/400&video=0&description=This%20video%20is%20awesome%21`

### Deeplinks ohne Parameter

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Begrüßungsbildschirm | `braze-pilot://navigation/moviecannon/splash` |
| Begrüßungsbildschirm | `braze-pilot://navigation/moviecannon/welcome` |
| Filmverzeichnis | `braze-pilot://navigation/moviecannon/moviecannon` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Deeplinks mit Parametern

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Filmdetails-Seite | `braze-pilot://navigation/moviecannon/moviedetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Akzeptierte Parameter

| Parameter | Beschreibung | Erforderlich | Typ | Beispiel |
| --- | --- | --- | --- | --- |
| `id` | Die ID des Films. | Ja | Zahl | (1 %) |
| `title` | Der Titel des Films. | Ja | String | Der weiße Hai |
| `thumbnail` | Die Internet-URL der Miniaturansicht, die vor dem Film angezeigt werden soll. | Ja | String | `https://picsum.photos/400` |
| `video` | Der Index in der Liste der anzuzeigenden Videos. | Kein:e | Zahl | 0 |
| `description` | Die Beschreibung des Videos. | Ja | String | `This%20video%20is%20awesome%21` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
