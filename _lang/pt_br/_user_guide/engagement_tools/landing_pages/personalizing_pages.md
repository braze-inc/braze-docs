---
nav_title: Personalizar landing pages
article_title: Personalizar landing pages
description: "Este artigo aborda como personalizar landing pages do Braze com o editor de arrastar e soltar."
page_order: 4
---

# Personalizar landing pages

> Use a personalização Liquid em landing pages para adaptar dinamicamente o conteúdo com dados do perfil do usuário. Por exemplo, você pode personalizar títulos com base em diferentes atributos do usuário sem gerenciar várias landing pages estáticas.

{% alert important %}
A personalização Liquid para landing pages está disponível apenas no nível Pro das landing pages. Atualmente, [Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content), [multi-idioma]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings) e [códigos de promoção]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) não são suportados com a personalização Liquid em landing pages.
{% endalert %}

## Inserindo Liquid

No editor de arrastar e soltar, você pode inserir a personalização Liquid tanto no editor quanto nas configurações da página ou bloco no painel à direita. Para instruções sobre como implementar Liquid, confira nossa [documentação Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid-1) dedicada.

![Editor de landing page com personalização Liquid adicionada.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Visualizando e testando

Ao visualizar uma landing page no editor, você pode ver a página como um usuário aleatório, um usuário existente ou um usuário personalizado.

No entanto, ao visualizar a landing page a partir da tabela de dados ou da página **Detalhes da Landing Page**, você só poderá visualizá-la como um usuário aleatório.

## Considerações sobre personalização

Para manter um desempenho ideal com landing pages personalizadas, observe os seguintes limites de tamanho:

- **Salvando uma landing page:** Se o tamanho exceder 500 KB, você pode receber uma mensagem de aviso indicando que a página excedeu nossos limites de tamanho, o que pode impedir sua publicação.
- **Renderizando com personalização Liquid:** O tamanho total não deve exceder 1 MB. Caso contrário, a página pode ser automaticamente despublicada pelo Braze.

### Evite despublicar páginas de destino

Se sua página exceder esses limites de tamanho, você receberá um e-mail informando que ela pode ser despublicada se continuar a exceder o limite. Quando o limite for atingido, a página será automaticamente despublicada e você receberá uma notificação.

Para evitar que sua página exceda os limites de tamanho ou experimente tempos de carregamento lentos, certifique-se de usar a personalização Liquid que:

- Não faz loops contínuos ou referências a grandes conjuntos de dados.
- Não depende de lógica matemática ou condicional extensa dentro do bloco Liquid.

### Use Liquid para usuários identificados e anônimos 

Liquid pode personalizar a experiência da página de destino para visitantes identificados e anônimos.

- **Usuários identificados:** Link para a página de destino a partir de uma mensagem Braze e inclua a [tag Liquid da página de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users/#using-landing-page-liquid-tags). Isso associa o usuário ao seu perfil Braze e personaliza a experiência da página.
- **Visitantes anônimos:** Use Liquid para conteúdo contextual, não baseado em perfil, como um número aleatório ou uma saudação de acordo com a hora do dia.

## Páginas de fallback

Se seus usuários tentarem acessar uma página que foi despublicada, eles verão uma mensagem indicando que a página não pode ser carregada no momento. Razões pelas quais uma página foi despublicada incluem:

- Liquid complexo ou quebrado, que pode causar longos tempos de renderização
- Problemas de rede do usuário
- Excedendo os limites máximos de tamanho da página de destino
