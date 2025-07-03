def is_same_reflection(org_str, rot_str):
    temp_str= rot_str + rot_str
    if org_str in temp_str:
        return 1
    else:
        return -1
org_str = input('Enter original word :')
rot_str = input('Enter the right rotated word : ')
result = is_same_reflection(org_str, rot_str)
print(result)