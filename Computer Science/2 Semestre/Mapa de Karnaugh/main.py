# OBS: A forma mais rápida de resolver seria com certeza com o dicionário de todas as possíveis formas do mapa usando o valor decimal como chave ou até mesmo o
# binário que usamos como input, mas isso é inviável a medida que crescemos a potência de dois (ex: 2^8 poderia ocupar muitos (MUITOS) Bytes considerando que o cache seguiria 2^n^n)
# mas mesmo que hoje em dia tenhamos poder computacional para processar uma entrada de 32 variáveis a medida que isso cresce seria cada vez mais difícil de alocar tudo em RAM ou
# em SSD's então a forma mais rápida seria, na verdade, o cálculo em si.

class Kmap:
    def __init__(self, variables: list):
        self.var = variables
        self.mintermos_in_order = [int(v) for v in variables]

        self.kmap_vals = [
            self.mintermos_in_order[0],
            self.mintermos_in_order[1],
            self.mintermos_in_order[3],
            self.mintermos_in_order[2]
        ]

    # Pode receber tanto valores booleanos quanto inteiros
    def resolve_for_2(self) -> str:
        mintermos = [int(self.var[0]), int(self.var[1]), int(self.var[2]), int(self.var[3])]

        # Lista para armazenar os termos simplificados (Implicações Primárias)
        termos = []

        # Se todos os valores forem 0 ou 1
        if all(m == 0 for m in mintermos):
            return "0"  # Função sempre falsa

        if all(m == 1 for m in mintermos):
            return "1"  # Função sempre verdadeira (Grupo de 4)

        # Busca por grupos de 2
        if mintermos[0] == 1 and mintermos[1] == 1:
            termos.append("A'")
            mintermos[0] = mintermos[1] = 2  # Marca como coberto

        if mintermos[2] == 1 and mintermos[3] == 1:
            termos.append("A")
            mintermos[2] = mintermos[3] = 2  # Marca como coberto

        if mintermos[0] == 1 and mintermos[2] == 1:
            termos.append("B'")
            mintermos[0] = mintermos[2] = 2  # Marca como coberto

        if mintermos[1] == 1 and mintermos[3] == 1:
            termos.append("B")
            mintermos[1] = mintermos[3] = 2  # Marca como coberto

        # Busca por grupos de 1 (Mintermos restantes, se não foram cobertos)
        # 0: A'B'
        if mintermos[0] == 1:
            termos.append("A'B'")

        # 1: A'B
        if mintermos[1] == 1:
            termos.append("A'B")

        # 2: AB'
        if mintermos[2] == 1:
            termos.append("AB'")

        # 3: AB
        if mintermos[3] == 1:
            termos.append("AB")

        # Retorna a Soma de Produtos
        return " + ".join(termos)

    # Exemplo usando um dicionário para armazenar os valores possíveis
    def resolve_for_2_using_dict(self) -> str:
        # Cache com a solução mais simplificada para cada combinação de mintermos (2^4 = 16)
        DICT_KMAP_2 = {
            0: "0",
            1: "A'B'",
            2: "A'B",
            3: "A'",
            4: "AB'",
            5: "B'",
            6: "A'B + AB'",
            7: "A' + B'",
            8: "AB",
            9: "A'B' + AB",
            10: "B",
            11: "A' + AB",
            12: "A",
            13: "B' + AB",
            14: "A + B",
            15: "1"
        }

        m0, m1, m2, m3 = self.mintermos_in_order
        decimal_key = (m3 * 8) + (m2 * 4) + (m1 * 2) + (m0 * 1)

        return DICT_KMAP_2.get(decimal_key, "Erro na chave")

if __name__ == "__main__":
    def _print_kmap_solution(mintermos_list):
        # Cria a Tabela Verdade
        print("A B | Saída")
        for i in range(2**2):
            A = 1 if i >= 2 else 0
            B = 1 if i % 2 == 1 else 0
            saida = mintermos_list[i]
            print(f"{A} {B} | {saida}")

    # ----------------------------------------------------------------------
    # Exemplo 1: F(A, B) = A' + B  (m0, m1, m3)
    # mintermos: 1 (A'B'), 1 (A'B), 0 (AB'), 1 (AB)
    # Resultado esperado: A' + B
    print("\n--- Exemplo 1: A' + B ---")
    mintermos_1 = [1, 1, 0, 1]
    _print_kmap_solution(mintermos_1)
    print("Resolução (Cálculo): " + Kmap(mintermos_1).resolve_for_2())
    print("Resolução (Dicionário): " + Kmap(mintermos_1).resolve_for_2_using_dict())

    # ----------------------------------------------------------------------
    # Exemplo 2: F(A, B) = B' (m0, m2)
    # mintermos: 1, 0, 1, 0
    # Resultado esperado: B'
    print("\n--- Exemplo 2: B' ---")
    mintermos_2 = [1, 0, 1, 0]
    _print_kmap_solution(mintermos_2)
    print("Resolução (Cálculo): " + Kmap(mintermos_2).resolve_for_2())
    print("Resolução (Dicionário): " + Kmap(mintermos_2).resolve_for_2_using_dict())

    # ----------------------------------------------------------------------
    # Exemplo 3: F(A, B) = A'B (m1)
    # mintermos: 0, 1, 0, 0
    # Resultado esperado: A'B
    print("\n--- Exemplo 3: A'B ---")
    mintermos_3 = [0, 1, 0, 0]
    _print_kmap_solution(mintermos_3)
    print("Resolução (Cálculo): " + Kmap(mintermos_3).resolve_for_2())
    print("Resolução (Dicionário): " + Kmap(mintermos_3).resolve_for_2_using_dict())

    # ----------------------------------------------------------------------
    # Exemplo 4: F(A, B) = 1 (Tudo 1)
    # mintermos: 1, 1, 1, 1
    # Resultado esperado: 1
    print("\n--- Exemplo 4: 1 ---")
    mintermos_4 = [1, 1, 1, 1]
    _print_kmap_solution(mintermos_4)
    print("Resolução (Cálculo): " + Kmap(mintermos_4).resolve_for_2())
    print("Resolução (Dicionário): " + Kmap(mintermos_4).resolve_for_2_using_dict())

    # ----------------------------------------------------------------------
    # Exemplo 5: F(A, B) = 0 (Tudo 0)
    # mintermos: 0, 0, 0, 0
    # Resultado esperado: 0
    print("\n--- Exemplo 5: 0 ---")
    mintermos_5 = [0, 0, 0, 0]
    _print_kmap_solution(mintermos_5)
    print("Resolução (Cálculo): " + Kmap(mintermos_5).resolve_for_2())
    print("Resolução (Dicionário): " + Kmap(mintermos_5).resolve_for_2_using_dict())