// Why use jagged array? 
// Data comes in various shapes and sometimes that shape is 
// uneven with a 2D-array, there's a potential to waste a great
// amount of memory by having a great amount of unsed space. 
// Jagged arrays can be optimized at the intermedicate language level
// and this can be exploited to speed up programs.
// C# natvely knows the differences between jagged and 
// mult-dimensional array. But many other languages don't 
// this means you'll have to create a custom enumerator or 
// implement your own iteration in order to reap the benefits 
// of using a jagged array. 
using System; 

class Program 
{
    static void Main()
    {
        // creating an array that will have only 
        // three rows 
        int[][] jagged = new int[3][]; 

        // Set row 0 
        // Note 1; setting the row 0 to 'new int [2]'
        // means that this row is going to have a new integer
        // array that has two spots inside of it. 
        // It can contain two integers. 
        jagged[0] = new int[2]; 
        // The first integer is at jagged[0][0]??
        jagged[0][0] = 8;
        // The second item in this row is at jagged[0][1]??
        jagged[0][1] = 10; 

        // Set row 1
        jagged[1] = new int[9]; 

        // Set row 2 ??
        jaggeddp[2] = new int[4] { 20, 30, 40, 50}; 

    Console.Writeline("At row, col 0: " + jagged[2][0])
    }    


}