---
nav_title: Criação de um modelo de webhook
article_title: Criação de um modelo de webhook
page_order: 2
tool:
  - Templates
channel:
  - webhooks
description: "Este artigo de referência aborda como criar e personalizar modelos de webhook para uso posterior na plataforma Braze."

---

# Criação de um modelo de webhook

> Ao criar e personalizar seus webhooks, você pode criar e aproveitar modelos de webhooks para uso posterior na plataforma Braze. Dessa forma, você pode criar consistentemente uma variedade de webhooks em suas diferentes campanhas.

## Etapa 1: Acesse o editor de modelos de webhook

No dashboard do Braze, acesse **Modelos** > **Modelos de Webhook**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar essa página em **Engajamento** > **Modelos e mídias** > **Modelos de webhook**.
{% endalert %}

![A página "Webhook Templates" com modelos de webhook predefinidos e salvos.]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## Etapa 2: Escolha seu modelo

A partir daí, você pode optar por criar um novo modelo, usar um dos modelos de webhook predefinidos ou editar um modelo existente.

Por exemplo, se estiver usando o [LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line) como um canal de envio de mensagens, poderá configurar vários webhooks usando os modelos predefinidos para o **LINE Carousel** ou o **LINE Image**.

## Etapa 3: Preencher os detalhes do modelo

1. Dê ao seu modelo de webhook um nome exclusivo.
2. (Opcional) Adicione uma descrição do modelo para explicar como esse modelo deve ser usado.
3. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário para ajudar a encontrar e filtrar seu modelo.

## Etapa 4: Crie seu modelo

1. Digite o URL do webhook.
2. Selecione o método HTTP.
3. Adicione um corpo de solicitação. Pode ser **um par de chave/valor JSON** ou **texto bruto**.
4. (Opcional) Adicione um cabeçalho de solicitação. Isso pode ser exigido por seu destino de webhook.

![A guia "Compose" ao criar um modelo de webhook. Os campos disponíveis são URL do webhook, método HTTP, corpo da solicitação e cabeçalhos da solicitação. Você também pode adicionar idiomas.]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## Etapa 5: Teste seu modelo

Para ver a aparência do webhook antes de enviá-lo aos usuários, é possível enviar um webhook de teste usando a guia **Teste**. Aqui, é possível selecionar a prévia da mensagem como um usuário aleatório, usuário existente ou usuário personalizado.

## Etapa 6: Salve seu modelo

Certifique-se de salvar seu modelo selecionando **Save Template (Salvar modelo)**. Agora você está pronto para usar esse modelo em qualquer campanha que escolher.

{% alert note %}
As edições feitas em um modelo existente não são refletidas nas campanhas criadas com versões anteriores desse modelo.
{% endalert %}

## Gerenciando seus modelos

Você pode [duplicar e arquivar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) modelos de webhook para ajudar a organizar e gerenciar melhor sua lista de modelos.

Saiba mais sobre como criar e gerenciar modelos e conteúdo criativo em [Modelos e mídias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

