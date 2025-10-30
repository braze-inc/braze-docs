---
nav_title: PERGUNTAS FREQUENTES
article_title: Perguntas frequentes sobre testes multivariados e A/B
page_order: 21
page_type: reference
toc_headers: h2
description: "Este artigo aborda as perguntas frequentes sobre testes multivariados e A/B com o Braze."
---

# Perguntas frequentes sobre testes multivariados e A/B

## Noções básicas de teste

### Qual é a diferença entre testes A/B e testes multivariados?

#### Teste A/B

No teste A/B, o profissional de marketing está fazendo experimentos com uma única variável dentro da campanha (como linhas de assunto de e-mail ou horário de envio da mensagem). Isso envolve a divisão aleatória de um subconjunto do público-alvo em dois ou mais grupos, apresentando a cada grupo uma variação diferente e observando qual variação apresenta a maior taxa de conversão. Normalmente, a variação com melhor desempenho é enviada posteriormente para o restante do público.

#### Testes multivariados 

O teste multivariado é uma extensão do teste A/B, que permite que o profissional de marketing teste diversas variáveis de uma só vez para determinar a combinação mais eficaz. Por exemplo, você pode testar a linha de assunto da sua mensagem de e-mail, a imagem que acompanha o texto e a cor do botão de CTA. Esse tipo de teste permite explorar mais variáveis e combinações de variações em um único experimento e obter insights de forma mais rápida e abrangente do que o teste A/B. No entanto, testar mais variáveis e combinações em um único experimento requer um público maior para produzir significância estatística.

### Como os resultados dos testes A/B são calculados?

O Braze testa todas as variantes umas contra as outras com os testes de qui-quadrado de Pearson, que medem se uma variante supera estatisticamente todas as outras em um nível de significância de p < 0,05, ou o que chamamos de significância de 95%. Em todas as variantes que excedem esse limite de significância, a variante com melhor desempenho é determinada como a "vencedora".

Esse é um teste separado da pontuação de confiança, que descreve apenas o desempenho de uma variante em comparação com o controle com um valor numérico entre 0 e 100%. Especificamente, ele representa nossa confiança de que a diferença padronizada na taxa de conversão entre a variante e o controle é significativamente maior do que o acaso.

### Por que a distribuição de variantes não é uniforme?

{% multi_lang_include multivariant_testing.md section='Variant distribution' %}

## Execução e conclusão de testes

### Quando o teste inicial termina?

Ao usar a Variante vencedora para campanhas de envio único, o teste termina quando chega a hora de envio da Variante vencedora. O Braze considerará uma variante como vencedora se ela apresentar a maior taxa de conversão por uma margem estatisticamente significativa.

Para campanhas recorrentes, baseadas em ações e acionadas por API, você pode usar o Intelligent Selection para rastrear continuamente os dados de desempenho de cada variante e otimizar continuamente o tráfego da campanha para as variantes de melhor desempenho. Com o Intelligent Selection, em vez de definir explicitamente um grupo de experimentos em que os usuários recebem variantes aleatórias, o algoritmo do Braze refina continuamente sua estimativa da variante de melhor desempenho, o que pode permitir uma seleção mais rápida do melhor desempenho.

### Como o Braze lida com os usuários que receberam uma variante de mensagem em uma campanha recorrente ou em uma etapa de entrada do Canvas? 

Os usuários são atribuídos aleatoriamente a uma variante específica antes de receber a campanha pela primeira vez. Cada vez que a campanha for recebida (ou o usuário entrar novamente em uma variante do Canvas), ele receberá a mesma variante, a menos que as porcentagens da variante sejam modificadas. Se as porcentagens de variantes mudarem, os usuários poderão ser redistribuídos para outras variantes. Os usuários permanecem nessas variantes até que as porcentagens sejam modificadas novamente. Os usuários só serão redistribuídos para as variantes que foram editadas.

Por exemplo, digamos que temos uma campanha ou um Canvas com três variantes. Se apenas a Variante A e a Variante B forem alteradas ou atualizadas, os usuários da Variante C não serão redistribuídos porque a porcentagem da variante da Variante C não foi alterada. Os grupos de controle permanecem consistentes se a porcentagem da variante não for alterada. Os usuários que receberam mensagens anteriormente não podem entrar no grupo de controle em um envio posterior, nem qualquer usuário do grupo de controle pode receber uma mensagem.

#### E quanto aos caminhos de experimentos?

O mesmo se aplica porque os caminhos do Canvas após um experimento também são variantes.

#### Posso realizar ações para redistribuir usuários em campanhas e Canvases?

A única maneira de redistribuir usuários em Canvases é usar [Randomized Paths em Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#step-1-choose-the-number-of-paths-and-audience-distribution), que sempre aleatorizará as atribuições de caminho quando os usuários entrarem novamente no Canvas. No entanto, esse não é um experimento padrão e pode invalidar os resultados do experimento, pois o grupo de controle pode ser contaminado pelos usuários do tratamento.

## Confiança e preconceito

### A confiança aumenta com o tempo?

A confiança aumenta com o tempo se tudo o mais se mantiver constante. Manter-se constante significa que não há outros fatores de marketing que possam influenciar as variantes, como a Variante A falando sobre uma venda com 25% de desconto que termina no meio do teste.

A confiança é uma medida de quão confiante o Braze está de que a variante é diferente do controle. À medida que mais mensagens são enviadas, o poder estatístico do teste aumenta, o que aumentaria a confiança de que as diferenças medidas no desempenho não se devem ao acaso. Em geral, um tamanho de amostra maior aumenta nossa confiança na identificação de diferenças menores no desempenho entre as variantes e o controle.

### As atribuições de grupos de controle e de teste podem introduzir tendências nos testes?

Não há nenhuma maneira prática de que os atributos ou comportamentos de um usuário antes da criação de uma determinada campanha ou Canvas possam variar sistematicamente entre as variantes e o controle. 

Para atribuir usuários a variantes de mensagens, variantes do Canvas ou seus respectivos grupos de controle, começamos vinculando a ID de usuário gerada aleatoriamente à ID da campanha ou do Canvas gerada aleatoriamente. Em seguida, aplicamos um algoritmo de hash sha256, dividimos o resultado por 100 e mantemos o restante (também conhecido como módulo com 100). Por fim, ordenamos os usuários em fatias que correspondem às atribuições de porcentagem para variantes (e controle opcional) escolhidas no painel.

### Por que não posso usar a limitação de taxa com um grupo de controle?

Atualmente, o Braze não oferece suporte à limitação de taxa com testes A/B que tenham um grupo de controle. Isso ocorre porque a limitação da taxa não se aplica ao grupo de controle da mesma forma que as variantes, introduzindo assim um viés. Em vez disso, considere usar o [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), que ajusta automaticamente a porcentagem de usuários que receberão cada variante com base em análises e no desempenho da campanha.
