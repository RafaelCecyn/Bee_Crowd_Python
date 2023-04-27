hi,mi,hf,mf = input().split()
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)



if hf > hi and mf > mi:
    hr = hf - hi
    mn = mf - mi
    print(f"O JOGO DUROU {hr} HORAS (S) E {mn} MINUTO (S)")
elif hf > hi and  mi > mf:
     hr = (hf - hi) -1
     mn = (mf-mi) + 60
     print(f"O JOGO DUROU {hr} HORAS (S) E {mn} MINUTO (S)")
elif hf == hi and mi > mf:
    hr = 23
    mn = (mf-mi) + 60
    print(f"O JOGO DUROU {hr} HORAS (S) E {mn} MINUTO (S)")
elif hf == hi and mf > mi:
    hr = 0
    mn = mf - mi
    print(f"O JOGO DUROU {hr} HORAS (S) E {mn} MINUTO (S)")
elif hf > hi and mf == mi:
    hr = hf - hi
    mn = 0
    print(f"O JOGO DUROU {hr} HORAS (S) E {mn} MINUTO (S)")
elif hi < hf and mf == mi:
    hr = (hf-hi) + 24
    mn = 0
    print(f"O JOGO DUROU {hr} HORAS (S) E {mn} MINUTO (S)")
elif hi > hf and mf > mi:
    hr = (hf-hi) + 24
    mn = mf - mi
    print(f"O JOGO DUROU {hr} HORAS (S) E {mn} MINUTO (S)")
elif hi > hf and mi > mf:
    hr = (hf-hi) + 23
    mn = (mf - mi) + 60
    print(f"O JOGO DUROU {hr} HORAS (S) E {mn} MINUTO (S)")
else:
    print(f"O JOGO DUROU 24 HORAS (S) E 0 MINUTO (S)")
    
    

    
    