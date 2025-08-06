---
nav_title: Agosto
page_order: 6
noindex: true
page_type: update
description: "Este artigo contém notas de versão de agosto de 2018."
---
# Agosto de 2018

## Grupos de notificação do iOS 12

A versão mais recente do iOS 12 oferece suporte ao agrupamento de notificações (semelhante aos canais de notificação do Android) para aplicativos. [A Braze permite que você utilize esse recurso de agrupamento no iOS usando nosso criador de mensagens.]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)

## Disparo de story por push

Agora é possível redirecionar usuários com base em cliques em páginas específicas nos slides do Push Story. Use o filtro adicional para **Interagir com a campanha**.

## Eventos de dados do S3 e do Azure de usuários anônimos

Os clientes que exportam dados para o Amazon S3 e o Microsoft Azure agora podem incluir eventos de usuários anônimos. Essa funcionalidade será ativada por padrão para todas as integrações recém-criadas, mas permanecerá desativada para todas as integrações existentes. Se tiver alguma dúvida, entre em contato com seu gerente de conta ou abra um [ticket de suporte]({{site.baseurl}}/braze_support/).

## Integração de coortes do Mixpanel

Os clientes do Braze e do Mixpanel agora podem integrar e [enviar coortes do Mixpanel para o Braze como filtros de segmento]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#mixpanel-cohort-import). Você pode configurar uma exportação manual única ou uma exportação dinâmica a cada duas horas. Cada usuário atualizado contará como um ponto de dados, mas o Mixpanel envia apenas as alterações desde a última sincronização.

