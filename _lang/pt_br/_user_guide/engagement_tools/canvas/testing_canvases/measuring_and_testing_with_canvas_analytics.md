---
nav_title: Análise de dados do Canva
article_title: Análise de dados do Canva
page_order: 2
page_type: reference
description: "Este artigo de referência descreve as várias análises de dados e relatórios que você pode utilizar para entender a performance do seu Canva."
tool: 
  - Canvas
  - Reports
  
---

# Análise de dados do Canva

> É preciso saber se o que você está construindo está fazendo a diferença. Com a análise de dados do Canva, é possível criar um quadro completo para entender como as experiências que você está criando estão afetando suas metas. 

Depois de criar seu Canvas e colocá-lo no ar, navegue até a página **do Canvas** e selecione-o para abrir a página de detalhes. Aqui, você pode medir e testar a performance de seu Canva.

## Visão geral do Canva

A parte superior da página **Detalhes do Canvas** contém estatísticas de primeira linha do Canva. Isso inclui o número de mensagens enviadas dentro do Canvas, o número total de vezes que os clientes entraram no Canvas, quantos converteram e sua taxa total, a receita gerada pelo Canvas e o público total estimado. 

Esse é um ótimo lugar para obter uma visão geral de alto nível e verificar como está a performance do seu Canva em relação à sua meta.

![]({% image_buster /assets/img_archive/Journey_5.png %})

### alterações desde a última visualização

O número de atualizações no Canva feitas por outros membros da sua equipe é rastreado pela métrica *Alterações desde a última visualização* na página de visão geral do Canvas. Selecione **Alterações desde a última visualização** para ver um changelog de atualizações do nome do Canva, programação, tags, mensagem, público, status de aprovação ou configuração de acesso da equipe. Para cada atualização, você pode ver quem realizou a atualização e quando. Você pode usar esse changelog para auditar as alterações em suas Canvas.

## Visualização da performance

À medida que avança na página **Detalhes do Canvas**, é possível ver a performance de cada componente, como quantos usuários entraram, passaram para a próxima etapa ou saíram do Canvas. 

{% alert note %}
Para o Canvas Flow, um usuário sairá do Canvas depois de entrar e receber a carga útil da mensagem na última etapa da jornada do usuário.
{% endalert %}

As métricas também incluem impressões, destinatários únicos, contagem de conversões e receita gerada. Você pode clicar em um componente para detalhar melhor seus dados e ver a performance específica do canal.

![Dois exemplos de detalhes de performance para componentes do canva. À esquerda, são mostrados os detalhes de performance de uma jornada de usuário com um componente do canva. À direita, são mostrados os detalhes de performance de um componente Canva expandido e uma etapa aninhada que mostra a contagem de impressões de mensagens no app.]({% image_buster /assets/img_archive/Journey_6.png %})

## Detalhamento da performance por variante

Na parte inferior da página **Detalhes do Canvas**, clique em **Analisar Variantes** para abrir o modal **Analisar Canvas**. Esse modal contém três guias: 

- Analisar variantes
- Relatório de funil do canva
- Relatório de retenção do canva

### Analisar variantes

Na guia **Analyze Variants (Analisar variantes** ), é possível ver um detalhamento da performance por variante e grupo de controle, se houver mais de uma. Você também pode copiar o identificador da API do Canvas, baixar um arquivo CSV das métricas e copiar as células. A guia **Analyze Variants (Analisar variantes** ) contém uma tabela que mostra um detalhamento de cada variante em vários níveis. 

Você pode inferir rapidamente as variantes eficazes e identificar as cadências, o conteúdo, os disparos, o momento certos e muito mais.

![]({% image_buster /assets/img_archive/analyze_variants.png %})

As métricas básicas incluem o seguinte:  

- **Identificador da API de variantes:** O identificador de API de sua variante, que pode ser usado em suas chamadas de API.
- **Total de inscrições:** O número total de usuários que entraram na variante do Canva.
- **Total de envios:** O número total de mensagens enviadas na variante do Canva.
- **Total de etapas:** O número total de etapas na variante do Canva.
- **Receita total:** A receita total em dólares dos destinatários do Canvas dentro da janela de conversão primária definida.

{% alert note %}
Assim como as conversões, a receita é tecnicamente rastreada no nível da tela, mas é atribuída ao componente mais recente e à variante mais recente da qual o usuário recebeu uma mensagem (ou entrou, se ainda não tiver recebido uma mensagem).<br><br>
Por exemplo, se um usuário concluir duas etapas e depois fizer uma compra, essa receita será atribuída ao segundo componente e à variante inserida. Se ele entrar no canva, mas fizer uma compra antes de receber o primeiro componente do canva, essa receita será atribuída à variante em que ele entrou, mas não a nenhum componente.
{% endalert %}

Além disso, você pode ver um detalhamento mais explícito dos [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), incluindo o seguinte:

- Totais de conversão e taxas de conversão para cada evento de conversão
- Elevação em relação à variante de controle
- Confiança estatística para cada evento de conversão

### Relatório de funil

O relatório de funil oferece um relatório visual que permite analisar as jornadas que seus clientes fazem depois de receber um Canva. Se o seu Canva usar um grupo de controle ou várias variantes, você poderá entender como as diferentes variantes afetaram o funil de conversão em um nível mais granular e otimizar com base nesses dados. Para saber mais sobre relatórios de funil, consulte [Relatórios de funil]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

### Relatório de retenção

A retenção de usuários é uma das métricas mais importantes para qualquer profissional de marketing. Manter os usuários engajados voltando para comprar mais indica que os negócios estão saudáveis. O Braze agora permite que você meça a retenção de usuários diretamente na página de **análise de dados do Canva**. Para saber mais sobre como ler e interpretar seu relatório de retenção, consulte [Relatórios de retenção]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/).

