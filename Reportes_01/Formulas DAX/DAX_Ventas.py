# Rentabilidad


CALCULATE(
    SUM('Base de Ventas'[Total Fact])
    -
    SUM(Merge1[Stock - CMV.CMV])
)

# Rentabilidad %


IF(
   SUM('Base de Ventas'[Total Fact])=0, 0, 
   (SUM('Base de Ventas'[Total Fact])-SUM(Merge1[Stock - CMV.CMV]))/SUM(Merge1[Stock - CMV.CMV])
)

# Rentabilidad % 2


IF(
   SUM('Base de Ventas'[Total Fact])=0,
   0,
   DIVIDE(
   SUM('Base de Ventas'[Total Fact])-SUM('Stock - CMV'[CMV]),
   SUM('Stock - CMV'[CMV]))
)

# Rentabilidad 2

CALCULATE(
    SUM('Base de Ventas'[Total Fact])
    -
    SUM('Stock - CMV'[CMV])
)