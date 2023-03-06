// package java.wordly.v2; need to fix the project structure for proper package imports

import java.awt.*;
import java.awt.event.*;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.concurrent.ThreadLocalRandom;

public class Wordly{

    private Frame mainFrame;
    private Panel gameControlPanel;
    private Panel gameSpacePanel;
    private String difficulty;
    String chosenWord;

    HashMap<String, String[]> words = new HashMap<String, String[]>();



    public Wordly(){
        createUI();
    }

    public void populateWordMap(){
        String[] easyWords = {"dogs", "cats", "hair", "know", "cart", "gave"};
        String[] mediumWords = {"grape", "known", "visor", "flown", "treat", "hands"};
        String[] hardWords = {"grades", "handle", "mentor", "pulses", "soften", "dongle"};
    
        words.put("Easy", easyWords);
        words.put("Medium", mediumWords);
        words.put("Hard", hardWords);
    }

    public String getWord(String difficulty){
        int val = ThreadLocalRandom.current().nextInt(0, words.get(difficulty).length);
        String word = words.get(difficulty)[val];
        System.out.println(word);

        return word;
    }

    public String compareWords(String answerWord, String guessWord){
        List<String> displayArr = new ArrayList<String>();

        String ANSI_RESET = "\u001B[0m";
        //String ANSI_BLACK = "\u001B[0m";
        String ANSI_GREEN = "\u001B[32m";
        String ANSI_YELLOW = "\u001B[33m";
        String ANSI_RED = "\u001B[31m";
        String ANSI_WHITE = "\u001B[37m";

        for(int i=0; i < answerWord.length(); i++){
            char guessWordChar = guessWord.charAt(i);
            char answerWordChar = answerWord.charAt(i);
            if (guessWordChar == answerWordChar){
                displayArr.add(ANSI_GREEN + answerWordChar + ANSI_RESET);
            }else if(answerWord.contains("" + guessWordChar)){
                displayArr.add(ANSI_YELLOW + guessWordChar + ANSI_RESET);
            }else{
                displayArr.add(ANSI_RED + "" + guessWordChar + ANSI_RESET);
            }
        }
        System.out.println(displayArr);
        String out = "";
        for(String s: displayArr){
            out += s;
        }
        System.out.println(out);
        return "tempOut";
        //return out;
        
    }

    public void createUI(){
        //String chosenWord = ""; // bad idea, find a proper way to do this

        mainFrame = new Frame("Wordly Game");
        mainFrame.setSize(400, 400);
        mainFrame.setLayout(new GridLayout(2,1));
        mainFrame.addWindowListener(new WindowAdapter(){
            public void windowClosing(WindowEvent windowEvent){
                System.exit(0);
            }
        });
        // all UI bits should be in here
        // build the game control dropdown and buttons
        gameControlPanel = new Panel();
        final Choice difficulty = new Choice();
        difficulty.add("Easy");
        difficulty.add("Medium");
        difficulty.add("Hard");

        populateWordMap();

        final Button startButton = new Button("Start");
        final Button resetButton = new Button("Reset");
        final Button hintButton = new Button("Hint"); // not sure what hint to provide, may replace with "Answer"
        
        startButton.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                String diff = difficulty.getItem(difficulty.getSelectedIndex());
                chosenWord = getWord(diff);
                System.out.println("Difficulty: " + diff + "\nChosen Word: " + chosenWord);
            }
        });
        gameControlPanel.add(difficulty);
        gameControlPanel.add(startButton);
        gameControlPanel.add(resetButton);
        gameControlPanel.add(hintButton);

        //build "gameplay" area
        gameSpacePanel = new Panel();
        Label userInputLabel = new Label("Enter a Word: ");
        TextField userInput = new TextField(6); //temp value, 

        Button userInputButton = new Button("Submit");
        userInputButton.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e) {
                String guessWord = userInput.getText();
                System.out.println(guessWord);
                String output = compareWords(chosenWord, guessWord);
                Label outputLabel = new Label(output);
                gameSpacePanel.add(outputLabel);
            }
        });

        gameSpacePanel.add(userInputLabel);
        gameSpacePanel.add(userInput);
        gameSpacePanel.add(userInputButton);

        
        // the other text field, the answer comparison field may need to be added during runtime
        
        mainFrame.add(gameControlPanel);
        mainFrame.add(gameSpacePanel);
        mainFrame.setVisible(true);

    }

    public void runGame(){

    }


    public static void main(String args[]){
        System.out.println("hello world");
        Wordly game = new Wordly();
        //game.createUI();
    }
}