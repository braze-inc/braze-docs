---
nav_title: Uninstall Tracking
article_title: Desinstalar o rastreamento para iOS
platform: iOS
page_order: 7
description: "Este artigo aborda como configurar o rastreamento de desinstalação para seu aplicativo iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Desinstalar o rastreamento para iOS

> Este artigo aborda como configurar o rastreamento de desinstalação para seu aplicativo iOS e como testar para que seu app não execute nenhuma ação automática indesejada ao receber um push de rastreamento de desinstalação do Braze.

O rastreamento de desinstalação utiliza notificações por push em segundo plano com um sinalizador Braze na carga útil. Para saber mais, consulte o [rastreamento de desinstalação]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking) em nosso guia do usuário.

## Etapa 1: Ativando o push em segundo plano

Certifique-se de ter ativado a opção **Remote notifications (Notificações remotas** ) na seção **Background Modes (Modos de segundo plano** ) da guia **Capabilities (Capacidades)** do seu projeto Xcode. Consulte nossa documentação [sobre notificações por push silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/silent_push_notifications/) para obter mais detalhes.

## Etapa 2: Verificação do push do fundo do Braze

O Braze usa notificações por push em segundo plano para coletar análises de dados de rastreamento de desinstalação. Certifique-se de que seu aplicativo [não execute nenhuma ação indesejada]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/customization/ignoring_internal_push/) ao receber nossas notificações de rastreamento de desinstalação.

## Etapa 3: Teste no dashboard

Em seguida, envie a si mesmo um push de teste a partir do dashboard. Esse push de teste não atualizará seu perfil de usuário.

1. Na página **Campaigns (Campanhas** ), crie uma campanha de notificação por push e selecione **iOS push** como sua plataforma.<br><br>
2. Na página **Settings (Configurações)**, adicione a chave `appboy_uninstall_tracking` com o valor correspondente `true` e marque **Add Content-Available Flag (Adicionar sinalizador de conteúdo disponível**).<br><br>
3. Use a página **Prévia** para enviar a si mesmo um push de rastreamento de desinstalação de teste.<br><br>
4. Verifique se o seu app não executa nenhuma ação automática indesejada ao receber o push.

{% alert important %}
Essas etapas de teste são um proxy para o envio de um push de rastreamento de desinstalação da Braze. Se a contagem de crachás estiver ativada, um número de crachá será enviado junto com o push de teste, mas os pushes de rastreamento de desinstalação do Braze não definirão um número de crachá em seu aplicativo.
{% endalert %}

## Etapa 4: Ativar o rastreamento de desinstalação

Siga as instruções para [ativar o rastreamento de desinstalação]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

