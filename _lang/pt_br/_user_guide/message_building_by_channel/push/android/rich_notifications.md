---
nav_title: "Criação de notificações avançadas"
article_title: "Criação de notificações push avançadas para Android"
page_order: 3
page_layout: tutorial
description: "Este tutorial aborda como configurar notificações Android Rich para suas campanhas no Braze."
platform: Android
channel:
  - Push
tool:
  - Campaigns
  
---

# Criação de notificações push avançadas para Android

> As notificações avançadas permitem mais personalização em suas notificações por push, acrescentando conteúdo adicional além da simples cópia. As notificações do Android já incluem imagens nas notificações por push há algum tempo, chamadas de "imagem de notificação expandida".

## Pré-requisitos

Antes de criar uma notificação por push avançada para Android, observe os detalhes a seguir:

- As notificações avançadas do Android não estão disponíveis ao criar uma campanha push rápida.
- As imagens de notificação estendida do Android devem ter uma proporção de 2:1, mas não têm um limite de tamanho.
- O Android também permite a configuração de uma imagem separada para a exibição de notificação padrão. Essas são as imagens de tamanho recomendado: 
  - **Pequeno:** 512x256
  - **Médio:** 1024x512 
  - **Grande:** 2048x1024
- Atualmente, as notificações ricas do Android só permitem imagens estáticas, incluindo os formatos de imagem JPEG e PNG. Ainda não há suporte para GIF e outros formatos de imagem.
- A inclusão de botões de ação em sua notificação por push pode afetar a área da imagem que pode ser exibida. Teste com a visualização do painel e com dispositivos ativos para confirmar se os resultados estão de acordo com o esperado.
- O Braze Android SDK deve estar ativado para que a imagem seja renderizada.

{% alert note %}
Embora o Braze forneça instruções sobre como configurar o rich push, a renderização real das notificações rich push pode variar dependendo de fatores externos, como proporção do dispositivo, versão do Android, restrições específicas do OEM, entre outros. Recomendamos fazer um teste de envio para vários dispositivos Android para garantir que as notificações push avançadas apareçam como você pretende.
{% endalert %}

## Configuração de sua notificação avançada do Android

### Etapa 1: Criar uma campanha push

Siga as etapas para [criar uma campanha]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) para compor uma notificação por push para Android. Você usará o mesmo compositor para configurar notificações push que não contenham conteúdo avançado.

### Etapa 2: Adicionar legendas

Adicione o **texto de resumo/capítulo da imagem** que você deseja exibir antes da imagem na notificação.

A seção Expanded notification image (Imagem de notificação expandida), onde é possível adicionar uma imagem ou inserir um URL de imagem.]({% image_buster /assets/img_archive/android_rich_summarytext.png %})

### Etapa 3: Adicionar mídia

Adicione sua imagem no campo **Expanded Notification Image (Imagem de notificação expandida** ) no compositor da mensagem. As imagens podem ser carregadas diretamente pelo painel ou especificando um URL de conteúdo que esteja hospedado em outro lugar.

Para obter detalhes sobre as imagens compatíveis, consulte [Especificações da imagem]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push).

Um usuário recebe uma notificação por push para iOS com "Hi there" como título e "Thanks for joining out loyalty program!" como texto.]({% image_buster /assets/img_archive/android_rich_image.png %})

### Etapa 4: Continue criando sua campanha

Depois que o conteúdo da notificação avançada for carregado no painel, você poderá continuar a [programar sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

