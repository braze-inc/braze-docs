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

| Parameter | Description | Required | Default (if not specified) | Type | Example |
| --- | --- | --- | --- | --- | --- |
| `title` | The title to be used at the top of the screen. | Yes |  | String | Running |
| `icon` | A string representing which icon to use. | No | `RUNNING_HOME` | String | HEART_DETAILS |
| `image` | The URL of the image of the item. | Yes |  | String | `https://picsum.photos/400` |
| `info` | Information about the workout to be placed over the workout start button. | Yes |  | String | This%20workout%20is%20awesome%21 |
| `workout` | The name of the workout. Sent in the `st_completed_class` event. | Yes |  | Number | 5k%20Run |
| `calories` | The number of calories to be shown on the active workout screen. Sent in the `st_completed_class` event. | No | Random number between 500 and 1,250 | Number | 600 |
| `length` | The length of the workout. Sent in the `st_completed_class` event. | No |  | Number | 25 |
| `workout_info_left_text` | The text to be used in the left card on the active workout screen. | No | | String | Road%20Run |
| `workout_info_left_icon` | The icon to be used in the left card on the active workout screen. | No | | String | RUNNING_HOME |
| `workout_info_center_text` | The text to be used in the center card on the active workout screen. | No | | String | 120%20BPM |
| `workout_info_center_icon` | The icon to be used in the center card on the active workout screen. | No | | String | HEART_DETAILS |
| `workout_info_right_text` | The text to be used in the right card on the active workout screen. | No | | String | 25%3A00 |
| `workout_info_right_icon` | The icon to be used in the right card on the active workout screen. | No | | String | TIMER_DETAILS |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }

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

| Parameter | Description | Required | Default (if not specified) | Type | Example |
| --- | --- | --- | --- | --- | --- |
| `name` | The name of the item. | Yes |  | String | Jeans |
| `price` | The price of the item. | Yes |  | String | 85 |
| `image` | The URL of the image of the item. | Yes |  | String | `https://picsum.photos/400` |
| `description` | The description of the item. | Yes |  | String | `This%20item%20is%20awesome%21` |
| `quantity` | The quantity of the item. | No | 1 | Number | 2 |
| `size` | A string representing the size of the item. | No | M | String | Large |
| `colors` | A list of hex colors separated by commas. These are the colors available for the item. | No | %23000000 | String | %230000FF,%23FF0000 |
| `color_strings` | A list of the color strings separated by commas. Represents the colors in text. | No | Black | String | Blue, Red
| `selected_color` | The selected index of the color to be selected in the color selector when the user arrives on the screen. If no value is used, it has the first color selected. | No | 0 | Number | 1 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }

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
