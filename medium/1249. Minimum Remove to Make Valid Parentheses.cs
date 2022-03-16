/*
variables:
    int balance:
        - positive (+, >0) more '('
        - negative (-, <0) more ')'
        - balanced-ish (0) same amount of '(' and ')'
        - examples:
            1. a(bc(d) -> balance=1, 2 '(', 1 ')'
            2. (a)b(c))aaa)v)d(e)) -> balance=-4, 3 '(', 7 ')'
            3. a)(b(c(d)) -> balance=0, 3 '(', 3 ')'
                3.1 a(b(c(d)) -> balance=1
                3.2 ab(c(d)) -> valid
            TODO:4. (a))(b(c) -> balance=0, 3 '(', 3 ')'
                -> (a)b(c)
                    4.1 (a))b(c)(d)) -> balance=0, 3 '(', 3 ')'
                    4.2 (a))b(c)(d)) -> balance=0, 3 '(', 3 ')'
*/
/*
ex 1:
    details:
        2 '('
        3 ')'
        removed 0 '(' and 1 ')'

ex 4:
    input:
        a(bc))d(
    output:
        a(bc)d
    details:
        2 '('
        2 ')'
        removed 1 '(' and 1 ')'
ex 5:
    input:
        a((b(c)(
    output:
        a(bc)
     or
        ab(c)
    details:
        4 '('
        1 ')'
        removed 3'(' and 0')'
        
case 1 - starting with (
    - 

case 2 - removing starting )
    easy case
*/
public class Solution {
    public string MinRemoveToMakeValid(string s) {
        int balance = 0;
        
        // handling case 2
        for (int i = 0; i < s.Length; i++)
        {
            if (i >= s.Length)
                break;
            
            if (s[i] == '(' || s[i] == ')')
            {
                if (s[i] == '(')
                    break;
                else
                    s = s.Remove(i) + s.Substring(i+1);
            }
        }
        
        // getting balance
        foreach (char c in s)
        {
            if (c == '(') balance += 1;
            if (c == ')') balance -= 1;
        }
        
        // handling the rest of the cases
        int removed = 0;
        int auxBalance = 0;
        if (balance != 0)
        {
            for (int i = 0; i < s.Length; i++)
            {
                // double check
                if (i >= s.Length)
                    break;
                
                // increasing or decreasing balance
                if (s[i] == '(') auxBalance += 1;
                if (s[i] == ')') auxBalance -= 1;

                // removing...
                if ((balance < 0 && auxBalance < 0) || (balance > 0 && auxBalance > 0))
                {
                    s = s.Remove(i) + s.Substring(i+1);
                    removed++;
                    auxBalance = 0;
                }

                if (removed == Math.Abs(balance))
                    break;
            }
        }
        else
        {
            int i = 0;
            bool balanced = true;
            while (i <= s.Length)
            {
                // double check
                if (i >= s.Length)
                    break;

                // increasing or decreasing balance
                if (s[i] == '(') auxBalance += 1;
                if (s[i] == ')') auxBalance -= 1;

                if (balanced && auxBalance < 0)
                {
                    s = s.Remove(i) + s.Substring(i+1);
                    balanced = false;
                    continue;
                }
                else if (!balanced && auxBalance == 0)
                {
                    s = s.Remove(i) + s.Substring(i+1);
                    balanced = true;
                    continue;
                }

                i++;
            }
        }
        
        return s;
    }
}