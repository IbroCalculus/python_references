
#Filter creates a collection of elements from an iterable for which a function returns true

#filter(function, iterable)

names_ages = [("Ibrahim", 26),
              ("Salim", 12),
              ("Kal", 19),
              ("Philip", 26),
              ("Muhammad", 54),
              ("Mark", 18),
              ("Shalom", 22),
              ("Qadir", 4)]

filter_key = lambda filter_value: filter_value[1] >= 18 #Sort by index 1, greater than 18

Adults = filter(filter_key, names_ages)
#print(list(filtered_values))
print('===== ADULTS =========')
for i in Adults:
    print(i)