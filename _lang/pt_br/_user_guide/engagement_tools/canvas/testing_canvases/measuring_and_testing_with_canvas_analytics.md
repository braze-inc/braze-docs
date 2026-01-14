---
nav_title: Análise do Canvas
article_title: Análise do Canvas
page_order: 2
page_type: reference
description: "Este artigo de referência descreve as várias análises e relatórios que você pode utilizar para entender o desempenho do seu Canvas."
tool: 
  - Canvas
  - Reports
  
---

# Análise do Canvas

> É preciso saber se o que você está construindo está fazendo a diferença. Com a análise do Canvas, você pode criar um quadro completo para entender como as experiências que você está criando estão afetando suas metas. 

Depois de criar seu Canvas e colocá-lo no ar, navegue até a página **do Canvas** e selecione-o para abrir a página de detalhes. Aqui, você pode medir e testar o desempenho do seu Canvas.

## Visão geral do Canvas

A parte superior da página **Detalhes do Canvas** contém estatísticas de primeira linha do Canvas. Isso inclui o número de mensagens enviadas no Canvas, o número total de vezes que os clientes entraram no Canvas, quantos converteram e sua taxa total, a receita gerada pelo Canvas e o público total estimado. 

Esse é um ótimo lugar para obter uma visão geral de alto nível e verificar como está o desempenho do seu Canvas em relação à sua meta.

\![]({% image_buster /assets/img_archive/Journey_5.png %})

### Alterações desde a última visualização

O número de atualizações no Canvas feitas por outros membros da sua equipe é monitorado pela métrica *Alterações desde a última visualização* na página de visão geral do Canvas. Selecione **Changes Since Last Viewed (Alterações desde a última visualização** ) para ver um registro de alterações das atualizações do nome do Canvas, da agenda, das tags, da mensagem, do público, do status de aprovação ou da configuração de acesso da equipe. Para cada atualização, você pode ver quem realizou a atualização e quando. Você pode usar esse registro de alterações para auditar as alterações em seus Canvases.

## Visualização de desempenho

À medida que avança na página **Detalhes do Canvas**, você pode ver o desempenho de cada componente, como quantos usuários entraram, passaram para a próxima etapa ou saíram do Canvas. 

{% alert note %}
Para o Canvas Flow, um usuário sairá do Canvas depois de entrar e receber a carga útil da mensagem na última etapa da jornada do usuário.
{% endalert %}

As métricas também incluem impressões, destinatários exclusivos, contagem de conversões e receita gerada. Você pode clicar em um componente para detalhar melhor seus dados e ver o desempenho específico do canal.

\![Dois exemplos de detalhes de desempenho para componentes do Canvas. À esquerda, são mostrados os detalhes de desempenho de um caminho de usuário com um componente Canvas. À direita, são mostrados os detalhes de desempenho de um componente Canvas expandido e uma etapa aninhada que mostra a contagem de impressões de mensagens in-app.]({% image_buster /assets/img_archive/Journey_6.png %})

## Detalhamento do desempenho por variante

Na parte inferior da página **Detalhes do Canvas**, clique em **Analisar Variantes** para abrir o modal **Analisar Canvas**. Esse modal contém três guias: 

- Analisar variantes
- Relatório de funil do Canvas
- Relatório de retenção do Canvas

### Analisar variantes

Na guia **Analyze Variants (Analisar variantes** ), é possível ver um detalhamento do desempenho por variante e grupo de controle, se houver mais de uma. Você também pode copiar o identificador da API do Canvas, fazer download de um arquivo CSV das métricas e copiar as células. A guia **Analyze Variants (Analisar variantes** ) contém uma tabela que mostra um detalhamento de cada variante em vários níveis. 

Você pode inferir rapidamente as variantes eficazes e identificar as cadências, o conteúdo, os acionadores, o momento certos e muito mais.

\![]({% image_buster /assets/img_archive/analyze_variants.png %})

As métricas básicas incluem o seguinte:  

- **Identificador de API de variantes:** O identificador de API de sua variante, que pode ser usado em suas chamadas de API.
- **Total de inscrições:** O número total de usuários que entraram na variante do Canvas.
- **Total de envios:** O número total de mensagens enviadas na variante do Canvas.
- **Total de etapas:** O número total de etapas na variante do Canvas.
- **Receita total:** A receita total em dólares dos destinatários do Canvas dentro da janela de conversão primária definida.

{% alert note %}
Assim como as conversões, a receita é tecnicamente rastreada no nível do Canvas, mas é atribuída ao componente mais recente e à variante mais recente da qual o usuário recebeu uma mensagem (ou entrou, se ainda não tiver recebido uma mensagem).<br><br>
Por exemplo, se um usuário concluir duas etapas e depois fizer uma compra, essa receita será atribuída ao segundo componente e à variante inserida. Se eles entrarem no Canvas, mas fizerem uma compra antes de receberem o primeiro componente do Canvas, essa receita será atribuída à variante em que entraram, mas não a nenhum componente.
{% endalert %}

Além disso, você pode ver um detalhamento mais explícito dos [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), incluindo o seguinte:

- Totais de conversão e taxas de conversão para cada evento de conversão
- Elevação em relação à variante de controle
- Confiança estatística para cada evento de conversão

### Como as conversões são rastreadas 

Um usuário só pode converter uma vez por evento de conversão e por entrada no Canvas. As conversões são atribuídas à mensagem mais recente recebida pelo usuário para essa entrada. O resumo do Canvas reflete todas as conversões realizadas pelos usuários nesse caminho e se eles receberam ou não uma mensagem. Cada etapa subsequente mostrará apenas as conversões que ocorreram enquanto essa foi a etapa mais recente que o usuário recebeu. 

Considere o seguinte exemplo: um Canvas tem 10 notificações por push e o evento de conversão é "Abre o aplicativo" (ou "Início da sessão").
- O usuário A abre o aplicativo depois de entrar, mas antes de receber a primeira mensagem.
- O usuário B abre o aplicativo após cada notificação push.

O resumo do Canvas mostrará duas conversões, enquanto as etapas individuais mostrarão uma conversão na primeira etapa e nenhuma em todas as etapas subsequentes. Se o Quiet Hours estiver ativo quando o evento de conversão ocorrer, as mesmas regras serão aplicadas. 

Agora, digamos que temos um Canvas com Quiet Hours e os seguintes eventos ocorrem:

1. O usuário A entra em um Canvas.
2. A primeira etapa é uma etapa de atraso dentro das horas de silêncio definidas, de modo que a mensagem é suprimida.
3. O usuário A realiza o evento de conversão.

O usuário A será contado como convertido na variante geral do Canvas, mas não na etapa, pois não recebeu a etapa.

Para nosso último exemplo, digamos que temos um Canvas com a reelegibilidade ativada. Se um usuário reelegível realizar o evento de conversão na primeira e na segunda entrada, serão contadas duas conversões.

### Relatório de funil

O relatório de funil oferece um relatório visual que permite que você analise as jornadas que seus clientes fazem depois de receber um Canvas. Se o seu Canvas usar um grupo de controle ou várias variantes, você poderá entender como as diferentes variantes afetaram o funil de conversão em um nível mais granular e otimizar com base nesses dados. Para obter mais informações sobre relatórios de funil, consulte [Relatórios de funil]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

### Relatório de retenção

A retenção de usuários é uma das métricas mais importantes para qualquer profissional de marketing. Manter os usuários engajados voltando para mais indica que os negócios estão saudáveis. O Braze agora permite que você meça a retenção de usuários diretamente na página **do Canvas Analytics**. Para obter mais informações sobre como ler e interpretar seu relatório de retenção, consulte [Relatórios de retenção]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/).

