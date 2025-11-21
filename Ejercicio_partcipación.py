def DUI_validacion():
   DUI = input("Digite su número de DUI: ")
   condiciones_cumplidas = 0
   if len(DUI) == 10:
       condiciones_cumplidas = condiciones_cumplidas + 1
   if DUI.count('-') == 1:
       condiciones_cumplidas = condiciones_cumplidas + 1
   if DUI[9] == 1:
       condiciones_cumplidas = condiciones_cumplidas + 1
print(f"Cumple {condiciones_cumplidas} condiciones")
DUI_validacion()
