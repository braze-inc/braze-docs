---
nav_title: Tutorials
article_title: "Tutorials: Schreiben von Liquid-Code"
page_order: 11
description: "Diese Referenzseite enthält anfängerfreundliche Anleitungen, die Ihnen den Einstieg in den Liquid-Code erleichtern."
page_type: tutorial
---

# Tutorials: Schreiben von Liquid-Code

> Neu bei Liquid? Diese Tutorials helfen Ihnen dabei, Liquid-Code für anfängerfreundliche Anwendungsfälle zu schreiben. Jedes Tutorial behandelt eine andere Kombination von Lernzielen, z.B. bedingte Logik und Operatoren.

Nach Abschluss dieser Tutorials können Sie Folgende Aktionen ausführen:

- Schreiben Sie Liquid-Code für gängige Anwendungsfälle
- Bedingte Liquid-Logik zusammenstellen, um Nachrichten auf der Grundlage von Nutzerdaten zu personalisieren.
- Variablen und Filter verwenden, um Gleichungen zu schreiben, die die Werte von Attributen verwenden
- Grundlegende Befehle im Liquid Code zu erkennen und ein allgemeines Verständnis dafür zu entwickeln, was der Code tut

| Tutorial | Lernziele |
| --- | --- |
| [Personalisieren Sie Nachrichten für Benutzersegmente](#segments) | Standardwerte, bedingte Logik |
| [Erinnerungen an verlassene Einkaufswagen](#reminders) | Operatoren, bedingte Logik |
| [Countdown für das Event](#countdown) | Variablen, Datumsfilter |
| [Monatliche Geburtstagsnachricht](#birthday) | Variablen, Datumsfilter, Operatoren |
| [Lieblingsprodukt bewerben](#favorite-product) | Variablen, Datumsfilter, Gleichungen, Operatoren |
{: .reset-br-td-1 .reset-br-td-2}

## Personalisierte Nachrichten für Benutzersegmente {#segments}

Lassen Sie uns Nachrichten für verschiedene Benutzersegmente, wie VIP-Kunden und neue Abonnenten, anpassen.

1. Öffnen Sie die Nachricht mit personalisierten Begrüßungen, die Sie senden können, wenn Sie den Vornamen eines Benutzers haben oder nicht haben. Erstellen Sie dazu ein Liquid-Tag, das das Attribut `first_name` und einen Standardwert enthält, der verwendet wird, wenn `first_name` leer ist. In diesem Szenario verwenden wir „Reisende:r“ als Standardwert.

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2\. Lassen Sie uns nun die Nachricht eingeben, die gesendet werden soll, wenn der oder die Nutzer:in ein:e VIP-Kund:in ist. Hierfür müssen wir einen Tag mit bedingter Logik verwenden: `if`. Dieser Tag besagt, dass, wenn das nutzerdefinierte Attribut `vip_status` gleich `VIP` ist, das folgende Liquid ausgeführt wird. In diesem Fall wird eine spezielle Nachricht gesendet.

{% raw %}
```liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3\. Lassen Sie uns eine nutzerdefinierte Nachricht an Nutzer:innen senden, die neue Abonnent:innen sind. Wir verwenden das Tag `elsif` für bedingte Logik, um festzulegen, dass die folgende Nachricht gesendet wird, wenn die `vip_status` des Nutzers oder der Nutzerin `new` ist.

{% raw %}
```liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4\. Was ist mit den Nutzer:innen, die nicht VIP oder neu sind? Wir können eine Nachricht an alle anderen Benutzer mit dem Tag `else` senden, die angibt, dass die folgende Nachricht gesendet werden soll, wenn die vorherigen Bedingungen nicht erfüllt sind. Dann können wir die bedingte Logik mit dem Tag `endif` schließen, da es keine weiteren VIP-Status zu berücksichtigen gibt.

{% raw %}
```liquid
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}
{% enddetails %}

## Erinnerungen an verlassene Einkaufswagen {#reminders}

Senden Sie personalisierte Nachrichten, um Benutzer an Artikel zu erinnern, die sich noch in ihrem Warenkorb befinden. Wir passen sie außerdem an die Anzahl der Artikel im Warenkorb an, sodass wir alle Artikel auflisten, wenn sie mehr als drei Artikel oder weniger haben. Wenn es mehr als drei Artikel sind, senden wir eine kürzere Nachricht.

1. Lassen Sie uns prüfen, ob der Einkaufswagen des Nutzers oder der Nutzerin leer ist, indem wir eine bedingte Liquid-Logik mit dem Operator `!=` öffnen, was „ist nicht gleich“ bedeutet. In diesem Fall setzen wir die Bedingung, dass das angepasste Attribut `cart_items` nicht gleich einem leeren Wert ist.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2\. Dann müssen wir unseren Fokus eingrenzen und prüfen, ob der Warenkorb mehr als drei Artikel enthält, indem wir den Operator \`>' verwenden, der „größer als“ bedeutet.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3\. Schreiben Sie eine Nachricht, die den oder die Nutzer:in mit seinem oder ihrem Vornamen begrüßt, oder verwenden Sie nur „Hallo“ als Standardwert, wenn dieser nicht verfügbar ist. Geben Sie an, was angegeben werden soll, wenn sich mehr als drei Artikel im Warenkorb befinden. Da wir den oder die Nutzer:in nicht mit einer vollständigen Liste überfordern möchten, listen wir nur die ersten drei `cart_items` auf.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4\. Verwenden Sie das Tag `else`, um anzugeben, was geschehen soll, wenn die vorherigen Bedingungen nicht erfüllt sind (mit anderen Worten, wenn `cart_items` leer oder weniger als drei ist), und geben Sie dann die zu sendende Nachricht an. Da drei Artikel nicht viel Platz beanspruchen, können wir sie alle auflisten. Wir verwenden die Liquid-Operatoren `join` und `,` und geben damit an, dass die Elemente mit einem Komma getrennt aufgelistet werden sollen. Schließen Sie die Logik mit `endif`.

{% raw %}
```liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you. 
{% endif %}
```
{% endraw %}

{: start="5"}
5\. Verwenden Sie `else` und dann `abort_message`, um dem Liquid-Code mitzuteilen, dass keine Nachricht gesendet werden soll, wenn der Warenkorb keine der vorherigen Bedingungen erfüllt. Mit anderen Worten, wenn der Einkaufswagen leer ist. Schließen Sie die Logik mit `endif`.

{% raw %}
```liquid
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Countdown für das Event {#countdown}

Senden Sie Nutzer:innen eine Nachricht, die angibt, wie viele Tage noch bis zu einem Jubiläumsverkauf verbleiben. Dazu verwenden wir Variablen, mit denen wir Gleichungen erstellen können, die die Werte von Attributen manipulieren.

1. Lassen Sie uns zunächst die Variable `sale_date` dem benutzerdefinierten Attribut `anniversary_date` zuweisen und den Filter `date: "s"` anwenden. Damit wird `anniversary_date` in ein Zeitstempelformat konvertiert, das in Sekunden ausgedrückt ist, und dieser Wert wird dann `sale_date` zugewiesen.

{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2\. Wir müssen auch eine Variable zuweisen, um den heutigen Zeitstempel zu erfassen. Weisen wir der Variablen `today` `now` (das aktuelle Datum und die aktuelle Uhrzeit) zu und wenden dann den Filter `date: "%s"` an.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3\. Lassen Sie uns nun berechnen, wie viele Sekunden zwischen jetzt (`today`) und dem Anniversary Sale (`sale_date`) liegen. Dazu weisen Sie der Variablen `difference` den Wert von `sale_date` minus `today` zu.

{% raw %}
```liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4\. Jetzt müssen wir `difference` in einen Wert umwandeln, auf den wir in einer Nachricht verweisen können, da es nicht ideal ist, dem oder der Nutzer:in mitzuteilen, wie viele Sekunden bis zum Verkauf verbleiben. Weisen wir `difference_days` der `event_date` zu und dividieren es durch `86400`, um die Anzahl der Tage zu erhalten.

{% raw %}
```liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5\. Zum Schluss erstellen wir die zu versendende Nachricht.

{% raw %}
```liquid
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}
{% enddetails %}

## Monatliche Geburtstagsnachricht {#birthday}

Lassen Sie uns allen Nutzern, die im heutigen Monat Geburtstag haben, ein spezielles Angebot zukommen. Benutzer, die in diesem Monat keinen Geburtstag haben, erhalten keine Nachricht.

1. Lassen Sie uns zunächst den heutigen Monat ziehen. Wir weisen der Variablen `this_month` `now` (das aktuelle Datum und die aktuelle Uhrzeit) zu und verwenden dann den Filter `date: "%B"`, um anzugeben, dass die Variable dem Monat entsprechen soll.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
```
{% endraw %}

{: start="2"}
2\. Lassen Sie uns nun den Geburtsmonat aus der `date_of_birth` des Benutzers abrufen. Wir weisen die Variable `birth_month` der Variable `date_of_birth` zu und verwenden dann den Filter `date: "%B"`.

{% raw %}
```liquid
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
```
{% endraw %}

{: start="3"}
3\. Da wir nun zwei Variablen haben, die einen Monat als Wert haben, können wir sie mit bedingter Logik vergleichen. Legen wir als Bedingung `date_of_birth` fest, die der `birth_month` des Nutzers oder der Nutzerin entspricht.

{% raw %}
```liquid
{% if {{this_month}} == {{birth_month}} %}
```
{% endraw %}

{: start="4"}
4\. Lassen Sie uns die Nachricht erstellen, die gesendet werden soll, wenn dieser Monat auch der Geburtsmonat des Nutzers oder der Nutzerin ist.

{% raw %}
```liquid
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
```
{% endraw %}

{: start="5"}
5\. Verwenden Sie das Tag `else`, um anzugeben, was passiert, wenn die Bedingung nicht erfüllt ist (weil dieser Monat nicht der Geburtsmonat des Nutzers oder der Nutzerin ist).

{% raw %}
```liquid
{% else %} 
```
{% endraw %}

{: start="6"}
6\. Wir wollen keine Nachricht senden, wenn der Geburtsmonat des Nutzers oder der Nutzerin nicht dieser Monat ist, also verwenden wir `abort_message`, um die Nachricht abzubrechen, und schließen dann die bedingte Logik mit `endif`.

{% raw %}
```liquid
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
{% else %} 
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## Werbung für Lieblingsprodukt {#favorite-product}

Lassen Sie uns das Lieblingsprodukt eines Nutzers bewerben, wenn sein letzter Kauf mehr als sechs Monate zurückliegt.

1. Zunächst verwenden wir eine bedingte Logik, um zu prüfen, ob wir das Lieblingsprodukt des Nutzers oder der Nutzerin und das Datum des letzten Kaufs haben.

{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
```
{% endraw %}

{: start="2"}
2\. Dann geben wir an, dass wir keine Nachricht senden sollen, wenn wir das Lieblingsprodukt oder das letzte Kaufdatum des Benutzers nicht haben.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="3"}
3\. Wir verwenden `else`, um festzulegen, was passieren soll, wenn die obige Bedingung nicht erfüllt ist (denn wir haben _das_ Lieblingsprodukt und das Datum des letzten Kaufs des Benutzers).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="4"}
4\. Wenn wir ein Kaufdatum haben, müssen wir es einer Variablen zuweisen, damit wir es mit dem heutigen Datum vergleichen können. Lassen Sie uns zunächst einen Wert für das heutige Datum erstellen, indem wir der Variablen `today` `now` (das aktuelle Datum und die aktuelle Uhrzeit) zuweisen und den Filter `date: "%s"` verwenden, um den Wert in ein Zeitstempelformat zu konvertieren, das in Sekunden ausgedrückt wird. Wir fügen den Filter `plus: 0` hinzu, um eine „0“ an den Zeitstempel anzuhängen. Dies ändert den Wert des Zeitstempels nicht, ist aber nützlich für die Verwendung des Zeitstempels in zukünftigen Gleichungen.


{% raw %}
```liquid
{% assign today = 'now' | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="5"}
5\. Lassen Sie uns nun das Datum des letzten Kaufs in Sekunden erfassen, indem wir die Variable `last_purchase_date` dem benutzerdefinierten Attribut `last_purchase_date` zuweisen und den Filter `date: "s"` verwenden. Wir fügen wieder den Filter `plus: 0` hinzu.

{% raw %}
```liquid
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="6"}
6\. Da das Datum des letzten Kaufs und das heutige Datum in Sekunden angegeben sind, müssen wir berechnen, wie viele Sekunden in sechs Monaten liegen. Lassen Sie uns eine Gleichung aufstellen (ungefähr 6 Monate * 30,44 Tage * 24 Stunden * 60 Minuten * 60 Sekunden) und sie der Variablen `six_months` zuweisen. Wir werden `times` verwenden, um die Multiplikation von Zeiteinheiten anzugeben.

{% raw %}
```liquid
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
```
{% endraw %}

{: start="7"}
7\. Da nun alle unsere Zeitwerte in Sekunden angegeben sind, können wir ihre Werte in Gleichungen verwenden. Weisen wir eine Variable namens `today_minus_last_purchase_date` zu, die den heutigen Wert nimmt und davon `last_purchase_date` abzieht. Dies zeigt uns, wie viele Sekunden seit dem letzten Kauf vergangen sind.

{% raw %}
```liquid
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
```
{% endraw %}

{: start="8"}
8\. Lassen Sie uns nun unsere Zeitwerte in bedingter Logik direkt vergleichen. Definieren wir die Bedingung, dass `today_minus_last_purchase_date` größer oder gleich (`>=`) sechs Monate ist. Mit anderen Worten: Das letzte Kaufdatum liegt mindestens sechs Monate zurück.

{% raw %}
```liquid
{% if today_minus_last_purchase_date >= six_months %}
```
{% endraw %}

{: start="9"}
9\. Lassen Sie uns die Nachricht erstellen, die gesendet werden soll, wenn der letzte Kauf mindestens sechs Monate zurückliegt.

{% raw %}
```liquid
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
```
{% endraw %}

{: start="10"}
10\. Mit dem Tag `else` geben wir an, was passieren soll, wenn die Bedingung nicht erfüllt ist (weil der Kauf noch nicht mindestens sechs Monate zurückliegt).

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="11"}
11\. Wir fügen eine `abort_message` hinzu, um die Nachricht zu löschen.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="12"}
12\. Zum Schluss schließen wir das Liquid mit zwei `endif` Tags ab. Das erste `endif`-Tag schließt die bedingte Prüfung für das bevorzugte Produkt oder das letzte Kaufdatum. Das zweite`endif`-Tag schließt die bedingte Prüfung für das letzte Kaufdatum, das mindestens sechs Monate zurückliegt.

{% raw %}
```liquid
{% endif %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
{% abort_message("No favorite product or last purchase date") %}
{% else %}
{% assign today = 'now' | date: "%s" | plus: 0 %}
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
{% if today_minus_last_purchase_date >= six_months %}
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
{% else %}
{% abort_message("Last purchase was less than six months ago") %}
{% endif %}
{% endif %}
```
{% endraw %}
{% enddetails %}
