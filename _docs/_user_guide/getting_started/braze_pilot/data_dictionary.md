---
nav_title: Data dictionary
article_title: Data Dictionary for Braze Pilot
page_order: 3
page_type: reference
description: "This reference article briefly covers the integration steps required from your engineers or developers."
---

# Data dictionary

> Each app simulation in Braze Pilot is instrumented to collect a variety of events and attributes based on user activity in the app. 

## The approach to data

The app logs custom attributes and events typical of the industry represented by the fictional brand. You can use these attributes to power demos for a variety of common use cases. 
Generally, all events and attributes are prefixed with a short code that corresponds to the app simulation responsible for the data. For example:

- All data logged by the Steppington app simulation are prefixed with `st_`
- All data logged by the PantsLabyrinth app simulation are prefixed with `pl_`
- All data logged by the MovieCanon app simulation are prefixed with `mc_`

## List of logged events and attributes

The following table lists the events and attributes logged by Braze Pilot.

Update the following table styling to make the first column 30%, the second column 15%, the third column 15%, the fourth column 20%, and the last column 20%.
Here is the updated HTML table with the specified column widths:

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
            <th>Type</th>
            <th>Properties</th>
            <th>When it's logged</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>mc_entered_app</code></td>
            <td>MovieCanon</td>
            <td>Event</td>
            <td></td>
            <td>When the user enters the MovieCanon app</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>MovieCanon</td>
            <td>Event</td>
            <td><code>title: string</code></td>
            <td>When the user finishes watching a video</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>MovieCanon</td>
            <td>Event</td>
            <td><code>title: string</code></td>
            <td>When the user views a movie page</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>PantsLabyrinth</td>
            <td>Event</td>
            <td><code>item_name: string</code></td>
            <td>When the user views a product page</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>PantsLabyrinth</td>
            <td>Event</td>
            <td></td>
            <td>When the user enters the PantsLabyrinth app</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>PantsLabyrinth</td>
            <td>Event</td>
            <td><code>item_name: string</code></td>
            <td>When the user adds an item to their wish list</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>PantsLabyrinth</td>
            <td>Event</td>
            <td><code>item_name: string</code></td>
            <td>When the user adds an item to their cart</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event&gt;</code></td>
            <td>PantsLabyrinth</td>
            <td>Event</td>
            <td><code>name: string</code><br><code>price: number</code></td>
            <td>When the user completes a purchase</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td></td>
            <td>When the user enters the Steppington app</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>When the user completes a workout</td>
        </tr>
        <tr>
            <td><code>st_viewed_premium_benefit</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>benefit_type: string</code></td>
            <td>When the user visits the Steppington+ tab (if it's enabled with feature flag)</td>
        </tr>
        <tr>
            <td><code>st_viewed_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code></td>
            <td>When the user visits a workout page</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code><br><code>calories_burned: number</code><br><code>workout_length: number</code></td>
            <td>When the user completes a workout</td>
        </tr>
        <tr>
            <td><code>st_most_recent_completed_class</code></td>
            <td>Steppington</td>
            <td>Attribute</td>
            <td><code>string</code></td>
            <td>When the user completes a workout</td>
        </tr>
        <tr>
            <td><code>st_favorited_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code></td>
            <td>When the user favorites a class</td>
        </tr>
        <tr>
            <td><code>st_unfavorited_class</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>class_type: string</code></td>
            <td>When the user unfavorites a class</td>
        </tr>
        <tr>
            <td><code>st_started_free_trial</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td></td>
            <td>When the user selects the <strong>Start Free Trial</strong> button</td>
        </tr>
        <tr>
            <td><code>st_set_goal</code></td>
            <td>Steppington</td>
            <td>Event</td>
            <td><code>goal_name: string</code><br><code>goal: number</code><br><code>units: string</code></td>
            <td>When the user selects the <strong>Start Free Trial</strong> button.</td>
        </tr>
    </tbody>
</table>