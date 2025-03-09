segs = int(input("Por favor,entre com o número de segudos que deseja converter: "))

a = segs // 86400
b = segs % 86400 // 3600
c = segs % 3600 // 60
d = segs % 60

print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")
