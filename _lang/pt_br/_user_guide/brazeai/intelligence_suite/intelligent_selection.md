---
nav_title: Intelligent Selection
article_title: Intelligent Selection
page_order: 1.0
description: "Este artigo descreve o Intelligent Selection, um recurso que analisa o desempenho de uma campanha ou Canvas recorrente duas vezes por dia e ajusta automaticamente a porcentagem de usuários que recebem cada variante de mensagem."
search_rank: 10
toc_headers: h2
---

# Intelligent Selection {#intelligent-selection}

> O Intelligent Selection é um recurso que analisa o desempenho de uma campanha ou Canvas recorrente duas vezes por dia e ajusta automaticamente a porcentagem de usuários que recebem cada variante de mensagem.

## Sobre o Intelligent Selection

Uma variante que parece ter melhor desempenho é enviada a mais usuários; variantes com pior desempenho são direcionadas a menos usuários. Cada ajuste é feito por um [algoritmo estatístico](https://en.wikipedia.org/wiki/Multi-armed_bandit) que garante que a Braze reaja a diferenças reais de desempenho, e não ao acaso.

![Área de teste A/B de uma campanha com Intelligent Selection ativado.]({% image_buster /assets/img/intelligent_selection1.png %})

O Intelligent Selection:

- revisa repetidamente os dados de desempenho e desloca o tráfego da campanha gradualmente em direção às variantes vencedoras;
- garante que mais usuários recebam sua melhor variante sem sacrificar a confiança estatística;
- descarta variantes com pior desempenho e identifica variantes de alto desempenho mais rápido que um [teste A/B tradicional]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/);
- testa com mais frequência e com mais confiança de que seus usuários verão sua melhor mensagem.

O Intelligent Selection funciona melhor para campanhas que enviam mais de uma vez. Para campanhas de envio único, recomendamos um [teste A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) tradicional.

## Pré-requisitos

Antes de adicionar o Intelligent Selection à sua campanha, verifique se:

- sua campanha é enviada em um cronograma recorrente (envios únicos não são suportados);
- há pelo menos duas variantes de mensagem;
- um evento de conversão está definido para medir o desempenho entre variantes;
- a janela de re-elegibilidade é de 24 horas ou mais (janelas mais curtas não são suportadas, pois afetariam a integridade da variante de controle).

Para um Canvas: o passo de mensagem inclui pelo menos duas variantes e pelo menos um evento de conversão.

Para etapas de adição a campanhas e Canvas, tempo de execução, distribuição de variantes e FAQ, consulte a versão completa deste artigo no índice à esquerda ou na ajuda do dashboard da Braze.
