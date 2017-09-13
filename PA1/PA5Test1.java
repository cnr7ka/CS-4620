/**
 * PA45est1.java
 * 
 * Test variable declaration and type changes from int to byte
 * for the PA5 grammar
 * 
 *CNR 9/12/2017
 */

import meggy.Meggy;

class PA5Test1 {

    public static void main(String[] id) {
            new Horizontal().Move((byte)0,(byte)4);
        }
}
        
class Horizontal {
    int i;
    public void Move(byte x, byte y) {
	    if (Meggy.getPixel((byte)7,(byte)y) == Meggy.Color.DARK) {
	      Meggy.setPixel((byte)(x), (byte)(y), Meggy.Color.GREEN);
	      i = x + 1;
	      Meggy.delay(100);
	      this.Move((byte)i,(byte)y);
	      

	    }
	}
}

