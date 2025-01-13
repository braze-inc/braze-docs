---
nav_title: Criação de um item do feed de notícias
article_title: Criação de um item do feed de notícias
page_order: 3
page_type: reference
description: "Este artigo de referência aborda como criar um item do Feed de notícias. Os itens do feed de notícias permitem inserir conteúdo permanente diretamente em seu app a partir do dashboard da Web."
channel: news feed
hidden: true


---

# Criação de um item do feed de notícias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Os itens do feed de notícias permitem inserir conteúdo permanente diretamente em seu app a partir do dashboard da Web. Melhor ainda, o Feed de notícias também pode ser direcionado a segmentos individuais, assim como todos os nossos outros tipos de mensagens. Isso significa que o que você vê no feed pode ser completamente diferente de outra pessoa. As possibilidades para o feed de notícias são quase ilimitadas.

Dê uma olhada em nossos [estudos de caso][13], [casos de uso][15] e [práticas recomendadas][16] para ver exemplos e dicas úteis sobre feeds de notícias.

## Etapa 1: Clique em criar cartão

Primeiro, é preciso escolher o tipo de item do feed de notícias que deseja enviar aos seus usuários. No menu suspenso, você pode selecionar qualquer um dos quatro tipos de cartão do Feed de notícias.

![O botão Create Card (Criar cartão) no dashboard do Braze. As opções expandidas do menu suspenso para criar um cartão: Clássico, Imagem com legenda e Banner.][1]

### Especificações do cartão do feed de notícias

#### Cartões do feed de notícias

<br>![Uma prévia do cartão clássico com o ícone do Facebook, um cabeçalho que diz "Like us on Facebook!" (Curta-nos no Facebook!) com duas linhas de texto: "Click Here!" e "www.facebook.com".][2]{: style="max-width:40%;"}

Os cartões padrão do feed de notícias consistem em:

- Imagem 110x110
- Título
- Texto do corpo
- Link (no app ou na Web)

#### Cartões com imagens legendadas

<br>![Uma prévia do cartão de imagem legendada com uma imagem de uma torta de maçã e maçãs. Há um cabeçalho abaixo da imagem que diz "Promoção de férias! Economize quase 50 dólares!" com o seguinte texto: "Por tempo limitado, ganhe quatro tortas de maçã premium pelo preço de 3. Corra! A oferta não vai durar muito. Clique aqui para resgatar. www.example.com".][3]{: style="max-width:40%;"}

Os cartões com imagens legendadas consistem em:

- Imagem 600x450
- Título
- Texto do corpo
- Link (no app ou na Web)

#### Cartões de banner

<br>![Prévia de um cartão de banner com uma imagem que diz "Isto é um banner".][4]{: style="max-width:40%;"}

Os cartões de banner consistem em:

- Imagem 600x100
- Link (no app ou na Web)

#### Diretrizes de imagem

|          Tipo de cartão         |          Relação de aspecto         | Tamanho de imagem recomendado | Tamanho máximo da imagem |   Tipos de arquivos  |
|:-----------------------------:|:----------------------:|:------------------:|:-------------:|
|          Clássico         | 1:1 (mínimo de 110 pixels de largura) |          500 KB         |         1 MB        | PNG, JPEG, GIF |
|          Imagem legendada         | 4:3 (mínimo de 600 pixels de largura) |          500 KB         |         1 MB        | PNG, JPEG, GIF |
|          Banner         | 6:1 (mínimo de 600 pixels de largura) |          500 KB         |         1 MB        | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

- Recomenda-se o uso de arquivos PNG.
- É necessária uma biblioteca de carregamento de imagens personalizada para exibir GIFs no Android. Recomendamos o Glide.
- Imagens menores e de alta qualidade serão carregadas mais rapidamente, portanto é recomendável usar o menor ativo possível para obter o resultado desejado.

## Etapa 2: Adicione um título, resumo, imagem e links

É hora de criar seu cartão do Feed de notícias! Crie um título e um resumo para seu cartão e faça upload de uma imagem para acompanhá-lo. Você também pode definir o comportamento do link nessa página. Esse link pode ser um link padrão ou um [deep linking][7] para o conteúdo do app.

![Editor de itens do feed de notícias que mostra o nome do cartão, a prévia do cartão e os detalhes de personalização do idioma.][6]

## Etapa 3: Selecione uma programação

No editor do cartão do feed de notícias, você encontrará opções de quando publicar esse item. Você pode optar por publicá-lo imediatamente após a criação ou definir um horário no futuro para publicá-lo. Também é possível optar por entregar o cartão do feed de notícias em um horário específico no **fuso local dos usuários, marcando a caixa de seleção Publicar para usuários no fuso horário local**.

![][8]

## Etapa 4: Selecione um segmento

Você pode configurar seu cartão do feed de notícias para direcionamento a qualquer [segmento][10] que você tenha definido no dashboard em qualquer horário que desejar. Selecione seu segmento-alvo clicando no menu suspenso. Aqui, é possível ver estatísticas de alto nível, incluindo a disponibilidade de e-mail e o valor do tempo de vida por usuário.

![][11]

## Etapa 5: Revisar detalhes e publicar

Em seguida, você será levado a uma página que exibe todos os detalhes sobre o seu cartão (e a mensagem no app do acompanhante, se aplicável). Você pode revisar qualquer detalhe desses itens e editá-los, se necessário, clicando no ícone de lápis em qualquer um dos cabeçalhos.

![][12]

É isso aí! Você está pronto! Você publicou seu primeiro cartão de feed de notícias!

## Opcional: Vincule um cartão do feed de notícias a uma mensagem no app

As campanhas em vários canais geralmente levam a melhores taxas gerais de conversão e engajamento, por isso o Braze facilitou a vinculação de uma mensagem no app a um cartão específico do feed de notícias. 

Depois de iniciar um cartão do feed de notícias, um botão aparecerá na página de estatísticas do novo feed, permitindo que você "crie uma mensagem associada no app". Ao clicar nessa opção, você será levado ao criador da campanha para uma nova campanha de mensagens no app. Enquanto você insere o texto, a aparência e a sensação da mensagem no app, o Braze copia automaticamente as regras de entrega e direcionamento do cartão do Feed de notícias associado para garantir que as campanhas sejam lançadas juntas.

## Organização de seu feed de notícias

Você pode reordenar seus cartões na página do Feed de notícias.
- Os cartões no feed são ordenados primeiro pelo fato de terem sido vistos ou não pelo usuário; os itens não vistos ficam na parte superior do feed.
  - Um cartão é considerado lido se tiver recebido uma impressão no feed.
  - As impressões só serão contadas se o cartão puder ser visualizado no feed (ou seja, se um usuário não rolar a tela para baixo para ler um cartão, a impressão não será contada).
- Os cartões são então ordenados pela data e hora de criação, onde os itens mais recentes são os primeiros.

[1]: {% image_buster /assets/img_archive/newsfeed1_new.png %}
[2]: {% image_buster /assets/img_archive/classiccard.png %}
[3]: {% image_buster /assets/img_archive/captionedimage.png %}
[4]: {% image_buster /assets/img_archive/newsfeedbanner.png %}
[6]: {% image_buster /assets/img_archive/news-feed-title-summary_new.png %}
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/
[8]: {% image_buster /assets/img_archive/newsfeed2_new.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[11]: {% image_buster /assets/img_archive/targetsegment_new.png %}
[12]: {% image_buster /assets/img_archive/newsfeedpreview_new.png %}
[13]: https://www.braze.com/customers
[14]: {% image_buster /assets/img_archive/linked-in-app_new.png %}
[15]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/news_feed_use_cases/
[16]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
