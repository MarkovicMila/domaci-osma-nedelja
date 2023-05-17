import psycopg2 as pg
import openpyxl as op
import pandas as pd

class Artikli:
    def __init__(self):
        pass
    def export_excel_all(self):
        try:
            con=pg.connect(
                database='artikli',
                port='5432',
                host='localhost',
                user='postgres',
                password='itoip'
            )
            df=pd.read_sql('SELECT * FROM ARTIKLI',con=con)
            df.to_excel('Excel_all.xlsx', index=False)
        except(Exception,pg.Error) as e:
            print('Error: ',e)
        finally:
            con.close()
    def export_excel_naziv(self,naziv):
        try:
            con=pg.connect(
                database='artikli',
                port='5432',
                host='localhost',
                user='postgres',
                password='itoip'
            )
            df=pd.read_sql('''SELECT * FROM ARTIKLI WHERE NAZIV='{}' '''.format(naziv),con=con)
            df.to_excel('Excel_naziv.xlsx', index=False)
        except(Exception,pg.Error) as e:
            print('Error: ',e)
        finally:
            con.close()
    def export_csv_all(self):
        try:
            con=pg.connect(
                database='artikli',
                port='5432',
                host='localhost',
                user='postgres',
                password='itoip'
            )
            df=pd.read_sql('SELECT * FROM ARTIKLI',con=con)
            df.to_csv('CSV_all.csv', index=False)
        except(Exception,pg.Error) as e:
            print('Error: ',e)
        finally:
            con.close()
    def export_csv_naziv(self,naziv):
        try:
            con=pg.connect(
                database='artikli',
                port='5432',
                host='localhost',
                user='postgres',
                password='itoip'
            )
            df=pd.read_sql('''SELECT * FROM ARTIKLI''',con=con)
            pom=df.loc[df['naziv'] == naziv]
            print(pom)
            pom.to_csv('CSV_naziv.csv', index=False)
        except(Exception,pg.Error) as e:
            print('Error: ',e)
        finally:
            con.close()

a=Artikli()
a.export_csv_naziv('Lasko pivo')