---
nav_title: Dictionnaire de données
article_title: Dictionnaire de données pour Braze Pilot
page_order: 3
page_type: reference
description: "Cet article de référence couvre brièvement les étapes d'intégration requises de la part de vos ingénieurs ou développeurs."
---

# Dictionnaire de données

> Chaque simulation d'app dans Braze Pilot est instrumentée pour collecter une variété d'événements et d'attributs basés sur l'activité de l'utilisateur dans l'app. 

## L'approche des données

L'appli enregistre les attributs et les événements personnalisés typiques du secteur d'activité représenté par la marque fictive. Vous pouvez utiliser ces attributs pour réaliser des démonstrations dans divers cas d'utilisation courants.
En général, tous les événements et attributs sont précédés d'un code court qui correspond à la simulation d'application responsable des données. Par exemple :

- Toutes les données enregistrées par l'application de simulation Steppington sont précédées du préfixe `st_`
- Toutes les données enregistrées par la simulation de l'application PantsLabyrinth sont précédées du préfixe `pl_`
- Toutes les données enregistrées par la simulation de l'application MovieCanon sont précédées du préfixe `mc_`

## Liste des événements et attributs enregistrés

Le tableau suivant répertorie les événements et les attributs consignés par Braze Pilot.

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 32%;
}
th:nth-child(2), td:nth-child(2) {
    width: 15%;
}
th:nth-child(3), td:nth-child(3) {
    width: 10%;
}
th:nth-child(4), td:nth-child(4) {
    width: 20%;
}
th:nth-child(5), td:nth-child(5) {
    width: 28%;
}
</style>

<table>
    <thead>
        <tr>
            <th>Nom</th>
            <th>Application</th>
            <th>Type</th>
            <th>Propriétés</th>
            <th>Lorsqu'il est enregistré</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>mc_entered_app</code></td>
            <td>MovieCanon</td>
            <td>Événement</td>
            <td></td>
            <td>Lorsque l'utilisateur entre dans l'application MovieCanon</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>MovieCanon</td>
            <td>Événement</td>
            <td><code>titre : chaîne de caractères</code></td>
            <td>Lorsque l'utilisateur a fini de regarder une vidéo</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>MovieCanon</td>
            <td>Événement</td>
            <td><code>titre : chaîne de caractères</code></td>
            <td>Lorsque l'utilisateur consulte une page de film</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>PantalonLabyrinthe</td>
            <td>Événement</td>
            <td><code>item_name: chaîne de caractères</code></td>
            <td>Lorsque l'utilisateur consulte une page produit</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>PantalonLabyrinthe</td>
            <td>Événement</td>
            <td></td>
            <td>Lorsque l'utilisateur entre dans l'application PantsLabyrinth</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>PantalonLabyrinthe</td>
            <td>Événement</td>
            <td><code>item_name: chaîne de caractères</code></td>
            <td>Lorsque l'utilisateur ajoute un article à sa liste de souhaits</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>PantalonLabyrinthe</td>
            <td>Événement</td>
            <td><code>item_name: chaîne de caractères</code></td>
            <td>Lorsque l'utilisateur ajoute un article à son panier</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event></code></td>
            <td>PantalonLabyrinthe</td>
            <td>Événement</td>
            <td><code>nom : chaîne de caractères</code><br><code>prix : nombre</code></td>
            <td>Lorsque l'utilisateur effectue un achat</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td></td>
            <td>Lorsque l'utilisateur entre dans l'application Steppington</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>class_type: chaîne de caractères</code><br><code>calories_burned: nombre</code><br><code>workout_length: nombre</code></td>
            <td>Lorsque l'utilisateur termine une séance d'entraînement</td>
        </tr>
        <tr>
            <td><code>st_viewed_premium_benefit</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>benefit_type: chaîne de caractères</code></td>
            <td>Lorsque l'utilisateur visite l'onglet Steppington+ (s'il est activé avec le drapeau de fonctionnalité)</td>
        </tr>
        <tr>
            <td><code>st_viewed_class</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>class_type: chaîne de caractères</code></td>
            <td>Lorsque l'utilisateur visite une page d'entraînement</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>class_type: chaîne de caractères</code><br><code>calories_burned: nombre</code><br><code>workout_length: nombre</code></td>
            <td>Lorsque l'utilisateur termine une séance d'entraînement</td>
        </tr>
        <tr>
            <td><code>st_most_recent_completed_class</code></td>
            <td>Steppington</td>
            <td>Attribut</td>
            <td><code>chaîne de caractères</code></td>
            <td>Lorsque l'utilisateur termine une séance d'entraînement</td>
        </tr>
        <tr>
            <td><code>st_favorited_class</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>class_type: chaîne de caractères</code></td>
            <td>Lorsque l'utilisateur privilégie une classe</td>
        </tr>
        <tr>
            <td><code>st_unfavorited_class</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>class_type: chaîne de caractères</code></td>
            <td>Lorsque l'utilisateur désapprouve une classe</td>
        </tr>
        <tr>
            <td><code>st_started_free_trial</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td></td>
            <td>Lorsque l'utilisateur sélectionne le bouton <strong>Démarrer l'essai gratuit</strong> </td>
        </tr>
        <tr>
            <td><code>st_set_goal</code></td>
            <td>Steppington</td>
            <td>Événement</td>
            <td><code>goal_name: chaîne de caractères</code><br><code>objectif : nombre</code><br><code>unités : chaîne de caractères</code></td>
            <td>Lorsque l'utilisateur sélectionne le bouton <strong>Démarrer l'essai gratuit</strong>.</td>
        </tr>
    </tbody>
</table>
