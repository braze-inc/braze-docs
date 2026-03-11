---
nav_title: Liens profonds de navigation
article_title: Liens profonds de navigation dans Braze Pilot
page_order: 4
page_type: reference
description: "Le présent article de référence couvre brièvement les étapes d’intégration dont vos ingénieurs ou développeurs ont besoin."
---

# Liens profonds dans Braze Pilot

> Braze Pilot prend en charge la création de liens profonds depuis l'envoi de messages Braze vers des sections spécifiques de l'application Pilot. Cela vous permet de créer des cas d'utilisation engageants, incitant les utilisateurs à explorer différentes parties de l'application Pilot. Vous pouvez également utiliser des paramètres de lien profond facultatifs pour rendre le contenu de certaines pages de l'application personnalisé pour l'utilisateur. Pour plus d'informations sur la création de liens profonds, veuillez consulter [la section Création de liens profonds vers du contenu intégré à l'application]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

## Généralités

Voici les liens profonds vers les principales pages de navigation de l'application Pilot. 

| Écran | Lien profond |
| --- | --- |
| Projets | `braze-pilot://navigation/projects` |
| Données de connexion | `braze-pilot://navigation/logdata` |
| Configuration | `braze-pilot://navigation/setup` |
| Changer de langue | `braze-pilot://navigation/selectlanguage` |
| Appareil photo | `braze-pilot://navigation/camera` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Steppington

Voici les liens profonds pour l'application de la marque fictive Steppington dans Pilot.

### Exemple de lien profond

`braze-pilot://navigation/steppington/workout?title=Running&icon=HEART_DETAILS&image=https://picsum.photos/400&info=This%20workout%20is%20awesome%21&workout=5k%20Run&calories=600&length=25&workout_info_left_text=Road%20Run&workout_info_left_icon=RUNNING_HOME&workout_info_center_text=120%20BPM&workout_info_center_icon=HEART_DETAILS&workout_info_right_text=25%3A00&workout_info_right_icon=TIMER_DETAILS`

### Liens profonds sans paramètres

| Écran | Lien profond |
| --- | --- |
| Écran de démarrage | `braze-pilot://navigation/steppington/splash` |
| Accueil | `braze-pilot://navigation/steppington/home` |
| Page Steppington | `braze-pilot://navigation/steppington/plus` |
| Écran des objectifs | `braze-pilot://navigation/steppington/goals` |
| Modifier l'écran des objectifs | `braze-pilot://navigation/steppington/changegoals` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Liens profonds avec paramètres

| Écran | Lien profond |
| --- | --- |
| Entraînement | `braze-pilot://navigation/steppington/workout` |
| Entraînement actif | `braze-pilot://navigation/steppington/activeworkout` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Paramètres acceptés

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
            <th>Paramètre</th>
            <th>Description</th>
            <th>Requis</th>
            <th>Par défaut (si non spécifié)</th>
            <th>Type</th>
            <th>Exemple</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>title</code></td>
            <td>Le titre à utiliser en haut de l'écran.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>En cours</td>
        </tr>
        <tr>
            <td><code>icon</code></td>
            <td>Une chaîne de caractères représentant l'icône à utiliser.</td>
            <td>Non</td>
            <td><code>RUNNING_HOME</code></td>
            <td>Chaîne de caractères</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>L'URL de l'image de l'article.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>info</code></td>
            <td>Veuillez indiquer les informations relatives à l'entraînement au-dessus du bouton de démarrage de l'entraînement.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>Cet entraînement est remarquable.</td>
        </tr>
        <tr>
            <td><code>workout</code></td>
            <td>Le nom de l'entraînement. Envoyé dans le <code>st_completed_class</code> événement.</td>
            <td>Oui</td>
            <td></td>
            <td>Nombre</td>
            <td>Course de 5 km</td>
        </tr>
        <tr>
            <td><code>calories</code></td>
            <td>Le nombre de calories à afficher sur l'écran d'entraînement actif. Envoyé dans le <code>st_completed_class</code> événement.</td>
            <td>Non</td>
            <td>Nombre aléatoire compris entre 500 et 1 250</td>
            <td>Nombre</td>
            <td>six cents</td>
        </tr>
        <tr>
            <td><code>length</code></td>
            <td>La durée de l'entraînement. Envoyé dans le <code>st_completed_class</code> événement.</td>
            <td>Non</td>
            <td></td>
            <td>Nombre</td>
            <td>25</td>
        </tr>
        <tr>
            <td><code>workout_info_left_text</code></td>
            <td>Texte à utiliser dans la carte de gauche sur l'écran d'entraînement actif.</td>
            <td>Non</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>Course sur route</td>
        </tr>
        <tr>
            <td><code>workout_info_left_icon</code></td>
            <td>L'icône à utiliser dans la carte de gauche sur l'écran d'entraînement actif.</td>
            <td>Non</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>RUNNING_HOME</td>
        </tr>
        <tr>
            <td><code>workout_info_center_text</code></td>
            <td>Texte à utiliser dans la carte centrale de l'écran d'entraînement actif.</td>
            <td>Non</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>120 % BPM</td>
        </tr>
        <tr>
            <td><code>workout_info_center_icon</code></td>
            <td>L'icône à utiliser dans la carte centrale de l'écran d'entraînement actif.</td>
            <td>Non</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>workout_info_right_text</code></td>
            <td>Texte à utiliser dans la carte de droite sur l'écran d'entraînement actif.</td>
            <td>Non</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>25 % 3A00</td>
        </tr>
        <tr>
            <td><code>workout_info_right_icon</code></td>
            <td>L'icône à utiliser dans la carte de droite sur l'écran d'entraînement actif.</td>
            <td>Non</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>TIMER_DETAILS</td>
        </tr>
    </tbody>
</table>

##### Options des icônes

| Icône | Image |
| --- | --- |
| `RUNNING_HOME` | ![Une icône parmi les chaussures de course.]({% image_buster /assets/img/braze_pilot/running_home_icon.png %}){:style="max-width:30%"} |
| `HEART_DETAILS` | ![Une icône en forme de cœur.]({% image_buster /assets/img/braze_pilot/heart_details_icon.png %}){:style="max-width:30%"} |
| `TIMER_DETAILS` | ![Une icône représentant un chronomètre.]({% image_buster /assets/img/braze_pilot/timer_details_icon.png %}){:style="max-width:30%"} |
| `YOGA_HOME` | ![Une icône représentant une personne dans une posture de yoga.]({% image_buster /assets/img/braze_pilot/yoga_home_icon.png %}){:style="max-width:30%"} |
| `BICYCLE_HOME` | ![Une icône du cyclisme.]({% image_buster /assets/img/braze_pilot/bicycle_home_icon.png %}){:style="max-width:30%"} |
| `DUMBBELL_HOME` | ![Une icône représentant un haltère.]({% image_buster /assets/img/braze_pilot/dumbbell_home_icon.png %}){:style="max-width:30%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## PantsLabyrinth

Voici les liens profonds pour l'application de la marque fictive PantsLabyrinth dans Pilot.

### Exemple de lien profond

`braze-pilot://navigation/pantslabyrinth/itemdetails?name=Jeans&price=85&image=https://picsum.photos/400&description=This%20item%20is%20awesome%21&quantity=2&size=Large&colors=%230000FF,%23FF0000&color_strings=White,Blue&selected_color=1`

### Liens profonds sans paramètres

| Écran | Lien profond |
| --- | --- |
| Écran de démarrage | `braze-pilot://navigation/pantslabyrinth/splash` |
| Écran d'accueil | `braze-pilot://navigation/pantslabyrinth/welcome` |
| Écran de liste | `braze-pilot://navigation/pantslabyrinth/listing` |
| Page du panier | `braze-pilot://navigation/pantslabyrinth/cart` |
| Page de liste de souhaits | `braze-pilot://navigation/pantslabyrinth/wishlist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Liens profonds avec paramètres

| Écran | Lien profond |
| --- | --- |
| Page de détails de l'article | `braze-pilot://navigation/pantslabyrinth/itemdetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Paramètres acceptés

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
            <th>Paramètre</th>
            <th>Description</th>
            <th>Requis</th>
            <th>Par défaut (si non spécifié)</th>
            <th>Type</th>
            <th>Exemple</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>name</code></td>
            <td>Le nom de l'article.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>Jeans</td>
        </tr>
        <tr>
            <td><code>price</code></td>
            <td>Le prix de l'article.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>85</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>L'URL de l'image de l'article.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>description</code></td>
            <td>La description de l'article.</td>
            <td>Oui</td>
            <td></td>
            <td>Chaîne de caractères</td>
            <td>Cet article est remarquable.</td>
        </tr>
        <tr>
            <td><code>quantity</code></td>
            <td>La quantité de l'article.</td>
            <td>Non</td>
            <td>1</td>
            <td>Nombre</td>
            <td>2</td>
        </tr>
        <tr>
            <td><code>size</code></td>
            <td>Une chaîne de caractères représentant la taille de l'élément.</td>
            <td>Non</td>
            <td>M</td>
            <td>Chaîne de caractères</td>
            <td>Grand</td>
        </tr>
        <tr>
            <td><code>colors</code></td>
            <td>Une liste de couleurs hexadécimales séparées par des virgules. Voici les couleurs disponibles pour cet article.</td>
            <td>Non</td>
            <td>#23000000</td>
            <td>Chaîne de caractères</td>
            <td>#230000FF,#FF0000</td>
        </tr>
        <tr>
            <td><code>color_strings</code></td>
            <td>Une liste des chaînes de caractères de couleurs séparées par des virgules. Représente les couleurs dans le texte.</td>
            <td>Non</td>
            <td>Noir</td>
            <td>Chaîne de caractères</td>
            <td>Bleu, Rouge</td>
        </tr>
        <tr>
            <td><code>selected_color</code></td>
            <td>L'index sélectionné de la couleur à choisir dans le sélecteur de couleurs lorsque l'utilisateur accède à l'écran. Si aucune valeur n'est utilisée, la première couleur sélectionnée est appliquée.</td>
            <td>Non</td>
            <td>0</td>
            <td>Nombre</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

## MovieCanon

Voici les liens profonds pour l'application de la marque fictive Steppington dans Pilot.

### Exemple de lien profond

`braze-pilot://navigation/moviecannon/moviedetails?id=1&title=Jaws&thumbnail=https://picsum.photos/400&video=0&description=This%20video%20is%20awesome%21`

### Liens profonds sans paramètres

| Écran | Lien profond |
| --- | --- |
| Écran de démarrage | `braze-pilot://navigation/moviecannon/splash` |
| Écran d'accueil | `braze-pilot://navigation/moviecannon/welcome` |
| Page de liste des films | `braze-pilot://navigation/moviecannon/moviecannon` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Liens profonds avec paramètres

| Écran | Lien profond |
| --- | --- |
| Page de détails du film | `braze-pilot://navigation/moviecannon/moviedetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Paramètres acceptés

| Paramètre | Description | Requis | Type | Exemple |
| --- | --- | --- | --- | --- |
| `id` | L'ID du film. | Oui | Nombre | 1 |
| `title` | Le titre du film. | Oui | Chaîne de caractères | Les Dents de la mer |
| `thumbnail` | L'URL Web de la vignette à afficher avant le film. | Oui | Chaîne de caractères | `https://picsum.photos/400` |
| `video` | L'index dans la liste des vidéos à diffuser. | Non | Nombre | 0 |
| `description` | La description de la vidéo. | Oui | Chaîne de caractères | `This%20video%20is%20awesome%21` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
