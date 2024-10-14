using System;
using System.IO;
using System.Linq;
using System.Text;

namespace Enfliptor
{
    class Program
    {
        static void Main(string[] args)
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
                Console.WriteLine($"Error: {ex.Message}");
            }
        }

        static void EnfliptFile(string inputFile, string outputFile)
        {
            byte[] fileBytes = File.ReadAllBytes(inputFile);
            for (int i = 0; i < fileBytes.Length; i++)
            {
                fileBytes[i] = (byte)~fileBytes[i]; 
            }
            File.WriteAllBytes(outputFile, fileBytes);
        }
    }
}