---
nav_title: Einverständnis &amp; Adresserfassung
article_title: Einverständnis &amp; Adresserfassung
page_order: 6
page_type: reference
description: "Dieser Referenzartikel behandelt Best Practices für die Einholung von Zustimmungen und E-Mail-Adressen von Nutzer:innen und definiert die verschiedenen möglichen Statusangaben von Nutzer:innen, die sich für den Newsletter angemeldet haben."
channel: email

---

# Zustimmung und Adressenerfassung

> Bevor Sie Ihre ersten E-Mails verschicken, sollten Sie zunächst die Erlaubnis Ihrer Kunden einholen. Das ist eine Frage der Höflichkeit und wirkt sich positiv auf Ihre Öffnungsraten aus!

## Statusangaben von Abonnent:innen

Es gibt drei Zustände des E-Mail-Abonnements für einen Benutzer: **angemeldet**, **abonniert** und **abgemeldet**. Um den Abonnementstatus eines Benutzers zu ändern, lesen Sie unseren Artikel zum [Ändern von Abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-subscriptions) oder verwenden Sie unsere [Abonnement-APIs]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

| Statusangaben von Abonnent:innen | Beschreibung |
|---|---|
| Opt-in | Diese Kunden haben auf den Link in einer Bestätigungs-E-Mail geklickt und sich aktiv für den Erhalt Ihrer Nachrichten entschieden. |
| Abonniert | Standardmäßig sind Nutzer:innen für E-Mails angemeldet, solange sie eine gültige E-Mail-Adresse in ihrem Profil gespeichert haben. Nutzer:innen bleiben angemeldet, bis sie sich abmelden oder sich anmelden. |
| Abgemeldet | Um als abgemeldet markiert zu werden, hat sich ein:e Kund:in entweder ausdrücklich von Ihren E-Mails abgemeldet oder eine E-Mail als Spam markiert. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Methoden zur Erfassung von Adressen

Neben der Einholung der Erlaubnis Ihrer Nutzer vor der Versendung von Nachrichten gibt es verschiedene Methoden zur Erfassung dieser E-Mail-Adressen, die sich auf Ihre Zustellbarkeit auswirken können. 

### Gekaufte Adresslisten

Der Versand von E-Mails an gekaufte oder gemietete Listen verstößt gegen Ihren Braze-Vertrag! Wenn Sie E-Mails kaufen, verschicken Sie völlig unerwünschte Nachrichten und setzen sich dem Risiko von Zustellbarkeitsproblemen aus.

### Gemeinsame Registrierung

Die gemeinsame Registrierung bezieht sich auf eine Vereinbarung zwischen Unternehmen, um Nutzerdaten zu erfassen. Dies ist eine riskante Methode der Erfassung. Es öffnet den Nutzern die Möglichkeit, E-Mails von Dritten zu erhalten, manchmal ohne das Wissen oder die Erlaubnis des Kunden. Wenn Sie sich für diesen Weg entscheiden, stellen Sie sicher, dass Sie klare Angaben machen und die Möglichkeit haben, das Abonnement zu kündigen, wenn Sie die Daten abholen.

### Vorausgewähltes oder erzwungenes Opt-in

Das vorgewählte Opt-in ist eine E-Mail-Registrierungsmethode, bei der das E-Mail-Anmeldefeld bereits angekreuzt ist, damit die Abonnenten Ihre E-Mail erhalten. Wenn Sie das Kästchen aktiviert lassen, erklären sich Abonnent:innen mit dem Erhalt Ihrer E-Mail einverstanden. Diese Methode neigt dazu, Menschen zu verärgern (außerdem ist sie für Sendungen nach oder innerhalb von Kanada illegal). Sie können zwar eine anständig große E-Mail-Liste erhalten, aber Sie können nicht sicher sein, dass diese Nutzer Ihre Marketing-E-Mails wirklich wollen.

### Einmaliges Opt-in

Eine einmalige Anmeldung liegt vor, wenn sich die Abonnenten über ein Anmeldeformular anmelden und sofort in Ihre E-Mail-Liste aufgenommen werden. Bei dieser Methode müssen Nutzer:innen einem einzigen Schritt ein Abonnement abschließen, z. B. indem sie ihre E-Mail Adresse in ein Erfassungsfeld eingeben oder ein Kontrollkästchen als Teil einer Transaktion aktivieren.

### Bestätigtes Opt-in

Ein bestätigtes Opt-in liegt vor, wenn ein:e Nutzer:in ein Kontrollkästchen aktiviert, in dem er oder sie um E-Mail-Kommunikation bittet, und im Gegenzug eine Bestätigungsnachricht gesendet wird. Diese Methode erlaubt es den Nutzer:innen, die Art und Häufigkeit des Contents zu wählen und verbessert so das Engagement. 

Um sicherzustellen, dass Sie nur die Nutzer:innen mit dem größten Engagement ansprechen, können Sie auch die Methode des zweifach bestätigten Opt-ins verwenden. Bei diesem Ansatz wird ein zusätzlicher Schritt eingefügt, bei dem der Benutzer auf eine Schaltfläche oder einen Link in der Bestätigungs-E-Mail klicken muss, um in die E-Mail-Liste aufgenommen zu werden. 
