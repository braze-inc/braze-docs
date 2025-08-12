---
nav_title: Abril
page_order: 9
noindex: true
page_type: update
description: "Este artigo contém notas de versão de abril de 2018."
---
# Abril de 2018

## Atualização de webhooks a caminho

Em maio, a Braze implementará uma iniciativa de segurança para redirecionamentos de webhooks. Acessando o site, o remetente do webhook não poderá seguir esses redirecionamentos. Em vez disso, os redirecionamentos serão tratados como erros para evitar loops de redirecionamento infinitos. O Braze não espera que isso afete ninguém, mas se você tiver webhooks que redirecionam, recomendamos revisar e editar essa campanha.

## Aumento do armazenamento de CSV

O Braze atualizou o filtro CSV X para incluir os 100 CSVs mais recentes em que um usuário foi atualizado, em vez dos 10 anteriores.

## Desinstale o rastreamento ativado por padrão para apps Android

A função [Desinstalar rastreamento]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/) de todos os novos apps para Android terá como padrão a opção "ligado". Todos os apps Android existentes que têm o rastreamento de desinstalação desativado agora serão alterados para "ativado". O rastreamento de desinstalação do Android não envia mais push para o dispositivo, e nenhuma outra atualização ou ação é necessária de sua parte.

## Funções de pesquisa atualizadas e aprimoradas

O Braze adicionou tag e melhor funcionalidade de pesquisa ao Braze para aprimorar sua experiência no gerenciamento de implantações em larga escala do Braze enquanto você pesquisa [eventos e atributos personalizados]({{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#custom-event-and-attribute-management), modelos e muito mais.

## Stories por push

[Crie notificações]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_stories/#push-stories) com várias páginas, uma imagem, comportamento de clique e um título e subtítulo opcionais. Basta criar uma mensagem push e selecionar **Push Story** no menu suspenso.

Note que você deve atualizar para a versão mais recente do Android (versão 2.2.0+) e do iOS (versão 3.2.0+) para usar esse recurso.


## Visão da caixa de entrada

Agora é possível fazer [uma prévia de seus e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#inbox-vision) com base na plataforma do cliente, seja por meio de uma página de visão geral de miniaturas ou de uma exibição de lista que inclui uma captura de tela grande e uma análise mais específica de quaisquer problemas que possam existir com a renderização de HTML para cada cliente. Entre em contato com seu gerente de sucesso do cliente ou gerente de conta para saber mais.


