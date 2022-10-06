class BlueFlame:
    def __init__(self, material, key):
        self.material = material
        self.key = key

def First_key_generator(material):
    return 0

def Key_Encryption_Key(First_key):
    return 0

BF = BlueFlame("yuri")
print(BF.key)


Original_Material = ""

F_key = First_key_generator(Original_Material)

KEK = Key_Encryption_Key(F_key)
