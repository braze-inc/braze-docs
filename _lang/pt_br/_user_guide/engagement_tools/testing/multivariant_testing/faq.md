---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre testes multivariantes e Testes A/B
page_order: 21
page_type: reference
toc_headers: h2
description: "Este artigo aborda as perguntas frequentes sobre testes multivariantes e A/B com o Braze."
---

# Perguntas frequentes sobre testes multivariantes e A/B

## Noções básicas de teste

### Qual é a diferença entre os Testes A/B e os testes multivariantes?

#### Testes A/B

Nos Testes A/B, o profissional de marketing está experimentando uma única variável dentro da campanha (como linhas de assunto de e-mail ou horário de envio de mensagens). Isso envolve a divisão aleatória de um subconjunto do público em dois ou mais grupos, apresentando a cada grupo uma variação diferente e observando qual variação exibe a maior taxa de conversão. Normalmente, a variação com melhor performance é enviada posteriormente para o restante do público.

#### Testes multivariantes 

Os testes multivariantes são uma extensão dos Testes A/B, que permitem que o profissional de marketing teste várias variáveis de uma só vez para determinar a combinação mais eficaz. Por exemplo, você pode testar a linha de assunto de sua mensagem de e-mail, a imagem que acompanha o texto e a cor do botão de CTA. Esse tipo de teste permite explorar mais variáveis e combinações de variações em um único experimento e obter insights de forma mais rápida e abrangente do que os Testes A/B. No entanto, testar mais variáveis e combinações em um único experimento requer um público maior para produzir significância estatística.

### Como os resultados dos Testes A/B são calculados?

O Braze testa todas as variantes umas contra as outras com os testes de qui-quadrado de Pearson, que medem se uma variante supera estatisticamente todas as outras em um nível de significância de p < 0,05, ou o que chamamos de significância de 95%. Em todas as variantes que excedem esse limite de significância, a variante com melhor performance é determinada como a "vencedora".

Esse é um teste separado da pontuação de confiança, que descreve apenas a performance de uma variante em comparação com o controle com um valor numérico entre 0 e 100%. Especificamente, ele representa nossa confiança de que a diferença padronizada na taxa de conversão entre a variante e o controle é significativamente maior do que o acaso.

## Execução e conclusão de testes

### Quando o teste inicial termina?

Ao usar a Variante vencedora para campanhas de envio único, o teste termina quando chega a hora de envio da Variante vencedora. O Braze considerará uma variante como vencedora se ela apresentar a maior taxa de conversão por uma margem estatisticamente significativa.

Para campanhas recorrentes, baseadas em ações e disparadas por API, você pode usar o Intelligent Selection para rastrear continuamente os dados de performance de cada variante e otimizar continuamente o tráfego da campanha para as variantes de melhor performance. Com a Seleção Inteligente, em vez de definir explicitamente um grupo de experimentos em que os usuários recebem variantes aleatórias, o algoritmo do Braze refinará continuamente sua estimativa da variante de melhor performance, o que pode permitir uma seleção mais rápida da variante de melhor performance.

### Como o Braze lida com os usuários que receberam uma variante de mensagem em uma campanha recorrente ou etapa de entrada do Canva? 

Os usuários são atribuídos aleatoriamente a uma variante específica antes de receber a campanha pela primeira vez. Cada vez que a campanha for recebida (ou o usuário entrar novamente em uma variante do Canva), ele receberá a mesma variante, a menos que as porcentagens da variante sejam modificadas. Se as porcentagens de variantes mudarem, os usuários poderão ser redistribuídos para outras variantes. Os usuários permanecem nessas variantes até que as porcentagens sejam modificadas novamente. Os usuários só serão redistribuídos para as variantes que foram editadas.

Por exemplo, digamos que temos uma campanha ou um Canva com três variantes. Se apenas a Variante A e a Variante B forem alteradas ou atualizadas, os usuários da Variante C não serão redistribuídos porque a porcentagem da variante da Variante C não foi alterada. Os grupos de controle permanecem consistentes se a porcentagem da variante não for alterada. Os usuários que receberam mensagens anteriormente não podem entrar no grupo de controle em um envio posterior, nem qualquer usuário do grupo de controle pode receber uma mensagem.

#### E quanto às jornadas experimentais?

O mesmo se aplica porque as jornadas do canva após um experimento também são variantes.

#### Posso realizar ações para redistribuir usuários em campanhas e Canvas?

A única maneira de redistribuir usuários em Canvas é usar [Jornadas aleatórias em jornadas de experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#step-1-choose-the-number-of-paths-and-audience-distribution), que sempre atribuirá caminhos aleatórios quando os usuários entrarem novamente no Canvas. No entanto, esse não é um experimento padrão e pode invalidar os resultados do experimento, pois o grupo de controle pode ser contaminado pelos usuários do tratamento.

## Confiança e preconceito

### A confiança aumenta com o tempo?

A confiança aumenta com o tempo se tudo o mais se mantiver constante. Manter-se constante significa que não há outros fatores de marketing que possam influenciar as variantes, como a Variante A falando sobre uma venda com 25% de desconto que termina no meio do teste.

A confiança é uma medida do grau de confiança do Braze de que a variante é diferente do controle. À medida que mais mensagens são enviadas, o poder estatístico do teste aumenta, o que aumentaria a confiança de que as diferenças medidas no desempenho não se devem ao acaso. Geralmente, um tamanho de amostra maior aumenta nossa confiança na identificação de diferenças menores de performance entre variantes e controle.

### As atribuições do grupo de controle e do grupo de teste podem introduzir viés nos testes?

Não há nenhuma maneira prática de que as atribuições ou os comportamentos de um usuário antes da criação de uma determinada campanha ou Canva possam variar sistematicamente entre variantes e controle. 

Para atribuir usuários a variantes de mensagens, variantes do Canvas ou seus respectivos grupos de controle, começamos vinculando a ID de usuário gerada aleatoriamente à ID da campanha ou do Canvas gerada aleatoriamente. Em seguida, aplicamos um algoritmo de hash sha256, dividimos o resultado por 100 e mantemos o restante (também conhecido como módulo com 100). Por fim, ordenamos os usuários em fatias que correspondem às atribuições percentuais para variantes (e controle opcional) escolhidas no dashboard.

### Por que não posso usar o limite de frequência com um grupo de controle?

Atualmente, o Braze não oferece suporte a limites de frequência com Testes A/B que tenham um grupo de controle. Isso ocorre porque o limite de frequência não se aplica ao grupo de controle da mesma forma que as variantes, introduzindo assim um viés. Em vez disso, considere usar a [Seleção Inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), que ajusta automaticamente a porcentagem de usuários que receberão cada variante com base na análise de dados e na performance da campanha.
