using System;

namespace Prime_Numbers
{
    class Prime_Checks
    {
        public void PrimeCheck1(int chk) {
            int i;
            //Console.Write("chk/2 = {0} ", chk / 2 + "\n\r");
            for ( i = 2; i <= chk/2; i++) {
                if (chk%i == 0) { break; }
            }
            
            if (i == chk/2+1)  {
                Console.Write("{0} is a Prime Number",chk);
                }
            else  {
                Console.WriteLine("{0} is not a prime number", chk);
            }
        }
        public void PrimeCheck2(int chk) {
            int i, divisor = 0;
            for (i = 1; i <= chk; i++) {
                if (chk % i == 0) { divisor++; }
            }
            Console.WriteLine("number of divisor(s) = {0}\n\r", divisor);
            if (divisor == 2)  {
            Console.WriteLine("{0} is a Prime Number. ",chk);
            }
            else {
                Console.WriteLine("{0} is not a Prime Number.", chk);
            }
        }
        public void PrimeCheck3(int chk) {
            int loopCounter = 0;
            for (int i = 2; i < chk/2; i++) {
                
                if (chk % i == 0) {
                     Console.WriteLine("{0} is not a Prime Number. ", chk);
                    break;
                }
                else {
                    Console.WriteLine("{0} is a Prme Number.", chk);
                    break;
                }
                
            }
            Console.WriteLine("\n loopCounter = {0}", loopCounter);
        }
    }
}
