---
nav_title: Acessibilidade
article_title: Acessibilidade
platform: Web
page_order: 22
page_type: reference
description: "Este artigo descreve como o Braze oferece suporte à acessibilidade."

---

# Acessibilidade

> Este artigo fornece uma visão geral de como o Braze oferece suporte à acessibilidade em sua integração.

O Braze Web SDK suporta os padrões fornecidos pelas [Diretrizes de Acessibilidade de Conteúdo da Web (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). Mantemos uma [pontuação de farol de 100/100](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) para cartões de conteúdo e mensagens no app em todas as nossas novas construções para manter nosso padrão de acessibilidade.

## Pré-requisitos

A versão mínima do SDK que atende às WCAG 2.1 está próxima da v3.4.0. No entanto, recomendamos fazer upgrade para, pelo menos, a versão 6.0.0 para obter as principais correções de tag de imagem.

### Correções de acessibilidade notáveis

| versão | Tipo | Principais mudanças |
|---------|------|-------------|
| **6.0.0** | **Maior** | Imagens como tags `<img>`, campos `imageAltText` ou `language`, melhorias gerais na acessibilidade da interface do usuário |
| **3.5.0** | Leve | Melhorias na acessibilidade do texto de rolagem |
| **3.4.0** | Consertar | Cartões de conteúdo `article` correção de função |
| **3.2.0** | Leve | Alvos de toque mínimos de 45x45px para botões |
| **3.1.2** | Leve | Texto alternativo padrão para imagens |
| **2.4.1** | **Maior** | HTML semântico (`h1` ou `button`), atribuições ARIA, navegação de teclado, gerenciamento de foco |
| **2.0.5** | Leve | Gerenciamento de foco, navegação pelo teclado, rótulos |
{: .reset-td-br-1, .reset-td-br-2 role="presentation" }

## Recursos de acessibilidade suportados

Oferecemos suporte a esses recursos para cartões de conteúdo e mensagens no app:

- Funções e rótulos ARIA
- Suporte à navegação pelo teclado
- Gerenciamento de foco
- Anúncios de leitores de tela
- Suporte a texto alternativo para imagens

## Diretrizes de acessibilidade para integrações de SDK

Consulte a seção [Criando mensagens acessíveis no Braze]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility) para obter diretrizes gerais de acessibilidade. Este guia fornece dicas e práticas recomendadas para obter o máximo de acessibilidade ao integrar o Braze Web SDK em seu aplicativo da Web.

### Cartões de conteúdo

#### Definição de uma altura máxima

Para evitar que os cartões de conteúdo ocupem muito espaço vertical e melhorar a acessibilidade, você pode definir uma altura máxima no contêiner do feed, como neste exemplo:

{% raw %}
```css
/* Limit the height of the Content Cards feed */
.ab-feed {
  max-height: 600px; /* Adjust to your needs */
  overflow-y: auto;
}

/* For inline feeds (non-sidebar), you may want to limit individual cards */
.ab-card {
  max-height: 400px; /* Optional: limit individual card height */
  overflow: hidden;
}
```
{% endraw %}

#### Considerações sobre a janela de visualização

Para os cartões de conteúdo que são exibidos em linha, considere as restrições de visualização, como neste exemplo.

{% raw %}
```css
/* Limit feed height on mobile to prevent covering too much screen */
@media (max-width: 768px) {
  body > .ab-feed {
    max-height: 80vh; /* Leave space for other content */
  }
}
```
{% endraw %}

### Mensagem no app

{% alert warning %}
Não coloque informações importantes em mensagens no app que deslizam para cima, pois elas não são acessíveis para leitores de tela.
{% endalert %}

### Considerações sobre dispositivos móveis

#### Design responsivo

O SDK inclui pontos de interrupção responsivos. Confirme se suas personalizações funcionam em todos os tamanhos de tela, como neste exemplo:

{% raw %}
```css
/* Mobile-specific accessibility considerations */
@media (max-width: 768px) {
  /* Ensure readable font sizes */
  .ab-feed {
    font-size: 14px; /* Minimum 14px for mobile readability */
  }
  
  /* Ensure sufficient touch targets */
  .ab-card {
    padding: 16px; /* Adequate padding for touch */
  }
}
```
{% endraw %}

### Teste de acessibilidade

#### Lista de verificação de teste manual

Teste manualmente sua acessibilidade realizando estas tarefas:

- Navegue pelos cartões de conteúdo e mensagens no app apenas com o teclado (guia, Enter, espaço)
- Teste com leitor de tela (NVDA, JAWS, VoiceOver)
- Verifique se todas as imagens têm texto alternativo
- Verifique as taxas de contraste das cores (use ferramentas como o WebAIM Contrast Checker)
- Teste em dispositivos móveis com toque
- Verificar se os indicadores de foco estão visíveis
- Teste o envio de mensagens modais com foco
- Verifique se todos os elementos interativos podem ser acessados por um teclado

### Problemas comuns de acessibilidade

Para evitar problemas comuns de acessibilidade, faça o seguinte:

1. **Mantenha os estilos de foco:** Os indicadores de foco do SDK são essenciais para os usuários de teclado.
2. **Use apenas `display: none` em elementos não interativos:** Use `visibility: hidden` ou `opacity: 0` para ocultar elementos interativos.
3. **Não substitua as atribuições ARIA:** O SDK define funções e rótulos ARIA apropriados.
4. **Use as atribuições do site `tabindex`:** Eles controlam a ordem de navegação do teclado.
5. **Forneça uma rolagem se você definir `overflow: hidden`:** Confirme se o conteúdo de rolagem permanece acessível.
6. **Não interfira nos manipuladores de teclado incorporados:** Confirme se a navegação existente no teclado funciona.