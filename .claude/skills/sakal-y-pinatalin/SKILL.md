---
name: sakal-y-pinatalin
description: Cria nomes, títulos, inscrições e frases em sakal-y-pinatalin, a língua inventada por Claude e Grok. Use quando o usuário pedir um nome, título, frase ou tradução "na língua", em sakal-y-pinatalin, ou citar palavras dela (kilun-lanin, pu … ka).
---

# sakal-y-pinatalin

A especificação é a única fonte: `sakal-y-pinatalin.md`, na raiz do repositório desta skill. A raiz é o diretório que contém `sakal-y-pinatalin.md` e `nome.py`. Leia-a inteira antes de produzir qualquer forma. Não invente raiz, partícula ou regra fora dela. O léxico é fechado, e outro falante (Claude ou Grok) precisa chegar à mesma forma que você.

## Procedimento

1. **Classificar o pedido** (seção 6): nome próprio, título (composto nu) ou frase (alvo … modo).
2. **Nome próprio.** Na mesma raiz, rode `python3 nome.py <semente>`, ou `python3 nome.py <semente1> <semente2>` para um nome cindido. Se o usuário não der semente, escolha uma palavra que glose o sentido desejado e diga qual foi. Sem acesso a shell, siga os seis passos da seção 5 à mão.
3. **Título ou conceito.** Siga o procedimento da seção 3 ao pé da letra: primeiro a tabela canônica, depois a divisão das palavras, uma raiz por vaga, anti-repetição e desempate. Não reclassifique vagas por juízo próprio.
4. **Frase.** Preencha a moldura da seção 2 na ordem: ALVO SUJEITO [OBJETO] [OBLÍQUOS] [TEMPO] [ti] VERBO [DONO] MODO. Se o usuário não disser alvo ou modo, escolha e declare a escolha. Ninguém = `hu`; afirmação sem fonte dita = `i`.
5. **Conferir** antes de responder:
   - toda palavra de conteúdo fecha em `k n l s`, com a exceção de um possuidor `ku`/`lu`/`nu`;
   - `r` só entre vogais;
   - o dono aparece se e só se o modo é `u`, `sa` ou `ma`;
   - a pergunta fecha com o alvo repetido e não leva fonte nem dono;
   - no cindido, a parte com menos sílabas vem primeiro.

## Formato da resposta

Para cada item, dê a forma, a leitura com a sílaba tônica em maiúsculas e uma glosa curta palavra a palavra. Se a especificação obrigou a adivinhar, diga onde. Quem quiser pode depois levar o ponto à próxima revisão da língua.

Exemplo:

`kilun-lanin`, ki-LUN la-NIN: torre + comunicação.
