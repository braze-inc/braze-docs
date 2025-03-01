---
nav_title: Deaktivieren des Web-SDK-Trackings
article_title: Deaktivieren des Web-SDK-Trackings
platform: Web
page_order: 6
page_type: reference
description: "Dieser Artikel beschreibt die Deaktivierung des Web-SDK-Trackings, beantwortet die Fragen nach dem Warum und Wie und beschäftigt sich mit den Auswirkungen auf das Web."

---

# Web-SDK-Tracking deaktivieren

{% multi_lang_include archive/web-v4-rename.md %}

> Zur Einhaltung von Datenschutzvorschriften kann das Tracking von Daten im Web SDK mit der Methode [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) gänzlich unterbunden werden. 

Diese Methode synchronisiert alle Daten, die vor dem Aufruf von `disableSDK()` protokolliert wurden, und bewirkt, dass alle nachfolgenden Aufrufe des Braze Web SDK für diese Seite und zukünftige Seitenladevorgänge ignoriert werden. Wenn Sie die Datenerfassung zu einem späteren Zeitpunkt wieder aufnehmen möchten, können Sie dies mit der Methode [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) tun.

Wenn Sie den Nutzern die Möglichkeit geben möchten, das Tracking zu beenden, empfehlen wir Ihnen, eine einfache Seite mit zwei Links oder Schaltflächen zu erstellen, von denen einer `disableSDK()` aufruft, wenn er angeklickt wird, und der andere `enableSDK()`, damit die Nutzer sich wieder anmelden können. Mit diesen Steuerelementen können Sie das Tracking auch über andere Daten-Subprozessoren starten oder beenden.

Beachten Sie, dass das Braze SDK nicht initialisiert werden muss, um `disableSDK()` aufzurufen. So können Sie das Tracking für völlig anonyme Nutzer deaktivieren. Umgekehrt wird das Braze SDK nicht durch `enableSDK()` initialisiert, sodass Sie anschließend auch `initialize()` aufrufen müssen, um das Tracking zu aktivieren.
