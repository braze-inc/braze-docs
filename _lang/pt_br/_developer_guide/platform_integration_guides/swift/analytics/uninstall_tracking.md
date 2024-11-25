---
nav_title: Uninstall Tracking
article_title: Desinstalar o rastreamento para iOS
platform: Swift
page_order: 7
description: "Este artigo aborda como configurar o rastreamento de desinstalação para o Swift SDK."

---

# Desinstalar o rastreamento

> Saiba como configurar o rastreamento de desinstalação para seu aplicativo iOS, para que você possa garantir que seu app não execute nenhuma ação automática indesejada ao receber um push de rastreamento de desinstalação do Braze. O rastreamento de desinstalação utiliza notificações por push em segundo plano com um sinalizador Braze na carga útil. Para obter informações gerais, consulte [uninstall tracking][6].

{% alert important %}
Lembre-se de que o rastreamento de desinstalação pode ser impreciso. As métricas que você vê no Braze podem sofrer postergação ou ser imprecisas.
{% endalert %}

## Etapa 1: ativar push em segundo plano

Em seu projeto Xcode, acesse **Capacidades** e verifique se **os Modos de segundo plano** estão ativados. Para saber mais, consulte [notificação por push silenciosa]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/).

## Etapa 2: Verifique o push de fundo do Braze

O Braze usa notificações por push em segundo plano para coletar análises de dados de rastreamento de desinstalação. Certifique-se de que seu aplicativo [não execute nenhuma ação indesejada]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/ignoring_internal_push/) ao receber nossas notificações de rastreamento de desinstalação.

## Etapa 3: Teste no dashboard do Braze

Em seguida, envie a si mesmo um push de teste no dashboard do Braze. Lembre-se de que esse push de teste não atualizará seu perfil de usuário.

1. Na página **Campaigns (Campanhas** ), crie uma campanha de notificação por push e selecione **iOS push** como sua plataforma.
2. Na página **Settings (Configurações)**, adicione a chave `appboy_uninstall_tracking` com o valor correspondente `true` e marque **Add Content-Available Flag (Adicionar sinalizador de conteúdo disponível**).
3. Use a página **Prévia** para enviar a si mesmo um push de rastreamento de desinstalação de teste.
4. Verifique se o seu app não executa nenhuma ação automática indesejada ao receber o push.

{% alert important %}
Essas etapas de teste são um proxy para o envio de um push de rastreamento de desinstalação da Braze. Se a contagem de crachás estiver ativada, um número de crachá será enviado junto com o push de teste, mas os pushes de rastreamento de desinstalação do Braze não definirão um número de crachá em seu aplicativo.
{% endalert %}

## Etapa 4: Ativar o rastreamento de desinstalação

Siga as instruções para [ativar o rastreamento de desinstalação]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

