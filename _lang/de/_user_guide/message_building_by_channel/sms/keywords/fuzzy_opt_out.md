---
nav_title: Fuzzy Opt-out
article_title: Fuzzy Opt-out
description: "In diesem Referenzartikel erfahren Sie, wie Sie das Fuzzy-Opt-out konfigurieren, eine Einstellung, die erkennt, wenn eine eingehende Nachricht nicht mit einem Opt-out-Schlüsselwort übereinstimmt."
page_type: reference
channel:
  - SMS
page_order: 1

---

# Fuzzy-Opt-out

![][1]{: style="float:right;max-width:30%;margin-left:15px;"}

> Nutzer:innen, die mit Braze SMS versenden, müssen sich an die geltenden Gesetze, Vorschriften und Branchenstandards halten, die definiert sind. Beim Opt-out schreiben die Gesetze vor, dass alle nachfolgenden Nachrichten im Zusammenhang mit diesem Messaging-Programm gestoppt werden, wenn ein:e Nutzer:in "STOP" schreibt. Braze verarbeitet diese Nachrichten automatisch und meldet den Benutzer ab.<br><br>Fuzzy Opt-Out versucht zu erkennen, wenn eine eingehende Nachricht nicht mit einem [Opt-Out-Schlüsselwort]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/optin_optout/) übereinstimmt, aber eine Opt-Out-Absicht erkennen lässt. Wenn Fuzzy Opt-out aktiviert ist und eine eingehende Keyword-Antwort als "unscharf" eingestuft wird, antwortet Braze automatisch und fordert die:den Nutzer:in auf, ihre:seine Absicht zu bestätigen. 

Derzeit werden nur Opt-out-Schlüsselwörter unterstützt, die in Englisch als [lokaler Sprache]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support) erstellt wurden.

## Was wird als unscharf angesehen?

Die Kriterien, nach denen eine eingehende Antwort als "unscharf" eingestuft wird, lauten wie folgt:
- Wenn Sie bei einem QWERTY-Schlüsselwort einen Buchstaben mit dem Buchstaben eins links oder rechts daneben vertauschen, erhalten Sie ein passendes Opt-out-Schlüsselwort.
- Eine Teilzeichenkette der Nachricht stimmt mit einem Opt-out-Schlüsselwort überein.

Zum Beispiel werden "Stpo" oder "Bitte stopppp" als unscharf angesehen und eine unscharfe Opt-out-Antwort wird gesendet.

## Fuzzy Opt-Out konfigurieren

Um das Fuzzy-Opt-out zu konfigurieren, navigieren Sie zur Seite Abo-Gruppen Schlüsselwortverwaltung.

1. Gehen Sie zu **Zielgruppe** > **Abonnements** und wählen Sie eine SMS-Abonnementgruppe.

{:start="2"}
2\. Suchen Sie unter **SMS Global Keywords** die Kategorie **Opt-out** und wählen Sie das Bleistiftsymbol.
3\. Aktivieren Sie **Fuzzy Opt-Out**, indem Sie die Option einschalten.
4\. Ändern Sie die Fuzzy-Opt-in-Antwort wie gewünscht. 

![][2]{: style="max-width:70%;"}

[1]: {% image_buster /assets/img/sms/fuzzy1.jpg %}
[2]: {% image_buster /assets/img/sms/fuzzy2.png %}

