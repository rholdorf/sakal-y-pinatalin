#!/usr/bin/env python3
"""Gera um nome em sakal-y-pinatalin a partir de uma semente.  uso: nome.py <semente> [<semente2>]"""
import sys, unicodedata

RAIZES = set("""kan kas kilun kinus kipul kitil kuk kulan kumal kun kurun kusan lamun lanin las
linak lik lis luk lumin lunas makin malan manil maral mil min mirun mukul mulin mun mupak
murak mus namil nalis nanul narak nasul nil nimal nin nukal nul nun pakis palik pan pas pik
pil pin pis puk pusak sakun sal san sil sinak sinik sipul suk sulan sumal sun tak tal tamis
tamun tanis tasin tik til tisak tukas tulak tumal tunal turan tus""".split())
MAPA = {"a":"a","e":"i","i":"i","o":"u","u":"u","y":"i",
        **{c:"p" for c in "bdfvp"}, **{c:"k" for c in "cgkq"}, **{c:"s" for c in "jsxz"},
        **{c:c for c in "lmntr"}, "h":"", "w":""}
DIGITOS = dict(zip("0123456789", "ktpsnmlaiu"))
V, CODA = set("aiu"), set("knls")

def latinizar(semente):
    s = semente.lower().replace("ç", "s")
    saida = ""
    for ch in s:
        base = unicodedata.normalize("NFD", ch)[0]
        if "a" <= base <= "z" or base.isdigit():
            saida += base
        elif not ch.isspace() and unicodedata.category(ch)[0] in "LN":
            saida += ch.encode("utf-8").hex()  # o resto vira hex e reentra
    return saida

def nome(semente):
    s = "".join(DIGITOS.get(c, MAPA.get(c, "")) for c in latinizar(semente))
    # r fora de entre vogais vira l, num passo
    s = "".join("l" if c == "r" and not (0 < i < len(s)-1 and s[i-1] in V and s[i+1] in V) else c
                for i, c in enumerate(s))
    # inserções num passo: a entre consoantes, t entre vogais
    out = ""
    for i, c in enumerate(s):
        if i and (s[i-1] in V) == (c in V):
            out += "t" if c in V else "a"
        out += c
    s = out
    if not s:
        return "sik"
    if s[0] in V: s = "p" + s
    if s[-1] in V: s = s + "n"
    elif s[-1] == "m": s = s[:-1] + "n"
    elif s[-1] not in CODA: s = s[:-1] + "k"
    return s + "sik" if s in RAIZES else s

def cindir(a, b):
    a, b = sorted([a, b], key=lambda w: (sum(c in "aiu" for c in w), w))
    return f"{a}-y-{b}"

if __name__ == "__main__":
    nomes = [nome(x) for x in sys.argv[1:3]]
    print(cindir(*nomes) if len(nomes) == 2 else nomes[0])
