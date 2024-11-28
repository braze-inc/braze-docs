---
nav_title: Campanhas push rápidas
article_title: Campanhas push rápidas
alias: "/quick_push/"
description: "Este artigo descreve o que você deve saber ao criar uma campanha push usando a experiência de edição rápida de push."
---

# Campanhas push rápidas

Ao criar uma campanha de mensagens push no Braze, você pode selecionar várias plataformas e dispositivos para criar uma mensagem para todas as plataformas em uma única experiência de edição chamada quick push.

{% alert important %}
Essa funcionalidade está disponível apenas para campanhas.
{% endalert %}

## Casos de uso

Essa experiência de edição é melhor para os seguintes casos de uso:

- Campanhas push para celular que precisam ser enviadas para vários tipos de dispositivos (como iOS e Android).
- Notificações por push sensíveis ao tempo que precisam ser direcionadas a várias plataformas de forma rápida e precisa, onde o conteúdo é o mesmo em todas as plataformas (como notícias de última hora ou atualizações de jogos ao vivo).

## Criação de uma campanha push rápida

Para criar uma campanha com direcionamento para várias plataformas e dispositivos:

1. Acesse **Campaigns (Campanhas** ) e clique em **Create Campaign (Criar campanha**).
2. Selecione **Notificações por push**.
3. Selecione as plataformas desejadas (Mobile, Web, Kindle) e os dispositivos móveis (iOS, Android). Se você selecionar vários dispositivos, os testes multivariantes não estarão disponíveis para sua campanha.

![Opções para selecionar várias plataformas para uma campanha push, como Mobile, Web e Kindle, e vários dispositivos, como iOS e Android.][1]

{:start="4"}
4\. Clique em **Avançar**. Após clicar em **Next**, não será possível alterar as plataformas ou dispositivos selecionados.
5\. Continue configurando sua campanha push.

Seu criador terá uma aparência ligeiramente diferente da habitual. Continue lendo para ver o que há de diferente.

### O que há de diferente

Na guia **Compose**, é possível especificar um título, uma mensagem e um comportamento ao clicar para todas as plataformas e dispositivos escolhidos.

O painel de prévia mostra uma aproximação da aparência de sua mensagem em cada plataforma. Embora isso possa lhe dar um bom indicador de onde você pode atingir os limites de caracteres, lembre-se de sempre testar suas mensagens em um dispositivo real antes de enviar sua campanha.

![Visualização de edição única com um campo de título, mensagem e comportamento ao clicar para três tipos de push: iOS, Android e Web.][2]

Na seção **Assets (Ativos** ), selecione ou faça upload das imagens que deseja exibir para cada plataforma. Lembre-se de que dispositivos diferentes têm especificações diferentes para imagens e contagem de caracteres. Consulte [Formatos de mensagens e imagens push][3] para obter ajuda.

![Seção de ativos da visualização de edição única com campos para imagem de ícone por push, imagem de notificação do iOS, imagem de notificação do Android e imagem de notificação da Web.][4]{:style="max-width:50%"}

Em seguida, termine de configurar sua campanha push normalmente. Consulte [Criação de uma campanha push][5] para obter mais detalhes.

## Coisas para saber

### Tipo de notificação

O tipo de notificação padrão é "Standard Push" e não pode ser alterado. Para criar outro push, como stories por push ou imagem inline (Android), crie campanhas separadas para cada tipo de dispositivo.

### Testes multivariantes

Se você selecionar vários dispositivos para plataformas móveis, como iOS e Android, os testes multivariantes não estarão disponíveis para sua campanha. Se você quiser realizar testes multivariantes, crie campanhas separadas para cada tipo de dispositivo.

### Configurações específicas do dispositivo

As configurações específicas para iOS e Android não são suportadas quando várias plataformas ou dispositivos são selecionados. Isso inclui configurações como [botões de ação por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_action_buttons/), canais e grupos de notificação, TTL, prioridade de exibição, sons e muito mais.

Para saber mais sobre as configurações específicas do dispositivo, consulte as seguintes coleções de artigos:

- [Opções do iOS][6]
- [Opções do Android][7]


[1]: {% image_buster /assets/img_archive/quick_push_1.png %}
[2]: {% image_buster /assets/img_archive/quick_push_2.png %}
[4]: {% image_buster /assets/img_archive/quick_push_3.png %}

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/ios
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android