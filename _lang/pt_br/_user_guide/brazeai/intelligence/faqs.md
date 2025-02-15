---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre inteligência
page_order: 191
description: "Este artigo fornece respostas a perguntas frequentes sobre o Canal Inteligente, a Seleção Inteligente e o Intelligent Timing."
---

# Perguntas frequentes

> Este artigo fornece respostas a perguntas frequentes sobre o Intelligence Suite.

## Seleção Inteligente

### Por que a reelegibilidade em menos de 24 horas não está disponível quando combinada com o Intelligent Selection?

Não permitimos que as campanhas da Seleção Inteligente sejam reelegíveis em um período muito curto, pois isso afetaria a integridade da variante de controle. Ao criar um intervalo de 24 horas, ajudamos a garantir que o algoritmo tenha um conjunto de dados estatisticamente válido para trabalhar.

Normalmente, as campanhas com reelegibilidade farão com que os usuários insiram novamente a mesma variante que receberam antes. Com a Seleção Inteligente, a Braze não pode garantir que um usuário receberá a mesma variante de campanha porque a distribuição de variantes teria mudado devido ao aspecto de alocação ideal para esse recurso. Se for permitido que o usuário entre novamente antes de a Intelligent Selection reexaminar a performance da variante, os dados de usuários que entraram novamente poderão ser distorcidos.

Por exemplo, se uma campanha estiver usando estas variantes:

- Variante A: 20%
- Variante B: 20%
- Controle: 60%

Então, a distribuição de variantes poderia ser a seguinte para a segunda rodada:

- Variante A: 15%
- Variante B: 25%
- Controle: 60%

### Por que minhas variantes do Intelligent Selection estão mostrando envios iguais durante os estágios iniciais da minha campanha?

O Intelligent Selection aloca variantes para envio com base no status atual da conversão da campanha. Ele só determina as alocações finais de variantes após um período de treinamento, em que os envios são feitos de forma homogênea entre as variantes. Se não quiser que a Seleção Inteligente envie uniformemente durante os estágios iniciais de sua campanha, use variantes fixas para um teste A/B tradicional.

### A Intelligent Selection deixará de otimizar sem escolher um vencedor claro?

A Seleção Inteligente interromperá a otimização quando tiver 95% de confiança de que a continuação do experimento não melhorará a taxa de conversão em mais de 1% da taxa atual.

### Por que não consigo ativar a Seleção Inteligente em minha canva ou campanha (acinzentado)?

O Intelligent Selection não estará disponível se:

- Você não adicionou eventos de conversão à sua campanha ou ao Canva
- Você está criando uma campanha de envio único
- Sua capacitação foi ativada com uma janela de menos de 24 horas
- Seu Canva é criado com uma única variante, sem variantes adicionais ou grupos de controle adicionados
- Seu Canva é composto por um único grupo de controle, sem variantes adicionadas

## Intelligent Timing

### O Intelligent Timing prevê quando é mais provável que um usuário converta, ou apenas quando é mais provável que ele abra ou clique?

O Intelligent Timing prevê quando é mais provável que um usuário abra ou clique.

### Como é determinado o tempo do app mais popular?

O horário mais popular do app é determinado pelo horário médio de início da sessão para o espaço de trabalho (no fuso local). Essa métrica pode ser encontrada no dashboard durante a prévia dos tempos de uma campanha, mostrada em vermelho.

### O Intelligent Timing leva em conta as aberturas de máquina?

Sim, as aberturas por máquina são filtradas pelo Intelligent Timing, de modo que não influenciam o resultado.

### Como posso garantir que o Intelligent Timing funcione da melhor forma possível?

O Intelligent Timing usa o histórico individual de engajamento com mensagens de cada usuário, independentemente do horário em que ele recebeu as mensagens. Antes de usar o Intelligent Timing, certifique-se de ter enviado mensagens aos usuários em diferentes momentos do dia. Dessa forma, você pode "experimentar" qual é o melhor momento para cada usuário. A amostragem inadequada de diferentes horários do dia pode fazer com que o Intelligent Timing escolha um horário de envio abaixo do ideal para um usuário. 

### Com quanto tempo de antecedência devo lançar uma campanha do Intelligent Timing para entregá-la com sucesso a todos os usuários em todos os fusos horários?

A Braze calcula o horário ideal à meia-noite no horário de Samoa, um dos primeiros fusos horários do mundo. Em um único dia, ele se estende por aproximadamente 48 horas. Por exemplo, uma pessoa cujo horário ideal é 12h01 e que mora na Austrália já teve seu horário ideal ultrapassado e é "tarde demais" para enviar para ela. Por esses motivos, você precisa agendar com 48 horas de antecedência para garantir que todos no mundo que usam seu app o recebam com sucesso.

### Por que minha campanha Intelligent Timing está mostrando pouco ou nenhum envio?

A Braze precisa de um número básico de pontos de dados para fazer uma boa estimativa. Se não houver dados de sessão suficientes ou se os usuários direcionados tiverem poucos ou nenhum clique ou abertura de e-mail (como novos usuários), o Intelligent Timing poderá usar como padrão a hora mais popular do espaço de trabalho naquele dia da semana. Se não houver informações suficientes sobre o espaço de trabalho, voltaremos ao horário padrão de 17 horas. Você também pode optar por definir um [tempo de fallback]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options) específico.

### Por que minha campanha do Intelligent Timing está sendo enviada após a data programada?

Sua campanha Intelligent Timing pode estar sendo enviada após a data programada porque você está usando testes A/B. As campanhas que usam Testes A/B podem enviar automaticamente a variante vencedora após o término do teste A/B, aumentando a duração do envio da campanha. Por padrão, as campanhas do Intelligent Timing serão programadas para enviar a Variante Vencedora para os usuários restantes no dia seguinte, mas você pode alterar essa data de envio.

Recomendamos que, se você tiver campanhas Intelligent Timing, deixe mais tempo para o teste A/B terminar e programe a variante vencedora para ser enviada em dois dias, em vez de um. 

### Quando a Braze verifica os critérios de elegibilidade para os filtros de segmento e público?

A Braze realiza duas verificações quando uma campanha é lançada:

1. Assim que o primeiro fuso horário for identificado, iniciar o processo de enfileiramento de usuários e
2. No horário programado para ver se os usuários ainda são elegíveis para receber a campanha.

Tenha cuidado ao criar campanhas que filtram os envios de outras campanhas. Por exemplo, se você enviar duas campanhas no mesmo dia, em horários diferentes, e adicionar um filtro que só permita que os usuários recebam a segunda campanha se tiverem recebido a primeira, os usuários não receberão a segunda campanha. Isso se deve ao fato de que ninguém era elegível quando a campanha foi criada pela primeira vez e os segmentos foram formados.

### Posso usar o horário de silêncio em minha campanha Intelligent Timing?

Não recomendamos o uso do Intelligent Timing e do horário de silêncio em sua campanha ou no canva, pois isso é contraproducente. O Horário de silêncio é baseado em suposições de cima para baixo sobre o comportamento do usuário, enquanto o Intelligent Timing é baseado na atividade do usuário.

### Posso usar o Intelligent Timing e o limite de frequência?

A Braze não recomenda o uso do Intelligent Timing e do limite de frequência porque não há garantia de quando a mensagem será entregue.

### Posso usar o Intelligent Timing durante o aquecimento de IP?

A Braze não recomenda o uso do Intelligent Timing quando os usuários estão fazendo o aquecimento de IP pela primeira vez, pois alguns de seus comportamentos podem causar dificuldades para atingir os volumes diários. Isso é causado pelo fato de o Intelligent Timing avaliar os segmentos de campanha duas vezes. Uma vez, quando a campanha é criada pela primeira vez, e uma segunda vez antes de enviar aos usuários para verificar se eles ainda devem estar nesse segmento. 

Isso pode fazer com que os segmentos se desloquem e mudem, muitas vezes fazendo com que alguns usuários saiam do segmento na segunda avaliação. Esses usuários não são substituídos, o que afeta a proximidade do limite máximo de usuários que você pode atingir.
