---
nav_title: Future Anthem
article_title: Future Anthem
description: "Erfahren Sie, wie Sie Future Anthem in Braze integrieren können."
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# Future Anthem

> Das All-in-One-Produkt von Future Anthem für die Echtgeldspielbranche, Amplifier KI, stellt Personalisierung von Inhalten, Realtime-Erlebnisse und dynamische Zielgruppen zu. Amplifier AI funktioniert nahtlos in den Bereichen Sport, Casino und Lotterie und erlaubt es Kunden, die Profile von Braze-Spielern um branchenspezifische Attribute zu erweitern, wie z.B. Lieblingsspiel, Lieblingsteam, Engagement-Score, Empfehlung für die nächste Wette, erwartete nächste Wette und mehr.

{% alert important %}
Dieses Feature befindet sich derzeit im Early Access. Bitte wenden Sie sich an das Future Anthem Customer Success Team, um den Anfang zu machen.
{% endalert %}

## Voraussetzungen

| Anforderung              | Beschreibung                                            |
|--------------------------|--------------------------------------------------------|
| Zukünftiges Anthem-Konto    | Ein Konto von Future Anthem. |
| Braze REST API-Schlüssel       | Ein Braze REST API-Schlüssel mit dem [`users.track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt      | Der Braze [REST Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), der zu Ihrer Instanz passt, z.B. `rest.iad-01.com`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Mit dieser Integration können Sie:

- Identifizieren Sie Nutzer:innen mit hohem Engagement und Targeting mit personalisierten Angeboten, wie z.B. exklusiven Aktionen oder VIP Rewards.
- Schlagen Sie einem Nutzer:in ähnliche Spiele vor, basierend auf den Spielen, die er bereits mag.

## Integration

Das Future Anthem Customer Success Team wird Ihnen bei der Einrichtung Ihrer Integration helfen. Wenden Sie sich an Ihren Ansprechpartner bei Customer Success. Er wird Ihnen dabei helfen, die wichtigsten Attribute zu ermitteln, die Sie an Braze senden können.

|Beispiel-Attribute in Future Anthem|Beispiel-Attribute in Braze|
|-----------------------------------|---------------------------|
|![Die Attribute im Profil des Nutzers.]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %})|![Das Attribut des Objekts.]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %})|

## Angepasste Attribute brechen

Dies sind die verfügbaren angepassten Attribute von Braze. Ausführlichere Informationen finden Sie unter [Future Anthem: Erste Schritte](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab Wett-Empfehlungen %}

| Unterkategorie | Beispiel (JSON) | Datentyp |
| ------- | ----------- |----------- |
| Nutzer:in Präferenzen | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| Objekt |
| Empfehlungen für Einzelwetten | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| Objekt |
| Akkumulator-Wettempfehlungen | `{"Bet_1": "Halland Goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}`| Objekt |
| Akkumulator-Wettempfehlungen | `{"Bet_1": 1.5, "Bet_2": 2}` | Objekt |
| Bet Builder Wett-Empfehlungen | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahwaks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}`| Objekt |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Bonus-Empfehlungen %}

| Unterkategorie | Beispiel | Datentyp |
| ------- | ----------- |----------- |
|NGR - Nettospielertrag für die Lifetime der Nutzer:innen | 2232| Zahl|
| NGR14 - Nettospielertrag für die letzten 14 Tage der Aktivität | 42 | Zahl
| Gewinne der Spieler| 130 | Zahl |
| Engagement Score | 0.78 | Zahl |
| Abwanderungsrisiko-Score | 0.02 | Zahl |
| Geschätztes nächstes Wettdatum | 2024-08-29 | Uhrzeit |
| Bet and Get - Bonuswert-Empfehlung | 20 | Zahl |
| Weitere Empfehlungen für Bonuswerte in der Zukunft | 0 | Zahl |
| Zukunft CLTV  | 3126 | Zahl |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Spiel-Empfehlungen %}

| Unterkategorie | Beispiel | Datentyp |
| ------- | ----------- |----------- |
| Für Sie empfohlen | Fluffy Favourites, Fishin' Frenzy, Big Bass Bonanza, Rainbow Gold, Wild West| Array |
| Lieblingsspiele | Fischerei-Raserei | Array |
| Empfohlene neue Spiele | Sticky Bees, Beware the Deep Megaways, Gold Party, The Flintstones| Array |
| Spieler wie Sie spielen (kollaboratives Filtern) |Gold Blitz, Big Bass Splash, Rick and Morty, Book of Dead, Gates of Olympus, Luck O' the Irish | Array |
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
| Risiko-Score | 0.5| Zahl |
| Riskanter Spieler | Wahr | Boolesch |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}
