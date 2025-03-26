---
nav_title: Ereignisprotokollierung verwenden
article_title: Ereignisprotokollierung verwenden
page_order: 6
page_type: solution
description: "Dieser Hilfeartikel beschreibt, wie Sie die Ereignisprotokollierung verwenden, um Probleme mit Ihrer Braze-Integration zu beheben."
---

# Ereignisprotokollierung verwenden

Um Probleme mit Ihrer Braze-Integration zu beheben, können Sie ein anonymes Benutzerprofil und ein [Ereignisbenutzerprotokoll][1] einrichten. Wie Sie ein anonymes Profil einrichten können, erfahren Sie unter [Hinzufügen von Testbenutzern][2].

## Über das Protokollieren

Verwenden Sie die Ereignisprotokollierung, um zu testen, wie das Verhalten eines anonymen Benutzers aussieht. Dies kann besonders hilfreich sein, um die Benutzer-ID zu identifizieren, wenn die getestete App keine E-Mails sammelt. Sie können Braze und die IP-Adresse Ihres Geräts verwenden, um dieses Gerät als Testbenutzer hinzuzufügen.

Dies ist eine gute Möglichkeit, anonyme Benutzer zu finden. Sie können diese Informationen auch verwenden, um zu prüfen, welche Daten an Braze gesendet werden und um Unstimmigkeiten festzustellen. In dieser Ansicht können Sie erkennen, ob die Deltas Ihrer Daten an Braze gesendet werden. Wenn mit jedem protokollierten Ereignis eine E-Mail-Adresse oder ein Push-Token gesendet wird, werden alle Daten an Braze gesendet.

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 16\. November 2022_

[1]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users