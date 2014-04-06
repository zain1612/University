import java.io.*;
import java.util.*;

/*
 * Name: Zain Tahir
 * Student number: C1308094
 */

/*
 * A command-line application that shortens a message.
 */
public class ShortenerUtility {
    public static void main(String[]args) throws FileNotFoundException{
    Shortener sh = new Shortener();
    String finalMessage = sh.shortenMessage(args[0]);
    System.out.println(finalMessage);
    }
    
    
}