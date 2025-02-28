---
nav_title: Zukunft Hymne
article_title: Zukunft Hymne
description: "Erfahren Sie, wie Sie Future Anthem mit Braze integrieren können."
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# Zukunft Hymne

> Das All-in-One-Produkt von Future Anthem für die Echtgeldspielbranche, Amplifier AI, bietet Inhaltspersonalisierung, Echtzeit-Erlebnisse und dynamische Zielgruppen. Amplifier AI funktioniert nahtlos in den Bereichen Sport, Casino und Lotterie und ermöglicht es Kunden, die Spielerprofile von Braze um branchenspezifische Spielerattribute zu erweitern, wie z.B. Lieblingsspiel, Lieblingsmannschaft, Engagement Score, Empfehlung für die nächste Wette, erwartete nächste Wette und mehr.

{% alert important %}
Diese Funktion befindet sich derzeit im Early Access. Wenden Sie sich bitte an das Future Anthem Customer Success Team, um zu beginnen.
{% endalert %}

## Voraussetzungen

| Anforderung              | Beschreibung                                            |
|--------------------------|--------------------------------------------------------|
| Zukünftiges Anthem-Konto    | Ein Konto von Future Anthem. |
| Braze REST API Schlüssel       | Ein Braze REST API Schlüssel mit der [`users.track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt      | Der Braze [REST-Endpunkt](https://www.braze.com/docs/developer_guide/rest_api/basics/#endpoints), der zu Ihrer Instanz passt, z. B. `rest.iad-01.com`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Mit dieser Integration können Sie:

- Identifizieren Sie Nutzer mit hohen Engagementwerten und bieten Sie ihnen personalisierte Angebote, wie z.B. exklusive Werbeaktionen oder VIP-Belohnungen.
- Schlagen Sie einem Benutzer ähnliche Spiele vor, die auf den Spielen basieren, die er bereits mag.

## Integration

Das Future Anthem Customer Success Team wird Ihnen bei der Einrichtung Ihrer Integration helfen. Wenden Sie sich an Ihren Ansprechpartner bei Customer Success, der Ihnen helfen wird, die wichtigsten Attribute zu identifizieren, die Sie an Braze senden können.

|Beispielattribute in Future Anthem|Beispiel-Attribute in Braze|
|-----------------------------------|---------------------------|
|![Die Attribute im Profil des Benutzers.]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %})|![Das Objekt-Attribut.]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %})|

## Benutzerdefinierte Attribute löten

Dies sind die verfügbaren benutzerdefinierten Attribute von Braze. Ausführlichere Informationen finden Sie unter [Future Anthem: Erste Schritte](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab Wett-Empfehlungen %}

| Unterkategorie | Beispiel (JSON) | Datentyp |
| ------- | ----------- |----------- |
| Benutzerpräferenzen | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| Objekt |
| Empfehlungen für Einzelwetten | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| Objekt |
| Accumulator-Wettempfehlungen | `{"Bet_1": "Halland Goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}`| Objekt |
| Accumulator-Wettempfehlungen | `{"Bet_1": 1.5, "Bet_2": 2}` | Objekt |
| Bet Builder Wett-Empfehlungen | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahwaks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}`| Objekt |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Bonus-Empfehlungen %}

| Unterkategorie | Beispiel | Datentyp |
| ------- | ----------- |----------- |
|NGR - Nettospielertrag für die Lebenszeit des Nutzers | 2232| Nummer|
| NGR14 - Nettospielertrag für die letzten 14 Tage der Aktivität | 42 | Nummer
| Spieler Profitabilität Score| 130 | Nummer |
| Engagement Score | 0.78 | Nummer |
| Abwanderungsrisiko-Score | 0.02 | Nummer |
| Geschätztes nächstes Wettdatum | 2024-08-29 | Uhrzeit |
| Bet and Get - Bonuswert-Empfehlung | 20 | Nummer |
| Weitere Empfehlungen für Bonuswerte in der Zukunft | 0 | Nummer |
| Zukunft CLTV  | 3126 | Nummer |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Spiel-Empfehlungen %}

| Unterkategorie | Beispiel | Datentyp |
| ------- | ----------- |----------- |
| Für Sie empfohlen | Fluffy Favourites, Fishin' Frenzy, Big Bass Bonanza, Rainbow Gold, Wild West| Array |
| Lieblingsspiele | Fischereirausch | Array |
| Empfohlene neue Spiele | Sticky Bees, Beware the Deep Megaways, Gold Party, The Flintstones| Array |
| Spieler wie Sie spielen (kollaborative Filterung) |Gold Blitz, Big Bass Splash, Rick and Morty, Book of Dead, Gates of Olympus, Luck O' the Irish | Array |
| Weil Sie gespielt haben (Spielähnlichkeit)|Fluffy Favourites 2, Luck Rish Express, Gold Cash, Aztec Treasure Hunt, Stars Bonanza | Array |
| Up Next (Spielablauf) | Fishin' Frenzy The Big Catch, Big Banker, 9 Masks Of Fire, Super Lion, Fishin' Bigger Pots Of Gold | Array |
| Beliebte Spiele | Tempel der Iris, Fishin' Frenzy, Rishing Reward, Crazy Time, Fluffy Favourites | Array |
| Kommende Spiele | Pig Banker, Hyper Gold, Pyramid King, Gold Cash | Array |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Spieler Cluster %}

| Unterkategorie | Beispiel | Datentyp |
| ------- | ----------- |----------- |
| Zeigen, in welchem Cluster sich der Spieler befindet | Hochwertiges Spiel Vielfältig| String |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Spieler Sustain - Potenzielles Risiko des Spielers %}

| Unterkategorie | Beispiel | Datentyp |
| ------- | ----------- |----------- |
| Risiko-Score | 0.5| Nummer |
| Riskanter Spieler | Wahr | Boolesch |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}
