---
nav_title: Outubro
page_order: 3
noindex: true
page_type: update
description: "Este artigo contém notas de versão de outubro de 2016."
---

# Outubro de 2016

## Novas configurações de segurança
Adicionamos recursos de segurança aprimorados à Braze, incluindo regras de expiração de senha, regras de comprimento de senha, regras de complexidade de senha, lista de permissões de login de IP no dashboard e autenticação de dois fatores.

> Atualizar: As **Configurações de Segurança** do Braze, acessadas na página **Configurações da Empresa**, também incluem regras para reutilização e expiração de senhas.

## Baixar CSV após a importação
Os usuários do Braze agora podem baixar CSVs de usuários importados recentemente. Isso oferece mais visibilidade na sincronização de dados de seus sistemas. Saiba mais sobre a [importação de CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).

## Filtro de aniversário
Além do [filtro de aniversário]({{site.baseurl}}/user_guide/Engagement_Tools/Segments/Segmentation_Filters/), o Braze agora suporta um filtro de aniversário que lhe permite direcionar os usuários com base em uma data do calendário para marcos de fidelidade, avisos de recarga e muito mais! Acesse esse recurso selecionando o filtro "Date of Custom Attribute" (Data do atributo personalizado) na página Segments (Segmentos). Saiba mais sobre [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#segmentation-filters).

## Atualizações do limite de frequência
Anteriormente, uma campanha ou um Canva que ignorasse as restrições de limite de frequência ainda contaria para os limites de frequência. Alteramos o comportamento para que, por padrão, as novas campanhas e Canvas que não obedecerem aos limites de frequência também não sejam contabilizadas para esses limites. Isso é configurável para cada campanha e Canva. Saiba mais sobre o [limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping).

## Perfis de cores de mensagens no app
Adicionamos [perfis de cores]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) para mensagens no app, permitindo que os clientes reutilizem esquemas de cores da marca ao criar novas mensagens no Braze.
