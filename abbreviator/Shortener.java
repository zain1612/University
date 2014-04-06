
import java.io.*;
import java.util.*;
public class Shortener {
    // This class is only a starting point. You should complete all members
    // below, but you may also need to add other fields and methods to
    // finish the implementation as per the question on the assignment sheet.

    public String[] abbreviations;
    public String word; //Store split word
    public String punctuation; //store punctuation
    public String abbreviatedWord; //store abbreviated word
    public String returnWord; //final return for inWord
    /*
     * Default constructor that will load a default abbreviations text file.
     */
    public Shortener() throws FileNotFoundException {
        Scanner s = new Scanner(new File("abbreviations.txt"));
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
    public Shortener( File inAbbreviationsFile ) throws FileNotFoundException {

        Scanner s = new Scanner("inAbbreviationsFile");
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
    public Shortener( String inAbbreviationsFilePath ) throws FileNotFoundException {

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
    


    public String shortenWord( String inWord ) {
        //Declaring variables to be used to store the word and punctuation

        //Check for punctuation...If found store it in a string variable to be used later
        if (inWord.matches(".*[,?.!;].*")) {
            String parts[] = inWord.split("\\b");
            word = parts[1];
            punctuation = parts[2];

        } else{
            word = inWord;
        }

        // for loop to check if the inputed word is in the abbreavation text file
        for(int i = 0; i < abbreviations.length; i++) {

            if(word.equals(abbreviations[i])) {
                //assign word to the abbreviated word
                abbreviatedWord = abbreviations[i+1]; //The next element in the array is the abbreveation
                break;
            } else {
                abbreviatedWord = word;
            }
        }

            //if loop, if punctuation is not empty combine abbreviatedWord with the punctuation ... else returnWord = abbreviatedWord
        if (punctuation != null && !punctuation.isEmpty()) {
            returnWord = abbreviatedWord + punctuation;
        } else {
            returnWord = abbreviatedWord;
        }
        
        punctuation = "";

        //Return the shortened word with the punctuation character at the end if it exist.
            return returnWord;

    }


    /*
     * Attempts to shorten a message by replacing words with their
     * abbreviations.
     *
     * You may assume that messages are always lower case.
     *
     * Punctuation characters (,?.!;) should be retained after shortening. See
     * `shortenWord( String inWord )` for more information.
     */
    public String shortenMessage( String inMessage ) {
        String wordList[] = inMessage.split(" "); //An array to store the inMessage0
        String outMessage="";
        ArrayList message = new ArrayList<String>();
        for(int i=0; i< wordList.length; ++i){
            outMessage = outMessage + " " + shortenWord(wordList[i] ); //loop throiugh
        }
        outMessage = outMessage.substring(1, outMessage.length());
        return outMessage;
    
}
}

