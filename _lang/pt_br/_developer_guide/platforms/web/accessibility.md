---
nav_title: Acessibilidade
article_title: Acessibilidade
platform: Web
page_order: 22
page_type: reference
description: "Este artigo descreve como o Braze suporta acessibilidade."

---

# Acessibilidade

> Este artigo fornece uma visão geral de como o Braze suporta acessibilidade dentro da sua integração.

O SDK Web do Braze suporta os padrões fornecidos pelas [Diretrizes de Acessibilidade para Conteúdo da Web (WCAG 2.1)](https://www.w3.org/TR/WCAG21/). Mantemos uma [pontuação de 100/100 no Lighthouse](https://developer.chrome.com/docs/lighthouse/accessibility/scoring) para cartões de conteúdo e mensagens no aplicativo em todas as nossas novas versões para manter nosso padrão de acessibilidade.

## Pré-requisitos

A versão mínima do SDK que atende à WCAG 2.1 é próxima da v3.4.0. No entanto, recomendamos a atualização para pelo menos a v6.0.0 para correções importantes de tags de imagem.

### Correções notáveis de acessibilidade

| versão | Tipo | Principais mudanças |
|---------|------|-------------|
| **6.0.0** | **Importante** | Imagens como `<img>` tags, `imageAltText` ou `language` campos, melhorias gerais de acessibilidade da interface do usuário |
| **3.5.0** | Leve | Melhorias de acessibilidade de texto rolável |
| **3.4.0** | Consertar | Correção de papel `article` para Cartões de Conteúdo |
| **3.2.0** | Leve | Alvos de toque mínimos de 45x45px para botões |
| **3.1.2** | Leve | Texto alternativo padrão para imagens |
| **2.4.1** | **Importante** | HTML semântico (`h1` ou `button`), atributos ARIA, navegação por teclado, gerenciamento de foco |
| **2.0.5** | Leve | Gerenciamento de foco, navegação por teclado, rótulos |
{: .reset-td-br-1, .reset-td-br-2 role="presentation" }

## Recursos de acessibilidade suportados

Suportamos esses recursos para cartões de conteúdo e mensagens no aplicativo:

- Funções e rótulos ARIA
- Suporte à navegação por teclado
- Gerenciamento de foco
- Anúncios para leitores de tela
- Suporte a texto alternativo para imagens

## Diretrizes de acessibilidade para integrações de SDK

Consulte [Construindo mensagens acessíveis no Braze]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/accessibility) para diretrizes gerais de acessibilidade. Este guia fornece dicas e melhores práticas para máxima acessibilidade ao integrar o SDK Web do Braze em sua aplicação web.

### Cartões de conteúdo

#### Definindo uma altura máxima

Para evitar que os Cartões de Conteúdo ocupem muito espaço vertical e melhorar a acessibilidade, você pode definir uma altura máxima no contêiner de feed, como neste exemplo:

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

#### Considerações sobre a área de visualização

Para Cartões de Conteúdo que são exibidos em linha, considere as restrições da área de visualização, como neste exemplo.

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
Não coloque informações importantes dentro de mensagens no aplicativo que deslizam para cima, pois não são acessíveis para leitores de tela.
{% endalert %}

### Considerações para dispositivos móveis

#### Design responsivo

O SDK inclui pontos de interrupção responsivos. Confirme que suas personalizações funcionam em diferentes tamanhos de tela, como neste exemplo:

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

### Testando acessibilidade

#### Lista de verificação de teste manual

Teste manualmente sua acessibilidade completando estas tarefas:

- Navegue pelos Cartões de Conteúdo e mensagens no aplicativo apenas com o teclado (Tab, Enter, Espaço)
- Teste com leitor de tela (NVDA, JAWS, VoiceOver)
- Verifique se todas as imagens têm texto alternativo
- Verifique as proporções de contraste de cores (use ferramentas como o WebAIM Contrast Checker)
- Teste em dispositivos móveis com toque
- Verifique se os indicadores de foco estão visíveis
- Teste a captura de foco de mensagens modais
- Verifique se todos os elementos interativos são acessíveis pelo teclado

### Problemas comuns de acessibilidade

Para evitar problemas comuns de acessibilidade, faça o seguinte:

1. ** Mantenha estilos de foco:** Os indicadores de foco do SDK são essenciais para usuários de teclado.
2. ** Use `display: none` apenas em elementos não interativos:** Use `visibility: hidden` ou `opacity: 0` para ocultar elementos interativos.
3. ** Não substitua atributos ARIA:** O SDK define papéis e rótulos ARIA apropriados.
4. **Use `tabindex` atributos:** Esses controlam a ordem de navegação pelo teclado.
5. **Forneça uma rolagem se você definir `overflow: hidden`:** Confirme que o conteúdo rolável permanece acessível.
6. **Não interfira com os manipuladores de teclado embutidos:** Confirme que a navegação existente pelo teclado funciona.