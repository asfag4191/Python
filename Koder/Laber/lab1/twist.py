lag_medlemmer=int(input('Hvor mange er dere på laget?\n'))
antall_twist=int(input('Hvor mange twist er det i posen dere vant?\n'))

twist_per_medlem=antall_twist//lag_medlemmer #finner heltallet vi kan dele med, // runder ned
twist_igjen=antall_twist%lag_medlemmer #finner hva som er i rest etter divisjonen

print(f'Det blir {twist_per_medlem} twist til hver, og det blir {twist_igjen} twist til overs.')
