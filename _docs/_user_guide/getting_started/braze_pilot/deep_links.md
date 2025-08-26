---
nav_title: Navigation Deep Links
article_title: Navigation Deep Links in Braze Pilot
page_order: 4
page_type: reference
description: "This reference article briefly covers the integration steps required from your engineers or developers."
---

# Navigation deep links in Braze Pilot

> Braze Pilot supports deep linking from Braze messaging to particular parts of the Pilot app. This allows you to create engagement use cases, driving users into various parts of the Pilot application. You can also use optional deep link parameters to customize the content on particular pages in the app for the user. For more on deep linking, see [Deep linking to in-app content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

## General

These are the deep links for the main navigation pages in the Pilot app. 

| Screen | Deep link |
| --- | --- |
| Projects | `braze-pilot://navigation/projects` |
| Log Data | `braze-pilot://navigation/logdata` |
| Setup | `braze-pilot://navigation/setup` |
| Change Language | `braze-pilot://navigation/selectlanguage` |
| Camera | `braze-pilot://navigation/camera` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Steppington

These are the deep links for the Steppington fictional brand app in Pilot.

### Example deep link

`braze-pilot://navigation/steppington/workout?title=Running&icon=HEART_DETAILS&image=https://picsum.photos/400&info=This%20workout%20is%20awesome%21&workout=5k%20Run&calories=600&length=25&workout_info_left_text=Road%20Run&workout_info_left_icon=RUNNING_HOME&workout_info_center_text=120%20BPM&workout_info_center_icon=HEART_DETAILS&workout_info_right_text=25%3A00&workout_info_right_icon=TIMER_DETAILS`

### Deep links without parameters

| Screen | Deep link |
| --- | --- |
| Splash screen | `braze-pilot://navigation/steppington/splash` |
| Home | `braze-pilot://navigation/steppington/home` |
| Steppington+ page | `braze-pilot://navigation/steppington/plus` |
| Goals screen | `braze-pilot://navigation/steppington/goals` |
| Change goals screen | `braze-pilot://navigation/steppington/changegoals` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Deep links with parameters

| Screen | Deep link |
| --- | --- |
| Workout | `braze-pilot://navigation/steppington/workout` |
| Active Workout | `braze-pilot://navigation/steppington/activeworkout` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Accepted parameters

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
            <th>Description</th>
            <th>Required</th>
            <th>Default (if not specified)</th>
            <th>Type</th>
            <th>Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>title</code></td>
            <td>The title to be used at the top of the screen.</td>
            <td>Yes</td>
            <td></td>
            <td>String</td>
            <td>Running</td>
        </tr>
        <tr>
            <td><code>icon</code></td>
            <td>A string representing which icon to use.</td>
            <td>No</td>
            <td><code>RUNNING_HOME</code></td>
            <td>String</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>The URL of the image of the item.</td>
            <td>Yes</td>
            <td></td>
            <td>String</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>info</code></td>
            <td>Information about the workout to be placed over the workout start button.</td>
            <td>Yes</td>
            <td></td>
            <td>String</td>
            <td>This%20workout%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>workout</code></td>
            <td>The name of the workout. Sent in the <code>st_completed_class</code> event.</td>
            <td>Yes</td>
            <td></td>
            <td>Number</td>
            <td>5k%20Run</td>
        </tr>
        <tr>
            <td><code>calories</code></td>
            <td>The number of calories to be shown on the active workout screen. Sent in the <code>st_completed_class</code> event.</td>
            <td>No</td>
            <td>Random number between 500 and 1,250</td>
            <td>Number</td>
            <td>600</td>
        </tr>
        <tr>
            <td><code>length</code></td>
            <td>The length of the workout. Sent in the <code>st_completed_class</code> event.</td>
            <td>No</td>
            <td></td>
            <td>Number</td>
            <td>25</td>
        </tr>
        <tr>
            <td><code>workout_info_left_text</code></td>
            <td>The text to be used in the left card on the active workout screen.</td>
            <td>No</td>
            <td></td>
            <td>String</td>
            <td>Road%20Run</td>
        </tr>
        <tr>
            <td><code>workout_info_left_icon</code></td>
            <td>The icon to be used in the left card on the active workout screen.</td>
            <td>No</td>
            <td></td>
            <td>String</td>
            <td>RUNNING_HOME</td>
        </tr>
        <tr>
            <td><code>workout_info_center_text</code></td>
            <td>The text to be used in the center card on the active workout screen.</td>
            <td>No</td>
            <td></td>
            <td>String</td>
            <td>120%20BPM</td>
        </tr>
        <tr>
            <td><code>workout_info_center_icon</code></td>
            <td>The icon to be used in the center card on the active workout screen.</td>
            <td>No</td>
            <td></td>
            <td>String</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>workout_info_right_text</code></td>
            <td>The text to be used in the right card on the active workout screen.</td>
            <td>No</td>
            <td></td>
            <td>String</td>
            <td>25%3A00</td>
        </tr>
        <tr>
            <td><code>workout_info_right_icon</code></td>
            <td>The icon to be used in the right card on the active workout screen.</td>
            <td>No</td>
            <td></td>
            <td>String</td>
            <td>TIMER_DETAILS</td>
        </tr>
    </tbody>
</table>

##### Icon options

| Icon | Image |
| --- | --- |
| `RUNNING_HOME` | ![A running shoe icon.]({% image_buster /assets/img/braze_pilot/running_home_icon.png %}){:style="max-width:30%"} |
| `HEART_DETAILS` | ![A heart icon.]({% image_buster /assets/img/braze_pilot/heart_details_icon.png %}){:style="max-width:30%"} |
| `TIMER_DETAILS` | ![A stopwatch icon.]({% image_buster /assets/img/braze_pilot/timer_details_icon.png %}){:style="max-width:30%"} |
| `YOGA_HOME` | ![An icon of person in a yoga pose.]({% image_buster /assets/img/braze_pilot/yoga_home_icon.png %}){:style="max-width:30%"} |
| `BICYCLE_HOME` | ![A bicycle icon.]({% image_buster /assets/img/braze_pilot/bicycle_home_icon.png %}){:style="max-width:30%"} |
| `DUMBBELL_HOME` | ![A dumbbell icon.]({% image_buster /assets/img/braze_pilot/dumbbell_home_icon.png %}){:style="max-width:30%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## PantsLabyrinth

These are the deep links for the PantsLabyrinth fictional brand app in Pilot.

### Example deep link

`braze-pilot://navigation/pantslabyrinth/itemdetails?name=Jeans&price=85&image=https://picsum.photos/400&description=This%20item%20is%20awesome%21&quantity=2&size=Large&colors=%230000FF,%23FF0000&color_strings=White,Blue&selected_color=1`

### Deep links without parameters

| Screen | Deep link |
| --- | --- |
| Splash screen | `braze-pilot://navigation/pantslabyrinth/splash` |
| Welcome screen | `braze-pilot://navigation/pantslabyrinth/welcome` |
| Listing screen | `braze-pilot://navigation/pantslabyrinth/listing` |
| Cart page | `braze-pilot://navigation/pantslabyrinth/cart` |
| Wishlist page | `braze-pilot://navigation/pantslabyrinth/wishlist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Deep links with parameters

| Screen | Deep link |
| --- | --- |
| Item details page | `braze-pilot://navigation/pantslabyrinth/itemdetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Accepted parameters

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
            <th>Description</th>
            <th>Required</th>
            <th>Default (if not specified)</th>
            <th>Type</th>
            <th>Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>name</code></td>
            <td>The name of the item.</td>
            <td>Yes</td>
            <td></td>
            <td>String</td>
            <td>Jeans</td>
        </tr>
        <tr>
            <td><code>price</code></td>
            <td>The price of the item.</td>
            <td>Yes</td>
            <td></td>
            <td>String</td>
            <td>85</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>The URL of the image of the item.</td>
            <td>Yes</td>
            <td></td>
            <td>String</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>description</code></td>
            <td>The description of the item.</td>
            <td>Yes</td>
            <td></td>
            <td>String</td>
            <td>This%20item%20is%20awesome%21</td>
        </tr>
        <tr>
            <td><code>quantity</code></td>
            <td>The quantity of the item.</td>
            <td>No</td>
            <td>1</td>
            <td>Number</td>
            <td>2</td>
        </tr>
        <tr>
            <td><code>size</code></td>
            <td>A string representing the size of the item.</td>
            <td>No</td>
            <td>M</td>
            <td>String</td>
            <td>Large</td>
        </tr>
        <tr>
            <td><code>colors</code></td>
            <td>A list of hex colors separated by commas. These are the colors available for the item.</td>
            <td>No</td>
            <td>%23000000</td>
            <td>String</td>
            <td>%230000FF,%23FF0000</td>
        </tr>
        <tr>
            <td><code>color_strings</code></td>
            <td>A list of the color strings separated by commas. Represents the colors in text.</td>
            <td>No</td>
            <td>Black</td>
            <td>String</td>
            <td>Blue, Red</td>
        </tr>
        <tr>
            <td><code>selected_color</code></td>
            <td>The selected index of the color to be selected in the color selector when the user arrives on the screen. If no value is used, it has the first color selected.</td>
            <td>No</td>
            <td>0</td>
            <td>Number</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

## MovieCanon

These are the deep links for the Steppington fictional brand app in Pilot.

### Example deep link

`braze-pilot://navigation/moviecannon/moviedetails?id=1&title=Jaws&thumbnail=https://picsum.photos/400&video=0&description=This%20video%20is%20awesome%21`

### Deep links without parameters

| Screen | Deep link |
| --- | --- |
| Splash screen | `braze-pilot://navigation/moviecannon/splash` |
| Welcome screen | `braze-pilot://navigation/moviecannon/welcome` |
| Movie listing page | `braze-pilot://navigation/moviecannon/moviecannon` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Deep links with parameters

| Screen | Deep link |
| --- | --- |
| Movie details page | `braze-pilot://navigation/moviecannon/moviedetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Accepted parameters

| Parameter | Description | Required | Type | Example |
| --- | --- | --- | --- | --- |
| `id` | The ID of the movie. | Yes | Number | 1 |
| `title` | The title of the movie. | Yes | String | Jaws |
| `thumbnail` | The web URL of the thumbnail to be shown before the movie. | Yes | String | `https://picsum.photos/400` |
| `video` | The index in the list of videos to be shown. | No | Number | 0 |
| `description` | The description of the video. | Yes | String | `This%20video%20is%20awesome%21` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
