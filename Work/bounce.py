# bounce.py
height = 100
bounce = 1

while bounce <=10:
    height = (3/5) * height
    print(bounce , round(height,4))
    bounce = bounce + 1

