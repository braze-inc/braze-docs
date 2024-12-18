---
nav_title: Sessões de rastreamento
article_title: Sessões de rastreamento para o Windows Universal
platform: Windows Universal
page_order: 0
description: "Este artigo de referência aborda como rastrear sessões na plataforma Windows Universal."
hidden: true
---

# Análise de dados
{% multi_lang_include archive/windows_deprecation.md %}

## Rastreamento de sessão

O SDK do Braze relata dados de sessão que são usados pelo dashboard do Braze para calcular o engajamento do usuário e outras análises essenciais para entender seus usuários. Com base na semântica de sessão a seguir, nosso SDK gera pontos de dados de "início de sessão" e "encerramento de sessão" que contabilizam a duração da sessão e as contagens de sessão visíveis no dashboard do Braze.

### Ciclo de vida da sessão

Nossa sessão de registros de integração do Windows é aberta quando o app é iniciado e a sessão de registros é fechada quando o aplicativo é encerrado. O valor mínimo para `sessionTimeoutInSeconds` é 1 segundo. Se precisar forçar uma nova sessão, poderá fazê-lo mudando de usuário.

### Teste de rastreamento de sessão

Para detectar sessões por meio de seu usuário, localize-o no dashboard e navegue até "App Usage" (Uso do app) no perfil do usuário. Você pode confirmar que o rastreamento de sessão está funcionando verificando se a métrica "Sessões" aumenta quando você espera que isso aconteça.

![Um perfil de usuário que mostra o uso do app como 25 sessões, a última usada há duas horas e a primeira usada há vinte dias][session_tracking_7]

[session_tracking_1]: {{ site.baseurl }}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview#customizing-braze-on-startup
[session_tracking_3]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-appboyxml
[session_tracking_5]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize
[session_tracking_6]: http://msdn.microsoft.com/en-us/library/windows/apps/hh464925.aspx
[session_tracking_7]: {% image_buster /assets/img_archive/test_session.png %}
[session_tracking_8]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android

