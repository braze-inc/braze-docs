---
nav_title: Datenwörterbuch
article_title: Datenwörterbuch für Braze Pilot
page_order: 3
page_type: reference
description: "Dieser Artikel beschreibt die erforderlichen Integrationsschritte für Ihre Entwicklerabteilung."
---

# Datenwörterbuch

> Jede App-Simulation in Braze Pilot ist so konfiguriert, dass sie verschiedene Ereignisse und Attribute basierend auf den Aktivitäten der Nutzer:innen in der App erfasst. 

## Der Umgang mit Daten

Die App protokolliert benutzerdefinierte Attribute und Ereignisse, die für die Branche, die durch die fiktive Marke repräsentiert wird, typisch sind. Sie können diese Attribute verwenden, um Demos für eine Vielzahl gängiger Anwendungsfälle zu erstellen.
Im Allgemeinen werden alle Ereignisse und Attribute mit einem Shortcode vorangestellt, der der für die Daten verantwortlichen App-Simulation entspricht. Zum Beispiel:

- Alle von der Steppington-App-Simulation protokollierten Daten sind mit einem Präfix versehen. `st_`
- Alle von der PantsLabyrinth-App-Simulation protokollierten Daten sind mit einem Präfix versehen. `pl_`
- Alle von der MovieCanon-App-Simulation protokollierten Daten sind mit dem Präfix `mc_`

## Liste der protokollierten Ereignisse und Attribute

Die folgende Tabelle listet die von Braze Pilot protokollierten Ereignisse und Attribute auf.

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
            <td>Filmkanon</td>
            <td>Event</td>
            <td></td>
            <td>Wenn der Nutzer:in die MovieCanon-App öffnet</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>Filmkanon</td>
            <td>Event</td>
            <td><code>title: string</code></td>
            <td>Wenn die Nutzer:innen das Video angesehen haben</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>Filmkanon</td>
            <td>Event</td>
            <td><code>title: string</code></td>
            <td>Wenn die Nutzer:in eine Filmseite aufruft</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>Hosenlabyrinth</td>
            <td>Event</td>
            <td><code>item_name: string</code></td>
            <td>Wenn die Nutzer:in eine Produktseite aufruft</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>Hosenlabyrinth</td>
            <td>Event</td>
            <td></td>
            <td>Wenn die Nutzer:innen die PantsLabyrinth-App öffnen</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>Hosenlabyrinth</td>
            <td>Event</td>
            <td><code>item_name: string</code></td>
            <td>Wenn die Nutzer:in einen Artikel zu ihrer Wunschliste hinzufügt</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>Hosenlabyrinth</td>
            <td>Event</td>
            <td><code>item_name: string</code></td>
            <td>Wenn der Nutzer:in einen Artikel in seinen Warenkorb legt</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event&gt;</code></td>
            <td>Hosenlabyrinth</td>
            <td>Event</td>
            <td><code>name: string</code><br><code>price: number</code></td>
            <td>Wenn die Nutzer:in einen Kauf abschließt</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td></td>
            <td>Wenn die Nutzer:in die Steppington-App öffnet</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>Wenn der Nutzer:in ein Training abgeschlossen hat</td>
        </tr>
        <tr>
            <td><code>st_viewed_premium_benefit</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>benefit_type: string</code></td>
            <td>Wenn der Nutzer:in die Registerkarte „Steppington+“ aufruft (sofern diese mit dem Feature-Flag aktiviert ist)</td>
        </tr>
        <tr>
            <td><code>st_viewed_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code></td>
            <td>Wenn die Nutzer:in eine Trainingsseite aufruft</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>Wenn der Nutzer:in ein Training abgeschlossen hat</td>
        </tr>
        <tr>
            <td><code>st_most_recent_completed_class</code></td>
            <td>Steppington</td>
            <td>Attribut</td>
            <td><code>string</code></td>
            <td>Wenn der Nutzer:in ein Training abgeschlossen hat</td>
        </tr>
        <tr>
            <td><code>st_favorited_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code></td>
            <td>Wenn die Nutzer:in eine Klasse als Favorit speichert</td>
        </tr>
        <tr>
            <td><code>st_unfavorited_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code></td>
            <td>Wenn die Nutzer:in eine Klasse aus den Favoriten entfernt</td>
        </tr>
        <tr>
            <td><code>st_started_free_trial</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td></td>
            <td>Wenn die Nutzer:in den Button <strong>„Kostenlose Demo starten“</strong> auswählt</td>
        </tr>
        <tr>
            <td><code>st_set_goal</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>goal_name: string</code><br><code>goal: number</code><br><code>units: string</code></td>
            <td>Wenn der Nutzer:in den Button <strong>„Kostenlose Demo starten“</strong> auswählt.</td>
        </tr>
    </tbody>
</table>
