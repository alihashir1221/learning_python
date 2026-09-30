name_list = ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']
print("Original list", name_list) # Original list ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']


name_list.sort(key=lambda name: name.split()[1])
print("Sorted name list", name_list) # Sorted name list ['John Ann', 'Luigi Austin', 'Ben Benson', 'Zen Jack']