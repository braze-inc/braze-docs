---
nav_title: Doppelte E-Mails
article_title: Doppelte E-Mails
page_order: 7
page_type: reference
description: "Dieser Artikel befasst sich mit bewährten Methoden zur Verwaltung doppelter E-Mails."
channel: email

---

# Doppelte E-Mails

> Wenn sich mehrere Profile eine E-Mail Adresse teilen und sich ein Profil abmeldet, aktualisiert Braze die anderen Profile (bis zu 100) mit dieser Adresse auf den gleichen Abo-Status. Dies gilt für Abmeldungen und andere Änderungen wie den globalen Abo-Status und den Status der einzelnen Abo-Gruppen.

## Aktualisierung von E-Mail-Abos

Braze sucht automatisch nach doppelten E-Mail-Adressen und entfernt diese, wenn es eine Kampagne versendet. Dadurch wird verhindert, dass Braze die E-Mail mehr als einmal sendet, selbst wenn mehrere Nutzerprofile eine Adresse gemeinsam nutzen.

{% alert tip %}
Vergewissern Sie sich, dass Sie mit den Tools vertraut sind, die Braze für die [Verwaltung von Benutzer-E-Mail-Abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions) und die Ausrichtung von Kampagnen auf Benutzer mit bestimmten Abonnementstatus bietet. Diese Tools sind entscheidend für die Einhaltung von [Anti-Spam-Gesetzen]({{site.baseurl}}/help/best_practices/spam_regulations/#spam-regulations).
{% endalert %}

Wenn Nutzer:innen eine gemeinsame E-Mail Adresse haben und Sie ein Profil aktualisieren, überträgt Braze die Änderungen am Abo auf alle Nutzer:innen (bis zu 100).

## Verhalten beim Senden von Nachrichten

Da eine Deduplizierung stattfindet, wenn die Zielnutzer:innen in derselben Sendung enthalten sind, können getriggerte Kampagnen (ausgenommen API-getriggerte Kampagnen) und Canvase zu mehreren Sendungen an dieselbe E-Mail-Adresse führen (selbst innerhalb eines Zeitraums, in dem Nutzer:innen aufgrund einer erneuten Qualifizierung ausgeschlossen werden könnten), wenn unterschiedliche Nutzer:innen mit übereinstimmenden E-Mails das Trigger-Event zu unterschiedlichen Zeiten protokollieren.

## Beispiele

Wenn beispielsweise Nutzer:in A und Nutzer:in B die E-Mail `johndoe@example.com` gemeinsam nutzen, ihr Profil aber in einer anderen Zeitzone liegt, erhält die E-Mail `johndoe@example.com` zwei E-Mails, wenn das Event, das die Kampagne auslöst, das Senden in der Zeitzone eines Nutzers oder einer Nutzerin beinhaltet.

Wenn Sie die E-Mail-Adresse von Benutzer A auf eine andere E-Mail-Adresse setzen oder aktualisieren, die von einem bereits existierenden Benutzer B verwendet wird, erbt Benutzer A den bereits bestehenden Abonnementstatus von Benutzer B, es sei denn, die Einstellung **Benutzer bei Aktualisierung ihrer E-Mail erneut anmelden** ist aktiviert.

{% alert important %}
Wenn Sie eine API-Kampagne über einen API-Aufruf senden (mit Ausnahme von API-ausgelösten Kampagnen) und im Zielgruppensegment mehrere Benutzer mit derselben E-Mail-Adresse angegeben sind, senden wir die Kampagne an diese Adresse so oft, wie im Aufruf angegeben ist. Das liegt daran, dass wir davon ausgehen, dass API-Aufrufe zielgerichtet aufgebaut sind.
<br><br>
**Per API getriggerte Kampagnen**<br>
Beachten Sie, dass per API getriggerte Kampagnen Duplikate herausfiltern oder senden, je nachdem, wo die Zielgruppe definiert ist. <br>\- Eine Deduplizierung kann auftreten, wenn es doppelte E-Mails in einem Zielsegment oder doppelte E-Mails aufgrund von doppelten IDs innerhalb des [Empfängerfeldes]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) eines durch die API ausgelösten Aufrufs gibt. <br>\- Es kommt zu doppelten E-Mails, wenn Sie im Empfängerfeld eines über die API ausgelösten Aufrufs direkt auf verschiedene Benutzer-IDs abzielen.
{% endalert %}
