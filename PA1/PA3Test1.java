/**
 * PA3Test1.java
 * 
 * Test the if and else statement for the PA3 grammar as well as booleans
 *
 * CNR 9/12/2017
 */

import meggy.Meggy;

class PA3Test1 {

    public static void main(String[] id){
    Meggy.delay(10000);
        if (Meggy.checkButton(Meggy.Button.Left) == true) {
            Meggy.setPixel((byte)0, (byte)4, Meggy.Color.GREEN );}
            else {Meggy.setPixel((byte)0, (byte)4, Meggy.Color.BLUE);}
    }
}
