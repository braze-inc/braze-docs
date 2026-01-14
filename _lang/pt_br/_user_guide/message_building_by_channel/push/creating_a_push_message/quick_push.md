---
nav_title: Mensagens push rápidas
article_title: Mensagens push rápidas
alias: "/quick_push/"
description: "Este artigo descreve o que você deve saber ao criar uma campanha push ou o Canvas usando a experiência de edição rápida de push."
---

# Mensagens push rápidas

Ao criar uma campanha push ou Canvas no Braze, você pode selecionar várias plataformas e dispositivos para criar uma mensagem para todas as plataformas em uma única experiência de edição chamada quick push.

## Casos de uso

Essa experiência de edição é melhor para os seguintes casos de uso:

- Campanhas push para celular e etapas do Canvas Message que precisam ser enviadas para vários tipos de dispositivos (como iOS e Android).
- Notificações push sensíveis ao tempo que precisam ser direcionadas a várias plataformas de forma rápida e precisa, onde o conteúdo é o mesmo em todas as plataformas (como notícias de última hora ou atualizações de jogos ao vivo).

## Criação de uma campanha push rápida ou Canvas

Para criar uma campanha direcionada a várias plataformas e dispositivos:

1. Crie uma campanha ou adicione uma [etapa de mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) a um Canvas.  
2. Selecione **Notificação por push**.
3. Selecione as plataformas desejadas (Mobile, Web, Kindle) e os dispositivos móveis (iOS, Android). Se você selecionar vários dispositivos, o teste multivariado não estará disponível para sua campanha.

### Seleção de plataformas para uma campanha
Opções para selecionar várias plataformas para uma campanha push, como Mobile, Web e Kindle, e vários dispositivos, como iOS e Android.]({% image_buster /assets/img_archive/quick_push_1.png %})

### Seleção de plataformas para uma etapa do Canvas
Opções para selecionar várias plataformas para uma etapa de mensagem push, como Mobile, Web e Kindle, e vários dispositivos, como iOS e Android.]({% image_buster /assets/img_archive/quick_push_4.png %})

{:start="4"}
4\. Selecione **Confirm (Confirmar**). Depois de selecionar **Confirm (Confirmar**), você não poderá alterar as plataformas ou os dispositivos selecionados.
5\. Continue configurando sua campanha ou Canvas.

Seu compositor terá uma aparência ligeiramente diferente da usual. Continue lendo para ver o que há de diferente.

### O que há de diferente

Na guia **Compose**, você pode especificar um título, uma mensagem e um comportamento ao clicar para todas as plataformas e dispositivos escolhidos.

O painel de visualização mostra uma aproximação da aparência de sua mensagem em cada plataforma. Embora isso possa lhe dar um bom indicador de onde você pode atingir os limites de caracteres, lembre-se de sempre testar suas mensagens em um dispositivo real antes de enviar sua campanha.

Visualização de edição única com um campo de título, mensagem e comportamento ao clicar para três tipos de push: iOS, Android e Web.]({% image_buster /assets/img_archive/quick_push_2.png %})

Na seção **Assets (Ativos** ), selecione ou carregue as imagens que deseja exibir para cada plataforma. Lembre-se de que dispositivos diferentes têm especificações diferentes para imagens e contagem de caracteres. Consulte [Formatos de mensagens e imagens push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/) para obter ajuda.

Seção Assets da visualização de edição única com campos para Push Icon Image, imagem de notificação do iOS, imagem de notificação do Android e imagem de notificação da Web.]({% image_buster /assets/img_archive/quick_push_3.png %}){:style="max-width:50%"}

Em seguida, conclua a configuração de sua campanha push normalmente. Consulte [Criação de uma campanha push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) para obter mais detalhes.

## Coisas para saber

### Tipo de notificação

O tipo de notificação padrão é "Standard Push" e não pode ser alterado. Se você quiser criar um push diferente, como Push Stories ou Inline Image (Android), crie campanhas separadas para cada tipo de dispositivo.

### Testes multivariados

Se você selecionar vários dispositivos para plataformas móveis, como iOS e Android, o teste multivariado não estará disponível para sua campanha. Se você quiser realizar testes multivariados, crie campanhas separadas para cada tipo de dispositivo.

### Configurações específicas do dispositivo

Você pode editar as configurações específicas da plataforma no editor. Isso inclui configurações como [botões de ação]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_action_buttons/), canais e grupos de notificação, TTL, prioridade de exibição, sons e muito mais. 

Observe que os botões de ação de envio não são compatíveis quando se tem como alvo o iOS e o Android usando campanhas de envio rápido. Para obter mais informações sobre as configurações específicas do dispositivo, consulte as coleções de artigos a seguir:

- [Opções do iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios)
- [Opções do Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android)


