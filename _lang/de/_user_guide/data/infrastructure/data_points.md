---
nav_title: Datenpunkte
article_title: Datenpunkte – Übersicht
page_order: 10
page_type: reference
description: "In diesem referenzierten Artikel erfahren Sie, welche Datenpunkte es bei Braze gibt und wie Sie sich über deren Verwendung informieren können."
search_rank: 6
---

# Datenpunkte

> Bei Braze sind Daten gleichbedeutend mit Aktion: Jede Information, die in Braze eingeht, aktualisiert die Segmente, kann Nachrichten triggern und stornieren, ist sofort für die Personalisierung von Nachrichten verfügbar und vieles mehr. Datenpunkte helfen Ihnen, die wichtigsten Informationen für Ihr Unternehmen zu definieren. Indem Sie sich genau überlegen, welche Daten Sie tracken wollen, stellen Sie sicher, dass Sie das Targeting für die Daten Ihrer Nutzer:innen mit dem höchsten Wirkungsgrad durchführen.

Die Datenpunkte basieren auf Informationen, die anhand von Nutzer:innen-Profilen aufgezeichnet wurden. Eine genauere Aufschlüsselung dieser Definition finden Sie in Ihrem Braze-Vertrag. Unser Customer-Success-Team kann Ihnen helfen, die besten Datenpraktiken an Ihre Bedürfnisse anzupassen. 

## Definition

"Datenpunkte" beziehen sich auf eine abrechenbare Nutzungseinheit der Braze Dienste, gemessen an einem Sitzungsbeginn, einem Sitzungsende, einem angepassten Event oder einem aufgezeichneten Kauf, sowie auf einen beliebigen Attribut-Satz in einem Endbenutzerprofil. Der Klarheit halber gilt jeder der oben genannten Datenpunkte (wie z.B. Sitzungsbeginn, Sitzungsende, angepasstes Event oder aufgezeichneter Kauf sowie jedes Attribut), die dem Profil eines Endnutzers zu einem bestimmten Zeitpunkt zugeordnet sind, als ein einzelner Datenpunkt.

Daten und Ereignisse, die standardmäßig von den Serviceleistungen; Diensten von Braze erfasst werden, wie z.B. Push-Token, Geräteinformationen und alle Ereignisse zur Verfolgung des Engagements in Kampagnen, wie z.B. die Öffnung von E-Mails und Klicks auf Push-Benachrichtigungen, werden *nicht* als Datenpunkte gezählt.

Lesen Sie den Abschnitt [Verbrauchszählung](#consumption-count) in diesem Artikel, um zu verstehen, welche Daten für die Zuweisung Ihrer Datenpunkte zählen.

## Anzeigen der Datenpunkt-Nutzung

Um Ihre Datenpunkt-Nutzung einzusehen, gehen Sie zu **Einstellungen** > **Abrechnung** und wählen Sie den Tab **Gesamtdatenpunkt-Nutzung**.

Weitere Informationen zu den Komponenten des Dashboards für Datenpunkte finden Sie unter [Abrechnung]({{site.baseurl}}/user_guide/administrative/app_settings/subscription_and_usage/).

{% alert tip %}
**Verschwenden Sie keine Datenpunkte. Aktualisieren Sie nur sich ändernde Daten!**<br><br>
Um die Datenpunkt-Nutzung zu minimieren, empfehlen wir Ihnen, ein Programm einzurichten, das verhindert, dass immer dieselben unveränderlichen Daten gesendet werden, und nur neue und relevante Daten an Braze weitergibt. Braze wird mit Ihnen zusammenarbeiten, um diese Best Practice während des Onboarding zu etablieren.
{% endalert %}

## Verbrauch zählen

Insgesamt werden Datenpunkte gesammelt, wenn die Profildaten eines Nutzers:innen aktualisiert werden oder wenn sie bestimmte Aktionen durchführen. Im Wesentlichen handelt es sich bei den Datenpunkten um die Anzahl der einzelnen `session starts`, `session ends`, `events` und `purchases` Ihrer Nutzer:innen.

In den folgenden Abschnitten finden Sie eine Aufschlüsselung, wie Braze Datenpunkte sammelt. Wenn Sie Fragen zu den Datenpunkten von Braze haben, kann Ihr Braze-Konto Manager:in sie beantworten.

Bei den folgenden Aktionen werden keine Datenpunkte protokolliert:
- Löschen von Nutzer:innen aus Braze
- Connected-Content im Messaging verwenden
- Änderungen des Abo-Status global und um Abo-Gruppen herum
- Umbenennung der externen IDs Ihrer Nutzer:innen durch [API-Aufrufe]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_rename/)
- Blockieren von Ereignissen, Attributen oder Event-Eigenschaften

### Besondere Umstände

#### Arrays

Ein Array ist eine geordnete Sammlung von Artikeln, die in einem angepassten Attribut gespeichert sind. Was den Verbrauch betrifft, so kostet das Update eines Arrays einen Datenpunkt pro API-Aufruf. Wenn Sie einem Array schrittweise Werte hinzufügen, wird dies als ein Datenpunkt pro Wert gezählt. 

{% alert tip %}
Wenn Sie das gesamte Array auf einmal setzen, wird es als ein einziger Datenpunkt gezählt. Daher sind Arrays ein hervorragendes Instrument, um Nutzer:innen-Profile mit relevanten Informationen auf dem neuesten Stand zu halten und Kosten zu senken.
{% endalert %}

#### Verschachtelte angepasste Attribute

Verschachtelte angepasste Attribute beziehen sich auf ein Objekt, das eine Reihe von Attributen als Eigenschaft eines anderen Attributs definiert. Jeder Schlüssel des Objekts gilt als Datenpunkt.

{% alert note %}
Das Update eines angepassten Attributs auf `null` verbraucht ebenfalls einen Datenpunkt.
{% endalert %}

#### CSV

Angepasste Attribute, die über den CSV-Import hochgeladen werden, zählen für Ihre Datenpunkte. Bei CSV-Importen zum Zwecke der Segmentierung (Importe mit `external_id`, `braze_id` oder `user_alias_name` als einzigem Feld) werden jedoch keine Datenpunkte protokolliert.

Da bei Änderungen des Abo-Status keine Datenpunkte protokolliert werden, fallen auch beim Update der Felder `email_subscribe`, `push_subscribe`, `subscription_group_id` oder `subscription_state` in Ihrer CSV-Datei keine Kosten an.

## Datenpunkte

{% alert note %}
Die folgenden Tabellen sind zur Veranschaulichung gedacht. Die genauen Namenskonventionen, die Großschreibung und die akzeptierten Werte für bestimmte Felder finden Sie in der entsprechenden Dokumentation für Ihre Ingestionsmethode.
{% endalert %}

{% tabs %}
{% tab Non-billable %}

#### Nicht fakturierbare Datenpunkte (Standard)

<div class="small_table"></div>

| Datentyp | Datenpunkt |
| --------- | ---------- |
| Profil Daten | Land |
| Profil Daten | Sprache |
| Profil Daten | Nutzer-ID |
| Profil Daten | Nutzer:in alias |
| Neueste Geräte | Anzahl der Geräte |
| Neueste Geräte | Letzte Uhr |
| Neueste Geräte | Version der App |
| Neueste Geräte | Gerät |
| Neueste Geräte | Betriebssystem |
| Kontakt-Einstellungen | E-Mail abonniert |
| Kontakt-Einstellungen | Push abonniert |
| Kontakt-Einstellungen | Für Push registrierte Apps |
| Kontakt-Einstellungen | Abo-Gruppe |
| Erhaltene Kampagnen | E-Mail-Adresse |
| Install-Attribution | Quelle installieren |
| Install-Attribution | Kampagne |
| Install-Attribution | Anzeigengruppe |
| Install-Attribution | Werbung |
| Verschiedenes | Zufällige Bucket-Nummer |
| Empfangene Canvas Nachrichten | Empfangene Canvas Nachrichten |
| Messaging Engagement | Alle Engagement-Ereignisse (wie Öffnungen, Klicks, Impressionen und Abbrüche) |
| Twitter | Follower |
| Twitter | Nach |
| Twitter | Anzahl von Tweets |
| Facebook | Mag |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Billable %}

#### Abrechenbare Datenpunkte

{% alert important %}
Das Hinzufügen, Entfernen oder Aktualisieren der folgenden Datentypen führt zu einem kostenpflichtigen Datenpunkt.
{% endalert %}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 30%;
}
table th:nth-child(3) {
    width: 50%;
}
table td {
    word-break: break-word;
}
</style>

| Datentyp | Datenpunkt | Anmerkungen |
| --------- | ---------- | ----- |
| Profil Daten | Vorname | |
| Profil Daten | Nachname | |
| Profil Daten | E-Mail-Adresse | |
| Profil Daten | Geschlecht | |
| Profil Daten | Altersgruppe | |
| Profil Daten | Land | Bei manueller Erfassung. Zählt nicht zum Verbrauch, wenn es automatisch gesammelt wird. |
| Profil Daten | Ort | |
| Profil Daten | Sprache | Bei manueller Erfassung. Zählt nicht zum Verbrauch, wenn es automatisch gesammelt wird. |
| Profil Daten | Neueste Lokalisierung des Geräts | |
| Profil Daten | Zeitzone | |
| Profil Daten | Geburtsdatum (DOB) | |
| Profil Daten | Bio | |
| Profil Daten | Telefonnummer | |
| Daten zur App-Nutzung | Beginn der Sitzung | |
| Daten zur App-Nutzung | Ende der Sitzung | |
| Angepasste Attribute | Alle angepassten Attribute | |
| Angepasste Events | Alle angepassten Events | |
| Benutzerdefinierte Ereigniseigenschaften | Alle angepassten Event-Eigenschaften | Angepasste Event-Eigenschaften, die für die Segmentierung mit den Filtern `X Custom Event Property in Y Days` oder `X Purchase Property in Y Days` aktiviert wurden, werden alle als separate Datenpunkte gezählt, zusätzlich zu dem Datenpunkt, der von dem angepassten Event selbst gezählt wird.
| Käufe | Alle Einkäufe | |
| Eigenschaften des Kaufs | Alle Kauf-Details | |
| Zuweisung der Amplitude-Kohorte | Alle Zuweisungen | |
| Zuweisung der Mixpanel-Kohorte | Alle Zuweisungen | |
| Zuweisung der Hightouch Kohorte | Alle Zuweisungen | |
| Appsflyer Kohorten-Zuordnung | Alle Zuweisungen | |
| Jüngster Standort | Alle aktuellen Standorte | Beim Betreten oder Verlassen von Geoofences werden keine Datenpunkte protokolliert, da Geofence-Daten nicht im Nutzerprofil gespeichert sind. Geofences werden von Apple und Google Serviceleistungen; Diensten überwacht; Braze wird nur benachrichtigt, wenn ein Nutzer:innen einen Geofence triggert. |
| Twitter | Nutzername | |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

