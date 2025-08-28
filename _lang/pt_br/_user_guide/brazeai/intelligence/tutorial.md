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

> Novo no Braze Intelligence Suite? Comece com este tutorial! Para saber mais sobre informações gerais, consulte [Intelligence Suite]({{site.baseurl}}/user_guide/brazeai/intelligence/).

## Tutorial: Restaurante de serviço rápido

Vamos imaginar que trabalhamos no SandwichEmperor, um restaurante de fast food que tem um novo item de menu por tempo limitado: o Royal Roast. Usaremos dois recursos do Intelligence Suite para enviar promoções personalizadas em um canva.

### Etapa 1: Use o Intelligent Timing para saber quando enviar notificações

Usaremos o Intelligent Timing para analisar as interações anteriores de nossos usuários com nosso app e cada canal de envio de mensagens e, em seguida, selecionaremos automaticamente o melhor momento para promover o Royal Roast para cada usuário. Alguns usuários podem receber a promoção à tarde, enquanto outros podem recebê-la à noite. 

Forneceremos um tempo de fallback para usuários que não têm interações anteriores suficientes para analisar: o tempo mais popular para usar o app entre todos os usuários.

![Configurações de envio de mensagens do Intelligent Timing para uma etapa de Mensagem.]({% image_buster /assets/img/intelligence_suite1.png %})

### Etapa 2: Use a Seleção Inteligente para selecionar a promoção

Para as mensagens promocionais reais, usaremos o Intelligent Selection para testar três mensagens diferentes (notificação por push, envio de e-mail e SMS) para o Royal Roast. A Intelligent Selection analisará a performance de todas as nossas mensagens promocionais duas vezes por dia e, em seguida, enviará gradualmente mais mensagens de melhor performance e menos mensagens de outras.

Depois que a Seleção Inteligente reunir dados suficientes para determinar a mensagem de melhor performance, ele usará essa mensagem em 100% dos envios futuros.

![Seção Testes A/B de um Canva com a Seleção Inteligente ativada.]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

### Etapa 3: Iniciar o Canva

Com o Intelligent Timing e a Seleção Inteligente, configuramos nossas promoções Royal Roast para serem otimizadas em termos de tempo e envio de mensagens. Podemos lançar nosso canva e observar como nossos envios mudam para acomodar as preferências do usuário.
