# 1. Profil Karaketr
nama_hero = "TRIPLE T"                                                  # String
level = 67                                                              # Interger
health_point = 666.7770                                                  # Float
is_alive = True                                                         # Boolean
list_inventory = ["Mystique Stick", "Lantern", "Throwing Stick"]        # List
hero_atribut = {                                                        # Dictionary
    "Kekuatan" : "676",
    "Kelincahan" : "767"
}

# 2. Menampilkan seluruh  informasi dengan Print()
print("=== YOUR CHARACTER ===")
print("Name         :", nama_hero)
print("Level        :", level)
print("HP           :", health_point)
print("Status Alive :", is_alive)
print("Inventory    :", list_inventory)
print("Atribute     :", hero_atribut)

# 3. Menampilkan tipe masing-masing data variabel dengan type()
print("\n--- Tipe Data Variabel ---")
print("Tipe (nama_hero)           :", type(nama_hero))
print("Tipe (level)               :", type(level))
print("Tipe (health_point)        :", type(health_point))
print("Tipe (is_alive)            :", type(is_alive))
print("Tipe (list_inventory)      :", type(list_inventory))
print("Tipe (hero_atribut)        :", type(hero_atribut))

# 4. Aksi Karakter
list_inventory.append("Ramuan HP")

level = float(level) + 0.5

# 5. Inforamsi Terbaru Karakter
print("\n\n=== YOUR CHARACTER ===")
print("\n+ Level Up")
print("+ New Items (Ramuan HP)")
print("\nName         :", nama_hero)
print("Level        :", level)
print("HP           :", health_point)
print("Status Alive :", is_alive)
print("Inventory    :", list_inventory)
print("Atribute     :", hero_atribut)