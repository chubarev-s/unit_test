package seminars.third.hw;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;


public class TestHW {

    @Test
    public void evenOddNumber(){
        int n = 8;
        boolean result = mainHW.evenOddNumber(n);
        Assertions.assertTrue(result);
        int k = 13;
        boolean res = mainHW.evenOddNumber(k);
        Assertions.assertFalse(res);
    }

    @Test
    public void numberInInterval(){
        int n = 2;
        boolean result_1 = mainHW.numberInInterval(n);
        Assertions.assertFalse(result_1);
        int k = 50;
        boolean result_2 = mainHW.numberInInterval(k);
        Assertions.assertTrue(result_2);
        int f = 106;
        boolean result_3 = mainHW.numberInInterval(f);
        Assertions.assertFalse(result_3);

    }
    private final MainHW mainHW = new MainHW();
}
