#  defenir une fonction get_vowels_numbers(mot)
def get_vowels_numbers(word):
    nb_voyelle = 0
    # créer un compteur voyelles
    for letter in word:
        # pour chaque lettre du mot vous verifiez s'il s'agit d'une voyelle
          if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
              # si c'est le cas, on ajoute 1 au compteur
              nb_voyelle += 1
    return nb_voyelle



word = input("Entrer un mot")
vowels_count = get_vowels_numbers(word)
print("Il y a", vowels_count, "voyelles dans le mot", word)

