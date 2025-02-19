---
nav_title: Abo-Gruppen
article_title: Abo-Gruppen
page_order: 1
description: "Dieser Artikel behandelt die Abonnementgruppen für LINE-Nachrichten."
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# LINE-Abonnementgruppen

> Es gibt zwei Abonnement-Status für LINE-Benutzer: abonniert und abgemeldet. LINE kann bis zu 100 Abo-Gruppen pro Workspace haben, wobei jede Abo-Gruppe mit ihrem eigenen LINE-Kanal verbunden ist.

| Status | Definition |
| --- | --- |
| Abonniert | Der Nutzer ist dem LINE-Kanal von seiner LINE-App aus gefolgt. Nutzer:innen werden automatisch zu Abonnent:innen wenn sie Ihnen folgen, nachdem Sie die Integration abgeschlossen haben. |
| Abgemeldet | Der Nutzer ist dem LINE-Kanal nicht von seiner LINE-App aus gefolgt, oder der Nutzer hat den LINE-Kanal ausdrücklich nicht mehr verfolgt. <br><br> Benutzer, die sich von einer LINE-Abonnementgruppe abmelden, erhalten keine LINE-Nachrichten mehr von Sendekanälen, die zu dieser Abonnementgruppe gehören. |
{: .reset-td-br-1 .reset-td-br-2 }

## Einstellen der LINE-Abonnementgruppe eines Benutzers

LINE hostet den Abo-Status der Nutzer:innen. Braze verarbeitet die Follow- und Unfollow-Ereignisse, die den Abonnementstatus aktualisieren.