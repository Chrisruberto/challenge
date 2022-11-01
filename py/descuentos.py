


''''
 cantidad = float(input ('Ingresa la cantidad: '))
costo_del_articulo = float (input ('Ingresa el valor de costo del articulo: '))
if cantidad <=2:
    descuento=costo_del_articulo*5/100
else:
    descuento=costo_del_articulo*10/100
total_a_pagar=costo_del_articulo-descuento
print ('Valor de descuento: $' + repr (descuento))
print ('Valor de total a pagar: $' + repr (total_a_pagar))


'''''

cantidad = float (input ('Ingrese la cantidad: '))
def invoice(amount, desc1=5, desc2=10):
   
    if  cantidad <=2:
        return   cantidad *  (amount - amount*desc1/100)

    else: return cantidad * (amount - amount*desc2/100)

print(invoice(float (input ('Ingresa el valor de costo del articulo: '))))
