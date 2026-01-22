---
nav_title: Benutzerdefinierte E-Mail-Fußzeile
article_title: Benutzerdefinierte E-Mail-Fußzeile
page_order: 6.5
description: "Dieser Artikel beschreibt, wie Sie eine angepasste E-Mail-Fußzeile für den gesamten Workspace einrichten können."
channel:
  - email

---

# Benutzerdefinierte E-Mail-Fußzeile

> Sie können eine nutzerdefinierte E-Mail-Fußzeile für den gesamten Workspace festlegen, die Sie mithilfe des {% raw %}`{{${email_footer}}}`{% endraw %}-Liquid-Attributs in jede E-Mail einfügen können.

Durch die Verwendung von benutzerdefinierten E-Mail-Fußzeilen müssen Sie nicht mehr für jede E-Mail-Vorlage oder E-Mail-Kampagne, die Sie verwenden, eine neue Fußzeile erstellen. Änderungen, die Sie an Ihrer benutzerdefinierten Fußzeile vornehmen, werden in allen neuen und bestehenden E-Mail-Kampagnen übernommen. Denken Sie daran, dass Sie gemäß dem [CAN-SPAM Act von 2003](https://www.ftc.gov/tips-advice/business-center/guidance/can-spam-act-compliance-guide-business) eine physische Adresse Ihres Unternehmens und einen Link zum Abbestellen in Ihren E-Mails angeben müssen.

{% alert warning %}
Es liegt in Ihrer Verantwortung, sicherzustellen, dass Ihre benutzerdefinierte Fußzeile die oben genannten Anforderungen erfüllt.
{% endalert %}

## Erstellen Ihrer benutzerdefinierten Fußzeile

Um Ihre benutzerdefinierte Fußzeile zu erstellen oder zu bearbeiten, gehen Sie wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **E-Mail-Voreinstellungen**.
2. Gehen Sie zum Abschnitt **Benutzerdefinierte Fußzeilen** und aktivieren Sie die benutzerdefinierten Fußzeilen.
3. Bearbeiten Sie Ihre Fußzeile im Bereich **Verfassen**.
4. Senden Sie eine Testnachricht. 

![Ein Beispiel für eine angepasste Fußzeile.]({% image_buster /assets/img_archive/custom_footer.png %})

Die Standard-Fußzeile verwendet das Attribut {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} und unsere physische Postanschrift. Wenn Sie diesen Standard verwenden, müssen Sie bei Protokoll die Option **<other>** für das **Protokoll**.

{% alert important %}
Um den CAN-SPAM-Vorschriften zu entsprechen, muss Ihre benutzerdefinierte Fußzeile {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} enthalten. Ohne dieses Attribut können Sie eine benutzerdefinierte Fußzeile nicht speichern.
{% endalert %}

![Protokoll- und URL-Werte, die für die angepasste Fußzeile benötigt werden.]({% image_buster /assets/img_archive/email_unsub_protocol.png %}){: style="max-width:50%;"}

## Fußzeilen ohne Abmeldelinks

Seien Sie sehr vorsichtig, wenn Sie ein Template mit der angepassten Fußzeile {% raw %}`{{${email_footer}}}` aber ohne den `{{${set_user_to_unsubscribed_url}}}`{% endraw %}-Tag für den Abmeldelink verwenden. Es erscheint eine Warnung, aber Sie haben die Wahl, eine E-Mail mit oder ohne Abmeldelink zu versenden.

Hier ist eine Warnung im E-Mail-Composer:

![Beispiel einer E-Mail, die ohne Fußzeile verfasst wurde.]({% image_buster /assets/img_archive/no_unsub_link_warning.png %})

Hier ist eine Warnung im Kampagnen-Composer:

![No-footer Kampagne Zusammensetzung.]({% image_buster /assets/img_archive/no_footer_test.png %})

### Hinzufügen eines angepassten Links zum Abmelden

Um einen angepassten Link zum Abmelden hinzuzufügen, können Sie den Link zum Abmelden in der angepassten Fußzeile von {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} in einen Link zu Ihrer eigenen Website mit einem Abfrageparameter ändern, der die Nutzer:innen-ID enthält. Ein Beispiel ist:
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Als nächstes rufen Sie den [`/email/status`Endpunkt]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) auf, um den Nutzerstatus zu aktualisieren. Weitere Einzelheiten finden Sie in unserer Dokumentation zur [Änderung des E-Mail-Abonnementstatus]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

Speichern Sie dann diesen neuen Link. Der Standard-Braze-Tag zum Abmelden {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} muss in der Fußzeile stehen. Das bedeutet, dass Sie den Standardlink einfügen müssen, indem Sie ihn „verstecken“, indem Sie den Tag entweder in einem Kommentar oder in einem versteckten `<div>`-Tag platzieren.

## Bewährte Praktiken

Wir empfehlen Ihnen, bei der Erstellung und Verwendung von benutzerdefinierten Fußzeilen die folgenden bewährten Verfahren anzuwenden.

### Personalisierung mit Attributen

Wenn Sie eine benutzerdefinierte Fußzeile erstellen, empfiehlt Braze die Verwendung von [Attributen für die Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/). Es stehen alle Standardattribute und angepassten Attribute zur Verfügung, aber hier sind einige, die Sie vielleicht nützlich finden:

| Attribut | Taggen |
| --------- | --- |
| E-Mail Adresse des Benutzers | {% raw %}`{{${email_address}}}`{% endraw %} |
| Angepasste Abmelde-URL des oder der Nutzers:in | {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} <br><br>Dieser Tag ersetzt den bisherigen Tag {% raw %}`{{${unsubscribe_url}}}`{% endraw %}. Wir empfehlen, dass Sie stattdessen den neueren Tag {% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %} verwenden. |
| Benutzerdefinierte Opt-In URL | {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} |
| Benutzerdefinierte URL zum Abonnieren | {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}|
| Benutzerdefinierte URL des Braze Preference Center | {% raw %}`{{${preference_center_url}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Mit einem Link zum Abbestellen und einem Opt-in-Link

{% raw  %}
Als Best Practice empfiehlt Braze, sowohl einen Abmeldelink (z. B. ``{{${set_user_to_unsubscribed_url}}}``) als auch einen Anmeldelink (z. B. ``{{${set_user_to_opted_in_url}}}``) in Ihre angepasste Fußzeile aufzunehmen. Auf diese Weise können Nutzer:innen sich sowohl abmelden als auch anmelden, und Sie können passiv Anmeldedaten für einen Teil Ihrer Nutzer:innen sammeln.
{% endraw %}

### Benutzerdefinierte Fußzeilen für Klartext-E-Mails einstellen

Sie können auf der Registerkarte **Abonnementseiten und Fußzeilen** der Seite **E-Mail-Einstellungen** auch eine benutzerdefinierte Fußzeile für Klartext-E-Mails festlegen, die denselben Regeln folgt wie die benutzerdefinierte Fußzeile für HTML-E-Mails. 

Wenn Sie keine Klartext-Fußzeile einfügen, wird Braze automatisch eine aus der HTML-Fußzeile erstellen. Wenn Ihre benutzerdefinierten Fußzeilen Ihren Vorstellungen entsprechen, wählen Sie **Speichern**.

![E-Mail mit ausgewählter Option Angepasste Klartext-Fußzeile einstellen.]({% image_buster /assets/img_archive/custom_footer_save_changes.png %}){: style="max-width:70%" }

