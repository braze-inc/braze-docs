---
nav_title: Liquid Bibliothek für Anwendungsfälle
article_title: Bibliothek für Liquid-Anwendungsfälle
page_order: 10
search_rank: 2
excerpt_separator: ""
page_type: glossary
layout: liquid_use_case_glossary
description: "Auf dieser Landing Page finden Sie Beispiele für Liquid-Anwendungsfälle, die nach Kategorien geordnet sind, z. B. Jahrestage, App-Nutzung, Countdowns und mehr."

---

{% api %}

## Jahrestage und Feiertage

{% apitags %}
Jahrestage und Feiertage
{% endapitags %}

- [Nachrichten basierend auf dem Jubiläumsjahr einer Nutzerin oder eines Nutzers personalisieren](#anniversary-year)
- [Nachrichten basierend auf der Geburtstagswoche einer Nutzerin oder eines Nutzers personalisieren](#birthday-week)
- [Kampagnen an Nutzer:innen in deren Geburtstagsmonat senden](#birthday-month)
- [Versand von Nachrichten an wichtigen Feiertagen vermeiden](#holiday-avoid)

### Nachrichten basierend auf dem Jubiläumsjahr einer Nutzerin oder eines Nutzers personalisieren {#anniversary-year}

Dieser Anwendungsfall zeigt, wie man das App-Jubiläum eines Nutzers bzw. einer Nutzerin auf der Grundlage des Erstanmeldedatums berechnet und je nach Anzahl der gefeierten Jahre unterschiedliche Nachrichten anzeigt.

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

**Erläuterung:** Hier verwenden wir die reservierte Variable `now`, um das aktuelle Datum und die Uhrzeit im [ISO 8601-Format](http://en.wikipedia.org/wiki/ISO_8601) als Template einzufügen. Die Filter `%B` (Monat wie „Mai") und `%d` (Tag wie „18") formatieren den aktuellen Monat und Tag. Anschließend verwenden wir dieselben Datums- und Zeitfilter für die Werte von `signup_date`, um sicherzustellen, dass wir die beiden Werte mithilfe von bedingten Tags und Logik vergleichen können.

Dann wiederholen wir drei weitere Variablenanweisungen, um `%B` und `%d` für das `signup_date` zu erhalten, fügen aber auch `%Y` (Jahr wie „2021") hinzu. Damit wird das Datum und die Uhrzeit von `signup_date` auf die Jahreszahl reduziert. Wenn wir den Tag und den Monat kennen, können wir überprüfen, ob der Nutzer bzw. die Nutzerin heute Jubiläum hat, und wenn wir das Jahr kennen, wissen wir, wie viele Jahre es her ist – und damit auch, zu wie vielen Jahren wir gratulieren können!

{% alert tip %} Je nachdem, wie viele Jahre Sie bereits Registrierungsdaten sammeln, können Sie entsprechend viele Bedingungen erstellen. {% endalert %}  

### Nachrichten basierend auf der Geburtstagswoche einer Nutzerin oder eines Nutzers personalisieren {#birthday-week}

Dieser Anwendungsfall zeigt, wie Sie den Geburtstag eines Nutzers bzw. einer Nutzerin ermitteln, ihn mit dem aktuellen Datum vergleichen und dann spezielle Geburtstagsnachrichten vor, während und nach der Geburtstagswoche anzeigen.

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

**Erläuterung:** Ähnlich wie im Anwendungsfall [Jubiläumsjahr](#anniversary-year) nehmen wir hier die reservierte Variable `now` und verwenden den Filter `%W` (Woche, z. B. Woche 12 von 52 in einem Jahr), um die Kalenderwoche zu ermitteln, in die der Geburtstag des Nutzers bzw. der Nutzerin fällt. Wenn die Geburtstagswoche mit der aktuellen Woche übereinstimmt, senden wir eine Glückwunschnachricht! 

Wir fügen auch Anweisungen für `last_week` und `next_week` hinzu, um Ihr Messaging noch persönlicher zu gestalten.

### Kampagnen an Nutzer:innen in deren Geburtstagsmonat senden {#birthday-month}

Dieser Anwendungsfall zeigt, wie Sie den Geburtstagsmonat eines Nutzers bzw. einer Nutzerin berechnen, prüfen, ob der Geburtstag in den aktuellen Monat fällt, und wenn ja, eine spezielle Nachricht senden.

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

**Erläuterung:** Ähnlich wie beim Anwendungsfall [Geburtstagswoche](#birthday-week), nur dass wir hier den Filter `%B` (Monat wie „Mai") verwenden, um zu berechnen, welche Nutzer:innen in diesem Monat Geburtstag haben. Eine mögliche Anwendung könnte darin bestehen, Geburtstagskinder in einer monatlichen E-Mail anzusprechen.

### Versand von Nachrichten an wichtigen Feiertagen vermeiden {#holiday-avoid}

Dieser Anwendungsfall zeigt, wie Sie während der Ferienzeit Nachrichten versenden und dabei die Tage der großen Feiertage vermeiden können, an denen das Engagement wahrscheinlich gering ist.

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

**Erläuterung:** Hier weisen wir den Term `today` der reservierten Variablen `now` (das aktuelle Datum und die Uhrzeit) zu und verwenden die Filter `%Y` (Jahr wie „2023"), `%m` (Monat wie „12") und `%d` (Tag wie „25"), um das Datum zu formatieren. Anschließend führen wir unsere bedingte Anweisung aus, die besagt, dass die Nachricht abgebrochen wird, wenn die Variable `today` mit den von Ihnen gewählten Feiertagen übereinstimmt. 

Das angegebene Beispiel bezieht sich auf Heiligabend, den ersten Weihnachtsfeiertag und den zweiten Weihnachtsfeiertag.

{% endapi %}

{% api %}

## App-Nutzung

{% apitags %}
App-Nutzung
{% endapitags %}

- [Nachrichten in der Sprache eines Nutzers bzw. einer Nutzerin senden, wenn eine Sitzung protokolliert wurde](#app-session-language)
- [Nachrichten basierend darauf personalisieren, wann ein:e Nutzer:in die App zuletzt geöffnet hat](#app-last-opened)
- [Eine andere Nachricht anzeigen, wenn ein:e Nutzer:in die App zuletzt vor weniger als drei Tagen verwendet hat](#app-last-opened-less-than)

### Nachrichten in der Sprache eines Nutzers bzw. einer Nutzerin senden, wenn keine Sitzung protokolliert wurde {#app-session-language}

Dieser Anwendungsfall prüft, ob ein:e Nutzer:in eine Sitzung protokolliert hat, und falls nicht, enthält er eine Logik zur Anzeige einer Nachricht auf der Grundlage der Sprache, die über ein angepasstes Attribut manuell erfasst wurde. Wenn keine Sprachinformationen mit dem Konto verknüpft sind, wird die Nachricht in der Standardsprache angezeigt. Wenn ein:e Nutzer:in eine Sitzung protokolliert hat, werden alle mit dem Nutzer bzw. der Nutzerin verbundenen Sprachinformationen abgerufen und die entsprechende Nachricht angezeigt. 

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
**Erläuterung:** Hier verwenden wir zwei gruppierte `if`-Anweisungen, die ineinander verschachtelt sind. Die erste `if`-Anweisung prüft, ob der Nutzer bzw. die Nutzerin eine Sitzung gestartet hat, indem überprüft wird, ob `last_used_app_date` den Wert `nil` hat. Das liegt daran, dass `{{${language}}}` automatisch vom SDK erfasst wird, wenn ein:e Nutzer:in eine Sitzung protokolliert. Wenn noch keine Sitzung protokolliert wurde, kennen wir die Sprache noch nicht. Daher wird geprüft, ob sprachbezogene angepasste Attribute gespeichert wurden, und auf der Grundlage dieser Informationen wird eine Nachricht in dieser Sprache angezeigt, falls möglich.
{% endraw %}

Die zweite `if`-Anweisung prüft nur das Standard-Attribut, da der Nutzer bzw. die Nutzerin keinen `nil`-Wert für `last_used_app_date` hat. Das bedeutet, dass eine Sitzung protokolliert wurde und wir die Sprache kennen.

{% alert note %}
[`Nil`](https://shopify.github.io/liquid/basics/types/#nil) ist eine reservierte Variable, die zurückgegeben wird, wenn Liquid-Code keine Ergebnisse liefert. `Nil` wird in einem `if`-Block wie `false` behandelt.
{% endalert %}

### Nachrichten basierend darauf personalisieren, wann ein:e Nutzer:in die App zuletzt geöffnet hat {#app-last-opened}

Dieser Anwendungsfall berechnet, wann ein:e Nutzer:in Ihre App das letzte Mal geöffnet hat, und zeigt je nach Zeitdauer eine andere personalisierte Nachricht an.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
{% assign now = 'now' | date: "%s" %}
{% assign difference_in_days = {{now}} | minus: {{last_used_date}} | divided_by: 86400 %}
{% if {{difference_in_days}} < 3 %}
Happy to see you again!
{% else %}
It's been a while; here are some of our latest updates.
{% endif %}
```
{% endraw %}

### Eine andere Nachricht anzeigen, wenn ein:e Nutzer:in die App zuletzt vor weniger als drei Tagen verwendet hat {#app-last-opened-less-than}

Dieser Anwendungsfall berechnet, wie lange es her ist, dass ein:e Nutzer:in Ihre App verwendet hat, und zeigt je nach Zeitdauer eine andere personalisierte Nachricht an.

{% raw %}
```liquid
{% assign last_used_date = {{${last_used_app_date}}} | date: "%s" %}
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
- [Einen Countdown in Tagen erstellen](#countdown-days)
- [Einen Countdown von Tagen über Stunden bis Minuten erstellen](#countdown-dynamic)
- [Anzeigen, wie viele Tage bis zu einem bestimmten Datum verbleiben](#countdown-future-date)
- [Anzeigen, wie viele Tage bis zum Eintreffen eines angepassten Datumsattributs verbleiben](#countdown-custom-date-attribute)
- [Anzeigen, wie viel Zeit noch verbleibt, und Abbruch der Nachricht, wenn nur noch X Zeit verbleibt](#countdown-abort-window)
- [In-App-Nachricht, die X Tage vor dem Ende der Mitgliedschaft gesendet wird](#countdown-membership-expiry)
- [In-App-Nachrichten basierend auf dem Datum und der Sprache des Nutzers bzw. der Nutzerin personalisieren](#countdown-personalize-language)
- [Template für das Datum in 30 Tagen, formatiert als Monat und Tag](#countdown-template-date)

### X Tage zum heutigen Datum hinzufügen {#countdown-add-x-days}

Dieser Anwendungsfall fügt dem aktuellen Datum eine bestimmte Anzahl von Tagen hinzu, um darauf Bezug zu nehmen und in Nachrichten einzufügen. So können Sie z. B. eine Nachricht zur Wochenmitte senden, in der Sie auf Veranstaltungen in der Umgebung am Wochenende hinweisen.

{% raw %}
```liquid
Here are the movies we're showing on {{ "now" | date:'%s' | plus:259200 | date:"%F" }}!
```
{% endraw %}

Der Wert `plus` wird immer in Sekunden angegeben, daher verwenden wir am Ende den Filter `%F`, um die Sekunden in Tage umzurechnen.

{% alert important %}
Sie können in Ihrer Nachricht eine URL oder einen Deeplink zu einer Liste von Events einfügen, damit Sie den Nutzer bzw. die Nutzerin zu einer Liste von Aktionen weiterleiten können, die in Zukunft stattfinden.
{% endalert %}

### Einen Countdown ab einem bestimmten Zeitpunkt berechnen {#countdown-difference-days}

In diesem Anwendungsfall wird die Differenz in Tagen zwischen einem bestimmten Datum und dem aktuellen Datum berechnet. Diese Differenz kann verwendet werden, um Ihren Nutzer:innen einen Countdown anzuzeigen.

{% raw %}
```liquid
{% assign event_date = '2023-12-31' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
you have {{ difference_days }} days left!
```
{% endraw %}

### Einen Countdown für bestimmte Versanddaten und Prioritäten erstellen {#countdown-shipping-options}

In diesem Anwendungsfall werden verschiedene Versandoptionen erfasst, die Dauer der Zustellung berechnet und Nachrichten angezeigt, die Nutzer:innen ermutigen, rechtzeitig zu kaufen, um ihr Paket bis zu einem bestimmten Datum zu erhalten.

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

### Einen Countdown in Tagen erstellen {#countdown-days}

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
Sie benötigen ein angepasstes Attributfeld mit einem `date`-Wert.
{% endalert %}

### Einen Countdown von Tagen über Stunden bis Minuten erstellen {#countdown-dynamic}

In diesem Anwendungsfall wird die verbleibende Zeit zwischen einem bestimmten Ereignis und dem aktuellen Datum berechnet. Je nach verbleibender Zeit bis zum Event ändert sich der Zeitwert (Tage, Stunden, Minuten), um verschiedene personalisierte Nachrichten anzuzeigen.

Wenn beispielsweise die Bestellung einer Kundin oder eines Kunden in zwei Tagen eintrifft, könnten Sie sagen: „Ihre Bestellung trifft in 2 Tagen ein." Wenn es hingegen weniger als einen Tag ist, könnten Sie es in „Ihre Bestellung trifft in 17 Stunden ein" ändern.

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
Sie benötigen ein angepasstes Attributfeld mit einem `date`-Wert. Sie müssen auch Zeitschwellen festlegen, ab wann die Zeit in Tagen, Stunden und Minuten angezeigt werden soll.
{% endalert %}

### Anzeigen, wie viele Tage bis zu einem bestimmten Datum verbleiben {#countdown-future-date}

In diesem Anwendungsfall wird die Differenz zwischen dem aktuellen Datum und einem zukünftigen Ereignisdatum berechnet und eine Nachricht angezeigt, die angibt, wie viele Tage es noch bis zum Ereignis sind.

{% raw %}
```liquid
{% assign event_date = '2024-01-15' | date: "%s" %}
{% assign today = 'now' | date: "%s" %}
{% assign difference = event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
There are {{difference_days}} days until your birthday!
```
{% endraw %}

### Anzeigen, wie viele Tage bis zum Eintreffen eines angepassten Datumsattributs verbleiben {#countdown-custom-date-attribute}

Dieser Anwendungsfall berechnet die Differenz in Tagen zwischen dem aktuellen und dem zukünftigen Datum und zeigt eine Nachricht an, wenn die Differenz mit einer bestimmten Zahl übereinstimmt.

In diesem Beispiel erhält ein:e Nutzer:in zwei Tage vor dem angepassten Datumsattribut eine Nachricht. Andernfalls wird die Nachricht nicht gesendet.

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

In diesem Anwendungsfall wird berechnet, wie lange es noch bis zu einem bestimmten Datum dauert, und je nach Dauer werden verschiedene personalisierte Nachrichten angezeigt (wobei die Nachricht übersprungen wird, wenn das Datum zu nah ist). 

Zum Beispiel: „Sie haben noch x Stunden Zeit, um Ihr Ticket nach London zu kaufen" – aber die Nachricht wird nicht gesendet, wenn die Flugzeit nach London weniger als zwei Stunden entfernt ist.

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

{% alert important %} Sie benötigen eine angepasste Event-Eigenschaft. {% endalert %}

### In-App-Nachricht, die X Tage vor dem Ende der Mitgliedschaft gesendet wird {#countdown-membership-expiry}

Dieser Anwendungsfall erfasst das Ablaufdatum Ihrer Mitgliedschaft, berechnet, wie lange es noch bis zum Ablauf dauert, und zeigt je nach verbleibender Zeit verschiedene Nachrichten an.

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

### In-App-Nachrichten basierend auf dem Datum und der Sprache des Nutzers bzw. der Nutzerin personalisieren {#countdown-personalize-language}

Dieser Anwendungsfall berechnet einen Countdown bis zu einem Ereignis und zeigt den Countdown basierend auf der Spracheinstellung des Nutzers bzw. der Nutzerin in der jeweiligen Sprache an.

Sie könnten zum Beispiel einmal im Monat eine Reihe von Upsell-Nachrichten an die Nutzer:innen senden, um sie mit vier In-App-Nachrichten darüber zu informieren, wie lange ein Angebot noch gültig ist:

- Anfangsnachricht
- Noch 2 Tage
- Noch 1 Tag
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
Sie müssen einen `date`-Wert zuweisen und eine Abbruchlogik einbauen, falls das angegebene Datum außerhalb des Datumsbereichs liegt. Für taggenaue Berechnungen muss das zugewiesene Enddatum 23:59:59 beinhalten.
{% endalert %}

### Template für das Datum in 30 Tagen, formatiert als Monat und Tag {#countdown-template-date}

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

- [Eine Nachricht auf der Grundlage passender angepasster Attribute personalisieren](#attribute-matching)
- [Zwei angepasste Attribute subtrahieren, um die Differenz als Geldwert anzuzeigen](#attribute-monetary-difference)
- [Den Vornamen eines Nutzers bzw. einer Nutzerin referenzieren, wenn der vollständige Name im Feld first_name gespeichert ist](#attribute-first-name)

### Eine Nachricht auf der Grundlage passender angepasster Attribute personalisieren {#attribute-matching}

Dieser Anwendungsfall prüft, ob ein:e Nutzer:in über bestimmte angepasste Attribute verfügt, und zeigt in diesem Fall verschiedene personalisierte Nachrichten an. 

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

Dieser Anwendungsfall erfasst zwei monetäre angepasste Attribute, berechnet dann die Differenz und zeigt sie an, damit die Nutzer:innen wissen, wie weit sie noch von ihrem Ziel entfernt sind.

{% raw %}
```liquid
{% assign event_goal = {{custom_attribute.${last_selected_event_personal_goal}}} %}
{% assign current_raised =  {{custom_attribute.${last_selected_event_personal_amount_raised}}} %}
{% assign difference =  event_goal | minus: current_raised %}
You only have ${{ difference | round: 0 | number_with_delimiter }} left to raise!
```
{% endraw %}

### Den Vornamen eines Nutzers bzw. einer Nutzerin referenzieren, wenn der vollständige Name im Feld first_name gespeichert ist {#attribute-first-name}

Dieser Anwendungsfall erfasst den Vornamen eines Nutzers bzw. einer Nutzerin (wenn sowohl Vor- als auch Nachname in einem einzigen Feld gespeichert sind) und verwendet dann diesen Vornamen, um eine Willkommensnachricht anzuzeigen.

{% raw %}
```liquid
{{${first_name} | truncatewords: 1, "" | default: 'hi'}}
{% assign name = {{${first_name}}} | split: ' ' %}
Hi {{name[0]}}, here's your message!
```

**Erläuterung:** Der Filter `split` verwandelt den in `{{${first_name}}}` gespeicherten String in ein Array. Durch die Verwendung von `{{name[0]}}` verweisen wir dann nur auf das erste Element im Array, also den Vornamen des Nutzers bzw. der Nutzerin. 

{% endraw %}
{% endapi %}

{% api %}

## Angepasstes Event

{% apitags %}
Angepasstes Event
{% endapitags %}

- [Push-Benachrichtigung abbrechen, wenn ein angepasstes Event innerhalb von zwei Stunden stattfindet](#event-abort-push)
- [Jedes Mal eine Kampagne senden, wenn ein:e Nutzer:in ein angepasstes Event dreimal ausführt](#event-three-times)
- [Eine Nachricht an Nutzer:innen senden, die nur in einer Kategorie gekauft haben](#event-purchased-one-category)
- [Verfolgen, wie oft ein angepasstes Event im vergangenen Monat aufgetreten ist](#track)


### Push-Benachrichtigung abbrechen, wenn ein angepasstes Event innerhalb von zwei Stunden stattfindet {#event-abort-push}

Dieser Anwendungsfall berechnet die Zeit bis zu einem Ereignis und zeigt je nach verbleibender Zeit verschiedene personalisierte Nachrichten an.

So können Sie beispielsweise verhindern, dass eine Push-Benachrichtigung versendet wird, wenn eine angepasste Event-Eigenschaft in den nächsten zwei Stunden abläuft. Dieses Beispiel verwendet das Szenario eines Warenkorb-Abbruchs für ein Zugticket.

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

### Jedes Mal eine Kampagne senden, wenn ein:e Nutzer:in ein angepasstes Event dreimal ausführt {#event-three-times}

Dieser Anwendungsfall prüft, ob ein:e Nutzer:in ein angepasstes Event dreimal ausgeführt hat, und zeigt in diesem Fall eine Nachricht an oder sendet eine Kampagne. 

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

{% alert important %} Sie müssen über eine Event-Eigenschaft des Zählers für angepasste Events verfügen oder einen Webhook an Ihren Braze-Endpunkt verwenden. Damit wird ein angepasstes Attribut (`example_event_count`) jedes Mal inkrementiert, wenn der Nutzer bzw. die Nutzerin das Event ausführt. In diesem Beispiel wird eine Dreierkadenz verwendet (1, 4, 7, 10, usw.). Um die Kadenz bei Null zu beginnen (0, 3, 6, 9, usw.), entfernen Sie `minus: 1`.
{% endalert %}

### Eine Nachricht an Nutzer:innen senden, die nur in einer Kategorie gekauft haben {#event-purchased-one-category}

Dieser Anwendungsfall erfasst eine Liste der Kategorien, in denen ein:e Nutzer:in eingekauft hat, und zeigt eine Nachricht an, wenn nur eine Kaufkategorie vorhanden ist.

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

In diesem Anwendungsfall wird berechnet, wie oft ein angepasstes Event zwischen dem 1. des aktuellen Monats und dem Vormonat protokolliert wurde. Sie können dann einen users/track-Aufruf ausführen, um diesen Wert als angepasstes Attribut zu speichern. Beachten Sie, dass diese Kampagne zwei aufeinanderfolgende Monate laufen muss, bevor die monatlichen Daten verwendet werden können.

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
- [Ein Bild basierend auf der Sprache des Nutzers bzw. der Nutzerin anzeigen](#language-image-display)
- [Nachrichten basierend auf dem Wochentag und der Sprache des Nutzers bzw. der Nutzerin personalisieren](#language-personalize-message)

### Monatsnamen in einer anderen Sprache anzeigen {#language-display-month}

In diesem Anwendungsfall werden das aktuelle Datum, der Monat und das Jahr angezeigt, wobei der Monat in einer anderen Sprache erscheint. Das angegebene Beispiel verwendet Schwedisch.

{% raw %}
```liquid
{% assign day = 'now' | date: "%e" %}
{% assign year =  'now' | date: "%Y" %}
{% assign month =  'now' | date: "%B" %}

{% if {{month}} == 'January' %}
{{day}} Januari {{year}}
{% elsif {{month}} == 'February' %}
{{day}} Februari {{year}}
{% elsif {{month}} == 'March' %}
{{day}} Mars {{year}}
{% elsif {{month}} == 'April' %}
{{day}} April {{year}}
{% elsif {{month}} == 'May' %}
{{day}} Maj {{year}}
{% elsif {{month}} == 'June' %}
{{day}} Juni {{year}}
{% elsif {{month}} == 'July' %}
{{day}} Juli {{year}}
{% elsif {{month}} == 'August' %}
{{day}} Augusti {{year}}
{% elsif {{month}} == 'September' %}
{{day}} September {{year}}
{% elsif {{month}} == 'October' %}
{{day}} Oktober {{year}}
{% elsif {{month}} == 'November' %}
{{day}} November {{year}}
{% elsif {{month}} == 'December' %}
{{day}} December {{year}}
{% endif %}
```
{% endraw %}

### Ein Bild basierend auf der Sprache des Nutzers bzw. der Nutzerin anzeigen {#language-image-display}

In diesem Anwendungsfall wird ein Bild basierend auf der Sprache des Nutzers bzw. der Nutzerin angezeigt. Beachten Sie, dass dieser Anwendungsfall nur mit Bildern getestet wurde, die in die Braze-Mediathek hochgeladen wurden.

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

### Nachrichten basierend auf dem Wochentag und der Sprache des Nutzers bzw. der Nutzerin personalisieren {#language-personalize-message}

Dieser Anwendungsfall prüft den aktuellen Wochentag und zeigt – sofern die Sprache des Nutzers bzw. der Nutzerin auf eine der angebotenen Sprachoptionen eingestellt ist – eine bestimmte Nachricht in der jeweiligen Sprache an.

Das Beispiel endet am Dienstag, kann aber für jeden Wochentag wiederholt werden.

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

- [Versand von E-Mails an Kund:innen vermeiden, die Marketing-E-Mails blockiert haben](#misc-avoid-blocked-emails)
- [Den Abo-Status von Kund:innen verwenden, um den Inhalt von Nachrichten zu personalisieren](#misc-personalize-content)
- [Den ersten Buchstaben jedes Wortes in einem String großschreiben](#misc-capitalize-words-string)
- [Angepasste Attributwerte mit einem Array vergleichen](#misc-compare-array)
- [Eine Erinnerung an ein bevorstehendes Event erstellen](#misc-event-reminder)
- [Einen String innerhalb eines Arrays suchen](#misc-string-in-array)
- [Den größten Wert in einem Array finden](#misc-largest-value)
- [Den kleinsten Wert in einem Array finden](#misc-smallest-value)
- [Das Ende eines Strings abfragen](#misc-query-end-of-string)
- [Werte in einem Array aus einem angepassten Attribut mit mehreren Kombinationen abfragen](#misc-query-array-values)
- [Einen String als Telefonnummer formatieren](#phone-number)

### Versand von E-Mails an Kund:innen vermeiden, die Marketing-E-Mails blockiert haben {#misc-avoid-blocked-emails}

In diesem Anwendungsfall wird eine Liste gesperrter Nutzer:innen, die in einem Content-Block gespeichert ist, verwendet, um sicherzustellen, dass diese gesperrten Nutzer:innen in kommenden Kampagnen oder Canvasen nicht angesprochen werden.

{% alert important %}
Um dieses Liquid zu verwenden, speichern Sie zunächst die Liste der blockierten E-Mails in einem Content-Block. Die Liste sollte keine zusätzlichen Leerzeichen oder Zeichen zwischen den E-Mail-Adressen enthalten (z. B. `test@braze.com,abc@braze.com`).
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

**Erläuterung:** Hier überprüfen wir, ob die E-Mail-Adresse des potenziellen Empfängers bzw. der potenziellen Empfängerin in dieser Liste enthalten ist, indem wir den Content-Block der blockierten E-Mails referenzieren. Wenn die E-Mail gefunden wird, wird die Nachricht nicht gesendet.

{% alert note %}
Content-Blöcke haben eine maximale Größe von 5 MB.
{% endalert %}

### Den Abo-Status von Kund:innen verwenden, um den Inhalt von Nachrichten zu personalisieren {#misc-personalize-content}

Dieser Anwendungsfall verwendet den Abo-Status von Kund:innen, um personalisierte Inhalte zu senden. Kund:innen, die eine bestimmte Abo-Gruppe abonniert haben, erhalten eine exklusive Nachricht für E-Mail-Abo-Gruppen.

{% raw %}
```liquid
{% if {{subscribed_state.${subscription_group_id}}} == 'subscribed' %}
This is an exclusive message for subscribed users!
{% else %} This is the default message for other users.
{% endif %}
```
{% endraw %}

### Den ersten Buchstaben jedes Wortes in einem String großschreiben {#misc-capitalize-words-string}

In diesem Anwendungsfall wird ein String von Wörtern in ein Array aufgeteilt und der erste Buchstabe jedes Wortes großgeschrieben.

{% raw %}
```liquid
{% assign words_array = {{custom_attribute.${address}}} | split: ' ' %}
{% for words in {{words_array}} %}
{{ words | capitalize | append: ' ' }}
{% endfor %} 
```
{% endraw %}

**Erläuterung:** Hier haben wir unserem gewählten String-Attribut eine Variable zugewiesen und den Filter `split` verwendet, um den String in ein Array aufzuteilen. Anschließend haben wir das Tag `for` verwendet, um die Variable `words` jedem Element in unserem neu erstellten Array zuzuweisen, bevor wir diese Wörter mit dem Filter `capitalize` und dem Filter `append` anzeigen, um Leerzeichen zwischen den einzelnen Begriffen hinzuzufügen.

### Angepasste Attributwerte mit einem Array vergleichen {#misc-compare-array}

In diesem Anwendungsfall wird eine Liste von Lieblingsgeschäften verwendet. Es wird geprüft, ob sich eines der Lieblingsgeschäfte des Nutzers bzw. der Nutzerin in dieser Liste befindet, und wenn ja, wird ein Sonderangebot dieser Geschäfte angezeigt.

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

{% alert important %} Diese Sequenz enthält ein `break`-Tag in der primären bedingten Anweisung. Dadurch wird die Schleife angehalten, wenn eine Übereinstimmung gefunden wird. Wenn Sie viele oder alle Treffer anzeigen möchten, entfernen Sie das Tag `break`. {% endalert %}

### Eine Erinnerung an ein bevorstehendes Event erstellen {#misc-event-reminder}

Mit diesem Anwendungsfall können Nutzer:innen anstehende Erinnerungen auf der Grundlage von angepassten Events einrichten. In dem Beispielszenario kann ein:e Nutzer:in eine Erinnerung für ein Verlängerungsdatum einer Richtlinie festlegen, das 26 oder mehr Tage in der Zukunft liegt, wobei Erinnerungen 26, 13, 7 oder 2 Tage vor dem Verlängerungsdatum gesendet werden.

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

{% elsif {{time_to_reminder}} < 604799 and {{time_to_reminder}} > 172860 %}
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

Sie benötigen ein angepasstes Event `reminder_capture`, und die angepassten Event-Eigenschaften müssen mindestens Folgendes enthalten:

- `reminder-id`: Bezeichner des angepassten Events
- `reminder_date`: Vom Nutzer bzw. der Nutzerin eingegebenes Datum, an dem die Erinnerung fällig ist
- `message_personalisation_X`: Alle Eigenschaften, die zur Personalisierung der Nachricht zum Zeitpunkt des Versands benötigt werden

{% endalert %}

### Einen String innerhalb eines Arrays suchen {#misc-string-in-array}

Dieser Anwendungsfall prüft, ob ein angepasstes Attribut-Array einen bestimmten String enthält, und zeigt in diesem Fall eine bestimmte Nachricht an.

{% raw %}
```liquid
{% if custom_attribute.${PartnershipProgramsNotLinked} contains 'Hertz' %}
Link your Hertz account to use Hertz Fast Lane.
{% endif %}
```
{% endraw %}

### Den größten Wert in einem Array finden {#misc-largest-value}

Dieser Anwendungsfall berechnet den höchsten Wert in einem gegebenen angepassten Attribut-Array zur Verwendung in Nachrichten an Nutzer:innen.

Zum Beispiel können Sie einem Nutzer bzw. einer Nutzerin den aktuellen Highscore oder das höchste Gebot für einen Artikel anzeigen.

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

### Den kleinsten Wert in einem Array finden {#misc-smallest-value}

Dieser Anwendungsfall berechnet den niedrigsten Wert in einem gegebenen angepassten Attribut-Array zur Verwendung in Nachrichten an Nutzer:innen.

Zum Beispiel können Sie einem Nutzer bzw. einer Nutzerin die niedrigste Punktzahl oder den günstigsten Artikel anzeigen.

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

### Das Ende eines Strings abfragen {#misc-query-end-of-string}

Dieser Anwendungsfall fragt das Ende eines Strings für die Verwendung in Nachrichten ab.

{% raw %}
```liquid
{% assign interest = {{custom_attribute.${Buyer Interest}}} | first %}
{% assign marketplace = {{interest}} | split: "" | reverse | join: "" |  truncate: 4, "" %}
{% if {{marketplace}} == '3243' %}

Your last marketplace search was on {{custom_attribute.${Last marketplace buyer interest}}} | date: '%d.%m.%Y'}}. Check out all of our new offers.

{% else %}
{% abort_message() %}