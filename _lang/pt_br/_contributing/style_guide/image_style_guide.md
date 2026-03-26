---
nav_title: Guia de estilo para cópia em imagens
article_title: Guia de estilo para cópia em imagens
description: "Diretrizes para criar e estilizar imagens na Braze Docs."
page_order: 1
noindex: true
---

# Guia de estilo para cópia em imagens

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

## Otimize o posicionamento e o dimensionamento

Sempre que possível, posicione as imagens próximas ao texto relevante e use o markdown de estilização de imagens para redimensionar imagens maiores. Para alguns conteúdos, isso deve ser feito [ancorando o texto ao lado esquerdo ou direito da página]({{site.baseurl}}/home/styling_test_page/#image-test), dependendo da imagem e do espaço disponível.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_do.png %}" alt="Exemplo de posicionamento de imagem otimizado corretamente."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/optimize_placement_dont.png %}" alt="Exemplo de posicionamento de imagem otimizado incorretamente."></td></tr>
</tbody>
</table>
{:/}

## Recorte as imagens

Recorte as seções relevantes de forma ajustada. A menos que seja necessário, não inclua a barra de navegação lateral e, em vez disso, inclua as direções de navegação no artigo. Isso limita o número de imagens que precisam ser alteradas quando ocorrem mudanças na interface.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_1.png %}" alt="Exemplo de uma imagem recortada corretamente."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_1.png %}" alt="Exemplo de uma imagem recortada incorretamente."></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_do_2.png %}" alt="Exemplo de uma imagem recortada corretamente."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/cropping_dont_2.png %}" alt="Exemplo de uma imagem recortada incorretamente."></td></tr>
</tbody>
</table>
{:/}

Como a Braze Docs já adiciona uma borda a cada imagem, omita as bordas em capturas de tela de seções. Estamos buscando um recorte limpo. A borda pode ser mantida se houver componentes que ficam fora ou dentro da borda. Veja as imagens a seguir como exemplos.

**Faça:**
![Exemplo de recorte correto de uma imagem.]({% image_buster /assets/img/contributing/style_guide/cropping_do_3.png %})

**Não faça:**  
![Exemplo de recorte incorreto de uma imagem.]({% image_buster /assets/img/contributing/style_guide/cropping_dont_3.png %})
  
**Faça:**  
![Exemplo de recorte correto de uma imagem.]({% image_buster /assets/img/contributing/style_guide/cropping_do_4.png %})

## Desfoque informações sensíveis

Desfoque qualquer informação pessoal identificável (IPI), como nomes, e-mails e chaves de API.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_do.png %}" alt="Exemplo de desfoque correto."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/censorship_dont.png %}" alt="Exemplo de desfoque incorreto."></td></tr>
</tbody>
</table>
{:/}

## Não incorpore texto importante dentro de imagens

Evite incorporar texto dentro de imagens, pois nem todos os usuários conseguem ler texto em inglês (e as ferramentas de tradução de páginas não traduzem imagens). Esse texto deve ser fornecido no artigo. Forneça texto alternativo para as imagens para garantir a máxima acessibilidade aos usuários.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_do.png %}" alt="Exemplo de imagem sem texto incorporado corretamente."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/embed_text_dont.png %}" alt="Exemplo de texto incorporado incorretamente em uma imagem."></td></tr>
</tbody>
</table>
{:/}

## Não enfatize componentes

Não enfatize componentes das imagens, a menos que seja necessário. Use quadrados azuis (a opção mais acessível) com espessura fina a média para destacar diferentes componentes das imagens. Certifique-se de que as "seções destacadas" não obstruam a interface normal.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Faça</th><th style="width: 50%;">Não faça</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_1.png %}" alt="Exemplo de ênfase correta em componentes de uma imagem."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_1.png %}" alt="Exemplo de ênfase incorreta em componentes de uma imagem."></td></tr>
<tr><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_do_2.png %}" alt="Exemplo de ênfase correta em componentes de uma imagem."></td><td style="width: 50%;"><img src="{% image_buster /assets/img/contributing/style_guide/emphasis_dont_2.png %}" alt="Exemplo de ênfase incorreta em componentes de uma imagem."></td></tr>
</tbody>
</table>
{:/}