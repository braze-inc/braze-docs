---
nav_title: Comportamento da ID de despacho
article_title: Comportamento da ID de despacho
page_order: 0

page_type: solution
description: "Este artigo de ajuda cobre o comportamento do ID de despacho, incluindo seu uso, implicações e limitações."
---

# Comportamento de ID de despacho

Um `dispatch_id` é o ID do envio da mensagem—um ID único para cada "transmissão" enviada pela Braze. Os usuários que recebem uma mensagem agendada recebem o mesmo `dispatch_id`. Normalmente, mensagens baseadas em ações ou acionadas por API receberão um `dispatch_id` único por usuário, mas mensagens enviadas em proximidade próxima a outra podem compartilhar o mesmo `dispatch_id` entre vários usuários.

Isso pode resultar em dois usuários diferentes tendo IDs de despacho diferentes para uma única campanha se as mensagens foram enviadas em dois momentos diferentes. Isso costuma acontecer porque as solicitações da API foram feitas separadamente. Se ambos os usuários estivessem no mesmo público de campanha em um único envio, seus IDs de despacho seriam os mesmos.

## Comportamento de ID de despacho em campanhas

Mensagens de campanha agendadas recebem o mesmo `dispatch_id`. Mensagens de campanha baseadas em ação ou acionadas por API podem obter um `dispatch_id` exclusivo por usuário, ou o `dispatch_id` pode ser o mesmo para vários usuários quando enviadas em proximidade ou na mesma chamada de API, conforme descrito acima. Por exemplo, dois usuários no público da sua campanha agendada terão o mesmo `dispatch_id` cada vez que a campanha for agendada. No entanto, dois usuários no público de uma campanha acionada por API podem ter IDs de despacho diferentes se foram enviados em chamadas de API separadas e não em proximidade um do outro.

As campanhas multicanal terão o mesmo comportamento descrito para o seu tipo de entrega.

{% alert warning %}
Um `dispatch_id` é gerado aleatoriamente para todas as etapas do canva porque o Braze trata as etapas do canva como eventos acionados, mesmo quando estão "agendadas". Isso pode resultar em inconsistências na geração dos IDs. Às vezes, um componente de canva terá um `dispatch_id` exclusivo por usuário por envio, ou poderá ter IDs de despacho compartilhados entre usuários por envio.
{% endalert %}

## Modelo de ID de despacho em mensagens com Liquid

Se você quiser rastrear o envio de uma mensagem de dentro da mensagem (em um URL, por exemplo), você pode usar o modelo no `dispatch_id`. Você pode encontrar a formatação para isso em Atributos de canva em nossa lista de [tags de personalização suportadas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Isso se comporta exatamente como `api_id`, pois como o `api_id` não está disponível na criação da campanha, ele é modelado como um espaço reservado e será prévia como `dispatch_id_for_unsent_campaign`. O ID é gerado antes que a mensagem seja enviada e será incluído no momento do envio.

{% alert warning %}
A modelagem Liquid de `dispatch_id_for_unsent_campaign` não funciona com mensagens no app, pois as mensagens no app não têm um `dispatch_id`.
{% endalert %}

## Campo de Correntes de ID de despacho para e-mail

Para continuar aprimorando nossos recursos do Currents, `dispatch_id` também é um campo nos eventos de e-mail do Currents em todos os tipos de conector. O `dispatch_id` é o ID único gerado para cada transmissão, ou despacho, enviado da plataforma Braze.

Embora todos os clientes que recebem uma mensagem agendada recebam o mesmo `dispatch_id`, os clientes que recebem mensagens baseadas em ações ou acionadas por API receberão um `dispatch_id` único por mensagem. O campo `dispatch_id` permite que você identifique qual instância de uma campanha recorrente é responsável pela conversão, fornecendo assim mais insights e informações sobre quais tipos de campanhas estão ajudando a push a agulha em seus objetivos de negócios.

Você pode usar `dispatch_id` como uma [tag de personalização]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags), em [eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/), ou quando você usa [Segment]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details), [Mixpanel]({{site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents/#email-events) ou [Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_for_currents/) para Currents.

_Última atualização em 15 de julho de 2021_
