#“Are we there yet?” is a phrase that has existed for as long as there are children, vehicles, and road trips.
#First, ask the user “Are we there yet?” using the input() function and store it in an answer variable.
#Then, use a while loop that asks the user “Are we there yet?” over and over again until they respond with a “Yes”.

print("Keep telling me if we are there yet, to end this type 'yes'")
answer=str(input("Are we there yet?"))
condition=True

while condition:
  if answer == 'yes':
    break
  else:
    answer=str(input("Are we there yet?")).lower()

