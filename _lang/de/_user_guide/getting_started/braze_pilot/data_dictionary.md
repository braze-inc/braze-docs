---
nav_title: Wörterbuch der Daten
article_title: Wörterbuch für Braze Pilot
page_order: 3
page_type: reference
description: "Dieser Artikel beschreibt die erforderlichen Integrationsschritte für Ihre Entwicklerabteilung."
---

# Wörterbuch der Daten

> Jede App-Simulation in Braze Pilot ist so instrumentiert, dass sie eine Vielzahl von Ereignissen und Attributen sammelt, die auf der Aktivität des Nutzers in der App basieren. 

## Der Umgang mit Daten

Die App protokolliert angepasste Attribute und Events, die typisch für die Branche sind, die von der fiktiven Marke vertreten wird. Sie können diese Attribute verwenden, um Demos für eine Vielzahl gängiger Anwendungsfälle zu erstellen.
Im Allgemeinen wird allen Ereignissen und Attributen ein Shortcode vorangestellt, der der für die Daten verantwortlichen App-Simulation entspricht. Zum Beispiel:

- Allen Daten, die von der Steppington App Simulation aufgezeichnet werden, wird ein Präfix vorangestellt `st_`
- Allen Daten, die von der PantsLabyrinth App Simulation aufgezeichnet werden, wird ein Präfix vorangestellt `pl_`
- Allen Daten, die von der MovieCanon App Simulation aufgezeichnet werden, wird ein Präfix vorangestellt `mc_`

## Liste der protokollierten Ereignisse und Attribute

In der folgenden Tabelle sind die von Braze Pilot protokollierten Ereignisse und Attribute aufgeführt.

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
            <th>Name</th>
            <th>App</th>
            <th>Typ</th>
            <th>Eigenschaften</th>
            <th>Wenn es protokolliert ist</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>mc_entered_app</code></td>
            <td>MovieCanon</td>
            <td>Event</td>
            <td></td>
            <td>Wenn der Nutzer:innen die MovieCanon App betritt</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>MovieCanon</td>
            <td>Event</td>
            <td><code>Titel: String</code></td>
            <td>Wenn der Nutzer:innen ein Video zu Ende angesehen hat</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>MovieCanon</td>
            <td>Event</td>
            <td><code>Titel: String</code></td>
            <td>Wenn der Nutzer:in eine Filmseite blickt</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>HosenLabyrinth</td>
            <td>Event</td>
            <td><code>item_name: String</code></td>
            <td>Wenn der Nutzer:innen eine Produktseite aufruft</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>HosenLabyrinth</td>
            <td>Event</td>
            <td></td>
            <td>Wenn der Nutzer:innen die App PantsLabyrinth betritt</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>HosenLabyrinth</td>
            <td>Event</td>
            <td><code>item_name: String</code></td>
            <td>Wenn der Nutzer:innen einen Artikel zu seinem Wunschzettel hinzufügt</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>HosenLabyrinth</td>
            <td>Event</td>
            <td><code>item_name: String</code></td>
            <td>Wenn der Nutzer:innen einen Artikel in den Warenkorb legt</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event></code></td>
            <td>HosenLabyrinth</td>
            <td>Event</td>
            <td><code>Name: String</code><br><code>Preis: Nummer</code></td>
            <td>Wenn der Nutzer:innen einen Kauf abschließt</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td></td>
            <td>Wenn der Nutzer:innen die Steppington App betritt</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: String</code><br><code>calories_burned: Nummer</code><br><code>workout_length: Nummer</code></td>
            <td>Wenn der Nutzer:in ein Training abgeschlossen hat</td>
        </tr>
        <tr>
            <td><code>st_viewed_premium_benefit</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>benefit_type: String</code></td>
            <td>Wenn der Nutzer:innen den Tab Steppington+ besucht (wenn er mit dem Feature-Flag aktiviert ist)</td>
        </tr>
        <tr>
            <td><code>st_viewed_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: String</code></td>
            <td>Wenn der Nutzer:innen eine Trainingsseite besucht</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: String</code><br><code>calories_burned: Nummer</code><br><code>workout_length: Nummer</code></td>
            <td>Wenn der Nutzer:in ein Training abgeschlossen hat</td>
        </tr>
        <tr>
            <td><code>st_most_recent_completed_class</code></td>
            <td>Steppington</td>
            <td>Attribut</td>
            <td><code>String</code></td>
            <td>Wenn der Nutzer:in ein Training abgeschlossen hat</td>
        </tr>
        <tr>
            <td><code>st_favorited_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: String</code></td>
            <td>Wenn der Nutzer:innen eine Klasse favorisiert</td>
        </tr>
        <tr>
            <td><code>st_unfavorited_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: String</code></td>
            <td>Wenn der Nutzer:innen eine Klasse ablehnt</td>
        </tr>
        <tr>
            <td><code>st_started_free_trial</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td></td>
            <td>Wenn der Nutzer:innen den Button <strong>Kostenlose Demo starten</strong> auswählt</td>
        </tr>
        <tr>
            <td><code>st_set_goal</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>goal_name: String</code><br><code>Ziel: Nummer</code><br><code>Einheiten: String</code></td>
            <td>Wenn der Nutzer:innen den Button <strong>Kostenlose Demo starten</strong> auswählt.</td>
        </tr>
    </tbody>
</table>
