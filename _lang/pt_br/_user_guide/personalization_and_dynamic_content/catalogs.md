---
nav_title: Catálogos
article_title: Catálogos
page_order: 6
layout: dev_guide

guide_top_header: "Catálogos"
guide_top_text: "Os catálogos acessam dados de arquivos CSV importados e pontos de extremidade da API para enriquecer suas mensagens, de forma semelhante a como você acessaria atributos personalizados ou propriedades de eventos personalizados por meio do Liquid."

description: "Esta landing page contém catálogos. Use catálogos e conjuntos filtrados para aproveitar os dados de não usuários em suas campanhas do Braze para enviar mensagens personalizadas."

guide_featured_title: "Artigos de seção"
guide_featured_list:
- name: Criação de um catálogo
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/
  image: /assets/img/braze_icons/users-01.svg
- name: Uso de catálogos
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/
  image: /assets/img/braze_icons/users-01.svg
- name: Notificações de estoque em espera
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Notificações de queda de preço
  link: /docs/price_drop_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Seleções
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/selections/
  image: /assets/img/braze_icons/list.svg
- name: Endpoints da API de catálogos
  link: /docs/api/endpoints/catalogs/
  image: /assets/img/braze_icons/server-01.svg

guide_menu_title: "Other articles"
guide_menu_list:
- name: Blocos de produtos de arrastar e soltar
  link: /docs/dnd_product_blocks/
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## Casos de uso do catálogo

Você pode trazer qualquer tipo de dados para um catálogo. Normalmente, os dados são metadados sobre ofertas, como produtos, descontos, promoções, eventos e similares. Veja os casos de uso abaixo para obter alguns exemplos de como usar esses dados para direcionar os usuários com envios de mensagens altamente relevantes.

### Varejo e e-commerce

- **Promoções sazonais:** Importe coleções de produtos sazonais e personalize mensagens para refletir as tendências atuais.
- **Envio de mensagens localizadas:** Importe os endereços, horários e serviços do seu local físico e, em seguida, personalize as notificações com base nos locais dos usuários.
- **Notificações de falta de estoque:** Importe informações sobre o produto que incluam a quantidade em [estoque]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/) e, em seguida, use [notificações de estoque em espera]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/) e eventos personalizados do Braze para disparar uma campanha ou um Canva que envie aos usuários uma notificação de que um produto está agora em estoque.
- **Notificações de queda de preço:** Importe informações de produtos que incluam os preços dos produtos e, em seguida, use [as notificações de queda de preço]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications/) e os eventos personalizados do Braze para disparar um Canva que envia aos usuários uma notificação de que o preço de um produto caiu.

### entretenimento

- **Planos de inscrição:** Importe planos de inscrição e promova add-ons para seus usuários com base em seus padrões de uso e nos tipos de conteúdo que eles consomem com mais frequência.
- **Próximos eventos:** Importe listas de eventos futuros, seus locais e idades do público e, em seguida, envie notificações personalizadas para usuários que estejam na área e nas idades direcionadas.
- **Preferências de mídia:** Importe informações sobre filmes e programas e, em seguida, recomende conteúdo aos seus usuários com base nos títulos favoritos e nos gêneros mais assistidos.

### Viagens e hospitalidade

- **Destinos:** Importe destinos de viagem e suas atrações, restaurantes e atividades mais populares e, em seguida, personalize as recomendações para seus usuários com base em suas viagens anteriores.
- **Acomodações:** Importe propriedades de hotéis e suas comodidades, tipos de quartos e preços e, em seguida, envie promoções para seus usuários com base nas preferências selecionadas.
- **Métodos de viagem**: Importe ofertas e promoções para modos de viagem (como voos, trens, aluguel de carros e outros) e, em seguida, envie-as aos seus usuários com base no histórico de pesquisa recente deles.
- **Preferências de refeições:** Importação de informações sobre ofertas de refeições e uso de [seleções]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) para enviar mensagens personalizadas aos usuários que têm preferências específicas de refeições com base na categoria de alimentos visualizada mais recentemente.

## Como os catálogos e o Liquid funcionam juntos

Os catálogos são um recurso de armazenamento de dados. Eles contêm grandes conjuntos de dados que podem ser referenciados em suas mensagens para personalização. Para realmente fazer referência aos dados, você usará [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) como linguagem de modelo. Em outras palavras, os catálogos são o armazenamento onde os dados são mantidos, e Liquid é a linguagem que extrai os dados relevantes do armazenamento.

Para obter exemplos de como você pode usar o Liquid para extrair informações do catálogo, consulte os casos de uso adicionais em [Criação de um catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases/).

#### Limitações de armazenamento de dados

O armazenamento de dados para catálogos é limitado com base no tamanho dos itens e seleções do catálogo, que podem ser diferentes dos tamanhos dos arquivos CSV feitos upload.

Para a versão gratuita dos catálogos, a quantidade de armazenamento permitida é de até 100 MB. Você pode ter itens ilimitados, desde que o espaço de armazenamento não exceda 100 MB. As seleções contribuirão para seu armazenamento. Quanto mais complexa for uma seleção, mais espaço de armazenamento ela ocupará.

Para o Catalogs Pro, as opções de tamanho de armazenamento são: 5 GB, 10 GB, 15 GB ou 50 GB. Note que o armazenamento da versão gratuita (100 MB) está incluído em cada um desses planos.
