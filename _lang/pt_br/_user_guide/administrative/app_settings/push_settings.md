---
nav_title: Configurações de push
article_title: Configurações push
page_order: 16
page_type: reference
description: "Este artigo fornece uma visão geral das configurações de push no painel do Braze."
channel: push

---

# Configurações push

> A página **Push Settings (Configurações** de push) permite que você defina as principais configurações para suas notificações push, incluindo o Push Time to Live (TTL) e a prioridade FCM padrão para campanhas do Android. Essas configurações ajudam a otimizar a entrega e a eficácia das suas notificações por push, garantindo uma melhor experiência para os usuários.

## O que é Push TTL?

O Push Time to Live (TTL) controla por quanto tempo o Braze tentará enviar uma notificação push para dispositivos que estejam off-line no momento em que a campanha for enviada. Se um dispositivo se reconectar após a expiração do TTL, a mensagem não será entregue. Essa configuração não removerá uma notificação se ela já tiver sido recebida pelo dispositivo do usuário - ela controla apenas por quanto tempo o provedor de push tenta entregar uma notificação.

## Configuração dos valores padrão do Push TTL

Por padrão, o Braze define o Push TTL como o máximo para cada serviço de mensagens push. 

| Serviço de mensagens push | Máximo TTL |
| --- | --- |
| Web (por meio de serviços FCM ou Web Push) | 28 dias |
| Firebase Cloud Messaging (FCM) | 28 dias |
| Kindle (ADM) | 31 dias |
| Huawei (HMS) | 15 dias |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Essas configurações se aplicam globalmente a todas as campanhas push, a menos que um TTL diferente seja definido para uma mensagem específica. Para ajustar o TTL de uma mensagem, consulte [Configurações avançadas de campanha]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#ttl).

Para definir um Push TTL padrão diferente:

1. Vá para **Configurações** > **Gerenciar configurações** > **Configurações por push**.
2. Para cada plataforma Android, defina um valor padrão de tempo de vida. É possível definir incrementos menores, como horas ou segundos, para um controle mais preciso.
3. Selecione **Salvar** para aplicar suas alterações.

Configurações push TTL para dispositivos Firebase, Web, Kindle e Huawei.]({% image_buster /assets/img/push_ttl.png %})

## Prioridade FCM padrão para campanhas Android

Você pode definir a prioridade padrão do Firebase Cloud Messaging (FCM) para todas as campanhas push do Android. Essa prioridade determina como a notificação por push é entregue aos dispositivos dos usuários.

As opções de prioridade da FCM incluem:

| Prioridade | Descrição | Caso de uso |
| --- | --- | --- |
| Normal | Prioridade de entrega padrão que otimiza o uso da bateria | Conteúdo que não requer atenção imediata |
| Alta | As mensagens são enviadas imediatamente | Notificações sensíveis ao tempo que exigem entrega imediata |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para definir a prioridade padrão do FCM:

1. Vá para **Configurações** > **Gerenciar configurações** > **Configurações por push**.
2. Na seção FCM Priority (Prioridade do FCM), selecione "Normal" ou "High" como a configuração padrão.
3. Selecione **Salvar** para aplicar suas alterações.

\![Configurações de prioridade de entrega do Android.]({% image_buster /assets/img/push_fcm_priority_settings.png %})

Essa configuração se aplica globalmente a todas as novas campanhas push do Android, a menos que uma prioridade diferente seja selecionada ao criar uma campanha específica. 

{% alert note %}
Se o FCM detectar que seu aplicativo envia com frequência mensagens de alta prioridade que não resultam em notificações visíveis para o usuário ou no envolvimento do usuário, essas mensagens poderão ser automaticamente despriorizadas para a prioridade normal.
{% endalert %}

Para obter informações mais detalhadas sobre os níveis de prioridade e a despriorização do FCM, consulte [Configurações avançadas de campanha]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#fcm-priority).

