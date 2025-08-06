---
nav_title: Junho
page_order: 7
noindex: true
page_type: update
description: "Este artigo contém notas de versão para junho de 2020."
---
# Junho de 2020

## Relatórios de retenção

Os Relatórios de retenção agora oferecem Retenção de intervalo para [campanhas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/) e [telas]({{site.baseurl}}/user_guide/engagement_tools/canvas/retention_reports/). O Range Retention mede quantos usuários retornam e realizam um evento de retenção selecionado durante intervalos de tempo específicos. 

## Atualizações da API de rastreamento do usuário

O [endpoint`users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) agora tem uma taxa padrão de 50.000 solicitações de API por minuto para empresas de dashboard criadas após 2 de junho de 2020. As empresas existentes criadas antes dessa data e seus espaços de trabalho ainda poderão receber solicitações ilimitadas de API para o ponto de extremidade `users/track`.

O Braze está impondo esse padrão em nosso endpoint voltado para o cliente mais utilizado como uma etapa em direção às nossas metas de estabilidade e confiabilidade para nossa API e infraestrutura. O limite imposto é muito liberal e afetará muito poucas empresas do dashboard e suas operações regulares. Caso precise aumentar esse limite, entre em contato com seu gerente de sucesso do cliente ou com nossa equipe de suporte para solicitar um aumento.

