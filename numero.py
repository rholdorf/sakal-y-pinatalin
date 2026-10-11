#!/usr/bin/env python3
"""Numerologia pitagórica de formas em sakal-y-pinatalin.  regras em numerologia.md

uso:
  numero.py <forma>                                   detalha uma forma
  numero.py --alvo N <forma>                          confere uma forma pronta
  numero.py --alvo N --sementes <s> [<s2>]            nome próprio, simples ou cindido, com afinação
  numero.py --alvo N --miolo "<sujeito … verbo>" --modos <m>[,<m>…] [--alvos <a>[,<a>…]]
  numero.py --alvo N --miolo "<sujeito … verbo>" --pergunta [--alvos <a>[,<a>…]]
opções: --eixo expressao|alma|personalidade (padrão expressao)
"""
import os, re, sys
from nome import nome, cindir

VALOR = {"a": 1, "i": 9, "u": 3, "y": 7, "h": 8, "p": 7, "t": 2,
         "k": 2, "m": 4, "n": 5, "l": 3, "r": 9, "s": 1}
VOGAIS = set("aiuy")
MESTRES = (11, 22, 33)
EIXOS = ("expressao", "alma", "personalidade")
ALVOS = ["pu", "mu", "hu", "su"]
ALVOS_PERGUNTA = ["pu", "mu", "su"]
MODOS = {"i", "u", "ka", "la", "na", "ta", "sa", "ma"}
AFINACAO = 99

def ler_sentidos():
    """Os significados vêm da tabela da seção 4 de numerologia.md: uma fonte só."""
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "numerologia.md"), encoding="utf-8") as f:
        return {int(m[1]): m[2].strip() for m in re.finditer(r"^\| (\d+) \| ([^|]+) \|", f.read(), re.M)}

SENTIDO = ler_sentidos()

def reduzir(n):
    """Devolve a cadeia de redução: [57, 12, 3]. Para em 1–9 ou num número mestre."""
    cadeia = [n]
    while n > 9 and n not in MESTRES:
        n = sum(map(int, str(n)))
        cadeia.append(n)
    return cadeia

def somas(texto):
    letras = [c for c in texto if c in VALOR]
    alma = sum(VALOR[c] for c in letras if c in VOGAIS)
    pers = sum(VALOR[c] for c in letras if c not in VOGAIS)
    return {"expressao": alma + pers, "alma": alma, "personalidade": pers}

def numero(forma, eixo="expressao"):
    return reduzir(somas(forma)[eixo])[-1]

def pecas(forma):
    """Separa a forma em domínios (raiz, nome simples), engrenagem e solda y."""
    for palavra in forma.split():
        for parte in palavra.split("-"):
            if parte == "y":
                yield "solda", parte
            elif parte[-1] in VOGAIS:
                yield "engrenagem", parte
            else:
                yield "domínio", parte

def validar(forma):
    estranhas = sorted({c for c in forma if c not in VALOR and c not in " -"})
    if not forma.strip() or estranhas:
        sys.exit(f"não é forma da língua: {forma!r}" + (f" (letras {''.join(estranhas)})" if estranhas else ""))

def cadeia_txt(n):
    return " → ".join(map(str, reduzir(n))) if n else "0, sem número"

def detalhar(forma, eixo="expressao"):
    print(forma)
    for tipo, parte in pecas(forma):
        letras = [c for c in parte if eixo == "expressao" or (c in VOGAIS) == (eixo == "alma")]
        conta = "+".join(str(VALOR[c]) for c in letras) or "—"
        print(f"  {parte:<12} {tipo:<10} {conta} = {cadeia_txt(somas(parte)[eixo])}")
    for e, s in somas(forma).items():
        sentido = SENTIDO[reduzir(s)[-1]] if s else ""
        print(f"  {e:<14} {cadeia_txt(s):<14} {sentido}")

def lista(valor, permitidos, chave):
    itens = valor.split(",")
    if not all(i in permitidos for i in itens):
        sys.exit(f"{chave} aceita só {', '.join(sorted(permitidos))}: {valor}")
    return itens

def candidatos_nome(sementes):
    """Primeiro as sementes dadas; depois a primeira semente seguida de 1 … 99, soldada de novo."""
    for k in [""] + [str(k) for k in range(1, AFINACAO + 1)]:
        usadas = [sementes[0] + k] + sementes[1:]
        nomes = [nome(s) for s in usadas]
        yield " + ".join(usadas), cindir(*nomes) if len(nomes) == 2 else nomes[0]

def opcao(args, chave, padrao=None):
    if chave in args:
        i = args.index(chave)
        if i + 1 >= len(args):
            sys.exit(f"falta valor para {chave}")
        valor = args[i + 1]
        del args[i:i + 2]
        return valor
    return padrao

def falhar(alvo, forma, eixo, nota=""):
    print(f"o alvo {alvo} não é alcançável aqui; {forma}{nota} dá {cadeia_txt(somas(forma)[eixo])}")
    sys.exit(1)

def main(args):
    pergunta = "--pergunta" in args
    if pergunta:
        args.remove("--pergunta")
    eixo = opcao(args, "--eixo", "expressao")
    if eixo not in EIXOS:
        sys.exit(f"eixo desconhecido: {eixo}")
    alvo = opcao(args, "--alvo")
    miolo = opcao(args, "--miolo")
    alvos = opcao(args, "--alvos")
    modos = opcao(args, "--modos")

    if alvo is None:
        if len(args) != 1:
            sys.exit(__doc__)
        validar(args[0].lower())
        return detalhar(args[0].lower(), eixo)
    alvo = int(alvo)
    if alvo not in SENTIDO:
        sys.exit(f"alvo deve ser 1–9, 11, 22 ou 33: {alvo}")
    print(f"alvo {alvo} ({SENTIDO[alvo]}), eixo {eixo}")

    if args and args[0] == "--sementes":
        sementes = args[1:]
        if not 1 <= len(sementes) <= 2:
            sys.exit("--sementes leva uma semente, ou duas para um nome cindido")
        for usadas, forma in candidatos_nome(sementes):
            if numero(forma, eixo) == alvo:
                print(f"{forma}  (semente {usadas})")
                return detalhar(forma, eixo)
        _, base = next(candidatos_nome(sementes))
        falhar(alvo, base, eixo, f" (semente {' + '.join(sementes)})")

    if miolo is not None:
        miolo = miolo.lower()
        validar(miolo)
        if pergunta:
            alvos = lista(alvos, ALVOS_PERGUNTA, "--alvos na pergunta") if alvos else ALVOS_PERGUNTA
            formas = [f"{a} {miolo} {a}" for a in alvos]
        else:
            if not modos:
                sys.exit("--modos é obrigatório fora da pergunta: o modo dito, ou ka,la,na se o pedido endossou sem fonte")
            alvos = lista(alvos, ALVOS, "--alvos") if alvos else ALVOS
            if modos != "ka,la,na" and modos not in MODOS:
                sys.exit(f"--modos leva um modo só, ou exatamente ka,la,na para um endosso sem fonte: {modos}")
            formas = [f"{a} {miolo} {m}" for a in alvos for m in modos.split(",")]
        for forma in formas:
            if numero(forma, eixo) == alvo:
                return detalhar(forma, eixo)
        falhar(alvo, formas[0], eixo)

    if len(args) != 1:
        sys.exit("--alvo sem --sementes nem --miolo confere uma forma só")
    forma = args[0].lower()
    validar(forma)
    if numero(forma, eixo) != alvo:
        falhar(alvo, forma, eixo)
    detalhar(forma, eixo)

if __name__ == "__main__":
    main(sys.argv[1:])
