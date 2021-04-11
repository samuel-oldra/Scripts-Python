def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total


def resultado_final(**kwargs):
    status = 'aprovado(a)' if kwargs['nota'] >= 7 else 'reprovado(a)'
    return f'{kwargs["nome"]} foi {status}'
