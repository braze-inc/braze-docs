---
nav_title: Números aleatórios de baldes
article_title: Números aleatórios de baldes
page_order: 2
page_type: reference
description: "Este artigo aborda o conceito de números aleatórios e como você pode usá-los para criar variantes e grupos de controle."
page_type: reference
tool:
  - Campaign
  - Canvas

---

# Números aleatórios de baldes

> Um número de bucket aleatório é um atributo de usuário que pode ser usado para criar segmentos uniformemente distribuídos de usuários aleatórios. 

## Visão geral

Quando um perfil de usuário é criado no Braze, esse usuário recebe automaticamente um número de bucket aleatório entre 0 e 9999 (inclusive). Você pode usar esses segmentos para testar a eficácia de várias campanhas ou Canvases em grupos de usuários ao longo do tempo.

### Uso do Grupo de Controle Global

Os números de bucket aleatórios são usados no seu Global Control Group - um grupo de usuários que não recebe nenhuma campanha ou Canvases. O Braze seleciona aleatoriamente vários intervalos de números de buckets aleatórios e inclui usuários desses buckets selecionados. Números de baldes aleatórios são atribuídos sem ponderação ou consideração de números alocados recentemente. 

{% alert note %}
Quando um usuário é excluído e recriado, ele recebe um número de bucket aleatório diferente, pois é considerado um novo usuário.
{% endalert %}

Se você tiver um Grupo de Controle Global configurado e quiser usar números aleatórios para outros casos de uso, consulte [Coisas a serem observadas]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for).

### Quando usar números de balde aleatórios

Se quiser realizar testes de longo prazo sobre a eficácia de várias campanhas ou Canvases ao longo do tempo, você poderá usar números aleatórios para segmentar seus usuários.

### Quando usar outra coisa

Se quiser segmentar usuários para testes em uma única campanha ou em um único Canvas, use [o teste A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) para campanhas. Para Canvases, você pode criar diferentes [variantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#adding-a-variant) para testes em nível de jornada ou usar [caminhos de experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) para testes em nível de etapa.

## Crie segmentos usando números aleatórios de baldes

Ao [criar um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), adicione o filtro "Random Bucket #". Em seguida, especifique um número ou intervalo de números para incluir em seu segmento.

\![Um filtro de segmento que é para números aleatórios de balde não mais que "3000".]({% image_buster /assets/img_archive/random_buckets_filterexample.png %})

Talvez você queira usar esses tipos de segmentos se quiser executar um teste de três variantes diferentes e também incluir um grupo de controle. Considere o seguinte exemplo de plano para criar segmentos de tamanho igual para três variantes e um grupo de controle:

- Os números dos compartimentos de 0 a 2499 correspondem ao segmento de controle
- Os números de balde 2500 a 4999 correspondem ao segmento que receberá a variante 1
- Os números de balde 5000 a 7499 correspondem ao segmento que receberá a variante 2
- Os números de balde 7500 a 9999 correspondem ao segmento que receberá a variante 3

Dependendo do número de segmentos desejados e da distribuição de usuários em cada segmento, seu plano pode ser diferente.

Para cada um de seus segmentos de números aleatórios, incluindo o grupo de controle, ative [o rastreamento analítico]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/). Ao avaliar o sucesso das variantes em relação ao grupo de controle, você pode acessar a página de [eventos personalizados]({{site.baseurl}}/user_guide/data/export_braze_data/export_custom_event_data/) e ver com que frequência cada segmento concluiu determinados eventos personalizados.

### Reentrada aleatória do público usando números de baldes aleatórios

A reentrada aleatória do público-alvo pode ser útil para [testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing) ou para segmentar grupos de usuários específicos em suas campanhas. Para realizar a reentrada aleatória do público com números de balde aleatórios, faça o seguinte:

1. [Crie seu segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).
2. Defina os compartimentos aleatórios. Em sua campanha ou Canvas, use o filtro de intervalo aleatório para dividir seu público-alvo em grupos diferentes. Por exemplo, você pode especificar exatamente dois compartimentos aleatórios para dividir seu público (50% dos usuários por compartimento).
3. Na seção **Target Audiences (Públicos-alvo** ) de sua campanha ou Canvas, especifique as configurações de bucket aleatório. Isso permite que o Braze atribua automaticamente os usuários aos compartimentos apropriados com base nas porcentagens definidas.
4. Configure a lógica que permite que os usuários entrem novamente no segmento. Por exemplo, você pode permitir que os usuários entrem novamente no segmento se não se envolverem com um aplicativo por 15 dias.
5. Lance sua campanha e monitore o desempenho de cada pacote. Você pode analisar métricas como taxas de engajamento e taxas de conversão para determinar a eficácia da reentrada aleatória do público-alvo em seu caso de uso.


