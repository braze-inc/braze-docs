---
nav_title: Números aleatórios de baldes
article_title: Números aleatórios de baldes
page_order: 2
page_type: reference
description: "Este artigo aborda o conceito de números aleatórios e como é possível usá-los para criar variantes e grupos de controle."
page_type: reference
tool:
  - Campaign
  - Canvas

---

# Números aleatórios de baldes

> Um número de bucket aleatório é uma atribuição do usuário que pode ser usada para criar segmentos uniformemente distribuídos de usuários aleatórios. Quando um perfil de usuário é criado no Braze, é atribuído automaticamente a esse usuário um número de bucket aleatório entre 0 e 9999 (inclusive). É possível usar esses segmentos para testar a eficácia de várias campanhas ou Canvas em grupos de usuários ao longo do tempo.

## Visão geral

Os números de bucket aleatórios são usados no seu Global Control Group (Grupo de controle global) - um grupo de usuários que não recebe nenhuma campanha ou Canvas. O Braze seleciona aleatoriamente vários intervalos de números de buckets aleatórios e inclui usuários desses buckets selecionados. 

Se você tiver um grupo de controle global configurado e quiser usar números aleatórios para outros casos de uso, consulte [Coisas a serem observadas]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for).

### Quando usar números de balde aleatórios

Se quiser realizar testes de longo prazo sobre a eficácia de várias campanhas ou Canvas ao longo do tempo, poderá usar números aleatórios para segmentar seus usuários.

### Quando usar outra coisa

Se quiser segmentar usuários para testes em uma única campanha ou em um único Canva, use [Testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) para campanhas. Para Canvas, você pode criar diferentes [variantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#adding-a-variant) para testes em nível de jornada ou usar [Caminhos Experimentais]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) para testes em nível de etapa.

## Crie segmentos usando números aleatórios de baldes

Ao [criar um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), adicione o filtro "Random Bucket #". Em seguida, especifique um número ou intervalo de números para incluir em seu segmento.

![Um filtro de segmento que é para números de balde aleatórios não superiores a "3000".]({% image_buster /assets/img_archive/random_buckets_filterexample.png %})

Talvez você queira usar esses tipos de segmentos se quiser executar um teste de três variantes diferentes e também incluir um grupo de controle. Considere o seguinte exemplo de plano para criar segmentos de tamanho igual para três variantes e um grupo de controle:

- Os números dos compartimentos de 0 a 2499 correspondem ao segmento de controle
- Os números de balde 2500 a 4999 correspondem ao segmento que receberá a variante 1
- Os números de balde 5000 a 7499 correspondem ao segmento que receberá a variante 2
- Os números de balde 7500 a 9999 correspondem ao segmento que receberá a variante 3

Dependendo do número de segmentos desejados e da distribuição de usuários em cada segmento, seu plano pode ser diferente.

Para cada um dos segmentos de números aleatórios, incluindo o grupo de controle, ative o [rastreamento da análise de dados]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/). Ao avaliar o sucesso das variantes em relação ao grupo de controle, é possível acessar a página de [eventos personalizados]({{site.baseurl}}/user_guide/data/export_braze_data/export_custom_event_data/) e visualizar a frequência com que cada segmento concluiu determinados eventos personalizados.

### Reentrada aleatória do público usando números de baldes aleatórios

O reingresso aleatório do público pode ser útil para [Testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing) ou direcionamento de grupos de usuários específicos em suas campanhas. Para realizar a reentrada aleatória do público com números de balde aleatórios, faça o seguinte:

1. [Crie seu segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).
2. Defina os compartimentos aleatórios. Em sua campanha ou no Canva, use o filtro de intervalo aleatório para dividir seu público em diferentes grupos. Por exemplo, você pode especificar exatamente dois grupos aleatórios para dividir seu público (50% dos usuários por grupo).
3. Na seção **Direcionamento do público-alvo** da sua campanha ou Canva, especifique as configurações do compartimento aleatório. Isso permite que o Braze atribua automaticamente os usuários aos compartimentos apropriados com base nas porcentagens definidas.
4. Configure a lógica que permite que os usuários entrem novamente no segmento. Por exemplo, você pode permitir que os usuários entrem novamente no segmento se não tiverem se engajado com um app por 15 dias.
5. Lance sua campanha e monitore a performance de cada pacote. É possível analisar métricas como taxas de engajamento e taxas de conversão para determinar a eficácia da reentrada aleatória do público no seu caso de uso.


