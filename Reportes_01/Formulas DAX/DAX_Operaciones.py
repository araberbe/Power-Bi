# Total Real Cant.

CALCULATE (
    SUM ( BaseOps[Cantidad] ),
    BaseOps[Real o Pto.] = "Real"
)


# Var % Cant.

IF( DIVIDE(
    CALCULATE(
        SUM( BaseOps[Cantidad]),
        BaseOps[Real o Pto.] = "Real"
    )
        - CALCULATE (
          SUM ( BaseOps[Cantidad] ),
                BaseOps[Real o Pto.] = "Presupuesto"
          ),
    CALCULATE(
        SUM(BaseOps[Cantidad]),
        BaseOps[Real o Pto.] = "Presupuesto"
    )
)
= BLANK(),
1,
DIVIDE(
    CALCULATE(
        SUM( BaseOps[Cantidad]),
        BaseOps[Real o Pto.] = "Real"
    )
        - CALCULATE (
          SUM ( BaseOps[Cantidad] ),
                BaseOps[Real o Pto.] = "Presupuesto"
          ),
    CALCULATE(
        SUM(BaseOps[Cantidad]),
        BaseOps[Real o Pto.] = "Presupuesto"
    )
)
)


# Total Real USD

CALCULATE (
    SUM ( BaseOps[Monto USD] ),
    BaseOps[Real o Pto.] = "Real"
)

# Var % USD.

IF(DIVIDE (
    CALCULATE (
        SUM ( BaseOps[Monto USD] ),
        BaseOps[Real o Pto.] = "Real"
    )
        - CALCULATE (
            SUM ( BaseOps[Monto USD] ),
            BaseOps[Real o Pto.] = "Presupuesto"
            ),
    CALCULATE (
        SUM ( BaseOps[Monto USD] ),
        BaseOps[Real o Pto.] = "Presupuesto"
    )
)
= BLANK(),
1 ,
DIVIDE(
    CALCULATE (
        SUM ( BaseOps[Monto USD] ),
        BaseOps[Real o Pto.] = "Real"
    )
        - CALCULATE (
            SUM ( BaseOps[Monto USD] ),
            BaseOps[Real o Pto.] = "Presupuesto"
           ),
    CALCULATE (
        SUM ( BaseOps[Monto USD] ),
        BaseOps[Real o Pto.] = "Presupuesto"
    )
)
)

# Total Ppto Cant.

CALCULATE (
    SUM ( BaseOps[Cantidad] ),
    BaseOps[Real o Pto.] = "Presupuesto"
)

# Total Ppto USD.

CALCULATE (
    SUM ( BaseOps[Monto USD] ),
    BaseOps[Real o Pto.] = "Presupuesto"
)

# Target Q Pto.

CALCULATE (
    SUM ( BaseOps[Cantidad] ),
    BaseOps[Real o Pto.] = "Presupuesto" ,
    BaseOps[Mes] < 11
)

# Target USD Pto

CALCULATE (
    SUM ( BaseOps[Monto USD] ),
    BaseOps[Real o Pto.] = "Presupuesto" ,
    BaseOps[Mes] < 11
)

# Var Cant

CALCULATE(
    SUM(BaseOps[Cantidad] ),
    BaseOps[Real o Pto.] = "Real" )
    -
    CALCULATE(
        SUM(BaseOps[Cantidad] ) ,
        BaseOps[Real o Pto.] = "Presupuesto"
    )

# Var USD

CALCULATE(
    SUM(BaseOps[Monto USD] ),
    BaseOps[Real o Pto.] = "Real" )
    -
    CALCULATE(
        SUM(BaseOps[Monto USD] ) ,
        BaseOps[Real o Pto.] = "Presupuesto"
    )

# Costo Serv. Promedio

DIVIDE(
    sum( BaseOps[Monto USD] ),
    sum (BaseOps[Cantidad] )
)