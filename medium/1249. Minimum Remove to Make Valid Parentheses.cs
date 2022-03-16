public class Solution
{
    public string MinRemoveToMakeValid(string s)
    {
        int open = 0;
        string aux = "";
        string result = "";
        
        // handling ')' cases, ex.: a)b(c) -> ab(c)
        foreach (char c in s)
        {
            if (c == '(')
                open++;
            else if (c == ')')
            {
                if (open == 0) continue;
                open--;
            }

            aux += c;
        }

        // handling '(' cases
        for (int i = aux.Length-1; i >= 0; i--)
        {
            if (aux[i] == '(' && open-- > 0) continue;
            result += aux[i];
        }

        return new string(result.Reverse().ToArray());
    }
}