---
nav_title: "Criação de notificações Rich"
article_title: "Criação de notificações por push avançadas para Android"
page_order: 3
page_layout: tutorial
description: "Este tutorial aborda como configurar as notificações Rich do Android para suas campanhas do Braze."
platform: Android
channel:
  - Push
tool:
  - Campaigns
  
---

# Criação de notificações por push avançadas para Android

> As notificações Rich permitem mais personalização em suas notificações por push, acrescentando conteúdo adicional além da simples cópia. As notificações do Android já incluem imagens nas notificações por push há algum tempo, chamadas de "imagem de notificação expandida".

## Pré-requisitos

Antes de criar uma notificação por push avançada para Android, observe os seguintes detalhes:

- As notificações Rich do Android não estão disponíveis ao criar uma campanha push rápida.
- As imagens de notificação estendida do Android devem ter uma proporção de 2:1, mas não têm um limite de tamanho.
- O Android também permite a configuração de uma imagem separada para a exibição de notificação padrão. Essas são as imagens de tamanho recomendado: 
  - **Pequeno:** 512x256
  - **Médio:** 1024x512 
  - **Grande:** 2048x1024
- Atualmente, as notificações Rich do Android só permitem imagens estáticas, incluindo os formatos de imagem JPEG e PNG. Ainda não há suporte para GIF e outros formatos de imagem.
- A adição de botões de ação por push à notificação por push pode afetar a área da imagem que pode ser exibida. Teste com a prévia do dashboard e dispositivos ativos para confirmar se os resultados estão de acordo com o esperado.

{% alert note %}
Embora a Braze forneça instruções sobre como configurar o rich push, a renderização real das notificações por push pode variar dependendo de fatores externos, como proporção do dispositivo, versão do Android, restrições específicas do OEM, entre outros. Recomendamos fazer um teste de envio para vários dispositivos Android para garantir que suas notificações por push sejam exibidas como você pretende.
{% endalert %}

## Configuração de sua notificação Rich no Android

### Etapa 1: Criar uma campanha push

Siga as etapas para [criar uma campanha]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) para compor uma notificação por push para Android. Você usará o mesmo criador para configurar notificações por push que não contenham conteúdo avançado.

### Etapa 2: Adicionar legendas

Adicione o **texto de resumo/capítulo da imagem** que você deseja exibir antes da imagem na notificação.

![A seção de imagem de notificação expandida onde você pode adicionar uma imagem ou inserir uma URL de imagem.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### Etapa 3: Adicionar mídia

Adicione sua imagem no campo **Expanded Notification Image (Imagem de notificação expandida)** no criador da mensagem. As imagens podem ser feitas upload diretamente pelo dashboard ou especificando um URL de conteúdo que esteja hospedado em outro lugar.

Para saber mais sobre as imagens compatíveis, consulte [Especificações da imagem]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push).

![Um usuário recebe uma notificação por push para iOS com "Olá" como título e "Obrigado por participar do nosso programa de fidelidade!" como texto.]({% image_buster /assets/img_archive/android_rich_image.png %})

### Etapa 4: Continue criando sua campanha

Depois que o conteúdo da notificação Rich for feito upload no dashboard, você poderá continuar [programando sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

