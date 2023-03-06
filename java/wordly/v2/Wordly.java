// package java.wordly.v2; need to fix the project structure for proper package imports

import java.awt.*;
import java.awt.event.*;

public class Wordly{

    private Frame mainFrame;
    private Panel gameControlPanel;
    private Panel gameSpacePanel;



    public Wordly(){
        createUI();
    }

    public void createUI(){
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

        final Button startButton = new Button("Start");
        final Button resetButton = new Button("Reset");
        final Button hintButton = new Button("Hint"); // not sure what hint to provide, may replace with "Answer"
        
        gameControlPanel.add(difficulty);
        gameControlPanel.add(startButton);
        gameControlPanel.add(resetButton);
        gameControlPanel.add(hintButton);

        mainFrame.add(gameControlPanel);
        
        mainFrame.setVisible(true);
    }


    public static void main(String args[]){
        System.out.println("hello world");
        Wordly game = new Wordly();
        //game.createUI();
    }
}