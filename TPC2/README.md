# TPC2: Conversor de MD para HTML

**Autor:** João Pastore, A100543

## Requisitos

Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na *"Basic Syntax" *da [Cheat Sheet](https://www.markdownguide.org/cheat-sheet/):

## Descrição do Programa - Funções Utilizadas

### `convertHeading(markdown, level)`

Esta função converte cabeçalhos Markdown em cabeçalhos HTML correspondentes.

### `convertItalic(markdown)`

Esta função converte texto em itálico Markdown em texto em itálico HTML.

### `convertBold(markdown)`

Esta função converte texto em negrito Markdown em texto em negrito HTML.

### `convertBlockquote(markdown)`

Esta função converte citações Markdown em citações de bloco HTML correspondentes.

### `convertLists(markdown)`

Esta função converte listas ordenadas e não ordenadas Markdown em listas HTML correspondentes.

### `convertCode(markdown)`

Esta função converte blocos de código Markdown em blocos de código HTML correspondentes.

### `convertHorizontalRules(markdown)`

Esta função converte horizontal rules (quebra temática entre elementos de nível de parágrafo) Markdown em elementos `<hr>` HTML.

### `convertLinks(markdown)`

Esta função converte links Markdown em links HTML correspondentes.

### `convertImages(markdown)`

Esta função converte imagens Markdown em elementos `<img>` HTML correspondentes.

### `convertMDtoHTML(markdowninput, htmloutput)`

Esta função principal lê um ficheiro Markdown de input, aplica todas as funções de conversão e escreve o HTML resultante num ficheiro de output.

## Exemplo de Uso

```python
convertMDtoHTML('exemplo.md', 'saida.html')
```
