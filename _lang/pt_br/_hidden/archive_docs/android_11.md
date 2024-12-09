---
nav_title: Guia de atualização do Android 11
article_title: Guia de atualização do Android 11
page_order: 9
platform: 
  - Android
  - FireOS
description: "Este artigo de referência aborda a atualização do SDK do Android 11, destacando alterações como deep linking, compatibilidade do SDK e muito mais."
hidden: true
---

# Guia de atualização do SDK do Android 11

Este guia descreve as alterações relevantes introduzidas no Android 11 (lançado em 8 de setembro de 2020) e as etapas de atualização necessárias para a integração de seu Braze Android SDK.

Para obter um guia de migração completo do Android 11, consulte a [documentação do desenvolvedor do Android](https://developer.android.com/preview/migration).

## Compatibilidade com o SDK do Braze

Todos os apps _direcionados_ ao Android 11 (API 30) devem fazer upgrade para o [Braze Android SDK v8.1.0+][1] para continuar usando os recursos de envio de mensagens da Braze.

{% alert important %}
Devido às alterações nas APIs do Android 11, os apps direcionados ao Android 11 que não fizerem upgrade para o Braze Android SDK v8.1.0 ou superior terão problemas com o deep linking dos componentes da interface do usuário da Braze e não exibirão corretamente as mensagens personalizadas com HTML no app.
{% endalert %}

### Deep links

Os apps direcionados ao Android 11 ou posterior (API versão 30+) devem fazer upgrade para o [Braze Android SDK v8.1.0][1] para manter o uso do deep linking nas mensagens da Braze. Devido a uma alteração nas APIs do Android 11, os aplicativos que não fizerem upgrade para pelo menos o Android SDK v8.1.0 enfrentarão dificuldades com deep linkings nas mensagens da Braze (mensagens no app ou cartões de conteúdo).

### Mensagens no app em HTML

Os apps direcionados ao Android 11 ou posterior (versão API 30+) devem fazer upgrade para o Braze Android SDK v8.1.0 para continuar usando mensagens no app com HTML personalizado. Devido a uma alteração nas configurações do WebView do Android 11, as mensagens HTML no app não serão exibidas corretamente nos aplicativos direcionados para o Android 11 até que seja feito o upgrade para o [Braze Android SDK v8.1.0][1]. 

### Permissões de local

Os apps que usam permissões de local devem seguir as [práticas recomendadas](https://developer.android.com/preview/privacy/location#change-details) do Android ao solicitar acesso ao local. Nenhuma alteração em sua integração com o Braze é necessária para essas atualizações de local.

## Mudanças de comportamento no Android 11

### Permitir permissões uma vez

Os usuários agora podem conceder permissões, como coleta de local, uma única vez (consulte [os documentos do Android](https://developer.android.com/preview/privacy/location#one-time-access) para obter mais informações). Depois que um app for fechado ou ficar em segundo plano por um período prolongado, essa permissão será revogada automaticamente. O app precisaria solicitar novamente essa permissão quando necessário no futuro. Os apps que já seguem o fluxo recomendado para solicitar permissões de local serão compatíveis com permissões únicas.

![][3]{: height="230px" }

### Permissão de local de fundo

O Android 11 exigirá que os apps solicitem primeiro a permissão de local em primeiro plano e, depois que o app estiver em segundo plano, ele poderá solicitar novamente ao usuário a permissão de local em segundo plano.
Os clientes que usam geofences devem garantir que seu app siga as recomendações do Android sobre a coleta de permissão de local em segundo plano. Para saber mais, consulte [os documentos do Android](https://developer.android.com/preview/privacy/location#background-location).

[1]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#810
[3]: {% image_buster /assets/img/android/android-11-one-time-permission.svg %}
