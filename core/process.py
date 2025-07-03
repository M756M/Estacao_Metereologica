def apparent_temperature(*, temperatura: float, umidade_rel: float, velocidade_vento: float):
    if(type(temperatura) != float): raise TypeError("'temperatura' must be a float value")
    if(type(umidade_rel) != float): raise TypeError("'umidade_rel' must be a float value")
    if(type(velocidade_vento) != float): raise TypeError("'velocidade_vento' must be a float value")
    
    from math import exp;
    
    T = temperatura;
    MR = umidade_rel;
    W = velocidade_vento;
    
    return T + 0.0201465 * MR * exp(17.27 * T/(237.7 + T)) - 0.70 * W - 4;