from datetime import date, datetime, timedelta, time

TIPO_CARRO: str = "P" # "M", "G"
TEMPO_PEGUENO = 30
TEMPO_MEDIO = 46
TEMPO_GRANDE = 60
data_atual = datetime.now()

if TIPO_CARRO == "P":
    data_estimada: datetime = data_atual + timedelta(minutes=TEMPO_PEGUENO)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif TIPO_CARRO == "M":
    data_estimada: datetime = data_atual + timedelta(minutes=TEMPO_MEDIO)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada: datetime = data_atual + timedelta(minutes=TEMPO_GRANDE)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

print(date.today() - timedelta(days=1))
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())