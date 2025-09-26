---
nav_title: Mensagens de Push Rápidas
article_title: Mensagens de Push Rápidas
alias: "/quick_push/"
description: "Este artigo descreve coisas a saber ao criar uma campanha de push ou Canvas usando a experiência de edição rápida de push."
---

# Mensagens de push rápidas

Ao criar uma campanha de push ou Canvas no Braze, você pode selecionar várias plataformas e dispositivos para criar uma mensagem para todas as plataformas em uma única experiência de edição chamada push rápido.

## Casos de uso

Essa experiência de edição é melhor para os seguintes casos de uso:

- Campanhas de push móvel e etapas de mensagem do Canvas que precisam ser enviadas para vários tipos de dispositivos (como iOS e Android).
- Notificações por push sensíveis ao tempo que precisam ser direcionadas a várias plataformas de forma rápida e precisa, onde o conteúdo é o mesmo em todas as plataformas (como notícias de última hora ou atualizações de jogos ao vivo).

## Criando uma campanha de push rápida ou Canvas

Para criar uma campanha com direcionamento para várias plataformas e dispositivos:

1. Crie uma campanha ou adicione uma [etapa de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) a um canva.  
2. Selecione **Notificação por push**.
3. Selecione as plataformas desejadas (Mobile, Web, Kindle) e os dispositivos móveis (iOS, Android). Se você selecionar vários dispositivos, os testes multivariantes não estarão disponíveis para sua campanha.

### Selecionando plataformas para uma campanha
![Opções para selecionar várias plataformas para uma campanha de push, como Mobile, Web e Kindle, e vários dispositivos, como iOS e Android.]({% image_buster /assets/img_archive/quick_push_1.png %})

### Selecionando plataformas para uma etapa do Canvas
![Opções para selecionar várias plataformas para um passo de Mensagem push, como Mobile, Web e Kindle, e vários dispositivos, como iOS e Android.]({% image_buster /assets/img_archive/quick_push_4.png %})

{:start="4"}
4\. Selecione **Confirmar**. Após selecionar **Confirmar**, você não poderá alterar suas plataformas ou dispositivos selecionados.
5\. Continue configurando sua campanha ou Canvas.

Seu criador terá uma aparência ligeiramente diferente da habitual. Continue lendo para ver o que há de diferente.

### O que há de diferente

Na guia **Compose**, é possível especificar um título, uma mensagem e um comportamento ao clicar para todas as plataformas e dispositivos escolhidos.

O painel de prévia mostra uma aproximação da aparência de sua mensagem em cada plataforma. Embora isso possa lhe dar um bom indicador de onde você pode atingir os limites de caracteres, lembre-se de sempre testar suas mensagens em um dispositivo real antes de enviar sua campanha.

![Visualização de edição única com um título, mensagem e campo de comportamento ao clicar para três tipos de push: iOS, Android e Web.]({% image_buster /assets/img_archive/quick_push_2.png %})

Na seção **Assets (Ativos** ), selecione ou faça upload das imagens que deseja exibir para cada plataforma. Lembre-se de que dispositivos diferentes têm especificações diferentes para imagens e contagem de caracteres. Consulte [Formatos de mensagens e imagens push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/) para obter ajuda.

![Seção de ativos da visualização de edição única com campos para Imagem do Ícone de Push, imagem de notificação do iOS, imagem de notificação do Android e imagem de notificação da Web.]({% image_buster /assets/img_archive/quick_push_3.png %}){:style="max-width:50%"}

Em seguida, termine de configurar sua campanha push normalmente. Consulte [Criação de uma campanha push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) para obter mais detalhes.

## Coisas para saber

### Tipo de notificação

O tipo de notificação padrão é "Standard Push" e não pode ser alterado. Para criar outro push, como stories por push ou imagem inline (Android), crie campanhas separadas para cada tipo de dispositivo.

### Testes multivariantes

Se você selecionar vários dispositivos para plataformas móveis, como iOS e Android, os testes multivariantes não estarão disponíveis para sua campanha. Se você quiser realizar testes multivariantes, crie campanhas separadas para cada tipo de dispositivo.

### Configurações específicas do dispositivo

Você pode editar configurações específicas da plataforma no editor. Isso inclui configurações como [botões de ação por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_action_buttons/), canais e grupos de notificação, TTL, prioridade de exibição, sons e muito mais. 

Observe que os botões de ação por push não são suportados ao direcionar tanto iOS quanto Android usando campanhas de push rápidas. Para saber mais sobre as configurações específicas do dispositivo, consulte as seguintes coleções de artigos:

- [Opções do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios)
- [Opções do Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android)


