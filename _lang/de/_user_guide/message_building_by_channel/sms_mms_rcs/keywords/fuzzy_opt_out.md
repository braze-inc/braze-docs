---
nav_title: Fuzzy-Opt-out
article_title: Fuzzy Opt-out
description: "In diesem Referenzartikel erfahren Sie, wie Sie das Fuzzy-Opt-out konfigurieren, eine Einstellung, die erkennt, wenn eine eingehende Nachricht nicht mit einem Opt-out-Schlüsselwort übereinstimmt."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
page_order: 1

---

# Fuzzy-Opt-out

![iOS Messaging, das ausgehende Opt-out Nachrichten als Antwort auf das eingehende Fuzzy Opt-out "Please stopppp" anzeigt.]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Nutzer:innen, die SMS, MMS und RCS mit Braze versenden, müssen sich an die geltenden Gesetze, Vorschriften und Branchenstandards halten, die definiert sind. Beim Opt-out schreiben die Gesetze vor, dass alle nachfolgenden Nachrichten im Zusammenhang mit diesem Messaging-Programm gestoppt werden, wenn ein:e Nutzer:in "STOP" schreibt. Braze verarbeitet diese Nachrichten automatisch und meldet den Benutzer ab.<br><br>Fuzzy Opt-Out versucht zu erkennen, wenn eine eingehende Nachricht nicht mit einem [Opt-Out-Schlüsselwort]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/) übereinstimmt, aber eine Opt-Out-Absicht erkennen lässt. Wenn Fuzzy Opt-out aktiviert ist und eine eingehende Keyword-Antwort als "unscharf" eingestuft wird, antwortet Braze automatisch mit einer Nachricht, die die Nutzer:innen auffordert, sich abzumelden.

Derzeit werden nur Opt-out-Schlüsselwörter unterstützt, die in Englisch als [lokaler Sprache]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support) erstellt wurden.

## Was wird als unscharf angesehen?

Die Kriterien, nach denen eine eingehende Antwort als "unscharf" eingestuft wird, lauten wie folgt:
- Wenn Sie bei einem QWERTY-Schlüsselwort einen Buchstaben mit dem Buchstaben eins links oder rechts daneben vertauschen, erhalten Sie ein passendes Opt-out-Schlüsselwort.
- Eine Teilzeichenkette der Nachricht stimmt mit einem Opt-out-Schlüsselwort überein.

Zum Beispiel werden "Stpo" oder "Bitte stopppp" als unscharf angesehen und eine unscharfe Opt-out-Antwort wird gesendet. Wenn der Nutzer:in dann mit einem Opt-in-Schlüsselwort antwortet, wird ein Abmelde-Ereignis getriggert.

## Fuzzy Opt-Out konfigurieren

Um das Fuzzy-Opt-out zu konfigurieren, navigieren Sie zur Seite Abo-Gruppen Schlüsselwortverwaltung.

1. Gehen Sie zu **Zielgruppe** > **Abo-Gruppen-Management** und wählen Sie eine **SMS/MMS/RCS** Abo-Gruppe aus.
2. Suchen Sie unter **Globale Schlüsselwörter** die **Opt-in-Kategorie** und wählen Sie das Bleistiftsymbol aus.
3. Aktivieren Sie **Fuzzy Opt-Out**, indem Sie die Option einschalten.
4. Ändern Sie die Fuzzy-Opt-in-Antwort wie gewünscht. 

![Abschnitt zum Bearbeiten von Opt-in-Schlüsselwörtern.]({% image_buster /assets/img/sms/fuzzy2.png %})

## Bewährte Verfahren für unscharfe Opt-out Nachrichten

Um ein klares, gesetzeskonformes und positives Erlebnis für Ihre Abonnenten zu gewährleisten, müssen Sie Ihre unscharfe Opt-out Nachricht sorgfältig konfigurieren. Der Hauptzweck der unscharfen Opt-out-Nachricht besteht darin, **Nutzer:innen zu leiten, die eine Nachricht senden, die dem von Ihnen festgelegten Opt-out-Schlüsselwort ähnelt, aber nicht genau diesem entspricht**. Die Nachricht fordert die Nutzer:innen auf, sich erfolgreich abzumelden.

### Kritische Überlegungen

{% alert warning %}
Konfigurieren Sie Ihre unscharfe Opt-out Nachricht **NICHT**, um eine Abmeldung zu bestätigen. Ihre unscharfe Opt-out Nachricht darf keine Formulierungen enthalten, die andeuten, dass ein Nutzer:innen sich bereits erfolgreich abgemeldet hat. Verwenden Sie zum Beispiel **nicht** "Sie wurden abgemeldet", "Sie werden keine Nachrichten mehr von dieser Nummer erhalten" oder "Sie haben sich jetzt abgemeldet".
{% endalert %}

Die unscharfe Opt-Out Nachricht wird gesendet, bevor der Nutzer:innen sich erfolgreich abgemeldet hat. Die Verwendung der Bestätigungssprache führt den Abonnenten zu der Annahme, dass er abgemeldet ist, obwohl dies nicht der Fall ist. Dies führt zu weiteren unerwünschten Nachrichten, zur Frustration der Abonnenten und zu erheblichen Compliance-Risiken.

{% alert warning %}
Konfigurieren Sie Ihre unscharfe Opt-out Nachricht **NICHT** so, dass sie mit Ihrem exakten Opt-out Schlüsselwort identisch oder diesem ähnlich ist.
{% endalert %}

Wenn Ihre unscharfe Nachricht mit Ihrem exakten Opt-out-Schlüsselwort identisch ist oder diesem zu nahe kommt (z.B. wenn "STOP" Ihr exaktes Schlüsselwort ist und Ihre unscharfe Nachricht "Text STOP um sich abzumelden" lautet), kann dies Verwirrung darüber stiften, ob die ursprüngliche Nachricht des Nutzers:in tatsächlich zu einer Abmeldung geführt hat oder ob er eine andere Aktion durchführen muss. Die unscharfe Nachricht sollte immer klarstellen, welche Aktion der Nutzer:in durchführen muss.

### Beispiele für unscharfe Opt-out Nachrichten

Konzentrieren Sie sich auf die Anleitung der Nutzer:innen. Wenn Ihr Opt-in-Schlüsselwort zum Beispiel "STOP" lautet, sind dies gute und schlechte Beispiele für unscharfe Opt-in-Nachrichten, die Sie erstellen könnten:

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Gute Beispiele <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Schlechte Beispiele <span aria-hidden="true">🚫.</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Um sich von allen Nachrichten abzumelden, antworten Sie bitte mit dem Wort STOP."</td>
      <td>"Sie haben sich erfolgreich abgemeldet. Sie werden keine Nachrichten mehr von dieser Nummer erhalten. Antworten Sie START, um sich erneut anzumelden." (Dies ist eine direkte Bestätigung des Abmeldens, was in einem unscharfen Opt-out-Szenario irreführend ist).</td>
    </tr>
    <tr>
      <td>"Wir haben Ihre Nachricht erhalten. Wenn Sie keine SMS mehr erhalten möchten, schreiben Sie bitte STOP."</td>
      <td>"STOP" (Dies ist nur das exakte Schlüsselwort selbst, das den Nutzer:in nicht anleitet.)</td>
    </tr>
    <tr>
      <td>"Wollten Sie sich abmelden? Antworten Sie STOP, um alle zukünftigen Nachrichten abzubestellen."</td>
      <td>"Schreiben Sie STOPP, um sich abzumelden" (Wenn "STOPP" auch Ihr genaues Schlüsselwort ist, ist dies redundant und klärt die Aktion nicht, wenn die ursprüngliche Nachricht unscharf war).</td>
    </tr>
  </tbody>
</table>
