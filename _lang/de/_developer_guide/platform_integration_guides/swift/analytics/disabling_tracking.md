---
nav_title: iOS SDK Tracking deaktivieren
article_title: SDK Tracking für iOS deaktivieren
platform: Swift
page_order: 8
description: "Dieser Artikel zeigt, wie Sie die Datenerfassung für das Swift SDK deaktivieren können."

---

# Deaktivieren des iOS SDK Tracking

> Um den Datenschutzbestimmungen zu entsprechen, kann das Tracking von Daten auf dem iOS SDK vollständig gestoppt werden, indem Sie die  Eigenschaft [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) in Ihrer Braze-Instanz auf `false` setzen. 

Wenn `enabled` auf `false` eingestellt ist, ignoriert das Braze SDK alle Aufrufe an die öffentliche API. Das SDK bricht auch alle In-Flight-Aktionen ab, z. B. Netzwerkanfragen, Eventverarbeitung usw. Um die Datenerfassung wieder aufzunehmen, setzen Sie [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) auf `true`.

Sie können auch die Methode [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) verwenden, um lokal gespeicherte SDK-Daten auf dem Gerät eines Nutzers vollständig zu löschen. Wenn Sie Swift SDK Version 5.7.0 oder früher verwenden oder `useUUIDAsDeviceId` auf `false` eingestellt ist, müssen Sie auch eine Post-Anfrage an [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) stellen, da Ihr Identifier for Vendors (IDFV) als ihre Geräte-ID verwendet wird. Für Braze Swift Versionen 7.0.0 und höher generieren das SDK und die `wipeData()`-Methode stattdessen zufällig eine UUID für ihre Geräte-ID.
