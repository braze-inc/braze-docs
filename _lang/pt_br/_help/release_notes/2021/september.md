---
nav_title: Setembro
page_order: 3
noindex: true
page_type: update
description: "Este artigo contém notas de versão para setembro de 2021."
---

# Setembro de 2021

## iOS 15

### Proteção de privacidade de e-mail da Apple 

O MPP (Mail Privacy Protection) da Apple é uma atualização de privacidade que estará disponível para os usuários do app Apple Mail no iOS 15, iPadOS 15, macOS Monterey e watchOS 8, lançado em meados de setembro. Para os usuários que aceitam o MPP, os e-mails agora serão pré-carregados usando servidores proxy, armazenando imagens em cache e dificultando a capacidade de aproveitar os pixels de rastreamento para métricas como [rastreamento de abertura]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#open-tracking-pixel). Para saber mais sobre o MPP e problemas relacionados a métricas de entregabilidade de e-mail e problemas com campanhas pré-existentes e Canvas que disparam com base nessas métricas, visite nossa [documentação]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/).

### Recursos push

O iOS 15 introduziu novos recursos de notificação para ajudar os usuários a manter o foco e evitar interrupções frequentes ao longo do dia. Estamos empolgados em oferecer suporte a esses novos recursos, incluindo [Interruption Levels (níveis de interrupção) e Relevance Scores (pontuações de relevância]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/)).

## Cartões de contato

Os cartões de contato são um formato de arquivo padronizado para enviar informações comerciais e de contato que podem ser facilmente importadas para catálogos de endereços ou de contatos. Agora é possível fazer upload e criar cartões de contato para suas mensagens SMS e MMS. Para saber mais sobre como criar cartões de contato em nosso gerador de cartões de contato integrado, visite nossa [documentação]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/).

## Personalização dos cartões de conteúdo padrão

Você pode criar sua própria interface de cartões de conteúdo estendendo o site `ABKContentCardsTableViewController` para personalizar todos os elementos da interface do usuário e o comportamento dos cartões de conteúdo. Para saber mais sobre como personalizar o feed de cartões de conteúdo, acesse nossa [documentação]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/). 

## Limites de frequência da API

[Os limites de frequência]({{site.baseurl}}/api/basics/#api-limits/) serão aplicados a todos os clientes com integração após 16 de setembro de 2021. 

## Atualizações dos guias do desenvolvedor do Android e do FireOS

Os guias do desenvolvedor do Android e do FireOS foram mesclados em um único local. Artigos dedicados ao FireOS estarão disponíveis nesta [nova seção do Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Atualizações nos relatórios de funil e retenção

[Relatórios de funil]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) e [relatórios de retenção]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/) agora estão disponíveis para campanhas de SMS.
