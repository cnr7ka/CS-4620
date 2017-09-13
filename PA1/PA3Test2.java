/**
 * PA3Test2.java
 * 
 * Tesdting the while statement of the PA3 grammar
 *
 * CNR 9/12/2017
 */

import meggy.Meggy;

class PA3Test2 {

    public static void main(String[] id){
        while (Meggy.checkButton(Meggy.Button.A)) {
            Meggy.setPixel((byte)4, (byte)3, Meggy.Color.BLUE );
        }

    }
}
