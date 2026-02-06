---
nav_title: Liquid Bibliothek für Anwendungsfälle
article_title: Bibliothek für Liquid-Anwendungsfälle
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "Auf dieser Landing Page finden Sie Beispiele für Liquid-Anwendungen, die nach Kategorien geordnet sind, z. B. Jahrestage, App-Nutzung, Countdowns und mehr."

---

{% api %}

## Jahrestage und Feiertage

{% apitags %}
Jahrestage und Feiertage
{% endapitags %}

- [Nachrichten basierend auf dem Jubiläumsjahr eines Nutzers bzw. einer Nutzerin personalisieren](#anniversary-year)
- [Nachrichten basierend auf der Geburtstagswoche eines Nutzers bzw. einer Nutzerin personalisieren](#birthday-week)
- [Kampagnen an Nutzer:innen in deren Geburtstagsmonat senden](#birthday-month)
- [Vermeiden Sie den Versand von Nachrichten an wichtigen Feiertagen](#holiday-avoid)

### Personalisieren Sie Nachrichten basierend auf dem Jubiläumsjahr eines Benutzers {#anniversary-year}

Dieser Anwendungsfall zeigt, wie man das App-Jubiläum eines Benutzers auf der Grundlage seines Erstanmeldedatums berechnet und je nach dem, wie viele Jahre er feiert, unterschiedliche Nachrichten anzeigt.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %} 
{% assign this_day = 'now' | date: "%d" %}
{% assign anniversary_month = {{custom_attribute.${registration_date}}} | date: "%B" %}
{% assign anniversary_day = {{custom_attribute.${registration_date}}} | date: "%d" %}
{% assign anniversary_year = {{custom_attribute.${registration_date}}} | date: "%Y" %}

{% if this_month == anniversary_month %} 
{% if this_day == anniversary_day %} 
{% if anniversary_year == '2021' %}
Exactly one year ago today we met for the first time!

{% elsif anniversary_year == '2020' %}
Exactly two years ago today we met for the first time!

{% elsif anniversary_year == '2019' %}
Exactly three years ago today we met for the first time!

{% else %}
{% abort_message("Not same year") %}
{% endif %}

{% else %} 
{% abort_message("Not same day") %} 
{% endif %}

{% else %}
{% abort_message("Not same month") %}
{% endif %}
```
{% endraw %}

**Erläuterung:** Hier verwenden wir die reservierte Variable `now`, um das aktuelle Datum und die Uhrzeit im [ISO 8601-Format](http://en.wikipedia.org/wiki/ISO_8601) als Template einzugeben. Die Filter `%B` (Monat wie „Mai“) und `%d` (Tag wie „18“) formatieren den aktuellen Monat und Tag. Anschließend verwenden wir dieselben Datums- und Zeitfilter für die Werte von `signup_date`, um sicherzustellen, dass wir die beiden Werte mithilfe von bedingten Tags und Logik vergleichen können.

Dann wiederholen wir drei weitere Variablenanweisungen, um `%B` und `%d` das `signup_date` zu erhalten, fügen aber auch `%Y` (Jahr wie „2021“) hinzu. Damit wird das Datum und die Uhrzeit von `signup_date` zu einer Jahreszahl. Wenn wir den Tag und den Monat kennen, können wir überprüfen, ob der Benutzer heute seinen Jahrestag hat, und wenn wir das Jahr kennen, wissen wir, wie viele Jahre es her ist - und damit auch, zu wie vielen Jahren wir gratulieren können!

{% alert tip %} Je nachdem, wie viele Jahre Sie bereits sammeln, können Sie so viele Bedingungen erstellen wie es Anmeldedaten gibt. {% endalert %}  

### Personalisieren Sie Nachrichten basierend auf der Geburtstagswoche eines Benutzers {#birthday-week}

Dieser Anwendungsfall zeigt, wie Sie den Geburtstag eines Benutzers ermitteln, ihn mit dem aktuellen Datum vergleichen und dann spezielle Geburtstagsnachrichten vor, während und nach der Geburtstagswoche anzeigen.

{% raw %}
```liquid
{% assign this_week = 'now' | date: '%W' %}
{% assign birthday_week = ${date_of_birth}  | date: '%W' %}
{% assign last_week = {{this_week}} | minus: 1 %}
{% assign next_week = {{this_week}} | plus: 1 %}
{% assign birthday_week_conversion = {{birthday_week}} | plus: 0 %}
{% if {{last_week}} == {{birthday_week_conversion}} %}
Happy birthday for last week!
{% elsif {{birthday_week}} == {{this_week}} %}
Happy birthday for this week!
{% elsif {{next_week}} == {{birthday_week_conversion}} %}
Happy birthday for next week!
{% else %}
No birthday for you!
{% endif %}
```
{% endraw %}

**Erläuterung:** Ähnlich wie im Anwendungsfall [Jahrestag](#anniversary-year) nehmen wir hier die reservierte Variable `now` und verwenden den Filter `%W` (Woche, z.B. Woche 12 von 52 in einem Jahr), um die Nummer der Woche des Jahres zu erhalten, in die der Geburtstag des Benutzers fällt. Wenn die Geburtstagswoche des Benutzers mit der aktuellen Woche übereinstimmt, schicken wir ihm eine Glückwunschnachricht! 

Wir fügen auch Anweisungen für `last_week` und `next_week` hinzu, um Ihr Messaging noch persönlicher zu gestalten.

### Senden Sie Kampagnen an Benutzer in deren Geburtstagsmonat {#birthday-month}

Dieser Anwendungsfall zeigt, wie Sie den Geburtstagsmonat eines Nutzers oder einer Nutzerin berechnen, ob sein oder ihr Geburtstag in den aktuellen Monat fällt und wenn ja, eine spezielle Nachricht gesendet wird.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
Message body 
{% else %} 
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

**Erläuterung:** Ähnlich wie beim Anwendungsfall [Geburtstagswoche](#birthday-week), nur dass wir hier den Filter `%B` (Monat wie "Mai") verwenden, um zu berechnen, welche Benutzer in diesem Monat Geburtstag haben. Eine mögliche Anwendung könnte darin bestehen, Geburtstagskinder in einer monatlichen E-Mail anzusprechen.

### Vermeiden Sie den Versand von Nachrichten an wichtigen Feiertagen {#holiday-avoid}

Dieser Anwendungsfall zeigt, wie Sie während der Ferienzeit Nachrichten versenden und dabei die Tage der großen Ferien vermeiden können, an denen das Engagement wahrscheinlich gering ist.

{% raw %}
```liquid
{% assign today = 'now' | date: '%Y-%m-%d' %}
{% if today == "2023-12-24" or today == "2023-12-25" or today == "2023-12-26" %}
{% abort_message %}
{% else %}
Message if today isn't one of the provided holidays.
{% endif %}
```
{% endraw %}

**Erläuterung:** Hier weisen wir den Term `today` der reservierten Variablen `now` (das aktuelle Datum und die Uhrzeit) zu und verwenden die Filter `%Y` (Jahr wie "2023"), `%m` (Monat wie "12") und `%d` (Tag wie "25"), um das Datum zu formatieren. Wir führen dann unsere bedingte Anweisung aus, die besagt, dass die Nachricht abgebrochen wird, wenn die Variable `today` mit den von Ihnen gewählten Feiertagen übereinstimmt. 

Das angegebene Beispiel bezieht sich auf Heiligabend, den ersten Weihnachtsfeiertag und den zweiten Weihnachtsfeiertag (den Tag nach Weihnachten).

{% endapi %}

{% api %}

## App-Nutzung

{% apitags %}
App-Nutzung
{% endapitags %}

- [Senden Sie Nachrichten in der Sprache eines Benutzers, wenn dieser eine Sitzung angemeldet hat](#app-session-language)
- [Personalisieren Sie Nachrichten basierend darauf, wann ein Benutzer die App zuletzt geöffnet hat](#app-last-opened)
- [Eine andere Nachricht anzeigen, wenn ein Nutzer oder eine Nutzerin die App zuletzt vor weniger als drei Tagen verwendet hat](#app-last-opened-less-than)

### Senden Sie Nachrichten in der Sprache eines Benutzers, wenn dieser keine Sitzung angemeldet hat {#app-session-language}

Dieser Anwendungsfall prüft, ob ein Benutzer eine Sitzung protokolliert hat, und falls nicht, enthält er eine Logik zur Anzeige einer Nachricht auf der Grundlage der Sprache, die über ein benutzerdefiniertes Attribut manuell erfasst wurde. Wenn keine Sprachinformationen mit ihrem Konto verknüpft sind, wird die Nachricht in der Standardsprache angezeigt. Wenn ein Nutzer oder eine Nutzerin eine Sitzung angemeldet hat, werden alle mit dem Nutzer oder Nutzerin verbundenen Sprachinformationen abgerufen und die entsprechende Nachricht angezeigt. 

{% raw %}
```liquid
{% if {{${last_used_app_date}}} == nil %}
{% if {{custom_attribute.${user_language}}} == 'en' %}
Message in English based on custom attribute
{% elsif {{custom_attribute.${user_language}}} == 'fr' %}
Message in French based on custom attribute
{% else %}
Does not have language - Default language
{% endif %}
{% else %}
{% if ${language} == 'en' %}
Message in English based on Language
{% elsif ${language} == 'fr' %}
Message in French based on Language
{% else %}
Has language - Default language
{% endif %}
{% endif %}
```
{% endraw %}

{% raw %}
**Erläuterung:** Hier verwenden wir zwei gruppierte `if`-Anweisungen, die ineinander verschachtelt sind. Die erste `if`-Anweisung prüft, ob der Nutzer oder die Nutzerin eine Sitzung gestartet hat, indem überprüft wird, ob es sich bei `last_used_app_date` um `nil` handelt. Das liegt daran, dass `{{${language}}}` automatisch vom SDK erfasst wird, wenn ein Nutzer oder eine Nutzerin eine Sitzung anmeldet. Wenn der Benutzer noch keine Sitzung angemeldet hat, kennen wir seine Sprache noch nicht. Daher wird geprüft, ob sprachbezogene benutzerdefinierte Attribute gespeichert wurden, und auf der Grundlage dieser Informationen wird eine Nachricht in dieser Sprache angezeigt, falls möglich.
{% endraw %}

Die zweite `if`-Anweisung sucht nur nach dem Standardattribut (Standard), da der Nutzer oder die Nutzerin nicht über `nil` für `last_used_app_date` verfügt. Das bedeutet, dass eine Sitzung angemeldet wurde und wir die Sprache des Nutzers oder der Nutzerin kennen.

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) ist eine reservierte Variable, die zurückgegeben wird, wenn Liquid-Code keine Ergebnisse liefert. `Nil` wird wie `false` in einem `if` Block behandelt.
{% endalert %}

### Personalisieren Sie Nachrichten basierend darauf, wann ein Benutzer die App zuletzt geöffnet hat {#app-last-opened}

Dieser Anwendungsfall berechnet, wann ein Benutzer Ihre App das letzte Mal geöffnet hat, und zeigt je nach Zeitdauer eine andere personalisierte Nachricht an.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while; here are some of our latest updates.
{% endif %}
```
{% endraw %}

### Eine andere Nachricht anzeigen, wenn ein Nutzer oder eine Nutzerin die App zuletzt vor weniger als drei Tagen verwendet hat {#app-last-opened-less-than}

Dieser Anwendungsfall berechnet, wie lange es her ist, dass ein Benutzer Ihre App verwendet hat, und zeigt je nach Zeitdauer eine andere personalisierte Nachricht an.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Message for a recently active user
{% else %}
Message for a less active user
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Countdowns

{% apitags %}
Countdowns
{% endapitags %}

- [X Tage zum heutigen Datum hinzufügen](#countdown-add-x-days)
- [Einen Countdown ab einem bestimmten Zeitpunkt berechnen](#countdown-difference-days)
- [Einen Countdown für bestimmte Versanddaten und Prioritäten erstellen](#countdown-shipping-options)
- [Erstellen Sie einen Countdown in Tagen](#countdown-days)
- [Erstellen Sie einen Countdown von Tagen, Stunden und Minuten](#countdown-dynamic)
- [Anzeigen, wie viele Tage bis zu einem bestimmten Datum verbleiben](#countdown-future-date)
- [Zeigt an, wie viele Tage bis zum Eintreffen eines benutzerdefinierten Datumsattributs verbleiben](#countdown-custom-date-attribute)
- [Anzeigen, wie viel Zeit noch verbleibt, und Abbruch der Nachricht, wenn nur noch X Zeit verbleibt](#countdown-abort-window)
- [In-App-Nachricht, die X Tage vor dem Ende der Mitgliedschaft des Nutzers oder der Nutzerin gesendet wird](#countdown-membership-expiry)
- [Personalisieren Sie In-App-Nachrichten basierend auf dem Datum und der Sprache des Benutzers](#countdown-personalize-language)
- [Template für das Datum in 30 Tagen ab jetzt, formatiert als Monat und Tag](#countdown-template-date)

### x Tage zum heutigen Datum hinzufügen{#countdown-add-x-days}

Dieser Anwendungsfall fügt dem aktuellen Datum eine bestimmte Anzahl von Tagen hinzu, um darauf Bezug zu nehmen und Nachrichten hinzuzufügen. So können Sie z.B. eine Nachricht zur Wochenmitte senden, in der Sie auf Veranstaltungen in der Umgebung am Wochenende hinweisen.

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

Der Wert `plus` wird immer in Sekunden angegeben, so dass wir den Filter `%F` verwenden, um die Sekunden in Tage umzurechnen.

{% alert important %}
Sie können in Ihrer Nachricht eine URL oder einen Deeplink zu einer Liste von Events einfügen, damit Sie den Nutzer oder die Nutzerin zu einer Liste von Aktionen weiterleiten können, die in Zukunft stattfinden.
{% endalert %}

### Berechnen eines Countdowns ab einem bestimmten Zeitpunkt {#countdown-difference-days}

In diesem Anwendungsfall wird die Differenz in Tagen zwischen einem bestimmten Datum und dem aktuellen Datum berechnet. Dieser Unterschied kann verwendet werden, um Ihren Benutzern einen Countdown anzuzeigen.

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### Einen Countdown für bestimmte Versanddaten und Prioritäten erstellen

In diesem Anwendungsfall werden verschiedene Versandoptionen erfasst, die Dauer der Zustellung berechnet und Nachrichten angezeigt, die den Benutzer ermutigen, rechtzeitig zu kaufen, um sein Paket bis zu einem bestimmten Datum zu erhalten.

{% raw %}
```liquid
{% assign standard_shipping_start = "2023-12-10T00:00-05:00" | date: "%s" %}
{% assign standard_shipping_end = "2023-12-20T13:00-05:00" | date: "%s" %}
{% assign express_shipping_end = "2023-12-22T24:00-05:00" | date: "%s" %}
{% assign overnight_shipping_end = "2023-12-23T24:00-05:00" | date: "%s" %}
{% assign today = 'now' | date: "%s" %}

{% assign difference_s = standard_shipping_end | minus: today %}
{% assign difference_s_days = difference_s | divided_by: 86400.00 | round %}
{% assign difference_e = express_shipping_end | minus: today %}
{% assign difference_e_days = difference_e | divided_by: 86400.00 | round %}
{% assign difference_o = overnight_shipping_end | minus: today %}
{% assign difference_o_days = difference | divided_by: 86400.00 | round %}

{% if today >= standard_shipping_start and today <= standard_shipping_end %}
{% if difference_s_days == 0 %}
This is the last day to order with standard shipping, so your order gets here on time for Christmas Eve!
{% elsif difference_s_days == 1 %}
There is {{difference_s_days}} day left to order with standard shipping, so your order gets here on time for Christmas Eve!

{% else %}
There are {{difference_s_days}} days left to order with standard shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today > standard_shipping_end and today < express_shipping_end %}
{% if difference_e_days == 1 %}
There is {{difference_e_days}} day left to order with express shipping, so your order gets here on time for Christmas Eve!
{% else %}
There are {{difference_e_days}} days left to order with express shipping so your order gets here on time for Christmas Eve!
{% endif %}
{% elsif today >= express_shipping_end and today < overnight_shipping_end %}
This is the last day for overnight shipping so your order gets here on time for Christmas Eve!
{% else %}
{% abort_message("Unable to order and ship in time") %}
{% endif %}
```
{% endraw %}

### Einen Countdown in Tagen erstellten {#countdown-days}

Dieser Anwendungsfall berechnet die verbleibende Zeit zwischen einem bestimmten Ereignis und dem aktuellen Datum und zeigt an, wie viele Tage bis zum Ereignis verbleiben.

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${last_selected_event_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Your order will arrive in {{ difference_days }} days!
```
{% endraw %}

{% alert important %}
Sie benötigen ein benutzerdefiniertes Attributfeld mit einem `date` Wert.
{% endalert %}

### Erstellen Sie einen Countdown von Tagen, Stunden und Minuten {#countdown-dynamic}

In diesem Anwendungsfall wird die verbleibende Zeit zwischen einem bestimmten Ereignis und dem aktuellen Datum berechnet. Je nach verbleibender Zeit bis zum Event ändert sich der Zeitwert (Tage, Stunden, Minuten), um verschiedene personalisierte Nachrichten anzuzeigen.

Wenn beispielsweise die Bestellung eines Kunden oder einer Kundin in zwei Tagen eintrifft, könnten Sie sagen: „Ihre Bestellung trifft in zwei Tagen ein.“ Wenn es hingegen weniger als einen Tag ist, könnten Sie es in "Ihre Bestellung wird in 17 Stunden eintreffen" ändern.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign scheme_finish = "2017-10-13T10:30:30" | date: "%s" %}
{% assign difference_seconds =  scheme_finish | minus: today %}
{% assign difference_minutes = difference_seconds | divided_by: 60 %}
{% assign difference_hours = difference_seconds | divided_by: 3600 %}
{% assign difference_days = difference_seconds | divided_by: 86400 %}
{% if {{difference_minutes}} > 59 and {{difference_minutes}} < 1440 %}
You have {{difference_hours}} hours left till your order arrives!
{% elsif {{difference_minutes}} < 59 %}
You have {{difference_minutes}} minutes left till your order arrives!
{% else %}
You have {{difference_days}} days left till your order arrives!
{% endif %}
```
{% endraw %}

{% alert important %}
Sie benötigen ein benutzerdefiniertes Attributfeld mit einem `date` Wert. Sie müssen auch Zeitschwellen festlegen, wann die Zeit in Tagen, Stunden und Minuten angezeigt werden soll.
{% endalert %}

### Anzeigen, wie viele Tage bis zu einem bestimmten Datum verbleiben {#countdown-future-date}

In diesem Anwendungsfall wird die Differenz zwischen dem aktuellen Datum und dem zukünftigen Ereignisdatum berechnet und eine Meldung angezeigt, die angibt, wie viele Tage es noch bis zum Ereignis sind.

{% raw %}
```liquid
{% assign event_date = '2024-01-15' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
There are {{difference_days}} days until your birthday!
```
{% endraw %}

### Anzeigen, wie viele Tage noch bis zum Eintreffen eines nutzerdefinierten Datumsattributs verbleiben {#countdown-custom-date-attribute}

Dieser Anwendungsfall berechnet die Differenz in Tagen zwischen dem aktuellen und dem zukünftigen Datum und zeigt eine Meldung an, wenn die Differenz mit einer bestimmten Zahl übereinstimmt.

In diesem Beispiel erhält ein Benutzer innerhalb von zwei Tagen nach dem benutzerdefinierten Datumsattribut eine Nachricht. Andernfalls wird die Nachricht nicht gesendet.

{% raw %}
```liquid
{% assign today = 'now' | date: '%j' | plus: 0 %}
{% assign surgery_date = {{custom_attribute.${surgery_date}}} | date: '%j' | plus: 0 %}

{% assign difference_days = {{surgery_date}} | minus: {{today}} %}
{% if difference_days == 2 %}
Your surgery is in 2 days on {{custom_attribute.${surgery_date}}}
{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Anzeigen, wie viel Zeit noch verbleibt, und Abbruch der Nachricht, wenn nur noch X Zeit verbleibt {#countdown-abort-window}

In diesem Anwendungsfall wird berechnet, wie lange es noch bis zu einem bestimmten Datum dauert, und je nach Länge werden verschiedene personalisierte Nachrichten angezeigt (wobei die Nachrichten übersprungen werden, wenn das Datum zu früh ist). 

Zum Beispiel: "Sie haben noch x Stunden Zeit, um Ihr Ticket nach London zu kaufen", aber senden Sie die Nachricht nicht, wenn die Flugzeit nach London weniger als zwei Stunden beträgt.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} < 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours!
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now!
{% endif %}
```
{% endraw %}

{% alert important %} Sie benötigen eine Eigenschaft für ein angepasstes Event. {% endalert %}

### In-App-Nachricht, die x Tage vor dem Ende der Mitgliedschaft gesendet wird {#countdown-membership-expiry}

Dieser Anwendungsfall erfasst das Ablaufdatum Ihrer Mitgliedschaft, berechnet, wie lange es noch dauert, bis sie abläuft, und zeigt je nachdem, wie lange es noch dauert, verschiedene Nachrichten an.

{% raw %}
```liquid
{% assign membership_expiry = {{custom_attribute.${membership_expiry_date}}} | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = membership_expiry | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}

{% if difference_days > 4 and difference_days <= 7 %}
You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days > 2 and difference_days <= 4 %}
HURRY! You have {{difference_days}} days left in your trial, make sure you upgrade!

{% elsif difference_days == 2 %}
LAST CHANCE! You have {{difference_days}} days left in your trial. Make sure you upgrade!

{% else %}
You have few days left in your trial. Make sure to upgrade!
{% endif %}
```
{% endraw %}

### Personalisieren Sie In-App-Nachrichten basierend auf dem Datum und der Sprache des Benutzers {#countdown-personalize-language}

Dieser Anwendungsfall berechnet einen Countdown bis zu einem Ereignis und zeigt den Countdown auf der Grundlage der Spracheinstellung des Benutzers in dessen Sprache an.

Sie könnten zum Beispiel einmal im Monat eine Reihe von Upsell-Nachrichten an die Nutzer senden, um sie mit vier In-App-Nachrichten darüber zu informieren, wie lange ein Angebot noch gültig ist:

- Ursprünglich
- Noch 2 Tage
- 1 Tag übrig
- Letzter Tag

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign end_date = "2021-04-16T23:59:59" | date: "%s" %}
{% assign difference = end_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
{% if {{difference_days}} >= 3 %}
{% if ${language} == 'de' %}

Hallo, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'ch' %}
Grüezi, das Angebot gilt bis zum 16.04.

{% elsif ${language} == 'en' %}
The offer is valid until 16.04.

{% else %}
The offer is valid until 16.04.

{% endif %}
{% elsif {{difference_days}} == 2 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 1 %}
{% if ${language} == 'de' %}
INSERT MESSAGE

{% elsif ${language} == 'ch' %}
INSERT MESSAGE

{% elsif ${language} == 'en' %}
INSERT MESSAGE

{% else %}
INSERT MESSAGE
{% endif %}

{% elsif {{difference_days}} == 0 %}
{% if ${language} == 'de' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'ch' %}
Hallo, das Angebot gilt noch heute.

{% elsif ${language} == 'en' %}
Grüezi, das Angebot gilt noch heute.

{% else %}
Hi, the offer is only valid today.
{% endif %}

{% else %}
{% abort_message("Calculation failed") %}
{% endif %}
```
{% endraw %}

{% alert important %}
Sie müssen einen `date`-Wert zuweisen und eine Abbruchlogik einbauen, wenn das angegebene Datum außerhalb des Datumsbereichs liegt. Für taggenaue Berechnungen muss das zugewiesene Enddatum 23:59:59 beinhalten.
{% endalert %}

### Template für das Datum in 30 Tagen ab jetzt, formatiert als Monat und Tag {#countdown-template-date}

In diesem Anwendungsfall wird das Datum in 30 Tagen angezeigt, das Sie in Ihren Nachrichten verwenden können.

{% raw %}
```liquid
{% assign today = 'now' | date: "%s" %}
{% assign thirty_days = today | plus: 2592000 | date: "%B %d" %}
```
{% endraw %}

{% endapi %}

{% api %}

## Angepasstes Attribut

{% apitags %}
Angepasstes Attribut
{% endapitags %}

- [Personalisieren Sie eine Nachricht auf der Grundlage passender benutzerdefinierter Attribute](#attribute-matching)
- [Subtrahieren Sie zwei benutzerdefinierte Attribute, um die Differenz als Geldwert anzuzeigen](#attribute-monetary-difference)
- [Den Vornamen eines Nutzers:innen referenzieren, wenn der vollständige Name im Feld first_name gespeichert ist](#attribute-first-name)

### Personalisieren Sie eine Nachricht auf der Grundlage passender benutzerdefinierter Attribute {#attribute-matching}

Dieser Anwendungsfall prüft, ob ein Benutzer über bestimmte benutzerdefinierte Attribute verfügt, und wenn ja, werden verschiedene personalisierte Nachrichten angezeigt. 

{% raw %}
```liquid
{% if custom_attribute.${hasShovel} == true and custom_attribute.${VisitToGroundTooTough} > 0 %}
The ground is very hard. The dirt road goes East.
{% elsif custom_attribute.${hasShovel} == true %}
The dirt road goes East.
{% elsif custom_attribute.${VisitToStart} > 0 %}
The dirt road goes East.
The shovel here.
{% else %}
You are at a dead-end of a dirt road. The road goes to the east. In the distance, you can see that it will eventually fork off. The trees here are very tall royal palms, and they are spaced equidistant from each other.
There is a shovel here.
{% endif %}
```
{% endraw %}

### Zwei angepasste Attribute subtrahieren, um die Differenz als Geldwert anzuzeigen {#attribute-monetary-difference}

Dieser Anwendungsfall erfasst zwei benutzerdefinierte monetäre Attribute, berechnet dann die Differenz und zeigt sie an, damit die Benutzer wissen, wie weit sie noch von ihrem Ziel entfernt sind.

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### Den Vornamen eines Nutzers:innen referenzieren, wenn der vollständige Name im Feld first_name gespeichert ist {#attribute-first-name}

Dieser Anwendungsfall erfasst den Vornamen eines Benutzers (wenn sowohl Vor- als auch Nachname in einem einzigen Feld gespeichert sind) und verwendet dann diesen Vornamen, um eine Willkommensnachricht anzuzeigen.

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**Erläuterung:** Der Filter `split` verwandelt die Zeichenkette in `{{${first_name}}}` in ein Array. Durch die Verwendung von `{{name[0]}}` verweisen wir dann nur auf das erste Element im Array, nämlich den Vornamen des Nutzers oder der Nutzerin. 

{% endraw %}
{% endapi %}

{% api %}

## Angepasstes Event

{% apitags %}
Angepasstes Event
{% endapitags %}

- [Push-Benachrichtigung abbrechen, wenn ein angepasstes Event innerhalb von zwei Stunden ab jetzt stattfindet](#event-abort-push)
- [Jedes Mal eine Kampagne senden, wenn ein Nutzer oder eine Nutzerin ein angepasstes Event dreimal ausführt](#event-three-times)
- [Senden Sie eine Nachricht an Benutzer, die nur in einer Kategorie gekauft haben](#event-purchased-one-category)
- [Verfolgen, wie oft ein angepasstes Event im vergangenen Monat aufgetreten ist](#track)


### Abbruch der Push-Benachrichtigung, wenn ein benutzerdefiniertes Ereignis innerhalb der nächsten zwei Stunden eintritt {#event-abort-push}

Dieser Anwendungsfall berechnet die Zeit bis zu einem Ereignis und zeigt je nach der verbleibenden Zeit verschiedene personalisierte Nachrichten an.

So können Sie beispielsweise verhindern, dass eine Push-Mitteilung versendet wird, wenn eine benutzerdefinierte Ereigniseigenschaft in den nächsten zwei Stunden abläuft. Dieses Beispiel verwendet das Szenario eines verlassenen Wagens für ein Zugticket.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
{% assign dep_time = {{event_properties.${outboundDate_Time}}} | date: "%s" %}
{% assign time_to_dep = dep_time | minus: today %}
{% if {{time_to_dep}} <= 7200 %}
{% abort_message("OutboundDate less than 2 hours") %}
{% elsif {{time_to_dep}} > 7200 and {{time_to_dep}} < 86400 %}
Don't forget to buy your ticket to {{event_properties.${toStation}}} within next 24 hours
{% else %}
Still traveling to {{event_properties.${toStation}}} in more than 24 hours? Book now
{% endif %}
```
{% endraw %}

### Jedes Mal eine Kampagne senden, wenn ein Nutzer oder eine Nutzerin ein angepasstes Event dreimal ausführt

Dieser Anwendungsfall prüft, ob ein Benutzer ein benutzerdefiniertes Ereignis dreimal ausgeführt hat, und wenn ja, wird eine Nachricht angezeigt oder eine Kampagne gesendet. 

{% raw %}
```liquid
{% assign cadence = custom_attribute.${example} | minus: 1 | modulo: 3 %}
{% if custom_attribute.${example} == blank %}
{% abort_message("Error calculating cadence") %}
{% elsif cadence != 0 %}
{% abort_message("Skip message") %}
{% endif %}
Did you forget something in your shopping cart?
```
{% endraw %}

{% alert important %} Sie müssen über eine Event-Eigenschaft des Zählers für angepasste Events verfügen oder einen Webhook für Ihren Braze-Endpunkt verwenden. Damit wird ein angepasstes Attribut (`example_event_count`) jedes Mal inkrementiert, wenn der Nutzer oder die Nutzerin das Ereignis ausführt. In diesem Beispiel wird eine Dreierkadenz verwendet (1, 4, 7, 10, usw.). Um die Kadenz bei Null zu beginnen (0, 3, 6, 9, usw.), entfernen Sie `minus: 1`.
{% endalert %}

### Senden Sie eine Nachricht an Benutzer, die nur in einer Kategorie gekauft haben {#event-purchased-one-category}

Dieser Anwendungsfall erfasst eine Liste der Kategorien, in denen ein Benutzer eingekauft hat, und wenn nur eine Kaufkategorie vorhanden ist, wird eine Meldung angezeigt.

{% raw %}
```liquid
{% assign category = {{custom_attribute.${categories_purchased}}} %}
{% assign uniq_cat = {{category | uniq }} %}
{% if {{uniq_cat | size}} == 1%}
{{uniq_cat}}
{% else %}
{% abort_message("Purchase category doesn't exist") %}
{% endif %}
```
{% endraw %}

### Verfolgen, wie oft ein angepasstes Event im vergangenen Monat aufgetreten ist {#track}

In diesem Anwendungsfall wird berechnet, wie oft ein benutzerdefiniertes Ereignis zwischen dem 1\. des aktuellen Monats und dem Vormonat protokolliert wurde. Sie können dann einen users/track-Aufruf ausführen, um diesen Wert als angepasstes Attribut zu speichern. Beachten Sie, dass diese Kampagne zwei aufeinanderfolgende Monate laufen muss, bevor die monatlichen Daten verwendet werden können.

{% raw %}
```liquid

{% capture body %}
{
 "braze_id": "{{${braze_id}}}",
 "fields_to_export": ["custom_events"]
}

{% endcapture %}

{% connected_content YOUR_BRAZE_ENDPOINT/users/export/ids
 :method post
  :headers { "Authorization": "Bearer YOUR_API_KEY" }
  :body {{body}}
 :content_type application/json
 :save response
  :retry %}

{% for custom_event in response.users[0].custom_events %}
{% assign ce_name = custom_event.name %}
{% comment %} The following custom event name will need to be amended for the target custom event. {% endcomment %}

{% if ce_name == "Project Exported" %}
{% comment %}{{custom_event.name}}: {{custom_event.count}}{% endcomment %}
{% assign current_count = custom_event.count %}
{% endif %}
{% endfor %}

{% assign prev_month_count = {{custom_attribute.${projects_exported_prev_month}}} %}
{% assign latest_count = current_count | minus: prev_month_count %}
{% assign now = "now" | date: "%s" %}
{% assign yesterday = {{now}} | minus: 86400 %}
{% assign previous_month = {{yesterday}} | date: "%B" %}
{% assign previous_year = {{yesterday}} | date: "%y" %}
{% assign formatted_month = previous_month | downcase %}
{% comment %}The Custom Event name that is being tracked will be needed to be amended for the target Custom Event in the Attribute Name below. {% endcomment %}
```

```json
"attributes": [
  {
    "external_id":"{{${user_id}}}",
       "projects_exported_{{formatted_month}}_{{previous_year}}": "{{latest_count}}"
  }
]
```

{% endraw %}

{% endapi %}

{% api %}

## Sprache

{% apitags %}
Sprache
{% endapitags %}

- [Monatsnamen in einer anderen Sprache anzeigen](#language-display-month)
- [Bild basierend auf der Sprache des Nutzers oder der Nutzerin anzeigen](#language-image-display)
- [Nachrichten basierend auf dem Wochentag und der Sprache des Nutzers oder der Nutzerin personalisieren](#language-personalize-message)

### Monatsnamen in einer anderen Sprache anzeigen {#language-display-month}

In diesem Anwendungsfall werden das aktuelle Datum, der Monat und das Jahr angezeigt, wobei der Monat in einer anderen Sprache erscheint. Das angegebene Beispiel verwendet Schwedisch.

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Januari {{year}}
{% elsif {{month)) == 'February' %}
{{day}} Februari {{year}}
{% elsif {{month)) == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month)) == 'April' %}
{{day}} April {{year}}
{% elsif {{month)) == 'May' %}
{{day}} Maj {{year}}
{% elsif {{month)) == 'June' %}
{{day}} Juni {{year}}
{% elsif {{month)) == 'July' %}
{{day}} Juli {{year}}
{% elsif {{month)) == 'August' %}
{{day}} Augusti {{year}}
{% elsif {{month)) == 'September' %}
{{day}} September {{year}}
{% elsif {{month)) == 'October' %}
{{day}} Oktober {{year}}
{% elsif {{month)) == 'November' %}
{{day}} November {{year}}
{% elsif {{month)) == 'December' %}
{{day}} December {{year}}
{% endif %}
```
{% endraw %}

### Ein Bild basierend auf der Sprache des Nutzers oder der Nutzerin anzeigen

In diesem Anwendungsfall wird ein Bild basierend auf der Sprache des Benutzers angezeigt. Beachten Sie, dass dieser Anwendungsfall nur mit Bildern getestet wurde, die in die Braze-Mediathek hochgeladen wurden.

{% raw %}
```liquid
{% if ${language} == 'en' %}
English image URL (for example, https://cdn-staging.braze.com/appboy/communication/assets/image_assets/images/60aecba96a93150c749b4d57/original.png?1622068137)
{% elsif ${language} == 'ru' %}
Russian image URL
{% elsif ${language} == 'es' %}
Spanish image URL
{% else %}
Fallback image URL
{% endif %}
```
{% endraw %}

### Nachrichten basierend auf dem Wochentag und der Sprache des Nutzers oder der Nutzerin personalisieren

Dieser Anwendungsfall prüft den aktuellen Wochentag und zeigt auf der Grundlage des Tages, wenn die Sprache des Benutzers auf eine der angebotenen Sprachoptionen eingestellt ist, eine bestimmte Nachricht in seiner Sprache an.

Das Beispiel endet am Dienstag, kann aber für jeden Tag der Woche wiederholt werden.

{% raw %}
```liquid
{% assign today  = 'now' | date: '%A' %}

{% if today == 'Monday' %}
{% if ${language} == 'es' %}
Compra hoy y lleva tu aprendizaje de idiomas a niveles más altos. 🚀

{% elsif ${language} == 'en' %}
Purchase today and take your language learning to the next level. 🚀

{% elsif ${language} == 'zh' %}
今天就购买并将您的语言提高到一个新水平吧。🚀

{% else %}
It's Monday, but the language doesn't match 
{% endif %}

{% elsif today == 'Tuesday' %}

{% if ${language} == 'zh' %}
不要忘记解锁以获取完整版本哦。🔓

{% elsif ${language} == 'en' %}
Don't forget to unlock the full version of your language. 🔓

{% elsif ${language} == 'ja' %}
すべての機能を使ってみませんか 🔓

{% elsif ${language} == 'es' %}
No te olivides de desbloquear la versión completa del programa de idiomas. 🔓

{% else %}
tuesday default
{% endif %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Verschiedenes

{% apitags %}
Verschiedenes
{% endapitags %}

- [Vermeiden Sie den Versand von E-Mails an Kunden, die Marketing-E-Mails blockiert haben](#misc-avoid-blocked-emails)
- [Den Abonnementstatus eines Kunden oder einer Kundin verwenden, um den Inhalt von Nachrichten zu personalisieren](#misc-personalize-content)
- [Den ersten Buchstaben eines jeden Wortes in einer Zeichenkette groß schreiben](#misc-capitalize-words-string)
- [Benutzerdefinierte Attributwerte mit einem Array vergleichen](#misc-compare-array)
- [Eine Erinnerung an ein bevorstehendes Event erstellen](#misc-event-reminder)
- [Suche nach einer Zeichenkette innerhalb eines Arrays](#misc-string-in-array)
- [Finden Sie den größten Wert in einem Array](#misc-largest-value)
- [Finden Sie den kleinsten Wert in einem Array](#misc-smallest-value)
- [Abfrage des Endes einer Zeichenkette](#misc-query-end-of-string)
- [Abfrage von Werten in einem Array aus einem benutzerdefinierten Attribut mit mehreren Kombinationen](#misc-query-array-values)
- [Eine Zeichenkette in eine Telefonnummer formatieren](#phone-number)

### Vermeiden Sie den Versand von E-Mails an Kunden, die Marketing-E-Mails blockiert haben {#misc-avoid-blocked-emails}

In diesem Anwendungsfall wird eine Liste gesperrter Nutzer:innen, die in einem Inhaltsblock gespeichert ist, verwendet, um zu überprüfen, ob diese gesperrten Nutzer:innen in kommenden Kampagnen oder Werbekampagnen nicht angesprochen oder angesprochen werden.

{% alert important %}
Um dieses Liquid zu verwenden, speichern Sie zunächst die Liste der blockierten E-Mails in einem Content-Block. Die Liste sollte keine zusätzlichen Leerzeichen oder Zeichen zwischen den E-Mail-Adressen enthalten (z. B. `test@braze.com,abc@braze.com`).
{% endalert %}

{% raw %}
```liquid
{% assign blocked_emails = {{content_blocks.${BlockedEmailList}}} | split: ',' %}
{% for email in blocked_emails %}
    {% if {{${email_address}}} == email %}
    {% abort_message("Email is blocked") %}
    {% break %}
    {% endif %}
{% endfor %} 
Your message here!
```
{% endraw %}

**Erläuterung:** Hier überprüfen wir, ob die E-Mail Ihres potenziellen Empfängers in dieser Liste enthalten ist, indem wir den Inhaltsblock der blockierten E-Mails abfragen. Wenn die E-Mail gefunden wird, wird die Nachricht nicht gesendet.

{% alert note %}
Content-Blöcke haben eine maximale Größe von 5 MB.
{% endalert %}

### Abonnementstatus eines Kunden oder einer Kundin verwenden, um den Inhalt von Nachrichten zu personalisieren {#misc-personalize-content}

Dieser Anwendungsfall verwendet den Abonnementstatus eines Kunden oder einer Kundin, um personalisierte Inhalte zu senden. Kunden oder Kundinnen, die eine bestimmte Abonnementgruppe abonniert haben, erhalten eine exklusive Nachricht für E-Mail-Abonnementgruppen.

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### Den ersten Buchstaben eines jeden Wortes in einer Zeichenkette groß schreiben {#misc-capitalize-words-string}

In diesem Anwendungsfall wird eine Zeichenkette von Wörtern in ein Array aufgeteilt und der erste Buchstabe jedes Wortes großgeschrieben.

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %} 
```
{% endraw %}

**Erläuterung:** Hier haben wir unserem gewählten String-Attribut eine Variable zugewiesen und den Filter `split` verwendet, um den String in ein Array aufzuteilen. Wir haben dann das Tag `for` verwendet, um die Variable `words` jedem der Elemente in unserem neu erstellten Array zuzuweisen, bevor wir diese Wörter mit dem Filter `capitalize` und dem Filter `append` anzeigen, um Leerzeichen zwischen den einzelnen Begriffen hinzuzufügen.

### Benutzerdefinierte Attributwerte mit einem Array vergleichen {#misc-compare-array}

In diesem Anwendungsfall wird eine Liste von Lieblingsgeschäften verwendet. Es wird geprüft, ob sich eines der Lieblingsgeschäfte des Benutzers in dieser Liste befindet, und wenn ja, wird ein Sonderangebot dieser Geschäfte angezeigt.

{% raw %}
```liquid
{% assign favorite_stores = 'Target,Walmart,Costco' | split: ',' %}
{% for store in favorite_stores %}
{% if {{custom_attribute.${favorited_stores}}} contains {{store}} %}
Today's offer from {{store}}

{% break %}

{% else %}
{% abort_message("No attribute found") %}
{% endif %}
{% endfor %}
```
{% endraw %}

{% alert important %} Diese Sequenz weist ein `break`-Tag in der primären bedingten Anweisung auf. Dadurch wird die Schleife angehalten, wenn eine Übereinstimmung gefunden wird. Wenn Sie viele oder alle Treffer anzeigen möchten, entfernen Sie das Tag `break`. {% endalert %}

### Eine Erinnerung an ein bevorstehendes Event erstellen {#misc-event-reminder}

Mit diesem Anwendungsfall können Benutzer anstehende Erinnerungen auf der Grundlage von benutzerdefinierten Ereignissen einrichten. In dem Beispielszenario kann ein Nutzer oder eine Nutzerin eine Erinnerung für ein Verlängerungsdatum einer Police festlegen, das 26 oder mehr Tage in der Zukunft liegt, wobei Erinnerungen 26, 13, 7 oder 2 Tage vor dem Verlängerungsdatum der Police gesendet werden.

Bei diesem Anwendungsfall sollte Folgendes in den Text einer [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) oder eines Canvas-Schritts aufgenommen werden.

{% raw %}
```liquid
{% comment %}
Depending on how the reminder_capture property is passed to Braze, with/without a timestamp, the number of days could impact whether a user falls on either side of the 26/13/7/2-day windows.
Once users have been assigned to a Reminder journey/flow, they are then scheduled to enter a subsequent Canvas.
This 'Event Listener' can be used to split out users into different journeys based on the Custom Event properties sent to Braze.
{% endcomment %}

{% comment %}
When testing, make sure the campaign ID, campaign API endpoint, Canvas ID, Canvas API endpoint are entered correctly. In this example, the Canvas ID and Canvas API endpoint have been set up for sharing with the client. In practice, this can be testing using a campaign ID and Campaign API endpoint.
{% endcomment %}

{% comment %}
The following step calculates how much there is between today's date and the Reminder Date as 'time_to_reminder'.
{% endcomment %}

{% assign today = "now" | date: '%s' %}
{% assign reminder_start_date = {{event_properties.${reminder_date}}} | date: '%s' %}
{% assign time_to_reminder = reminder_start_date | minus: today %}

{% comment %}
The following step checks if the time_to_reminder is more than 26 days away; if this is true, then the user is scheduled to enter the subsequent Canvas 26 days before the reminder_date.
The time is converted from 'seconds from 1970' to the appropriate Reminder Date in the required ISO 8601 format.
N.B. Additional time zones would need to be catered for by adding an additional API Schedule property of "in_local_time"
{% endcomment %}

{% if {{time_to_reminder}} > 2246400 %}
{% assign time_to_first_message = reminder_start_date | plus: 2246400 %}
{{ time_to_first_message | date: '%Y-%m-%dT%H:%M' }}
{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 26 days away but more than 13 days away.
Users are scheduled to enter the journey on day 13.
{% endcomment %}

{% elsif 1123200 > {{time_to_reminder}} and {{time_to_reminder}} < 2246399 %}
{% assign time_to_first_message = reminder_start_date | plus: 1123200 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than 13 days away but more than seven days away.
Users are scheduled to enter the journey on day 7.
{% endcomment %}

{% elsif 604800 > {{time_to_reminder}} and {{time_to_reminder}} < 1123199 %}
{% assign time_to_first_message = reminder_start_date | plus: 604800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}

{% comment %}
The following step checks if the time_to_reminder is less than seven days away but more than two days away.
Users are scheduled to enter the journey on day 2.
{% endcomment %}

{% else {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
{% assign time_to_first_message = reminder_start_date | plus: 172800 %}

{
"canvas_id": "954e15bc-af93-9dc8-a863-ad2580f1750e",
"recipients": [
{
"external_user_id": "{{${user_id}}}"
}
],
"trigger_properties" : {
"enquiry_id" : "{{event_properties.${reminder_id}}}",
"reminder_date" : "{{event_properties.${reminder_date} | date: '%Y-%m-%dT%H:%M:%S+0000'}}",
"message_personalisation_X" : "{{event_properties.${property_x}}}",
"message_personalisation_Y" : "{{event_properties.${property_y}}}",
"message_personalisation_Z" : "{{event_properties.${property_z}}}"
},

"schedule": {
"time": "{{ time_to_first_message | date: '%Y-%m-%dT%H:%M:%S+0000' }}"
}
}
{% endif %}
```
{% endraw %}

{% alert important %} 

Sie benötigen ein angepasstes Event `reminder_capture`, und die angepassten Event-Eigenschaften müssen Folgendes enthalten:

- `reminder-id`: Kennung des angepassten Events
- `reminder_date`: Vom Benutzer eingegebenes Datum, an dem die Erinnerung fällig ist
- `message_personalisation_X`: Alle Eigenschaften, die zur Personalisierung der Nachricht zum Zeitpunkt des Versands benötigt werden

{% endalert %}

### Suche nach einer Zeichenkette innerhalb eines Arrays {#misc-string-in-array}

Dieser Anwendungsfall prüft, ob ein benutzerdefiniertes Attribut-Array eine bestimmte Zeichenfolge enthält, und zeigt, falls vorhanden, eine bestimmte Meldung an.

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### Finden Sie den größten Wert in einem Array {#misc-largest-value}

Dieser Anwendungsfall berechnet den höchsten Wert in einem gegebenen benutzerdefinierten Attribut-Array zur Verwendung in Benutzernachrichten.

Zum Beispiel können Sie einem Benutzer den aktuellen Highscore oder das höchste Gebot für einen Artikel anzeigen.

{% raw %}
```liquid
{% assign maxValue = 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue > maxValue %}
{% assign maxValue = compareValue %}
{% endif %}
{% endfor %}
{{maxValue}}
```
{% endraw %}

{% alert important %}
Sie müssen ein angepasstes Attribut verwenden, das einen ganzzahligen Wert hat und Teil eines Arrays (einer Liste) ist. {% endalert %}

### Finden Sie den kleinsten Wert in einem Array {#misc-smallest-value}

Dieser Anwendungsfall berechnet den niedrigsten Wert in einem gegebenen benutzerdefinierten Attribut-Array zur Verwendung in Benutzernachrichten.

Zum Beispiel können Sie einem Benutzer die niedrigste Punktzahl oder den billigsten Artikel anzeigen.

{% raw %}
```liquid
{% assign minValue = custom_attribute.${array_attribute}[0] | plus: 0 %}
{% for attribute in {{custom_attribute.${array_attribute}}} %}
{% assign compareValue = {{attribute | plus: 0}} %}
{% if compareValue < minValue %}
{% assign minValue = compareValue %}
{% endif %}
{% endfor %}
{{minValue}}
```
{% endraw %}

{% alert important %} Sie müssen ein angepasstes Attribut verwenden, das einen ganzzahligen Wert hat und Teil eines Arrays (einer Liste) ist. {% endalert %}

### Abfrage des Endes einer Zeichenkette {#misc-query-end-of-string}

Dieser Anwendungsfall fragt das Ende einer Zeichenkette für die Verwendung in Nachrichten ab.

{% raw %}
```liquid
{% assign interest = {{custom_attribute.${Buyer Interest}} | first } %}
{% assign marketplace = {{{{interest}} | split: "" | reverse | join: "" |  truncate: 4, ""}} %}
{% if {{marketplace}} == '3243' %}

Your last marketplace search was on {{custom_attribute.${Last marketplace buyer interest} | date: '%d.%m.%Y'}}. Check out all of our new offers.

{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

### Abfrage von Werten in einem Array aus einem benutzerdefinierten Attribut mit mehreren Kombinationen {#misc-query-array-values}

Dieser Anwendungsfall nimmt eine Liste mit bald ablaufenden Sendungen, prüft, ob eine der Lieblingssendungen des Benutzers in dieser Liste enthalten ist, und wenn ja, wird eine Nachricht angezeigt, die den Benutzer darüber informiert, dass sie bald ablaufen werden.

{% raw %} 
```liquid
{% assign expired_shows = 'Modern Family,The Rookie,Body of Proof,Felicity' | split: ',' %}
{% for show in expired_shows %}
{% if {{custom_attribute.${Favorite Shows}}} contains {{show}} %}
{% assign new_shows = new_shows | append: {{show}} | append: '*' %}
{% endif %}
{% endfor %}
{% assign new_shows_clean = new_shows | split: '*' %}
{% if new_shows_clean.size != 0 %}

All episodes of {{new_shows_clean | join: ', ' }} expire on 9/8 - watch them now before they're gone!

{% else %}
{% abort_message("Not found") %}
{% endif %}
```
{% endraw %}

{% alert important %} Sie müssen zunächst Übereinstimmungen zwischen den Arrays finden und dann am Ende eine Logik erstellen, um die Übereinstimmungen aufzuteilen. {% endalert %}

### Eine Zeichenkette in eine Telefonnummer formatieren {#phone-number}

Dieser Anwendungsfall zeigt Ihnen, wie Sie das Feld des Benutzerprofils `phone_number` (standardmäßig als Ganzzahlenkette formatiert) indizieren und auf der Grundlage Ihrer lokalen Telefonnummernstandards neu formatieren können. Zum Beispiel: 1234567890 an (123)-456-7890.

{% raw %} 
```liquid
{% assign phone = {{${phone_number}}} | remove: "-" | split: '' %}

({{ phone[0] }}{{ phone[1] }}{{ phone[2] }})-{{ phone[3] }}{{ phone[4] }}{{ phone[5] }}-{{ phone[6] }}{{ phone[7] }}{{ phone[8] }}{{ phone[9] }}
```
{% endraw %}

{% endapi %}

{% api %}

## Plattform-Targeting

{% apitags %}
Plattform-Targeting
{% endapitags %}

- [Kopien je nach Betriebssystem des Geräts unterscheiden](#platform-device-os)
- [Nur eine bestimmte Plattform anvisieren](#platform-target)
- [Nur iOS-Geräte mit einer bestimmten Betriebssystemversion anvisieren](#platform-target-ios-version)
- [Nur Webbrowser anvisieren](#platform-target-web)
- [Einen bestimmten Mobilfunkanbieter anvisieren](#platform-target-carrier)

### Kopien je nach Betriebssystem des Geräts unterscheiden {#platform-device-os}

Dieser Anwendungsfall prüft, auf welcher Plattform sich ein Benutzer befindet, und zeigt je nach Plattform bestimmte Nachrichten an.

So können Sie z. B. mobilen Nutzer:innen kürzere Versionen der Nachricht anzeigen, während anderen Nutzer:innen die normale, längere Version der Nachricht angezeigt wird. Sie könnten mobilen Nutzer:innen auch bestimmte Nachrichten zeigen, die für sie relevant sind, aber für Webnutzer:innen nicht relevant wären. Zum Beispiel könnte in iOS-Nachrichten von Apple Pay die Rede sein, aber in Android-Nachrichten sollte Google Pay erwähnt werden.

{% raw %}
```liquid
{% if targeted_device.${platform} == "ios" or targeted_device.${platform} == "android" %}
This is a shorter copy.

{% else %}
This is the regular copy and much longer than the short version. 
{% endif %}
```
{% endraw %}

{% alert note %}
Bei Liquid wird zwischen Groß- und Kleinschreibung unterschieden. `targeted_device.${platform}` gibt den Wert in Kleinbuchstaben zurück.
{% endalert %}

### Nur eine bestimmte Plattform anvisieren {#platform-target}

Dieser Anwendungsfall erfasst die Geräteplattform des Benutzers und zeigt je nach Plattform eine Meldung an.

Sie möchten zum Beispiel eine Nachricht nur an Android-Nutzer senden. Dies kann als Alternative zur Auswahl einer App im Segmentierungstool verwendet werden.

{% raw %}
```liquid
{% if {{targeted_device.${platform}}} == 'android' %} 

This is a message for an Android user! 

{% else %}  
{% abort_message %} 
{% endif %}
```
{% endraw %}

### Nur Geräte mit einer bestimmten Betriebssystemversion anvisieren {#platform-target-ios-version}

Dieser Anwendungsfall prüft, ob die Betriebssystemversion eines Benutzers in eine bestimmte Gruppe von Versionen fällt, und wenn dies der Fall ist, wird eine bestimmte Meldung angezeigt.

Das verwendete Beispiel sendet eine Warnung an Benutzer mit einem Betriebssystem der Version 10.0 oder früher, dass die Unterstützung für das Betriebssystem des Geräts des Benutzers ausläuft.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == "10.0" or {{targeted_device.${os}}} == "10.0.1" or {{targeted_device.${os}}} == "10.0.2" or {{targeted_device.${os}}} == "10.0.3" or {{targeted_device.${os}}} == "10.1" or {{targeted_device.${os}}} == "10.2" or {{targeted_device.${os}}} == "10.2.1" or {{targeted_device.${os}}} == "10.3" or {{targeted_device.${os}}} == "10.3.1" or {{targeted_device.${os}}} == "10.3.2" or {{targeted_device.${os}}} == "10.3.3" or {{targeted_device.${os}}} == "10.3.4" or {{targeted_device.${os}}} == "9.3.1" or {{targeted_device.${os}}} == "9.3.2" or {{targeted_device.${os}}} == "9.3.3" or {{targeted_device.${os}}} == "9.3.4" or {{targeted_device.${os}}} == "9.3.5" %}

We are phasing out support for your device's operating system. Be sure to update to the latest software for the best app experience.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

### Nur Webbrowser anvisieren {#platform-target-web}

Dieser Anwendungsfall prüft, ob das Zielgerät eines Benutzers unter Mac oder Windows läuft, und zeigt in diesem Fall eine bestimmte Meldung an.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'Mac' or {{targeted_device.${os}}} == 'Windows' %}

This message will display on your desktop web browser.

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

Der folgende Anwendungsfall überprüft, ob ein:e Webnutzer:in iOS oder Android verwendet, und zeigt in diesem Fall eine bestimmte Nachricht an.

{% raw %}
```liquid
{% if {{targeted_device.${os}}} == 'iOS' and {{targeted_device.${platform}}} == 'web' %}

Content for iOS.

{% elsif {{targeted_device.${os}}} == 'android' and {{targeted_device.${platform}}} == 'web' %}

Content for Android.

{% else %}
{% abort_message %} 
{% endif %}
```
{% endraw %}

### Einen bestimmten Mobilfunkanbieter anvisieren {#platform-target-carrier}

Dieser Anwendungsfall prüft, ob das Gerät eines Benutzers von Verizon betrieben wird, und wenn ja, wird eine spezielle Nachricht angezeigt.

Für Push-Benachrichtigungen und In-App-Nachrichtenkanäle können Sie mit Liquid den Geräteträger in Ihrem Nachrichtentext angeben. Wenn der Geräteträger des Empfängers oder der Empfängerin nicht übereinstimmt, wird die Nachricht nicht gesendet.

{% raw %}
```liquid
{% if {targeted_device.${carrier}} contains "verizon" or {targeted_device.${carrier}} contains "Verizon" %}

This is a message for Verizon users!

{% else %}
{% abort_message %}
{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## SMS

{% apitags %}
SMS
{% endapitags %}

- [Reagieren Sie mit verschiedenen Nachrichten auf eingehende SMS-Schlüsselwörter](#sms-keyword-response)

### Reagieren Sie mit verschiedenen Nachrichten auf eingehende SMS-Schlüsselwörter {#sms-keyword-response}

Dieser Anwendungsfall beinhaltet eine dynamische SMS-Schlüsselwortverarbeitung, um auf bestimmte eingehende Nachrichten mit unterschiedlichen Nachrichtentexten zu reagieren. Sie können zum Beispiel unterschiedliche Antworten senden, wenn jemand "START" oder "JOIN" schreibt.

{% raw %}
```liquid
{% assign inbound_message = {{sms.${inbound_message_body}}} | downcase | strip %}
{% if inbound_message contains 'start' %}
Thanks for joining our SMS program! Make sure your account is up to date for the best deals!

{% elsif inbound_message contains 'join' %}
Thanks for joining our SMS program! Create an account to get the best deals!

{% else %}
Thanks for joining our SMS program!

{% endif %}
```
{% endraw %}

{% endapi %}

{% api %}

## Zeitzonen

{% apitags %}
Zeitzonen
{% endapitags %}

- [Eine Nachricht abhängig von der Zeitzone eines Nutzers oder einer Nutzerin personalisieren](#personalize-timezone)
- [Anhängen der CST-Zeitzone an ein benutzerdefiniertes Attribut](#time-append-cst)
- [Einen Zeitstempel einfügen](#time-insert-timestamp)
- [Senden Sie einen Canvas-Push nur während eines Zeitfensters in der lokalen Zeitzone eines Benutzers](#time-canvas-window)
- [Senden Sie eine wiederkehrende In-App-Nachrichtenkampagne innerhalb eines Zeitfensters in der lokalen Zeitzone eines Benutzers.](#time-reocurring-iam-window)
- [Unterschiedliche Nachrichten an Wochentagen und Wochenenden in der lokalen Zeitzone eines Nutzers oder einer Nutzerin senden](#time-weekdays-vs-weekends)
- [Unterschiedliche Nachrichten je nach Tageszeit in der lokalen Zeitzone eines Nutzers oder einer Nutzerin senden](#time-of-day)

### Personalisieren Sie eine Nachricht abhängig von der Zeitzone eines Benutzers {#personalize-timezone}

In diesem Anwendungsfall werden je nach Zeitzone des Benutzers unterschiedliche Nachrichten angezeigt.

{% raw %}
```liquid
{% if {{${time_zone}}} == 'xx' %}
Message for time zone xx.
{% elsif {{$time_zone}}} == 'yy' %}
Message for time zone yy.
{% else %}
{% abort_message("Invalid time zone") %}
{% endif %}
```
{% endraw %}

### Anhängen der CST-Zeitzone an ein benutzerdefiniertes Attribut {#time-append-cst}

Dieser Anwendungsfall zeigt ein benutzerdefiniertes Datumsattribut in einer bestimmten Zeitzone an.

Option 1:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: -0005 | date: '%B, %d %Y' }}
```
{% endraw %}

Option 2:
{% raw %}
```liquid
{{custom_attribute.${application_expires_date} | time_zone: 'America/Chicago' | date: '%B %d %Y %z' }}
```
{% endraw %}

### Einen Zeitstempel einfügen {#time-insert-timestamp}

In diesem Anwendungsfall wird eine Nachricht angezeigt, die einen Zeitstempel in ihrer aktuellen Zeitzone enthält.

Im folgenden Beispiel wird das Datum als JJJJ-mm-tt HH:MM:SS angezeigt, z. B. 2021-05-03 10:41:04.

{% raw %}
```liquid
{{${user_id} | default: 'You'}} received a campaign, rendered at ({{ "now" | time_zone: ${time_zone} | date: "%Y-%m-%d %H:%M:%S" }})
```
{% endraw %}

### Senden Sie einen Canvas-Push nur während eines Zeitfensters in der lokalen Zeitzone eines Benutzers {#time-canvas-window}

Dieser Anwendungsfall prüft die Zeit eines Benutzers in seiner lokalen Zeitzone und zeigt, wenn sie innerhalb einer bestimmten Zeitspanne liegt, eine bestimmte Nachricht an.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Here's a message that will send between 8 am and 8 pm!
```
{% endraw %}

### Eine wiederkehrende In-App-Nachrichtenkampagne innerhalb eines Zeitfensters in der lokalen Zeitzone eines Nutzers oder einer Nutzerin senden {#time-reoccurring-iam-window}

In diesem Anwendungsfall wird eine Nachricht angezeigt, wenn die aktuelle Zeit eines Benutzers innerhalb eines festgelegten Zeitfensters liegt.

Das folgende Szenario informiert einen Benutzer zum Beispiel darüber, dass ein Geschäft geschlossen ist.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %} 
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 21 or hour < 10 %}

Store's closed. Come back between 11 am and 9 pm!

{% else %} 
{% abort_message("Not sent because the store is open") %}
{% endif %}
```
{% endraw %}

### Unterschiedliche Nachrichten an Wochentagen und Wochenenden in der lokalen Zeitzone eines Nutzers oder einer Nutzerin senden {#time-weekdays-vs-weekends}

In diesem Anwendungsfall wird geprüft, ob der aktuelle Wochentag eines Benutzers Samstag oder Sonntag ist, und je nach Tag werden unterschiedliche Nachrichten angezeigt.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: ${time_zone} | date: "%A" %}
{% if {{today}} == 'Saturday' or {{today}} == 'Sunday' %}
It's {{today}}, why don't you open the app for your transactions?

{% else %}
It's {{today}}, why don't you visit the store?
{% endif %}
```
{% endraw %}

### Senden Sie unterschiedliche Nachrichten je nach Tageszeit in der lokalen Zeitzone eines Benutzers {#time-of-day}

In diesem Anwendungsfall wird eine Meldung angezeigt, wenn die aktuelle Zeit eines Benutzers außerhalb eines festgelegten Zeitfensters liegt.

Zum Beispiel können Sie einen Nutzer oder eine Nutzerin über eine zeitkritische Gelegenheit informieren, die von der Tageszeit abhängt.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 20 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}

Check out this new bar after work today. HH specials!
```
{% endraw %}

{% alert note %} Dies ist das Gegenteil von [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/time_based_campaign/#time-based-functionalities-for-campaigns). {% endalert %}

{% endapi %}

{% api %}

## Woche/Tag/Monat

{% apitags %}
Woche/Tag/Monat
{% endapitags %}

- [Den Namen des Vormonats in eine Nachricht ziehen](#month-name)
- [Am Ende jedes Monats eine Kampagne senden](#month-end)
- [Eine Kampagne am letzten (Wochentag) des Monats senden](#day-of-month-last)
- [An jedem Tag des Monats eine andere Nachricht senden](#day-of-month)
- [An jedem Tag der Woche eine andere Nachricht senden](#day-of-week)

### Den Namen des Vormonats in eine Nachricht ziehen {#month-name}

Dieser Anwendungsfall nimmt den aktuellen Monat und zeigt den Vormonat an, der in den Nachrichten verwendet werden soll.

{% raw %}
```liquid
{% assign today = 'now' | date: "%m" %}
{% assign last_month = {{today}} | minus: 1 %}
{% if last_month == 1 %}
{% assign month = "January" %}
{% elsif last_month == 2 %}
{% assign month = "February" %}
{% elsif last_month == 3 %}
{% assign month = "March" %}
{% elsif last_month == 4 %}
{% assign month = "April" %}
{% elsif last_month == 5 %}
{% assign month = "May" %}
{% elsif last_month == 6 %}
{% assign month = "June" %}
{% elsif last_month == 7 %}
{% assign month = "July" %}
{% elsif last_month == 8 %}
{% assign month = "August" %}
{% elsif last_month == 9 %}
{% assign month = "September" %}
{% elsif last_month == 10 %}
{% assign month = "October" %}
{% elsif last_month == 11 %}
{% assign month = "November" %}
{% elsif last_month == 0 %}
{% assign month = "December" %}
{% endif %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

Sie können alternativ auch Folgendes verwenden, um das gleiche Ergebnis zu erzielen.

{% raw %}
```liquid
{% assign last_month_name = 'now' | date: "%Y-%m-01" | date: '%s' | minus: 1 | date: "%B" %}

Here's an overview of what your spending looked like in {{month}}.
```
{% endraw %}

### Am Ende jedes Monats eine Kampagne senden {#month-end}

In diesem Anwendungsfall wird geprüft, ob das aktuelle Datum in eine Liste von Daten fällt, und je nach Datum wird eine bestimmte Nachricht angezeigt.

{% alert note %} Schaltjahre (29\. Februar) sind dabei nicht berücksichtigt. {% endalert %}

{% raw %}
```liquid
{% assign current_date = 'now' | date: '%b %d' %}

{% if current_date == "Jan 31" or current_date == "Feb 28" or current_date == "Mar 31" or current_date == "Apr 30" or current_date == "May 31" or current_date == "Jun 30" or current_date == "Jul 31" or current_date == "Aug 31" or current_date == "Sep 30" or current_date == "Oct 31" or current_date == "Nov 30" or current_date == "Dec 31" %}

The date is correct

{% else %}
{% abort_message("Date is not listed") %}
{% endif %}
```
{% endraw %}

### Senden Sie eine Kampagne am letzten (Wochentag) des Monats {#day-of-month-last}

Dieser Anwendungsfall erfasst den aktuellen Monat und Tag und berechnet, ob der aktuelle Tag in den letzten Wochentag des Monats fällt.

Sie könnten zum Beispiel am letzten Mittwoch des Monats eine Umfrage an Ihre Benutzer senden und um Produktfeedback bitten.

{% raw %}
```liquid
{% comment %}Pull the day, day name, month, and year from today's date.{% endcomment %}
{% assign current_day = "now" | date: "%d" %}
{% assign current_day_name = "now" | date: "%a" %}
{% assign current_month = "now" | date: "%b" %}
{% assign current_year = "now" | date: "%Y" %}

{% comment %}Assign the correct number of days for the current month.{% endcomment %}

{% if current_month == "Jan" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Mar" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Apr" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "May" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Jun" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Jul" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Aug" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Sep" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Oct" %}
{% assign last_day_of_month = 31 %}
{% elsif current_month == "Nov" %}
{% assign last_day_of_month = 30 %}
{% elsif current_month == "Dec" %}
{% assign last_day_of_month = 31 %}
{% endif %}

{% comment %}Assign the correct number of days if the current month is February, taking into account leap years.{% endcomment %}

{% assign leap_year_remainder = {{current_year | modulo: 4 }} != "0" %}
{% if leap_year_remainder == 0 and current_month == "Feb" %}
{% assign last_day_of_month = 29 %}
{% elsif leap_year_remainder != "0" and current_month == "Feb" %}
{% assign last_day_of_month = 28 %}
{% endif %}

{% comment %}Check that today's date is within a week of the last day of the month. If not, abort the message. If so, check that today is Wednesday. If not, abort the message.{% endcomment %}

{% assign diff_in_days = last_day_of_month | minus: current_day | plus: 1%} 
{% if diff_in_days <= 7 %} 
{% unless current_day_name == "Wed" %} 
{% abort_message("Wrong day of the week") %} 
{% endunless %} 
{% else %} 
{% abort_message("Not the last week of the month") %} 
{% endif %}
```
{% endraw %}

### An jedem Tag des Monats eine andere Nachricht senden {#day-of-month}

Dieser Anwendungsfall prüft, ob das aktuelle Datum mit einem Datum in einer Liste übereinstimmt, und zeigt je nach Tag eine bestimmte Nachricht an.

{% raw %}
```liquid
{% assign today = 'now' | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_1 = "2019-12-01" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_2 = "2019-12-02" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}
{% assign day_3 = "2019-12-03" | time_zone: {{${time_zone}}} | date: "%Y-%m-%d" %}

{% if today == day_1 %}
Message for 2019-12-01

{% elsif today == day_2 %}
Message for 2019-12-02

{% elsif today == day_3%}
Message for 2019-12-03

{% else %}
{% abort_message("Date not listed") %}
{% endif %}
```
{% endraw %}

### An jedem Tag der Woche eine andere Nachricht senden {#day-of-week}

Dieser Anwendungsfall prüft den aktuellen Wochentag und zeigt je nach Tag eine bestimmte Nachricht an.

{% raw %}
```liquid
{% assign today = 'now' | date: "%A" %}
{% case today %}
{% when 'Monday' %}
Monday copy

{% when 'Tuesday' %}
Tuesday copy

{% when 'Wednesday' %}
Wednesday copy

{% when  'Thursday' %}
Thursday copy

{% when  'Friday' %}
Friday copy

{% when 'Saturday' %}
Saturday copy

{% when 'Sunday' %}
Sunday copy

{% else %}
Default copy
{% endcase %}
```
{% endraw %}

{% alert note %}
Sie können die Zeile „Standardkopie“ durch {% raw %}`{% abort_message() %}`{% endraw %} ersetzen, um zu verhindern, dass die Nachricht gesendet wird, wenn der Wochentag unbekannt ist.
{% endalert %}

{% endapi %}
