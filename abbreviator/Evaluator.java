
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

/*
 * Name: Zain Tahir 
 * Student number: C1308094
 */

public class Evaluator extends Shortener {
    // This class is only a starting point. You should complete all members
    // below, but you may also need to add other fields and methods to
    // finish the implementation as per the question on the assignment sheet.
    
    /*
     * Default constructor that will load a default abbreviations text file.
     */
    public Evaluator() throws FileNotFoundException {
        Scanner s = new Scanner(new File("H:\\java\\Assessment3\\abbreviations.txt"));
        ArrayList<String> list = new ArrayList<String>();

        while (s.hasNext()) {
          String line = s.next();
          String[] lineSplit = line.split(","); //split into two tokens
          list.add(lineSplit[0]); //word
          list.add(lineSplit[1]); //abbreveatiion 
   }

    abbreviations = list.toArray(new String[list.size()]);
    s.close();
    }
    
    /*
     * Constructor that will load the abbreviations file represented by the
     * File parameter.
     */
    public Evaluator( File inAbbreviationsFile ) throws FileNotFoundException {
        
        Scanner s = new Scanner(inAbbreviationsFile);
        ArrayList<String> list = new ArrayList<String>();

        while (s.hasNext()) {
          String line = s.next();
          String[] lineSplit = line.split(","); //split into two tokens
          list.add(lineSplit[0]); //word
          list.add(lineSplit[1]); //number
   }

    abbreviations = list.toArray(new String[list.size()]);
    s.close();
    }
    
    /*
     * Constructor that will load the abbreviations file that the String 
     * parameter is a file path for.
     */
    public Evaluator( String inAbbreviationsFilePath ) throws FileNotFoundException {
        Scanner s = new Scanner(new File(inAbbreviationsFilePath));
        ArrayList<String> list = new ArrayList<String>();

        while (s.hasNext()) {
          String line = s.next();
          String[] lineSplit = line.split(","); //split into two tokens
          list.add(lineSplit[0]); //word
          list.add(lineSplit[1]); //number
   }

    abbreviations = list.toArray(new String[list.size()]);
    s.close();
    }
    
    /*
     * Evaluate the message.
     */
    public String evaluateMessage( String inMessage ) {
        //Calculate the length of inMessage
        float length = inMessage.length();
        String beforeAbbreviation = ("Length of input: " + length);
        //Number of Words
        String noOfWords[] = inMessage.split(" ");
        String numberOfWord = ("Number of words: " + noOfWords.length);
        //The abbreviated message
        String a = shortenMessage(inMessage);
        String shortenedMessage = ("Output: " + shortenMessage(inMessage));
        //length of out output
        float lengthA = a.length();
        String lengthOutput = ("Length of output: "+lengthA);
        //Shortened by
        float abbreviated = (((length-lengthA)/length)*100);
        String shortenedBy = ("Shortened by: "+abbreviated+"%");
        
        //Return Everything 
        return beforeAbbreviation + "\n" + numberOfWord + "\n" + shortenedMessage + "\n" + lengthOutput + "\n" + shortenedBy  ;
        
    }
}