<img align="left" width="40" height="40" src="https://cdn.worldvectorlogo.com/logos/c--4.svg" alt="Leetcode">

# Documentation
Here you'll find how to run C# files (.cs extension), for that, you'll need:
- [.NET SDK](https://dotnet.microsoft.com/en-us/download)

## Running code
Once you meet the requirments in the [src](../src/) folder you'll ned to intialize a C# project with the following command on terminal
```bash
dotnet new console
```

A `Program.cs` and other directories will be generated. Your `Program.cs` should look like:
```cs
var solution = new Solution()/*.MethodToSolveProblem(args[0])*/;
if (solution is string) Console.WriteLine(solution);
else Console.WriteLine(solution.ToString());
```

Notice that the `MethodToSolveProblem` should handle the args transformation to whatever the problem needs to use unit tests. 

Another important point to remark is that once you've resolved a problem the `Solution` class should be renamed to `SolutionX` where X is the number of the problem (this is just a suggestion, you can use whatever nomenclature best suits for you), in order not to have conflicts for methods with the same name. You can achieve that with the following command.
```git
git update-index --assume-unchanged #.\ FileName.cs
```
Where `#` is the number of the problem and `FileName` the name of the problem.