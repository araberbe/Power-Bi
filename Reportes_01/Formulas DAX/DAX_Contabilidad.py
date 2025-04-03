# Total Real Monto Usd


CALCULATE(
    SUM(Base[Monto USD]) ,
    Base[TIPO] = "Real"
)

# Total Presto Monto Usd

CALCULATE(
    SUM(Base[Monto USD]) ,
    Base[TIPO] = "Presupuesto"
)


#Variacion USD %

DIVIDE (
    CALCULATE ( SUM ( Base[Monto USD] ), Base[TIPO] = "Real" )
        - CALCULATE ( SUM ( Base[Monto USD] ), Base[TIPO] = "Presupuesto" ),
    CALCULATE ( SUM ( Base[Monto USD] ), Base[TIPO] = "Presupuesto" )
)


# Variacion USD

CALCULATE ( SUM ( Base[Monto USD] ), Base[TIPO] = "Real" )
        - CALCULATE ( SUM ( Base[Monto USD] ), Base[TIPO] = "Presupuesto" )


# ARS

CALCULATE(
    SUM(Base[Monto USD]) ,
    Base[TIPO] = "Real")
*
CALCULATE(
    SUM(Cotizaciones[Cotizacion Dolar]),
    Cotizaciones[Divisa] = "Argentine Peso")


#Rdto Real Operativo diario

DIVIDE(
    CALCULATE(SUM(Base[Monto USD]), Base[TIPO] = "Real") , 
    CALCULATE(SUM(Dias[Días]), Dias[Tipo] = "Real")
)
