---
nav_title: Catálogos
article_title: Catálogos
page_order: 6
layout: dev_guide

guide_top_header: "Catálogos"
guide_top_text: "Os catálogos acessam dados de arquivos CSV importados e pontos de extremidade de API para enriquecer suas mensagens, da mesma forma que você acessaria atributos personalizados ou propriedades de eventos personalizados por meio do Liquid."

description: "Essa página de destino abriga os catálogos. Use catálogos e conjuntos filtrados para aproveitar os dados de não usuários em suas campanhas no Braze para enviar mensagens personalizadas."

guide_featured_title: "Artigos de seção"
guide_featured_list:
- name: Criação de um catálogo
  link: /docs/user_guide/data/activation/catalogs/create/
  image: /assets/img/braze_icons/users-01.svg
- name: Uso de catálogos
  link: /docs/user_guide/data/activation/catalogs/use/
  image: /assets/img/braze_icons/users-01.svg
- name: Notificações de estoque em espera
  link: /docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Notificações de queda de preço
  link: /docs/price_drop_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Seleções
  link: /docs/user_guide/data/activation/catalogs/selections/
  image: /assets/img/braze_icons/list.svg

guide_menu_title: "Other articles"
guide_menu_list:
- name: Endpoints da API de catálogos
  link: /docs/api/endpoints/catalogs/
  image: /assets/img/braze_icons/server-01.svg
- name: Blocos de produtos de arrastar e soltar
  link: /docs/dnd_product_blocks/
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## Casos de uso do catálogo

Você pode trazer qualquer tipo de dados para um catálogo. Normalmente, os dados são metadados sobre ofertas, como produtos, descontos, promoções, eventos e similares. Veja os casos de uso abaixo para obter alguns exemplos de como você pode usar esses dados para direcionar os usuários com mensagens altamente relevantes.

### Varejo e comércio eletrônico

- **Promoções sazonais:** Importe coleções de produtos sazonais e personalize mensagens para refletir as tendências atuais.
- **Mensagens localizadas:** Importe os endereços, horários e serviços do seu local físico e, em seguida, personalize as notificações com base nos locais dos usuários.
- **Notificações de falta de estoque:** Importe informações do produto que incluam a quantidade em estoque e, em seguida, use [as notificações de estoque em espera]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/) e os eventos personalizados do Braze para acionar uma campanha ou um Canvas que envie aos usuários uma notificação de que um produto está em estoque.
- **Notificações de queda de preço:** Importe informações de produtos que incluam preços de produtos e, em seguida, use [notificações de queda de preço]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/) e eventos personalizados do Braze para acionar um Canvas que envia aos usuários uma notificação de que o preço de um produto caiu.

### Entretenimento

- **Planos de assinatura:** Importe planos de assinatura e promova add-ons para seus usuários com base em seus padrões de uso e nos tipos de conteúdo que eles consomem com mais frequência.
- **Próximos eventos:** Importe listagens de eventos futuros, seus locais e idades do público e, em seguida, envie notificações personalizadas para usuários que estejam na área e tenham as idades desejadas.
- **Preferências de mídia:** Importe informações sobre filmes e programas e, em seguida, recomende conteúdo aos seus usuários com base nos títulos favoritos e nos gêneros mais assistidos.

### Viagens e hospitalidade

- **Destinos:** Importe destinos de viagem e suas atrações, restaurantes e atividades mais populares e, em seguida, personalize as recomendações para seus usuários com base em suas viagens anteriores.
- **Acomodações:** Importe propriedades de hotéis e suas comodidades, tipos de quartos e preços e, em seguida, envie promoções para seus usuários com base nas preferências selecionadas.
- **Métodos de viagem**: Importe ofertas e promoções para modos de viagem (como voos, trens, aluguel de carros e outros) e, em seguida, envie-as aos seus usuários com base no histórico de pesquisa recente deles.
- **Preferências de refeições:** Importe informações sobre ofertas de refeições e use [seleções]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) para enviar mensagens personalizadas a usuários que tenham preferências específicas de refeições com base na categoria de alimentos visualizada mais recentemente.

## Como os catálogos e o Liquid funcionam juntos

Os catálogos são um recurso de armazenamento de dados. Eles contêm grandes conjuntos de dados que podem ser referenciados em suas mensagens para personalização. Para realmente fazer referência aos dados, você usará [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) como linguagem de modelo. Em outras palavras, os catálogos são o armazenamento onde os dados são mantidos, e o Liquid é a linguagem que extrai os dados relevantes do armazenamento.

Para obter exemplos de como você pode usar o Liquid para extrair informações do catálogo, consulte os casos de uso adicionais em [Criação de um catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#additional-use-cases/).

#### Limitações de armazenamento de dados

O armazenamento de dados para catálogos é limitado com base no tamanho dos itens do catálogo, que pode ser diferente do tamanho dos arquivos CSV carregados.

Para a versão gratuita dos catálogos, a quantidade de armazenamento permitida é de até 100 MB. Você pode ter itens ilimitados, desde que o espaço de armazenamento não exceda 100 MB.

Para o Catalogs Pro, as opções de tamanho de armazenamento são: 5 GB, 10 GB, 15 GB ou 50 GB. Observe que o armazenamento da versão gratuita (100 MB) está incluído em cada um desses planos.
