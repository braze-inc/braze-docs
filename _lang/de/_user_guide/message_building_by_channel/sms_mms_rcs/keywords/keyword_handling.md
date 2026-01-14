---
nav_title: Benutzerdefinierter Umgang mit Schlüsselwörtern
article_title: Benutzerdefinierte Schlüsselwortbehandlung
page_order: 3
description: "In diesem referenzierten Artikel erfahren Sie, wie Braze mit bidirektionalen SMS-, MMS- und RCS-Nachrichten und Auto-Responses umgeht. Beinhaltet Erläuterungen zur Funktionsweise von auslösenden Schlüsselwörtern, benutzerdefinierten Schlüsselwörtern und Mehrsprachigkeit."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# Benutzerdefinierter Umgang mit Schlüsselwörtern

> In diesem referenzierten Artikel erfahren Sie, wie Braze mit bidirektionalen SMS-, MMS- und RCS-Nachrichten und Auto-Responses umgeht. Beinhaltet Erläuterungen zur Funktionsweise von auslösenden Schlüsselwörtern, benutzerdefinierten Schlüsselwörtern und Mehrsprachigkeit.

## Zwei-Wege-Nachrichten (benutzerdefinierte Schlüsselwortantworten)

Mit Two-Way-Messaging können Sie Nachrichten senden und die Antworten auf diese Nachrichten verarbeiten. Dazu müssen die Endbenutzer ein Schlüsselwort an Braze senden, auf das sie dann eine automatische Antwort erhalten. Richtig angewandt, sind wechselseitige Nachrichten eine einfache, unmittelbare und dynamische Lösung für das Kundenmarketing und sparen Zeit und Ressourcen.

## Schlüsselwörter und automatische Antworten verwalten

SMS, MMS und RCS mit Braze bietet Ihnen die Möglichkeit, Schlüsselwort-Trigger und angepasste Antworten zu erstellen, Schlüsselwortsätze für mehrere Sprachen zu definieren und eigene Schlüsselwortkategorien einzurichten. 

{% tabs %}
{% tab Add Keyword Triggers %}

#### Auslösewörter hinzufügen

Zusätzlich zu den standardmäßigen Opt-In- und Opt-Out-Schlüsselwörtern können Sie auch Ihre eigenen Schlüsselwörter definieren, um Opt-In-, Opt-Out- und Hilfe-Antworten auszulösen.

Um Ihre eigenen Schlüsselwörter zu definieren, gehen Sie wie folgt vor:

1. Gehen Sie im Braze-Dashboard zu **Zielgruppe** > **Abo-Gruppen-Management** und wählen Sie eine **SMS/MMS/RCS** Abo-Gruppe aus.<br><br>
2. Wählen Sie unter **Globale Schlüsselwörter** das Bleistiftsymbol neben der Schlüsselwortkategorie aus, der Sie ein Schlüsselwort hinzufügen möchten. ![Opt-in-Schlüsselwörter, bei denen das Bleistiftsymbol angezeigt wird.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. In der sich öffnenden Registerkarte fügen Sie ein Stichwort hinzu, das diese Stichwortkategorie auslösen soll. Beachten Sie, dass bei den Schlüsselwörtern die Groß- und Kleinschreibung keine Rolle spielt und dass universelle Schlüsselwörter wie `START`, `YES` und `UNSTOP` nicht geändert werden können. ![Bearbeiten von Schlüsselwörtern für die Kategorie "Opt-in". Die hinzugefügten Schlüsselwörter sind "START", "UNSTOP" und "YES". Im Feld für die Antwortnachricht steht: "Sie haben Nachrichten von dieser Nummer abbestellt. Antworten Sie HELP für Hilfe. Antworten Sie STOP, um sich abzumelden. Es können Nachrichten- und Datengebühren anfallen."]({% image_buster /assets/img/sms/keyword_edit2.png %})

Die folgenden Regeln gelten für Schlüsselwörter und Schlüsselwortantworten:

| Keyword | Schlüsselwort-Antworten |
| -------- | ----------------- |
| \- Gültige UTF-8 kodierte Zeichen<br>\- Maximal 20 Schlüsselwörter pro Kategorie<br>\- Maximale Länge von 34 Zeichen<br>\- Mindestlänge von 1 Zeichen <br>\- Darf keine Leerzeichen enthalten<br>\- Groß- und Kleinschreibung muss nicht beachtet werden und muss in der gesamten Abonnementgruppe eindeutig sein. | \- Kann nicht leer sein<br>\- Maximale Länge von 300 Zeichen<br>\- Gültige UTF-8 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Möchten Sie sehen, wie diese Schlüsselwörter in Ihren Kampagnen und Canvases verwendet werden können, um Nachrichten erneut anzusprechen und auszulösen? Besuchen Sie [Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) für weitere Informationen.
{% endalert %}
{% endtab %}

{% tab Manage responses %}

#### Antworten verwalten

Sie können Ihre eigenen Antworten verwalten, die an Benutzer gesendet werden, nachdem diese ein Stichwort in eine bestimmte Stichwortkategorie eingegeben haben.

1. Gehen Sie im Braze-Dashboard zu **Zielgruppe** > **Abo-Gruppen-Management** und wählen Sie eine **SMS/MMS/RCS** Abo-Gruppe aus. <br><br>
2. Wählen Sie unter **Globale Schlüsselwörter** eine Schlüsselwortkategorie aus, für die Sie eine Antwort bearbeiten möchten, indem Sie das Bleistiftsymbol auswählen. ![Opt-in-Schlüsselwörter, bei denen das Bleistiftsymbol angezeigt wird.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br> 
3. In der sich öffnenden Registerkarte können Sie Ihre Antwort bearbeiten. Beachten Sie bei der Erstellung Ihrer Antwort unsere [sechs Regeln zur Einhaltung der Vorschriften]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) und lesen Sie die folgenden Regeln, die für Schlüsselwörter und Schlüsselwortantworten gelten. ![Antworten]({% image_buster /assets/img/sms/keyword_home.png %}){: style="max-width:70%;"}<br><br>
4. Um statische URLs in Ihrer Antwort automatisch zu verkürzen, aktivieren Sie die Option **Linkverkürzung**. Der Zeichenzähler wird aktualisiert, um die erwartete Länge der gekürzten URL anzuzeigen. ![Ein GIF, das zeigt, wie der Zeichenzähler aktualisiert wird, wenn das Umschalten von "Linkverkürzung" aktiviert ist.]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:60%;"}

##### Überlegungen

| Keyword | Schlüsselwort-Antworten |
| -------- | ----------------- |
| \- Gültige UTF-8 kodierte Zeichen<br>\- Maximal 20 Schlüsselwörter pro Kategorie<br>\- Maximale Länge von 34 Zeichen<br>\- Mindestlänge von 1 Zeichen <br>\- Darf keine Leerzeichen enthalten<br>\- Groß- und Kleinschreibung muss nicht beachtet werden und muss in der gesamten Abonnementgruppe eindeutig sein. | \- Kann nicht leer sein<br>\- Maximale Länge von 300 Zeichen<br>\- Gültige UTF-8 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

{% alert tip %}
Wenn ein aktionsbasiertes Canvas durch eine eingehende SMS-, MMS- oder RCS-Nachricht ausgelöst wird, können Sie im ersten [Nachrichten-Schritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) des Canvas auf SMS-, MMS- oder RCS-Eigenschaften referenzieren.
{% endalert %}

## Unterstützung mehrerer Sprachen

Beim Versand in bestimmte Länder kann es erforderlich sein, muss der Absender ggf. eingehende Schlüsselwörter und ausgehende Antworten in der Landessprache unterstützen. Dazu können Sie mit Braze eine sprachspezifische Schlüsselwortkonfiguration erstellen.
![Dropdown mit den Sprachen, die Sie als Schlüsselworteinstellung hinzufügen können.]({% image_buster /assets/img/sms/multi-language.png %}){: style="float:right;max-width:50%;margin-left:10px;"}

### Sprachspezifische Schlüsselwörter erstellen

Wählen Sie **Sprache hinzufügen** und wählen Sie Ihre Zielsprache aus oder suchen Sie in der Dropdown-Liste nach einer Sprache.

{% alert important %}
Für nicht-englische Sprachen gibt es keine voreingestellten Schlüsselwörter und Antworten, so dass Absender mit ihren Marketing- und Rechtsteams zusammenarbeiten müssen, um alle erforderlichen Schlüsselwörter zu diesem Satz hinzuzufügen. Andernfalls wird Braze keine lokalisierten eingehenden Nachrichten für diese Sprachen verarbeiten.
{% endalert %}

Wenn Sie eine Sprache löschen möchten, wählen Sie den Button **Sprache löschen** unten rechts.

![Seite Globale Schlüsselwörter mit ausgewähltem Tab "Italienisch". Für jede hinzugefügte Sprache gibt es zusätzliche Registerkarten.]({% image_buster /assets/img/sms/multi-language2.png %})

## Benutzerdefinierte Stichwortkategorien

Zusätzlich zu den drei Standardkategorien für Schlüsselwörter (Opt-in, Opt-out und Hilfe) können Sie bis zu 25 weitere Kategorien erstellen. Auf diese Weise können Sie beliebige Schlüsselwörter identifizieren und für Ihr Unternehmen spezifische Antworten einrichten. Ein Beispiel dafür ist "PROMO" oder "DISCOUNT" mit einer Antwort zu den im jeweiligen Monat laufenden Werbeaktionen. 

Diese benutzerdefinierten Schlüsselwörter sind immer aktiv, d.h. jeder Benutzer, der Ihren Nachrichtendienst abonniert hat, kann Schlüsselwörter texten und jederzeit eine Antwort erhalten. Zusätzlich zu diesem Verhalten haben Sie auch die Möglichkeit, bestimmte Schlüsselwörter zu definieren, die nur zu [bestimmten Zeitpunkten]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords) im Lebenszyklus Ihres Benutzers gesendet werden können. 

![Stichwörter für eine "Promo"-Kategorie. Wenn ein Nutzer:innen "YO" schreibt, erhält er die Nachricht mit einem Promo Code.]({% image_buster /assets/img/sms/sms_custom_keyword.png %})

### Erstellen einer benutzerdefinierten Kategorie

Um eine benutzerdefinierte Stichwortkategorie zu erstellen, gehen Sie wie folgt vor:

1. Bearbeiten Sie die entsprechende Abonnementgruppe.
2. Wählen Sie **Angepasstes Schlüsselwort hinzufügen**. Felder, um neue Schlüsselwörter hinzuzufügen.]({% image_buster /assets/img/sms/sms_custom_step.png %}){: style="max-width:90%;"}
3. Geben Sie den Namen für die Stichwortkategorie ein und legen Sie fest, welche Stichwörter eine Antwort auslösen.

Nachdem Sie diese Stichwortkategorie erstellt haben, können Sie sie in Ihren Kampagnen und Canvases [filtern und auslösen]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/).

Schlüsselwörter, die in benutzerdefinierten Schlüsselwortkategorien erstellt werden, erfüllen alle Regeln und Validierungen für die Erstellung neuer Schlüsselwörter. 

### Lebenszyklus-spezifische Schlüsselwörter

Wenn Sie einen Anwendungsfall haben, bei dem Sie einschränken möchten, wann ein Kunde ein bestimmtes Schlüsselwort während seines Lebenszyklus senden kann (z.B. während seines ersten Onboardings), um eine Antwort zu erhalten, können Sie den Auslöser **Gesendete eingehende SMS an Abonnementgruppe innerhalb der Schlüsselwortkategorie ANDERE** in Ihrer Kampagne oder Ihrem Canvas verwenden und Schlüsselwörter definieren, die Ihre Benutzer zu einem bestimmten Zeitpunkt senden können.

Dieser Auslöser unterstützt das Filtern der eingehenden Nachricht mittels "ist" und "ist nicht" sowie Regex-Regeln zur Validierung der Benutzereingaben.

#### Canvas

![Aktionsbasierter Canvas-Schritt mit dem Auslöser Eingehende SMS an die Abo-Gruppe "Messaging Service" innerhalb der Schlüsselwortkategorie "Andere" senden, wenn der Nachrichtentext dem regulären Ausdruck "Caret-Symbol überspringen" entspricht.]({% image_buster /assets/img/sms/canvas_trigger.png %}){: style="max-width:90%;"}

#### Kampagne

![Aktionsbasierte Kampagne mit dem Auslöser Eingehende SMS an die Abo-Gruppe "Marketing Message Service A" innerhalb der Keyword-Kategorie "Andere" senden, wobei der Nachrichtentext "Keyword1" oder "Keyword2" oder nicht "Keyword A" ist.]({% image_buster /assets/img/sms/campaign_trigger.png %}){: style="max-width:90%;"}

### Umgang mit unbekannten Schlüsselwörtern

Es ist zwar nicht erforderlich, aber wir empfehlen dringend, eine automatische Antwort einzurichten, wenn Nutzer:innen eingehende Schlüsselwörter senden, die nicht mit einem bestehenden Schlüsselwort übereinstimmen. Diese Meldung weist darauf hin, dass das Schlüsselwort nicht erkannt wurde, und enthält eine Anleitung. 

Dazu können Sie eine SMS-, MMS- oder RCS-Kampagne mit einer Nachricht wie "Sorry! dieses Schlüsselwort kennen wir nicht. Schreiben Sie STOP, um anzuhalten oder HELP, um Hilfe zu erhalten." erstellen. Als Nächstes wählen Sie im Schritt Zustellung die Option **Aktionsbasierte Zustellung** und verwenden den Auslöser **Eingehende SMS an Abonnementgruppe innerhalb der Stichwortkategorie ANDERE**.

![Aktionsbasiertes Senden für eine Kampagne mit dem Trigger "Eingehende SMS an Abo-Gruppe innerhalb der Schlüsselwortkategorie "Sonstige" gesendet".]({% image_buster /assets/img/sms/sms_other.png %})

{% alert tip %}
Möchten Sie sehen, wie diese Schlüsselwörter und Schlüsselwortkategorien in Ihren Kampagnen und Canvases für Retargeting und Trigger-Nachrichten verwendet werden können? Besuchen Sie [Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) für weitere Informationen.
{% endalert %}

