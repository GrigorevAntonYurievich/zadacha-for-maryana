def main():
    n = int(input())
    
    all_languages = set()
    any_languages = set()
    
    
    first_student_languages = set(input().split()[1:])
    
    
    all_languages.update(first_student_languages)
    any_languages.update(first_student_languages)
    
    
    for _ in range(1, n):
        student_languages = set(input().split()[1:])
        all_languages.intersection_update(student_languages)  
        any_languages.update(student_languages) 
    
    print(len(all_languages))
    for lang in sorted(all_languages):
        print(lang)
    print(len(any_languages))
    for lang in sorted(any_languages):
        print(lang)

if __name__ == "__main__":
    main()
