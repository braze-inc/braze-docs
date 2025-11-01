---
nav_title: Testes multivariados e A/B
article_title: Testes multivariados e A/B
page_order: 2
page_type: reference
description: "Este artigo de referência explica os testes multivariados e A/B e seus benefícios."
search_rank: 2
---

# Testes multivariados e A/B

> Esta página explica o que são testes multivariados e A/B e seus benefícios. Para obter etapas sobre como criar um teste multivariado ou A/B, consulte [Criação de testes multivariados e A/B com o Braze]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/). 

Testes multivariados e A/B podem ser usados com o [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

## O que são testes multivariados e A/B?

### Teste A/B

Um teste A/B é um experimento que compara as respostas dos usuários a várias versões da mesma campanha de marketing. Essas versões compartilham objetivos de marketing semelhantes, mas diferem em termos de redação e estilo.

O objetivo é identificar a versão da campanha que melhor atinja suas metas de marketing. Nesta seção, mostraremos como testar a eficácia das diferenças no conteúdo.

{% alert note %}
Se quiser avaliar diferenças no agendamento ou no tempo das mensagens (por exemplo, enviar uma mensagem de carrinho abandonado após uma hora de inatividade versus um dia de inatividade), consulte nossa seção sobre como [configurar um Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
{% endalert %}

Suponha que você tenha duas opções para uma notificação por push:

- "Esta oferta expira amanhã!"
- "Esta oferta expira em 24 horas!"

Usando um teste A/B, você pode ver qual texto resulta em uma taxa de conversão mais alta. Na próxima vez que enviar uma notificação push sobre uma oferta, você saberá qual tipo de texto é mais eficaz. No entanto, esse teste examina apenas o efeito de uma variável: a cópia na notificação push.

### Teste multivariado

Um teste multivariado é semelhante a um teste A/B, exceto pelo fato de que ele testa os efeitos de duas ou mais variáveis. Vamos voltar ao nosso exemplo de notificação por push. Outra variável que podemos querer testar é a inclusão ou não de um emoji no final da mensagem. Agora estaríamos testando duas variáveis (ou variantes - não confundir com variantes), daí o termo "multivariada". Para isso, precisaríamos testar quatro versões totais da mensagem - duas opções para o texto multiplicadas por duas opções para o emoji (presente ou não) equivalem a quatro variantes totais da mensagem.

Na documentação do Braze, "teste multivariado" é usado de forma intercambiável com "teste A/B", pois o processo de configuração é o mesmo.

## Benefícios dos testes multivariados e A/B {#the-benefits-of}

Os testes multivariados e A/B oferecem uma maneira fácil e clara de conhecer o seu público. Você não precisa mais adivinhar qual será a resposta dos usuários - cada campanha se torna uma oportunidade de experimentar diferentes variantes de uma mensagem e avaliar a resposta do público.

Os cenários específicos nos quais os testes multivariados e A/B podem ser úteis incluem:

- **Ao experimentar um tipo de mensagem pela primeira vez:** Preocupado em acertar nas mensagens no aplicativo logo na primeira vez? Os testes multivariados permitem que você faça experiências e saiba o que repercute nos seus usuários.
- **Ao criar campanhas de integração e outras campanhas que são enviadas constantemente:** Como a maioria dos seus usuários encontrará essa campanha, por que não garantir que ela seja a mais eficaz possível?
- **Quando você tem várias ideias de mensagens a serem enviadas:** Se você não tiver certeza de qual escolher, faça um teste e, em seguida, tome uma decisão baseada em dados.
- **Ao investigar se seus usuários respondem a técnicas de marketing "testadas e comprovadas":** Os profissionais de marketing geralmente usam táticas convencionais para interagir com os usuários, mas a base de usuários de cada produto é diferente. Às vezes, repetir sua frase de chamariz e usar a prova social não lhe trará os resultados desejados. Os testes multivariados e A/B permitem que você saia da caixa e descubra táticas não convencionais que funcionam para seu público específico.

### Distribuição de variantes

{% multi_lang_include multivariant_testing.md section='Variant distribution' %}

## Dicas para testes multivariados e A/B

Os testes multivariados e A/B podem revelar insights poderosos sobre seus usuários. Para obter resultados de testes que realmente reflitam o comportamento dos usuários, siga estas diretrizes.

#### Execute o teste em um grande número de usuários

Amostras grandes garantem que seus resultados reflitam as preferências do usuário médio e tenham menos probabilidade de serem influenciados por exceções. Amostragens maiores também permitem que você identifique as variantes vencedoras que têm margens menores de vitória.

#### Classifique aleatoriamente os usuários em diferentes grupos de teste

O teste multivariado permite que você crie até oito grupos de teste selecionados aleatoriamente. A randomização foi projetada para remover a tendência no conjunto de testes e aumentar as chances de os grupos de teste terem composição semelhante. Isso garante que as diferentes taxas de resposta se devam a diferenças em suas mensagens e não em suas amostras.

#### Saiba quais elementos você está tentando testar

Os testes multivariados e A/B permitem que você teste as diferenças entre várias versões de uma mensagem. Em alguns casos, um teste simples pode ser mais eficaz, pois o isolamento das alterações permite que você identifique quais elementos tiveram o maior impacto na resposta. Em outras ocasiões, a apresentação de mais diferenças entre as variantes permitirá que você examine os valores discrepantes e compare diferentes conjuntos de elementos. Nenhum dos métodos é necessariamente errado, desde que esteja claro desde o início o que você está tentando testar.

#### Decida por quanto tempo seu teste será executado e não o encerre antes do tempo

Antes de iniciar o teste, decida por quanto tempo ele será realizado e atenha-se a ele. Os profissionais de marketing muitas vezes são tentados a interromper os testes depois de verem resultados que lhes agradam, distorcendo suas descobertas. Resista à tentação de dar uma olhada e nunca termine seu teste antes do tempo!

#### Adicione seu teste às campanhas antes do lançamento, não depois

Se você adicionar seu teste a uma campanha depois de ela ter sido lançada, o teste não será executado corretamente e você poderá receber estatísticas incorretas ou enganosas. Por exemplo, se você adicionar um teste a uma campanha lançada que permita a reentrada, os usuários que entrarem novamente na campanha sempre passarão pelo mesmo caminho para evitar imprecisões de dados com o teste. Além disso, se você alterar qualquer uma das variantes enquanto o teste estiver em execução, a alteração invalidará o teste e o reiniciará.

Para obter resultados de teste precisos:
1. Clonar a campanha lançada.
2. Interromper a campanha original.
3. Em seguida, adicione o teste à campanha clonada. 

#### Se possível, inclua um grupo de controle

A inclusão de um [grupo de controle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#including-a-control-group) permite que você saiba se as suas mensagens têm um impacto maior na conversão do usuário do que o envio de nenhuma mensagem.


