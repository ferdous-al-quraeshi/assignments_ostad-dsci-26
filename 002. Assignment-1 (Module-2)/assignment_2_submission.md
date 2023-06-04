# Assignment-2

> Sum all the odd numbers from 0 to 100 and print it to the screen.

**Code:**

```
sum_of_odds = 0

for n in range(100):
    if n % 2 != 0: # filter odds
        sum += n

print("The sum of odd numbers from 0 to 100 is:", sum_of_odds)

```