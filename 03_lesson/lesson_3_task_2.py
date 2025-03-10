from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "AS12A", "+79256067847"),
    Smartphone("Lenovo", "YT12451M", "+79545625874"),
    Smartphone("Nokia", "12457A", "+79852144578"),
    Smartphone("Motorola", "54781", "+7987451245"),
    Smartphone("Honor", "8lite", "+79852514563")
]

for smartphone in catalog:
    print(f"{smartphone.brand}, {smartphone.model}, {smartphone.number}")