---
nav_title: Configurações push
article_title: Configurações push
page_order: 16
page_type: reference
description: "Este artigo fornece uma visão geral das configurações de push no dashboard do Braze."
channel: push

---

# Configurações push

> A página **Configurações de push** permite que você defina as principais configurações das notificações por push, incluindo o TTL (Push Time to Live) e a prioridade FCM padrão para campanhas Android. Essas configurações ajudam a otimizar a entrega e a eficácia de suas notificações por push, garantindo uma melhor experiência para seus usuários.

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

1. Acesse **Configurações** > **Gerenciar configurações** > Configurações **push**.
2. Para cada plataforma Android, defina um valor padrão de TTL. É possível definir incrementos menores, como horas ou segundos, para um controle mais preciso.
3. Selecione **Salvar** para aplicar suas alterações.

![Configurações push TTL para dispositivos Firebase, Web, Kindle e Huawei.]({% image_buster /assets/img/push_ttl.png %})

## Prioridade FCM padrão para campanhas no Android

Você pode definir a prioridade padrão do Firebase Cloud Messaging (FCM) para todas as campanhas de mensagens do Android. Essa prioridade determina como a notificação por push é entregue aos dispositivos dos usuários.

As opções de prioridade da FCM incluem:

| Prioridade | Descrição | Caso de uso |
| --- | --- | --- |
| Normal | Prioridade de entrega padrão que otimiza o uso da bateria | Conteúdo que não requer atenção imediata |
| Alta | As mensagens são enviadas imediatamente | Notificações sensíveis ao tempo que exigem entrega imediata |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para definir a prioridade padrão do FCM:

1. Acesse **Configurações** > **Gerenciar configurações** > Configurações **push**.
2. Na seção FCM Priority (Prioridade do FCM), selecione "Normal" ou "High" como a configuração padrão.
3. Selecione **Salvar** para aplicar suas alterações.

![Configurações de prioridade de entrega do Android.]({% image_buster /assets/img/push_fcm_priority_settings.png %})

Essa configuração se aplica globalmente a todas as novas campanhas push do Android, a menos que uma prioridade diferente seja selecionada ao criar uma campanha específica. 

{% alert note %}
Se o FCM detectar que seu app envia frequentemente mensagens de alta prioridade que não resultam em notificações visíveis para o usuário ou no engajamento com o usuário, essas mensagens poderão ser automaticamente despriorizadas para a prioridade normal.
{% endalert %}

Para saber mais sobre os níveis de prioridade e a despriorização do FCM, consulte [Configurações avançadas de campanha]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#fcm-priority).

