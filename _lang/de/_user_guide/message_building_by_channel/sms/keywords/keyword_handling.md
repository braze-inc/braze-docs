---
nav_title: Benutzerdefinierte Schlüsselwortbehandlung
article_title: Benutzerdefinierte Schlüsselwortbehandlung
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Braze mit Zwei-Wege-SMS-Nachrichten und automatischen Antworten umgeht. Beinhaltet Erläuterungen zur Funktionsweise von auslösenden Schlüsselwörtern, benutzerdefinierten Schlüsselwörtern und Mehrsprachigkeit."
page_type: reference
channel:
  - SMS

---

# Benutzerdefinierter Umgang mit Schlüsselwörtern

> Dieser Referenzartikel beschreibt, wie Braze mit Zwei-Wege-SMS-Nachrichten und automatischen Antworten umgeht. Beinhaltet Erläuterungen zur Funktionsweise von auslösenden Schlüsselwörtern, benutzerdefinierten Schlüsselwörtern und Mehrsprachigkeit.

## Zwei-Wege-Nachrichten (benutzerdefinierte Schlüsselwortantworten)

Mit Two-Way-Messaging können Sie Nachrichten senden und die Antworten auf diese Nachrichten verarbeiten. Dazu müssen die Endbenutzer ein Schlüsselwort an Braze senden, auf das sie dann eine automatische Antwort erhalten. Richtig angewandt, sind wechselseitige Nachrichten eine einfache, unmittelbare und dynamische Lösung für das Kundenmarketing und sparen Zeit und Ressourcen.

## Schlüsselwörter und automatische Antworten verwalten

SMS mit Braze bietet Ihnen die Möglichkeit, Auslösewörter und benutzerdefinierte Antworten zu erstellen, Stichwortsätze für mehrere Sprachen zu definieren und benutzerdefinierte Stichwortkategorien einzurichten. 

{% tabs %}
{% tab Auslösewörter hinzufügen %}

#### Auslösewörter hinzufügen

Zusätzlich zu den standardmäßigen Opt-In- und Opt-Out-Schlüsselwörtern können Sie auch Ihre eigenen Schlüsselwörter definieren, um Opt-In-, Opt-Out- und Hilfe-Antworten auszulösen.

Um Ihre eigenen Schlüsselwörter zu definieren, gehen Sie wie folgt vor:

1. Gehen Sie im Braze-Dashboard zu **Audience** > **Abonnementgruppen** und wählen Sie Ihre SMS-Abonnementgruppe aus.<br><br>
2. Klicken Sie unter **SMS Global Keywords** auf das Bleistiftsymbol neben der Schlüsselwortkategorie, der Sie ein Schlüsselwort hinzufügen möchten. ![]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. In der sich öffnenden Registerkarte fügen Sie ein Stichwort hinzu, das diese Stichwortkategorie auslösen soll. Beachten Sie, dass bei den Schlüsselwörtern die Groß- und Kleinschreibung keine Rolle spielt und dass universelle Schlüsselwörter wie `START`, `YES` und `UNSTOP` nicht geändert werden können. ![Schlüsselwörter für die Kategorie "Opt-In" bearbeiten. Die hinzugefügten Schlüsselwörter sind "START", "UNSTOP" und "YES". Im Feld für die Antwortnachricht steht: "Sie haben Nachrichten von dieser Nummer abbestellt. Antworten Sie HELP für Hilfe. Antworten Sie STOP, um sich abzumelden. Nachrichten und Datenvolumen sind ggf. kostenpflichtig."]({% image_buster /assets/img/sms/keyword_edit2.png %})

Die folgenden Regeln gelten für Schlüsselwörter und Schlüsselwortantworten:

| Keyword | Schlüsselwort-Antworten |
| -------- | ----------------- |
| \- Gültige UTF-8 kodierte Zeichen<br>\- Maximal 20 Schlüsselwörter pro Kategorie<br>\- Maximale Länge von 34 Zeichen<br>\- Mindestlänge von 1 Zeichen <br>\- Darf keine Leerzeichen enthalten<br>\- Groß- und Kleinschreibung muss nicht beachtet werden und muss in der gesamten Abonnementgruppe eindeutig sein. | \- Kann nicht leer sein<br>\- Maximale Länge von 300 Zeichen<br>\- Gültige UTF-8 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Möchten Sie sehen, wie diese Schlüsselwörter in Ihren Kampagnen und Canvases verwendet werden können, um Nachrichten erneut anzusprechen und auszulösen? Besuchen Sie unseren Artikel über [SMS-Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) für weitere Informationen.
{% endalert %}
{% endtab %}

{% tab Antworten koordinieren %}

#### Antworten verwalten

Sie können Ihre eigenen Antworten verwalten, die an Benutzer gesendet werden, nachdem diese ein Stichwort in eine bestimmte Stichwortkategorie eingegeben haben.

1. Gehen Sie im Braze-Dashboard zu **Audience** > **Abonnementgruppen** und wählen Sie Ihre SMS-Abonnementgruppe aus. <br><br>
2. Wählen Sie unter **SMS Global Keywords** eine Stichwortkategorie aus, für die Sie eine Antwort bearbeiten möchten, indem Sie auf das Bleistiftsymbol klicken. ![]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br> 
3. In der sich öffnenden Registerkarte können Sie Ihre Antwort bearbeiten. Beachten Sie bei der Erstellung Ihrer Antwort unsere [sechs Regeln zur Einhaltung der Vorschriften]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) und lesen Sie die folgenden Regeln, die für Schlüsselwörter und Schlüsselwortantworten gelten. ![Antworten]({% image_buster /assets/img/sms/keyword_home.png %})<br><br>
4. Um statische URLs in Ihrer Antwort automatisch zu verkürzen, aktivieren Sie die Option **Linkverkürzung**. Der Zeichenzähler wird aktualisiert und zeigt die erwartete Länge der gekürzten URL an. ![Ein GIF, das die Aktualisierung des Zeichenzählers zeigt, wenn der Schalter "Linkverkürzung" aktiviert ist.]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:50%;"}

##### Überlegungen

| Keyword | Schlüsselwort-Antworten |
| -------- | ----------------- |
| \- Gültige UTF-8 kodierte Zeichen<br>\- Maximal 20 Schlüsselwörter pro Kategorie<br>\- Maximale Länge von 34 Zeichen<br>\- Mindestlänge von 1 Zeichen <br>\- Darf keine Leerzeichen enthalten<br>\- Groß- und Kleinschreibung muss nicht beachtet werden und muss in der gesamten Abonnementgruppe eindeutig sein. | \- Kann nicht leer sein<br>\- Maximale Länge von 300 Zeichen<br>\- Gültige UTF-8 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

{% alert tip %}
Wenn ein aktionsbasiertes Canvas durch eine eingehende SMS-Nachricht ausgelöst wird, können Sie im ersten [Nachrichtenschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) des Canvas auf SMS-Eigenschaften verweisen.
{% endalert %}

## Unterstützung mehrerer Sprachen

Beim Versand in bestimmte Länder kann es erforderlich sein, muss der Absender ggf. eingehende Schlüsselwörter und ausgehende Antworten in der Landessprache unterstützen. Dazu können Sie mit Braze eine sprachspezifische Schlüsselwortkonfiguration erstellen.
![][16]{: style="float:right;max-width:40%;margin-left:10px;"}

### Sprachspezifische Schlüsselwörter erstellen

Klicken Sie auf **Sprache hinzufügen** und wählen Sie Ihre Zielsprache aus oder suchen Sie in der Dropdown-Liste nach einer Sprache.

{% alert important %}
Beachten Sie, dass es für andere Sprachen keine voreingestellten Schlüsselwörter und Antworten wie für Englisch gibt. Daher müssen die Absender mit ihren Marketing- und Rechtsteams zusammenarbeiten, um alle erforderlichen Schlüsselwörter zu diesem Satz hinzuzufügen. Andernfalls wird Braze keine lokalisierten eingehenden Nachrichten für diese Sprachen verarbeiten.
{% endalert %}

Wenn Sie eine Sprache löschen möchten, klicken Sie unten rechts auf die Schaltfläche **Sprache löschen**.

![Die Seite "Globale SMS-Keywords" mit der Auswahl "Französisch". Für jede hinzugefügte Sprache gibt es zusätzliche Registerkarten.][5]

## Benutzerdefinierte Stichwortkategorien

Zusätzlich zu den drei Standardkategorien für Schlüsselwörter (Opt-in, Opt-out und Hilfe) können Sie bis zu 25 weitere Kategorien erstellen. Auf diese Weise können Sie beliebige Schlüsselwörter identifizieren und für Ihr Unternehmen spezifische Antworten einrichten. Ein Beispiel dafür ist "PROMO" oder "DISCOUNT" mit einer Antwort zu den im jeweiligen Monat laufenden Werbeaktionen. 

Diese benutzerdefinierten Schlüsselwörter sind immer aktiv, d.h. jeder Benutzer, der Ihren Nachrichtendienst abonniert hat, kann Schlüsselwörter texten und jederzeit eine Antwort erhalten. Zusätzlich zu diesem Verhalten haben Sie auch die Möglichkeit, bestimmte Schlüsselwörter zu definieren, die nur zu [bestimmten Zeitpunkten]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords) im Lebenszyklus Ihres Benutzers gesendet werden können. 

![Schlüsselwörter für eine Kategorie "Doubleoptin". Wenn ein Benutzer "J" schreibt, erhält er die Nachricht "Vielen Dank, dass Sie Ihre Anmeldung bei Hair Cuttery SMS bestätigt haben."][12]

### Erstellen einer benutzerdefinierten Kategorie

Um eine benutzerdefinierte Stichwortkategorie zu erstellen, gehen Sie wie folgt vor:

1. Bearbeiten Sie die entsprechende Abonnementgruppe.
2. Klicken Sie auf **Benutzerdefiniertes Schlüsselwort hinzufügen**. ![][13]{: style="max-width:90%;"}
3. Geben Sie den Namen für die Stichwortkategorie ein und legen Sie fest, welche Stichwörter eine Antwort auslösen.

Nachdem Sie diese Stichwortkategorie erstellt haben, können Sie sie in Ihren Kampagnen und Canvases [filtern und auslösen]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/).

Schlüsselwörter, die in benutzerdefinierten Schlüsselwortkategorien erstellt werden, erfüllen alle Regeln und Validierungen für die Erstellung neuer Schlüsselwörter. 

### Lebenszyklus-spezifische Schlüsselwörter

Wenn Sie einen Anwendungsfall haben, bei dem Sie einschränken möchten, wann ein Kunde ein bestimmtes Schlüsselwort während seines Lebenszyklus senden kann (z.B. während seines ersten Onboardings), um eine Antwort zu erhalten, können Sie den Auslöser **Gesendete eingehende SMS an Abonnementgruppe innerhalb der Schlüsselwortkategorie ANDERE** in Ihrer Kampagne oder Ihrem Canvas verwenden und Schlüsselwörter definieren, die Ihre Benutzer zu einem bestimmten Zeitpunkt senden können.

Dieser Auslöser unterstützt das Filtern der eingehenden Nachricht mittels "ist" und "ist nicht" sowie Regex-Regeln zur Validierung der Benutzereingaben.

#### Canvas

![Aktionsabhängiger Canvas-Schritt mit dem Auslöser "Eingehende SMS senden" an die Abonnementgruppe "Messaging Service" innerhalb der Schlüsselwortkategorie "Other" senden, sofern der Nachrichtentext dem regulären Ausdruck "caret symbol skip" entspricht.][14]{: style="max-width:90%;"}

#### Kampagne

![Aktionsbasierte Kampagne mit dem Auslöser Eingehende SMS an die Abonnementgruppe "Marketing Message Service A" innerhalb der Schlüsselwortkategorie "Andere" senden, wobei der Nachrichtentext "Schlüsselwort1" oder "Schlüsselwort2" oder nicht "Schlüsselwort A" ist.][15]{: style="max-width:90%;"}

### Umgang mit unbekannten Schlüsselwörtern

Es ist zwar nicht erforderlich, aber wir empfehlen dringend, eine automatische Antwort einzurichten, wenn Benutzer eingehende SMS-Keywords senden, die nicht mit einem vorhandenen Keyword übereinstimmen. Diese Meldung weist darauf hin, dass das Schlüsselwort nicht erkannt wurde, und enthält eine Anleitung. 

Dazu können Sie eine SMS-Kampagne mit einer Nachricht wie "Entschuldigung, dieses Schlüsselwort kennen wir nicht. Schreiben Sie STOP, um anzuhalten oder HELP, um Hilfe zu erhalten." erstellen. Als Nächstes wählen Sie im Schritt Zustellung die Option **Aktionsbasierte Zustellung** und verwenden den Auslöser **Eingehende SMS an Abonnementgruppe innerhalb der Stichwortkategorie ANDERE**.

![]({% image_buster /assets/img/sms/sms_other.png %})

{% alert tip %}
Möchten Sie sehen, wie diese Schlüsselwörter und Schlüsselwortkategorien in Ihren Kampagnen und Canvases für Retargeting und Trigger-Nachrichten verwendet werden können? Besuchen Sie unseren Artikel über [SMS-Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) für weitere Informationen.
{% endalert %}

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %}
[2]: {% image_buster /assets/img/sms/keyword_home.png %}
[unbekannt]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/unknown_phone_numbers/
[endpoint]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[IMAGE2]: {% image_buster /assets/img/sms/sms_message_body.png %}
[5]: {% image_buster /assets/img/sms/multi-language2.png %}
[12]: {% image_buster /assets/img/sms/sms_custom_keyword.png %}
[13]: {% image_buster /assets/img/sms/sms_custom_step.png %}
[14]: {% image_buster /assets/img/sms/canvas_trigger.png %}
[15]: {% image_buster /assets/img/sms/campaign_trigger.png %}
[16]: {% image_buster /assets/img/sms/multi-language.png %}
