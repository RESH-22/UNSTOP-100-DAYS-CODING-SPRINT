def user_logic(fat, protein, vitamin):
    fat_set = set(fat)
    protein_set = set(protein)
    vitamin_set = set(vitamin)
    
    # Count elements (keeping duplicates) that are exclusive to their array
    fat_count = sum(1 for val in fat if val not in protein_set and val not in vitamin_set)
    protein_count = sum(1 for val in protein if val not in fat_set and val not in vitamin_set)
    vitamin_count = sum(1 for val in vitamin if val not in fat_set and val not in protein_set)
    
    print(fat_count, protein_count, vitamin_count)

n = int(input())
fat = list(map(int, input().split()))
protein = list(map(int, input().split()))
vitamin = list(map(int, input().split()))
user_logic(fat, protein, vitamin)
