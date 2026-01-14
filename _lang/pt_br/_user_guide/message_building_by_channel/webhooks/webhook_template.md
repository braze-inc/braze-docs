---
nav_title: Criando um modelo de webhook
article_title: Criando um Modelo de Webhook
page_order: 2
tool:
  - Templates
channel:
  - webhooks
description: "Este artigo de referência cobre como criar e personalizar modelos de webhook para uso posterior na plataforma Braze."

---

# Criando um modelo de webhook

> À medida que você constrói e personaliza seus webhooks, pode criar e aproveitar modelos de webhook para uso posterior na plataforma Braze. Dessa forma, você pode construir consistentemente uma variedade de webhooks em suas diferentes campanhas.

## Passo 1: Vá para o editor de modelos de webhook

No painel do Braze, vá para **Modelos** > **Modelos de Webhook**.

\![A página "Modelos de Webhook" com modelos de webhook pré-desenhados e salvos.]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## Passo 2: Escolha seu modelo

A partir daqui, você pode optar por criar um novo modelo, usar um dos modelos de webhook pré-desenhados ou editar um modelo existente.

Por exemplo, se você estiver usando [LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line) como um canal de mensagens, pode configurar vários webhooks usando os modelos pré-desenhados para **Carrossel LINE** ou **Imagem LINE**.

## Passo 3: Preencha os detalhes do modelo

1. Dê ao seu modelo de webhook um nome único.
2. (Opcional) Adicione uma descrição do modelo para explicar como este modelo deve ser usado.
3. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário para ajudar a encontrar e filtrar seu modelo.

## Passo 4: Construa seu modelo

1. Insira a URL do webhook.
2. Selecione o método HTTP.
3. Adicione um corpo de solicitação. Isso pode ser **pares de chave/valor JSON** ou **texto bruto**.
4. (Opcional) Adicione um cabeçalho de solicitação. Isso pode ser necessário para o destino do seu webhook.

\![A guia "Compor" ao criar um modelo de webhook. Os campos disponíveis são URL do webhook, método HTTP, corpo da solicitação e cabeçalhos da solicitação. Você também pode adicionar idiomas.]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## Passo 5: Teste seu modelo

Para ver como seu webhook aparece antes de enviá-lo para seus usuários, você pode enviar um webhook de teste usando a guia **Teste**. Aqui, você pode selecionar visualizar a mensagem como um usuário aleatório, usuário existente ou usuário personalizado.

## Passo 6: Salve seu modelo

Certifique-se de salvar seu modelo selecionando **Salvar Modelo**. Você está agora pronto para usar este modelo em qualquer campanha que escolher.

{% alert note %}
Edições feitas em um modelo existente não são refletidas em campanhas que foram criadas usando versões anteriores desse modelo.
{% endalert %}

## Gerenciando seus modelos

Você pode [duplicar e arquivar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) modelos de webhook para ajudar a organizar e gerenciar melhor sua lista de modelos.

Saiba mais sobre como criar e gerenciar modelos e conteúdo criativo em [Modelos e Mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

