/**
 * PA5Test2.java
 * 
 * Test assignment statements for the PA5 grammer
 * 
 *CNR 9/12/2017
 */

import meggy.Meggy;

class PA5Test2 {

    public static void main(String[] id) {
            new cover().horizontal((byte)0,(byte)0);
            new cover().horizontal((byte)0,(byte)1);
            new cover().horizontal((byte)0,(byte)2);
            new cover().horizontal((byte)0,(byte)3);
            new cover().horizontal((byte)0,(byte)4);
            new cover().horizontal((byte)0,(byte)5);
            new cover().horizontal((byte)0,(byte)6);
            new cover().horizontal((byte)0,(byte)7);
        }
}
      
class cover {
    int a;
    public void horizontal(byte x, byte y) {
    a = 0;
	    if (Meggy.getPixel((byte)7,(byte)y) == Meggy.Color.DARK) {
	      Meggy.setPixel((byte)(x), (byte)(y), Meggy.Color.GREEN);
	      a = x + 1;
	      Meggy.delay(100);
	      this.horizontal((byte)(a),(byte)(y));
	    }
	}

}