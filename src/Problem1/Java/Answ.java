import java.util.ArrayList;

public class Answ {
    private int array[], targ;
    private int holder[] = new int[5];
    public Answ(int array[], int targ ) {
        this.array = array;
        this.targ = targ;
    }

    public boolean answer() {
        boolean check = true;
        ArrayList tempArray = new ArrayList<Integer>();
        int temp;
        for (int i = 0; i < array.length; i++) {
            temp = targ - array[i];
            if (tempArray.contains(temp)) {
                return check;
            }
            tempArray.add(array[i]);
        }
        return !check;
    }

    public static void main(String[] args) {
        Answ prb = new Answ(new int[] {10, 15, 3, 7}, 13);
        System.out.println(prb.answer());
    }
}