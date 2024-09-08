def is_valid_credit_card(card):
    # Step 1: Check if the card contains hyphens and check proper grouping
    if '-' in card:
        parts = card.split('-')
        if len(parts) != 4 or not all(len(part) == 4 for part in parts):
            return "Invalid"
        card = ''.join(parts)  # Remove hyphens for further checking
    
    # Step 2: Check if the length of the card number is exactly 16
    if len(card) != 16:
        return "Invalid"
    
    # Step 3: Check if the card number contains only digits
    for char in card:
        if not char.isdigit():
            return "Invalid"
    
    # Step 4: Check if the card starts with 4, 5, or 6
    if card[0] not in '456':
        return "Invalid"
    
    # Step 5: Check for 4 or more consecutive repeated digits
    for i in range(13):
        if card[i] == card[i+1] == card[i+2] == card[i+3]:
            return "Invalid"
    
    return "Valid"

# Input the number of credit card numbers
n = int(input().strip())

# List to store results for each card
results = []

# Check each credit card number and store the result
for _ in range(n):
    card = input().strip()
    results.append(is_valid_credit_card(card))

# Output all results after all inputs
for result in results:
    print(result)