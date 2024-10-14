# enfliptor

I've encrypted my flag so you'll never get it back again! Mwa-ha-ha-ha!

## Solution

To solve this challenge, load the binary into DNSpy or ILSpy and read the source code.

```cs
internal class Program
{
    private static void Main(string[] args)
    {
        if (args.Length != 2)
        {
            Console.WriteLine("Usage: enfliptor <inputFile> <outputFile>");
            return;
        }
        string inputFile = args[0];
        string outputFile = args[1];
        try
        {
            EnfliptFile(inputFile, outputFile);
            Console.WriteLine("File encrypted successfully.");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error: " + ex.Message);
        }
    }

    private static void EnfliptFile(string inputFile, string outputFile)
    {
        byte[] array = File.ReadAllBytes(inputFile);
        for (int i = 0; i < array.Length; i++)
        {
            array[i] = (byte)(~array[i]);
        }
        File.WriteAllBytes(outputFile, array);
    }
}
```

The source code reveals that encryption is just a not operation or `~` which is trivially reversable. The flag can be recovered by running `.\enfliptor.exe flag.enc flag.txt`

flag:
`gigem{fl1pp1ng_4r0und_dotN3t}`
