---
nav_title: Testes multivariantes e Testes A/B
article_title: Testes multivariantes e Testes A/B
page_order: 2
page_type: reference
description: "Este artigo de referência explica os Testes Multivariantes e A/B e seus benefícios."
search_rank: 2
---

# Testes multivariantes e A/B

> Esta página explica o que são testes multivariantes e Testes A/B e seus benefícios. Para obter etapas sobre como criar um teste multivariante ou A/B, consulte [Criação de testes multivariantes e A/B com o Braze]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/). 

Testes multivariantes e A/B podem ser usados com o [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

## O que são testes multivariantes e Testes A/B?

### Testes A/B

Um Testes A/B é um experimento que compara as respostas dos usuários a várias versões da mesma campanha de marketing. Essas versões compartilham objetivos de marketing semelhantes, mas diferem em termos de redação e estilo.

O objetivo é identificar a versão da campanha que melhor atinja suas metas de marketing. Nesta seção, mostraremos como testar a eficácia das diferenças no conteúdo.

{% alert note %}
Se quiser avaliar diferenças no agendamento ou no tempo das mensagens (por exemplo, enviar uma mensagem de carrinho abandonado após uma hora de inatividade versus um dia de inatividade), consulte nossa seção sobre [como configurar um Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
{% endalert %}

Suponha que você tenha duas opções para uma notificação por push:

- "Esta oferta expira amanhã!"
- "Esta oferta expira em 24 horas!"

Usando um teste A/B, você pode ver qual texto resulta em uma taxa de conversão mais alta. Na próxima vez que enviar uma notificação por push sobre uma oferta, você saberá qual tipo de texto é mais eficaz. No entanto, esse teste examina apenas o efeito de uma variável: a cópia na notificação por push.

### Teste multivariante

Um teste multivariante é semelhante a um teste A/B, exceto pelo fato de que ele testa os efeitos de duas ou mais variáveis. Vamos voltar ao nosso exemplo de notificação por push. Outra variável que podemos querer testar é a inclusão ou não de um emoji no final da mensagem. Agora estaríamos testando duas variáveis (ou variantes - não confundir com variantes), daí o termo "multivariante". Para isso, precisaríamos testar quatro versões totais da mensagem - duas opções para o texto multiplicadas por duas opções para o emoji (presente ou não) equivalem a quatro variantes totais da mensagem.

Na documentação do Braze, "teste multivariante" é usado de forma intercambiável com "teste A/B", pois o processo para configurá-los é o mesmo.

## Benefícios dos testes multivariantes e dos testes A/B {#the-benefits-of}

Os testes multivariantes e A/B oferecem uma maneira fácil e clara de conhecer seu público. Não é mais necessário adivinhar o que os usuários responderão - cada campanha se torna uma oportunidade de experimentar variantes diferentes de uma mensagem e avaliar a resposta do público.

Os cenários específicos nos quais os testes multivariantes e os Testes A/B podem ser úteis incluem

- **Ao experimentar um tipo de envio de mensagens pela primeira vez:** Preocupado em acertar no envio de mensagens no app logo na primeira vez? Os testes multivariantes permitem fazer experiências e saber o que repercute nos usuários.
- **Ao criar campanhas de integração e outras campanhas que são enviadas constantemente:** Como a maioria dos seus usuários encontrará essa campanha, por que não garantir que ela seja a mais eficaz possível?
- **Quando você tem várias ideias para o envio de mensagens:** Se você não tiver certeza de qual escolher, faça um teste e, em seguida, tome uma decisão baseada em dados.
- **Ao investigar se seus usuários respondem a técnicas de marketing "testadas e comprovadas":** Os profissionais de marketing geralmente aderem às táticas convencionais para engajamento com os usuários, mas a base de usuários de cada produto é diferente. Às vezes, repetir sua frase de chamariz e usar a prova social não lhe trará os resultados desejados. Os testes multivariantes e A/B permitem que você saia da caixa e descubra táticas não convencionais que funcionam para seu público específico.

### Distribuição de variantes

A distribuição entre as variantes nem sempre é uniforme. Veja como funciona a distribuição de variantes.

Toda vez que uma mensagem é enviada em uma campanha multivariante, o sistema seleciona independentemente uma opção aleatória de acordo com as porcentagens definidas e atribui uma variante com base no resultado. É como jogar uma moeda - anomalias são possíveis. Se você já jogou uma moeda 100 vezes, sabe que provavelmente não obterá uma divisão exata de 50-50 entre cara e coroa todas as vezes, mesmo que tenha apenas duas opções. Você pode obter 52 caras e 48 coroas.

Se você tiver várias variantes que deseja dividir igualmente, também precisará garantir que o número de variantes seja um múltiplo de 100. Caso contrário, algumas variantes terão uma porcentagem maior de usuários distribuídos para essa variante em comparação com outras. Por exemplo, se sua campanha tiver 7 variantes, não poderá haver uma distribuição uniforme de variantes, pois 7 não se divide igualmente por 100 como um número inteiro. Nesse caso, você teria 2 variantes de 15% e 5 variantes de 14%.

#### Nota sobre mensagens no app

Ao executar Testes A/B em mensagens no app, sua análise de dados pode parecer mostrar uma distribuição de variantes maior entre uma variante e outra, mesmo que elas tenham uma divisão percentual uniforme. Por exemplo, considere o seguinte gráfico de *Destinatários Únicos* para a Variante A e a Variante C.

![Gráfico de Unique Recipients para duas variantes com uma forma semelhante entre a Variante A e a Variante C, em que a Variante A tem uma contagem maior de Unique Recipients por dia]({% image_buster /assets/img/variant_distribution_iam.png %})

A Variante A tem uma contagem consistentemente maior de *Destinatários Únicos* do que a Variante C. Isso não se deve à distribuição de variantes, mas sim à forma como *os Destinatários Únicos* são calculados para mensagens no app. Para mensagens no app, *os destinatários únicos* são, na verdade, *impressões únicas*, que é o número total de pessoas que receberam e visualizaram a mensagem no app. Isso significa que, se um usuário não receber a mensagem por qualquer motivo ou decidir não visualizá-la, ele não será incluído na contagem de *destinatários únicos*, e a distribuição de variantes poderá parecer distorcida.

## Dicas para testes multivariantes e Testes A/B

Os testes multivariantes e A/B podem revelar insights poderosos sobre seus usuários. Para receber resultados de testes que reflitam verdadeiramente o comportamento dos seus usuários, siga estas diretrizes.

#### Execute o teste em um grande número de usuários

Amostras grandes garantem que seus resultados reflitam as preferências do usuário médio e tenham menos probabilidade de serem influenciados por exceções. Amostragens maiores também permitem que você identifique as variantes vencedoras que têm margens menores de vitória.

#### Classifique aleatoriamente os usuários em diferentes grupos de teste

Os testes multivariantes permitem que você crie até oito grupos de teste selecionados aleatoriamente. A randomização foi projetada para remover a tendência no conjunto de testes e aumentar as chances de os grupos de teste terem composição semelhante. Isso garante que as diferentes taxas de resposta se devam a diferenças em suas mensagens e não em suas amostras.

#### Saiba quais elementos você está tentando testar

Os testes multivariantes e A/B permitem que você teste as diferenças entre várias versões de uma mensagem. Em alguns casos, um teste simples pode ser mais eficaz, pois o isolamento das alterações permite que você identifique quais elementos tiveram o maior impacto na resposta. Em outras ocasiões, a apresentação de mais diferenças entre as variantes permitirá que você examine as exceções e compare diferentes conjuntos de elementos. Nenhum dos métodos é necessariamente errado, desde que esteja claro desde o início o que você está tentando testar.

#### Decida por quanto tempo seu teste será executado e não o encerre antes do tempo

Antes de iniciar o teste, decida por quanto tempo ele será realizado e atenha-se a ele. Os profissionais de marketing muitas vezes são tentados a interromper os testes depois de verem resultados que lhes agradam, distorcendo suas descobertas. Resista à tentação de dar uma olhada e nunca termine seu teste antes do tempo!

#### Adicione seu teste às campanhas antes de elas serem lançadas, não depois

Se você adicionar seu teste a uma campanha após ela ter sido lançada, o teste não funcionará corretamente e você pode receber estatísticas incorretas ou enganosas. Por exemplo, se você adicionar um teste a uma campanha lançada que permite reentrada, os usuários que reentram na campanha sempre passarão pela mesma jornada para evitar imprecisões nos dados com o teste. Além disso, se você alterar qualquer uma das variantes enquanto o teste estiver em execução, a alteração invalidará seu teste e o reiniciará.

Para resultados de teste precisos:
1. Clone a campanha lançada.
2. Pare a campanha original.
3. Então, adicione o teste à campanha clonada. 

#### Se possível, inclua um grupo de controle

A inclusão de um [grupo de controle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#including-a-control-group) permite saber se suas mensagens têm um impacto maior na conversão do usuário do que o envio de nenhuma mensagem.


