

#My move 1
#Correctness:100%
#Task Score:100%
#Performance: Not assessed
def solution(N):
    N = bin(N);
    if '0' not in N:
        return 0;

    max_zeros = 0;
    string_list = N.split('1');

    list_length = len(string_list);
    
    first = string_list[0];
    last = string_list[list_length - 1];

    if last == '' or N.endswith('0'):
        string_list.pop(list_length - 1);

    if first=='' or first.startswith('0'):
            string_list.pop(0);

    string_set = set(string_list);

    for item in string_set:
        zeros_count = item.count('0');
        max_zeros = zeros_count if max_zeros < zeros_count else max_zeros;
 
    return max_zeros;
    


#mercenary move 1
#Correctness:100%
#Task Score:100%
#Performance: Not assessed
def solution_A(N):
    cnt = 0
    result = 0
    found_one = False
    i = N     
    while i:
        if i & 1 == 1:
            if (found_one == False):
                found_one = True
            else:
                result = max(result,cnt)
            cnt = 0
        else:
            cnt += 1
        i >>= 1
    return result





print(solution(529))
print(solution_A(529))

