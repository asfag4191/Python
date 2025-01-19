colA = int(input("Grunnfarge: "))  
colB = int(input("Målfarge: "))    
ratioB = float(input("Andel målfarge: "))  

colA_R = colA // 1000000            
colA_G = (colA // 1000) % 1000     
colA_B = colA % 1000                

colB_R = colB // 1000000            
colB_G = (colB // 1000) % 1000   
colB_B = colB % 1000                

ratioA = 1 - ratioB

new_R = round(ratioA * colA_R + ratioB * colB_R)
new_G = round(ratioA * colA_G + ratioB * colB_G)
new_B = round(ratioA * colA_B + ratioB * colB_B)

new_color = new_R * 1000000 + new_G * 1000 + new_B

print(new_color)
