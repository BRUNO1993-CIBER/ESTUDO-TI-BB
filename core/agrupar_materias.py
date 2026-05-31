from .ciclo_estudo import STUDY_CYCLE

def agrupar_materias_por_bloco():
    blocos = {}
    
    for materia in STUDY_CYCLE:
        prefixo = None
        
        if "[BANCO DE DADOS]" in materia:
            prefixo = "BD"
        elif "[ENGENHARIA DE SOFTWARE" in materia:   
            prefixo = "ES"
        elif "[REQUISITOS]" in materia:
            prefixo = "REQ"
        elif "[ARQUITETURA]" in materia:
            prefixo = "ARQ"
        elif "[LINGUAGENS]" in materia:
            prefixo = "LANG"
        elif "[QUALIDADE E ESTRUTURAS DE DADOS]" in materia:
            prefixo = "QUAL"
        elif "[SEGURANÇA DA INFORMACAO]" in materia:
            prefixo = "SEG"
        elif "[CLOUD]" in materia:
            prefixo = "CLOUD"
        elif "[PRODUTIVIDADE E DADOS]" in materia:
            prefixo = "PROD"
        elif "[INFRAESTRUTURA]" in materia:
            prefixo = "INFRA"
        elif "[GOVERNANÇA]" in materia:
            prefixo = "GOV"
        
        if prefixo:
            if prefixo not in blocos:
                blocos[prefixo] = []
            blocos[prefixo].append(materia)
    
    return blocos