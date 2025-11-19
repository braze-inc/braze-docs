---
nav_title: Anwendungsfall Sammlung
article_title: Anwendungsfälle für die Sammlung
page_order: 3
page_type: reference
description: "Dieser referenzierte Artikel behandelt einen Anwendungsfall zur Datenerfassung, wie eine Mitfahr-App entscheiden könnte, welche Nutzerdaten sie erfassen soll."

---

# Anwendungsfall Sammlung

> Dieser Artikel befasst sich mit einem Anwendungsfall zur Datenerfassung, wie eine Mitfahr-App entscheiden kann, welche Nutzer:innen Daten erfassen sollen.

Nehmen wir an, eine Taxi- oder Mitfahr-App namens StyleRyde möchte entscheiden, welche Nutzer:innen-Daten sie sammeln möchte. Die folgenden Fragen und der Brainstorming-Prozess sind ein hervorragendes Modell für ihre Marketing- und Entwickler:in-Teams. Am Ende dieser Übung sollten beide Teams ein solides Verständnis dafür haben, welche angepassten Events und -Attribute sinnvollerweise gesammelt werden sollten, um ihr Ziel zu erreichen.

## Fallfrage 1: Was ist das Ziel?

Das Ziel von StyleRyde ist ganz einfach: Die Nutzer sollen über die App Taxifahrten anfordern können.

## Fallfrage 2: Was sind die Schritte, um dieses Ziel nach der Installation der App zu erreichen?

1. StyleRyde verlangt von den Nutzer:innen, dass sie den Registrierungsprozess beginnen und ihre persönlichen Daten eingeben.
2. Bei StyleRyde müssen Nutzer:innen den Registrierungsprozess abschließen und überprüfen, indem sie einen Code in die App eingeben, den sie per SMS erhalten.
3. StyleRyde benötigt Nutzer:innen, die versuchen, ein Taxi anzuhalten.
4. StyleRyde muss verfügbar sein, wenn Nutzer:innen ein Taxi anhalten.

Diese Aktionen könnten dann als die folgenden angepassten Events getaggt werden:

- Beginn der Registrierung
- Abgeschlossene Registrierung
- Erfolgreiche Taxifahrten
- Erfolglose Taxi-Anrufe

Nach der Implementierung der Ereignisse kann StyleRyde Kampagnen wie die folgenden durchführen:

1. Nachrichten an Nutzer:innen, die die Registrierung begonnen, aber nicht innerhalb eines bestimmten Zeitrahmens abgeschlossen haben.
2. Senden Sie Nachrichten an Nutzer:innen, die die Registrierung abgeschlossen haben.
3. Schicken Sie Nutzern:innen, die erfolglos ein Taxi gerufen haben, auf das nicht innerhalb einer bestimmten Zeitspanne ein erfolgreiches Taxi gerufen wurde, eine Entschuldigung und eine Gutschrift für eine Aktion.
4. Senden Sie Aktionen an leistungsstarke Nutzer:innen mit vielen erfolgreichen Taxifahrten, um ihnen für ihre Treue zu danken.

## Fallfrage 3: Welche anderen Nutzer:innen-Informationen könnten wir sammeln und für unser Messaging verwenden?

- Haben die Nutzer:innen ein Aktionsguthaben?
- Die durchschnittliche Bewertung, die Nutzer:innen für ihre Fahrer abgeben?
- Eindeutige Promo-Codes für Nutzer:innen?

Diese Merkmale könnten dann als die folgenden angepassten Attribute getaggt werden:

- Aktionssaldo (Dezimaltyp)
- Durchschnittliche Fahrerbewertung (Typ Integer)
- Eindeutiger Promo Code (String Typ)

Diese Attribute ermöglichen es Ihnen, Kampagnen an Nutzer:innen zu senden:

1. Erinnern Sie Nutzer:innen, die die App sieben Tage lang nicht benutzt haben und über ein Aktionsguthaben verfügen, daran, zur App zurückzukehren und das Guthaben einzulösen.
2. Verwenden Sie unsere Templates für Nachrichten und die [Features zur Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/#personalized-messaging), um das eindeutige Attribut des Aktionscodes in die Nachrichten an die Nutzer:innen zu ziehen.

{% alert important %}
Braze sperrt Nutzer:innen mit mehr als 5.000.000 Sitzungen und nimmt ihre SDK-Ereignisse nicht mehr auf, da sie in der Regel das Ergebnis von Fehlintegration sind. Wenn Sie feststellen, dass dies bei einem rechtmäßigen Nutzer:in passiert ist, wenden Sie sich an Ihren Braze-Konto Manager:in.
{% endalert %}

