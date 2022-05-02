
annee =int (input(("Entrez année:")))
if annee%4==0 and annee%400==0 and annee !=0 :
    print("Cette année est bissextile")
else :
    print(f"Cette année n'est pas bissextile!")