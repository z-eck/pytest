def portaria(idade, tipo_convite, codigo):
    
    if idade <= 17:
        return "Negado."
        
    tipo_convite = tipo_convite.lower()

    if tipo_convite != "comum" and tipo_convite != "premium" and tipo_convite != "luxo":
        return "Negado."
        
    if codigo != "":
        codigo.lower()
        if tipo_convite == "comum" and codigo.startswith("xt"):
            return "Bem-vindo!"
        elif (tipo_convite == "premium" or tipo_convite == "luxo") and codigo.startswith("xl"):
            return "Bem-vindo!"
        else:
            return "Negado."
        
    return "Negado."