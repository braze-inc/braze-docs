---
nav_title: Segmentos
article_title: Segmentos
page_order: 1
layout: dev_guide
guide_top_header: "Segmentos"
guide_top_text: "A segmentação do público-alvo é fundamental para o marketing estratégico - ela pode evitar que você segmente demais, incomode ou perca uma possível conexão com um cliente. Veja os artigos a seguir para saber como segmentar e filtrar seu público-alvo para seu maior benefício (e o dele)."
descriptions: "A segmentação do público-alvo é fundamental para o marketing estratégico - ela pode evitar que você segmente demais, incomode ou perca uma possível conexão com um cliente. Confira esta página de destino para saber como segmentar e filtrar seu público-alvo para seu maior benefício (e o dele)."
search_rank: 4
tool: Segments
page_type: landing
description: "Essa página de destino abrange artigos sobre segmentação em campanhas de painel. Aqui, você pode encontrar informações sobre como configurar um segmento, filtros, funis, insights, extensões e muito mais."

guide_featured_title: "Artigos populares"
guide_featured_list:
  - name: Criação de um segmento
    link: /docs/user_guide/engagement_tools/segments/creating_a_segment/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Gerenciamento de segmentos
    link: /docs/user_guide/engagement_tools/segments/managing_segments/
    image: /assets/img/braze_icons/edit-05.svg
  - name: Filtros de segmentação
    link: /docs/user_guide/engagement_tools/segments/segmentation_filters/
    image: /assets/img/braze_icons/flag-02.svg
  - name: Dados do segmento
    link: /docs/viewing_and_understanding_segment_data/
    image: /assets/img/braze_icons/pie-chart-01.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: Informações sobre o segmento
    link: /docs/user_guide/engagement_tools/segments/segment_insights/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Extensão do segmento
    link: /docs/user_guide/engagement_tools/segments/segment_extension/
    image: /assets/img/braze_icons/users-01.svg
  - name: Segmentos SQL
    link: /docs/sql_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: Segmentos do catálogo
    link: /docs/catalog_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: Perfis de usuário
    link: /docs/user_guide/engagement_tools/segments/user_profiles/
    image: /assets/img/braze_icons/users-01.svg
  - name: Segmentação por localização
    link: /docs/user_guide/engagement_tools/segments/location_targeting/
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: Expressões regulares
    link: /docs/user_guide/engagement_tools/segments/regex/
    image: /assets/img/braze_icons/search-sm.svg
  - name: Listas de supressão
    link: /docs/user_guide/engagement_tools/segments/suppression_lists/
    image: /assets/img/braze_icons/list.svg 
  - name: Medição do tamanho do segmento
    link: /docs/user_guide/engagement_tools/segments/measuring_segment_size/
    image: /assets/img/braze_icons/pie-chart-02.svg
  - name: Solução de problemas
    link: /docs/user_guide/engagement_tools/segments/troubleshooting/
    image: /assets/img/braze_icons/annotation-question.svg

guide_menu_title2: "Other"
guide_menu_list2:
  - name: Atributos personalizados
    link: /docs/user_guide/data/custom_data/custom_attributes/
    image: /assets/img/braze_icons/table.svg

---

## Sobre a Braze segments

No Braze, os segmentos são grupos dinâmicos de usuários que se encaixam em critérios específicos definidos por você, como atributos do usuário, comportamento do usuário e eventos personalizados. É possível obter critérios granulares aninhando segmentos dentro de outros segmentos e aplicando recursos adicionais, restringindo o escopo do seu público-alvo para que você possa enviar conteúdo altamente personalizado e envolvente para os usuários certos.

Você pode criar quantos segmentos quiser para segmentar os usuários. Explore diferentes combinações de recursos de segmento e filtros de segmentação para descobrir maneiras criativas de utilizar seus dados de usuário e desbloquear novas formas de enviar mensagens relevantes aos usuários e aumentar o envolvimento.

Confira os casos de uso abaixo para ter uma pequena amostra de como os segmentos Braze podem ajudá-lo a direcionar seus usuários.

### Casos de uso

- **Mensagens de boas-vindas:** Segmente novos usuários para que você possa enviar e-mails de integração ou mensagens no aplicativo que os apresentem ao seu aplicativo.
- **Prêmios de fidelidade:** Segmente os usuários com base na frequência de compras, aniversário da associação ou outros marcos e envie ofertas ou recompensas exclusivas para os usuários mais fiéis.
- **Acionadores comportamentais:** Segmente os usuários com base em suas ações, como o abandono de um carrinho no checkout, para acionar mensagens no aplicativo ou notificações push.
- **Recomendações de itens:** Segmente os usuários que compraram produtos específicos e envie-lhes recomendações de produtos complementares ou de nível superior.
- **Teste A/B:** Segmente os usuários para fazer testes A/B com diferentes mensagens, linhas de assunto ou conteúdo para determinar o que repercute melhor em usuários de idades, gêneros e outros atributos específicos.

#### Casos de uso de extensão de segmento

Você pode refinar ainda mais seus segmentos usando [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) para direcionar usuários com base em eventos personalizados ou comportamento de compra armazenado durante toda a vida útil do perfil do usuário.

- **Compras históricas:** Segmente os usuários de acordo com o fato de terem comprado uma cor específica de um produto específico pelo menos duas vezes nos últimos dois anos.
- **Eventos e interações de mensagens:** Segmente os usuários de acordo com o fato de terem feito uma compra nos últimos trinta dias e também interagido com uma mensagem específica no aplicativo.
- **Dados de consulta:** 
  - **Query Snowflake:** Segmente os usuários com dados combinados do Braze e de fontes externas, como um CRM ou um data warehouse, usando [as Extensões de Segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) para consultar o Snowflake.
  - **Sincronização do data warehouse:** Segmente os usuários com dados sincronizados diretamente do seu data warehouse ou sistema de armazenamento de arquivos para o Braze usando [as Extensões de Segmento CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

