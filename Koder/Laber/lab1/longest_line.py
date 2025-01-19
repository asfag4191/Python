navn=str(input("Hva er ditt navn?\n"))
adresse=str(input("Hva er din adresse?\n"))
post=str(input("Hva er ditt postnummer og poststed?\n"))

lengde_navn=len(navn)
lengde_gateadresse=len(adresse)
lengde_post=len(post)

print(max(lengde_gateadresse,lengde_navn,lengde_post))

#print(f'Antall tegn i den lengste setningen er: {max(lengde_gateadresse,lengde_navn,lengde_post)}')