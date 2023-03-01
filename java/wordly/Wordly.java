import java.util.ArrayList;
import java.util.List;

public class Wordly {
    public static void main(String[] args){
        System.out.println("Hello World");
        game();
    }


    private static void game(){
        System.out.println("Hello?");
        boolean gameWon = false;
        String word = startGame();
        while(gameWon != true){
            String userWord = getInputWord();
            System.out.println("user word: " + userWord);
            gameWon = word.equals(userWord);
            draw(word, userWord);

        }


        // start_game() start the game, set the difficulty level, get the word, return string word
        // getInput() get terminal input string from user, return string
        // draw_compare(word, user_word)
    }

    public static final String ANSI_RESET = "\u001B[0m";
    //public static final String ANSI_BLACK = "\u001B[0m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_WHITE = "\u001B[37m";


    private static void draw(String word, String userWord) {
        //System.out.println(ANSI_RED + "This text is red!" + ANSI_RESET); //test string for coloring

        List<String> displayArr = new ArrayList<String>();
        try{
            for(int i =0; i < word.length(); i++){
                if(word.charAt(i) == userWord.charAt(i)){
                    displayArr.add(ANSI_GREEN + userWord.charAt(i) + ANSI_RESET);
                }else if(word.contains(""+userWord.charAt(i))){
                    displayArr.add(ANSI_YELLOW + userWord.charAt(i) + ANSI_RESET);
                }else{
                    displayArr.add(ANSI_RED + userWord.charAt(i) + ANSI_RESET);
                }
            }
        }catch(java.lang.StringIndexOutOfBoundsException e){
            displayArr.add(ANSI_RED + "*" + ANSI_RESET);
        }

        System.out.println(displayArr);

    }


    private static String getInputWord(){
        System.out.print("> ");
        String userWord = System.console().readLine();
        return userWord;

    }

    private static String startGame(){
        
        return "temp";
    }
}