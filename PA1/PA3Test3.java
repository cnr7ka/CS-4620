/**
 * PA3Test3.java
 * 
 * Test the getPixel expression for the PA3 grammar
 *
 * CNR 9/12/2017
 */

import meggy.Meggy;

class PA3Test3 {

    public static void main(String[] id){	
	Meggy.setPixel((byte)1,(byte)2, Meggy.Color.BLUE);
	Meggy.delay (1000);
        if (Meggy.getPixel ((byte)1,(byte)2) == Meggy.Color.BLUE) {
	  Meggy.setPixel ((byte)1, (byte)2, Meggy.Color.GREEN);
        }
        
	Meggy.delay (1000);
        if (Meggy.getPixel ((byte)1,(byte)2) == Meggy.Color.GREEN) {
	  Meggy.setPixel ((byte)1, (byte)2, Meggy.Color.BLUE);
    }
  }
}
