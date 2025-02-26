---
nav_title: Guia de atualização do Android 12
article_title: Guia de atualização do Android 12
page_order: 9
permalink: "/android_12/"
layout: "dev_guide"
hidden: true
platform: 
  - Android
  - FireOS
description: "Este artigo de referência aborda a atualização do SDK do Android 12, destacando alterações como deep linking, compatibilidade do SDK e muito mais."
---

# Guia de atualização do SDK do Android 12

Este guia descreve as alterações relevantes introduzidas no Android 12 (2021) e as etapas de upgrade necessárias para a integração de seu SDK da Braze para Android.

Para obter um guia de migração completo do Android 12, consulte a [documentação do desenvolvedor do Android](https://developer.android.com/about/versions/12).

## Compatibilidade com o SDK do Braze

Se seu direcionamento for para o Android 12, você deverá usar o [Braze Android SDK v13.1.2+][1]. Se você ainda não estiver direcionado ao Android 12, ainda é recomendável fazer upgrade.

**O que acontecerá se eu não fizer upgrade do Braze Android SDK?**

* Devido a uma alteração nas [caixas de diálogo do sistema de fechamento](https://developer.android.com/about/versions/12/behavior-changes-all#close-system-dialogs) do Android, as versões mais antigas do Braze Android SDK registrarão avisos ao receber notificações por push em dispositivos que executam o Android 12. Esse comportamento ocorre mesmo que seu app não tenha como direcionamento o Android 12.
* Alterações nas [exportações de componentes](https://developer.android.com/about/versions/12/behavior-changes-12#exported), [intenções pendentes](https://developer.android.com/about/versions/12/behavior-changes-12#pending-intent-mutability) e [trampolins de notificação](https://developer.android.com/about/versions/12/behavior-changes-12#notification-trampolines) podem afetar sua capacidade de compilar o app ou podem impedir a inicialização do Braze SDK. Esse comportamento ocorre apenas para apps com direcionamento para o Android 12.
* As alterações nas [notificações por push personalizadas](https://developer.android.com/about/versions/12/behavior-changes-12#custom-notifications) mudaram o layout do nosso novo recurso [de push de imagem em linha para Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/inline_image_push/). Esse comportamento ocorre apenas para apps com direcionamento para o Android 12.

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#1312
