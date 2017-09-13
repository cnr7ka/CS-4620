/**
 * PA5Test3.java
 * 
 * Test the int method declaration for the PA5 grammar
 * 
 *CNR 9/12/2017
 */

import meggy.Meggy;

class PA5Test3 {

    public static void main(String[] id) {
            new cover().horizontal((byte)0,(byte)0);
        }
}
      
class cover {
    public void horizontal(byte x, byte y) {
	    if (Meggy.getPixel((byte)7,(byte)7) == Meggy.Color.DARK) {
	      Meggy.setPixel((byte)(x), (byte)(y), Meggy.Color.GREEN);
	      this.horizontal((byte)(this.incX((byte)x)),(byte)(this.incY((byte)y)));
	      Meggy.delay(100);
	    }
	}
    public int incX(byte a) {
	return (a+1);
	}
	
    public int incY(byte b) {
	return (b+1);
	}
}