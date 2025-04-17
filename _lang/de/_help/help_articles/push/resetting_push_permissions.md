---
nav_title: Push-Berechtigungen zurücksetzen
article_title: Push-Berechtigungen zurücksetzen
page_type: solution
description: "In diesem Hilfeartikel erfahren Sie, wie Sie die Push-Berechtigungen und Daten Ihres Browsers zurücksetzen können."
channel: push
---

# Push-Berechtigungen zurücksetzen

Wenn Sie Probleme mit Push-Benachrichtigungen in Ihrem Browser haben, müssen Sie möglicherweise die Benachrichtigungsberechtigungen Ihrer Website zurücksetzen und den Speicher Ihrer Website leeren. Beziehen Sie sich auf diese Schritte für Hilfe.

## Chrome auf dem Desktop zurücksetzen

1. Klicken Sie im Chrome-Browser neben Ihrer URL auf das Schieberegler-Symbol **Site-Informationen anzeigen**.
2. Klicken Sie unter **Benachrichtigungen** auf **Berechtigung zurücksetzen**.
3. Öffnen Sie Chrome DevTools. Im Folgenden finden Sie die relevanten Tastenkombinationen pro Betriebssystem.

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | Tastaturkürzel                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4\. Navigieren Sie in DevTools zum Tab **Anwendung**.
5\. Wählen Sie in der Seitenleiste **Speicher** aus.
6\. Klicken Sie auf **Website-Daten löschen**.
7\. Chrome fordert Sie auf, die Seite neu zu laden, um Ihre aktualisierten Einstellungen zu übernehmen. Klicken Sie auf **Neu laden**.

Ihre Push-Berechtigungen werden jetzt zurückgesetzt. Öffnen Sie einen neuen Tab auf Ihrer Website und probieren Sie es aus.

## Chrome auf Android zurücksetzen

Wenn Sie eine Benachrichtigung von Ihrer Website in Ihrem Android Benachrichtigungsfeld sehen:

1. Tippen Sie in der Push-Benachrichtigung auf <i class="fas fa-cog" title="Einstellungen"></i> und wählen Sie **Website-Einstellungen**.
2. Tippen Sie in den **Website-Einstellungen** auf **Löschen & Zurücksetzen**.

Wenn Sie keine Benachrichtigung von Ihrer Website geöffnet haben:

1. Öffnen Sie Chrome auf Android.
2. Tippen Sie auf das Menü <i class="fas fa-ellipsis-vertical"></i>.
3. Gehen Sie zu **Einstellungen** > **Website-Einstellungen** > **Benachrichtigungen**.
4. Überprüfen Sie, ob die Benachrichtigungen auf "Vor dem Senden fragen (empfohlen)" eingestellt sind.
5. Finden Sie Ihre Website in der Liste.
6. Wählen Sie den Eintrag aus und tippen Sie auf **Löschen und Zurücksetzen**.

Ihre Push-Berechtigungen werden jetzt zurückgesetzt. Öffnen Sie einen neuen Tab auf Ihrer Website und probieren Sie es aus.

## Firefox auf dem Desktop zurücksetzen

1. Klicken Sie neben der URL Ihrer Website auf <i class="fa-solid fa-circle-info" alt="info icon"></i> oder <i class="fas fa-lock" alt="lock icon"></i>.
2. Wählen Sie unter **Berechtigungen**, neben **Benachrichtigungen erhalten**<i class="fa-solid fa-circle-xmark" title="Diese Berechtigung löschen und erneut fragen"></i> um die Berechtigungen für Benachrichtigungen zu löschen.
3. Wählen Sie im gleichen Menü **Cookies und Website-Daten löschen aus**.
4. Es wird ein Dialogfeld angezeigt, in dem Sie Ihre Wahl bestätigen müssen. Klicken Sie auf **OK**.

Ihre Push-Berechtigungen werden jetzt zurückgesetzt. Öffnen Sie einen neuen Tab auf Ihrer Website und probieren Sie es aus.

## Firefox auf Android zurücksetzen

Um Push-Berechtigungen unter Android zurückzusetzen, referenzieren Sie diesen [Support-Artikel von Mozilla](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

## Safari auf macOS zurücksetzen

{% alert note %}
Diese Schritte gelten nur für macOS, da Apple Web-Push für Safari unter Windows nicht unterstützt.
{% endalert %}

1. Öffnen Sie Safari.
2. Gehen Sie in der [Menüleiste auf dem Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac) zu **Safari** > **Einstellungen** > **Websites** > **Benachrichtigungen**.
3. Wählen Sie Ihren Standort aus der Liste aus.
4. Klicken Sie auf **Entfernen**, um die Benachrichtigungsberechtigungen für die Website zu löschen.
5. Gehen Sie dann zu **Datenschutz** > **Website-Daten verwalten**.
6. Wählen Sie Ihren Standort aus der Liste aus.
7. Klicken Sie auf **Entfernen**, oder um alle Daten der Website zu entfernen, klicken Sie auf **Alle entfernen**.
8. Klicken Sie auf **Erledigt**.

Ihre Push-Berechtigungen werden jetzt zurückgesetzt. Öffnen Sie einen neuen Tab auf Ihrer Website und probieren Sie es aus.


*Zuletzt aktualisiert am 12\. Februar 2024*