import datapane as dp
import pandas as pd

fichero_csv="/Users/dichaowang/Downloads/DI_U05_A02_02.csv"
df = pd.read_csv(fichero_csv) # Cargamos el fichero CSV en un DataFrame

table = dp.DataTable(df) # Creamos un objeto DataTable con el DataFrame
data_table = dp.DataTable(df) # Creamos un objeto DataTable con los datos del DataFrame

#Informe imprimir
report_imprimir = dp.Report(data_table) # Creamos un informe con la tabla de datos
report_imprimir.save("/Users/dichaowang/Downloads/Imprimir.html", True) # Guardamos el informe en un fichero HTML y lo abrimos en el navegador

#Informe visualizar
report_visulizar = dp.Report(data_table) # Creamos un informe con la tabla de datos
report_visulizar.save("/Users/dichaowang/Downloads/Visualizar.html",True) # Guardamos el informe en un fichero HTML y lo abrimos en el navegador

#Informe completo
report = dp.Report(data_table,table) # Creamos un informe con la tabla de datos
report.save("/Users/dichaowang/Downloads/Completo.html",True) # Guardamos el informe en un fichero HTML y lo abrimos en el navegador


