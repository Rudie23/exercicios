from operator import itemgetter


courses = ['History', 'Math', 'Physics', 'Chemistry']

nums = [1, 5, 2, 4, 3]

courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses)
print(nums)

# if you don't want change the list

sorted_courses = sorted(courses)
print(sorted_courses)

print(courses.index('Math'))


for item in courses:
    print(item, type(item))

for index, course in enumerate(courses, start= 1):
    print(index, course)

course_str = ' - '.join(courses)
print(course_str)

new_list = course_str.split(' - ')
print(new_list)
print('\n')

# Sets

cs_courses = {'History', 'Math', 'Physics', 'Chemistry'}
art_courses = {'History', 'Math', 'Art', 'Geography'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))