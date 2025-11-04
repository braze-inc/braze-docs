---
nav_title: Personalização de páginas de destino
article_title: Personalização de páginas de destino
description: "Este artigo aborda como personalizar as páginas de destino do Braze com o editor de arrastar e soltar."
page_order: 4
---

# Personalização de páginas de destino

> Use a personalização Liquid nas páginas de destino para adaptar dinamicamente o conteúdo com os dados do perfil do usuário. Por exemplo, é possível personalizar os títulos com base em diferentes atributos do usuário sem gerenciar várias páginas de destino estáticas.

{% alert important %}
A personalização líquida para páginas de destino só está disponível no nível Pro de páginas de destino. Atualmente, [o Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) e [os códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) não são compatíveis com a personalização do Liquid nas páginas de destino.
{% endalert %}

## Inserção de líquido

No editor de arrastar e soltar, você pode inserir a personalização do Liquid no editor e nas configurações da página ou do bloco no painel à direita. Para obter instruções sobre a implementação do Liquid, consulte nossa [documentação]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid-1) dedicada ao [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid-1).

\![Editor de página de destino com personalização Liquid adicionada.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Pré-visualização e teste

Ao visualizar uma landing page no editor, você pode visualizar a página como um usuário aleatório, um usuário existente ou um usuário personalizado.

No entanto, ao visualizar a página de destino na tabela de dados ou na página de **detalhes da página de destino**, você só poderá visualizá-la como um usuário aleatório.

## Considerações sobre personalização

Para manter o desempenho ideal com páginas de destino personalizadas, observe os seguintes limites de tamanho:

- **Salvar uma página de destino:** Se o tamanho for superior a 500 KB, você poderá receber uma mensagem de aviso indicando que a página excedeu nossos limites de tamanho, o que pode impedir sua publicação.
- **Renderização com personalização Liquid:** O tamanho total não deve exceder 1 MB. Caso contrário, a página poderá ser automaticamente despublicada pelo Braze.

### Evite cancelar a publicação de páginas de destino

Se a sua página exceder esses limites de tamanho, você receberá um e-mail informando que ela poderá não ser publicada se continuar excedendo o limite. Quando o limite for atingido, a página será automaticamente despublicada, e você receberá uma notificação.

Para evitar que sua página exceda os limites de tamanho ou tenha tempos de carregamento lentos, certifique-se de usar a personalização do Liquid:

- Não faz loops contínuos ou referências a grandes conjuntos de dados.
- Não depende de lógica matemática ou condicional extensa dentro do bloco Liquid.

## Páginas de reserva

Se os seus usuários tentarem acessar uma página que não foi publicada, eles verão uma mensagem indicando que a página não pode ser carregada no momento. Os motivos pelos quais uma página não foi publicada incluem:

- Líquido complexo ou quebrado, que pode causar longos tempos de renderização
- Problemas de rede do usuário
- Exceder os limites máximos de tamanho da página de destino
