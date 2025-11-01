---
nav_title: "Tutorial: Restaurante de serviço rápido"
article_title: Tutorial do Intelligence Suite
page_order: 10
search_rank: 12
description: "Novo na suíte de inteligência Braze? Comece com este tutorial."
tool:
  - Dashboard
---

# Tutorial do Intelligence Suite

> Novo no Braze Intelligence Suite? Comece com este tutorial! Para obter mais informações gerais, consulte [Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence/).

## Tutorial: Restaurante de serviço rápido

Vamos imaginar que trabalhamos no SandwichEmperor, um restaurante de fast food que tem um novo item de menu por tempo limitado: o Royal Roast. Usaremos dois recursos do Intelligence Suite para enviar promoções personalizadas em um Canvas.

### Etapa 1: Use o Intelligent Timing para saber quando enviar notificações

Usaremos o Intelligent Timing para analisar as interações anteriores de nossos usuários com nosso aplicativo e cada canal de mensagens e, em seguida, selecionaremos automaticamente o melhor momento para promover o Royal Roast para cada usuário. Alguns usuários podem receber a promoção à tarde, enquanto outros podem recebê-la à noite. 

Forneceremos um horário alternativo para usuários que não têm interações anteriores suficientes para analisar: o horário mais popular para usar o aplicativo entre todos os usuários.

Configurações de entrega do Intelligent Timing para uma etapa de Mensagem.]({% image_buster /assets/img/intelligence_suite1.png %})

### Etapa 2: Use a Seleção Inteligente para selecionar a promoção

Para as mensagens promocionais reais, usaremos o Intelligent Selection para testar três mensagens diferentes (notificação por push, e-mail e SMS) para o Royal Roast. A Intelligent Selection analisará o desempenho de todas as nossas mensagens promocionais duas vezes por dia e, em seguida, enviará gradualmente mais mensagens de melhor desempenho e menos mensagens de outras.

Depois que o Intelligent Selection reunir dados suficientes para determinar a mensagem com melhor desempenho, ele usará essa mensagem em 100% dos envios futuros.

Seção de teste A/B de um Canvas com a seleção inteligente ativada.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### Etapa 3: Iniciar o Canvas

Com o Intelligent Timing e o Intelligent Selection, configuramos nossas promoções do Royal Roast para serem otimizadas em termos de tempo e mensagens. Podemos lançar nosso Canvas e observar como nossos envios mudam para acomodar as preferências do usuário.
