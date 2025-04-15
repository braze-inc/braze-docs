---
nav_title: Configurações de TTL do push
article_title: Configurações de TTL do push
page_order: 16
page_type: reference
description: "Este artigo de referência aborda a página de configurações do Push Time to Live no dashboard da Braze."
channel: push

---

# Configurações push TTL

> Saiba mais sobre a página de configurações do Push Time to TTL no dashboard do Braze.

## O que é Push TTL?

O TTL (Push Time to Live) controla por quanto tempo o Braze tentará entregar uma notificação por push a dispositivos que estejam offline no momento em que a campanha for enviada. Se um dispositivo se reconectar após a expiração do TTL, a mensagem não será entregue. Essa configuração não removerá uma notificação se ela já tiver sido recebida pelo dispositivo do usuário - ela controla apenas por quanto tempo o provedor de push tenta entregar uma notificação.

## Configuração dos valores TTL padrão do push

Por padrão, o Braze define o Push TTL como o máximo para cada serviço de envio de mensagens push. 

| Serviço de envio de mensagens push | Máximo TTL |
| --- | --- |
| Web (por meio de serviços FCM ou Web Push) | 28 dias |
| Envio de mensagens do Firebase Cloud (FCM) | 28 dias |
| Kindle (ADM) | 31 dias |
| Huawei (HMS) | 15 dias |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Essas configurações se aplicam globalmente a todas as campanhas de mensagens, a menos que um TTL diferente seja definido para uma mensagem específica. Para ajustar o TTL de uma mensagem, consulte [Configurações avançadas de campanha]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#ttl).

Para definir um TTL padrão diferente para o push:

1. Acesse **Configurações** > **Gerenciar configurações** > **Configurações push TTL**.
2. Para cada plataforma Android, defina um valor padrão de TTL. É possível definir incrementos menores, como horas ou segundos, para um controle mais preciso.
3. Selecione **Salvar** para aplicar suas alterações.

![Guia de configurações de Push TTL no menu de Configurações][1]


[1]: {% image_buster /assets/img/push_ttl.png %}
