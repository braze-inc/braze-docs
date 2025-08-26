---
nav_title: Lógica de segmentação
article_title: Lógica de segmentação 
page_order: 3

page_type: solution
description: "Este artigo de ajuda o orienta sobre as diferenças entre os operadores AND e OR e como você pode usá-los para criar segmentos poderosos."
tool: Segments
---

# Lógica de segmentação 

Os operadores `AND` e `OR` ativam uma filtragem poderosa ao [criar um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/). Usando esses operadores, é possível direcionar seus usuários com base em suas ações ou comportamentos na etapa **Target Audience (Público-alvo)** da criação de suas campanhas ou Canvas.

## Compreensão dos operadores AND e OR

Os operadores `AND` e `OR` funcionam de maneiras diferentes. Você pode usar cada operador dependendo do que deseja alcançar ao segmentar seu público. 

### Quando usar o operador AND

Em geral, use `AND` se tiver interesse na interseção de dois ou mais valores para uma atribuição específica.

Vamos considerar como fazer o direcionamento de usuários em uma campanha de todos os países, exceto Canadá e Estados Unidos. Nesse caso, o uso do operador `AND` pode ajudar a filtrar esses usuários. A declaração `Country is not United States AND Country is not Canada` incluirá apenas usuários que não sejam dos Estados Unidos e do Canadá. Portanto, usando essa lógica, tanto os usuários do Canadá quanto os dos Estados Unidos serão excluídos.

### Quando usar o operador OR

Use `OR` se o seu objetivo for direcionar usuários que atendam a pelo menos uma condição em um conjunto de condições. Se você tiver três condições vinculadas por `OR`, então uma, duas ou todas as condições podem ser verdadeiras para que a afirmação seja verdadeira.

Por exemplo, imagine que você queira enviar uma mensagem para todos os seus usuários na versão 1.0 ou 1.1 do seu app. Para direcionar os usuários que estão na versão 1.0 e na versão 1.1, você pode usar os filtros `Is 1.0` e `Is 1.1` com o operador `OR` em seu segmento. Isso direcionará todos os usuários que estão nas versões 1.0 ou 1.1.

No próximo exemplo, considere uma promoção válida para usuários dos Estados Unidos e do Canadá. Quer mesmo ter certeza de que apenas os usuários em áreas onde a promoção é válida recebam a promoção. Nesse cenário, use a seguinte declaração para direcionar sua campanha: `Country is United States OR Country is Canada`. Com a operadora `OR`, sua campanha seria direcionada apenas aos usuários cujo país é o Canadá ou cujo país é os Estados Unidos.

#### Quando evitar o operador OR

Pode haver situações de direcionamento de usuários em que o uso do operador `OR` deve ser evitado. O operador `OR` cria uma declaração que é avaliada como verdadeira se um usuário atender aos critérios de um ou mais filtros em uma declaração. Por exemplo, se você quiser criar um segmento de usuários que pertençam a "foodies", mas não pertençam a "non-foodies" ou "candy-lovers", o operador `OR` funcionaria aqui.

![]({% image_buster /assets/img_archive/or_operator_segment.png %})

No entanto, se o seu objetivo for segmentar os usuários que pertencem ao segmento "foodies" e não estão em nenhum dos segmentos "non-foodies" e "candy-lovers", use o operador `AND`. Dessa forma, os usuários que recebem a campanha ou o Canva estão no segmento pretendido ("foodies") e não nos outros segmentos ("non-foodies" e "candy-lovers") ao mesmo tempo. 

Os seguintes critérios de direcionamento negativo não devem ser usados com o operador `OR` quando dois ou mais filtros estiverem fazendo referência ao mesmo atributo:

- `is not`
- `does not equal`
- `does not match regex`

Se `is not`, `does not equal`, ou `does not match regex` forem usados com o operador `OR` duas ou mais vezes em uma declaração, os usuários com todos os valores para a atribuição relevante serão direcionados.

### Usando ambos os operadores

No próximo exemplo, usaremos os operadores `AND` e `OR`. Aqui, o público-alvo inclui usuários que compraram tênis Nike ou Adidas e aceitaram receber notificações por e-mail.

![Criação de um segmento para compradores de tênis em que a marca favorita do usuário é Nike ou Adidas e ele aceitou o envio de e-mail]({% image_buster /assets/img_archive/NikeSneakers.png %})

Outra maneira de garantir que está construindo a lógica correta é criar seu segmento e fazer [uma prévia dos usuários]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/) que se enquadram nele com base em seus filtros. Dessa forma, você pode ter certeza de que as atribuições, a versão do app ou qualquer outra segmentação correspondem ao que você está vendo.

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

_Última atualização em 3 de junho de 2022_

