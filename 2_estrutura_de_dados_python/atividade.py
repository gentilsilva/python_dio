a = input() 
b = input() 
c = input()

aguia = ["vertebrado", "ave", "carnivoro", "aguia"]
pomba = ["vertebrado", "ave", "onivoro", "pomba"]
homem = ["vertebrado", "mamifero", "onivoro", "homem"]
vaca = ["vertebrado", "mamifero", "herbivoro", "vaca"]
pulga = ["invertebrado", "inseto", "hematofago", "pulta"]
lagarta = ["invertebrado", "inseto", "herbivoro", "lagarta"]
sanguessuga = ["invertebrado", "anelideo", "hematofago", "sanguessuga"]
minhoca = ["invertebrado", "anelideo", "hematofago", "sanguessuga"]

entrada = {a, b, c}

items = [aguia, pomba, homem, vaca, pulga, lagarta, sanguessuga, minhoca]
[print(item[-1]) for item in items if entrada.issubset(set(item))]