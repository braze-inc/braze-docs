---
nav_title: Navigation Deeplinks setzen
article_title: Navigation Deeplinks in Braze Pilot setzen
page_order: 4
page_type: reference
description: "Dieser Artikel beschreibt die erforderlichen Integrationsschritte für Ihre Entwicklerabteilung."
---

# Navigation Deeplinks in Braze Pilot setzen

> Braze Pilot unterstützt Deeplinks vom Braze Messaging zu bestimmten Teilen der Pilot App. Damit ist es zulässig, Engagement-Anwendungsfälle zu erstellen, die Nutzer:innen in verschiedene Bereiche der Pilot-Anwendung führen. Sie können auch optionale Deeplinks-Parameter verwenden, um die Inhalte auf bestimmten Seiten in der App für den Nutzer:innen anzupassen. Mehr über Deeplinks erfahren Sie unter [Deeplinks setzen zu In-App-Inhalten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

## Allgemein

Dies sind die Deeplinks für die Hauptnavigationsseiten in der Pilot App. 

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Projekte | `braze-pilot://navigation/projects` |
| Log Daten | `braze-pilot://navigation/logdata` |
| Einrichtung | `braze-pilot://navigation/setup` |
| Sprache ändern | `braze-pilot://navigation/selectlanguage` |
| Kamera | `braze-pilot://navigation/camera` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Steppington

Dies sind die Deeplinks für die App der fiktiven Marke Steppington in Pilot.

### Beispiel Deeplinks setzen

`braze-pilot://navigation/steppington/workout?title=Running&icon=HEART_DETAILS&image=https://picsum.photos/400&info=This%20workout%20is%20awesome%21&workout=5k%20Run&calories=600&length=25&workout_info_left_text=Road%20Run&workout_info_left_icon=RUNNING_HOME&workout_info_center_text=120%20BPM&workout_info_center_icon=HEART_DETAILS&workout_info_right_text=25%3A00&workout_info_right_icon=TIMER_DETAILS`

### Deeplinks ohne Parameter setzen

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Splash Screen | `braze-pilot://navigation/steppington/splash` |
| Home | `braze-pilot://navigation/steppington/home` |
| Steppington+ Seite | `braze-pilot://navigation/steppington/plus` |
| Bildschirm Ziele | `braze-pilot://navigation/steppington/goals` |
| Bildschirm Ziele ändern | `braze-pilot://navigation/steppington/changegoals` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Deeplinks mit Parametern setzen

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Workout | `braze-pilot://navigation/steppington/workout` |
| Aktives Workout | `braze-pilot://navigation/steppington/activeworkout` |
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
            <th>Standard (wenn nicht angegeben)</th>
            <th>Typ</th>
            <th>Beispiel</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>Titel</code></td>
            <td>Der Titel, der am oberen Rand des Bildschirms verwendet werden soll.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>Läuft …</td>
        </tr>
        <tr>
            <td><code>Ikone</code></td>
            <td>Ein String, der angibt, welches Symbol verwendet werden soll.</td>
            <td>Kein:e</td>
            <td><code>RUNNING_HOME</code></td>
            <td>String</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>Bild</code></td>
            <td>Die URL des Bildes des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>Infos</code></td>
            <td>Informationen über das Training, die über dem Button zum Starten des Trainings angezeigt werden.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>This%20workout%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>Workout</code></td>
            <td>Der Name des Workouts. Gesendet in dem <code>st_completed_class</code> Ereignis.</td>
            <td>Ja</td>
            <td></td>
            <td>Zahl</td>
            <td>5k%20Lauf</td>
        </tr>
        <tr>
            <td><code>Kalorien</code></td>
            <td>Die Anzahl der Kalorien, die auf dem Bildschirm für das aktive Training angezeigt werden soll. Gesendet in dem <code>st_completed_class</code> Ereignis.</td>
            <td>Kein:e</td>
            <td>Zufallszahl zwischen 500 und 1.250</td>
            <td>Zahl</td>
            <td>600</td>
        </tr>
        <tr>
            <td><code>Länge</code></td>
            <td>Die Länge des Workouts. Gesendet in dem <code>st_completed_class</code> Ereignis.</td>
            <td>Kein:e</td>
            <td></td>
            <td>Zahl</td>
            <td>25</td>
        </tr>
        <tr>
            <td><code>workout_info_left_text</code></td>
            <td>Der Text, der in der linken Karte auf dem aktiven Trainingsbildschirm verwendet werden soll.</td>
            <td>Kein:e</td>
            <td></td>
            <td>String</td>
            <td>Straße%20Lauf</td>
        </tr>
        <tr>
            <td><code>workout_info_left_icon</code></td>
            <td>Das Symbol, das in der linken Karte auf dem aktiven Trainingsbildschirm verwendet werden soll.</td>
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
            <td>120%20BPM</td>
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
            <td>Der Text, der in der rechten Karte auf dem aktiven Trainingsbildschirm verwendet werden soll.</td>
            <td>Kein:e</td>
            <td></td>
            <td>String</td>
            <td>25%3A00</td>
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

##### Icon Optionen

| Symbol | Bild |
| --- | --- |
| `RUNNING_HOME` | ![Eine Laufschuh-Ikone.]({% image_buster /assets/img/braze_pilot/running_home_icon.png %}){:style="max-width:30%"} |
| `HEART_DETAILS` | ![Ein Herz-Symbol.]({% image_buster /assets/img/braze_pilot/heart_details_icon.png %}){:style="max-width:30%"} |
| `TIMER_DETAILS` | ![Ein Stoppuhr-Symbol.]({% image_buster /assets/img/braze_pilot/timer_details_icon.png %}){:style="max-width:30%"} |
| `YOGA_HOME` | ![Eine Ikone einer Person in einer Yoga-Pose.]({% image_buster /assets/img/braze_pilot/yoga_home_icon.png %}){:style="max-width:30%"} |
| `BICYCLE_HOME` | ![Eine Fahrrad-Ikone.]({% image_buster /assets/img/braze_pilot/bicycle_home_icon.png %}){:style="max-width:30%"} |
| `DUMBBELL_HOME` | ![Ein Hantelsymbol.]({% image_buster /assets/img/braze_pilot/dumbbell_home_icon.png %}){:style="max-width:30%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## HosenLabyrinth

Dies sind die Deeplinks für die App der fiktiven Marke PantsLabyrinth in Pilot.

### Beispiel Deeplinks setzen

`braze-pilot://navigation/pantslabyrinth/itemdetails?name=Jeans&price=85&image=https://picsum.photos/400&description=This%20item%20is%20awesome%21&quantity=2&size=Large&colors=%230000FF,%23FF0000&color_strings=White,Blue&selected_color=1`

### Deeplinks ohne Parameter setzen

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Splash Screen | `braze-pilot://navigation/pantslabyrinth/splash` |
| Willkommensbildschirm | `braze-pilot://navigation/pantslabyrinth/welcome` |
| Listing-Bildschirm | `braze-pilot://navigation/pantslabyrinth/listing` |
| Warenkorb Seite | `braze-pilot://navigation/pantslabyrinth/cart` |
| Wunschzettel Seite | `braze-pilot://navigation/pantslabyrinth/wishlist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Deeplinks mit Parametern setzen

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Artikel-Detailseite | `braze-pilot://navigation/pantslabyrinth/itemdetails` |
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
            <th>Standard (wenn nicht angegeben)</th>
            <th>Typ</th>
            <th>Beispiel</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>Name</code></td>
            <td>Der Name des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>Jeans</td>
        </tr>
        <tr>
            <td><code>Preis</code></td>
            <td>Der Preis des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>85</td>
        </tr>
        <tr>
            <td><code>Bild</code></td>
            <td>Die URL des Bildes des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>Beschreibung</code></td>
            <td>Die Beschreibung des Artikels.</td>
            <td>Ja</td>
            <td></td>
            <td>String</td>
            <td>This%20item%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>Menge</code></td>
            <td>Die Menge des Artikels.</td>
            <td>Kein:e</td>
            <td>(1 %)</td>
            <td>Zahl</td>
            <td>(2 %)</td>
        </tr>
        <tr>
            <td><code>size</code></td>
            <td>Ein String, der die Größe des Artikels angibt.</td>
            <td>Kein:e</td>
            <td>M</td>
            <td>String</td>
            <td>Groß</td>
        </tr>
        <tr>
            <td><code>Farben</code></td>
            <td>Eine Liste von Hex-Farben, die durch Kommas getrennt sind. Dies sind die verfügbaren Farben für den Artikel.</td>
            <td>Kein:e</td>
            <td>%23000000</td>
            <td>String</td>
            <td>%230000FF,%23FF0000</td>
        </tr>
        <tr>
            <td><code>color_strings</code></td>
            <td>Eine Liste der Farbstrings, die durch Kommas getrennt sind. Stellt die Farben im Text dar.</td>
            <td>Kein:e</td>
            <td>Schwarz</td>
            <td>String</td>
            <td>Blau, Rot</td>
        </tr>
        <tr>
            <td><code>selected_color</code></td>
            <td>Der ausgewählte Index der Farbe, die im SELEKTOR ausgewählt werden soll, wenn der Nutzer:innen auf dem Bildschirm ankommt. Wenn kein Wert verwendet wird, hat es die erste ausgewählte Farbe.</td>
            <td>Kein:e</td>
            <td>0</td>
            <td>Zahl</td>
            <td>(1 %)</td>
        </tr>
    </tbody>
</table>

## MovieCanon

Dies sind die Deeplinks für die App der fiktiven Marke Steppington in Pilot.

### Beispiel Deeplinks setzen

`braze-pilot://navigation/moviecannon/moviedetails?id=1&title=Jaws&thumbnail=https://picsum.photos/400&video=0&description=This%20video%20is%20awesome%21`

### Deeplinks ohne Parameter setzen

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Splash Screen | `braze-pilot://navigation/moviecannon/splash` |
| Willkommensbildschirm | `braze-pilot://navigation/moviecannon/welcome` |
| Filmliste Seite | `braze-pilot://navigation/moviecannon/moviecannon` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Deeplinks mit Parametern setzen

| Bildschirm | Deeplinks setzen |
| --- | --- |
| Film-Detailseite | `braze-pilot://navigation/moviecannon/moviedetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Akzeptierte Parameter

| Parameter | Beschreibung | Erforderlich | Typ | Beispiel |
| --- | --- | --- | --- | --- |
| `id` | Die ID des Films. | Ja | Zahl | (1 %) |
| `title` | Der Titel des Films. | Ja | String | Der Kiefer |
| `thumbnail` | Die Internet-URL der Miniaturansicht, die vor dem Film angezeigt wird. | Ja | String | `https://picsum.photos/400` |
| `video` | Der Index in der Liste der anzuzeigenden Videos. | Kein:e | Zahl | 0 |
| `description` | Die Beschreibung des Videos. | Ja | String | `This%20video%20is%20awesome%21` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
