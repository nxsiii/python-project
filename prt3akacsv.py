import pandas as pd

try: 
    df = pd.read_csv('input.csv')
    lignes1= len(df)

    nettoyage = df.dropna(how='all').drop_duplicates()
    lignes2=len(nettoyage)
    
    supprimés = lignes1 - lignes2

    nettoyage.to_csv('input_propre.csv', index=False)
    
    print("--- BILAN DU NETTOYAGE ---")
    print(f"Lignes au départ : {lignes1}")
    print(f"Lignes supprimées : {lignes2}")
    print(f"Lignes restantes : {supprimés}")
    print("--------------------------")

except Exception as e:
    print(f"Une erreur imprévue est survenue : {e}")